import time
from mirzam import mirzam


def main():
    while 1:
        flag_list = []
        for line in iter(input, ''):
            flag_list.append(line)
        print("working...")
        for flag in flag_list:
            m = mirzam(flag)
            if m:
                print(">", m)
        print("end")


if __name__ == "__main__":
    main()
