# find_reads.py
# Ask ENA what a real sequencing run contains, before downloading anything.

import urllib.request

accession = "SRR1770413"

fields = "run_accession,scientific_name,instrument_model,library_layout,read_count,base_count,fastq_bytes,fastq_ftp"

url = (
    "https://www.ebi.ac.uk/ena/portal/api/filereport"
    "?accession=" + accession
    + "&result=read_run"
    + "&fields=" + fields
    + "&format=tsv"
)

print("Asking ENA about", accession)
print()

with urllib.request.urlopen(url) as response:
    text = response.read().decode("utf-8")

lines = text.strip().split("\n")
headers = lines[0].split("\t")
values = lines[1].split("\t")

report = {}
for i in range(len(headers)):
    report[headers[i]] = values[i]

for key in report:
    print(key, "=", report[key])

print()
for size in report["fastq_bytes"].split(";"):
    megabytes = int(size) / 1024 / 1024
    print("one file is", round(megabytes), "MB")
