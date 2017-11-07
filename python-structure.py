#/usr/bin/python3


flag = True
if flag:
    print("It is true")



i = 0
if i == 1 :
    print("It is 1")
elif i == 0 :
    print("It is 0")
else :
    print("It is not 1 or 0")


print("***************** while ****************")

i = 0

while True:
    if i >= 10:
        break;
    i += 1;
    print(i)

else:
    print("while else")



print("************ for ***********************")

l = ["a", "b", "c", "d", "e"]

for item in l :
    print(item)



print("************* generator  ********************")

ll = [t for t in range(20) if t % 2 == 0 ]
print(ll)


print("************** zip *************")



print("************ function *************")


def echo(str) :
    print("***** str = ", str)

echo("github")


def cap(words, func) :

    for word in words:
        func(word)

cap(["title", "python", "AI"], lambda word : print(word.capitalize()) )




print("******** namespace and scope ***********")

fruit = "banana"
def change_fruit() :
    fruit = "apple"
    print("fruit in change_fruit function is ", fruit)


print("fruit is ", fruit)
change_fruit()

def change_global_fruit():
    global fruit
    fruit = "avocado"
    print("fruit in change_global_fruit function is ", fruit)
    print("----- local vars : ", locals())

change_global_fruit()
print("fruit after change global ", fruit)

print("----- global vars: ", globals())



print("************  exception *******************")

l = [1, 3, 4]

try :
    print(l[5])
except:
    print("index out of exception")



short_list = [2, 4, 8]
while True:
    value = input("input your number [q to quit]")
    if value == 'q' :
        break
    try :
        print(short_list[int(value)])
    except IndexError as idxErr :
        print("Index Error ", idxErr)
    except Exception as other :
        print("other Exception ", other)



class MyException(Exception) :
    print("MyException")

try :
    raise MyException("HaHA")
except:
    print("Exception Testing...")
