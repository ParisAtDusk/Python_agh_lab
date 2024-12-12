

def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()  # Convert to uppercase
    return wrapper


@uppercase_decorator
def sample_function():
    return "Hi there"


print(sample_function())  # Output: "HI THERE"
