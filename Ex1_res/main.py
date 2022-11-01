from typing import Collection, Any, Iterable
import copy
import doctest

"""This function is used to check if 
    every arg in the called function is
    matched with its annotation,if so,execute the function
    it works by checking the length of both the args and the kwargs
    so both formats will work"""


def safe_call(func: callable, *args, **kwargs):
    """
    >>> safe_call(f, x=5, y=5.6, z=2)
    12.6
    >>> safe_call(f,x="my",y="name",z="is",k="tal")
    Traceback (most recent call last):
    ...
    Exception: Not all arguments match their annotations.
    >>> safe_call(f, 5, 2.3, y=2.3, z=1)
    Traceback (most recent call last):
    ...
    TypeError: f() missing 1 required positional argument: 'x'
    """
    anon = list(func.__annotations__.values())
    local_arg = list(locals()['args'])
    local_kw = list(locals()['kwargs'].values())  # get the local vars of this function
    arg_len = len(local_arg)
    for i in range(len(anon)):
        if i < arg_len and anon[i] is not type(local_arg[i]):
            raise Exception("Not all arguments match their annotations.")

        elif i >= arg_len and anon[i] is not type(local_kw[i - arg_len]):
            raise Exception("Not all arguments match their annotations.")
    print(func(**kwargs))


def f(x: int, y: float, z):
    return x + y + z


"""This function is used to generalize bfs algorithm 
    by only getting the start node,end node and neighbors function
    
"""


def bfs(start: Any, end: Any, neis_func: callable):
    """
    >>> bfs((0,0),(2,2),neis_func=neighbor_function)
    (0, 0) (1, 0) (-1, 0) (0, 1) (0, -1) (2, 0) (1, 1) (1, -1) (-2, 0) (-1, 1) (-1, -1) (0, 2) (0, -2) (3, 0) (2, 1) (2, 2)
    >>> bfs('c','n',neis_func=neighbor_func_2)
    c d b e a f ` g _ h ^ i ] j \ k [ l Z m n
    """
    visited = [start]
    queue = [start]
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for neighbor in neis_func(node):
            if neighbor == end:
                print(end)
                return
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


"""
This function is used to deep copy a collection (list,dict,etc..)
and send it to a sorting function
"""


def print_sorted(data_str: Collection):
    data = copy.deepcopy(data_str)
    datas = sorts(data)
    print(datas)


"""This function is used to sort a collection using recursive sorting"""


def sorts(data: Iterable):
    """
    >>> print_sorted({"a": 5, "c": 6, "b": [1, 3, 2, 4]})
    {'a': 5, 'b': [1, 2, 3, 4], 'c': 6}
    >>> print_sorted([3, 4, 1, 2, [2, 1, 6, 3, {"a": 5, "c": 6, "b": [1, 3, 2, 4]}]])
    ['1', '2', '3', '4', '[1, 2, 3, 6, {a: 5, c: 6, b: [1, 2, 3, 4]}]']
    """
    if type(data) is dict:
        data = dict(sorted(data.items()))
        iter = data.values()
    else:
        iter = data.__iter__()
    for item in iter:
        if type(item) is (list or tuple or set):
            ans = sorts(item)
            item.clear()
            item.extend(sort_expt(ans))
        elif type(item) is dict:
            sorts(item)
    if type(data) is not dict:
        return sort_expt(data)
    return data


"""This function is used to try and sort a list, but if the list contains another
    list an error will occur , this function is used to turn everything into string and sort 
    alphabetically"""


def sort_expt(lst: Iterable):
    try:
        return sorted(lst)
    except Exception as e:
        lst = (str(val).replace('\'', "") for val in lst)
        return sorted(lst)


"""testing functions:"""


def neighbor_function(node: Any) -> list:
    (x, y) = node
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


"""testing functions:"""


def neighbor_func_2(node) -> list:
    return [chr(ord(node) + 1), chr(ord(node) - 1)]


if __name__ == '__main__':
    print(doctest.testmod())
