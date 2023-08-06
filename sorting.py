
#import bubble_sort
ARRAY_LENGTH = 1000
from random import randint
from timeit import repeat
import sys
sys.path.append('./')
from bubble_sort import bubble_sort
from quicksort import quicksort

import psutil

print ('cpu count = ', psutil.cpu_count())
p = psutil.Process()
p.cpu_affinity()
all_cpus = list(range(psutil.cpu_count()))
p.cpu_affinity([0]) 
print ('cpu affinity = ', p.cpu_affinity())



def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=10, number=10)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")

if __name__ == "__main__":

    # Generate an array of `ARRAY_LENGTH` items consisting
    # of random integer values between 0 and 999
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    file = open ("unsorted_array.txt", "w+")
    content = '\n'.join(map(str, array))
    file.write(content)
    file.close()

    # Call the function using the name of the sorting algorithm
    # and the array you just created
#   run_sorting_algorithm(algorithm="bubble_sort", array=array)
    run_sorting_algorithm(algorithm="quicksort", array=array)






