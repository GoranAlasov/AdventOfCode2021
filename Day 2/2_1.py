from decoder_2_1 import decoder

file = open("navigation.txt", "r")
lines = file.read().splitlines()

decoded = decoder(lines)

horizontal = decoder[0]
vertical = decoder[1]

horizontal_sum = sum(horizontal)
vertical_sum = sum(vertical)

result = horizontal_sum * vertical_sum

print(result)
