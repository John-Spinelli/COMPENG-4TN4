img = [[0, 0, 0, 0, 0, 0],
       [0, 3, 5, 8, 4, 0],
       [0, 9, 1, 2, 9, 0],
       [0, 4, 6, 7, 3, 0],
       [0, 3, 8, 5, 4, 0],
       [0, 0, 0, 0, 0, 0]]

res = [[0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0]]

m1 = [[1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]]

m2 = [[0, 1, 0],
      [1, 1, 1],
      [0, 1, 0]]

# For each element in image
for row in range(1,5):
    for col in range(1,5):
        values = []
        # Surrounding elements
        for i in range(-1,2):
            for j in range(-1,2):
                if (m2[i+1][j+1]) > 0:
                    values.append(img[row+i][col+j])

        values.sort()
        print(values)
        res[row][col] = values[len(values)//2]
print()
print(res[1][1:5])
print(res[2][1:5])
print(res[3][1:5])
print(res[4][1:5])


        
        
    
       
