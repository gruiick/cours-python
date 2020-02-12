import sys
import subprocess


def main():
    dev = "--dev" in sys.argv
    if dev:
        program = "sphinx-autobuild"
    else:
        program = "sphinx-build"
    cmd = [program, "-d", "build", "-b", "html", "source", "build/html"]
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
