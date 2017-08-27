import re
import os
import jieba
import time
import json
import pickle
import random
from functools import partial
from pymongo import MongoClient
from functools import reduce
from itertools import combinations
from multiprocessing import Pool
from concurrent.futures import ProcessPoolExecutor

DATA_DIR = os.path.join('/home/jlan/Projects/nlp/crop_qa/sent2vec/data')
TARGET_FILE = os.path.join(DATA_DIR, 'qs_processed.txt') # 处理后生成的文件


def cut_sentences(sentences):
    """分句"""
    result = re.split('[。.！!？?\n]', sentences)
    result = [i.strip() for i in result if i.strip()]
    return result


def cut_words(sentence, stop_words):
    """分词"""
    word_list = jieba.cut(sentence)
    word_list = [word.strip() for word in word_list if word.strip() and word.strip() not in stop_words]
    # word_list = [word.strip() for word in word_list if word.strip()] # 不去停用词
    return word_list


def dump_text_to_disk(words, target_file):
    """把预处理后的文本写入文件，每次一句"""
    with open(target_file, 'a+') as f:
        f.write(words+' \n')


def process_data(data, stop_words, target_file):
    # 对每一行进行处理，一行可能有多句
    line = re.sub('<.*?>', '', data).strip()
    if line:
        words = cut_words(line, stop_words)
        dump_text_to_disk(' '.join(words), target_file)


def get_data():
    """从mongodb获取数据"""
    client = MongoClient('localhost', 27017)
    db = client['agri_resource']
    collection = db['agri_qa']
    rice_data = collection.find()
    ans = [''.join(d['title']) for d in rice_data]
    # qs = [d['title'] for d in rice_data]
    return ans

    # client = MongoClient('localhost', 27017)
    # db = client['agri_resource']
    # collection = db['agri_qa']
    # rice_data = collection.find({'crop': '水稻'})
    # print(rice_data.count())
    # for data in rice_data:
    #     content = re.sub('<.*?>', '', ''.join(data['content'])).strip()
    #     if content:
    #         yield content


def main():
    start = time.time()

    with open(os.path.join(DATA_DIR, 'stop_words.txt'), 'r') as f:
        stop_words = [word.strip() for word in f.readlines()if word.strip()]

    # 多进程，偏函数
    # data = get_data()
    # with Pool() as pool:
    #     pool.map(partial(process_data, stop_words=stop_words, target_file=TARGET_FILE), data)

    # 使用yield
    for d in get_data():
        process_data(d, stop_words, TARGET_FILE)

    # pool = Pool()
    # for d in ans:
    #     pool.apply_async(process_data, [d, stop_words, TARGET_FILE])
    # pool.close()
    # pool.join()

    # with ProcessPoolExecutor() as executor:
    #     executor.map(partial(process_data, stop_words=stop_words, target_file=TARGET_FILE), ans)

    print('run time: ', time.time() - start)


if __name__ == '__main__':
    # lp = LineProfiler()
    # lp.add_function(process_data)
    # lp_wrapper = lp(main)
    # lp_wrapper()
    # lp.print_stats()
    main()
