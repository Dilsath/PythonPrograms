user=[]
def multiple():
    m=int(input("how many elements to enter in list = "))
    for i in range(0,m):
        n=int(input("enter the element"))
        user.append(n)
def enter():
    print("to add one element = 1\nto add multiple element = 2")
    a=int(input("enter your choice = "))
    if(a==1):
        i=int(input("enter one element"))
        user.append(i)
    elif(a==2):
        multiple()
    else:
        print("invalid number")
def modify():
    print("to modify a element = 1 \nto replace a element = 2")
    a=int(input("enter your choice = "))
while True:
    print("add element = 1\nmodify element = 2\ndelete element = 3\nsort element = 4\ndisplay element = 5\nexit = 6")
    u=int(input("enter your choice = "))
    if(u==1):
        enter()
    if(u==2):
        modify()
    if(u==6):
        break
    
   
