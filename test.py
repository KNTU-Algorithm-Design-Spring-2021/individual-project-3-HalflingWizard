import random
import james_bond
import time


dict_file = open('dictionary.txt', 'r').read()
dictionary = dict_file.split('\n')

number_of_words = int(input('how many words do you want to have in the sentence? '))
sentence = ""
start_time = time.time()
for i in range(number_of_words):
    index = random.randint(0,len(dictionary)-1)
    while "_" in dictionary[index] or " " in dictionary[index] or "-" in dictionary[index]:
        index = random.randint(0,len(dictionary))
    sentence += (dictionary[index].upper())
print(sentence)
james_bond.decode(sentence.lower(),"")

print("--- %s seconds ---" % (time.time() - start_time))