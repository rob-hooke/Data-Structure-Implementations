def kmp(s1,s2):
    m = len(s1)
    n = len(s2)

    i = 1
    j = 0
    prefix_array = [0]
    

    while i < n:

        if s2[i] == s2[j]:
            prefix_array.append(j + 1)
            j += 1
            i+= 1
        elif s2[i] != s2[j]:
            if j == 0:
                prefix_array.append(j)
                i += 1
            else:
                j = prefix_array[j - 1]



    i,j = 0,0

    while i < m and j < n:
        if s1[i] == s2[j]:
            i += 1
            j += 1

        else:
            if s1[i] != s2[j] and j == 0:
                i += 1
            else:
                j = prefix_array[j - 1]
            

    if j >= n:
        print(True)
    else:
        print(False)
    #print(prefix_array)



kmp('aaaa','aa')
                
