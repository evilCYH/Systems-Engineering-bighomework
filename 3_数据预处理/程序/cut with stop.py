import jieba


def stopwordslist(filepath):  # 定义函数创建停用词列表
    stopword = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]  # 以行的形式读取停用词表，同时转换为列表
    return stopword


def cutsentences(sentences):  # 定义函数实现分词
    # print('原句子为：' + sentences)
    cutsentence = jieba.lcut(sentences.strip())  # 精确模式
    # print('\n' + '分词后：' + "/ ".join(cutsentence))
    stopwords = stopwordslist(filepath)  # 这里加载停用词的路径
    lastsentences = ''
    for word in cutsentence:  # for循环遍历分词后的每个词语
        if word not in stopwords:  # 判断分词后的词语是否在停用词表内
            if word != '\t':
                lastsentences += word
                lastsentences += "/ "
    return(lastsentences)


filepath = 'C:/Users/13391/Desktop/系统工程/DataScienceAssignment/src/2_Preprocessing/stop_words.txt'
stopwordslist(filepath)

fout = open('青桔-清洗分词去停用词.txt', 'a', encoding='utf-8')
f = open("青桔-清洗.txt",encoding='utf-8')
while True:
    line = f.readline()
    if line:
        fout.writelines(cutsentences(line) + '\n')
    else:
        break
f.close()
fout.close()
# sentences = '咱/ 就是说/  / 你/ 是/ 真的/ 13/ 我前/ 一分钟/ 刚/ 取消/ 了/ 续费/ 美团/ 单车/ 下/ 一分钟/ 再/ 找车/ 地图/ 上/ 一辆/ 都/ 没有/ 了/ 我/ 以为/'

# cutsentences(sentences)
