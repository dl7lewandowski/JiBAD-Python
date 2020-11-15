
def gdc(a, b):
    while a!= b:
        a, b = max(a, b), min(a, b)
        a = a - b
    return a

def main():
    while True:
        try:
            a = int(input("a = "))
            b = int(input("b = "))
            if a >= 1 and b >= 1:
                break
            else:
                print('a or b not can be negative')
        except ValueError as err:
            print("Provaids integer!")
            continue
    return gdc(a, b)

print(main())





