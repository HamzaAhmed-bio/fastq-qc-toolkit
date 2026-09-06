# fastq-qc-toolkit

Python tools for quality control of raw sequencing reads.

The toolkit parses FASTQ files, decodes Phred quality scores, profiles quality by read and by base position, reports base composition and GC content, and trims low-quality read ends. It also retrieves public sequencing runs from the European Nucleotide Archive so the tools can be tested against real data.

Written from scratch rather than assembled from an existing pipeline, to understand each stage of the quality control process. The per-position quality profile it produces was validated against FastQC output on the same file.

## Usage

Retrieve a public sequencing run, then run any of the analysis scripts against it. Sequencing data is not committed to the repository.

## Requirements

Python 3.9 or newer. Standard library only.
