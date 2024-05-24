import os
import subprocess
import argparse


def main(input_file, intermediate_folder, final_folder):
    # Step 1: Run init.py to process the initial notes
    print("Running init.py to process initial notes...")
    subprocess.run(
        ["python", "init.py", "--input", input_file, "--output", intermediate_folder],
        check=True,
    )

    # Step 2: Run tag.py to add tags to the notes
    print("Running tag.py to add tags to notes...")
    subprocess.run(
        ["python", "tag.py", "--input", input_file, "--output", intermediate_folder],
        check=True,
    )

    # Step 3: Run rename.py to rename the notes based on their titles
    print("Running rename.py to rename notes...")
    subprocess.run(
        [
            "python",
            "rename.py",
            "--source",
            intermediate_folder,
            "--target",
            final_folder,
        ],
        check=True,
    )

    print("All steps completed successfully!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process notes through all steps: init, tag, rename."
    )
    parser.add_argument(
        "--input",
        type=str,
        default="decrypted-sn-data.txt",
        help="Path to the input JSON file containing the notes and tags",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="sn_output",
        help="Path to the intermediate folder for processed notes",
    )
    parser.add_argument(
        "--final",
        type=str,
        default="sn_renamed_output",
        help="Path to the final folder for renamed notes",
    )
    args = parser.parse_args()

    main(args.input, args.output, args.final)
