import sys

f = open("input1.txt")

if f is None:
    sys.exit(1)

lines = f.readlines()

print(f"Nm of lines: {len(lines)}")

total = 0
cnt = 0
for line in lines:
    
    digits = [c for c in line if c.isdigit() == True]

    if len(digits) > 0:
        num_str = "" + digits[0] + digits[-1]
        num = int(num_str)
        total += num
        print(f"{digits} -> {num}")
    else:
        print(f"Not enough digits: {digits}")
    
    cnt += 1
    # if cnt > 10:
    #     break

print(f"Total is: {total}")

f.close()

