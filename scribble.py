from random_word import RandomWords
r = RandomWords()

if __name__ == '__main__':
    print(r.get_random_words(hasDictionaryDef="true", includePartOfSpeech="noun", excludePartOfSpeech="verb",
                             maxLength=8, minCorpusCount=10000))
