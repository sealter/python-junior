#/usr/bin/python3

a = 7
print(a)
type_a = type(a)
print(type_a)
type_b = type('b')
print(type_b)
type_c = type(58)
print(type_c)
type_d = type(88.8)
print(type_d)


print(3 + 2)
print(-2)
print(+3)
print(11 / 2)
print(11 // 2)
print(2 * 3)
print(2**4)
print(11 % 2)
s = "999"
print(type(s))
cs = int(s)
print(type(cs))
print(cs)

print(3.0 + 2)

print(0x10)

print(0o10)
print(0b10)

print(divmod(11, 2))

bp = True + 5.0


print(bp)


###############   Float     ####################

print("*****************  float datatype  ********************")
print(float(3))

print(5.0 % 3)

print(divmod(5.0 , 3))



#############  String ################
print("\n")
print("****************** String datatype ***********************")


str = "This is a string."
str2 = 'This is a string too'
str3 = "She laugue: 'is it true?'"
str4 = 'She said: "I love you."'

print(str)
print(str2)
print(str3)
print(str4)

str5 = """ I have a ....
            What the fuck?"""
print(str5)

str6 = "I thin it is a \n joke."
print(str6)



str7 = "Hello Python";
print(str7 * 2)

print(str7.replace("Python", "World"))


print(str7 + str7)

print("This is"" half.")

print("**** string len *****")

print(len(str))


print("***** string slice *********")



print(str7[:])
print(str7[2:])
print(str7[:len(str7) - 1])

print(str7[2:3])
print(str7[:-1])
print(str7[-2 : -1])
print(str7[-1 : -2])
print(str7[-1:])


print("****** string split **********")

str8 = "Hello, Python,Hello, World"
print(str8.split(","))

print("******** String join *******")

print(" ".join(["hello", "world"]))

print("******* String capitalize*******")

print("hello world".capitalize())

print("******* String title *********")

print("hello world".title())


print("******* String find")

str9 = "The actor model is designed to be message-driven and non-blocking, with throughput as part of the natural equation"
print(str9.find("the"))
print(str9.find("The"))

print("***** String count *****")

print(str9.count("the"))

print("**** string strip ****")

str10 = "   hi, actor model in multithread.  "
print(str10)
print(str10.strip())

print("***** string just")

str11 = "actor model ?"
print(len(str11))
print(str11)
print(str11.center(20))
print(str11.ljust(20))
print(str11.rjust(20, "@"))


print("**** string replace ****")

print("hello world".replace("world", "hadoop"))
print("hello world world hello world ".replace("world", "hadoop", 2))





print("***********   List datatype******************")

print("***** list create")

#empty list
l = []
print(l)
ll = list()
print(ll)

#create
l = ["java", "python", "go", "js"]
print(l)

ss = "LinkedIn has launched a new natural language processing (NLP) recommendation engine which is used to provide members with smart-reply recommendations to messages"
ll = list(ss)
print(ll)

li = [l, "scalar", "c"]
print(li)

sss = "One of the requirements of smart-reply is for only a single way of saying something to be suggested"

lil = sss.split(" ")
print(lil)


print("***** list add")

l.append("groovy")
print(l)

l.insert(2, "object-c")
print(l)


print("***** list get")

print(l[0])
print(l[-2])

print("***** list delete")

print(l.pop())
print(l)

del l[-2]
print(l)

l.remove("js")
print(l)

print("**** list index")

print("java" in l)
print("kotlin" in l)

print(l.index("java"))

print(l.index("python"))

print("**** list compine")

lt = ll + li
print(lt)

print("**** list copy")

l1 = l
print(l1)
l1.append("aka")
print(l1)
print(l)

l.append("c++")
print(l1)
print(l)

l2 = l.copy()

l2.remove("java")
print(l2)
print(l)

print("**** list pop")

t = l2.pop()
print(t)
print(l2)

print("**** list slice")

tt = l2[:: 2]
print(tt)


print("***** list other")

print(len(l2))
print(len(l))

print(len(ss))
print(len(ll))


print("**********   tuple datatype  ****************")

print("***** tuple create")

tu = ()
print(tu)
print(type(tu))

tu = ("hello", "world")
print(tu)
print(type(tu))


print("****** tuple unpacking")

sr1, sr2 = tu
print(sr1)
print(sr2)

print("***** tuple exchange")

i = 1
j = 2
i, j = j, i
print(i)
print(j)




print("************  dict datatype  *********************")


print("***** dict create")

dic = {}
print(dic)

dic = {"Simpler" : "Simpler and easier to train", "Faster" : "Faster to train, which is key in their use case of needing suggestions immediately", "Less" : "Less risk of an inappropriate reply"}

print(dic)


d = [("LinkedIn", "mechanism"), ("traditional", "messages"), ("classification", "model")]
print(dict(d))


e = (["also", "point"], ["anonymizing", "enineering"], ["due", "to"])
dc = dict(e)
print(dc)

print(dict(["cd", "ef", "ui"]))

print("****** dict add")

dic["sequence"] = "semantic"
print(dic)

print("***** dict remove")

del dic["sequence"]

print(dic)

print(dc)
dc.clear()
print(dc)



print("**** dict replace")

dic["Simpler"] = "Simpler haha"
print(dic)


print("***** dict get")


sa = dic["Simpler"]
print(sa)

#sb = dic["complex"]
#print(sb)


sc = dic.get("complex")
print(sc)

sd = dic.get("Simpler")
print(sd)

print("**** dict convert")


print("***** dict copy")

dicc = dic
print(dic)
print(dicc)
dicc["dic COpy"] = "dic Copy Test"
print(dic)
print(dicc)

dic["lalal"] = "hahhqah"
print(dic)
print(dicc)


dic2 = dic.copy()

print(dic2)
print(dic)

dic2["dic2"] = "dic2222"
print(dic2)
print(dic)

dic["dicccccc"] = "dicccccc"

print(dic2)
print(dic)


print("***** dict keys")


ttt = dic.keys()
print(type(ttt))
print(ttt)

print(list(ttt))


print("***** dict check")
print("Simpler" in dic)

print("ttt" in dic)


print("****** dict update")


dic2 = {"dic2" : "dic2 to update"}

dic.update(dic2)
print(dic)


print("******* dict values")


ht = dic.values()
print(type(ht))
print(ht)
print(list(ht))

print("****** dict items")


htcc = dic.items()
print(type(htcc))
print(htcc)
print(list(htcc))






print("************  set datatype  ******************")

print("**** set create")

empty_set = set()

print(empty_set)

even_number = {0, 2, 4, 6, 8}

print("even_number:", even_number)

odd_number = {1, 3, 5, 7, 9}


print("odd_number", odd_number)

print(set("letters"))


print("**** set add")


print("**** set remove")

print("***** set check")

print("***** set intersection")


print("***** set union")


print("**** set difference")


print("**** set exclusive")
