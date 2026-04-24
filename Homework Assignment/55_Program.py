class Solution:
    def equalPartition(self, arr):
        n = len(arr)
        total = sum(arr)
        target = total // 2

        # Required size of one subset
        need = n // 2

        result = []

        def backtrack(idx, count, curr_sum, path):
            if count == need:
                if curr_sum == target:
                    result.extend(path[:])
                    return True
                return False

            if idx == n:
                return False

            if count > need or curr_sum > target:
                return False

            # Take current element
            path.append(arr[idx])
            if backtrack(idx + 1, count + 1, curr_sum + arr[idx], path):
                return True
            path.pop()

            # Skip current element
            if backtrack(idx + 1, count, curr_sum, path):
                return True

            return False

        backtrack(0, 0, 0, [])

        # Build second subset
        used = {}
        for x in result:
            used[x] = used.get(x, 0) + 1

        second = []
        for x in arr:
            if used.get(x, 0):
                used[x] -= 1
            else:
                second.append(x)

        return [result, second]