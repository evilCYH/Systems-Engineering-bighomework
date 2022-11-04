import jieba

fout = open('青桔-清洗分词.txt', 'a', encoding='utf-8')
f = open("青桔-清洗.txt",encoding='utf-8')
while True:
    line = f.readline()
    if line:
        messages = jieba.cut(line)
        message = "/ ".join(messages)
        # print ("/ ".join(messages))
        fout.writelines(message + '\n')
    else:
        break
f.close()
fout.close()

# messages = jieba.cut("万里长城是中国古代劳动人民血汗的结晶和中国古代文化的象征和中华民族的骄傲")   #默认精确模式
# #print (.join(messages))
# message = "/ ".join(messages)
# print(message)
# # print ("/ ".join(messages))