def readFile(filename):
    infile = open(filename, 'w')
    content = infile.read()
    infile.close()
    wordList = content.split()
    print(wordList)
    return len(wordList), len(content)


n_words, n_chars = readFile('Exemplo.txt')
print('A quantidade de palavras contadas foram', n_words)
print('A quantidade de letras contadas foram', n_chars)
