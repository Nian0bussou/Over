from enum import Enum


class DirCategory(Enum):
    GoodQuality_Landscape = 1
    GoodQuality_Portrait = 2
    BadQuality_Landscape = 3
    BadQuality_Portrait = 4
    GoodQuality_Square = 5
    BadQuality_Square = 6
