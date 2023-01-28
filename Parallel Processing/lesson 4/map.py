list1=['leah','malky','esti','chavi','gitty','suri']
def length_word(list):
    length=[]
    for word in list:
        length.append(len(word))
    print(length) 

length_word(list1)

def length_word_map(word):
    return(len(word))
    

list_map=map(length_word_map,list1)
print(list(list_map))