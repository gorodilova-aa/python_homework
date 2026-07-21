# one time setup
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        pos_par = list(args) if args else "none"
        kw_par = kwargs if kwargs else "none"
        return_value = func(*args, **kwargs)
        log_string = f"function: {func.__name__}\n positional parameters: {pos_par}\n keyword parameters: {kw_par}\n return: {return_value}\n"
        logger.log(logging.INFO, log_string)
        return return_value
    return wrapper
        

@logger_decorator
def hello():
    print("Hello World!")

@logger_decorator
def pos_args(*args):
    return True

@logger_decorator
def kw_args(**kwargs):
    return logger_decorator

hello()
pos_args(1, 2, 3, 4, 5)
kw_args(a=1, b=2, c=3)
