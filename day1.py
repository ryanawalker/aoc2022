with open('day1.txt') as prompt:
  calories = [calorie for calorie in prompt.read().splitlines()]

calorie_count = 0
calories_per_elf = []

for idx in range(len(calories)):
  if calories[idx] == "" or idx == len(calories) - 1:
    calories_per_elf.append(calorie_count)
    calorie_count = 0
  else:
    calorie_count += int(calories[idx])

calories_per_elf.sort()

print("part 1:", calories_per_elf[-1])
print("part 2:", sum(calories_per_elf[-3:]))
