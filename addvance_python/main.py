# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         duration = end_time - start_time
#         print(f"Function '{func.__name__}' executed in {duration:.2f} seconds.")
#         return result
#     return wrapper



# @timer
# def my_function():
#     # Simulate some time-consuming operation
#     time.sleep(2)
#     print("Function executed.")



# @timer
# def another_function():
#     time.sleep(5)
#     print("this is another function")


# my_function()
# another_function()

def is_user_authenticated(username, password):
    # Custom authentication logic
    # Implement your authentication logic here
    valid_username = "john"
    valid_password = "password"

    if username == valid_username and password == valid_password:
        return True
    else:
        return False

def authenticate(func):
    def wrapper(username, password):
        if is_user_authenticated(username, password):
            return func(username, password)
        else:
            return "Authentication failed. Please check your username and password."
    return wrapper

@authenticate
def protected_function(username, password):
    return f"Welcome, {username}! This is a protected function."

# Test case 1: Correct username and password
print(protected_function("john", "password"))  # Output: "Welcome, john! This is a protected function."

# Test case 2: Incorrect password
print(protected_function("john", "wrong_password"))  # Output: "Authentication failed. Please check your username and password."

# Test case 3: Non-existent username
print(protected_function("jane", "password"))  # Output: "Authentication failed. Please check your username and password."
