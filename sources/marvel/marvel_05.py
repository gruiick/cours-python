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


class InformationRetriever:
    base_url = "http://gateway.marvel.com/v1/public"

    def __init__(self, auth):
        self.auth = auth

    def make_request(self, path, query_params):
        params = self.auth.generate_params()
        params.update(query_params)
        url = InformationRetriever.base_url + path
        response = requests.get(url, params=params)
        status_code = response.status_code
        if status_code != 200:
            sys.exit("got status: " + str(status_code))
        body = response.json()
        attribution = body["attributionText"]
        return (body, attribution)


class CharacterDescriptionGetter(InformationRetriever):

    def get_character_description(self, name):
        params = {"name": name}
        body, attribution = self.make_request("/characters", params)
        first_result = body["data"]["results"][0]
        description = first_result["description"]
        return (description, attribution)


class CreatorNumberOfSeriesGetter(InformationRetriever):

    def get_number_of_series(self, first_name, last_name):
        params = {
            "firstName": first_name,
            "lastName": last_name,
        }
        body, attribution = self.make_request("/creators", params)
        first_result = body["data"]["results"][0]
        return (first_result["series"]["available"], attribution)


class Display:
    def __init__(self, width=80):
        self.width = width

    def display(self, text):
        print("\n".join(textwrap.wrap(text, width=self.width)))


def main():
    auth = Authorization("api-keys.txt")

    query = sys.argv[1]
    if query == "character-description":
        name = sys.argv[2]
        character_description_getter = CharacterDescriptionGetter(auth)
        description, attribution = character_description_getter.get_character_description(name)
        text = description
    elif query == "creator-number-of-series":
        first_name = sys.argv[2]
        last_name = sys.argv[3]
        creator_number_of_series_getter = CreatorNumberOfSeriesGetter(auth)
        result, attribution = creator_number_of_series_getter.get_number_of_series(first_name, last_name)
        text = first_name + " " + last_name + " worked on " + str(result) + " series"

    terminal_size = shutil.get_terminal_size()
    columns = terminal_size.columns
    terminal = Display(width=columns)

    terminal.display(text)
    terminal.display("---")
    terminal.display(attribution)


if __name__ == "__main__":
    main()
