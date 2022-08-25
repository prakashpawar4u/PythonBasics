# import time
# import pdb
#
# def time_it(func):
#     #pdb.set_trace()
#     print(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         print("Starting Time:", start)
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(func.__name__ + " took " + str((end - start) * 1000) + "mil sec")
#         return result
#
#     return wrapper
#
#
# @time_it
# def calc_sq(numbers):
#     result = []
#     for number in numbers:
#         result.append(number * number)
#     return result
#
# @time_it
# def calc_cube(numbers):
#     print("inside CUBE")
#     result = []
#     for number in numbers:
#         result.append(number * number * number)
#     return result
#
#
#
# array = range(1,100)
# out_square = (calc_sq(array))
# print("SQ:", out_square)
# out_cube = calc_cube(array)
# print("CUBE:", out_cube)



def decorator(func):
    def wrapper(*args, **kwargs):
        print("Inside decorated func")
        l = [1,2,3,4]
        print("call this func:", func)
        result = func(l)
        print("Wrapper after execution:",result)
    return wrapper


@decorator
def caller12(l, start = 0, end = 2):
    print("called the func")
    finalList = []
    for i in range(start, len(l), end):
        finalList.append(l[i:i+end])
    return(finalList)

caller12()
