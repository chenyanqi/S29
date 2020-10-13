import re
phone_number = input('please input your phone:')

if re.match('^(13|14|15|17|16|18|19)[0-9]{9}$',phone_number):
    print('合法的手机号')
else:
    print('不是合法的手机号')