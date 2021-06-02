# for https://www.codewars.com/kata/52cf02cd825aef67070008fa/python

def decode(s):
    al = "!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,? "
    dl = len(al)
    d = ''
    for i,c in enumerate(s,1):
        cl = [al[2**i*v%dl]for v in range(len(al))]
        d += al[cl.index(c)]if c in cl else c
    return d


if __name__ == '__main__':
    al = "!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,? "
    dl = len(al)

    test = ["bhx,zWyLZ3pOGIhzeXTYtjAaDW",
            "bdhpF,82QsLir",
            "dhpF,82QsLirJ",
             "flxVC5WE94UA1",
             "1OoD70MkvRuPq",
             "MkvRuPqHabdhp",
             ".6YIcflxVC5WE",
             "6YIcflxVC5WE9"]

    for t in test:
        print(decode(t))
