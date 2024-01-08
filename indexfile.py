import json
import string
from linked_list import LinkedList

def remove_punctuation(word):
    word = word.strip(string.punctuation)
    return word.lower()

def index_file(files):
    wordList = LinkedList(len(files))

    with open('index', 'w', encoding='utf-8') as index_file:
        json.dump(wordList.toObj(), index_file, indent=2)

    with open('filenames', 'w', encoding='utf-8') as filenames_file:
        json.dump(list(files.keys()), filenames_file, indent=2)