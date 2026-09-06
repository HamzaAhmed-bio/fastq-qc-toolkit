handle = open("sample.fastq")
lines = handle.read().splitlines()
handle.close()

for i in range(0, len(lines), 4):
    name = lines[i]
    qual_line = lines[i + 3]

    scores = []
    for letter in qual_line:
        scores.append(ord(letter) - 33)

    average = sum(scores) / len(scores)

    print(name, "average quality:", round(average, 1))
