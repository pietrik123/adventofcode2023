import sys



f = open("input1.txt")

if f is None:
    sys.exit(1)

lines = f.readlines()

digits_as_words = ['one','two','three',
                   'four','five','six',
                   'seven','eight','nine']

digit_word_vs_digit = {
    'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5,
    'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9
}

def find_all_positions(text, word):
    res = []
    start = 0
    while True:
        pos = text.find(word, start)
        if pos == -1:
            return res
        res.append(pos)
        start = pos+1
    return res

total = 0
cnt = 0
for line in lines:
    
    digit_word_vs_positions = []
    digit_vs_positions = []
    for s in digits_as_words:
        all_positions = find_all_positions(line, s)
        digit_word_vs_positions.append((s,all_positions))

    min_position = 100
    min_position_digit = 0
    max_position = -1
    max_position_digit = 0
    for digit_word,positions in digit_word_vs_positions:
        for p in positions:
            if p < min_position:
                min_position = p
                min_position_digit = digit_word_vs_digit[digit_word]
            if p > max_position:
                max_position = p
                max_position_digit = digit_word_vs_digit[digit_word]
    
    digits_in_line = [c for c in line if c.isdigit() == True]

    if len(digits_in_line) > 0:
        pos = line.find(digits_in_line[0])
        if pos != -1 and pos < min_position:
            min_position = pos
            min_position_digit = int(digits_in_line[0])
        
        pos = line.rfind(digits_in_line[-1])
        if pos != -1 and pos > max_position:
            max_position = pos
            max_position_digit = int(digits_in_line[-1])

    if min_position_digit != 0 and max_position_digit != 0:
        num = min_position_digit * 10 + max_position_digit
        total += num
        print(f"Found: {line} : {num}, {digits_in_line}")
    else:
        print(f"Did not find digit words: {line}, {digits_in_line}")

    cnt += 1
    # if cnt > 15:
    #     break

print(f"Total is: {total}")

f.close()

