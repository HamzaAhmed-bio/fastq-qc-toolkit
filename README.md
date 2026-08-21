# fastq-qc-toolkit

Python and Bash tooling for inspecting raw sequencing reads: parse FASTQ files, summarize per-read quality metrics, and run a FastQC → Trimmomatic quality-control pass across a batch of samples.

Built as a self-directed project to learn NGS quality control from the ground up rather than only running an off-the-shelf pipeline.

## What it does

- Parses FASTQ files with Biopython and extracts per-read length, GC content, and Phred quality scores
- Summarizes quality per sample — mean quality, quality distribution, read count, length distribution
- Plots quality-by-position and read-length histograms with Matplotlib
- Runs a batch QC pass: FastQC on raw reads → Trimmomatic for adapter and low-quality base removal → FastQC again to confirm improvement

## Requirements

Python 3.9+ with `biopython`, `pandas`, `numpy`, `matplotlib`.
External tools on PATH: `fastqc`, `trimmomatic`.

## Notes

Test data is not committed to this repo — public datasets only.
