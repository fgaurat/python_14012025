from functools import wraps
def do_log(file_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print(f"LOG PARAMS to {file_name}",*args,**kwargs)
            r = func(*args,**kwargs)
            print(f"LOG RETURN to {file_name}",r)
            return r
        return wrapper
    return decorator
     

@do_log(file_name="leslogs.log")
def say_hello(name:str):
    """say_hello

    Args:
        name (str):the name
    """
    r = f"Hello {name}"
    return r


def main():
    r = say_hello('Fred')
    print(r)
    print(say_hello.__name__)
    print(say_hello.__doc__)
if __name__=='__main__':
    main()
