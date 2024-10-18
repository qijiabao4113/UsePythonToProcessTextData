import os
import shutil

# 打开相关文件
try:
    f_in = open("task1.trainSentence.new", encoding='utf_8')
    f_out = open("exp1_1.txt", "w", encoding='utf_8')
except FileNotFoundError:
    print("ERROR!TestFileNotFound!")
    exit(-1)  # 出现异常终止程序
else:
    print("FileOpenSuccess!")
    # 按行读取文件内容
    for line in f_in:
        # 用制表符分割每行内容并赋值给列表
        lineData = line.split('\t')
        # 只要前五个元素
        f_out.write(
            lineData[0] + "\t" + lineData[1] + "\t" + lineData[2] + "\t" + lineData[3] + "\t" + lineData[4] + "\n")
    # 关闭相关文件
    f_in.close()
    f_out.close()

# 判断文件是否存在
if os.path.exists("exp1_train"):
    # 如果存在则删除再重新创建
    shutil.rmtree("exp1_train")
    os.mkdir("exp1_train")
    print("exp1_train was existed")
    print("system will delete it")
    print("exp1_test was deleted")
    print("system was recreated a new one")
else:
    # 如果不存在则直接创建
    os.mkdir("exp1_train")

try:
    # 将文件夹中的文件拷贝到新文件夹中
    shutil.copy("task1.trainSentence.new", "exp1_train")
    shutil.copy("task1.test.new", "exp1_train")
except FileNotFoundError:
    print("ERROR!TestFileNotFound!")
    exit(-1)  # 出现异常终止程序
else:
    print("FileCopySuccess!")
# 更换新的工作目录并打开相关文件
os.chdir("exp1_train")
# 用于存储关系类型
relationshipType = []

try:
    f_in = open("task1.trainSentence.new", encoding='utf_8')
except FileNotFoundError:
    print("ERROR!TestFileNotFound!")
    exit(-1)  # 出现异常终止程序
else:
    print("FileOpenSuccess!")
    # 按行读取文件内容
    for line in f_in:
        # 用制表符分割每行内容并赋值给列表
        lineData = line.split('\t')
        # 判断当前关系类型是否已经存在于存储关系的列表中，若存在就跳过
        if lineData[0] in relationshipType:
            continue
        else:
            # 若不存在那么将当前关系类型添加到存储关系的列表中
            relationshipType.append(lineData[0])
    # 关闭相关文件
    f_in.close()
# 获取关系列表的长度也就是关系类型的个数
relationshipTypeNum = len(relationshipType)
# 初始化一个变量用于记录行数和循环运行次数
i = 0
# 要把所有关系类型处理完循环才会结束
while i < relationshipTypeNum:
    # 不能忘记更新循环变量
    i = i + 1
    # 用循环次数的变量名作为文件名
    fileName = str(i) + '.txt'
    # 打开相关文件
    try:
        f_out = open(fileName, "w", encoding='utf_8')
        f_in = open("task1.trainSentence.new", encoding='utf_8')
    except FileNotFoundError:
        print("ERROR!TestFileNotFound!")
        exit(-1)  # 出现异常终止程序
    else:
        # 按行读取文件内容
        for line in f_in:
            # 用制表符分割每行内容并赋值给列表
            lineData = line.split('\t')
            # 判断当前关系类型是否等于当前循环查找的关系类型
            if lineData[0] == relationshipType[i - 1]:
                # 如果是则将当前行写入文件
                f_out.write(lineData[0] + "\t" + lineData[1] + "\t" + lineData[2] + "\t" + lineData[3] + "\t" + lineData[4] + "\t""\n")
        # 关闭相关文件
        f_in.close()
        f_out.close()

# 把工作路径转移到上一级目录
os.chdir("../")
# 判断文件是否存在
if os.path.exists("exp1_test"):
    # 如果存在则删除再重新创建
    shutil.rmtree("exp1_test")
    os.mkdir("exp1_test")
    print("exp1_test was existed")
    print("system will delete it")
    print("exp1_test was deleted")
    print("system was recreated a new one")
else:
    # 如果不存在则直接创建
    os.mkdir("exp1_test")
# 将文件夹中的文件拷贝到新文件夹中
try:
    shutil.copy("task1.test.new", "exp1_test")
except FileNotFoundError:
    print("ERROR!TestFileNotFound!")
    exit(-1)  # 出现异常终止程序
else:
    print("FileCopySuccess!")

os.chdir("exp1_test")

# 初始化一个变量用于记录行数和循环运行次数
i = 0
# 要把所有关系类型处理完循环才会结束
while i < relationshipTypeNum:
    # 不能忘记更新循环变量
    i = i + 1
    # 用循环次数的变量名作为文件名
    fileName = str(i) + '_test.txt'
    # 用于创建索引的名字序号
    index = "index" + str(i) + '.txt'
    # 打开相关文件
    try:
        f_out = open(fileName, "w", encoding='utf_8')
        f_in = open("task1.test.new")
        f_index = open(index, "w", encoding='utf_8')
    except FileNotFoundError:
        print("ERROR!TestFileNotFound!")
        exit(-1)  # 出现异常终止程序
    else:
        print("FileOpenSuccess!")
        # 记录发现关系类型的行数用于建立索引
        k = 1
        # 按行读取文件内容
        for line in f_in:
            # 用制表符分割每行内容并赋值给列表
            lineData = line.split('\t')
            # 判断当前关系类型是否等于当前循环查找的关系类型
            if lineData[0] == relationshipType[i - 1]:
                # 如果是则将当前行写入文件
                f_out.write(lineData[0] + "\t" + lineData[1] + "\t" + lineData[2] + "\t" + lineData[3])
                # 将当前行的索引写入索引文件
                f_index.write(str(k) + "\n")
            # 每次读取一行后记录当前行数
            k = k + 1
        # 关闭相关文件
        f_in.close()
        f_out.close()
        f_index.close()
print("SystemRunEnd!")
