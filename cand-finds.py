def more_general(ex, gen_hyp, spf_hyp):
    for i in range(len(ex) - 1):
        if spf_hyp[i] == '0':
            spf_hyp[i] = ex[i]
        else:
            if ex[i] != spf_hyp[i]:
                spf_hyp[i] = '?'
    
    for i in list(gen_hyp):
        if i[1] not in spf_hyp:
            gen_hyp.remove(i)
        

def more_specific(ex, gen_hyp, spf_hyp):
    for i in range(len(spf_hyp)):
        if spf_hyp[i] != '?' and ex[i] != spf_hyp[i]:
            gen_hyp.add((i, spf_hyp[i]))
            

data = [['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'], 
        ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'], 
        ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'], 
        ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']]

spf_hyp = ['0'] * 6
gen_hyp = set()

for i, val in enumerate(data):
    if val[-1] == 'Yes':
        more_general(val, gen_hyp, spf_hyp)
    else:
        more_specific(val, gen_hyp, spf_hyp)
    
    print("S[{0}]:".format(i), spf_hyp)
    print("G[{0}]: ".format(i), end = '')

    if len(gen_hyp) == 0:
        print(['?'] * 6)
    else:
        for i in gen_hyp:
            gen = ['?'] * 6
            gen[i[0]] = i[1]
            print(gen)

    print()
