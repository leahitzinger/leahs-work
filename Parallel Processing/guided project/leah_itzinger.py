import pandas as pd
import math
from multiprocessing import Pool
import functools
import csv
with open ("Parallel Processing/guided project/twitterfriendsv2.csv", encoding ='UTF-8') as f:
    reader = csv.reader(f)
    rows = list(reader)
header = rows[0]
rows = rows[1:]
def make_chunks(df, num_chunks):
    num_rows= len(df)
    chunk_size= math.ceil(num_rows/num_chunks)
    chunks=[]
    for i in range(0, num_rows, chunk_size):
        chunk= df[i: i + chunk_size]
        chunks.append(chunk)
    return chunks
def friends_mapper(rows):
    friends_tuple={}
    for row in rows:
        row[9]= row[9].replace("'", '').replace('[', '').replace(']', '').strip().split(',')
        for value in row[9]:
            new_values=row[9]
            new_values.remove(value)
            friends_tuple[tuple([row[0],value])]=[new_values]
    return friends_tuple
def friends_reducer(chunk1,chunk2):
    for key,val in chunk2.items():
        if key not in chunk1 and tuple([key[1],key[0]]) not in chunk1:
            chunk1[key]=val
        else:
            chunk1[tuple([key[1],key[0]])]+=val
    for key, val in chunk1.items():
        try:
            chunk1[key] = {'common friends': set(val[0]).intersection(set(val[1]))}
        except:
            pass
    return chunk1
def map_reduce(data, num_processes, mapper,reducer):
    chunk_size = math.ceil(len(data) / num_processes)
    chunks= [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    with Pool(num_processes) as pool:
        chunk_results = pool.map(mapper, chunks)
    pool.close()
    pool.join()
    new_dict={}
    return functools.reduce(reducer, chunk_results, new_dict)
if __name__ == '__main__':
    result=map_reduce(rows,8,friends_mapper,friends_reducer)
    
# just to show that it worked
    # i=0
    # for key, val in result.items():
    #     if type(val) == dict:
    #         i+=1
    # print(i)