
import pandas as pd
import math
from concurrent.futures import ProcessPoolExecutor
df = pd.read_csv('parallel processing\Lesson3\googleplaystore.csv')
categories = df['Category'].unique()
def count_categories():
    count_categories_dict = {}
    for category in categories:
        count_categories = df['Category'].str.count(category).sum()
        count_categories_dict[category]=count_categories
    return count_categories_dict
def make_chunks(categories, num_chunks):
    len_rows = len(categories)
    chunk_size = math.ceil(len_rows / num_chunks)
    chunks = []
    for i in range(0, len_rows, chunk_size):
        chunk = df[i:i + chunk_size]
        chunks.append(chunk)
    return chunks
if __name__ == '__main__':
    with ProcessPoolExecutor() as exe:
        processes = [exe.submit(count_categories) for chunk in make_chunks(categories, 6)]
    results = [process.result() for process in processes]
    merged_results = {}
    for result in results:
        for category in set(result):
            merged_results[category] = merged_results.get(category, 0) + result.get(category, 0)
    print(merged_results)