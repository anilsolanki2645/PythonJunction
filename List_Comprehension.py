#Simple Word example

h_letters = []

for letter in 'human':
    h_letters.append(letter)

print(h_letters, "\n\n")

#using comprehension

h_letters = [ letter for letter in 'solanki' ]
print( h_letters, "\n\n")




#Simple
transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed, "\n\n")

#using list comprehension

matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print (transpose)
