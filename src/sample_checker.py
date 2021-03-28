from pathlib import Path
import subprocess
import re


def check_sample() -> None:
    task_id = str(Path.cwd()).split("/")[-1]
    number = 1
    passed = True
    while Path(f"sample/input{number}.txt").exists():
        subprocess.run(f"./task{task_id}", check=True, stdin=Path(
            f"sample/input{number}.txt").open("r"), stdout=Path(f"sample/answer{number}.txt").open("w"))
        print(f"Sample{number}... ", end="")
        if re.sub(" +", " ", Path(f"sample/output{number}.txt").read_text().replace("\n", " ")).strip() != re.sub(" +", " ", Path(f"sample/answer{number}.txt").read_text().replace("\n", " ")).strip():
            print("NG")
            print("Input : ")
            print(Path(f"sample/input{number}.txt").read_text())
            print("Expected : ")
            print(Path(f"sample/output{number}.txt").read_text())
            print("Found : ")
            print(Path(f"sample/answer{number}.txt").read_text())
            passed = False
        else:
            print("OK")
        number += 1
    if passed:
        print("Passed all tests!")


if __name__ == "__main__":
    check_sample()
