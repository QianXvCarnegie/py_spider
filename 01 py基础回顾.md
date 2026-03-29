# 

# 第一节,  python基础内容回顾



## 一. 关于爬虫的特殊性

爬虫是一个很蛋疼的东西, 可能今天讲解的案例. 明天就失效了. 所以, 不要死盯着一个网站干.  要学会见招拆招(爬虫的灵魂) 



爬虫程序如果编写的不够完善. 访问频率过高. 很有可能会对服务器造成毁灭性打击, 所以, 不要死盯着一个网站干. 请放慢你爬取的速度. 为你好, 也为网站好. 



腾讯, 阿里, 字节, 小红书, 美团...的网站, 反爬手段很**残忍**. 新手不要去挑战这种大厂. 等你有实力了. 慢慢研究(哪个都要研究很久....)



gov的网站, 非必要, 不爬取. 非要爬取. 请一定降低访问频率. 为你好....



不要以为gov的网站好欺负. 那是地方性的网站. 中央的很多重要网站都有非常强力的防护措施(瑞数等...) 这种. 愿意搞的. 自己研究. 樵夫搞不定....

网站防护很强. 但是服务器很垃圾. 

都是外包干的活....



**爬虫只能爬 你看得见的东西!!!!!** 

**个人信息不能碰.** 

**尽量不要妨碍人家网站服务器的正常运营.**   



网站的多变性: 这个是爬虫的魅力. 我们要全方位的去思考. 就像找漏洞一样. 思维逻辑不可能是固定的. 达到目的即可. 不要死磕牛角尖. 要不然, 你会死的很惨.... **要学会见招拆招**. 



关于憋代码这个事.  要憋. 一定要憋. 让你憋主要有两个原因. 

1. **简单的语法使用错误. 不憋记不住**
2. **复杂的程序逻辑. 不憋培养不出来独立思考能力.** 
3. **一定要有独立解决问题的能力.** 



## 二. 爬虫  py基础

### 2.1 基础语法相关

 1. if条件判断

    页面结构不统一, 会有两种页面结构

    ```python
    # 伪代码, 理解含义(思路)
    提取器1 = xxxx  #  用来提取页面中内容的
    提取器2 = xxxxxx
    
    # 页面有可能是不规则的。 张飞， 潘长江 
    结果1 = 提取器1.提取(页面)
    if 结果1:
        有结果. 存起来
    else:
        没有结果. 
        结果2 = 提取器2.提取(页面)
    ```
    
    相信我, 上面的逻辑并不难. 但是, 到了后面很多小伙伴容易踩坑. 我们完全没必要用一个提取器获取所有的数据. 完全没必要.....
    
    
    
    
    
 3. 关于True和False

    

    ```python
    # 几乎所有能表示为空的东西. 都可以认为是False
    print(bool(0))
    print(bool(""))
    print(bool([]))
    print(bool({}))
    print(bool(set()))
    print(bool(tuple()))
    print(bool(None))
    # 上面这一坨全是False, 相反的. 都是真. 利用这个特性. 我们可以有以下的一些写法
    
    # 伪代码, 理解逻辑. 
    结果 = 提取器.提取(页面)
    if 结果:
        有结果. 我要保存结果
    else:
        没结果. ......
    ```
    
    

### 2.2  字符串  (万恶之源, 必须要会的, 而且要熟..)

​	字符串在`爬虫`里. 必须要知道的几个操作:

  1. split()

     split,  做切割的. 

     ```python
     s = "10,男人本色,100000万"  # 你在网页上提取到这样的一段数据. 现在我需要电影名称
     tmps = s.split(",")  #split()返回列表
     name = tmps[1]
     print(name)  # 男人本色
     
     # 切割后. 把三个结果直接怼给三个变量
     id, name, money = s.split(",")  
     ```

     

  2. replace()

     replace, 字符串替换

     ```python
     # 这是你从网页上拿到的东西
     s = "我      \t\t\n\n爱   黎       明    "   
     
     # 干掉空格, \t, \n
     s1 = replace(" ", "").replace("\t", "").replace("\n", "")  
     print(s1)  # 我爱黎明
     ```

     

  3. join()

     join, 将列表拼接为一个完整的字符串

     ```python
     # 由于网页结构的不规则, 导致获取的数据是这样的. 
     lst = ["我妈", "不喜欢", "黎明"]  
     
      # 用空字符串把lst中的每一项拼接起来
     s1 = "".join(lst) 
     print(s1)  # 我妈不喜欢黎明
     
     
     lst2 = ["\n\r","\n\r","周杰伦\n\r", "\n不认识我\r"] 
     s2="".join(lst2).replace("\n","").replace("\r", "")
     print(s2)  # 周杰伦不认识我
     ```

     

  4. f-string

     格式化字符串的一种方案

     ```python
     s = "周杰伦"
     s1 = f"我喜欢{s}"  #  它会把一个变量塞入一个字符串
     print(s1)  # 我喜欢周杰伦
     
     k = 10085
     s2 = f"我的电话号是{k+1}" # 它会把计算结果赛入一个字符串
     print(s2)  # 我的电话号是10086
     
     # 综上, f-string的大括号里, 其实是一段表达式.能计算出结果
     ```




### 2.3  列表

列表, 我们未来遇见的仅次于字符串的一种数据类型. 它主要是能承载大量的数据. 理论上. 你的内存不炸. 它就能一直存

1. 索引, 切片

   列表的索引和切片逻辑与字符串完全一致

   ```python
   lst = ["赵本山", "王大陆", "大嘴猴", "马后炮"]
   item1 = lst[2]  # 大嘴猴
   item2 = lst[1]  # 王大陆
   
   lst2 = lst[2:]
   print(lst2)  # ["大嘴猴", "马后炮"]
   
   # 注意, 如果列表中没有数据. 取0会报错
   lst = []
   print(lst[0])  # 报错, Index out of bounds
   
   # 注意, 如果给出的索引下标超过了列表的最大索引. 依然会报错
   lst = ["123", "456"]
   print(lst[9999])  # 报错, Index out of bounds
   
   ```

   

2. 删除

   删除数据(不常用, 好不容易爬到的数据. 为什么要删)

   ```python
   lst.remove("周润发")  #  把周润发删掉
   ```

   

3. 修改

   ```python
   lst = ["赵本山", "王大陆", "大嘴猴", "马后炮"]
   lst[1] = "周杰伦"
   print(lst)  # ["赵本山", "周杰伦", "大嘴猴", "马后炮"]
   ```

   

4. enumerate

   ```python
   # enumerate
   lst = [11, 22, 33, 44, 55]
   
   # 得到的是一个元组. (index, item)
   for i, item in enumerate(lst):
       print(i, item)
   
   ```

   

### 2.4  字典

字典可以成对儿的保存数据. 

1. 增加

   ```python
   dic = {}
   dic['name'] = '樵夫'
   dic['age'] = 18
   
   print(dic)  # {"name": "樵夫", "age": 18}
   ```
   
   
   
2. 修改

   ```python
   dic = {"name": "樵夫", "age": 18}
   dic['age'] = 19
   print(dic)  # {"name": "樵夫", "age": 19}
   ```

   

4. 查询(重点)

   ```python
   dic = {"name": "樵夫", "age": 18}
   
   a = dic['name']  # 查询'name'的值
   print(a)  # 樵夫
   
   c = dic['哈拉少']   # 没有哈拉少. 报错
   d = dic.get("哈拉少")  
   # 没有哈拉少, 不报错. 返回None. 它好. 它不报错
   
   ```
   
   循环

   ```python
   dic = {"name": "樵夫", "age": 18}
   for k in dic:  # 循环出所有的key
       print(k)  
       print(dic[k])  # 获取到所有的value并打印
   ```
   
   嵌套
   
   ```python
   dic = {
       "name": "王峰",
       "age": 18,
       "wife": { "name": "章子怡","age": 19 },
       "children": 
       [{'name':"胡一菲", "age": 19},
           {'name':"胡二菲", "age": 18},
           {'name':"胡三菲", "age": 17},]
   }
   
   # 王峰的第二个孩子的名字
   print(dic['children'][1]['name'])
   # 王峰所有孩子的名称和年龄
   for item in dic['children']:
       print(item['name'])
       print(item['age'])
   ```
   
   
   

### 2.5  字符集和bytes

字符集, 记住两个字符集就够了. 一个是utf-8, 一个是gbk. 都是支持中文的. 但是utf-8的编码数量远大于gbk. 我们平时使用的最多的是utf-8

介绍：what   why   how ——是什么，为什么，怎么用

```python
 0101010101111000101 => 二进制的数字.
 进而. 计算机就可以完美的表示出来整数...
 需要做一个转化的规则(通用)
 1    我
 10   爱
 101  你
 这种转化规则叫 字符集...
 字符集里面放着 二进制和我们文字符号的一一对应关系

 ascii 美国人发明的. 只是编排了一些老美用到的英文文字, 符号, 特殊的操作
 ascii一共编码了128个文字和符号, 刚好是7个二进制0和1
 0000 0000
 ...
 0111 1111
 ascii的长度: 8bit,前面那个0是为了留着扩展的...
 8bit代表是1个字节...

 单纯的靠ascii最前面的0, 这一位是不够用的..
    ascii扩充了1倍....
    0000 0000 0000 0000  瞬间可编码数据量从 256 扩大到65536个
    基本上满足了大多数国家的使用了.

    长度是 16bit, 2byte
    扩充完之后. 它是制定了一个标准. ANSI
    ANSI. 下发给各个国家.你们自己去编排...
    各个国家按照自己的喜好. 进行了自己的编码.
    65536
    20063  ->  中
    20063  ->  あ

    中国人把ANSI进行编排之后. 形成了专门属于我们的编码: GB码
    GB-2312  GBK  GB-18030

    到今天. 我们操作系统默认使用的还是该编码逻辑.

    后来发现. ANSI这个标准. 省事儿. 但是不好用. 各个国家都有自己的规则
    转换很头疼....

    能不能把全世界所有的国家的文字放在一起...

    编排的时候发现文字和符号远超过65536.
    再次进行扩充1倍, 最终扩充到32bit, 4byte
    0000 0000 0000 0000 0000 0000 0000 0000

    全球统一编码. 叫unicode, unicode是没办法在网络通信和传输过程中使用
    存储一个字母:
    ascii: 1111 1111
    ANSI/gbk:  0000 0000 1111 1111
    unicode: 0000 0000 0000 0000 0000 0000 1111 1111

    unicode最多在内存层面使用...
    我们今天的程序. 在执行的时候. 内存层面使用的就是unicode

    s = "我爱你"

    为了保证数据的传输和存储. 聪明的科学家. 发明了可变长度的unicode
    utf-8, 最小的一个字符长度是8bit, 1byte  -> 我们今天用的最多的字符集就是它.
    utf-16, 最小的一个字符长度是16bit, 2byte
    utf-32, 最小的一个字符长度是32bit, 4byte

    utf-8的逻辑:
        ascii范围的东西: 1byte, 8bit
        欧洲文字: 2byte, 16bit
        中文: 3byte, 24bit

    总结:
        ascii: 1byte, 8bit
        gbk: 2byte, 16bit
        utf-8:
            ascii范围的东西: 1byte, 8bit
            欧洲文字: 2byte, 16bit
            中文: 3byte, 24bit

    所有的文字的传输和存储必须要转化成gbk或者utf-8来进行.
```

问题练习：

```python
s = "我爱你"
# 把字符串从内存中转化成字节. 然后才可以传输或者存储

bs = s.encode('gbk')     ？？多少字节
print(bs)  # 6个字节，gbk——1个字符2个字节

bs = s.encode('utf_8')     ？？多少字节
print(bs)  # 9个字节，utf_8——1个字符2个字节

\xff  -> 一个字节 -> 8bit -> 0~255   1111 1111


??多少个字节
 1byte -> 8bit  -> ascii
b'\xea\xabc\xcc\x1ab\xcd1f\xca'  
= b'\xea  \xab  \x63  \xcc   \x1a   b   \xcd  1  f   \xca'
解：
print(b'\xea\xabc\xcc\x1ab\xcd1f\xca'.__len__())
# 10个字节。
# why：\xabc：\xff是一个字节，多出来的"c" = "\x63"是一个字节
print(b"c" == b"\x63")  # True 
```

基础使用

```py
# 编码
s = "我爱你"
bs = s.encode('utf-8')  

# 解码
s = bs.decode("utf-8")
print(s)
```

记住, bytes不是给人看的. 是给机器看的. 我们遇到的所有文字, 图片, 音频, 视频. 所有所有的东西到了计算机里都是字节. 



### 2.6 文件操作

python中. 想要处理一个文件. 必须用open()先打开一个文件

语法规则

```python
f = open(文件名, mode="模式", encoding='文件编码')

f.read() | f.write()

f.close()
```

文件名就不解释了. 

模式: 
	我们需要知道的主要有4个. 分别是: r, w, a, b

1. r  只读模式. 含义是, 当前这一次open的目的是读取数据. 所以, 只能读. 不能写
2. w 只写模式. 含义是, 当前这一次open的目的是写入数据. 所以, 只能写, 不能读
3. a 追加模式. 含义是, 当前这一次open的目的是向后追加. 所以, 只能写, 不能读
4. b 字节模式. 可以和上面三种模式进行混合搭配. 目的是. 写入的内容或读取的内容是字节. 

encoding: 文件编码. 只有处理的文件是文本的时候才能使用. 并且mode不可以是`b`.   99%的时候我们用的是`utf-8`

另一种写法:

```python
with open(文件名, mode=模式, encoding=编码) as f:
    pass
```

这种写法的好处是, 不需要我们手动去关闭`f`

读取文件一行一行的数据:

```python
with open("躺尸一摆手.txt", mode="r", encoding="utf-8") as f:
    for line in f:  # for循环可以逐行的进行循环文件中的内容
        print(line)
```

w模式的一个坑

```python
# 网页上抓到的数据
lst = ["周杰伦", "林俊杰", "张无忌"]

for item in lst:
    f = open("人名.txt", mode="w", encoding="utf-8")
    f.write(item)
f.close()

# bug的现象是, 写入的数据只留下了最后一条...
# 因为w模式会每次清空文件，重写

# 调整:
lst = ["周杰伦", "林俊杰", "张无忌"]
f = open("人名.txt", mode="w", encoding="utf-8")
for item in lst:
    f.write(item)
    f.write("\n")  # 手动写个\n 换行
f.close()
```



### 3.7  关于函数

在代码量很少的时候, 我们并不需要函数.

 但是一旦代码量大了. 一次写个几百行代码. 调试起来就很困难. 此时, 建议把程序改写成一个一个具有特定功能的函数. 方便调试. 也方便代码的重用

```python
def 函数名(形式参数):
    # 函数体
    return 返回值
```

总结, 函数的好处就是, 以后需要该功能. 不用再写重复代码了. 



### 3.8 关于模块

模块是啥? 模块就是已经有人帮我们写好了的一些代码, 这些代码被保存在一个py文件或者一个文件夹里. 我们可以拿来直接用

在python中有三种模块.

1. python内置模块 .

   ​    不用安装. 直接导入就能用

   

2. 第三方模块.

   ​	需要安装. 安装后. 导入就可以用

   

3.  自定义模块(新手先别自己定义模块)

   ​	直接导入就能用

   

搞爬虫.必须要了解的一些python内置模块

1. #### time模块

   ```python
   import time
   ```

   时间戳

   ```python
   time.time()  # 获取到时间戳
   
   # 系统的时间戳, python的时间单位是  秒
   # 浏览器上计算的时间戳的单位是    毫秒.
   
   # 统一单位...我们是要模仿浏览器的
   tm = int(time.time() * 1000)  # int()取整
   #  1719586087142  # py
   #  1719586093546  # js
   ```

   时间暂停

   ```python
   time.sleep(999)  # 让程序暂停999秒
   ```

   

2. #### os模块

   ```python
   import os
   
   #  判断 文件 或者 文件夹 是否存在
   os.path.exists()  
   # 路径拼接
   os.path.join()    
   # 创建文件夹
   os.makedirs()    
   # 判断是否是文件夹
   os.path.isdir('./a/b/c/d/')
   
   # 获取某路径的文件夹
   file_path = "./abc/def/a/c/d.txt"
   os.path.dirname(file_path)  # ./abc/def/a/c 路径
   os.path.basename(file_path)  # d.txt 尾名
   ```

    创建文件的完整程序逻辑:

   ```py
   file_path = './ab/c/d/e/f/t.txt'
   
   # 判断文件夹路径是否存在. 如果存在. 才可以创建
   if not os.path.isdir(os.path.dirname(file_path)):
       os.makedirs(os.path.dirname(file_path))
   
   ```

   

3. #### json模块(重中之重)

   json是一种类似字典一样的东西.  对于python而言, json是字符串. 

   例如, 

   ```python
   s = '{"name": "jay", "age": 18}'
   ```

   如何来转化它. 

   **<span style="background-color:yellow;color:red;">json字符串 => python字典</span>**

   ```python
   dic = json.loads(s)
   ```

   **<span style="background-color:yellow;color:red;">python字典 => json字符串</span>**

   ```python
   s = json.dumps(dic)
   ```

   特别注意，一个爬虫小坑.

   ```py
   # 在前端，json无空格："{"money":null,"married":false}"
   
   # 在py解释器，会自动给json加空格: {"money": null, "married":false}
   
   import json
   s = '{"name": "汪峰", "age" : 18, "money" : null}'
   
   dic = {'money': None, 'married': False, 'name': '汪峰', 'age': 18}
   # 转化的时候. 增加一个参数
   s = json.dumps(dic, separators=(',', ':'))
   print(s)
   # ctrl+鼠标点 dumps：进入源码，复制 (',', ':')
   ```

   

4. #### random模块

   随机. 没别的用处.生成随机数

   ```python
   import random
   
   i = random.randint(1, 10) 
   #存在10，不用专门记，不确定的时候多打印打印试试
   print(i) 
   
   lst =[11,22,33]
   print(random.choice(lst))
   ```

   

5. #### 异常处理(重中之重)

   写爬虫时. 非常容易遇到问题. 但这些问题不一定是我们程序的问题. 

   比如：网络波动、服务器本身压力太大—— 导致本次请求失败.  此时, 我们的程序会崩溃.   怎么办?

   

   程序如果本次请求失败了. 那就重新来一次.
   
   ```python
   import traceback
   try: # 尝试...
       print(1/0)  # 出事儿了
       
   except Exception as e:  # 记录出错  Exception是错误的根
       # print(e)可以
       print(traceback.format_exc()) 
       # traceback 不仅记录 出错内容，还会记录 哪个文件哪一行
       
   ```
   
   主动抛出异常：raise   （用得比较少）
   
   ```py
   def cul_a_div_b(a, b):  # 计算a➗️b
       if b == 0:
           raise ZeroDivisionError("垃圾b，b不能为0")
       return a / b
   # 作为程序的设计人员，程序已经没有办法继续进行下去了，主动抛出错误
   ```
   
   实战 模版思路：
   
   ```py
   #实战逻辑：我要抓取 99页的数据，程序运行后，我去睡觉...让程序中间不中断
   import traceback,time
   
   f1 = open("错误_url.log", mode = "a", encoding = "utf_8")  # 看看错误是啥
   f2 = open("错误.log", mode = "a", encoding = "utf_8")  # 看看错误在哪
   
   def send_requests(page):
       for i in range(5):
           try:
               print("{page}页抓取完毕")
               time.sleep(1)
               return
           except Exception as e:
               # f2是为了看错误信息
               f2.write(f"{page}出现了问题")
               f2.write(traceback.format_exc())
               f2.write("\n")
               time.sleep(1)
   
   	# 模式走到这里，重试5次，仍未得到数据
   	# 所以把url和参数记录下来，第二天早上再去检查
   	f1.write(f"{page}出现了问题")  
   	f1.write("\n")
       """
   	f1只写page，明天
   	 for i in f1: 
               发请求(i)
   	# 全再跑一遍,量大管饱，轻松直接
       """
   
   def main():
       for page in range(1, 100):
           send_requests(page)
           
   if __name__ == "__main__" :
       main()
   	f1.close()
       f2.close()
   ```
   
   



