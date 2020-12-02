import sys


def main():
    name = "World"
    if len(sys.argv) == 1:
        print(f'Hello, {name}!')
    else:
        name = " "
        arguments = sys.argv[1:]
        name = name.join(arguments)
        print(f'Hello, {name}!')


if __name__ == '__main__':
    main()
