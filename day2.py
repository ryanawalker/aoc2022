with open('day2.txt') as prompt:
  rounds = [(game[0], game[2]) for game in prompt.read().splitlines()]

score_1, score_2 = 0, 0
score_dict = {'X': 1, 'Y': 2, 'Z': 3}
win_dict = {'A': 'Y', 'B': 'Z', 'C': 'X'}
tie_dict = {'A': 'X', 'B': 'Y', 'C': 'Z'}
lose_dict = {'A': 'Z', 'B': 'X', 'C': 'Y'}
outcome_dict = {'X': 0, 'Y': 3, 'Z': 6}
choice_dict = {'X': lose_dict, 'Y': tie_dict, 'Z': win_dict}

for game in rounds:
  score_1 += 6 if win_dict[game[0]] == game[1] else 3 if tie_dict[game[0]] == game[1] else 0
  score_1 += score_dict[game[1]]
  score_2 += outcome_dict[game[1]]
  score_2 += score_dict[choice_dict[game[1]][game[0]]]

print("part 1:", score_1)
print("part 2:", score_2)
