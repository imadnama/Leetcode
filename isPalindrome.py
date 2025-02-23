def isPalindrome(number):
    if number < 0:
        return False
    return str(number)[0::] == str(number)[::-1]

# number = 121
# number2 = -121
# number3 = 10000000001
# number4 = 1000000000012
#
# print(isPalindrome(number4))