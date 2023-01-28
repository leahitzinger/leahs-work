import pandas as pd
import math
from concurrent.futures import ProcessPoolExecutor
class Chunks:
    def __init__(self,path,col):
        self.df=pd.read_csv(path)
        self.col=self.df[col]
    
    def make_chunks(self, num_chunks):
        num_rows = self.df.shape[0]
        chunk_size = math.ceil(num_rows / num_chunks)
        chunks = []
        for i in range(0, num_rows, chunk_size):
            chunk = self.df[i:i + chunk_size]
            chunks.append(chunk)
        return chunks

    def count(self):
        col = self.col.unique()
        count_dict = {}
        for each in col:
            count = self.col.str.count(each).sum()
            count_dict[each]=count
        return count_dict

    def processes(self,num_chunks):
        with ProcessPoolExecutor() as exe:
            processes = [exe.submit(self.count) for chunk in self.make_chunks(num_chunks)]
        results = [process.result() for process in processes]
        merged_results = {}
        for result in results:
            for each in set(result):
                merged_results[each] = merged_results.get(each, 0) + result.get(each, 0)
        print(merged_results)

if __name__ == '__main__':
    googleplaystore=Chunks('parallel processing\Lesson3\googleplaystore.csv','Size')
    googleplaystore.processes(8)