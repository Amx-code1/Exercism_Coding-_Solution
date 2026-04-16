def square(number):
    if number == 1:
        return number
    elif number <=64 and number > 1:
        return 2**(number-1)
    else:
        raise ValueError("square must be between 1 and 64")


# def total(number):
#     sum=0
#     i=0
#     if number == 1:
#         sum += number
#         return sum
#     elif number <= 64 and number > 1:
#         if i< number:
#             sum += 2**(number - 1)
#             i += 1
#         return sum
#     else:
#         raise ValueError("square must be between 1 and 64")
        
def total():
    return 2**64-1
