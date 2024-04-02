def combination(arr, r):
    arr = sorted(arr)
    result = []

    def generate(chosen):
        if len(chosen) == r:
            result.append(chosen.copy())
            return

        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen)
            chosen.pop()

    generate([])
    return result

arr = [1, 2, 3, 4, 5]

print(*combination(arr, 2), sep="\n")
