def getValue():
    int1 = input("Please enter a integer to calculate the area of:")
    return int1


def validateValue(value):
    while True:
        try:
            value = int(value)
            return True
            break
        except:
            return False
    

def findArea(a, b):   
    return int(a) * int(b)    
