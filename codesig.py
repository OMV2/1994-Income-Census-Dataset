n = [12,235,-12]
n.sort()
print(n)

if n[i] <= n[i-1]:
    n.pop(i-1)
    
    for j in range(1,len(n)):
        if n[j] <= n[j-1]:
            return False
    return True
