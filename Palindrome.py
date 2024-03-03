## palindrome or not
def is_pal(n):
 return n == n[::-1]
n=input("\nEnter the no:")
if is_pal(n):
 print("Palindrome")
else:
 print("Not Palindrome")
 
