arr1 = [[1,1,5],[2,4,6],[3,7,8]]
arr2 = [[7,9,0],[8,8,9],[7,6,9]]


def Q2(arr1, arr2):
    mat = []
    mat2 = []
    val1 = 0 
    val2 = 0
    for i in arr1:
        for j in i:
            mat2 += [arr1[val1][val2]+ arr2[val1][val2] + 5]
            val2+=1
        mat += [mat2]
        mat2 = []
        val2 = 0
        val1+=1
    print(mat)
    return mat

Q2([[1,1,5],[2,4,6],[3,7,8]],[[7,9,0],[8,8,9],[7,6,9]])
