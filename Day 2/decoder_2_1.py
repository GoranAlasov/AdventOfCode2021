def calculate_position(lines):
    
    split_lines = []
    horizontal = []
    vertical = []

    for line in lines:
        split_lines.append(line.split())
    
    for line in split_lines:
        if "forward" in line[0]:                        
            horizontal.append(int(line[1]))
        elif "up" in line[0]:                        
            vertical.append(int(line[1]) * -1)
        else:                        
            vertical.append(int(line[1]))
    
    return(horizontal, vertical)