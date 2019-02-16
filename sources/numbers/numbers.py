import sys
import urllib.request


class NumbersApi:
    def __init__(self):
        self.base_url = "http://numbersapi.com/"

    def build_url(self, query, number):
        if query == "trivia":
            return self.base_url + number
        elif query == "math":
            return self.base_url + number + "/math"
        else:
            sys.exit("Unknown query: " + query)

    def do_request(self, url):
        with urllib.request.urlopen(url) as request:
            response = request.read().decode("utf-8")
            return response

    def get(self, query, number):
        url = self.build_url(query, number)
        return self.do_request(url)


def main():
    if len(sys.argv) < 3:
        sys.exit("not enough arguments")
    number = sys.argv[1]
    query = sys.argv[2]
    numbers_api = NumbersApi()
    trivia = numbers_api.get(query, number)
    print(trivia)



if __name__ == "__main__":
    main()
