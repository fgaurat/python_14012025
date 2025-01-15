# import lib as l 
from lib import hello as hl

def hello():
    return "Hoooooooo"

def main():
    # print("Hello main")
    # h = lib.hello()
    h = hl()
    print(h)
    print("main",__name__)

if __name__=='__main__':
    main()
