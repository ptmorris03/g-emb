"""
label.py
 * Label
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
    Label type used to retrieve model heads

    Parameters
    ==========
    key : which label is being assigned
    value : the value of the label
    """

    key: str
    value: str


class BaseLabel(Label):
    value: Annotated[LowerStr, BaseType]


class CaseLabel(Label):
    @field_validator("value")
    @classmethod
    def set_case(cls, value: str) -> bool:
        return value == value.lower()


class Span(BaseModel):
    """
    A span of a contiguous genomic sequence

    Parameters
    ==========
    start : the start index of the label in the sequence, inclusive
    end : the end position of the label in the sequence, inclusive
    """

    start: int = Field(ge=0, default=0)
    end: int = Field(ge=0, default=np.inf)

    @model_validator(mode="after")
    def assert_end_ge_start(cls, model: "LabelSpan") -> None:
        if model.end < model.start:
            raise ValueError(
                "end must be greater than or equal to start",
                f" * start: {model.start}",
                f" * end: {model.end}",
            )
