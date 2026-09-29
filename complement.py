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

    reverse_complement_sequence = complement_sequence[::-1]

    return reverse_complement_sequence
