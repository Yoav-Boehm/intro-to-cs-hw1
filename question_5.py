def test(string1):
    list1 = string1.split("'")
    for i in range(0, len(list1) - 1):
        if len(list1[i]) == 0:
            list1.pop(i)
    for i in range(0, len(list1)):
        try:
            a = int(list1[i])
            list1[i] = a
#            tmp = ""
#            for j in range(1, len(list1[i]) - 1):
#                a = int(list1[i][j])
#                tmp += str(a)
#            final_num = int(tmp)
#            list1[i] = final_num
        except:
            None
    print(list1)
    if type(list1[0]) == type(2):
        list1[0] = str(list1[0])
    final_string = list1[0]
    temp = ""
    loop_var = 0
    print(list1)
    for i in range(2, len(list1)):
        if list1[i-1] == '+':
            if type(list1[i]) == type(2):
                temp = str(list1[i])
            final_string += list1[i]
        elif list1[i-1] == '*':
            loop_var = list1[i]
            temp = final_string
            for i in range(1, loop_var):
                final_string += temp
        else:
            a = str(list1[i])
            temp = final_string.replace(a, '')
            final_string = temp
        i += 1
    print(final_string)


test("'hello'*'3'+'     '+'g'-'l'")


