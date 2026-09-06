handle = open("sample.fastq")
lines = handle.read().splitlines()
handle.close()

output = open("trimmed.fastq", "w")

for i in range(0, len(lines), 4):
    name = lines[i]
    seq = lines[i + 1]
    plus = lines[i + 2]
    qual = lines[i + 3]

    end = len(seq)
    while end > 0 and ord(qual[end - 1]) - 33 < 30:
        end = end - 1

    new_seq = seq[0:end]
    new_qual = qual[0:end]

    output.write(name + "\n")
    output.write(new_seq + "\n")
    output.write(plus + "\n")
    output.write(new_qual + "\n")

    print(name, "kept", end, "of", len(seq), "bases")

output.close()
print("Saved to trimmed.fastq")
