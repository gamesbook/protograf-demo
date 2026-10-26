"""
Customised grid for Hexon II hexes map

Written by: Derek Hohls
Created on: 22 Oct 2026

Notes:
    * Hexon II hexes are 100mm across the flats
    * Based off of the map for the design shown in:
        https://wargamingmiscellany.blogspot.com/2026/07/wargame-map-tool-my-operation.html
    * Name: Operation Barbarossa Minicampaign Counterattack! 01
"""
from protograf import *

# ---- page setup
Create(
    filename="hexon01.pdf",
    paper="A4",
    margin=2,
    font_size=18,
    stroke_width=2)

# ---- common terrain symbols and colors
from terrain import *

# ---- draw hexes
hg = Hexagons(common=grid, fill=HEXES)

# ---- draw road
GridLine(
    hg,
    start="0508",
    point="e",
    edges="nw,"*10,
    stroke=ROAD,
    stroke_width=25,
    stroke_ends="rounded")

# ---- draw trees
trees(hg, "0401")
trees(hg, "0402")
trees(hg, "0501")
trees(hg, "0502")
trees(hg, "0601")
trees(hg, "0602")

# ---- draw towns
Rectangle(
    height=0.8,
    width=0.6,
    x=hg.cxy("0607").x-0.6,
    y=hg.cxy("0607").y-0.2,
    rotation=30,
    fill=TOWN)
Rectangle(
    height=1.2,
    width=0.8,
    x=hg.cxy("0608").x-0.4,
    y=hg.cxy("0608").y-0.6,
    fill=TOWN)
Rectangle(
    height=0.8,
    width=1.2,
    x=hg.cxy("0508").x-0.6,
    y=hg.cxy("0508").y,
    fill=TOWN)

# ---- draw hills
Circle(common=hill, cxy=hg.cxy("0205"))
Circle(common=hill, cxy=hg.cxy("0105"))

# ---- grid overlay
Hexagons(common=grid, fill=None)
# Hexagons(common=grid, fill=None, coord_elevation="top")  # ONLY when designing

# ---- create PDF and PNG
Save(
    output='png',
    dpi=300)
