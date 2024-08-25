# import threading
import concurrent.futures
import time

start =time.perf_counter()

def do_something(x):
    time.sleep(x)
    # print(f'Sleeping for {x} seconds')
    return f'Sleeping for {x} seconds'

with concurrent.futures.ThreadPoolExecutor() as executor:
    sleep = [1,2,3,4,5]
    results = executor.map(do_something, sleep)
    
# print(type(results))
# print(results)
for result in results:
    print(result)


# t1= threading.Thread(target=do_something, args=(1,))
# t2= threading.Thread(target=do_something, args=(1,))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

finish = time.perf_counter()

print(f"Finished in {round(finish-start,2)} seconds")