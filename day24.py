import re
import numpy
import itertools

pattern = r"(\d{1,20}), (\d{1,20}), (\d{1,20}) @ {1,2}(-?\d{1,4}), {1,2}(-?\d{1,4}), {1,2}(-?\d{1,4})"

f = open("input24.txt")

xy_min = 200000000000000
xy_max = 400000000000000

#xy_min = 7
#xy_max = 27

lines = f.readlines()

coefs_list = []

haze_tuples_list = []

for line in lines:
    m = re.search(pattern, line)

    if m is None:
        print(f"Error : {line}")
        continue

    grps = m.groups()

    pos = [int(grps[0]),int(grps[1]),int(grps[2])]
    vel = [int(grps[3]), int(grps[4]), int(grps[5])]

    a_coef = -vel[1]/vel[0]

    coefs = [
        1,
        a_coef,
        pos[1] + a_coef*pos[0]
    ]

    haze_tuples_list.append((pos,vel,coefs))

    #print(f"{pos} {vel}")

# print(coefs_list)


cnt = 0
for i, j in itertools.combinations(range(len(haze_tuples_list)),r=2):

# for i in range(0, len(haze_tuples_list)-2):
#     first_line = haze_tuples_list[i][2]
#     for j in range(i+1, len(haze_tuples_list)-1):
    first_line = haze_tuples_list[i][2]
    second_line = haze_tuples_list[j][2]

    a = numpy.array([[first_line[0], first_line[1]],[second_line[0], second_line[1]]])
    b = numpy.array([first_line[2], second_line[2]])

    try:
        solution = numpy.linalg.solve(a, b)

        y = solution[0]
        x = solution[1]

        coord_ok = False
        if x >= xy_min and x <= xy_max and y >= xy_min and y <= xy_max:
            coord_ok = True
            #print(f"{x} {y} {first_line} {second_line}")
        
        first_start_intersect_vect = [x - haze_tuples_list[i][0][0],
                                        y - haze_tuples_list[i][0][1]]
        
        second_start_intersect_vect = [x - haze_tuples_list[j][0][0],
                                        y - haze_tuples_list[j][0][1]]
        
        first_dot_pr = first_start_intersect_vect[0] * haze_tuples_list[i][1][0] +\
            first_start_intersect_vect[1] * haze_tuples_list[i][1][1]
        
        second_dot_pr = second_start_intersect_vect[0] * haze_tuples_list[j][1][0] +\
            second_start_intersect_vect[1] * haze_tuples_list[j][1][1]
        
        #if coord_ok:
        #    print(f"{first_dot_pr} {second_dot_pr} {haze_tuples_list[i]} {haze_tuples_list[j]}")
        
        if coord_ok and first_dot_pr > 0 and second_dot_pr > 0:
            #pass
            cnt += 1

    except numpy.linalg.LinAlgError as e:
        print(f"{a} {b} error")

    #cnt+=1
    # print(solution)

print(cnt)