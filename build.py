import argparse
import os
import sys
import shutil
import subprocess


def run(*cmd, **kwargs):
    print("$", *cmd)
    process = subprocess.run(" ".join(cmd), shell=True, **kwargs)
    if process.returncode != 0:
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dev", action="store_true", help="Run with a live server")
    parser.add_argument(
        "--werror", action="store_true", help="Treat warnings as errors"
    )
    parser.add_argument("--clean", action="store_true", help="Clean first")
    parser.add_argument("--format", help="Output format", default="html")
    args = parser.parse_args()

    dev = args.dev
    werror = args.werror
    clean = "--clean" in sys.argv
    format = args.format
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
    if format == "html":
        builder = "html"
    elif format == "pdf":
        builder = "latex"
    build_path = f"build/{builder}"
    run(program, *opts, "-d", "build", "-b", builder, "source", build_path)
    if format == "pdf":
        run("tectonic", "*.tex", cwd="build/latex")


if __name__ == "__main__":
    main()
