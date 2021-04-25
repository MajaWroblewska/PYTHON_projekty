'''
zad31
Zmodyﬁkuj dekorator z zadania 30, aby przyjął argumenty typu bool z domyślnymi wartościami
True: name, args, kwags, execution_time. W zależności od argumentów wypisuj dane informacje lub nie.
'''
import time
from functools import wraps

def time_it(name=True, print_args=True, print_kwargs=True, execution_time=True):
    def decorator_time_it(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)  # result = 100 * 1000
            if execution_time:
                print(f"Duration time: {time.time() - start_time}")
            if name:
                print(f"Function executed: {func.__name__}")
            if print_args:
                print(f"Arguments: {args}")
            if print_kwargs:
                print(f"Keyword arguments: {kwargs}")
            return result
        return wrapper
    return decorator_time_it

@time_it()
def greet_president(name):
    print(f"Hello there, Mr. President")
    print(f'{name} '*2)
greet_president(name='Maja')

# @time_it(name=False, print_args=False,print_kwargs=True)
