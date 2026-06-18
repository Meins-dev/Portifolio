p1 = [7.0,8.3,10.0,6.5,9,3]
p2 = [8.5,6.9,5.0,7.5,9.8]
medias = []
for n1 , n2 in zip(p1,p2):
    medias.append((n1+n2) / 5)
    
for m in medias: 
    print(f"{m:.2f}")
