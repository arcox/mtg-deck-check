import argparse
import json
import pathlib

pointed_cards = {}
deck_list = {}

def load_point_list(fname):
  pl_data = None
  with open(fname, 'rt') as f:
    pl_data = json.load(f)
  for k, v in pl_data.items():
    k = k.replace("’", "'") # fix rogue apostrophes
    pointed_cards[k] = v


def load_deck_list(fname):
  lines = []
  with open(fname, 'rt') as f:
    lines = f.readlines()
  for line in lines:
    if line:
      if line.startswith('SB') or line.startswith('LAYOUT') or line.startswith('NAME'):
        continue
      card_name = line.split('] ')[1].strip()
      card_num = int(line.split()[0])
      if card_name not in deck_list:
        deck_list[card_name] = card_num
      else:
        deck_list[card_name] += card_num


def calculate_points():
  point_sum = 0
  cards = pointed_cards.keys() & deck_list.keys()
  for card in cards:
    points = pointed_cards[card] * deck_list[card]
    print('  {} x {} = {}'.format(card, deck_list[card], points))
    point_sum += points
  return point_sum


def main():
  parser = argparse.ArgumentParser(description='Highlander Deck Checker')
  parser.add_argument('--deck-file', type=pathlib.Path, required=True,
                      help='Path to your deck ".dck" file')
  parser.add_argument('--point-file', type=pathlib.Path, default="./points.json", required=False,
                      help='Path to JSON file of pointed cards. Default="./points.json"')
  parser.add_argument('--point-limit', type=int, default=7, required=False,
                      help='Number of points allowed per deck. Default=7')
  args = parser.parse_args()

  load_point_list(args.point_file)
  load_deck_list(args.deck_file)

  print('There are {} pointed cards in total...'.format(len(pointed_cards)))
  print('Analyzing deck...')
  point_sum = calculate_points()
  if point_sum <= args.point_limit:
    print('*** Your deck is LEGAL, using {} of {} possible points! :D'
          .format(point_sum, args.point_limit))
  else:
    print('*** SHAME! Your deck is ILLEGAL, using {} of a {} point limit!'
          .format(point_sum, args.point_limit))

if __name__ == '__main__':
  main()

