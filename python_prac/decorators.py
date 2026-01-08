# Problem 1: Write a decorator that measures the time a function takes to execute.
'''
import time

def timer(fx):
    def wrapper():
        start=time.time()
        result=fx()
        end=time.time()
        print(f"{fx.__name__} take time {end-start}s")
        print(result)
        return result
    return wrapper

@timer          # this means here , show = timer(show)
def example():
    time.sleep(2)
    return 2
    # print("Hello its done")

example()

'''

#Problem 2: Create a decorator to print the function name the values of its arguments every time the function is called.

'''
def debug(fx):
    def wrapper(*args,**kwargs):
        args_value=", ".join(str(arg) for arg in args)
        kwargs_value=", ".join(f"{k}={v}" for k,v in kwargs.items())
        print(f"Name of the functions : {fx.__name__} \nargs : {args_value}\nkwargs: {kwargs_value}")

        return fx(*args,**kwargs)
    
    return wrapper   

@debug
def greet(name,greeting="hello"):
    print("{}, {}".format(greeting,name))

greet("Anuj",greeting = "Namaste ")
'''

#Problem 3: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments , the cacked value is returned instead of re-executing the function.
'''
import time
def cache(func):
    cached_value={}
    
    def wrapper(*args):
        if args in cached_value:
            return cached_value[args]
        
        result=func(*args)
        cached_value[args]=result
        return result
    
    return wrapper

@cache    
def long_running_function(a,b):
    print("in sleep")
    time.sleep(4)  
    return a+b

print(long_running_function(2,5))
print(long_running_function(2,5))
print(long_running_function(4,9))
'''