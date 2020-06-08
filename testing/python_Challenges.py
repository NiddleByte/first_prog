def is_palindrome(word):
    if word.lower() == word[::-1].lower():
        return True
    return False

print(is_palindrome("155000"))
print(is_palindrome("1.(11(11(.1"))