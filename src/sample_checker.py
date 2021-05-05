from pathlib import Path
import subprocess
from subprocess import TimeoutExpired, CalledProcessError


def is_number(x) -> bool:
    try:
        float(x)
        return True
    except ValueError:
        return False


def is_close(x: float, y: float, tol: float) -> bool:
    if abs(x - y) < tol:
        return True
    if abs(x - y) / max(abs(x), abs(y)) < tol:
        return True
    return False


def show_details(number: int) -> None:
    print("NG")
    print("Input : ")
    print(Path(f"sample/input{number}.txt").read_text())
    print("Expected : ")
    print(Path(f"sample/output{number}.txt").read_text())
    print("Found : ")
    print(Path(f"sample/answer{number}.txt").read_text())


def check_sample() -> None:
    task_id: str = str(Path.cwd()).split("/")[-1]
    number: int = 1
    passed_all_samples: bool = True
    flag_float: bool = Path("allowable_error.txt").exists()
    while Path(f"sample/input{number}.txt").exists():
        print(f"Sample{number}... ", end="")
        try:
            subprocess.run(f"./task{task_id}", check=True, stdin=Path(f"sample/input{number}.txt").open(
                "r"), stdout=Path(f"sample/answer{number}.txt").open("w"), timeout=3.0)
        except TimeoutExpired:
            print("TLE")
            number += 1
            continue
        except CalledProcessError:
            print("RE")
            number += 1
            continue
        expected: list[str] = Path(
            f"sample/output{number}.txt").read_text().strip().splitlines()
        answer: list[str] = Path(
            f"sample/answer{number}.txt").read_text().strip().splitlines()
        if flag_float:
            tolerance: float = pow(
                10, int(Path("allowable_error.txt").read_text()))
            passed_sample = True
            for line_expected, line_answer in zip(expected, answer):
                for element_expected, element_answer in zip(line_expected.split(), line_answer.split()):
                    if is_number(element_expected) and is_number(element_answer):
                        if not is_close(float(element_expected), float(element_answer), tolerance):
                            passed_sample = passed_all_samples = False
                    else:
                        if element_expected != element_answer:
                            passed_sample = passed_all_samples = False
        else:
            passed_sample = True
            for line_expected, line_answer in zip(expected, answer):
                if line_expected.strip().split() != line_answer.strip().split():
                    passed_sample = passed_all_samples = False
        print("OK") if passed_sample else show_details(number)
        number += 1
    if passed_all_samples:
        print(f"Passed all sample cases!")


if __name__ == "__main__":
    check_sample()
