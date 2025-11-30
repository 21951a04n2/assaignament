Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
  Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
  Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string
 solution:
a=int(input("enter a no"))
b=int(input("enter a no"))
typeofoperation=input("enter operation")
if typeofoperation=="add":
    print(a+b)
elif typeofoperation=="subtarction":
    print(a-b)
elif typeofoperation=="multipication":
    print(a*b)
elif typeofoperation=="didvide":
    print(a//b)
else:
    print("choose correct operation")
