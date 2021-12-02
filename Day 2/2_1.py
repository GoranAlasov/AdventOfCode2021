from decoder_2_1 import calculate_position

file = open("navigation.txt", "r")
lines = file.read().splitlines()

position = calculate_position(lines)

horizontal = position[0]
vertical = position[1]

horizontal_sum = sum(horizontal)
vertical_sum = sum(vertical)

result = horizontal_sum * vertical_sum

print(result)
