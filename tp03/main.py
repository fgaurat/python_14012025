import traceback
class DivBy12Error(ArithmeticError):
    
    def __init__(self):
        super().__init__('Division par 12 !')

def div(a,b):
    if b==12:
        # raise ArithmeticError('Division par 12 !')
        raise DivBy12Error()
    return a/b




def main():
    try:
        a = 2
        b = int(input("b: "))
        c = call_div(a,b)
        print(c)
    # except ZeroDivisionError as e:
    #     print('ZeroDivisionError',e)
    # except TypeError as e:
    #     print('TypeError',e)
    # except ValueError as e:
    #     print('ValueError',e)
    except Exception as e:
        print('Exception',e,type(e))
        traceback.print_exc()
    else:
        print("pas d'erreur")
        
    print("La suite du code")


if __name__=='__main__':
    main()
