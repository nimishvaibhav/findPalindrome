

def find_palindrome_str(name: str) -> str:
    rev = name[::-1]

    if name == rev:
        print(f'{name} is palindrome')
    else:
        print(f'{name} is not palindrome')


def find_palindrome_num(num: int) -> str:
    temp = num
    rev = 0
    while num > 0:
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10

    if temp == rev:
        print(f'{temp} is palindrome')
    else:
        print(f'{temp} is not palindrome')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    find_palindrome_str('PyCharm')
    find_palindrome_str('RACECAR')

    find_palindrome_num(121)

