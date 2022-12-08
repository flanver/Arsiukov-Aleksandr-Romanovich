def sum_arf_arr(*arrays, res = []):
    for arr in arrays:
        summ, arf = sum(arr), sum(arr) / len(arr)
        res.append((summ, arf))
    return res
 
print( sum_arf_arr([6,8,4], [6,7,3], [8,7,9]) )