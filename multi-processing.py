# from multiprocessing import Process
import concurrent.futures
import time

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

if __name__ == "__main__":
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)

        for result in results:
            print(result)

    # p1 = Process(target=do_something, args=(1.5,))
    # p2 = Process(target=do_something, args=(1.5,))

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')