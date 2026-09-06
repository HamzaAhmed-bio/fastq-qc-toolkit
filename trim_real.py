# trim_real.py
# Cut every read down to the first 230 bases.

keep = 230
reads = 0

with open("real_reads.fastq") as f:
    with open("trimmed_real.fastq", "w") as out:
        while True:
            header = f.readline()
            if header == "":
                break
            sequence = f.readline().strip()
            plus = f.readline()
            quality = f.readline().strip()

            out.write(header)
            out.write(sequence[:keep] + "\n")
            out.write(plus)
            out.write(quality[:keep] + "\n")

            reads = reads + 1

print("Trimmed", reads, "reads to", keep, "bases each")
