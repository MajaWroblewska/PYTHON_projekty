from functools import wraps


def repeat(times,b):
    def decorator_repeat(func):
        @wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat

@repeat(times=24,b=125)
def greet(name):
    print(f"Hello {name}")

greet("John")