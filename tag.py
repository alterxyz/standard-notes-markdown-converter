import os
import json
import argparse
from collections import defaultdict, deque


def load_data(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)["items"]


def extract_tags_and_hierarchy(items):
    tags = {}
    child_to_parents = defaultdict(list)
    note_tags = defaultdict(list)

    for item in items:
        if item["content_type"] == "Tag":
            tag_id = item["uuid"]
            tags[tag_id] = item["content"]["title"]
            for ref in item["content"]["references"]:
                if ref["content_type"] == "Note":
                    note_tags[ref["uuid"]].append(tag_id)
                elif ref["content_type"] == "Tag":
                    child_to_parents[tag_id].append(ref["uuid"])

    # Resolve tag hierarchy to get full tag paths
    full_tag_paths = {}
    for tag_id, title in tags.items():
        path = [title]
        current = tag_id
        while current in child_to_parents:
            parent_id = child_to_parents[current][
                0
            ]  # Assuming only one parent for simplicity
            current = parent_id
            path.append(tags[current])
        full_tag_paths[tag_id] = "/".join(reversed(path))

    return note_tags, full_tag_paths


def add_tags_to_notes(note_tags, tag_paths, output_folder):
    for note_id, tag_ids in note_tags.items():
        filename = f"{note_id}.md"
        filepath = os.path.join(output_folder, filename)
        if os.path.exists(filepath):
            new_lines = []
            with open(filepath, "r", encoding="utf-8") as file:
                lines = file.readlines()
                tag_inserted = False
                for line in lines:
                    if line.strip() == "tags:" and not tag_inserted:
                        # Add tags right after "tags:"
                        new_lines.append(line)
                        for tag_id in tag_ids:
                            new_lines.append("  - " + tag_paths[tag_id] + "\n")
                        tag_inserted = True
                    else:
                        new_lines.append(line)
            with open(filepath, "w", encoding="utf-8") as file:
                file.writelines(new_lines)


def main(input_file, output_folder):
    items = load_data(input_file)
    note_tags, tag_paths = extract_tags_and_hierarchy(items)
    add_tags_to_notes(note_tags, tag_paths, output_folder)
    print("Tags have been added to markdown files in the folder:", output_folder)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Add tags to markdown files and organize files based on tags."
    )
    parser.add_argument(
        "--input",
        type=str,
        default="decrypted-sn-data.txt",
        help="Path to the JSON file containing the notes and tags",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="sn_output",
        help="Path to the output folder where markdown files are stored",
    )
    args = parser.parse_args()

    main(args.input, args.output)
