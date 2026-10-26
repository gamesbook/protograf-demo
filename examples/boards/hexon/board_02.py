"""
Customised grid for Hexon II hexes map

Written by: Derek Hohls
Created on: 23 Oct 2026

Notes:
    * Hexon II hexes are 100mm across the flats
    * Based off of the map for the design shown in:
        https://wargamingmiscellany.blogspot.com/2026/07/wargame-map-tool-my-operation.html
    * Name: Operation Barbarossa Minicampaign Crossing the River! 01
"""
from protograf import *

# ---- page setup
Create(
    filename="hexon02.pdf",
    paper="A4",
    margin=2,
    font_size=18,
    stroke_width=2)

# ---- common terrain symbols and colors
from terrain import *

# ---- draw hexes
hg = Hexagons(common=grid, fill=HEXES)

# ---- draw trees
trees(hg, "0502")
trees(hg, "0602")

# ---- draw river
Hexagon(common=river, cxy=hg.cxy("0104"))
Hexagon(common=river, cxy=hg.cxy("0204"))
Hexagon(common=river, cxy=hg.cxy("0304"))
Hexagon(common=river, cxy=hg.cxy("0404"))
Hexagon(common=river, cxy=hg.cxy("0504"))
Hexagon(common=river, cxy=hg.cxy("0604"))

# ---- draw bridges
Rectangle(common=bridge, cxy=hg.cxy("0204"))
Rectangle(common=bridge, cxy=hg.cxy("0504"))

# ---- draw hills
Circle(common=hill, cxy=hg.cxy("0107"))
Circle(common=hill, cxy=hg.cxy("0207"))

# ---- grid overlay
Hexagons(common=grid, fill=None)
# Hexagons(common=grid, fill=None, coord_elevation="top")  # ONLY when designing

# ---- create PDF and PNG
Save(
    output='png',
    dpi=300)
