import pandas as pd
import math
from multiprocessing import Pool
import functools
df = pd.read_csv('parallel processing\Lesson 4\chatgpt.csv')
df=df['like_count']

def map_reduce(data, num_processes, mapper, reducer):
    chunk_size = math.ceil(len(data) / num_processes)
    chunks= [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    with Pool(num_processes) as pool:
        chunk_results = pool.map(mapper, chunks)
    pool.close()
    pool.join()
    return functools.reduce(reducer, chunk_results)

if __name__ == '__main__':
    result=map_reduce(df,8,max,max)
    print(result)

