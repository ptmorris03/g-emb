"""
gemb/data.py
 * This module contains classes and functions for managing genomic datasets.

Classes:
--------
 * GenomeDatasetConfig - Configuration class for genomic datasets.
 * GenomeDataset - A PyTorch dataset class for genomic sequences.

Functions:
----------
 * assert_fai(fasta_path: FilePath) -> FilePath - Validate existence of .fai index file for a given fasta file.
"""

import torch
from pydantic import BaseModel, Field, FilePath, model_validator
from pydantic.functional_validators import AfterValidator
from selene_sdk.sequences import Genome
from torch.utils.data import Dataset
from typing_extensions import Annotated


def assert_fai(fasta_path: FilePath) -> FilePath:
    """
    Validates that a matching .fai index file exists alongside the given fasta file.

    Parameters
    ----------
    fasta_path : FilePath
        The path to the fasta file.

    Returns
    -------
    FilePath
        The validated fasta file path.

    Raises
    ------
    AssertionError
        If the .fai index file is missing.
    """
    assert (
        fasta_path.with_suffix(".fai").is_file()
        or fasta_path.with_suffix(fasta_path.suffix + ".fai").is_file()
    )
    return fasta_path


class GenomeDatasetConfig(BaseModel):
    """
    A configuration model for genomic datasets.

    Attributes
    ----------
    fasta_path : FilePath
        The path to the fasta file.
    kmer_size : int, optional
        The k-mer size. Defaults to 5.
    kmer_stride : int, optional
        The stride for k-mers. Defaults to 5.
    """

    fasta_path: Annotated[FilePath, AfterValidator(assert_fai)]
    kmer_size: int = 5
    kmer_stride: int = 5


class GenomeDataset(Dataset):
    """
    A PyTorch Dataset for genomic sequences.

    Attributes
    ----------
    config : GenomeDatasetConfig
        Configuration for the dataset.
    genome : Genome
        A genome instance from Selene SDK for reading fasta files.
    chromosomes : dict
        A dictionary containing the length of each chromosome.

    Methods
    -------
    __len__() -> int:
        Returns the total length of all chromosomes.
    __getitem__(idx: int) -> torch.Tensor:
        Gets the sequence at the given index.
    """

    def __init__(self, config: GenomeDatasetConfig) -> None:
        """
        Initializes the GenomeDataset.

        Parameters
        ----------
        config : GenomeDatasetConfig
            The configuration object.
        """
        self.config = config.model_dump()
        self.genome = Genome(self.config["fasta_path"])
        self.chromosomes = {
            name: length for name, length in self.genome.get_chr_lens()
        }

    def __len__(self):
        """
        Returns the total length of all chromosomes.

        Returns
        -------
        int
            The total length of all chromosomes.
        """
        total_length = sum(self.chromosomes.values())
        return total_length

    def __getitem__(self, idx: int) -> torch.Tensor:
        """
        Retrieve the sequence at a given index.

        Parameters
        ----------
        idx : int
            The index at which the sequence is located.

        Returns
        -------
        torch.Tensor
            The tensor containing the sequence data.
        """
        # Implement logic here
        pass
