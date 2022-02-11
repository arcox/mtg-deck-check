import argparse
import csv
import pathlib

pointed_cards = {}
deck_list = {}
point_sum = 0

def load_point_list(fname):
  with open(fname, 'rt') as f:
    reader = csv.DictReader(f)
    for row in reader:
      for k, v in row.items():
        if v:
          v = v.replace("’", "'") # fix rogue apostrophes
          pointed_cards[v] = int(k[0])


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
  global point_sum
  cards = pointed_cards.keys() & deck_list.keys()
  for card in cards:
    points = pointed_cards[card] * deck_list[card]
    print('  {} x {} = {}'.format(card, deck_list[card], points))
    point_sum += points


def main():
  parser = argparse.ArgumentParser(description='Highlander Deck Checker')
  parser.add_argument('--point-file', type=pathlib.Path, required=True,
                      help='Path to csv file of pointed cards.')
  parser.add_argument('--deck-file', type=pathlib.Path, required=True,
                      help='Path to your deck ".dck" file')
  parser.add_argument('--point-limit', type=int, default=7, required=False,
                      help='Number of points allowed per deck. Default=7')
  args = parser.parse_args()

  load_point_list(args.point_file)
  load_deck_list(args.deck_file)

  print('\nThere are {} pointed cards in the list!'.format(len(pointed_cards)))
  print('Analyzing deck...')
  calculate_points()
  if point_sum <= args.point_limit:
    print('*** Your deck is LEGAL, using {} of {} possible points! :D'
          .format(point_sum, args.point_limit))
  else:
    print('*** SHAME! Your deck is ILLEGAL, using {} of a {} point limit!'
          .format(point_sum, args.point_limit))

if __name__ == '__main__':
  main()

