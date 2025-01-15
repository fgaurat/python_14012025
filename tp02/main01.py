

def make_incrementor(init_value):
    # l = []
    def f(value):
        # r = sum(l)
        return value+init_value

    return f


def main():
    do_inc = make_incrementor(10)
    r = do_inc(5)
    print(r) # 15
    
    
    
    
if __name__=='__main__':
    main()
