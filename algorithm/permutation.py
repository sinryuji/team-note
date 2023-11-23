def permutation(arr, r):
    used = [0 for _ in range(len(arr))]
    result = []

    def generate(chosen, used):
        if len(chosen) == r:
            result.append(chosen.copy())
            return

        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)
    return result


arr = [0, 1, 2, 3, 4, 5]

print(*permutation(arr, 3), sep="\n")
