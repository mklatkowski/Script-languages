import logging
import inspect
import time

def log(level):
    def decorator(target):
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = target(*args, **kwargs)
            end_time = time.perf_counter()
            logging.log(level,
                        f"{target.__name__} called with arguments: {args}, {kwargs}. Returned {result}. Took {end_time - start_time} seconds.")
            return result
        return wrapper
    return decorator


@log(logging.CRITICAL)
def hello():
    print("Hello")


if __name__ == "__main__":
    hello()