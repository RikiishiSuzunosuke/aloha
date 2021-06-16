list = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
#flatten = [list[i][j] for i in range(len(list)) for j in range(len(list[1]))]
flatten = [i for data in list for i in data]
# listの要素をdataに代入する
# dataの要素をiに代入する
# iをflattenに格納する
print(flatten)