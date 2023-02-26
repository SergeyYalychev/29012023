n = int( input( 'n = ' ) )
lis = [ int(x) for x in input( '-> ' ).split() ]
n = len(lis)
lis = lis + lis[:2]
sum = 0
for i in range(n):
    sum = max( sum, lis[i] + lis[i+1] + lis[i+2] )
print(sum)