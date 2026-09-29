def count_nucleotides(sequence):
    count = {
        "A": 0,
        "T": 0,
        "C": 0,
        "G": 0
    }

    for base in sequence:
        count[base] += 1

    return count
