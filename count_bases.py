handle = open("sample.fastq")
lines = handle.read().splitlines()
handle.close()

all_seq = ""
for i in range(0, len(lines), 4):
    all_seq = all_seq + lines[i + 1]

counts = {}
for base in all_seq:
    if base in counts:
        counts[base] = counts[base] + 1
    else:
        counts[base] = 1

print("total bases:", len(all_seq))

for base in counts:
    print(base, counts[base])

gc = counts.get("G", 0) + counts.get("C", 0)
n_count = counts.get("N", 0)
gc_percent = gc / (len(all_seq) - n_count) * 100
print("GC content:", round(gc_percent, 1), "%")
