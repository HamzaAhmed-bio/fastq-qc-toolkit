# get_middle_reads.py
# Same stream as before, but throw away the first 100000 reads
# before keeping 20000. Sampling from the middle of the run.

import urllib.request
import gzip

url = "https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR177/003/SRR1770413/SRR1770413_1.fastq.gz"

skip = 100000
wanted = 20000
skipped = 0
kept = 0

print("Opening the stream...")

with urllib.request.urlopen(url) as response:
    with gzip.open(response, "rt") as reads:

        while skipped < skip:
            line = reads.readline()
            if line == "":
                break
            reads.readline()
            reads.readline()
            reads.readline()
            skipped = skipped + 1

        print("Skipped", skipped, "reads")

        with open("middle_reads.fastq", "w") as out:
            while kept < wanted:
                header = reads.readline()
                if header == "":
                    break
                sequence = reads.readline()
                plus = reads.readline()
                quality = reads.readline()

                out.write(header)
                out.write(sequence)
                out.write(plus)
                out.write(quality)

                kept = kept + 1

print("Kept", kept, "reads in middle_reads.fastq")
