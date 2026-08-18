### Multiprocessing - it allows you to create processes that runs in parallel

###CPU bound task

import multiprocessing

import time

def square_number():
    for i in range(5):
        time.sleep(1)
        print(f"Square {i*i}")

def cube_numbers():
    for i in range(5):
        print(f"Cube {i*i*i}")


if __name__ == '__main__':

    p1=multiprocessing.Process(target=square_number)
    p2=multiprocessing.Process(target=cube_numbers)

    p1.start()
    p2.start()

    p1.join()
    p1.join()

