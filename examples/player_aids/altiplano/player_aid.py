'''
protograf script to create player aid for "Altiplano"
Created on: 2026-10-27
'''
from protograf import *

Create(
    filename="altiplano_resources.pdf",
    paper="A5",
    margin=0.5,
    stroke_width=0.5
)

Rectangle(x=0, y=0, height=12, width=2.5, dotted=True)

def list_resources(tbl, resources):
    row = 0
    for item in resources:
        row = row + 1
        ID = item[0]
        name = item[1]
        freq = item[2]
        role = item[3]
        ext = item[4]
        source_1 = item[5]
        source_2 = item[6]
        source_3 = item[7]
        income = item[8]
        Text(
            xy=tbl.cell(f"A{row}").xy,
            height=tbl.cell(f"A{row}").height,
            width=tbl.cell(f"A{row}").width,
            html=True,
            align="right",
            text=f"""{name}""")
        D6(
            cxy=tbl.cell(f"B{row}").cxy,
            side=0.5,
            pips=freq)
        if role:
            Text(
                xy=tbl.cell(f"C{row}").xy,
                height=tbl.cell(f"C{row}").height,
                width=tbl.cell(f"C{row}").width,
                html=True,
                text=f"""{role}""")
        if ext:
            Text(
                xy=tbl.cell(f"D{row}").xy,
                height=tbl.cell(f"D{row}").height,
                width=tbl.cell(f"D{row}").width,
                html=True,
                text=f"""X:{ext}""")
        if source_1:
            Text(
                xy=tbl.cell(f"E{row}").xy,
                height=tbl.cell(f"E{row}").height,
                width=tbl.cell(f"E{row}").width,
                html=True,
                valign=True,
                text=f"""{source_1}""")
        if source_2:
            Text(
                xy=tbl.cell(f"F{row}").xy,
                height=tbl.cell(f"F{row}").height,
                width=tbl.cell(f"F{row}").width,
                valign=True,
                html=True,
                text=f"""{source_2}""")
        if source_3:
            Text(
                xy=tbl.cell(f"G{row}").xy,
                height=tbl.cell(f"G{row}").height,
                width=tbl.cell(f"G{row}").width,
                valign=True,
                html=True,
                text=f"""{source_3}""")
        if income:
            Text(
                xy=tbl.cell(f"H{row}").xy,
                height=tbl.cell(f"H{row}").height,
                width=tbl.cell(f"H{row}").width,
                html=True,
                text=f"""|:market 15:|{income}""")

tt = Table(
    x=2.5, y=0,
    height=12,
    rows=13,
    cols=[1.5, 1, 0.75, 1, 2, 2, 2, 1],
    stroke_width=0.5,
    borders_header=('n', 1, "black"),
    borders_footer=('s', 1, "black"),
    padding=0.05,
)

resources = [
    # ID, Name, Freq, Role, #Ext, Loc-1, Loc-2, Loc-3
    [1, "Corn", 4, "", "", "|:road 15:| =.=", "", "", ""],
    [2, "Money", 0, "R", "", "|:village 15:| Trading", "", "", ""],
    [3, "Food", 5, "", "", "|:farm 16:|<br/>1/Alpaca", "|:forest 15:|<br/>1/Cacao", "|:harbour 15:| Fish+Food", ""],
    [4, "Fish", 1, "R", "2", "", "", "", ""],
    [5, "Alpaca", 1, "R", "2", "", "", "", "1"],
    [6, "Wood", 3, "R", "4", "|:forest 15:|<br/>2 Food", "", "", ""],
    [7, "Stone", 3, "R", "4", "|:mine 15:|<br/>2 Food", "|:harbour 15:|<br/>2 Fish", "", "1"],
    [8, "Cacao", 1, "", "5", "", "", "", ""],
    [9, "Wool", 2, "R*", "3", "|:farm 16:| Alpaca+Food", "", "", "1"],
    [10, "Ore", 2, "R", "5", "", "", "", "1"],
    [11, "Cloth", 2, "", "", "|:farm 16:|<br/>Wool+Food", "|:forest 15:|<br/>1/Cacao", "", "2"],
    [12, "Silver", 2, "", "1", "|:mine 15:|<br/>Ore+Food", "", "", "3"],
    [13, "Glass", 1, "", "1", "|:forest 15:|<br/>1/Cacao", "", "", ""],
]

list_resources(tt, resources)

Save()
