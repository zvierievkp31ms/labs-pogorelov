from indexfile import remove_punctuation

def query_index(query_word, index, filenames):
    query_word = remove_punctuation(query_word)
    if query_word not in index:
        return f'The word "{query_word}" is not found in any of the indexed files.', 404

    result = []
    for k, v in enumerate(index[query_word]):
        if v != 0:
            result.append({"value": v, "filename": filenames[k]})
    
    result = sorted(result, key=lambda d: d['value'], reverse=True)
    res_str = ''
    for entry in result:
        filename = entry['filename']
        frequency = entry['value']
        res_str += f'{frequency} {filename}\n'
    return res_str, 200