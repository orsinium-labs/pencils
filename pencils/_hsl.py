

from dataclasses import dataclass


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
