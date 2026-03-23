"""
请想办法取出下列`json`中所有的`英雄名称`和`英雄title`. 并将`英雄名称`和`英雄title`写入`names.txt`文件中.
"""
import json
with open("01作业.json", mode ="r", encoding ="utf_8") as f1,\
    open("01_作业_name.txt", mode = "w", encoding = "utf_8") as f2:
    f1_dic = json.loads(f1.read())
    print(f1_dic)
    for hero in f1_dic["hero"]:
        line = f"{hero['name']}-{hero['title']}\n"
        f2.write(line)



