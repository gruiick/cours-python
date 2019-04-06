import abc
import hashlib
import json
import shutil
import time
import urllib.parse
import urllib.request
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

    def make_request(self, query):
        params = self.auth.generate_params()
        params.update(query.params())
        url = Client.base_url + query.path()
        url_query = urllib.parse.urlencode(params)
        full_url = url + "?" + url_query
       	with urllib.request.urlopen(full_url) as response:
            status_code = response.getcode()
            if status_code != 200:
                sys.exit("got status: " + str(status_code))
            body = json.loads(response.read())
        attribution = body["attributionText"]
        response = query.extract(body)
        return (response, attribution)


class Display:
    def __init__(self, width=80):
        self.width = width

    def display(self, text):
        print("\n".join(textwrap.wrap(text, width=self.width)))


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

    @abc.abstractmethod
    def text(self, response):
        pass


class CharacterDescription(Query):

    def __init__(self, name):
        self.name = name

    def get_character_description(self, name):
        params = {"name": name}
        body, attribution = self.make_request("/characters",
                                              params)
        first_result = body["data"]["results"][0]
        description = first_result["description"]
        return (description, attribution)

    def params(self):
        return {"name": self.name}

    def path(self):
        return "/characters"

    def extract(self, body):
        first_result = body["data"]["results"][0]
        description = first_result["description"]
        return description

    def text(self, response):
        return response


class CreatorNumberOfSeries(Query):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_number_of_series(self, first_name, last_name):
        params = {
            "firstName": first_name,
            "lastName": last_name,
        }
        body, attribution = self.make_request("/creators",
                                              params)
        first_result = body["data"]["results"][0]
        return (first_result["series"]["available"], attribution)

    def params(self):
        return { "firstName": self.first_name, "lastName": self.last_name }

    def path(self):
        return "/creators"

    def extract(self, body):
        first_result = body["data"]["results"][0]
        return first_result["series"]["available"]

    def text(self, response):
        return "{} {} worked on {} series".format(
        	self.first_name,
        	self.last_name,
                response
    	)



def main():
    auth = Authorization("api-keys.txt")

    query_type = sys.argv[1]
    if query_type == "character-description":
        name = sys.argv[2]
        query = CharacterDescription(name)

    elif query_type == "creator-number-of-series":
        first_name = sys.argv[2]
        last_name = sys.argv[3]
        query = CreatorNumberOfSeries(first_name, last_name)
    else:
        sys.exit("Unkwnon query type: {}".format(query_type))

    client = Client(auth)
    response,attribution = client.make_request(query)
    text = query.text(response)

    terminal_size = shutil.get_terminal_size()
    columns = terminal_size.columns
    terminal = Display(width=columns)

    terminal.display(text)
    terminal.display("---")
    terminal.display(attribution)


if __name__ == "__main__":
    main()
