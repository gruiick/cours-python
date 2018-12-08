import sys
import os
import subprocess


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: build.py NUMBER")

    number = sys.argv[1]

    os.makedirs("build", exist_ok=True)
    cmd = []
    if sys.platform == "darwin":
        # From mactex
        cmd.append("texi2pdf")
    else:
        cmd.append("pdflatex")
    cmd.append(f"../python-{number}.tex")
    subprocess.run(cmd, cwd="build", check=True)


if __name__ == "__main__":
    main()
