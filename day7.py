class Dir(object):
  def __init__(self, parent):
    self.children = {}
    self.parent = parent

  def size(self):
    total_size = 0
    for child in self.children.values():
      if isinstance(child, Dir):
        total_size += child.size()
      else:
        total_size += child.size
    return total_size

class File(object):
  def __init__(self, size):
    self.size = size

with open('day7.txt') as prompt:
  terminal_lines = [line for line in prompt.read().splitlines()]

root = Dir(parent=None)
cur_dir = root
all_dirs = {root}
ls_mode = False

for line_num in range(1, len(terminal_lines)):
  cur_line = terminal_lines[line_num]
  if cur_line[0] == "$":
    ls_mode = False
    if cur_line == "$ ls":
      ls_mode = True
    elif cur_line == "$ cd ..":
      cur_dir = cur_dir.parent
    elif cur_line == "$ cd /":
      cur_dir = root
    else:
      cur_dir = cur_dir.children[cur_line.split(" ")[2]]
  elif ls_mode:
    cur_line = terminal_lines[line_num]
    if cur_line[0] == "d":
      if not cur_line[4:] in cur_dir.children:
        new_dir = Dir(parent=cur_dir)
        cur_dir.children[cur_line[4:]] = new_dir
        all_dirs.add(new_dir)
    else:
      file = cur_line.split(" ")
      if not file[1] in cur_dir.children:
        cur_dir.children[file[1]] = File(size=int(file[0]))

dir_sizes = [dir.size() for dir in all_dirs]
small_dirs_size = 0
big_dir_size = 70000000

space_needed = 30000000 - (70000000 - root.size())

for dir_size in dir_sizes:
  if dir_size <= 100000:
    small_dirs_size += dir_size
  if dir_size >= space_needed and dir_size < big_dir_size:
    big_dir_size = dir_size


print("day 1:", small_dirs_size)
print("day 2:", big_dir_size)
