import os
import pickle
import subprocess
from subprocess import call


DATA_DIR = os.path.join('/home/jlan/Projects/spider/crop_qa/sent2vec/data')
FASTTEXT_EXEC_PATH = '/home/jlan/Projects/spider/crop_qa/sent2vec/sent2vec/fasttext'
MODEL_FILE = os.path.join(DATA_DIR, 'agri_model.bin')    # 训练生成的模型
TRAIN_FILE = os.path.join(DATA_DIR, 'train.txt') # 处理后生成的训练文件

CORPORA = os.path.join(DATA_DIR, 'qs_processed.txt')
TEST_FILE = os.path.join(DATA_DIR, 'sim_qs.txt') # 测试文件


def train(fasttext_exec_path, input_file, output_model):
    # train_command = '{} sent2vec -input {} -output {}'\
    #     .format(fasttext_exec_path, input_file, output_model)

    train_command = '{} sent2vec -input {} -output {} -minCount 8 -dim 700 -epoch 9 -lr 0.2 -wordNgrams 2 -loss ns ' \
                    '-neg 10 -thread 20 -t 0.000005 -dropoutK 4 -minCountLabel 20 -bucket 4000000'\
        .format(fasttext_exec_path, input_file, output_model)
    print(train_command)
    call(train_command, shell=True)


def get_nnSent(fasttext_exec_path, model_file, corpora, test_file, result, k=3):
    """执行"fasttext nnSent model.bin corpora.txt [k]，找到相似句子"""
    test_command = '{} nnSent {} {} {} {} > {}' \
        .format(FASTTEXT_EXEC_PATH, model_file, corpora, test_file, k, result)
    print(test_command)
    # call(test_command, shell=True)
    result = subprocess.check_output(test_command, shell=True)
    print(result)
    # handle = open(result, 'a+')
    # subprocess.Popen(test_command, stdout=handle, shell=True)


def compute_precision(result, k):
    std_results = pickle.load(open(os.path.join(DATA_DIR, 'zhubajie/questions_dict_processed.pkl'), 'rb'))
    num_std_q = len(std_results) # 标准问题数量
    num_sim_q = sum([len(i) for i in std_results.values()]) # 相似问题数量，一个标准问题可能对应多个相似问题
    num_correct = 0  # 预测正确的数量

    # 从get_nnSent函数生成的结果中读取，每k+1行为一个单元，第一行是相似问题，后k行是找出的最接近的k个标准问题
    with open(result, 'r') as f:
        lines = [line.strip() for line in f.readlines()[1:] if line.strip()]
    results_each = [lines[i:i+k+1] for i in range(0, len(lines), k+1)]

    for result_each in results_each:
        sim_q = result_each[0]  # 相似问题
        std_qs = [v.split(',') for v in result_each[1:]] # 预测出的标准问题
        # print('sim: ', sim_q)
        # print(std_qs)
        find = False
        for j in range(k):
            if sim_q in std_results.get(std_qs[j][0].strip()): # 从相似问题预测出每一个标准问题中反向查找相似问题，如果找到该相似问题，则预测成功
                num_correct += 1
                find = True
                # print('success predict std: ', std_qs)
                break
        if not find:
            print('sim: ', sim_q)
            print('failure predict std: ', std_qs)
    print('num_correct:', num_correct)
    print('num_std_q:', num_std_q)
    print('num_sim_q:', num_sim_q)
    print('accuracy: ', num_correct/num_sim_q)


if __name__ == '__main__':
    train(FASTTEXT_EXEC_PATH, TRAIN_FILE, MODEL_FILE)
    # result = 'result.txt'
    # k = 3
    # get_nnSent(FASTTEXT_EXEC_PATH, MODEL_FILE, CORPORA, TEST_FILE, result, k)
    # compute_precision(result, k)