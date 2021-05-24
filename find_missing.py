def find_missing(full, par):
    missing_items = set(full) - set(par)
    assert(len(missing_items) == 1)
    return list(missing_items)[0]
 

print("The missing number from the partial list, using linear time:",find_missing([4,12,9,5,6], [4,9,12,6]))


def find_missing_xor(full, par):
    xor_sum = 0
    for num in full:
        xor_sum ^= num
    for num in par:
        xor_sum ^= num

    return xor_sum

print("The misssing xor_sum is, which is constant time:",find_missing_xor([4,12,9,5,6], [4,9,12,6]))

#https://www.youtube.com/watch?v=cdCeU8DJvPM&list=PL_557Q1uZ7gLfEajI2TZDU80Y3kkpAxti&index=67

#https://www.youtube.com/watch?v=r0CAz6MdgEg&list=PL5tcWHG-UPH1D-JVSiZI_8I8LPUJtoHdg&index=5
