with open('day4.txt') as prompt:
  pairs = [pair for pair in prompt.read().splitlines()]

contained_pair_count = 0
overlapping_pair_count = 0

for pair in pairs:
  elves = [set(range(int(elf.split('-')[0]), int(elf.split('-')[1]) + 1)) for elf in pair.split(',')]
  if len(elves[0].difference(elves[1])) == 0 or len(elves[1].difference(elves[0])) == 0:
    contained_pair_count += 1
  if len(elves[0].intersection(elves[1])) != 0:
    overlapping_pair_count += 1
  

print("day 1:", contained_pair_count)
print("day 2:", overlapping_pair_count)
