import csv
import json

'''
json_load:读取json文件
return: json数据格式
'''

def json_load(filePath):
    with open(filePath, mode='r', newline='', encoding='utf8') as file:
        return json.load(file)


'''
json_dump:写入json文件
data： 写入的数据
filePath:文件路径及文件 示例* d:\\vsd\\csv\\123.json
'''
def json_dump(filePath, data):
    with open(filePath, mode='w', newline='', encoding='utf8') as file:
        json.dump(data, file,ensure_ascii=False)



'''
json_dumps:将数据转换成字符串
data: [{'username':'zhangsan','sex':6},{'username':'lisi','sex':3}]
return: 返回为当前数据的字符串类型
'''
def json_dumps(data):
    return json.dumps(data)

def write_csv(file_path,data_list_name):
    with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for row in data_list_name:
            writer.writerow(row)