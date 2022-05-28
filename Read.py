def read_file_content(filename):
    file= open('story.txt', 'r')
    filer = file.read()
    return filer
    
def count_words():
    text = read_file_content("story.txt")
    count_word = dict()
    words = text.split()

    for word in words:
        if word in count_word:
            count_word[word] = count_word[word] + 1
        else:
            count_word[word] = 1
    return(count_word)
print(count_words())



