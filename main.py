from difflib import SequenceMatcher

def binary_search(word, dict):
    first = 0
    last = len(dict) - 1
    while first<=last:
        midPoint = (first+last) // 2
        if dict[midPoint] == word:
            return True
        elif dict[midPoint] > word:
            last = midPoint-1
        else:
            first = midPoint+1
    return False

def best_suggestions(word, dict):
    suggested_words = []
    for w in dict:
        ratio = SequenceMatcher(None, word, w).ratio()
        if len(suggested_words) < 3:
            suggested_words.append((ratio, w))
        else:
            least_ratio = 1
            index = 0
            for ind in range(3):
                if least_ratio > suggested_words[ind][0]:
                    index = ind
                    least_ratio = suggested_words[ind][0]
            if ratio > least_ratio:
                suggested_words[index] = (ratio, w)
    return suggested_words

file = open('dictionary.txt', 'r')
dict = file.read()
newDict = dict.split()
text_input = input('Enter any sentence: ')
listOfWords = text_input.split()

for word in listOfWords:
    if not binary_search(word, newDict):
        print('this word is wrong: ', word)
        best_sg = best_suggestions(word, newDict)
        print('Suggestions: ')
        for i in best_sg:
            print(i[1], end='\n')

file.close()