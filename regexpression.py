import re
data='''555-555-5555
222-222-2222
3333-333-333'''

re_string=r"(\d{3})(\-)(\d{3})(\-)(\d{4})"
regen=re.compile(re_string)
matches=re.finditer(re_string,data)
for i in matches:
    print(i.group())




