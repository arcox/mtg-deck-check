# mtg-deck-check
Verifies that an Xmage deck file complies with a point list.

# Quick Tutorial

1. Make sure the `points.json` file is present alongside the deck check script (provided in repo as `points.json`).
2. Build a deck in Xmage. Save it in the default `.dck` format.
3. Run the script using Python 3

```
usage: deckcheck.py [-h] --deck-file DECK_FILE [--point-file POINT_FILE] [--point-limit POINT_LIMIT]

Highlander Deck Checker

options:
  -h, --help            show this help message and exit
  --deck-file DECK_FILE
                        Path to your deck ".dck" file
  --point-file POINT_FILE
                        Path to JSON file of pointed cards. Default="./points.json"
  --point-limit POINT_LIMIT
                        Number of points allowed per deck. Default=7
```
### Output
```
python3 deckcheck.py --deck-file ~/mtgdecks/game-night/7ph-goodbye-horses.dck 

There are 85 pointed cards in the list!
Analyzing deck...
  Strip Mine x 1 = 2
  Sun Droplet x 1 = 1
  Maze of Ith x 1 = 2
  Authority of the Consuls x 1 = 1
  Sol Ring x 1 = 3
  Karakas x 1 = 3
*** SHAME! Your deck is ILLEGAL, using 12 of a 7 point limit!
```
