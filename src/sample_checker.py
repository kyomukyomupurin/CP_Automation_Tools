from pathlib import Path
import subprocess
import re


def check_sample():
    task_id = Path(".").name
    subprocess.run(["make", f"task{task_id}"])
    number = 1
    passed = True
    while Path(f"input{number}.txt").exists():
        subprocess.run(f"./task{task_id}", check=True, stdin=Path(f"input{number}.txt").open("r"), stdout=Path(f"answer{number}.txt").open("w"))
        print(f"Sample{number}... ", end='')
        if re.sub(" +", ' ', Path(f"output{number}.txt").read_text().replace('\n', ' ')).strip(' ') != re.sub(" +", ' ', Path(f"answer{number}.txt").read_text().replace('\n', ' ')).strip(' '):
            print("NG")
            print("Input : ")
            print(Path(f"input{number}.txt").read_text())
            print("Expected : ")
            print(Path(f"output{number}.txt").read_text())
            print("Found : ")
            print(Path(f"answer{number}.txt").read_text())
            passed = False
        else:
            print("OK")
        number += 1
    if passed:
        print("Passed all tests!")

if __name__ == "__main__":
    check_sample()