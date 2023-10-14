"""
gemb/data.py
 * dataset config
 * torch dataset
"""
import torch
from pydantic import BaseModel, Field, FilePath, model_validator
from pydantic.functional_validators import AfterValidator
from selene_sdk.sequences import Genome
from torch.utils.data import Dataset
from typing_extensions import Annotated


def assert_fai(fasta_path: FilePath) -> FilePath:
    """
    Validate a matching .fai index file exists next to the fasta file.

    Parameters
    ==========
    fasta_path : path to the fasta file

    Returns
    =======
    fasta_path
    """
    assert (
        fasta_path.with_suffix(".fai").is_file()
        or fasta_path.with_suffix(fasta_path.suffix + ".fai").is_file()
    )

    return fasta_path


class GenomeDatasetConfig(BaseModel):
    fasta_path: Annotated[FilePath, AfterValidator(assert_fai)]
    kmer_size: int = 5
    kmer_stride: int = 5


class GenomeDataset(Dataset):
    """
    Read from a fasta file using selene-sdk.sequences.Genome.
    Configure dataset size by setting kmer_size and kmer_stride.
    """

    def __init__(self, config: GenomeDatasetConfig) -> None:
        self.config = config.model_dump()
        self.genome = Genome(self.config["fasta_path"])
        self.chromosomes = {
            name: length for name, length in self.genome.get_chr_lens()
        }

    def __len__(self):
        self.length = 0
        for name, length in self.chromosomes.items():
            self.length += length
        self.length = self.config
        return self.length

    def __getitem__(self, idx: int) -> torch.tensor:
        pass
