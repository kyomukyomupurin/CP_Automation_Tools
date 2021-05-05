class Color:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    DEFAULT = "\033[0m"


def print_ok(s: str) -> None:
    print(f"{Color.GREEN}{s}{Color.DEFAULT}")


def print_ng(s: str) -> None:
    print(f"{Color.YELLOW}{s}{Color.DEFAULT}")
