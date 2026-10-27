"""
Customised terrain for Hexon II hexes

Written by: Derek Hohls
Created on: 23 Oct 2026

Notes:
    * Hexon II hexes are 100mm across the flats
    * Based off of the maps for the design shown in:
        https://wargamingmiscellany.blogspot.com/2026/07/wargame-map-tool-my-operation.html
"""
from protograf import Common, steps, Triangle, Rectangle

# ---- colors
TOWN = "#7F7F7F"  # grey
RIVER = "#9AD9EA"  # blue
BRIDGE = "#C3C3C3"  # grey
ROAD = "#B97A57"  # light brown
WALL = "#B97A57"  # light brown
HEXES = "#B5E51D"  # background green
TREE_LEAF = "#21B04A"  # dark green

# ---- grid
grid = Common(
    height=2.5,  # quarter the Hexon II size
    hex_offset="odd",
    x=0, y=0,
    stroke="black",
    stroke_width=2,
    rows=8, cols=6,
)

# ---- hills
hill = Common(
    diameter=2.4,
    stroke=HEXES,
    fill=None,
    radii=steps(0,360,15),
    radii_offset=0.8,
    radii_length=0.3,
    radii_stroke="black",
    radii_stroke_width=2.5,
    radii_ends="rounded"
    )

# ---- bridge
bridge = Common(
    height=2.5,
    width=1,
    fill=BRIDGE,
    stroke="black",
    stroke_width=2,
    )

# ---- river
river = Common(
    stroke="black",
    stroke_width=2,
    fill=RIVER,
    height=2.5)

# ---- trees
def trees(grid, location):
    leaf = Common(
        side=0.5, height=1,
        stroke="black",
        stroke_width=2,
        fill=TREE_LEAF)
    trunk = Common(
        width=0.2, height=0.3,
        stroke="black",
        stroke_width=2,
        fill=ROAD)
    Triangle(
        x=grid.cxy(location).x+0.2,
        y=grid.cxy(location).y+0.7,
        common=leaf)
    Rectangle(
        x=grid.cxy(location).x+0.35,
        y=grid.cxy(location).y+0.7,
        common=trunk)
    Triangle(
        x=grid.cxy(location).x-0.8,
        y=grid.cxy(location).y+0.3,
        common=leaf)
    Rectangle(
        x=grid.cxy(location).x-0.65,
        y=grid.cxy(location).y+0.3,
        common=trunk)
