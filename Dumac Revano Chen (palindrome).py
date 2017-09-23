word1="nakikan"
word1=word1.casefold()#make it less sensitive for better comparison
Reverse1=reversed(word1)
if list(word1) == list(Reverse1):
    print("it is palindrome word")
else:
    print("it is not palindrome word")