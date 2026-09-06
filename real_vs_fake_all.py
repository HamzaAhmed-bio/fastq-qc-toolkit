# real_vs_fake_all.py
# Across all 20000 reads, sort every single base into two buckets
# based on whether the machine was sure about that base.

sure = {"A": 0, "C": 0, "G": 0, "T": 0, "N": 0}
gave_up = {"A": 0, "C": 0, "G": 0, "T": 0, "N": 0}

with open("trimmed_real.fastq") as f:
    while True:
        header = f.readline()
        if header == "":
            break
        sequence = f.readline().strip()
        plus = f.readline()
        quality = f.readline().strip()

        for i in range(len(sequence)):
            base = sequence[i]
            score = ord(quality[i]) - 33
            if score == 2:
                gave_up[base] = gave_up[base] + 1
            else:
                sure[base] = sure[base] + 1

def show(bucket, label):
    total = 0
    for base in bucket:
        total = total + bucket[base]

    print(label)
    print("   ", total, "bases")
    for base in "ACGTN":
        percent = bucket[base] / total * 100
        print("   ", base, bucket[base], "=", round(percent, 1), "%")
    gc = (bucket["G"] + bucket["C"]) / total * 100
    print("    GC =", round(gc, 1), "%")
    print()

show(sure, "SURE (quality above 2)")
show(gave_up, "GAVE UP (quality exactly 2)")
