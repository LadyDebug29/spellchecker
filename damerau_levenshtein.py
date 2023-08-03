def calculate_distance(first_word, second_word):
    ans = [[0 for _ in range(len(second_word) + 1)]
           for _ in range(len(first_word) + 1)]
    for i in range(len(first_word) + 1):
        ans[i][0] = i
    for i in range(len(second_word) + 1):
        ans[0][i] = i

    for i in range(1, len(first_word) + 1):
        for j in range(1, len(second_word) + 1):
            cost = 1 * (first_word[i - 1] != second_word[j - 1])
            ans[i][j] = min(ans[i - 1][j] + 1, ans[i][j - 1] + 1, ans[i - 1][j - 1] + cost)
            if first_word[i - 1] == second_word[j - 2] and first_word[i - 2] == second_word[j - 1]:
                ans[i][j] = min(ans[i][j], ans[i - 2][j - 2] + cost)
    return ans[-1][-1]

