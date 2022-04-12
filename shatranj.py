n = int(input("please insert first number : "))
m = int(input("Please insert Second number :"))

j=0
while j < m :
    
    if j%2 != 0 :
        for i in range(n):
            if i in range(1,n,2):
              print("🟨", end="")
            else:
              print("🟩",end="")
        print()
    elif j%2==0 :     
        for i in range(n):
            if i in range(1,n,2):
              print("🟩", end="")
            else:
              print("🟨",end="")
        print()
    j+=1
    
