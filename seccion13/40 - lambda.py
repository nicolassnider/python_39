#funciones anónimas

l=list(range(1,1000)) 
l2 = list(filter(lambda n : n % 7 ==0, l))
print(l2)
