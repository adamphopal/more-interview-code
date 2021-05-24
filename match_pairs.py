def find_pairs(values, target):
    ht = dict()
    for i in range(len(values)):
        if values[i] in ht:
            print("Found pairs:",ht[values[i]], "and", values[i], "from our values list, that equals our target:", str(target))
            return True
        else:
            ht[target - values[i]] = values[i]
    print("No Valid Pairs")
    return False

#print(find_pairs([14,13,6,7,8,10,1,2], 3)) == "1 and 2"
#print(find_pairs([14,13,6,7,8,10,1], 3)) == "no valid pairs"
#print(find_pairs([2,2], 4)) == "2 and 2"
print("Valid Pairs for values list 1:",find_pairs([14,13,6,7,8,10,1,2], 3))
print("Valid Pairs for values list 2:",find_pairs([14,13,6,7,8,10,1], 3))
print("Valid Pairs for values list 3:",find_pairs([2,2], 4))


#https://www.youtube.com/watch?v=wBXZD436JAg&list=PL_557Q1uZ7gIzDxN_rH_Vi6Egh0ID7un2&index=54
