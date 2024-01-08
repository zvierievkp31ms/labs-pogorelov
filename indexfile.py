import json
import string
from linked_list import LinkedList

def remove_punctuation(word):
    word = word.strip(string.punctuation)
    return word.lower()

def index_file(files):
    wordList = LinkedList(len(files))
    for k, v in enumerate(files):
        words = files[v].split()
        for word in words:
            cleaned_word = remove_punctuation(word)
            if cleaned_word:
                word_node = wordList.getNode(cleaned_word)
                if word_node is None:
                    el = wordList.push(cleaned_word)
                    el.incrementFreq(k)
                else:
                    word_node.incrementFreq(k)

    res_obj = {}
    res_obj['index'] = wordList.toObj()
    res_obj['filenames'] = list(files.keys())

    with open('index', 'w', encoding='utf-8') as index_file:
        json.dump(res_obj['index'], index_file, indent=2)

    with open('filenames', 'w', encoding='utf-8') as filenames_file:
        json.dump(res_obj['filenames'], filenames_file, indent=2)
    
    return res_obj