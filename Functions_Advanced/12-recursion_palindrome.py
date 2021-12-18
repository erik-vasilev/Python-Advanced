def palindrome(word, index):
    if word == ''.join(reversed(list(word))):
        return f'{word} is a palindrome'
    else:
        return f'{word} is not a palindrome'


print(palindrome("peter", 0))
