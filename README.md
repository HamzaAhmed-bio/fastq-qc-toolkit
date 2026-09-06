# fastq-qc-toolkit

Python tools for inspecting raw sequencing reads. FASTQ parsing, per-read and per-position quality summaries, and read trimming.

Self-directed project, built to learn sequencing quality control from the ground up rather than only running an off-the-shelf pipeline.

## Status

Work in progress. The scripts are being cleaned up and added to this repository.

## Scope

Parse FASTQ files and extract per-read length, base composition, and Phred quality scores.

Summarize quality per read and per base position.

Trim low-quality read ends.

Compare the results against FastQC output on the same file.

## Requirements

Python 3.9 or newer.

## Notes

Test data is not committed. Public datasets only.
