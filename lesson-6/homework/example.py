# def simple_iterator():
#     print('Start')
#     print('First')
#     yield 1
#     print('Second')
#     yield 2
#     yield 3



# val =  simple_iterator()
# for i in val:
#     print(i, end='end of iteration\n')


# def infinite_iterator():
#     i = 0
#     while True:
#         yield i
#         i += 1


# counter = infinite_iterator()

# for i in counter:
#     print(i, end=' ')

# def bold(func):
#     def wrapper():
#         return f"<Bold: {func()}>"
#     return wrapper

# @bold
# def hello():
#     return "Hello"

# print(hello())