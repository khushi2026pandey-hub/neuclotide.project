def count_nucleotides(sequence):
    count = {
        "A": 0,
        "T": 0,
        "C": 0,
        "G": 0
    }

    for base in sequence:
        if base in count:
            count[base] += 1
        else:
            print("Invalid nucleotide found:", base)

    return count


def reverse_complement(sequence):
    complement = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    complement_sequence = ""

    for base in sequence:
        complement_sequence += complement[base]

    # Reverse the complement sequence
    reverse_complement_sequence = complement_sequence[::-1]

    return reverse_complement_sequence


print("==============================================")
print(" NUCLEOTIDE FREQUENCY AND REVERSE COMPLEMENT")
print("==============================================")

sequence = input("Enter a DNA sequence: ")

sequence = sequence.upper()

valid = True

for base in sequence:
    if base not in "ATCG":
        valid = False
        break

if valid:

    print("\nOriginal DNA Sequence:", sequence)

    # Count nucleotides
    result = count_nucleotides(sequence)

    print("\nNucleotide Frequency:")
    print("Adenine (A)  :", result["A"])
    print("Thymine (T)  :", result["T"])
    print("Cytosine (C) :", result["C"])
    print("Guanine (G)  :", result["G"])

    reverse = reverse_complement(sequence)

    print("\nReverse Complement:", reverse)

else:
    print("\nInvalid DNA sequence!")
    print("Please enter only A, T, C and G.")

print("\nProgram completed.")
