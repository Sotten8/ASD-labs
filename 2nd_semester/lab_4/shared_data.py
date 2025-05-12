n1, n2, n3, n4 = 4, 3, 2, 2
n = 10 + n3
k1 = 1.0 - n3 * 0.01 - n4 * 0.01 - 0.3
k2 = 1.0 - n3 * 0.005 - n4 * 0.005 - 0.27

labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C"]

numeric_labels = [str(i + 1) for i in range(n)]

directed_matrix = []
undirected_matrix = []
k = k1
