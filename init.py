import os
import json
import argparse
import logging

logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def write_note_to_file(note, folder):
    try:
        filename = os.path.join(folder, f"{note['uuid']}.md")
        os.makedirs(folder, exist_ok=True)
        with open(filename, "w", encoding="utf-8") as file:
            file.write("---\n")
            file.write(f"title: {note['content']['title']}\n")
            file.write(f"uuid: {note['uuid']}\n")
            file.write("standardNotes: true\n")
            file.write(
                f"snType: {note['content'].get('noteType', 'unknown')}\n"
            )  # use .get() and default unknown
            file.write(f"time: {note['created_at']}\n")
            file.write(f"updated: {note['updated_at']}\n")
            file.write("tags:\n")
            file.write("---\n\n")
            file.write(
                f"> Standard_Notes Original Type: {note['content'].get('noteType', 'unknown')}\n\n"
            )
            file.write(note["content"]["text"])
    except Exception as e:
        error_message = f"Error processing note {note.get('uuid', 'unknown')}: {e}"
        print(error_message)
        logging.error(error_message)


def process_notes(data, folder):
    for item in data["items"]:
        if item["content_type"] == "Note":
            write_note_to_file(item, folder)


def main(input_file, output_folder):
    with open(input_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    process_notes(data, output_folder)
    print(f"The notes have been successfully exported to: {output_folder}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Export notes from JSON to markdown files."
    )
    parser.add_argument(
        "--input",
        type=str,
        default="decrypted-sn-data.txt",
        help="Path to the input JSON file",
    )
    parser.add_argument(
        "--output", type=str, default="sn_output", help="Path to the output directory"
    )
    args = parser.parse_args()

    main(args.input, args.output)
