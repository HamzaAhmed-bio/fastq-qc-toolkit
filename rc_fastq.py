def reverse_complement(seq):
    pairs = {"A": "T", "T": "A", "G": "C", "C": "G", "N": "N"}

    result = ""
    for base in seq:
        result = pairs[base] + result

    return result


handle = open("sample.fastq")
lines = handle.read().splitlines()
handle.close()

for i in range(0, len(lines), 4):
    name = lines[i]
    seq = lines[i + 1]

    rc = reverse_complement(seq)

    print(name)
    print("forward:", seq)
    print("reverse:", rc)
    print()
