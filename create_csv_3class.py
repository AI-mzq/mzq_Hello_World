import os

def get_files(file_dir):
    '''
    :param file_dir: 数据路径
    :return: 返回图片路径和标签
    '''
    files_list = []
    for file in os.listdir(file_dir):
        if file.startswith('20-32'):
            label = '0'
        # elif file.startswith('8-14'):
        #     label = '1'
        # elif file.startswith('15-19'):
        #     label = '2'
        # elif file.startswith('20-32'):
        #     label = '3'
        elif file.startswith('33-43'):
            label = '1'
        elif file.startswith('44-60'):
            label = '2'
        # elif file.startswith('60-100'):
        #     label = '6'
        # elif file.startswith('8'):
          #   label = '7'
        # else:
          #   label = '8'
        files_list.append([file,label])

    print(files_list)
    return files_list

# 写CSV文件
def write_csv(files_list,file_csv,mode='w'):
    with open(file_csv,mode) as f:
        for file in files_list:
            #print(file)
            line = ','.join(file)
            f.write(line+'\n')

def create_csv(data_dir,csv_path):
    filelist = get_files(data_dir)
    csv = write_csv(filelist, file_csv=csv_path, mode='w')
    print(csv)
    return csv


if __name__ == '__main__':
    data_dir = './UTKFace-mzq'
    csv_path = './UTKFace_train_mzq.csv'
    create_csv(data_dir,csv_path)
    # get_files(data_dir)
