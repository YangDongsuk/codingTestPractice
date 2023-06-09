def solution(s):
    answer = 1000
    for n in range(1, len(s)+1):
        lst = cut(s, n)
        num = count(lst)
        if num < answer:
            answer = num
    print(answer)

    return answer


def cut(s, n):
    lst = []
    while len(s) > n:
        lst.append(s[:n])
        s = s[n:]
    if len(s) != 0:
        lst.append(s)
    return lst


def count(lst):
    print(lst)
    new_str = ""
    pre = ""
    num = 1
    for i in lst:
        if i == pre:
            num += 1
        else:
            if num != 1:
                new_str += str(num)
                num = 1

            new_str += pre
            pre = i
    if num != 1:
        new_str += str(num)
        new_str += pre
    else:
        new_str += pre
    print(new_str)

    return len(new_str)


solution("xababcdcdababcdcd")
