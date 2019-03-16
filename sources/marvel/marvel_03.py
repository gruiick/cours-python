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


class Client:
    base_url = "http://gateway.marvel.com/v1/public"

    def __init__(self, auth):
        self.auth = auth

    def get_character_description(self, name):
        params = self.auth.generate_params()
        params["name"] = name
        url = Client.base_url + "/characters"
        response = requests.get(url, params=params)
        status_code = response.status_code
        if status_code != 200:
            sys.exit("got status: " + str(status_code))
        body = response.json()
        description = body["data"]["results"][0]["description"]
        attribution = body["attributionText"]
        return (description, attribution)


class Display:
    def __init__(self, width=80):
        self.width = width

    def display(self, text):
        print("\n".join(textwrap.wrap(text, width=self.width)))


def main():
    name = sys.argv[1]


    auth = Authorization("api-keys.txt")

    client = Client(auth)
    description, attribution = client.get_character_description(name)

    terminal_size = shutil.get_terminal_size()
    columns = terminal_size.columns
    terminal = Display(width=columns)

    terminal.display(description)
    terminal.display("---")
    terminal.display(attribution)


if __name__ == "__main__":
    main()
