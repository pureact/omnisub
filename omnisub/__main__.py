"""omnisub main."""
import argparse
from pathlib import Path

from omnisub.omnisub.omnisub import omnisub

REQUIRED_ARGS_LENGTH = 3


def get_args() -> argparse.Namespace:
    """Get the command line arguments.

    Returns
    -------
    argparse.Namespace
        The command line arguments.
    """
    args = argparse.ArgumentParser()
    args.add_argument("args", nargs="+")
    return args.parse_args()


def main() -> None:
    """Omnisub main."""
    args = get_args()

    if len(args.args) != REQUIRED_ARGS_LENGTH:
        return

    omnisub(Path(args.args[0]), args.args[1], args.args[2])


if __name__ == "__main__":
    main()
