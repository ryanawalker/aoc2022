with open('day5.txt') as prompt:
  whole_input = [line for line in prompt.read().splitlines()]

index_of_first_inst, idx = 0, 0

while index_of_first_inst == 0:
  if whole_input[idx] == "":
    index_of_first_inst = idx + 1
  else:
    idx += 1

crate_diagram = whole_input[:index_of_first_inst - 2]
instructions = [instruction.split(" ") for instruction in whole_input[index_of_first_inst:]]

crate_stacks_p1 = [[] for i in range(int((len(crate_diagram[0]) - 3) / 4 + 1))]
crate_stacks_p2 = [[] for i in range(int((len(crate_diagram[0]) - 3) / 4 + 1))]

for row in crate_diagram:
  idx = 1
  cur_stack = 0
  while idx < len(row):
    if row[idx].isalpha():
      crate_stacks_p1[cur_stack].insert(0, row[idx])
      crate_stacks_p2[cur_stack].insert(0, row[idx])
    idx += 4
    cur_stack += 1

for instruction in instructions:
  number_moved = int(instruction[1])
  from_stack = int(instruction[3]) - 1
  to_stack = int(instruction[5]) - 1
  for _ in range(number_moved):
    crate_stacks_p1[to_stack].append(crate_stacks_p1[from_stack].pop())
  crate_stacks_p2[to_stack] += crate_stacks_p2[from_stack][-number_moved:]
  crate_stacks_p2[from_stack] = crate_stacks_p2[from_stack][:-number_moved]

print("part 1:", "".join([stack[-1] for stack in crate_stacks_p1]))
print("part 2:", "".join([stack[-1] for stack in crate_stacks_p2]))
