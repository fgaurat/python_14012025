def add(*args):
    print(args)
    r = sum(args)
    return r


def hello(**kwargs):
    print(kwargs)
    print("Hello", *kwargs.values())

def hello2(name,firstName,/): # positional only
    print(name,firstName)

def hello3(*,name,firstName):# Keyword only
    print(name,firstName)

def main():
    # region the_region
    l = [10, 20, 30, 40, 50]
    # r = add(l) # 150
    r = add(10, 20, 30, 40, 50)  # 150
    # assert r == 151
    # endregion

    a, b, *c = 0, 1, 2, 3, 4, 5, 6

    print(a, b, c)

    print(*c, sep=';')
    r = add(*l)
    print(r)
    # hello("GAURAT","Frédéric","Dev")
    hello(job="Dev", firstName="Frédéric", name="GAURAT")
    
    d = {
        "job": "Dev", "firstName": "Frédéric", "name": "GAURAT"
    }
    hello(**d)

    hello2("GAURAT","fred")
    hello3(name="GAURAT",firstName="fred")

if __name__ == '__main__':
    main()
