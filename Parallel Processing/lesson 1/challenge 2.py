import multiprocessing

def tasks(tasks_list):
    for _ in range(len(tasks_list)):
        tasks_list.pop()
    
if __name__ == '__main__':
    tasks_list = ['Homework', 'clean floor', 'wash dishes', 'feed the kids', 'story time', 'bathes','iron shirts','put up a load','serve supper','put kids to sleep']
    process1= multiprocessing.Process(target=tasks, args=[tasks_list[7:]])
    process2 = multiprocessing.Process(target=tasks, args=[tasks_list[3:7]])
    process3=multiprocessing.Process(target=tasks, args=[tasks_list[:3]])

    process1.start()
    process2.start()
    process3.start()

    process1.join()
    process2.join()
    process3.join()
