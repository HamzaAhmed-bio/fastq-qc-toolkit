handle = open("sample.fastq")
lines = handle.read().splitlines()
handle.close()

for i in range(0, len(lines), 4):
    name = lines[i]
    seq = lines[i + 1]

    n_count = seq.count("N")

    if n_count > 0:
        print(name, seq, "FAIL", n_count, "N bases")
    else:
        print(name, seq, "PASS")
