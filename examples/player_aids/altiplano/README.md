## Altiplano Player Aid

This example shows how a player aid, in a tabular form, can be designed
with **protograf**.

The game chosen is "Altiplano", published by *dlp games* in 2017.

The [script](player_aid.py) contains a list of the items which needs to be
put into a table; setup with the `Table()` command.

The `def list_resource()` function then loops over each row in that list
and assigns the values in that list to various cells in each row of the
table, primarily as `Text()`. It uses the ability to refer to a cell in
the table using an Excel-like syntax; where `A1` is the top-left cell.

The final result is available as a [PDF](altiplano_resources.pdf).
