def prime(n):
 for i in range(2,n//2+1):
    if n%i==0:
        return False
    else:
        return True
n=int(input("\nEnter the number:"))
if prime(n):
 print("Prime No")
else:
 print("Not Prime")