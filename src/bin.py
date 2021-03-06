import base64
from pathlib import Path
import sys
import argparse
import zlib
import logging


if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="build target")
    args = parser.parse_args()
    src: str = args.target
    stem: str = Path(src).stem
    binary: str = str(base64.b85encode(zlib.compress(
        Path(stem).read_bytes())), encoding="utf-8")
    directory_path: list[str] = str(Path.cwd()).split("/")
    contest, task_id = directory_path[-2], directory_path[-1]
    Path(f"{stem}.py").write_text("# This code is generated and submitted by [CP_Automation_Tools](https://github.com/kyomukyomupurin/CP_Automation_Tools)\n"
                                  "# and [AtCoder_base64](https://github.com/kyomukyomupurin/AtCoder_base64)\n\n"
                                  "import base64\n"
                                  "import subprocess\n"
                                  "from pathlib import Path\n"
                                  "import zlib\n\n\n"
                                  f"binary = \"{binary}\"\n"
                                  "Path(\"kyomu\").write_bytes(zlib.decompress(base64.b85decode(binary)))\n"
                                  "Path(\"kyomu\").chmod(0o755)\n"
                                  "subprocess.run(\"./kyomu\")\n\n"
                                  "# Original source code : \n"
                                  "\"\"\"\n"
                                  f"{Path(src).read_text()}\n"
                                  "\"\"\""
                                  )
    sz: int = sys.getsizeof(Path(f"{stem}.py").read_text())
    logging.info(" The size of %s.py is %.1f KB, %.1f %% of limit. ",
                 stem, sz / 1000, sz / 5120)
