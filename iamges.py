from pathlib import Path
from PIL import Image
from Evn import DirCategory


class Iamges:
    @staticmethod
    def get_list(path) -> list[tuple[Path, str]]:
        images = Path(path).glob("*.*")
        image_extensions = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff"}
        return [
            (img, img.name) for img in images if img.is_file() and img.suffix.lower() in image_extensions
        ]

    @staticmethod
    def filtered_images(
        image_list: list[tuple[Path, str]], category: DirCategory
    ) -> list[tuple[Path, str]]:
        Image.MAX_IMAGE_PIXELS = None

        category_config = {
            DirCategory.GoodQuality_Square: {
                "min_w": 1000,
                "min_h": 1000,
                "min_ratio": 1,
                "max_ratio": 1,
            },
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
            DirCategory.BadQuality_Square: {
                "min_w": 0,
                "min_h": 0,
                "min_ratio": 1,
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
        }

        # Get the configuration for the specified category
        config = category_config[category]
        min_w, min_h = config["min_w"], config["min_h"]
        min_ratio, max_ratio = config["min_ratio"], config["max_ratio"]

        return [
            (image_path, img_name)
            for image_path, img_name in image_list
            if Iamges._is_image_valid(image_path, min_w, min_h, min_ratio, max_ratio)
        ]

    @staticmethod
    def _is_image_valid(
        image_path: Path,
        min_w: int,
        min_h: int,
        min_ratio: float,
        max_ratio: float,
    ) -> bool:
        if image_path.is_file():
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
                        color = "\033[31minvalid\033[0m"

                    print(
                        f"wh|r{width}, {height} | {ratio} |\
                                \n\tValid: \
                                \n\t\t{cond1},\
                                \n\t\t{cond2},\
                                \n\t\t{cond3}\
                                \n\t\t\t\t{color}"
                    )

                    return cond1 and cond2 and cond3
            except Exception as e:
                print(f"Error occurred while processing image {image_path}: {e}")

                return False
        return False
