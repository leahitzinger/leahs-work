import multiprocessing

def product(number1,number2,shared_value):
    a=number1*number2
    with shared_value.get_lock():
        shared_value.value += a
shared_value = multiprocessing.Value('i')

process1 = multiprocessing.Process(target=product, args=[10,6, shared_value])
process2 = multiprocessing.Process(target=product, args=[2,5,shared_value])


if __name__ == '__main__':
    process1.start()
    process2.start()

    process1.join()
    process2.join()
    print(shared_value.value) 