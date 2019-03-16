import abc
import hashlib
import requests
import shutil
import time
import textwrap
import sys


class Authorization:
    def __init__(self, filename):
        with open(filename, "r") as file:
            lines = file.readlines()

        if len(lines) != 2:
            sys.exit("Incorrect api-keys file")

        self.public_key = lines[0].strip()
        self.private_key = lines[1].strip()

    def generate_params(self):
        params = dict()
        params["apikey"] = self.public_key
        ts = str(time.time())
        to_hash = ts + self.private_key + self.public_key
        hasher = hashlib.md5()
        hasher.update(to_hash.encode())
        digest = hasher.hexdigest()
        params["ts"] = ts
        params["hash"] = digest
        return params


class Client():
    base_url = "http://gateway.marvel.com/v1/public"

    def __init__(self, auth):
        self.auth = auth

    def make_request(self, query):
        params = self.auth.generate_params()
        params.update(query.params())
        url = Client.base_url + query.path
        response = requests.get(url, params=params)
        status_code = response.status_code
        if status_code != 200:
            sys.exit("got status: " + str(status_code))
        body = response.json()
        result = query.extract(body)
        return (query.to_text(result), body["attributionText"])


class Query(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def params(self):
        pass

    @abc.abstractmethod
    def path(self):
        pass

    @abc.abstractmethod
    def extract(self, body):
        pass

    def to_text(self, result):
        return result


class CharacterDescription(Query):
    path = "/characters"

    def __init__(self, name):
        self.name = name

    def params(self):
        return { "name": self.name }

    def extract(self, body):
        return body["data"]["results"][0]["description"]


class CreatorNumberOfSeries(Query):
    path = "/creators"

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def params(self):
        return { "firstName": self.first_name, "lastName": self.last_name }

    def extract(self, body):
        return body["data"]["results"][0]["series"]["available"]

    def to_text(self, result):
        return f"{self.first_name} {self.last_name} worked on {result} series"


class Display:
    def __init__(self, width=80):
        self.width = width

    def display(self, text):
        print("\n".join(textwrap.wrap(text, width=self.width)))


def main():

    query_type = sys.argv[1]
    if query_type == "character-description":
        name = sys.argv[2]
        query = CharacterDescription(name)
    elif query_type == "creator-number-of-series":
        first_name = sys.argv[2]
        last_name = sys.argv[3]
        query = CreatorNumberOfSeries(first_name, last_name)

    auth = Authorization("api-keys.txt")
    client = Client(auth)
    text, attribution = client.make_request(query)

    terminal_size = shutil.get_terminal_size()
    columns = terminal_size.columns
    terminal = Display(width=columns)

    terminal.display(text)
    terminal.display("---")
    terminal.display(attribution)


if __name__ == "__main__":
    main()
