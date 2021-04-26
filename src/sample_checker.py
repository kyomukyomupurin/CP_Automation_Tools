from pathlib import Path
import subprocess


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


def check_sample() -> None:
    task_id: str = str(Path.cwd()).split("/")[-1]
    number: int = 1
    passed_all_samples: bool = True
    flag_float = Path("allowable_error.txt").exists()
    while Path(f"sample/input{number}.txt").exists():
        subprocess.run(f"./task{task_id}", check=True, stdin=Path(f"sample/input{number}.txt").open(
            "r"), stdout=Path(f"sample/answer{number}.txt").open("w"))
        expected: list[str] = Path(
            f"sample/output{number}.txt").read_text().strip().splitlines()
        answer: list[str] = Path(
            f"sample/answer{number}.txt").read_text().strip().splitlines()
        print(f"Sample{number}... ", end="")
        flag_continue = True
        if flag_float:
            tolerance: float = pow(
                10, int(Path("allowable_error.txt").read_text()))
            for line_expected, line_answer in zip(expected, answer):
                if not flag_continue:
                    break
                for element_expected, element_answer in zip(line_expected.split(), line_answer.split()):
                    if is_number(element_expected) and is_number(element_answer):
                        if not is_close(float(element_expected), float(element_answer), tolerance):
                            print("NG")
                            print("Input : ")
                            print(
                                Path(f"sample/input{number}.txt").read_text())
                            print("Expected : ")
                            print(
                                Path(f"sample/output{number}.txt").read_text())
                            print("Found : ")
                            print(
                                Path(f"sample/answer{number}.txt").read_text())
                            passed_all_samples = False
                            flag_continue = False
                            break
                    else:
                        if element_expected != element_answer:
                            print("NG")
                            print("Input : ")
                            print(
                                Path(f"sample/input{number}.txt").read_text())
                            print("Expected : ")
                            print(
                                Path(f"sample/output{number}.txt").read_text())
                            print("Found : ")
                            print(
                                Path(f"sample/answer{number}.txt").read_text())
                            passed_all_samples = False
                            flag_continue = False
                            break
            if passed_all_samples:
                print("OK")
        else:
            for line_expected, line_answer in zip(expected, answer):
                if line_expected.strip().split() != line_answer.strip().split():
                    print("NG")
                    print("Input : ")
                    print(Path(f"sample/input{number}.txt").read_text())
                    print("Expected : ")
                    print(Path(f"sample/output{number}.txt").read_text())
                    print("Found : ")
                    print(Path(f"sample/answer{number}.txt").read_text())
                    passed_all_samples = False
                    break
            if passed_all_samples:
                print("OK")
        number += 1
    if passed_all_samples:
        print(f"Passed all sample cases!")


if __name__ == "__main__":
    check_sample()
