f = open("input44.txt")

lines = f.readlines()

total_points = 0
for line in lines:

    tokens_1 = line.split(":")

    tokens_2 = tokens_1[1].split("|")

    winning_nums_str = tokens_2[0]
    numbers_str = tokens_2[1]

    str_winning_nums = winning_nums_str.split(" ")
    str_winning_nums_2 = [s.strip() for s in str_winning_nums]

    str_numbers = numbers_str.split(" ")
    str_numbers_2 = [s.strip() for s in str_numbers]

    winning_nums = []

    for s in str_winning_nums_2:
        try:
            winning_nums.append(int(s))
        except:
            print(f"conversion error {s}")

    nums = []

    for s in str_numbers_2:
        try:
            nums.append(int(s))
        except:
            print(f"conversion error {s}")

    print(winning_nums)
    print(nums)

    points = 0
    for win_num in winning_nums:
        if win_num in nums:
            if points == 0:
                points =1
            else:
                points *= 2
    print(points)

    total_points += points

print(f"Total: {total_points}")