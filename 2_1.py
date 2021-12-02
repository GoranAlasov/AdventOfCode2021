lines = []

with open("navigation.txt","r") as navigation:
    lines = navigation.readlines()

horizontal = []
vertical = []

for line in lines:
    if "forward" in line:
        line = line.replace("forward ", "")
        line = line.replace("\n", "")
        line = int(line)
        horizontal.append(line)
    else:
        line = line.replace("up ", "-")
        line = line.replace("down ","")
        line = line.replace("\n","")
        line = int(line)
        vertical.append(line)

horizontal_sum = sum(horizontal)
vertical_sum = sum(vertical)

result = horizontal_sum * vertical_sum

print(result)
