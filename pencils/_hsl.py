from __future__ import annotations
from colorsys import hls_to_rgb
from typing import TYPE_CHECKING

from dataclasses import dataclass

if TYPE_CHECKING:
    from ._rgb import RGB


@dataclass
class HSL:
    """
    https://en.wikipedia.org/wiki/HSL_and_HSV
    """
    hue: float
    saturation: float
    lightness: float

    @property
    def h(self) -> float:
        return self.hue

    @property
    def s(self) -> float:
        return self.saturation

    @property
    def l(self) -> float:  # noqa: E74
        return self.lightness

    @property
    def rgb(self) -> RGB:
        from ._rgb import RGB
        r, g, b = hls_to_rgb(self.hue, self.lightness, self.saturation)
        return RGB(round(r * 255), round(g * 255), round(b * 255))

    @property
    def hex(self) -> str:
        return self.rgb.hex
