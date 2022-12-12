with open('day10.txt') as prompt:
  instructions = [instruction for instruction in prompt.read().splitlines()]

x = 1
cycle = 1
idx = 0
interesting_signals = 0
pixels = []

def check_cycle(cycle, x):
  global interesting_signals
  if cycle == 20 or (cycle - 20) % 40 == 0:
    interesting_signals += cycle * x

def draw_pixel(cycle, x):
  cycle_pos = (cycle - 1) % 40

  draw = False
  for sprite_pos in range(x - 1, x + 2):
    if cycle_pos == sprite_pos:
      draw = True

  if draw:
    pixels.append("#")
  else:
    pixels.append(".")

while idx < len(instructions):
  check_cycle(cycle, x)
  draw_pixel(cycle, x)
  if instructions[idx][0] == 'a':
    cycle += 1
    check_cycle(cycle, x)
    draw_pixel(cycle, x)
    x += int(instructions[idx][4:])
    cycle += 1
  else:
    cycle += 1
  idx += 1

pixel_str = "".join(pixels)
print("day 1:", interesting_signals)
print("day 2:")
print(pixel_str[0:40])
print(pixel_str[40:80])
print(pixel_str[80:120])
print(pixel_str[120:160])
print(pixel_str[160:200])
print(pixel_str[200:240])
