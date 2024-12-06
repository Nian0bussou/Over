from iamges import Iamges
from moves import Moves
from Evn import DirCategory
import sys

def main():
    args = sys.argv
    if len(args) != 2:
        print("wrong number of args")
        return
    path = args[1]
    imgs = Iamges.get_list(path)
    while len(imgs) > 0: # makes sure no images are left behind
        imgs = Iamges.get_list(path)
        for dcat in DirCategory:
            filtered_imgs = Iamges.filtered_images(imgs, dcat)
            Moves.MovesList(filtered_imgs, path, dcat)
if __name__ == "__main__":
    main()
