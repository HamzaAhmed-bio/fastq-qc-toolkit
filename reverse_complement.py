def reverse_complement(seq):
    pairs = {"A": "T", "T": "A", "G": "C", "C": "G", "N": "N"}

    result = ""
    for base in seq:
        result = pairs[base] + result

    return result


print(reverse_complement("GATTACA"))
print(reverse_complement("AAAGGGCCCTTT"))
print(reverse_complement("GATTACAGATTACAGATTNNN"))
