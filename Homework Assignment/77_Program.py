from collections import deque


# ---------- Sliding Window Maximum ----------
def sliding_window_max(arr, k):
    dq = deque()
    result = []

    for i in range(len(arr)):
        # Remove out-of-window elements
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Maintain decreasing order
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(arr[dq[0]])

    return result


# ---------- Sliding Window Minimum ----------
def sliding_window_min(arr, k):
    dq = deque()
    result = []

    for i in range(len(arr)):
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Maintain increasing order
        while dq and arr[dq[-1]] >= arr[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(arr[dq[0]])

    return result


# ===== Example Usage =====
arr = list(map(int, input("Enter array: ").split()))
k = int(input("Enter window size: "))

print("\nSliding Window Maximum:", sliding_window_max(arr, k))
print("Sliding Window Minimum:", sliding_window_min(arr, k))