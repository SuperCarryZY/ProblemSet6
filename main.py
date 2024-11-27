import random, time
import tabulate

def ssort(L):
    for i in range(len(L)):
        m = L.index(min(L[i:]))
        L[i], L[m] = L[m], L[i]
    return L

def qsort(a, pivot_fn):
    if len(a) <= 1:  
        return a
    pivot_index = pivot_fn(a)  
    pivot = a[pivot_index]  
    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return qsort(left, pivot_fn) + middle + qsort(right, pivot_fn)

def time_search(sort_fn, mylist):

    start = time.time()
    sort_fn(mylist[:]) 
    return (time.time() - start) * 1000  

def compare_sort(sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]):

    qsort_fixed_pivot = lambda arr: qsort(arr, lambda a: 0)  
    qsort_random_pivot = lambda arr: qsort(arr, lambda a: random.randint(0, len(a) - 1))  
    tim_sort = sorted  
    selection_sort = ssort  

    result = []
    for size in sizes:
        mylist = list(range(size))
        random.shuffle(mylist)

        fixed_pivot_time = time_search(qsort_fixed_pivot, mylist[:])
        random_pivot_time = time_search(qsort_random_pivot, mylist[:])
        tim_sort_time = time_search(tim_sort, mylist[:])
        ssort_time = time_search(selection_sort, mylist[:])

        result.append((size, fixed_pivot_time, random_pivot_time, tim_sort_time, ssort_time))

    return result

def print_results(results):

    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot', 'timsort', 'ssort'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():

    print_results(compare_sort())

random.seed()
test_print()
