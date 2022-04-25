from __future__ import annotations
from typing import Generic, TypeVar

from dataclasses import dataclass

C = TypeVar('C')


@dataclass
class Palette(Generic[C]):
    id: str
    name: str
    emoji: str
    emojis: list[str]
    colors: C

    author: str = ""
    url: str = ""
    dribbble: str = ""
