import hw1

def main():
    int1 = hw1.getValue()
    int2 = hw1.getValue()
    if hw1.validateValue(int1) & hw1.validateValue(int2):
        print("Numbers are integers")
        print("The area of ({}) and ({}) is ({})".format(int1, int2,hw1.findArea(int1,int2) ))
    else:
        print("Numbers are not integers")


if __name__ == "__main__":
    main()
