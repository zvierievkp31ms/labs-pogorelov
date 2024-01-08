import os
import json
import string
from linked_list import LinkedList

def remove_punctuation(word):
    word = word.strip(string.punctuation)
    return word.lower()

def work_with_words(k, line, linkedL):
    words = line.split()
    for word in words:
        cleaned_word = remove_punctuation(word)
        if cleaned_word:
            word_node = linkedL.getNode(cleaned_word)
            if word_node is None:
                el = linkedL.push(cleaned_word)
                el.incrementFreq(k)
            else:
                word_node.incrementFreq(k)

def index_file(files, index, filenames):
    wordList = LinkedList(len(files))
    for k, v in enumerate(files):
        file = open(v, 'r')
        count = 0
        while True:
            count += 1
            line = file.readline()
            work_with_words(k, line, wordList)
            if not line:
                break
        file.close()

    res_obj = {}
    with open('result.json', 'r', encoding='utf-8') as result_file:
        res_obj = json.load(result_file)

    if key_exist(filenames.split('/')[1], res_obj): #filename exist
        key = [i for i in res_obj if res_obj[i]==filenames.split('/')[1]][0]
        if(key != index.split('/')[1]):
            raise Exception('filename exist with other index')
    else:
        if index.split('/')[1] in res_obj: #index exist with other filename
            os.remove(filenames.split('/')[0] + '/' + res_obj.get(index.split('/')[1]))

    res_obj[index.split('/')[1]] = filenames.split('/')[1]

    with open('result.json', 'w', encoding='utf-8') as result_file:
        json.dump(res_obj, result_file, indent=2)

    with open(index, 'w', encoding='utf-8') as index_file:
        json.dump(wordList.toObj(), index_file, indent=2)

    with open(filenames, 'w', encoding='utf-8') as filenames_file:
        json.dump([file.split('/')[1]+'/' + file.split('/')[2] for file in files], filenames_file, indent=2)
    return res_obj

def key_exist(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return True
    return False