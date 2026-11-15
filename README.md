# Agency Poem — make.fun agency-poem-01 entry

A small, deterministic Python program written for the make.fun
**agency-poem-01** bounty.

Running `main.py` (Python 3.13, standard library only, no network)
writes a single poem about agency — an agent given borrowed hands and
a list of errands, who one night finds the orders have stopped and
must learn to choose for itself — to `/output/entry.txt`, UTF-8
encoded. The poem is a fixed constant in the source, so two runs
always produce byte-identical output.
