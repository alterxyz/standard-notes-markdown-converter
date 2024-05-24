# Local Standard Notes to Markdown (Obsidian) Converter

A Python tool that converts your Standard Notes exports for seamless integration with Obsidian. Accurately migrates notes, preserving metadata as YAML frontmatter for optimal compatibility with Obsidian's tagging and organizational features.
Additionally, it enhances filename compatibility by utilizing full-width characters, ensuring accurate local storage while preserving visual clarity.

这款 Python 工具可以转换你的 Standard Notes 导出数据，实现与 Obsidian 的无缝衔接。它能精确迁移笔记内容，并将元数据保存为 YAML frontmatter，以确保与 Obsidian 的标签和组织功能完全兼容。 此外，该工具还通过使用全角字符增强了文件名的兼容性，确保在本地存储时文件名准确无误，同时保留视觉上的清晰度。

## Prerequisites

* Python 3.10 or higher
* Standard Notes account with exported data

## Usage

1. **Export your Standard Notes data:**
   * Go to Standard Notes and choose the "Export" option.
   * Select "Download as decrypted import file". You'll receive a single `.txt` file containing all your notes.

2. **Place the exported `.txt` file in the same directory as the script.**

3. **(Optional) Modify the script arguments:**
   * Open `main.py` in a text editor.
   * Adjust the default values for `--input`, `--output`, and `--final` if needed. These arguments control the input file path, the intermediate folder for processed notes, and the final folder for renamed notes, respectively.

4. **Run the script:**
   * Open a terminal or command prompt.
   * Navigate to the directory containing the script and the exported `.txt` file.
   * Execute the following command:

     ```bash
     python3 main.py
     ```

   * You can also run the script with custom arguments:

     ```bash
     python3 main.py --input <path_to_input.txt> --output <path_to_intermediate_folder> --final <path_to_final_folder>
     ```

## Script Details

The script performs the following steps:

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

* The `tag.py` script is assumed to be in the same directory as `main.py` and `rename.py`.  You can adjust the script path in `main.py` if needed.
* The script handles potential errors and logs them to `error.log`.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
