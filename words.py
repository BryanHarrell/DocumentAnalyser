from collections import Counter
import re
verbs = open('31kverbs.txt', 'r+')
adjectives = open('28Kadjectives.txt', 'r+')
nouns = open('91Knouns.txt', 'r+')
text_file = open("Output.txt", "w")

def string_found(string1, string2):
   if re.search(r"\b" + re.escape(string1) + r"\b", string2):
      return True
   return False

def count_words(inputFile,wordCount,whatTypeOfWord):
    
    word_count = Counter()
    listOfWords = []
    
    with open(inputFile,"r+") as file:
        word_count.update((word for word in file.read().split()))
    
    wordCountTotal = sum(word_count.values())
    
    if whatTypeOfWord == 'nouns':
        dictionaryListOfWords= nouns.read()
    elif whatTypeOfWord == 'verbs':
        dictionaryListOfWords = verbs.read()
    elif whatTypeOfWord == 'adjectives':
        dictionaryListOfWords = adjectives.read()
    
    for word, count in word_count.most_common():
        wordCountPercentage = ((float(count))/float(wordCountTotal))*100
        if string_found(word,dictionaryListOfWords):
                listOfWords.append(word)
        if (wordCount == 'Yes'):
            print word, count, wordCountPercentage
    for i in sorted(listOfWords):
        text_file.write(i)
        text_file.write("\n")
    
    nouns.closed
    verbs.closed
    adjectives.closed
    text_file.close()
    
    
    #print('Hello', person)

def main():
    inputFile = raw_input('Enter your file: ')
    wordCount = raw_input('Do you want to see the list of words in your text displayed by number of instances? ')
    whatTypeOfWord = raw_input('Do you want a list of verbs, nouns or adjectives? ')
    count_words(inputFile,wordCount,whatTypeOfWord)

if  __name__ =='__main__':
    main()