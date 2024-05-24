import os
import shutil
import argparse
import logging

logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def rename_files(source_folder, target_folder):
    os.makedirs(target_folder, exist_ok=True)
    seen_titles = {}  # store the number of times a title has been seen
    for filename in os.listdir(source_folder):
        if filename.endswith(".md"):
            filepath = os.path.join(source_folder, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as file:
                    lines = file.readlines()
                    title = [
                        line.split(": ")[1].strip()
                        for line in lines
                        if line.startswith("title:")
                    ][0]

                # zh_cn: 使用中文全角字符替换部分标点符号 en_us: Replace some punctuation marks with full-width characters
                char_map = {
                    "?": "？",
                    '"': "＂",
                    ":": "：",
                    "<": "＜",
                    ">": "＞",
                    "|": "｜",
                    "*": "＊",
                    "/": "／",
                    "\\": "＼",
                }
                for char, replacement in char_map.items():
                    title = title.replace(char, replacement)

                # Handle duplicate titles
                if title in seen_titles:
                    seen_titles[title] += 1
                    new_filename = f"{title} ({seen_titles[title]}).md"
                else:
                    seen_titles[title] = 1
                    new_filename = f"{title}.md"

                new_filepath = os.path.join(target_folder, new_filename)

                shutil.copy(filepath, new_filepath)
            except Exception as e:
                error_message = f"Error processing file {filename}: {e}"
                print(error_message)
                logging.error(error_message)


def main(source_folder, target_folder):
    rename_files(source_folder, target_folder)
    print(f"Files have been renamed and copied to: {target_folder}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Rename markdown files based on their titles and copy to a new folder."
    )
    parser.add_argument(
        "--source",
        type=str,
        default="sn_output",
        help="Path to the source folder containing the markdown files",
    )
    parser.add_argument(
        "--target",
        type=str,
        default="sn_renamed_output",
        help="Path to the target folder where renamed files will be stored",
    )
    args = parser.parse_args()

    main(args.source, args.target)
