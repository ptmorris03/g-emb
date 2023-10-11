from pathlib import Path

import typer
from selene_sdk.sequences import Genome, Proteome

app = typer.Typer()


@app.command()
def load_genome(
    data_folder: Path = typer.Option(
        ..., help="Path to the data folder containing .fasta files for genomes"
    )
):
    """
    Load a Genome using selene-sdk from .fasta files in the specified data folder.
    """
    fasta_files = list(data_folder.glob("genomes/*.fasta"))
    if not fasta_files:
        typer.echo(f"No .fasta files found in {data_folder}/genomes")
        raise typer.Exit(code=1)

    for fasta_file in fasta_files:
        genome = Genome(str(fasta_file))
        typer.echo(f"Loaded genome from {fasta_file}")


@app.command()
def load_proteome(
    data_folder: Path = typer.Option(
        ...,
        help="Path to the data folder containing .fasta files for proteomes",
    )
):
    """
    Load a Proteome using selene-sdk from .fasta files in the specified data folder.
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
