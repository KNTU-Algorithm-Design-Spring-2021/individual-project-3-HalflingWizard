# global scope
dict_file = open('dictionary.txt', 'r').read()
dictionary = dict_file.split('\n')

def decode(coded_sent, uncoded_sf):
    """decode the sentence

    Args:
        coded_sent (str): james bonds' code
        uncoded_sf (str): what we have uncoded so far
        dictionary (list): a list of possible words
    """
    for i in range(1, len(coded_sent) + 1):
    
        prefix = coded_sent[:i] # we split several characters from beggining
        if prefix in dictionary: # if it's in the dictionary, it's a word
            if i == len(coded_sent): # if i == len(coded_sent) it means we have reached the end of sentence
                print(uncoded_sf + " " + prefix)
            decode(coded_sent[i:], uncoded_sf + " " + prefix)    