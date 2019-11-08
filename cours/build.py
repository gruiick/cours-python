from path import Path
import sys
import subprocess


def main():
    template = Path("build.in.ninja").text()
    to_write = template
    for md_file in Path(".").files("*.md"):
        to_write += f"build {md_file.with_suffix('.pdf')}: pandoc ../{md_file}\n"
    build_path = Path("build")
    build_path.mkdir_p()
    out = build_path / "build.ninja"
    out.write_text(to_write)
    process = subprocess.run(["ninja", "-C", build_path])
    if process.returncode != 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
