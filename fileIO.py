# coding=utf-8
# 打开一个文件
import time

fo = open("/Users/maxiaoshi/PycharmProjects/untitled/foo.txt", "r+")
string = fo.readline()
findCount = {}
lines = 0
print time.localtime(time.time())
while 1:
    line = fo.readline()
    lines += 1
    lines += 1
    if not line:
        break
    if line.find("select") < 0:
        continue
    keyword = line[line.index("from") + 5:][:line[line.index("from") + 5:].index(" ")]
    count = findCount.get(keyword, 0)
    findCount[keyword] = count + 1

print findCount
print lines
print time.localtime(time.time())
fo.close()
