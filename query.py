from indexfile import remove_punctuation

def query_index(query_word, index, filenames):
    query_word = remove_punctuation(query_word)
    
    if query_word not in index:
        return f'The word "{query_word}" is not found in any of the indexed files.', 404

    result = 'frequency filename\n'
    return result, 200