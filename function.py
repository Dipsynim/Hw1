def get_summ(one, two, delimiter='&'):
    stroka = str(one) + delimiter + str(two)
    return stroka
res = get_summ("Learn","python")
print(res.upper())