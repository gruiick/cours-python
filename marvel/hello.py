import hashlib
import requests
import shutil
import time
import textwrap


def main():
    # Read api keys from the text file
    with open("api-keys.txt", "r") as file:
        lines = file.readlines()
    assert len(lines) == 2, "Incorrect api-keys file"
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


    # Other parameters:
    name = "Spider-Man"
    params["name"]  = name


    # Perform the request
    url = base_url + "/characters"
    response = requests.get(url, params=params)
    status_code = response.status_code
    assert status_code == 200, "got status: " + str(status_code)
    body = response.json()
    description = body["data"]["results"][0]["description"]

    # Print the description
    terminal_size = shutil.get_terminal_size()
    columns = terminal_size.columns
    print("\n".join(textwrap.wrap(description, width=columns)))


if __name__ == "__main__":
    main()
