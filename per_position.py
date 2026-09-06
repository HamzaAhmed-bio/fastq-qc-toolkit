handle = open("real_reads.fastq")
lines = handle.read().splitlines()
handle.close()

qual_lines = []
for i in range(0, len(lines), 4):
    qual_lines.append(lines[i + 3])

read_length = len(qual_lines[0])

for position in range(read_length):
    scores = []
    for qual_line in qual_lines:
        letter = qual_line[position]
        scores.append(ord(letter) - 33)

    average = sum(scores) / len(scores)

    bar = "#" * int(average)
    print(position + 1, round(average, 1), bar)
