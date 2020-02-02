import argparse
import subprocess
import sys


def build():
    process = subprocess.run(["hugo"])
    if process.returncode != 0:
        sys.exit("build failed")


def deploy(*, dry_run):
    cmd = [
        "rsync",
        "--itemize-changes",
        "--recursive",
        "--delete",
        "public/",
        "dedi3:/srv/nginx/html/books/python/",
    ]
    if dry_run:
        cmd += ["--dry-run"]
    process = subprocess.run(cmd)
    if process.returncode != 0:
        sys.exit("deployment failed")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--dry-run", action="store_true")
    args = parser.parse_args()
    build()
    deploy(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
