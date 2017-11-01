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

