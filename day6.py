with open('day6.txt') as prompt:
  signal = prompt.read()

packet_start = 0
message_start = 0
packet_done = False
message_done = False

for idx in range(len(signal)):
  if packet_done == False and len(set(signal[idx:idx+4])) == 4:
    packet_start = idx + 4
    packet_done = True
  if packet_done == True and message_done == False and len(set(signal[idx:idx+14])) == 14:
    message_start = idx + 14
    message_done = True
  if message_done and packet_done:
    break

print("day 1:", packet_start)
print("day 2:", message_start)
