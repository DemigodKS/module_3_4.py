def single_root_words(root_word, *other_words):
    same_words = []

    for word in other_words:
        if root_word.lower() in word.lower():
            same_words.append(word)

    return same_words


result = single_root_words('able', 'disable', 'cheers', 'ABLE', 'disablement', )
print(result)
result1 = single_root_words('Back', 'BacKgRound', 'BackYard', 'cheers', 'Backup')
print(result1)
result2 = single_root_words('merge', 'Emergent', 'forth',  'unMerge', 'Submerge')
print(result2)
