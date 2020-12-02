import re

from lib.input import read_lines


input = read_lines(2)


class Rule:
  def __init__(self, n1, n2, letter):
    self.n1 = n1
    self.n2 = n2
    self.letter = letter


class OldRule(Rule):
  def __init__(self, min, max, letter):
    super().__init__(min, max, letter)
    self.range = range(min, max + 1)

  def is_valid(self, password):
    return password.count(self.letter) in self.range


def parse_line(line):
  match = re.match(r"^(\d+)-(\d+)\s(\w):\s(\w*)$", line)
  n1, n2, letter, password = match.groups()
  n1, n2 = int(n1), int(n2)

  return n1, n2, letter, password


def count_valid(RuleType):
  valid_count = 0

  for line in input:
    n1, n2, letter, password = parse_line(line)

    rule = RuleType(n1, n2, letter)
    if rule.is_valid(password):
      valid_count += 1

  return valid_count


def solve():
  return count_valid(OldRule)
