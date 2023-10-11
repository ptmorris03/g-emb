"""
gemb/data.py
 * dataset config
 * torch dataset
"""
from pydantic import BaseModel, FilePath
from pydantic.functional_validators import AfterValidator
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


IndexedFastaPath = Annotated[FilePath, AfterValidator(assert_fai)]


class GenomeDatasetConfig(BaseModel):
    fasta_path: IndexedFastaPath
