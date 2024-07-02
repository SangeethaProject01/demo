#recursion
#call stack 

# def m3():
#     print("hello 3")
# def m2():
#     m3()
#     print("hello 2")
   
# def m1():
#     m2()
#     print("hello 1")
    

# m1()


# def sayHi():
#     print("hiiiiiiiiiiiii")
#     sayHi()

# sayHi()

#recursive function

# def number(n):
#     if n!=0:
#        number(n-1)
#        print(n)
# number(10)


def print_numbers(n):
    if n == 0:
        return
    else:
        print(n)
        print_numbers(n-1)
        print(n)
# Call the function with 10
print_numbers(10)
