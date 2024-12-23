from enum import Enum


class DirCategory(Enum):
    GoodQuality_Landscape = 1
    GoodQuality_Portrait = 2
    BadQuality_Landscape = 3
    BadQuality_Portrait = 4
    Video = 4
