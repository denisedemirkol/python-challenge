import os
import re

selected = input("Whic file do you want to work, please enter with the file extension: ")


file_path = os.path.join( "raw_data", selected)

try:
    with open(file_path,"rt") as f:
        data = f.read()
        words = data.split(" ") 
        words_app = re.split(' |-|\'',data)    

        average = round((sum(len(word) for word in words) / len(words)),1)
        sentences = data.split(".")
        sentences.remove("")


    print('Approximate Word Count: :', len(words_app))
    print(f'Approximate Sentence Count: {len(sentences)}')
    print(f"Average Letter Count : {average}")
    print(f"Average Sentence Length: {round(len(words)/len(sentences),1)}")


except IOError:
    print (f"Could not read file: {selected}. Please enter the file extension. ")
 
