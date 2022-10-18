import random, string, pyperclip

UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
DIGITS = string.digits
SYMBOLS = "!#%&/()=?-"

def get_random_chars(source, amount):
    result = []
    while len(result) < amount:
        random_char = random.choice(source)
        if random_char not in result:
            result.append(random_char)
    return result

def build_password():
    result = get_random_chars(UPPERCASE, random.randint(8, 10))
    result += get_random_chars(LOWERCASE, random.randint(8, 10))
    result += get_random_chars(DIGITS, random.randint(2, 4))
    result += get_random_chars(SYMBOLS, random.randint(2, 4))

    random.shuffle(result)
    result = "".join(result)

    return result

def main():
    password = build_password()
    pyperclip.copy(password)
    print("Password generated and copied to clipboard.")

if __name__ == "__main__":
    main()
