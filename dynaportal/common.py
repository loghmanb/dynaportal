"""Module for common data structures."""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict


class FieldType(Enum):
    """Field type enum."""

    INPUT_TEXT = 1
    CHECKBOXES = 2
    RADIOS = 3
    SELECT = 4


@dataclass
class Field:
    """Field data class."""

    id: str
    name: str
    field_type: FieldType
    caption: str
    hint: str = ""
    error: str = ""
    options: Dict = field(default_factory=dict)
