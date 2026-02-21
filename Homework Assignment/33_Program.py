def combination_sum2(candidates, target):
    candidates.sort()   # sort to handle duplicates
    result = []

    def dfs(start, remaining, path):
        if remaining == 0:
            result.append(path[:])
            return
        
        for i in range(start, len(candidates)):
            # skip duplicates
            if i > start and candidates[i] == candidates[i-1]:
                continue
            
            if candidates[i] > remaining:
                break
            
            dfs(i+1, remaining - candidates[i], path + [candidates[i]])

    dfs(0, target, [])
    return result


print(combination_sum2([10,1,2,7,6,1,5], 8))
print(combination_sum2([2,5,2,1,2], 5))