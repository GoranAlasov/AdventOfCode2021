def decoder(lines):
    horizontal = []
    vertical = []
    
    for line in lines:
        if "forward" in line:
            string_split = line.split()
            line = int(string_split[1])
            horizontal.append(line)
        elif "up" in line:
            string_split = line.split()        
            line = int(string_split[1]) * -1
            vertical.append(line)
        else:
            string_split = line.split()
            line = int(string_split[1])
            vertical.append(line)
    
    return(horizontal, vertical)