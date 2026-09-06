# look_at_one_read.py
# Take the very first read from the real file and show
# every base next to its quality letter and its quality number.

with open("real_reads.fastq") as f:
    header = f.readline().strip()
    sequence = f.readline().strip()
    plus = f.readline().strip()
    quality = f.readline().strip()

print("header:", header)
print("bases in this read:", len(sequence))
print("quality letters in this read:", len(quality))
print()
print("position, base, letter, score")

for i in range(len(sequence)):
    base = sequence[i]
    letter = quality[i]
    score = ord(letter) - 33
    print(i + 1, base, letter, score)
