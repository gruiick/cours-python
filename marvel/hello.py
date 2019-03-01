import hashlib
import requests
import time


def main():
    with open("api-keys", "r") as file:
        lines = file.readlines()
    assert len(lines) == 2, "Incorrect api-keys file"
    public_key = lines[0].strip()
    private_key = lines[1].strip()


    url = "http://gateway.marvel.com/v1/public/comics"
    params = dict()
    params["apikey"] = public_key
    ts = str(time.time())
    to_hash = ts + private_key + public_key
    hasher = hashlib.md5()
    hasher.update(to_hash.encode())
    digest = hasher.hexdigest()
    params["ts"] = ts
    params["hash"] = digest
    response = requests.get(url, params=params)
    print(response.status_code)
    print(response.text)


if __name__ == "__main__":
    main()
