from Evn import DirCategory
from iamges import Iamges
from moves import Moves
import sys

def main():
    path = sys.argv[1]
    while True:
        imgs = Iamges.get_list(path)
        for dcat in DirCategory:
            filtered_imgs = Iamges.filtered_images(imgs, dcat)
            Moves.MovesList(filtered_imgs, path, dcat)
            imgs = Iamges.get_list(path)
        if not imgs:
            break

if __name__ == "__main__":
    main()
