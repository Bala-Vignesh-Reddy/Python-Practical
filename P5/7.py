#Write a python function that checks whether a passed string is palindrome or not

def palin(s):
    s = s.replace(" ", "").lower()
     
    if s == s[::-1]:
        return True
    else:
        return False

string = input("Enter string:")
if palin(string):
    print("String is Palindrome")
else:
    print("Not palindrome")
