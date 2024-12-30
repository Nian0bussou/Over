from Evn import DirCategory
from images import Images
from moves import Moves
import sys

def main():
    path = sys.argv[1]
    while True:
        imgs = Images.get_list(path)
        for dcat in DirCategory:
            filtered_imgs = Images.filtered_images(imgs, dcat)
            Moves.MovesList(filtered_imgs, path, dcat)
            imgs = Images.get_list(path)
        if not imgs:
            break

if __name__ == "__main__":
    main()
