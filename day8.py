with open('day8.txt') as prompt:
  forest = [trees for trees in prompt.read().splitlines()]

visible_trees = (len(forest) * 2) + ((len(forest[0]) - 2) * 2)
highest_score = 0

for row_idx in range(1, len(forest) - 1):
  for col_idx in range(1, len(forest[row_idx]) - 1):
    visible_left, visible_right, visible_up, visible_down = True, True, True, True
    score_left, score_right, score_up, score_down = 0, 0, 0, 0
    for tree in forest[row_idx][:col_idx][::-1]:
      if int(tree) >= int(forest[row_idx][col_idx]):
        visible_left = False
        score_left += 1
        break
      else:
        score_left += 1
    for tree in forest[row_idx][col_idx + 1:]:
      if int(tree) >= int(forest[row_idx][col_idx]):
        visible_right = False
        score_right += 1
        break
      else:
        score_right += 1
    for row in forest[:row_idx][::-1]:
      if int(row[col_idx]) >= int(forest[row_idx][col_idx]):
        visible_up = False
        score_up += 1
        break
      else:
        score_up += 1
    for row in forest[row_idx + 1:]:
      if int(row[col_idx]) >= int(forest[row_idx][col_idx]):
        visible_down = False
        score_down += 1
        break
      else:
        score_down += 1
    
    if visible_left or visible_right or visible_up or visible_down:
      visible_trees += 1
    
    scenic_score = score_left * score_right * score_up * score_down
    
    if scenic_score > highest_score:
      highest_score = scenic_score

print("day 1:", visible_trees)
print("day 2:", highest_score)
