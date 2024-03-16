import os
#add your files to programme dir

def text_file_selector():
    names = os.listdir()
    text_files = []
    for i in names:
        if i.endswith(".txt"):
            text_files.append(i)

    for j in text_files:
        print(f'Press {text_files.index(j) + 1} select [{j}] text file')
    text_file_number = int(input("Please enter your selecting text file number:"))
    selected_text_file_name = text_files[text_file_number - 1]
    return selected_text_file_name

def number_of_words(data):
    word_count = 0
    lines = data.split()
    for word in lines:
        if not word.isnumeric():
            word_count += 1
    return word_count
    
    
def unique_words(data):
    data_split = data.split(' ')
    unique = set(data_split)
    return unique
def most_frequent_words(data):
    from collections import Counter
    spit_data = data.split()
    Counter = Counter(spit_data)
    frequent_word = Counter.most_common(5)
    return frequent_word
def avg_word_length():
    pass
def number_of_sentences():
    

    pass
def longest_sentences():
    pass
def shortest_sentences():
    pass
def percentege_of_uppercase_letter():
    pass
def list_5_most_frequent_bigrams():
    pass
def word_cloud_generation():
    pass



 
def main():
    file_name = text_file_selector()
    with open(file_name, 'r') as in_file:
        data = in_file.read()
        word_counts_ = number_of_words(data=data)
        unique_words_ = unique_words(data=data)
        most_frequent_word_ = most_frequent_words(data=data)
    print(most_frequent_word_)


if __name__ == "__main__":
    main()




