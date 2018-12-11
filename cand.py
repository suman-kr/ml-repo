from pandas import read_csv
df = read_csv('data.csv' , header = None)
data = df.values.tolist()
g = set()
sp = ['0']*6
def most_specific(ex):
	for i in range(len(ex)-1):
		if sp[i] == '0':
			sp[i] = ex[i]
		else:
			if ex[i] != sp[i]:
				sp[i] = '?'
	for i in list(g):
		if i[1] not in sp:
			g.remove(i)

def most_general(ex):
	for i in range(len(sp)):
		if sp[i] != '?' and ex[i] != sp[i]:
			g.add((i,sp[i]))

for i , val in enumerate(data):
	if val[-1] == 'yes':
		most_specific(val)
	else:
		most_general(val)

	print sp
	print g

	if len(gen_hyp) == 0:
		print ['?'] * 6
    else:
        for i in gen_hyp:
            gen = ['?'] * 6
            gen[i[0]] = i[1]
            print gen
    print 