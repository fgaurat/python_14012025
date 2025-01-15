# import lib
from lib import a
print(a)
a="toto"
a = 12

def main():
    global a
    a =123
    # a=3 # UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
    # print(a) #NameError: name 'a' is not defined

    # if True:
    #     a=2
    print("dans main",a)

if __name__=='__main__':
    print("avant",a)
    main()
    print("après",a)
