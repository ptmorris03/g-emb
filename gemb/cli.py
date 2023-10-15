"""
command_line.py
 * This module provides command-line interface (CLI) commands for loading genome and proteome data.

Functions:
-----------
 * load_genome() - Load genome sequences from .fasta files.
 * load_proteome() - Load proteome sequences from .fasta files.
"""

from pathlib import Path

import typer
from selene_sdk.sequences import Genome, Proteome

from gemb.data import \
    GenomeDatasetConfig  # Assuming this import works in your environment

app = typer.Typer()


@app.command()
def load_genome(
    data_folder: Path = typer.Option(
        default="data/",
        help="Path to the data folder containing .fasta files for genomes",
    )
):
    """
    Load a Genome using selene-sdk from .fasta files located in a specified data folder.

    Parameters
    ----------
    data_folder : Path
        The folder where .fasta files for genomes are located. Defaults to 'data/'.

    Raises
    ------
    typer.Exit
        Exits the program with code 1 if no .fasta files are found.
    """
    fasta_files = list(data_folder.glob("genomes/*.fasta"))
    if not fasta_files:
        typer.echo(f"No .fasta files found in {data_folder}/genomes")
        raise typer.Exit(code=1)

    for fasta_file in fasta_files:
        data_config = GenomeDatasetConfig(fasta_path=fasta_file)
        cfg = data_config.model_dump()
        genome = Genome(cfg["fasta_path"])
        typer.echo(f"Loaded genome from {fasta_file}")

        for chromosome, length in genome.get_chr_lens():
            sequence = genome.get_sequence_from_coords(
                chromosome, start=0, end=length
            )
            typer.echo(
                f" - {chromosome} - {len(sequence):10d} - {sequence[:32]}"
            )


@app.command()
def load_proteome(
    data_folder: Path = typer.Option(
        default="data/",
        help="Path to the data folder containing .fasta files for proteomes",
    )
):
    """
    Load a Proteome using selene-sdk from .fasta files located in a specified data folder.

    Parameters
    ----------
    data_folder : Path
        The folder where .fasta files for proteomes are located. Defaults to 'data/'.

    Raises
    ------
    typer.Exit
        Exits the program with code 1 if no .fasta files are found.
    """
    fasta_files = list(data_folder.glob("proteins/*.fasta"))
    if not fasta_files:
        typer.echo(f"No .fasta files found in {data_folder}/proteins")
        raise typer.Exit(code=1)

    for fasta_file in fasta_files:
        proteome = Proteome(str(fasta_file))
        typer.echo(f"Loaded proteome from {fasta_file}")


if __name__ == "__main__":
    app()
