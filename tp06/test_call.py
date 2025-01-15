class LaClass:
    
    def __new__(cls):
        print("def __new__(cls)")
        return object.__new__(cls)

    def __init__(self):
        print("def __init__(new)")
    
    def __call__(self):
        print("def __call__(self)")    

def main():
    l = LaClass()
    l()
if __name__=='__main__':
    main()
