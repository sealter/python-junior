#/usr/bin/python3

print("****** deractor ******")

def document_it(func) :
    def new_function(*arg, **args) :
        print("running in ", func.__name__)
        result = func(*arg, **args)
        print("Result : ", result)
        return result
    return new_function

def add_ints(arg1, arg2) :
    return arg1 + arg2

new_func = document_it(add_ints)
print(new_func)
new_func(3, 5)


@document_it
def add_int2(a, b, c) :
    return a + b + c

add_int2(1, 2, 3)


def talk(func) :
    def new_func(*arg, **args) :
        return func(*arg, **args)
    return new_func

@document_it
@talk
def add_multi(a, b) :
    return a * b

print("---------")

add_multi(7, 8)


@talk
@document_it
def add_multi2(a, b, c) :
    return a * b * c

add_multi2(1, 2, 3)

