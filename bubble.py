data = [9,5,8,3,1,7,6,10,4,2]
print("data sebelum diurutkan:",data)
for i in range (10-1):
    for j in range (10-1):
        if data[j]>data[j+1]:
            temp = data[j]
            data[j] = data[j+1]
            data[j+1] = temp
print("data setelah diurutkan:",data)
