#usr/bin/python3


import os

print("*********  file operate  *************")

print("is file : ", os.path.isfile("text.txt"))

print("is abs: ", os.path.isabs("text.txt"))

print("is abs: ", os.path.isabs("/d"))

print("exists", os.path.exists("/d/soft"))
print("exists .", os.path.exists("."))
print("exists .. ", os.path.exists(".."))

print("realPath . ", os.path.realpath("."))


f = open("file-test.txt", "wt")
print("This is for file test", file = f)
f.close()

if os.path.exists("file-test.txt") :
    f = open("file-test.txt", "r")
    print("file-test.txt contents : ", f.read())
    f.close()
else :
    print("file-test.txt no exists")

#print("rename file-test.txt to file-t.txt", os.rename("file-test.txt", "file-t.txt"))
print("file-test.txt exists after rename", os.path.exists("file-test.txt"))
print("file-t.txt exists after rename ", os.path.exists("file-t.txt"))

if os.path.exists("file-t.txt") :
    print("chmod", os.chmod("file-t.txt", 0o400))

import shutil
if os.path.exists("copy-from-file-t") :
    shutil.copy("file-t.txt", "copy-from-file-t")
print("exists after copy", os.path.exists("copy-from-file-t"))

print("*********  dir operate  *************")

print("is dir", os.path.isdir("text"))

print("is dir", os.path.isdir("/d"))

print("list dir in . ", os.listdir("."))

if  not os.path.exists("dir-test") :
    os.mkdir("dir-test")
    print("mkdir dir-test")

print("dir-test exists ? ", os.path.exists("dir-test"))

print("list content in dir-test", os.listdir("dir-test"))

print("remove dir dir-test", os.rmdir("dir-test"))

print("dir-test exists after remove", os.path.exists("dir-test"))

if os.path.exists("file-text.txt") :
    os.remove("file-text.txt")

if os.path.exists("file-t.txt") :
    os.chmod("file-t.txt", 0o777)
    os.remove("file-t.txt")

if os.path.exists("copy-from-file-t") :
    os.chmod("copy-from-file-t", 0o777)
    os.remove("copy-from-file-t")

print("file-text.txt exists after remove", os.path.exists("file-text.txt"))
print("file-t.txt exists after remove", os.path.exists("file-t.txt"))
print("copy-from-file-t exists after remove", os.path.exists("copy-from-file-t"))



print("********* glob operate  *************")

import glob
print("glob----", glob.glob("python*"))



print("********* program and process operate  *************")

print(" current workspace directory", os.getcwd())
print(" pid ----", os.getpid())

#import subprocess

#print("subprocess date", subprocess.getoutput("date -u"))


import multiprocessing

def whoami(what) :
    print("Process %s says: %s" % (os.getpid(), what))

def do_this(what) :
    whoami(what)

#if __name__ == "__main__" :
#    do_this("I am in main process")
#    for n in range(4) :
#        p = multiprocessing.Process(target=do_this, args=("I am in process %s" % n, ) )
#        p.start()

import time
def loopy(what) :
    whoami(what)
    start = 0
    stop = 10000
    for num in range(start, stop) :
        print("\tNumber %s of %s Honk" % (num, stop))
        time.sleep(1)

if __name__ == "__main__" :
    whoami("main")
    p = multiprocessing.Process(target=loopy, args=("loopy",))
    p.start()
    time.sleep(5)
    p.terminate()
