import sys
import subprocess


def main():
    dev = "--dev" in sys.argv
    if dev:
        program = "sphinx-autobuild"
        opts = []
    else:
        program = "sphinx-build"
        opts = ["-W"]
    cmd = [program, *opts, "-d", "build", "-b", "html", "source", "build/html"]
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
