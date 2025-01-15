import sys
def main():
    a = 2
    print(hex(id(a)))
    a=3 
    print(hex(id(a)))
    b=3 
    print(hex(id(b)))
    print(sys.getrefcount(987598752325))
    a=987598752325
    print(sys.getrefcount(987598752325))
    
        

if __name__=='__main__':
    main()
