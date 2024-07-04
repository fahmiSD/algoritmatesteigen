def find_longest_words(text):
    words = text.split() 
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length] 
    return longest_words

sentence = "Saya sangat senang mengerjakan algoritma"
longest_words = find_longest_words(sentence)
result = "".join([f"{word} : {len(word)} characters \n" for word in longest_words])
print(result)
