import re
def clean(text):
    text = re.sub(r"(回复)?(//)?\s*@\S*?\s*(:| |$)", " ", text)  # 去除正文中的@和回复/转发中的用户名
    text = re.sub(r"\[\S+\]", "", text)      # 去除表情符号
    text = re.sub(r"#\S+#", "", text)      # 保留话题内容
    URL_REGEX = re.compile(
        r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))',
        re.IGNORECASE)
    text = re.sub(URL_REGEX, "", text)       # 去除网址
    text = text.replace("转发微博", "")        # 去除无意义的词语
    text = text.replace("电单车", "")
    text = text.replace("单车", "")
    text = text.replace("美团", "")
    text = text.replace("哈啰", "")
    text = text.replace("青桔", "")
    text = text.replace("共享", "")
    text = re.sub(r"\s+", " ", text) # 合并正文中过多的空格
    return text.strip()

fout = open('青桔-清洗.txt', 'a', encoding='utf-8')
f = open("青桔.txt",encoding='utf-8')
while True:
    line = f.readline()
    if line:
        print (clean(line))
        fout.writelines(clean(line) + '\n')
    else:
        break
f.close()
fout.close()