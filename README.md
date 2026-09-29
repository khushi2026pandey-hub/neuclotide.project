# Nucleotide-Project
# Nucleotide Frequency and Reverse Complement Generator

## 1. Project Title

**Nucleotide Frequency and Reverse Complement Generator**

---

## 2. Overview

The **Nucleotide Frequency and Reverse Complement Generator** is a simple Python-based project that works with DNA sequences.

The project takes a DNA sequence as input and performs two main operations:

1. Counts the number of **Adenine (A), Thymine (T), Cytosine (C), and Guanine (G)** nucleotides.
2. Generates the **reverse complement** of the given DNA sequence.

The project also validates the input and displays an error message if the sequence contains characters other than **A, T, C, or G**.

This project is designed for beginners and demonstrates basic Python programming concepts such as strings, dictionaries, loops, functions, conditions, and string slicing.

---

## 3. Features

* Accepts a DNA sequence from the user.
* Automatically converts lowercase input to uppercase.
* Validates the DNA sequence.
* Counts the frequency of:

  * Adenine (A)
  * Thymine (T)
  * Cytosine (C)
  * Guanine (G)
* Generates the reverse complement of the DNA sequence.
* Displays an error message for invalid DNA sequences.
* Uses Python functions to organize the program.
* Uses string slicing (`[::-1]`) to reverse the sequence.

---

## 4. Technologies and Tools Used

### Programming Language

* **Python 3**

### Python Concepts Used

* Variables
* Strings
* Dictionaries
* `for` loops
* `if-else` statements
* Functions
* String methods
* String slicing
* User input and output

### Tools

* Python IDLE / Visual Studio Code / PyCharm
* Command Prompt or Terminal
* Git and GitHub (optional)

---

## 5. Project Structure

```text
Nucleotide_Project/
│
├── main.py
├── validation.py
├── frequency.py
├── complement.py
├── display.py
└── README.md
```

### File Description

| File            | Description                            |
| --------------- | -------------------------------------- |
| `main.py`       | Main program that controls the project |
| `validation.py` | Validates the DNA sequence             |
| `frequency.py`  | Counts A, T, C and G                   |
| `complement.py` | Generates the reverse complement       |
| `display.py`    | Displays the output                    |
| `README.md`     | Project documentation                  |

---

## 6. Installation and Setup

### Step 1: Install Python

Download and install Python 3 from the official Python website.

Check whether Python is installed by opening Command Prompt or Terminal and running:

```bash
python --version
```

You should see a Python version such as:

```text
Python 3.x.x
```

### Step 2: Download or Clone the Project

Download the project files and place them inside one folder.

For example:

```text
Nucleotide_Project
```

### Step 3: Open the Project

Open the project folder using:

* Visual Studio Code
* PyCharm
* Python IDLE
* Any other Python-supported editor

---

## 7. How to Run the Project

Open the terminal or Command Prompt inside the project folder.

Run:

```bash
python main.py
```

The program will display:

```text
==============================================
 NUCLEOTIDE FREQUENCY AND REVERSE COMPLEMENT
==============================================

Enter a DNA sequence:
```

Enter a DNA sequence such as:

```text
ATGCGTAA
```

---

## 8. Testing Instructions

The project should be tested with both valid and invalid DNA sequences.

### Test Case 1: Valid DNA Sequence

**Input:**

```text
ATGCGTAA
```

**Expected Output:**

```text
Original DNA Sequence: ATGCGTAA

Nucleotide Frequency:
Adenine (A)  : 3
Thymine (T)  : 2
Cytosine (C) : 1
Guanine (G)  : 2

Reverse Complement: TTACGCAT
```

---

### Test Case 2: Lowercase Input

**Input:**

```text
atgc
```

**Expected Output:**

```text
Original DNA Sequence: ATGC
```

The program converts lowercase letters into uppercase automatically.

The reverse complement should be:

```text
GCAT
```

---

### Test Case 3: Invalid Input

**Input:**

```text
ATGX123
```

**Expected Output:**

```text
Invalid DNA sequence!
Please enter only A, T, C and G.
```

---

### Test Case 4: Another Valid Sequence

**Input:**

```text
AATTCCGG
```

**Expected Output:**

```text
Nucleotide Frequency:
Adenine (A)  : 2
Thymine (T)  : 2
Cytosine (C) : 2
Guanine (G)  : 2
```

Reverse complement:

```text
CCGGAATT
```

---

## 9. How the Reverse Complement Works

Each DNA nucleotide has a complementary base:

| Nucleotide | Complement |
| ---------- | ---------- |
| A          | T          |
| T          | A          |
| C          | G          |
| G          | C          |

For example:

```text
Original:       ATGC
Complement:     TACG
Reverse:        GCAT
```

Therefore:

```text
Reverse Complement = GCAT
```

The Python slicing operation:

```python
[::-1]
```

is used to reverse the complementary sequence.

---

## 10. Example Program Output

```text
==============================================
 NUCLEOTIDE FREQUENCY AND REVERSE COMPLEMENT
==============================================

Enter a DNA sequence: ATGCGTAA

Original DNA Sequence: ATGCGTAA

Nucleotide Frequency:
Adenine (A)  : 3
Thymine (T)  : 2
Cytosine (C) : 1
Guanine (G)  : 2

Reverse Complement: TTACGCAT

Program completed.
```

---

## 11. Learning Outcomes

After completing this project, the student will understand:

* How to work with strings in Python.
* How to use dictionaries.
* How to create and call functions.
* How to use loops for processing data.
* How to use conditional statements.
* How to validate user input.
* How to use string slicing.
* How to organize a Python project into multiple files.
* Basic concepts of DNA sequences and complementary bases.

---

## 12. Future Improvements

The project can be improved in the future by adding:

* GC-content calculation.
* DNA sequence length calculation.
* Multiple sequence input.
* Saving results to a text file.
* A graphical user interface (GUI).
* Reading DNA sequences from FASTA files.
* Primer sequence analysis.

---

## 13. Conclusion

The **Nucleotide Frequency and Reverse Complement Generator** is a beginner-friendly Python project that demonstrates fundamental programming concepts while applying them to DNA sequence analysis.

The project successfully counts nucleotide frequencies, validates DNA sequences, and generates the reverse complement of a given sequence. It provides a simple introduction to using Python for basic bioinformatics tasks.
