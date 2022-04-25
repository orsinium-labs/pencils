from __future__ import annotations
from typing import TYPE_CHECKING, Generic, TypeVar

from dataclasses import dataclass

if TYPE_CHECKING:
    from ._color import Color
    from ._colors import Colors

C = TypeVar('C', bound='type[Colors]')


@dataclass
class Palette(Generic[C]):
    id: str
    name: str
    colors: C

    emoji: str = ""
    emojis: list[str] = []
    author: str = ""
    url: str = ""
    dribbble: str = ""

    def random_color(self) -> Color:
        return self.colors.random_color()
