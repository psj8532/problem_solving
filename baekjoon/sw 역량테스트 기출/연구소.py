:
            for k in range(j+1,m):
                if not matrix[y][i] and not matrix[y][j] and not matrix[y][k]:
                    if not matrix[y][i]:
                        matrix[y][i]=3
                    if not matrix[y][j]:
                        matrix[y][j]=3
                    if not matrix[y][k]:
                        matrix[y][k]=3
            else:
                y+=1