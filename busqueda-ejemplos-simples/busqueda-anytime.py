def max_sum_subarray(arr):
    def max_crossing_subarray(arr, low, mid, high):
        left_sum = float('-inf')
        sum = 0
        max_left = 0

        for i in range(mid, low - 1, -1):
            sum += arr[i]
            if sum > left_sum:
                left_sum = sum
                max_left = i

        right_sum = float('-inf')
        sum = 0
        max_right = 0

        for i in range(mid + 1, high + 1):
            sum += arr[i]
            if sum > right_sum:
                right_sum = sum
                max_right = i

        return (max_left, max_right, left_sum + right_sum)

    def max_subarray(arr, low, high):
        if low == high:
            return (low, high, arr[low])

        mid = (low + high) // 2

        left_low, left_high, left_sum = max_subarray(arr, low, mid)
        right_low, right_high, right_sum = max_subarray(arr, mid + 1, high)
        cross_low, cross_high, cross_sum = max_crossing_subarray(arr, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)

    return max_subarray(arr, 0, len(arr) - 1)

# Ejemplo de uso
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_sum_subarray(arr)
print("Subarreglo con suma máxima:", arr[result[0]:result[1] + 1])
print("Suma máxima:", result[2])
