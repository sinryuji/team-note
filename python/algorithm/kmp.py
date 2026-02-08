def kmp_table(pattern):
    table = [0] * len(pattern)

    pidx = 0
    for idx in range(1, len(pattern)):
        while pidx > 0 and pattern[idx] != pattern[pidx]:
            pidx = table[pidx - 1]

        if pattern[idx] == pattern[pidx]:
            pidx += 1
            table[idx] = pidx

    return table

def kmp(word, pattern):
    table = kmp_table(pattern)

    print(table)

    results = []
    pidx = 0

    for idx in range(len(word)):
        # 단어와 패턴이 일치하지 않는 경우, pidx를 table을 활용해 값 변경
        while pidx > 0 and word[idx] != pattern[pidx] :
            pidx = table[pidx-1]
        # 해당 인덱스에서 값이 일치한다면, pidx를 1 증가시킴
        # 만약 pidx가 패턴의 끝까지 도달하였다면, 시작 인덱스 값을 계산하여 추가 후 pidx 값 table의 인덱스에 접근하여 변경
        if word[idx] == pattern[pidx]:
            if pidx == len(pattern) - 1:
                results.append(idx - len(pattern) + 1)
                pidx = table[pidx]
            else:
                pidx += 1

    return results

print(kmp('abcdefbcbcdg', 'bcd'))
print(kmp('abababcababefabaabcdg', 'abab'))
