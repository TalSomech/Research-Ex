import re, doctest

"""This function is used to check the mail addresses of a certain txt file whilst using regex"""


def check_mail(path):
    """
    >>> check_mail("mail.txt")
    ['abc-d@mail.com', 'abc.def@mail.com', 'abc@mail.com', 'abc_def@mail.com', 'abc.def@mail.cc', 'abc.def@mail-archive.com', 'abc.def@mail.org', 'abc.def@mail.com', 'tal.somecx@mail.xc']
    ['abc-@mail.com', 'abc..def@mail.com', '.abc@mail.com', 'abc#def@mail.com', 'abc.def@mail.c', 'abc.def@mail#archive.com', 'abc.def@mail', 'abc.def@mail..com', '%tal.some@mail.s']
    """
    valid = []
    invalid = []
    mail_pattern = "[^\s].*@.*\s"
    predom_pattern = "[\w]+([-._]?[\w]+)+@[\w]+([-._]?[\w]+)*[\.][\w][\w]+"
    with open(path) as file:
        file_str = file.read()
        for mail in re.findall(mail_pattern, file_str):
            mail_str = mail[:-1]
            if re.match(predom_pattern, mail_str):
                valid.append(mail_str)
            else:
                invalid.append(mail_str)
    print(valid)
    print(invalid)


"""This function is used to run any function with a set of inputs
and checks whether the input has been used already,if so return a specified message"""
fun_input = {}


def last_call(func: callable):
    """
    >>> print(f(2))
    4

    >>> print(f(2))
    I already told you that the answer is 4

    >>> print(check_prof("tal ","somech ","elazar"))
    tal somech elazar

    >>> print(check_prof("tal ","somech ",a="elazar"))
    I already told you that the answer is tal somech elazar
    >>> print(fp(2, 4))
    6
    >>> print(fp(2, 4))
    I already told you that the answer is 6
    """
    global fun_input

    def wrap(*args, **kwargs):
        inp_str = str(list([*args, *kwargs.values()]))
        if func in fun_input.keys():
            if inp_str in fun_input[func].keys():
                ans = fun_input[func][inp_str]
                return f"I already told you that the answer is {ans}"
        ans = func(*args, **kwargs)
        fun_input[func] = {inp_str: ans}
        return ans

    return wrap


@last_call
def f(x: int):
    return x ** 2


@last_call
def fp(x: int, y: int):
    return x + y


@last_call
def check_prof(fn, ln, a):
    return fn + ln + a


if __name__ == '__main__':
    doctest.testmod()
    # valid, invalid = check_mail("mail.txt")
    # print("valid:")
    # print(valid)
    # print("invalid:")
    # print(invalid)
    # print(f(2))
    # print(f(2))
    # print(f(100))
    # print(f(100))
    # print(check_prof("tal ","somech ","elazar"))
    # print(check_prof("tal ","somech ",a="elazar"))
    #
    # print(fp(2, 4))
    # print(fp(2, 4))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
