import sys
import urllib.request


def main():
    number = sys.argv[1]
    with urllib.request.urlopen("http://numbersapi.com/" + number) as request:
        response = request.read().decode("utf-8")
        print(response)


if __name__ == "__main__":
    main()

