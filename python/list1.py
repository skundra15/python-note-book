mylist = ["apple","banana","cherry"]
print (mylist)
thislist=list (("apple","banana","cherry"))
print(thislist)
print (len(thislist))


a=("apple","banana","cherry")
y=("orange")
a+=y
print(a)


a,b,c,d=10,20,30,40
def fun():
    a,b,c=100,200,300
    print("in fun",a,b,c,d)
    def funb():
        a,b=1000,2000
        print("in funb",a,b,c,d)
        def func():
                  a=10000
        print("func",a,b,c,d)
        
        func()
    funb()
fun()
print("in__main",a,b,c,d)