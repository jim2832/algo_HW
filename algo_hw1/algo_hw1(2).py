def is_valid_word(word, tiles):
    for s in word:
        if s in tiles:
            if(word.count(s) == tiles.count(s)):
                return True
        else:
            return False

word = 'AB'
tiles = 'ABCDE'
print(is_valid_word(word,tiles))

