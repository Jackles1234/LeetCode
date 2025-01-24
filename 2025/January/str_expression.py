
def get_dicts():
    tup_nums = [("one", "1"), ("two", "2"), ("three", "3"), ("four", "4"), ("five", "5"), ("six", "6"), ("seven", "7"), ("eight", "8"), ("nine", "9"), ("zero", "0"), ("negative","-")]
    str_exp = {"plus": "+", "minus": "-"}
    str_nums = dict(tup_nums)
    num_to_word = {num: word for word, num in tup_nums}
    return str_exp, str_nums, num_to_word


def StringExpression(strParam):
    str_exp, str_nums, num_to_word = get_dicts()
    curr_num = ""
    l = 0
    for r in range(len(strParam)+1):
        if strParam[l:r] in str_nums:
            curr_num += str_nums[strParam[l:r]]
            l = r
        elif strParam[l:r] in str_exp:
            curr_num += str_exp[strParam[l:r]]
            l = r

    
    total = str(eval(curr_num))
    res = ""
    for i in total:
        res += num_to_word[i]
    return res


print(StringExpression("oneminusoneone"))