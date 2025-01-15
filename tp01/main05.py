# HelloWorld => UpperCamelCase class,interface,...
# helloWorld => camelCase
# hello_world => snake_case
# hello-world => kebab-case
from collections import deque

def main():
    """
    Main function
    """
    l = [10, 20, 30, 40, 50]
    l.append(60)
    print(l)
    last_value = l.pop()
    print(last_value)
    l.insert(0,-10)
    print(l)
    first_value = l.pop(0)
    print(first_value)
    d = deque(l)
    print(d)
    d.appendleft(-20)
    print(d)


if __name__ == '__main__':
    main()
