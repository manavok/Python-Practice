# function defination
# def greet(user = "Manav"):
#     print(user)
# greet("Krsna")

# labda function
# number = int(input("Enter Number:"))
# cube = lambda x: x ** 3
# ab = cube(3)
# print(f"The cube of the number is {ab}.")

# args => passing list, tuples, ...
# def sum_all(*args):
#     return sum(args)

# tu = (1,2,3,4)
# print(sum_all(1,2,3,4))     
# print(sum_all(*tu))    
# li = [1,2,3,4]
# print(sum_all(*li)) 

# yeild

# def count_up_to(n):
#     i=1
#     while i <= n:
#         yield(i)
#         i+=1

# print(count_up_to(3))
# for num in count_up_to(3):
#     print(num)

# # or it can be
# count = count_up_to(3)
# print(count)
# print(next(count))
# print(count)
# print(next(count))
# print(count)
# print(next(count))
# print(count)

# clouser and function inside function
def any_power(power):
    def actual(a):
        return a ** power
    return actual


square = any_power(2)
print(square(5))
cube = any_power(3)
print(cube(5))
power_four = any_power(4)
print(power_four(5))