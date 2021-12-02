from decoder_2_1 import decoder

file = open("navigation.txt", "r")
lines = file.read().splitlines()

decoded = decoder(lines)

horizontal = decoded[0]
vertical = decoded[1]

horizontal_sum = sum(horizontal)
vertical_sum = sum(vertical)

result = horizontal_sum * vertical_sum

print(result)
