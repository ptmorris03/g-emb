"""
label.py
 * This module contains classes related to labeling and defining spans of genomic sequences.
"""

from enum import Enum
from typing import Literal

import numpy as np
from pydantic import BaseModel, Field, field_validator, model_validator
from pydantic.functional_validators import AfterValidator
from pydantic.types import StringConstraints
from typing_extensions import Annotated

LowerStr = Annotated[str, StringConstraints(to_lower=True)]
BaseType = Literal["a", "t", "g", "c", "n"]


class Label(BaseModel):
    """
    A model representing a label with a key and associated value.

    Attributes
    ----------
    key : str
        The label's identifier.
    value : str
        The corresponding value of the label.
    """

    key: str
    value: str


class BaseLabel(Label):
    """
    An extended Label model which ensures the label value is both lowercased and one of the specified base types.

    Attributes
    ----------
    value : LowerStr
        The label's value which is always lowercased and one of the base types (a, t, g, c, n).
    """
    value: Annotated[LowerStr, BaseType]


class CaseLabel(Label):
    """
    A Label model with a validation that ensures its value is lowercased.

    Methods
    -------
    set_case(value: str) -> bool:
        Validates if the given value is in lowercase.
    """

    @field_validator("value")
    @classmethod
    def set_case(cls, value: str) -> bool:
        """
        Checks if the given value is in lowercase.

        Parameters
        ----------
        value : str
            The value to be validated.

        Returns
        -------
        bool
            True if the value is in lowercase, else False.
        """
        return value == value.lower()


class Span(BaseModel):
    """
    Represents a span of a contiguous genomic sequence.

    Attributes
    ----------
    start : int
        The starting index of the span in the sequence (inclusive). Defaults to 0.
    end : int
        The ending index of the span in the sequence (inclusive). Defaults to infinity.

    Methods
    -------
    assert_end_ge_start(model: "Span") -> None:
        Validates that the 'end' attribute is greater than or equal to the 'start' attribute.
    """

    start: int = Field(ge=0, default=0)
    end: int = Field(ge=0, default=np.inf)

    @model_validator(mode="after")
    def assert_end_ge_start(cls, model: "Span") -> None:
        """
        Ensures that the 'end' attribute of the model is greater than or equal to its 'start' attribute.

        Parameters
        ----------
        model : Span
            The Span model instance to be validated.

        Raises
        ------
        ValueError
            If 'end' is less than 'start'.
        """
        if model.end < model.start:
            raise ValueError(
                "end must be greater than or equal to start",
                f" * start: {model.start}",
                f" * end: {model.end}",
            )
