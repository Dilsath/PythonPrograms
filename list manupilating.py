user=[]

def multiple():
    m=int(input("how many elements to enter in list = "))
    for i in range(0,m):
        n=int(input("enter the element = "))
        user.append(n)

def enter():
    print("to add one element = 1\nto add multiple element = 2")
    a=int(input("enter your choice = "))
    if(a==1):
        i=int(input("enter one element = "))
        user.append(i)
    elif(a==2):
        multiple()
    else:
        print("invalid number")

def modify():
    print("to modify a element by index value = 1 \nto replace a element = 2")
    a=int(input("enter your choice = "))
    if(a==1):
        x=int(input("enter index value = "))
        y=int(input("enter the new element = "))
        user[x]=y
        print(user)
    if(a==2):
        a=int(input("enter the element that to be modified = "))
        b=int(input("enter the new element = "))
        if(a in user):
            x=user.index(a)
            user.pop(x)
            user.insert(x,b)
    else:
        print("invalid input")    
            
def delete():
    print("to delete a element =1\nto delete the last element =2\nto delete a element by index value = 3")
    a=int(input("enter your choice = "))
    if(a==1):
        x=int(input("enter the element = "))
        user.remove(x)
    if(a==2):
        user.pop()
    if(a==3):
        y=int(input("enter the index value = "))
        del user[y]
    else:
        print("invalid input")       
        

def sort():
    print("to print list in assending order = 1\nto print list in desending order =2") 
    a=int(input("enter your choice = "))
    if(a==1):
        user.sort()
        print(user)
    if(a==2):
        user.sort(reverse=True)
        print(user)
    else:
        print("invalid input")           

def display():
    print(user)

while True:
    print("add element = 1\nmodify element = 2\ndelete element = 3\nsort element = 4\ndisplay element = 5\nexit = 6")
    u=int(input("enter your choice = "))
    if(u==1):
        enter()
    if(u==2):
        modify()
    if(u==3):
        delete()    
    if(u==4):
        sort()    
    if(u==5):
        display()
    if(u==6):
        break
    else:
        print("invalid input")
    
   
