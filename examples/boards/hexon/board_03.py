"""
Customised grid for Hexon II hexes map

Written by: Derek Hohls
Created on: 23 Oct 2026

Notes:
    * Hexon II hexes are 100mm across the flats
    * Based off of the map for the design shown in:
        https://wargamingmiscellany.blogspot.com/2026/07/wargame-map-tool-my-operation.html
    * Name: Operation Barbarossa Minicampaign Defence Line 01
"""
from protograf import *

# ---- page setup
Create(
    filename="hexon03.pdf",
    paper="A4",
    margin=2,
    font_size=18,
    stroke_width=2)

# ---- common terrain symbols and colors
from terrain import *

# ---- draw hexes
hg = Hexagons(common=grid, fill=HEXES)

# ---- draw wall/fortification
GridLine(
    hg,
    start="0202",
    point="se",
    edges="se,e,se,e,ne",
    stroke=WALL,
    stroke_width=10,
    stroke_ends="rounded")

# ---- draw trees
trees(hg, "0102")
trees(hg, "0202")
trees(hg, "0502")
trees(hg, "0602")
trees(hg, "0505")
trees(hg, "0605")

# ---- draw hills
Circle(common=hill, cxy=hg.cxy("0301"))
Circle(common=hill, cxy=hg.cxy("0402"))

# ---- draw river
Hexagon(common=river, cxy=hg.cxy("0106"))
Hexagon(common=river, cxy=hg.cxy("0206"))
Hexagon(common=river, cxy=hg.cxy("0306"))
Hexagon(common=river, cxy=hg.cxy("0406"))
Hexagon(common=river, cxy=hg.cxy("0506"))
Hexagon(common=river, cxy=hg.cxy("0606"))

# ---- draw bridges
Rectangle(common=bridge, cxy=hg.cxy("0406"))

# ---- grid overlay
# Hexagons(common=grid, fill=None)
Hexagons(common=grid, fill=None, coord_elevation="top")  # ONLY when designing

# ---- create PDF and PNG
Save(
    output='png',
    dpi=300)
