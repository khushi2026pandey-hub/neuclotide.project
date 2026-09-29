# Nucleotide Frequency and Reverse Complement Generator

## 1. Problem Statement

DNA is made up of four types of nucleotides: **Adenine (A), Thymine (T), Cytosine (C), and Guanine (G)**.

When working with a DNA sequence, it is useful to determine how many times each nucleotide occurs and to find the reverse complement of the sequence. Doing these calculations manually can be time-consuming and may result in errors.

The purpose of this project is to develop a simple Python program that accepts a DNA sequence from the user, checks whether the sequence is valid, counts the frequency of each nucleotide, and generates the reverse complement of the DNA sequence.

The project provides a basic introduction to DNA sequence processing using Python programming concepts.

---

## 2. Scope of the Project

The scope of this project is limited to basic DNA sequence analysis.

The project includes the following operations:

* Accepting a DNA sequence from the user.
* Converting lowercase letters into uppercase letters.
* Checking whether the DNA sequence contains only valid nucleotides.
* Counting the occurrences of Adenine (A), Thymine (T), Cytosine (C), and Guanine (G).
* Generating the complementary sequence.
* Reversing the complementary sequence to obtain the reverse complement.
* Displaying the results to the user.
* Displaying an error message when an invalid DNA sequence is entered.

This project is intended for **educational and basic sequence-processing purposes**. It does not perform advanced biological, medical, or clinical analysis.

---

## 3. Target Users

The project is mainly intended for:

* **First-year computer science students** learning Python.
* **Biology and biotechnology students** learning basic DNA concepts.
* **Beginners in bioinformatics** interested in DNA sequence processing.
* **Students working on introductory Python mini-projects.**
* **Teachers and instructors** who want to demonstrate Python programming using a real-world example.

---

## 4. High-Level Features

### 4.1 DNA Sequence Input

The program allows the user to enter a DNA sequence using the keyboard.

Example:

```text
ATGCGTAA
```

---

### 4.2 Input Validation

The program checks whether the entered sequence contains only the four valid DNA nucleotides:

```text
A - Adenine
T - Thymine
C - Cytosine
G - Guanine
```

If an invalid character is entered, the program displays:

```text
Invalid DNA sequence!
Please enter only A, T, C and G.
```

---

### 4.3 Nucleotide Frequency Calculation

The program counts the exact number of occurrences of each nucleotide in the DNA sequence.

For example, for:

```text
ATGCGTAA
```

the frequency is:

```text
Adenine (A)  : 3
Thymine (T)  : 2
Cytosine (C) : 1
Guanine (G)  : 2
```

---

### 4.4 Reverse Complement Generation

The program generates the reverse complement of the DNA sequence using the following complementary base pairs:

Nucleotide	Complement
A	T
T	A
C	G
G	C

For example:

Original DNA:       ATGC
Complement:         TACG
Reverse Complement: GCAT

The program uses Python string slicing:

[::-1]

to reverse the complementary sequence.

4.5 Uppercase Conversion

The program automatically converts lowercase input into uppercase using:

sequence = sequence.upper()

For example:

Input:  atgc
Output: ATGC

This makes the program easier to use and ensures consistent processing.

4.6 User-Friendly Output

The program displays the results in a simple and organized format, including:

Original DNA sequence
Frequency of A
Frequency of T
Frequency of C
Frequency of G
Reverse complement
5. Project Objective

The main objective of this project is to develop a simple Python program for basic DNA sequence analysis while practicing fundamental programming concepts.

The project helps students understand:

Strings
Dictionaries
Functions
for loops
if-else statements
Input validation
String methods
String slicing
Basic algorithm design
6. Expected Outcome

After entering a valid DNA sequence, the program should:

Display the original DNA sequence.
Calculate and display the frequency of A, T, C, and G.
Generate and display the reverse complement.
Display an appropriate error message if the DNA sequence is invalid.

For example:

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
7. Conclusion

The Nucleotide Frequency and Reverse Complement Generator is a beginner-friendly Python project that combines basic programming concepts with a simple biological application.

It provides an easy way to validate DNA sequences, count nucleotide frequencies, and generate reverse complements. The project is suitable for a First Year, First Semester Python programming project and provides a foundation for learning more advanced bioinformatics applications in the future.
