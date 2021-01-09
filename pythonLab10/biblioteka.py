import json

class LibPosition:

    def __init__(self, title, author, year, id_):
        
        self.title = title
        self.author = author
        self.year = year
        self.id = id_
        self.is_available = True

    @classmethod
    def initFromDict(cls, dct):

        position = cls(dct["title"], dct["author"], dct["year"], dct["id"])
        position.is_available = dct["is_available"]
        return position

    def printOut(self):
        print("id: ", self.id, self.title, self.author, self.year)
    
    def getDictRepr(self):
        
        repr_dict = dict()
        repr_dict["title"] = self.title
        repr_dict["author"] = self.author
        repr_dict["year"] = self.year
        repr_dict["id"] = self.id
        repr_dict["is_available"] = self.is_available

        return repr_dict



class LibUser:

    def __init__(self, name, role):

        self.name = name
        self.role = role

    @classmethod
    def initFromDict(cls, dct):
        return cls(dct["name"], dct["role"])

    def getDictRepr(self):
        
        repr_dict = dict()
        repr_dict["name"] = self.name
        repr_dict["role"] = self.role

        return repr_dict

class LibRegistry:

    def __loadPositionsFromFile(self):
        
        jsoned_positions = ""
        with open(self.positions_file, "r") as f:
            jsoned_positions = f.read()
        
        dicted_positions = json.loads(jsoned_positions)
        
        self.positions = []
        for dicted in dicted_positions:
            self.positions.append(LibPosition.initFromDict(dicted))

    def __loadUsersFromFile(self):
        
        jsoned_users = ""
        with open(self.users_file, "r") as f:
            jsoned_users = f.read()
        
        dicted_users = json.loads(jsoned_users)
        
        self.users = []
        for dicted in dicted_users:
            self.users.append(LibUser.initFromDict(dicted))

    def saveSessionState(self):
        
        dicted_positions = []
        dicted_users = []

        for position in self.positions:
            dicted_positions.append(position.getDictRepr())
        
        for user in self.users:
            dicted_users.append(user.getDictRepr())
        
        jsoned_positions = json.dumps(dicted_positions)
        with open(self.positions_file, "w") as f:
            f.write(jsoned_positions)

        jsoned_users = json.dumps(dicted_users)
        with open(self.users_file, "w") as f:
            f.write(jsoned_users)

    def authoriseUser(self, name):

        for user in self.users:
            if user.name == name:
                return True, user.role
        
        return False, None
    
    def addReader(self, name):

        for user in self.users:
            if user.name == name:
                return False
        
        self.users.append(LibUser(name, "reader"))
        return True
    
    def getAllPositions(self):
        return self.positions
    
    def getAvailablePositions(self):

        available_positions = []
        for position in self.positions:
            if position.is_available:
                available_positions.append(position)
        
        return available_positions
    
    def getUnavailablePositions(self):

        unavailable_positions = []
        for position in self.positions:
            if position.is_available == False:
                unavailable_positions.append(position)
        
        return unavailable_positions
    
    def getPositionsMatchingString(self, match_str):

        matching_positions = []
        for position in self.positions:
            if match_str in position.title:
                matching_positions.append(position)
            
        return matching_positions
    
    def borrowPositionWithId(self, id):

        for i in range(len(self.positions)):
            if self.positions[i].id == id:
                if self.positions[i].is_available == True:
                    self.positions[i].is_available = False
                    return True
        
        return False
        
    def returnPositionWithId(self, id):

        for i in range(len(self.positions)):
            if self.positions[i].id == id:
                if self.positions[i].is_available == False:
                    self.positions[i].is_available = True
                    return True
        
        return False

    def removePositionWithId(self, id_):
        
        for i in range(len(self.positions)):
            if self.positions[i].id == id_:
                del self.positions[i]
                return True

        return False

    def addPosition(self, title, author, year, id_):

        new_position = LibPosition(title, author, year, id_)
        
        for position in self.positions:
            if position.id == id_:
                return False

        self.positions.append(new_position)
        return True

    def __init__(self, positions_file, users_file):

        self.users_file = users_file
        self.positions_file = positions_file
        self.__loadPositionsFromFile()
        self.__loadUsersFromFile()
        


def presentAvailableBooks(register):

    available_books = register.getAvailablePositions()

    print("wybierz id pozycji ktora chcesz wypozyczyc")

    for book in available_books:
        book.printOut()
    
    choice = input()
    success = register.borrowPositionWithId(choice)
    
    if success:
        print("ksiazka poprawnie wypozyczona")
    
    else:
        print("wprowadzono bledne id")



def presentSearchResults(register, phrase):

    searched_books = register.getPositionsMatchingString(phrase)
    
    if searched_books == []:
        print("nie znaleziono ksiazek z podana fraza w tytule")
        return
    
    print("wybierz id pozycji ktora chcesz wypozyczyc")

    for book in searched_books:
        book.printOut()
    
    choice = input()
    success = register.borrowPositionWithId(choice)
    
    if success:
        print("ksiazka poprawnie wypozyczona")
    
    else:
        print("wprowadzono bledne id")


def presentSearchMenu(register):

    phrase = input("wprowadz szukana fraze: ")
    presentSearchResults(register, phrase)



def presentReaderMenu(register):
    
    while True:
        
        print("""
WBIERZ CO CHCESZ ZROBIC:
1 Wyswietl dostepne ksiazki
2 Znajdz ksiazke po tytule
3 Zapisz i wyloguj
                """)
        
        choice = input()

        if choice == "1":
            presentAvailableBooks(register)
        
        elif choice == "2":
            presentSearchMenu(register)
        
        elif choice == "3":
            register.saveSessionState()
            break

        else:
            print("niepoprawny wybor... sprobuj jeszcze raz")

    print("wylogowano...")


def presentReturnMenu(register):

    unavailable_books = register.getUnavailablePositions()
    
    if unavailable_books == []:
        
        print("brak wypozyczonych ksiazek")
        return
    
    print("wybierz id pozycji ktorej zwrot chcesz zatwierdzic")

    for book in unavailable_books:
        book.printOut()
    
    choice = input()

    success = register.returnPositionWithId(choice)
    if success:
        print("pozycja zwrocona")
    
    else:
        print("bledne id")



def presentAddBookMenu(register):

    title = input("title: ")
    author = input("author: ")
    print(title, author)

    try:
        year = int(input("year: "))
    
    except ValueError:

        print("rok musi byc liczba calkowita")
        return
    
    id_ = input("id: ")

    success = register.addPosition(title, author, year, id_)

    if success:
        print("pozycja dodana")
    
    else:
        print("nie udalo sie dodac pozycji (kolizja id)")
    

def presentRemoveBookMenu(register):

    all_books = register.getAllPositions()

    print("pozycje w bibliotece:")

    for book in all_books:
        book.printOut()
    
    id_ = input("wprowadz id ksiazki do usuniecia: ")

    success = register.removePositionWithId(id_)

    if success:
        print("pomyslnie usunieto pozycje")

    else:
        print("nie udalo sie usunac pozycji (bledne id)")
    

def presentAddReaderMenu(register):

    name = input("wprowadz nazwe czytelnika: ")
    
    if name == "":
        
        print("nazwa nie moze byc pusta")
        return
    
    success = register.addReader(name)

    if success:
        print("pomyslnie dodano czytelnika")
    
    else:
        print("nie udalo sie dodac czytelnika")
    


def presentModMenu(register):
    
    while True:
        
        print("""
WBIERZ CO CHCESZ ZROBIC:
1 Przyjmij zwrot ksiazki
2 Dodaj ksiazke
3 Usun ksiazke
4 Dodaj czytelnika
5 Zapisz i wyloguj
                """)
        
        choice = input()

        if choice == "1":
            presentReturnMenu(register)
        
        elif choice == "2":
            presentAddBookMenu(register)
        
        elif choice == "3":
            presentRemoveBookMenu(register)
        
        elif choice == "4":
            presentAddReaderMenu(register)
        
        elif choice == "5":

            register.saveSessionState()
            break
        
        else:
            print("niepoprawny wybor... sprobuj jeszcze raz")

    print("wylogowano...")



def main():

    while True:

        registry = LibRegistry("positions.json", "users.json")
        nick = input("podaj swoj nick lub wpisz 'q' zeby wyjsc: ")

        if nick == 'q':

            print("do zobaczenia")
            break

        user_exists, role = registry.authoriseUser(nick)

        if user_exists:
            
            if role == "reader":
                presentReaderMenu(registry)

            elif role == "mod":
                presentModMenu(registry)
            
            else:
                print("blad w bazie danych")
        
        else:
            print("nie odnaleziono nicku, sprobuj jeszcze raz")



if __name__ == "__main__":
    main()