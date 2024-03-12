
# file_name = "scj_4"
file_names = ["11"]

import csv

def convert_file(input_path: str, file_name: str, save_path: str):
    project_path = input_path
    file_path = project_path + '/' + file_name + '.csv'

    # 打开CSV文件并读取内容
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        # 使用csv.DictReader来读取文件
        csv_reader = csv.DictReader(csvfile)
        
        data_list = csv_reader.fieldnames
        # data_list[0] = data_list[0][1:]
        data_list[-1] = data_list[-1][:-1]

        data_list = [i[1:] for i in data_list]


    print(data_list)

    # 将列表中的逗号转换为换行符
    csv_data = '\n'.join(data_list)

    # 将处理后的数据保存为CSV文件
    output_file_path = save_path + '/' + file_name + '_output.csv'
    with open(output_file_path, 'w', encoding='utf-8') as csvfile:
        csvfile.write(csv_data)
    pass


def convert_csv2dat(csv_path: str, dat_path: str):
    """
    intro:
        transform file from .csv to .dat.
        add time line at the first line.
    """
    # 读取.csv文件
    with open(csv_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        data = list(csv_reader)

    # 写入.dat文件
    with open(dat_path, 'w') as dat_file:
        for index, value in enumerate(data, start=1):
            dat_file.write(f"{index}, {value[0]}\n")


if __name__ == "__main__":
    # test 1
    # input_path = "/home/yingmuzhi/NotesML/src/csv"
    # save_path = "/home/yingmuzhi/NotesML/src/temp_csv"
    # for file_name in file_names:
    #     convert_file(input_path=input_path, file_name=file_name, save_path=save_path)

    # test 2
    import os
    input_path = "/home/yingmuzhi/NotesML/src/temp_csv"
    save_path = "/home/yingmuzhi/NotesML/src/software_origin"
    for root, dirs, files in os.walk(input_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            save_file_path = os.path.join(save_path, file_name[:-4]+'.dat')
            convert_csv2dat(file_path, save_file_path)


