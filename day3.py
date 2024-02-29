
f = open("input3.txt")

lines = f.readlines()


parts = []
gear_pos_vs_parts = {}
for i in range(0, len(lines)):
    single_line = lines[i]
    single_line = single_line.strip()

    num_str = ""
    start_x = -1
    end_x = -1

    for j in range(0, len(single_line)):
        
        c = single_line[j]
        if num_str == "" and c.isdigit():
            start_x = j
            num_str += c
        elif c.isdigit() and j == len(single_line)-1:
            num_str += c
            end_x = j
        elif c.isdigit():
            num_str += c
        elif not c.isdigit() and num_str != "":
            end_x = j-1

        if start_x != -1 and end_x != -1 and num_str != "":
            print(num_str)
            neighbor_chars_top = ""
            neighbor_chars_bottom = ""
            neighbor_chars_left = ""
            neighbor_chars_right = ""

            n_start_x = start_x-1 if start_x != 0 else start_x
            n_end_x = end_x+1 if end_x != len(single_line)-1 else end_x

            if i != 0:
                neighbor_chars_top = lines[i-1][n_start_x:n_end_x+1]
            if i != len(lines)-1:
                neighbor_chars_bottom = lines[i+1][n_start_x:n_end_x+1]
            
            if start_x != 0:
                neighbor_chars_left += lines[i][n_start_x]
            if end_x != len(single_line)-1:
                neighbor_chars_right += lines[i][n_end_x]

            neighbors = neighbor_chars_top + neighbor_chars_bottom +\
                 neighbor_chars_left + neighbor_chars_right

            is_part = False
            for neighbor in neighbors:
                if neighbor != '.':
                    is_part = True
                    parts.append(num_str)
                    break

            if is_part == True:
                pos = 0
                while True:
                    idx = neighbor_chars_top.find("*", pos)
                    pos = idx + 1
                    if idx == -1:
                        break
                    else:
                        gear_pos_x = idx + n_start_x
                        gear_pos_y = i-1
                        if (gear_pos_x,gear_pos_y) not in gear_pos_vs_parts.keys():
                            gear_pos_vs_parts[(gear_pos_x, gear_pos_y)] = [int(num_str)]
                        else:
                            gear_pos_vs_parts[(gear_pos_x, gear_pos_y)].append(int(num_str))

                pos = 0
                while True:
                    idx = neighbor_chars_bottom.find("*", pos)
                    pos = idx + 1
                    if idx == -1:
                        break
                    else:
                        gear_pos_x = idx + n_start_x
                        gear_pos_y = i+1
                        if (gear_pos_x,gear_pos_y) not in gear_pos_vs_parts.keys():
                            gear_pos_vs_parts[(gear_pos_x, gear_pos_y)] = [int(num_str)]
                        else:
                            gear_pos_vs_parts[(gear_pos_x, gear_pos_y)].append(int(num_str))
                if neighbor_chars_left == "*":
                    gear_pos_x = n_start_x
                    gear_pos_y = i
                    if (gear_pos_x,gear_pos_y) not in gear_pos_vs_parts.keys():
                        gear_pos_vs_parts[(gear_pos_x, gear_pos_y)] = [int(num_str)]
                    else:
                        gear_pos_vs_parts[(gear_pos_x, gear_pos_y)].append(int(num_str))
                if neighbor_chars_right == "*":
                    gear_pos_x = n_end_x
                    gear_pos_y = i
                    if (gear_pos_x,gear_pos_y) not in gear_pos_vs_parts.keys():
                        gear_pos_vs_parts[(gear_pos_x, gear_pos_y)] = [int(num_str)]
                    else:
                        gear_pos_vs_parts[(gear_pos_x, gear_pos_y)].append(int(num_str))


            # reset
            num_str = ""
            start_x = -1
            end_x = -1

# print(lines)
# print(parts)

sum_of_parts = 0
for p in parts:
    sum_of_parts += int(p)

print(sum_of_parts)
print(gear_pos_vs_parts)

sum_of_mult_parts = 0
for (key,val) in gear_pos_vs_parts.items():
    if len(val) == 2:
        sum_of_mult_parts += val[0]*val[1]

print(sum_of_mult_parts)


