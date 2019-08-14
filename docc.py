import argparse
import ast
import logging
from os import walk
from pathlib import Path
from sys import argv, exit

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

NAUGHTY_BOYS = {".git", "venv", "__pycache__"}  # Exluded dirs


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Doc generators are shit, use this, it isn't."
    )

    parser.add_argument(
        "--dir", type=Path, help="If you need to specify a spicy dir"
    )

    parser.add_argument(
        "--excludes",
        type=str,
        help="do,it,like,this,it,can,be,a,dir,or,a,file",
    )

    subparsers = parser.add_subparsers(dest="cmd")

    fucc_yu = subparsers.add_parser("fuckyou", aliases=["fu"], help="No")
    fucc_yu.set_defaults(cmd=fuckyou)

    return parser.parse_args()


def fuckyou(args: argparse.Namespace):
    print("No, fuck YOU")


def read_functions(functions, f, starter="Function"):
    for function in functions:
        f.write(f"#### {starter}: {function.name}\n\n")
        docstring = ast.get_docstring(function)
        if docstring is not None:
            f.write(f"```\n{ast.get_docstring(function)}\n```\n\n")


def read_classes(classes):
    f = open("doc.md", "a+")
    for class_ in classes:
        methods = [n for n in class_.body if isinstance(n, ast.FunctionDef)]
        f.write(f"### {class_.name}\n\n")
        docstring = ast.get_docstring(class_)
        if docstring is not None:
            f.write(f"```\n{ast.get_docstring(class_)}\n```\n\n")
        read_functions(methods, f, "Method")


def get_info(node):
    functions = [n for n in node.body if isinstance(n, ast.FunctionDef)]
    classes = [n for n in node.body if isinstance(n, ast.ClassDef)]

    f = open("doc.md", "a+")
    read_functions(functions, f)
    f.close()
    read_classes(classes)
    f.close()


def read_dir(dir_name: str):
    global NAUGHTY_BOYS

    for dir_name, sub_dirs, file_list in walk(dir_name):
        if not any(x in dir_name for x in NAUGHTY_BOYS):
            LOGGER.info(f"Found directory: {dir_name}")
            for f_name in file_list:
                if (
                    f_name.endswith(".py")
                    and not f_name.startswith("_")
                    and not any(x in f_name for x in NAUGHTY_BOYS)
                ):
                    f = open("doc.md", "a+")
                    f.write(f"## {f_name}\n")
                    f_name = f"{dir_name}/{f_name}"
                    LOGGER.info(f"\t\tFound file: {f_name}")
                    with open(f_name) as f:
                        get_info(ast.parse(f.read()))


def read_modules(source_dir: str):
    return read_dir(source_dir)


def main():
    args = parse_args()

    if len(argv) < 2:
        print("Invalid ops specified, use --help if you're stuck")
        return

    LOGGER.info("Creating new doc file")
    open("doc.md", "a").close()

    if args.excludes:
        ls = [value for value in args.excludes.split(",") if value is not None]
        NAUGHTY_BOYS.update(ls)

    if args.cmd:
        return args.cmd(args)

    default_dir = Path.cwd() / argv[1]
    if args.dir:
        default_dir = args.dir

        return read_modules(default_dir)

    return read_modules(default_dir)


if __name__ == "__main__":
    exit(0 if main() else 1)
