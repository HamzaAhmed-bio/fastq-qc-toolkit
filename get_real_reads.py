# get_real_reads.py
# Stream a real FASTQ from ENA, unzip it on the fly,
# keep only the first 20000 reads, then stop.

import urllib.request
import gzip

url = "https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR177/003/SRR1770413/SRR1770413_1.fastq.gz"

wanted = 20000
kept = 0

print("Opening the stream...")

with urllib.request.urlopen(url) as response:
    with gzip.open(response, "rt") as reads:
        with open("real_reads.fastq", "w") as out:
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

print("Kept", kept, "reads in real_reads.fastq")
