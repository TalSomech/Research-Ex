import doctest

"""This class is inherits from the list class to include list[1,2...] and
 list[1,2...]=..."""


class List(list):
    def __init__(self, items):

        super(List, self).__init__(items)
    """This function is used to override the list[] operator"""
    def __getitem__(self, item):
        """
        >>> List([[1, 2], [3, [5, 6], 4]])[0,1]
        2
        >>> List([[1, 2], [3, [5, 6], 4]])[1,1,0]
        5
        """
        if isinstance(item, int):
            return list.__getitem__(self, item)
        else:
            if len(item) == 2:
                rest = item[1]
            else:
                rest = item[1:]
            try:
                return List.__getitem__(self[item[0]], rest)
            except TypeError:
                raise IndexError("list index out of range")
    """This function is used to override the list[]= operator"""
    def __setitem__(self, key, value):
        """
        >>> lst = List([[1, 2], [3, [5, 6], 4]])
        >>> print(lst[1,0])
        3
        >>> lst[1,0]=6
        >>> print(lst[1,0])
        6
        """
        if isinstance(key, int):
            return list.__setitem__(self, key, value)
        else:
            if len(key) == 2:
                rest = key[1]
            else:
                rest = key[1:]
            List.__setitem__(self[key[0]], rest, value)
            return value


if __name__ == '__main__':
    doctest.testmod()

