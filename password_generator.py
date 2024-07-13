import random
import string

def generate_password(length):
    if length < 6:
        print("Password length should be at least 6.")
        return ""

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Password Generator")
    print("==================")
    
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    password = generate_password(length)
    if password:
        print(f"Generated password: {password}")

if __name__ == "__main__":
    main()

