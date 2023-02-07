def kth_rearrange(arr, left, right, k):
    while left < right:
        x = arr[(left + right) // 2]
        equal_x_first = left
        greater_x_first = left

        for i in range(left, right):
            now = arr[i]
            if now == x:
                arr[i] = arr[greater_x_first]
                arr[greater_x_first] = now

                greater_x_first += 1
            elif now < x:
                arr[i] = arr[greater_x_first]
                arr[greater_x_first] = arr[equal_x_first]
                arr[equal_x_first] = now

                greater_x_first += 1
                equal_x_first += 1

        if k < equal_x_first:
            right = equal_x_first - 1
        elif k >= greater_x_first:
            left = greater_x_first
        else:
            return


arr = [3, 5, 9, 9, 7, 0, 1, -3, 10]
print(arr, "- initial")

n = len(arr)

kth_rearrange(arr, 0, n, n - 1)  # max1
print(arr, " - max1")

kth_rearrange(arr, 0, n - 1, n - 2)  # max2, max3
print(arr, " - max2, max3")

kth_rearrange(arr, 0, n - 3, 2)  # min1, min2
print(arr, " - min1, min2")

if arr[-1] * arr[-2] * arr[-3] >= arr[-1] * arr[0] * arr[1]:
    print(arr[-1], arr[-2], arr[-3])
else:
    print(arr[-1], arr[0], arr[1])
