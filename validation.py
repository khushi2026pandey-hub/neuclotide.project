def validate_sequence(sequence):
    for base in sequence:
        if base not in "ATCG":
            return False

    return True
