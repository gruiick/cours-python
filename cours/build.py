import os
import sys
import shutil
import subprocess


def main():
    dev = "--dev" in sys.argv
    werror = "--werror" in sys.argv
    clean = "--clean" in sys.argv
    if dev:
        program = "sphinx-autobuild"
    else:
        program = "sphinx-build"
    opts = []
    if clean:
        if os.path.exists("build"):
            shutil.rmtree("build")
    if werror:
        opts.append("-W")
    cmd = [program, *opts, "-d", "build", "-b", "html", "source", "build/html"]
    print("$", *cmd)
    process = subprocess.run(cmd)
    if process.returncode != 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
