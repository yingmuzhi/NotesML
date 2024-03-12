import csv

# 读取.csv文件
with open('/home/yingmuzhi/NotesML/src/temp_csv/11_output.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    data = list(csv_reader)

# 写入.dat文件
with open('/home/yingmuzhi/NotesML/src/temp_csv/11_output.dat', 'w') as dat_file:
    for index, value in enumerate(data, start=1):
        dat_file.write(f"{index}, {value[0]}\n")