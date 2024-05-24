# Local Standard Notes to Markdown Converter

A Python tool that converts Standard Notes exports to markdown files. Accurately migrates notes, preserving metadata as YAML frontmatter for optimal compatibility Obsidian's tagging features.
Additionally, it enhances filename compatibility by utilizing full-width characters(zh_CN.UTF-8), ensuring accurate local storage while preserving visual clarity.

## Prerequisites

* Python 3.10 or higher (lower versions may work but are untested)
* Standard Notes account with exported data

## Usage

1. **Export your Standard Notes data:**
    * Go to Standard Notes and choose the "Export" option.
    * Select "Download as decrypted import file". You'll receive a single `.txt` file containing all your notes.

2. **Place the exported `.txt` file in the same directory as the tool.**

3. **Run the tool:**
    * Open a terminal or command prompt.
    * Navigate to the directory containing the tool and the exported `.txt` file.
    * Execute the following command:

     ```bash
     python3 main.py
     ```

    * The default name for the file is `decrypted-sn-data.txt`, if you have a different name, rename it to `decrypted-sn-data.txt` or specify the file name as an argument.:
  
     ```bash
     python3 main.py --input <path_to_input.txt>
     ```

    * You can also run the tool with custom arguments:

     ```bash
     python3 main.py --input <path_to_input.txt> --output <path_to_intermediate_folder> --final <path_to_final_folder>
     ```

## Tool Details

The tool performs the following steps:

1. **Initialization (`init.py`):**
   * Reads the decrypted Standard Notes export file.
   * Extracts note content, titles, creation dates, and other metadata.
   * Creates Markdown files for each note in the specified intermediate folder.

2. **Tagging (`tag.py`):**
   * Processes the exported data to extract tag information.
   * Adds tags as YAML frontmatter to the corresponding Markdown files.

3. **Renaming (`rename.py`):**
   * Renames the Markdown files based on their titles.
   * Handles duplicate file names by appending a sequence number.
   * Replaces special characters in file names with their full-width counterparts for compatibility.
   * Copies the renamed files to the final output folder.

## Notes

* The `tag.py` tool is assumed to be in the same directory as `main.py` and `rename.py`.  You can adjust the tool path in `main.py` if needed.
* The tool handles potential errors and logs them to `error.log`.

## To Do

* Export only for a specific tag.
* Folder structure based on tags.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
