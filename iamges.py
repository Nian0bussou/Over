from pathlib import Path
from PIL import Image
from Evn import DirCategory

# sometimes images that are a square are put in the wrong places... no idea what i need to change...
category_config  = {
    DirCategory.GoodQuality_Landscape: {
        "min_w": 1920,
        "min_h": 1080,
        "min_ratio": 1,
        "max_ratio": float("inf"),
    },
    DirCategory.GoodQuality_Portrait: {
        "min_w": 1080,
        "min_h": 1920,
        "min_ratio": float("-inf"),
        "max_ratio": 1,
    },
    DirCategory.BadQuality_Landscape: {
        "min_w": 0,
        "min_h": 0,
        "min_ratio": 1,
        "max_ratio": float("inf"),
    },
    DirCategory.BadQuality_Portrait: {
        "min_w": 0,
        "min_h": 0,
        "min_ratio": float("-inf"),
        "max_ratio": 1,
    },
    DirCategory.Video: {
        "min_w": 0,
        "min_h": 0,
        "min_ratio": float("-inf"),
        "max_ratio": float("inf"),
    },
}

class Iamges:
    @staticmethod
    def get_list(path) -> list[tuple[Path, str]]:
        """
        `tuple[Path, str]` represents:
            `tuple[the path of the file, filename]`
        """
        images = Path(path).glob("*.*")
        image_extensions = {".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".mp4", ".gif"}

        return [
            (img, img.name)
            for img in images
            if img.is_file() and img.suffix.lower() in image_extensions
        ]

    @staticmethod
    def filtered_images(
        image_list: list[tuple[Path, str]], category: DirCategory
    ) -> list[tuple[Path, str]]:
        """
        filter the a list of images (gotten from `get_list`) by the `DirCategory`
        """
        Image.MAX_IMAGE_PIXELS = None

        if category == DirCategory.Video:
            return [
                (image_path, img_name)
                for image_path, img_name in image_list
                if Iamges.is_video(image_path)
            ]


        # not tested yet / return the list of video skipping image checkings

        return [
            (image_path, img_name)
            for image_path, img_name in image_list
            if Iamges.is_image_valid(image_path, category)
        ]

    @staticmethod
    def is_video(image_path: Path) -> bool:
        """
        returns if `image_path` has filetype `.mp4` or `.gif`
        """
        return image_path.is_file() and image_path.suffix.lower() in [".mp4", ".gif"]

    @staticmethod
    def is_image_valid(
        image_path: Path,
        cat: DirCategory,
    ) -> bool:
        config = category_config[cat]
        min_w, min_h = config["min_w"], config["min_h"]
        min_ratio, max_ratio = config["min_ratio"], config["max_ratio"]

        if image_path.is_file():
            if image_path.suffix.lower() in [".mp4", ".gif"]:
                return False
            try:
                with Image.open(image_path) as img:
                    width, height = img.size
                    ratio = width / height

                    cond1 = min_w <= width
                    cond2 = min_h <= height
                    cond3 = min_ratio <= ratio <= max_ratio

                    questionmark3 = cond1 and cond2 and cond3

                    color = ""
                    if questionmark3:
                        color = "\033[32mValid\033[0m"
                    else:
                        color = "\t\033[31minvalid\033[0m"

                    print(
                        f"wh|r\t{width}, \t{height} \t| {ratio} |\
                                \n\t{cat}: \
                                \n\tValid: \
                                \n\t\t{cond1},\
                                \n\t\t{cond2},\
                                \n\t\t{cond3}\
                                \n\t\t\t\t{color}"
                    )

                    return questionmark3
            except Exception as e:
                print(f"Error occurred while processing image {image_path}: {e}")

                return False
        return False
