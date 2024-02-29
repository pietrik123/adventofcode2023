with open("input1.txt", "r") as file:
    totalNum = int()
    lineArr = []
    line_arr_changed = []
    strNumToCheckMap = {'one':'1','two':'2','three':'3','four':'4','five':'5',
                        'six':'6','seven':'7','eight':'8','nine':'9'}
    
    for line in file:
        lineArr.append(line)

    for i in lineArr:
        temp_i = ''
        for it in i:
            temp_i += it     
            for key, val in strNumToCheckMap.items():
                temp_i = temp_i.replace(key, val)
        line_arr_changed.append(temp_i)

    cnt = 0
    for line in line_arr_changed:
        strOfumbers = ""
        strNum = ""
        for element in line:
            if element.isnumeric():
                strOfumbers += element
        strNum = strOfumbers[0] + strOfumbers[-1]
        intNum = int(strNum)
        totalNum += intNum
        

        print(f"{lineArr[cnt]} -> num : {intNum}")
        cnt += 1

        if cnt > 20:
            break
    print(totalNum)