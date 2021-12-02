lines = []

with open("navigation.txt","r") as navigation:
    lines = navigation.readlines()

aim = 0
horizontal = 0
depth = 0

for line in lines:
    if "forward" in line:
        line = line.replace("forward ", "")
        line = line.replace("\n", "")
        line = int(line)

        horizontal += line
        depth += line * aim
    
    elif "down" in line:
        line = line.replace("down ", "")
        line = line.replace("\n", "")
        line = int(line)

        aim += line

    elif "up" in line:
        line = line.replace("up ", "-")
        line = line.replace("\n", "")
        line = int(line)

        aim += line

result = horizontal * depth
print(result)