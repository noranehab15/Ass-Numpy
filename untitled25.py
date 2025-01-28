import numpy as np

arr = np.array([1, 2, 3, 4])
test = np.all(arr != 0)
print("none of the elements of a given array is zero:" , test)

arr1 = np.array([0, 0, 3, 0])
result = np.any(arr1 != 0)
print("Any of the elements is non-zero:", result)

zeros_array = np.zeros(10)
ones_array = np.ones(10)
fives_array = np.ones(10) * 5
print("Array of 10 zeros:", zeros_array)
print("Array of 10 ones:", ones_array)
print("Array of 10 fives:", fives_array)

arr = np.arange(30, 71)
print("Array :", arr)

identity_matrix = np.eye(3)
print(identity_matrix)

random_number = np.random.rand()
print("random number between 0 and 1:", random_number)

random_array = np.random.randn(15)
print("array:", random_array)

vector = np.arange(15, 56)
print(" all values except the first and last:" , vector[1:-1])

vector = np.random.randint(0, 11, size=5)
print(vector)

matrix = np.zeros((10, 10), dtype=int )
matrix[0, :] = 1
matrix[-1, :] = 1
matrix[:, 0] = 1
matrix[:, -1] = 1

print(matrix)

matrix = np.zeros((5, 5), dtype=int)
np.fill_diagonal(matrix, [1, 2, 3, 4, 5])

print(matrix)

matrix = np.zeros((4, 4), dtype=int)
for i in range(4):
 for j in range(4):
  if i != j:
     matrix[i, j] = (i + j) % 2
print(matrix)

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])

np.savez_compressed('arrays_data.npz', arr1=array1, arr2=array2)
loaded_data = np.load('arrays_data.npz')
loaded_array1 = loaded_data['arr1']
loaded_array2 = loaded_data['arr2']

print("Loaded array 1:", loaded_array1)
print("Loaded array 2:", loaded_array2)

random_values = np.random.rand(40)
print(random_values)

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
specified_number = 35
less_than = arr[arr < specified_number]
greater_than = arr[arr > specified_number]

print(f"Numbers less than {specified_number}:" , less_than)
print(f"Numbers greater than {specified_number}:" ,greater_than)
