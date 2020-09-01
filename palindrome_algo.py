main_str = "whatahw"

def palindrome(word1):
    word = ''.join(x.lower() for x in word1)
    if len(word) == 1:
        return word
    if len(word) == 2:
        if word[0] == word[-1]:
            return word
    else:
        return word[0] + palindrome(word[1:-1]) + word[-1]


# print(palindrome(main_str))

# Second Method
def check_palindrome(main_str):

    if (''.join(x.strip(',').lower().strip() for x in main_str) == ''.join(
            x.strip(',').lower().strip() for x in main_str[::-1])):
        return "YES"
    else:
        return "No"

# print(check_palindrome(main_str))
