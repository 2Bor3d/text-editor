#!/usr/bin/python3.10
import io
import sys


def print_file(file):
    try:
        file = file.readlines()
        for i in range(len(file)):
            print(file[i].replace("\n", ""))
    except io.UnsupportedOperation:
        print("")


def open_file(path, mode="r"):
    try:
        file = open(path, mode)
    except FileNotFoundError:
        file = open(path, "x")
    return file


def open_new(path):
    file = open_file(path)
    print_file(file)


def print_help():
    print("open PATH - open file")
    print("-r / read - print inside of file")
    print("-w / write TEXT - overwrite file with text")
    print("-h / help - print this")


def main():
    path = "./text.txt"
    text = ""
    if len(sys.argv) > 1:
        if "-h" in sys.argv:
            print_help()
        else:
            for i in range(len(sys.argv)):
                if i != 0:
                    if sys.argv[i][0] != "-":
                        path = sys.argv[i]
                        if len(sys.argv) > i + 1:
                            text = sys.argv[i+1]
                        break
            if "-r" in sys.argv:
                try:
                    file = open_file(path)
                    print_file(file)
                except UnboundLocalError:
                    print("Please specify path")
            if "-w" in sys.argv:
                try:
                    with open_file(path, "w") as file:
                        try:
                            file.write(text)
                        except UnboundLocalError:
                            print("Please specify text")
                except UnboundLocalError:
                    print("Please specify path")

    else:
        path = input("path: ")
        file = open_file(path)
        print_file(file)
        while True:
            i = input(">")
            if i[:4] == "open":
                path = i[5:]
                open_new(path)
            if i == "read":
                file = open_file(path)
                print_file(file)
            if i[:5] == "write":
                with open_file(path, "w") as file:
                    file.write(i[6:])
            if i == "help":
                print_help()


if __name__ == "__main__":
    main()
