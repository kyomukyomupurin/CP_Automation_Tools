from pathlib import Path
import subprocess


def check_sample():
    subprocess.run(["make", "taskA"])
    number = 1
    while Path(f"input{number}.txt").exists():
        subprocess.run("./taskA", check=True, stdin=Path("input{number}.txt").open("r"), stdout=Path(f"answer{number}.txt").open("w"))
        print("fSample{number}... ", end='')
        if Path(f"output{number}.txt").read_text().strip(" \n") != Path(f"answer{number}.txt").read_text().strip(" \n"):
            print("NG")
            print("Input : ")
            subprocess.run(["cat", f"input{number}.txt"])
            print("Expected : ")
            subprocess.run(["cat", f"output{number}.txt"])
            print("Found : ")
            subprocess.run(["cat", f"answer{number}.txt"])
        else:
            print("OK")
        number += 1

if __name__ == "__main__":
    check_sample()