import re

test_date = '他的生日是2016-12-12 14:34,是个可爱的小宝贝.二宝的生日是2016-12-21 11:34,好可爱的.'
mat = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", "2020-01-02 ")
print(mat.group())
