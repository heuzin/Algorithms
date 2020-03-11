#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  outcomes = []
  plays = ['rock', "scissor", 'paper']

  def rec_rps(n, result=[]):
    # print(f"result: {result}")
    if n == 0:
      return outcomes.append(result)
    for play in plays:
      rec_rps(n-1, result + [play])
    
  rec_rps(n, [])
  return outcomes

# print(rock_paper_scissors(2))



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')