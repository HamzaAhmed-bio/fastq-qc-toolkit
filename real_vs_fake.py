# real_vs_fake.py
# Compare the base composition before and after the machine gave up.

with open("real_reads.fastq") as f:
    header = f.readline().strip()
    sequence = f.readline().strip()
    plus = f.readline().strip()
    quality = f.readline().strip()

good_part = sequence[:35]
bad_part = sequence[35:]

def count_bases(piece, label):
    print(label, "-", len(piece), "bases")
    for base in "ACGT":
        number = piece.count(base)
        percent = number / len(piece) * 100
        print("   ", base, number, "=", round(percent), "%")
    print()

count_bases(good_part, "BEFORE position 36 (machine was sure)")
count_bases(bad_part, "AFTER position 36 (machine gave up)")
