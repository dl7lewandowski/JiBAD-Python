class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'


class Panel:

    COLORS = ('black', 'white', 'red', 'green', 'blue', 'cyan', 'magenta', 'yellow')

    def __init__(self, size):
        self.size = float(size)
        self.center = Vector(0, 0)
        self.border_color = 'black'
        self.background_color = 'black'

    def __str__(self):
        return f'center: ({self.center}), size: {self.size}, border color: {self.border_color},' \
               f' background color: {self.background_color}'

    def move(self, x, y):
        self.center += Vector(x, y)

    def scale(self, ratio):
        if ratio[0] == 0:
            raise ValueError('Ratio must be different then zero')
        self.size *= float(ratio[0])

    def rotate(self, angle):
        pass

    def set_border_color(self, color):
        if color[0] in Panel.COLORS:
            self.border_color = color
        else:
            raise ValueError('Available colors: black, white, red, green, blue, cyan, magenta, yellow')


    def set_background_color(self, color):
        if color[0] in Panel.COLORS:
            self.background_color = color
        else:
            raise ValueError('Available colors: black, white, red, green, blue, cyan, magenta, yellow')


class Circle(Panel):
    def __str__(self):
        return 'Circle: (' + super(Circle, self).__str__() + ')'


class Square(Panel):
    def __init__(self, size):
        super().__init__(size)
        self.angle = 0

    def rotate(self, angle):
        self.angle += int(angle[0]) % 360

    def __str__(self):
        return 'Square: (' + super().__str__() + ', rotation ' + str(self.angle) + ')'


class Rectangle(Panel):
    def __init__(self, size):
        super().__init__(size)
        self.angle = 0

    def rotate(self, angle):
        self.angle += int(angle) % 360

    def __str__(self):
        return 'Rectangle: (' + super().__str__() + ', rotation ' + str(self.angle) + ')'


class Triangle(Panel):
    def __init__(self, size):
        super().__init__(size)
        self.angle = 0

    def rotate(self, angle):
        self.angle += int(angle) % 360

    def __str__(self):
        return 'Triangle: (' + super().__str__() + ', rotation ' + str(self.angle) + ')'


def correct_name(name):
    if name[0].isdigit():
        raise ValueError('Not use digit as first sign in name')
    return name

class Menu:
    AVAILABLE_FIGURES = {'circle': Circle, 'triangle': Triangle, 'square': Square, 'rectangle': Rectangle}

    def __init__(self):
        self.figures = dict()

    def help(self):
        print('''add <figure> <name> <size>
remove <name>
move <name> <vector>
scale <name> <ratio>
rotate <name> <angle>
set_border_color <name> <color>
set_background_color <name> <color>
help
quit
<figure> to jedno z: circle, square, rectangle, triangle
<name> - dowolny unikatowy identyfikator mogący zawierać litery, cyfry i podkreślniki, nie zaczynający się od cyfry
<ratio> - dowolna liczba rzeczywista, różna od 0
<angle> - dowolny kąt w stopniach
<color> to jedno z: black, white, red, green, blue, cyan, magenta, yellow
Każda figura po dodaniu ma środek w punkcie (0, 0). 
''')

    def add(self, figure, name, size):
        name = correct_name(name)
        if name in self.figures.keys():
            raise ValueError('Name already exist!')
        else:
            self.figures[name] = Menu.AVAILABLE_FIGURES[figure.lower()](size)
            print('Figure added')

    def remove(self, name):
        if name in self.figures.keys():
            del self.figures[name]
            print('Figure removed')
        else:
            raise ValueError('Name does not exist!')

    def quit(self):
        for f in self.figures.values():
            print(f)

    PANEL_COMMANDS = {'help': help, 'add': add, 'remove': remove, 'quit': quit}
    FIGURE_COMMANDS = {'move', 'scale', 'rotate', 'set_border_color', 'set_background_color'}

    class LineCommand:

        def __init__(self, line):
            element = line.split()
            self.command = element[0].lower()
            if self.command in Menu.FIGURE_COMMANDS:
                self.name = element[1]
                self.parameters = element[2:]
            else:
                self.parameters = element[1:]

    def run(self):
        print('Type: help or if u want leave type: quit')
        while True:
            try:
                line = self.LineCommand(input('Command: '))
                if line.command == 'quit':
                    self.PANEL_COMMANDS[line.command](self)
                    break
                elif line.command in self.FIGURE_COMMANDS:
                    self.set(line.command, line.name, line.parameters)
                elif line.command in self.PANEL_COMMANDS:
                    self.PANEL_COMMANDS[line.command](self, *line.parameters)
                else:
                    print('Type help, command is incorrect')
            except (ValueError, IndexError, TypeError) as e:
                print(e)

    def set(self, execute, name, parameters):
        if name in self.figures.keys():
            if execute == 'set_border_color':
                self.figures[name].set_border_color(parameters)
                print('Border color changed')
            if execute == 'set_background_color':
                self.figures[name].set_background_color(parameters)
                print('Background color changed')
            if execute == 'move':
                self.figures[name].move(parameters)
                print('Figure moved')
            if execute == 'scale':
                self.figures[name].scale(parameters)
                print('Figure resized')
            if execute == 'rotate':
                self.figures[name].rotate(parameters)
                print('Figure rotated')

        else:
            raise ValueError('Provide correct name')


if __name__ == '__main__':
    menu = Menu()
    menu.run()


