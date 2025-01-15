from RectangleSingleton import RectangleSingleton
from RectangleSingletonDeco import RectangleSingletonDeco
from RectangleMetaSingleton import RectangleMetaSingleton
def main():
    r = RectangleSingleton(2,6)
    r1 = RectangleSingleton(2,6)
    r2 = RectangleSingleton(200,659)
    print(id(r))
    print(id(r1))
    
    print(r)
    print(r1)
    # r1.longueur = 1000
    # print(r)
    # print(r1)
    
    print(50*'-')
    r = RectangleSingletonDeco(10,20)
    r1 = RectangleSingletonDeco(10,20)
    print(id(r))
    print(id(r1))
    
    print(r)
    print(r1)
    print(50*'-')
    
    print(type(12))
    print(type(int))
    
    print(50*'-')
    print("create r")
    r = RectangleMetaSingleton(2,3)
    print("create r1")
    r1 = RectangleMetaSingleton(5,5)
    print(r)
    print(r1)
    
    print(id(r))
    print(id(r1))
if __name__=='__main__':
    main()
