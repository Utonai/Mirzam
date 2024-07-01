import time
from mirzam import mirzam

FLAG_FILE = "flag.txt"


def main():
    flag_list = open(FLAG_FILE, "r").read().splitlines()
    for flag in flag_list:
        mirzam(flag)


if __name__ == "__main__":
    main()
