def display_frequency(result):
    print("\nNucleotide Frequency:")
    print("Adenine (A)  :", result["A"])
    print("Thymine (T)  :", result["T"])
    print("Cytosine (C) :", result["C"])
    print("Guanine (G)  :", result["G"])


def display_result(sequence, reverse):
    print("\nOriginal DNA Sequence:", sequence)
    print("Reverse Complement:", reverse)
