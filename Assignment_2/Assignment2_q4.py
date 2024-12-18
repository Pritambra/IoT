# Write a function find_longest_word() that takes a list of words and returns the length of the longestone.

def find_longest_word(word_list):  
    longest_word = ''  
    for word in word_list:    
          print(word, len(word))  


words = input('enter a few words')  
word_list = words.split()  
find_longest_word(word_list)  