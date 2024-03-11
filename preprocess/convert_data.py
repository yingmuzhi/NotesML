
# file_name = "scj_4"
file_names = ["scj_4", "scj_5", "scj_6", "scj_7", "scj_8", "scj_9", "scj_b_2", "scj_b_3", "scj_b_4", "scj_b_5", "scj_b_6",
              "scj_b_7", "scj_b_8", "scj_b_9", "scj_b_10", "scj_b_11", "scj_b_12", "scj_b_13", "scj_b_14",
              "scj_b_15", "scj_b_16", "scj_b_17", "scj_b_18", "scj_b_19"]

import csv

def convert_file(file_name: str):
    project_path = "D:\\shichaojing_data\\data\\20231228_MCU\\result\\generate_data\\"
    file_path = project_path + file_name + '.csv'

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
    output_file_path = project_path + file_name + '_output.csv'
    with open(output_file_path, 'w', encoding='utf-8') as csvfile:
        csvfile.write(csv_data)
    pass


if __name__ == "__main__":
    for file_name in file_names:
        convert_file(file_name)

