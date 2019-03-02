import hashlib
import requests
import shutil
import time
import textwrap
import sys


def main():
    # Get name from command line
    name = sys.argv[1]

    # Read api keys from the text file
    with open("api-keys.txt", "r") as file:
        lines = file.readlines()

    if len(lines) != 2:
        sys.exit("Incorrect api-keys file")

    public_key = lines[0].strip()
    private_key = lines[1].strip()


    # base url
    base_url = "http://gateway.marvel.com/v1/public"

    # Authorizsation stuff
    params = dict()
    params["apikey"] = public_key
    ts = str(time.time())
    to_hash = ts + private_key + public_key
    hasher = hashlib.md5()
    hasher.update(to_hash.encode())
    digest = hasher.hexdigest()
    params["ts"] = ts
    params["hash"] = digest


    # Perform the request
    params["name"]  = name
    url = base_url + "/characters"
    response = requests.get(url, params=params)
    status_code = response.status_code
    if status_code != 200:
        sys.exit("got status: " + str(status_code))
    body = response.json()

    description = body["data"]["results"][0]["description"]

    # Print the description
    terminal_size = shutil.get_terminal_size()
    columns = terminal_size.columns
    print("\n".join(textwrap.wrap(description, width=columns)))

    # Print attribution (comply with API agreement)
    print("---")
    print(body["attributionText"])


if __name__ == "__main__":
    main()
