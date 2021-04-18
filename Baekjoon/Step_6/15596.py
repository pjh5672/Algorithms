def solve(a: list) -> int:
    ans = 0
    for num in a:
        ans += num
    return ans

if __name__ == "__main__":
    a = [1, 2, 3, 4]
    print(solve(a))