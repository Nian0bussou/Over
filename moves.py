from datetime import datetime
from pathlib import Path

from PIL.Image import os
from Evn import DirCategory

cat_to_path = {
    DirCategory.GoodQuality_Landscape: "good_landscape",
    DirCategory.GoodQuality_Portrait: "good_portrait",
    DirCategory.BadQuality_Landscape: "bad_landscape",
    DirCategory.BadQuality_Portrait: "bad_portrait",
}


class Moves:
    @staticmethod
    def MovesList(imgs: list[tuple[Path, str]], path: str, category: DirCategory):
        dirName = Path(path + cat_to_path[category])
        dirName.mkdir(exist_ok=True)
        for fpath, fname in imgs:
            print(datetime.now(), " | moving... : ", fname)
            os.rename(str(fpath), dirName.joinpath(fname))
