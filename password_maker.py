import string
import secrets


# All the characters that can be used in a password.
CHARS = string.ascii_letters + string.digits + string.punctuation


def main() -> None:
    length_raw = input(
        "Please specify the number of characters you would like the password to contain: "
    )
    desired_length = int(length_raw)

    password = ""

    while len(password) != desired_length:
        password += secrets.choice(CHARS)

    print("Your password is:\n\n" + password + "\n\n")


if __name__ == "__main__":
    main()
