MOD = 10**9 + 7
        n = len(arr)

        # Sort the array in ascending order
        arr.sort()

        # Calculate the maximum value of ∑arr[i]*i
        max_sum = 0
        for i in range(n):
            max_sum = (max_sum + arr[i] * i) % MOD

        return max_sum