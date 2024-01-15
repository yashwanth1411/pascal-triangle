def getRow(k):
    if k == 0:
        return [1]
    
    row = [1]  
    
    for i in range(1, k + 1):
        
        row.append(row[i - 1] * (k - i + 1) // i)
    
    return row


a = int(input())
print(getRow(a))