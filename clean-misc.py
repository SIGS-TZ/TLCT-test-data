from pathlib import Path

for seqDir in Path("./recommend").iterdir():
    if not seqDir.is_dir():
        continue

    for filePath in seqDir.iterdir():
        if filePath.name in ["calib.cfg", "convert.sh"]:
            continue
        filePath.unlink()
