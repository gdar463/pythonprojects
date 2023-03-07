def is_anagram(a: str, b: str):
    alist = sorted(*a.split(), key=str.lower)
    blist = sorted(*b.split(), key=str.lower)
    if alist == blist:
        return True
    else:
        return False

first = input("Enter first word: ").replace(" ", "")
second = input("Enter second word: ").replace(" ", "")

if is_anagram(first, second):
    print(first + " and " + second + " are anagrams.")
else:
    print(first + " and " + second + " are not anagrams.")
