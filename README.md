# fastq-qc-toolkit

Python tools for inspecting raw sequencing reads. FASTQ parsing, per-read and per-position quality summaries, and read trimming.

Self-directed project, written from scratch to learn sequencing quality control rather than only running an off-the-shelf pipeline. The per-position quality curve it produces was checked against FastQC output on the same file.

## Scripts

make_fastq.py writes a small sample FASTQ for testing.

check_fastq.py flags reads containing N bases.

check_quality.py decodes Phred+33 quality letters and reports a mean score per read.

count_bases.py reports base composition and GC content, excluding N from the denominator.

reverse_complement.py and rc_fastq.py build the reverse complement of a sequence.

find_reads.py queries the ENA filereport API for run metadata before anything is downloaded.

get_real_reads.py streams a real gzipped FASTQ from ENA, unzips on the fly, and keeps the first 20000 reads.

get_middle_reads.py does the same but samples from the middle of the run.

look_at_one_read.py prints every base beside its quality letter and score.

per_position.py reports mean quality per base position as an ASCII bar chart.

trim_fastq.py trims trailing bases below Q30.

trim_real.py cuts every read to a fixed length chosen from the quality curve.

real_vs_fake.py and real_vs_fake_all.py sort bases into confident and discarded buckets using the Q2 flag that Illumina uses to mark unusable calls.

## Data

Run get_real_reads.py to fetch the sequencing data. FASTQ files are not committed.

## Requirements

Python 3.9 or newer. Standard library only, no external packages.
