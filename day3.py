with open('day3.txt') as prompt:
  rucksacks = [rucksack for rucksack in prompt.read().splitlines()]

value_dict = {
  'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
  'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
  'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
  'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33,
  'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41,
  'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49,
  'X': 50, 'Y': 51, 'Z': 52
}
total_priorities = 0

for rucksack in rucksacks:
  halfway_point = int(len(rucksack) / 2)
  for item in set(rucksack[:halfway_point]):
    if item in set(rucksack[halfway_point:]):
      total_priorities += value_dict[item]
      break

print("part 1:", total_priorities)

total_priorities = 0

idx = 0

while(idx < len(rucksacks) - 1):
  total_priorities += value_dict[
    list(
      set(rucksacks[idx])
      .intersection(set(rucksacks[idx + 1]))
      .intersection(set(rucksacks[idx + 2]))
    )[0]
  ]

  idx += 3

print("part 2:", total_priorities)
