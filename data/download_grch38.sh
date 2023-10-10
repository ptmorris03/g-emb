#!/bin/bash

apt install curl samtools gzip

mkdir -p genomes
mkdir -p transcripts
mkdir -p proteins

curl https://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/annotation/GRCh38_latest/refseq_identifiers/GRCh38_latest_genomic.fna.gz --output genomes/grch38.fasta.gz
gzip -d genomes/grch38.fasta.gz
samtools faidx genomes/grch38.fasta

curl https://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/annotation/GRCh38_latest/refseq_identifiers/GRCh38_latest_rna.fna.gz --output transcripts/grch38.fasta.gz
gzip -d transcripts/grch38.fasta.gz
samtools faidx transcripts/grch38.fasta

curl https://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/annotation/GRCh38_latest/refseq_identifiers/GRCh38_latest_protein.faa.gz --output proteins/grch38.fasta.gz
gzip -d proteins/grch38.fasta.gz
samtools faidx proteins/grch38.fasta

