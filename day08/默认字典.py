# 有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
#
# 即： {'k1': 大于66 , 'k2': 小于66}
l =  [11,22,33,44,55,66,77,88,99,90]
dic = {'bigger than 66':[],'llse than 66':[]}

for i in l:
    if i > 66:
        if dic.get('bigger than 66'):
            dic['bigger than 66'].append(i)
        else:
            dic['bigger than 66'] = [i]
    elif i < 666:
        if dic.get('llse than 66'):
            dic['llse than 66'].append(i)
        else:
            dic['llse than 66'] = [i]
print(dic)