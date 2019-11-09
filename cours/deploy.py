import subprocess


def main():
    subprocess.run("rsync --itemize-changes build/*.pdf dedi3:/srv/nginx/e2l/python/", shell=True)


if __name__ == "__main__":
    main()
