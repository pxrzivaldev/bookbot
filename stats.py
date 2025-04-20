def word_count(bookcontent):
    wordlist = bookcontent.split()
    wordcount = len(wordlist)
    return wordcount

def characters_count(bookcontent):
    uniqueChar = {}
    for char in bookcontent.lower():
        if(char in uniqueChar):
            uniqueChar[char] += 1
        else:
            uniqueChar[char] = 1
    return uniqueChar