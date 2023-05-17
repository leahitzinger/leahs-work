import pandas as pd
import math
from multiprocessing import Pool
import functools
hotel=pd.read_csv('hotel_bookings.csv', na_values=['none','undefined','','-'])
def mapper(hotel):
    dict_time=hotel.lead_time.value_counts().to_dict()
    list_10=[1,2,3,4,5,6,7,8,9,10]
    dict_2={}
    for list_1 in list_10:
        if list_1 in dict_time.keys():
            dict_2[list_1] = dict_time[list_1]
    return dict_2
def reducher(chunk1,chunk2):
    for key,val in chunk2.items():
        if key not in chunk1:
            chunk1[key]=val
        else:
            chunk1[key]+=val
    return chunk1
    
def map_reduce(data, num_processes, mapper, reducer):
    chunk_size = math.ceil(len(data) / num_processes)
    chunks= [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    with Pool(num_processes) as pool:
        chunk_results = pool.map(mapper, chunks)
    pool.close()
    pool.join()
    return functools.reduce(reducer, chunk_results)

if __name__ == '__main__':
    result=map_reduce(hotel,8,mapper,reducher)
    print(result)
