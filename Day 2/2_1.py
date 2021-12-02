from decoder_2_1 import decoder

file = open("navigation.txt", "r")
lines = file.read().splitlines()

horizontal = decoder(lines)[0]
vertical = decoder(lines)[1]

horizontal_sum = sum(horizontal)
vertical_sum = sum(vertical)

result = horizontal_sum * vertical_sum

print(result)
