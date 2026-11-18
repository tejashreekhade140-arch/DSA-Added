def rotateArray(arr, k):
    n = len(arr)
    k = k % n

    result = arr[-k:] + arr[:-k]

    print(result)


arr = [1, 2, 3, 4, 5]
k = 2

rotateArray(arr, k)