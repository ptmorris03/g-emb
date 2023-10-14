"""
label.py
 * Label
"""
from enum import Enum

import numpy as np
from pydantic import BaseModel, Field, model_validator
from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated

LowerStr = Annotated[str, AfterValidator(lambda string: string.lower())]


class LabelId(BaseModel):
    """
    Label type used to retrieve model heads

    Parameters
    ==========
    key : which label is being assigned
    value : the value of the label
    """

    key: LowerStr
    value: LowerStr


class Label(BaseModel):
    """
    A label of a contiguous genomic sequence

    Parameters
    ==========
    name : the string key and label value used to identify the label
    start : the start index of the label in the sequence, inclusive
    end : the end position of the label in the sequence, inclusive
    """

    label: LabelId
    start: int = Field(ge=0, default=0)
    end: int = Field(ge=0, default=np.inf)

    @model_validator(mode="after")
    def assert_end_ge_start(cls, model: "LabelSpan") -> None:
        if model.end < model.start:
            raise ValueError(
                "Label end must be greater than or equal to start",
                f" * name: {model.label}",
                f" * start: {model.start}",
                f" * end: {model.end}",
            )
