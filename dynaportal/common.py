"""Module for common data structures."""
from dataclasses import dataclass, field
from enum import Enum


class FieldType(Enum):
    """Field type enum."""
    INPUT_TEXT = 1
    CHECKBOXES = 2


@dataclass
class Field:
    """Field data class."""
    id: str
    name: str
    field_type: FieldType
    caption: str
    hint: str = ""
    error: str = ""
    options: dict = field(default_factory=dict)