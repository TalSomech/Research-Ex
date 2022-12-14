# This is a sample Python script.
import numpy as np
import cvxpy as cp
import time
import matplotlib.pyplot as plt


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def timer(func: callable):
    def wrap(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time() - t1
        return t2

    return wrap


@timer
def cvx_calc(A: np.ndarray, b: np.ndarray):
    x = cp.Variable(b.shape[0])
    b = b.reshape((b.shape[0]))
    calc = cp.Minimize(cp.sum_squares(A @ x - b))
    problem = cp.Problem(calc, [])
    problem.solve()
    return x.value


@timer
def np_calc(A: np.ndarray, b: np.ndarray):
    return np.linalg.solve(A, b)


def random_mat():
    size = np.random.randint(0, 1000)
    mat = np.random.randint(0, 100000, (size, size + 1))
    a = mat[:, :size]
    b = mat[:, size:]
    np_time = np_calc(a, b)
    cvx_time = cvx_calc(a, b)
    return (size, np_time, cvx_time)


def show_graph(np_lst, cvx_lst, sizes):
    plt.scatter(sizes, np_lst)
    plt.scatter(sizes, cvx_lst)
    plt.legend(["Numpy", "Cvxpy"])
    plt.show()


if __name__ == '__main__':

    np_lst, cvx_list, sizes = [], [], []
    for i in range(20):
        i_size, np_time, cvx_time = random_mat()
        np_lst.append(np_time)
        cvx_list.append(cvx_time)
        sizes.append(i_size)
    show_graph(np_lst, cvx_list, sizes)

