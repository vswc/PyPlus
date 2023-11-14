import time

"""
watch_process(func) takes in a function as an argument.
wrapper() is defined as an inner function where the function is executed.

This decorator is used to watch how long a process takes before finishing.
We can reference the decorator in our with @watch_process.
Providing a function is below it, it will output the time it took to execute the function.

Executed main in X.XXs.
"""

def watch_process(process):
    def wrapper():
        start = time.time()
        process()
        end = time.time()
        print(f'Executed {process.__name__} in {end - start}s.')
                                # __name__ 
                                # returns the name of the function.
    return wrapper

@watch_process
def main():
    for i in range(5):
        print("This simulates a long process...")
        time.sleep(0.1)

main()

"""
Anything I missed? Let me know.
@vsw on discord.
"""