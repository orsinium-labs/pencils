from __future__ import annotations
from random import choice
from typing import TYPE_CHECKING
from . import _palettes

if TYPE_CHECKING:
    from ._palette import Palette


PALETTES: tuple[Palette, ...] = (
    _palettes.DefoPalette,
    _palettes.NLPalette,
    _palettes.TRPalette,
    _palettes.INPalette,
    _palettes.SEPalette,
    _palettes.CAPalette,
    _palettes.AUPalette,
    _palettes.RUPalette,
    _palettes.FRPalette,
    _palettes.ESPalette,
    _palettes.DEPalette,
    _palettes.CNPalette,
    _palettes.USPalette,
    _palettes.GBPalette,
    _palettes.SocialPalette,
    _palettes.MetroPalette,
    _palettes.CSSPalette,
    _palettes.TailwindPalette,
    _palettes.BootstrapPalette,
)


def random_palette() -> Palette:
    return choice(PALETTES)
