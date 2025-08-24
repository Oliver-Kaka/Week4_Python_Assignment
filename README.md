# File Handling & Error Management in Python

## Overview
This project demonstrates basic **file handling** and **error management** in Python.  
It covers two main tasks:
1. Reading from a file and writing a modified version to a new file.
2. Handling errors gracefully when reading user-specified files.

---

## Features
### 1. File Read & Write Challenge 🖋️
- Reads content from `File.txt`.
- Creates a new file `newFile.txt`.
- Adds a header line:  
  `"This file is a modified version of File.txt."`
- Converts all text to **uppercase** before saving.

### 2. Error Handling Lab 🧪
- Prompts the user to enter a filename.
- Handles the following errors:
  - **FileNotFoundError** → When the file does not exist.
  - **PermissionError** → When the program lacks permission to read the file.
- Prints the file content if no errors occur.

---

## Usage
1. Place a text file named **`File.txt`** in the same directory as the script.
2. Run the Python script:
   ```bash
   python program.py
3. A new file named **`newFile.txt`** will be created/overwritten with modified content.
4. When prompted, enter the name of a file you want to open:

   ```text
   Enter a file name: newFile.txt
   ```

---

## Example Output

```
This file is a modified version of File.txt.
HELLO THERE, THIS IS THE ORIGINAL FILE. 
IT IS TO BE MODIFIED TO UPPERCASE AND STORED IN THE FILE NAMED NEWFILE.PDF
```

If the user enters a missing file:

```
Enter a file name: missing.txt
The file does not exist.
```

---

## Requirements

* Python 3.x
* A text file named `File.txt` (with some sample text).

---

## Author

* **Oliver Kaka Maganga**
* Aspiring Software Engineer | Python & Cloud Enthusiast
