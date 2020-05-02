def same_frequency(num_1,num_2):
    freq_1 = {x:str(num_1).count(x) for x in str(num_1)}
    freq_2 = {x:str(num_2).count(x) for x in str(num_2)}
    for key in freq_1.keys():
        if not key in freq_2 or freq_1[key] != freq_2[key]:
            return False
    return True

print(same_frequency(551122,221515))
print(same_frequency(321142,3212215))
print(same_frequency(1212,2211))