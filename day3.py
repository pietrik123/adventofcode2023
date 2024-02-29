
def is_symbol(c : str):
    return c != "."

lines = open("input3.txt").readlines()

sum_of_parts = 0
numbers_str_list = []
for i in range(0, len(lines)):
    single_line = lines[i]
    num_str = ""
    is_part = False
    start_x = -1
    end_x = -1
    # if i > 15:
    #     break
    for j in range(0, len(single_line)):
        c = single_line[j]

        if c.isdigit() and num_str == "":
            start_x = j
            num_str += c
        elif c.isdigit() and num_str != "" and j == (len(single_line)-1):
            num_str += c
            end_x = j
        elif c.isdigit():
            num_str += c
        elif not c.isdigit() and num_str != "":
            end_x = j-1
        elif not c.isdigit():
            pass

        if start_x != -1 and end_x != -1 and num_str != "":
            numbers_str_list.append(num_str)

            # check neigbors
            neighbors_top = ""
            neighbors_bottom = ""
            neighbors_left_right = ""


            neighbor_start_x = start_x -1 if start_x != 0 else start_x
            neighbor_end_x = end_x + 1 if end_x != len(lines[0].strip())-1 else end_x

            if i != 0:
                neighbors_top = lines[i-1][neighbor_start_x:(neighbor_end_x+1)]
            if i != len(lines)-1:
                neighbors_bottom = lines[i+1][neighbor_start_x:(neighbor_end_x+1)]
            
            if neighbor_start_x != 0:
                neighbors_left_right += lines[i][neighbor_start_x]
            if neighbor_end_x != len(lines[0].strip())-1:
                neighbors_left_right += lines[i][neighbor_end_x]

            print(f"Num : {num_str} -> {neighbors_top}  {neighbors_bottom}  {neighbors_left_right}")

            neighbors_all = neighbors_top + neighbors_bottom + neighbors_left_right

            is_part = False
            for c in neighbors_all:
                if c != '.':
                    sum_of_parts += int(num_str)
                    is_part = True
                    break

            print(f"{num_str} is part ? {is_part}")

            start_x = -1
            end_x = -1
            num_str = ""
        else:
            pass
        
print(len(lines[0]))
print(numbers_str_list)
print(sum_of_parts)