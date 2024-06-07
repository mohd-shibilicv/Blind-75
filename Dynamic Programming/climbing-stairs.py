def climb_stairs_using_recursion(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return climb_stairs_using_recursion(n - 1) + climb_stairs_using_recursion(n - 2)


def climb_stairs_using_memoization(n: int, memo: dict = {}) -> int:
    if n == 0 or n == 1:
        return 1

    if n not in memo:
        memo[n] = climb_stairs_using_memoization(
            n - 1, memo
        ) + climb_stairs_using_memoization(n - 2, memo)
    return memo[n]


def climb_stairs_using_tabulation(n: int) -> int:
    if n == 0 or n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def climb_stairs_using_space_optimization(n: int) -> int:
    if n == 0 or n == 1:
        return 1

    prev, current = 1, 1
    for i in range(2, n + 1):
        temp = current
        current = prev + current
        prev = temp

    return current


print(climb_stairs_using_recursion(3))
