"""
Platform : Codeforces
Contest  : Round 1105 (Div. 2)

Problem  : A - Another Popcount Problem

Tags:
- Greedy
- Constructive
- Mathematics
- Bit Manipulation

Complexity:
Time  : O(log n)
Space : O(1)

Key Idea:
Represent every number using either (2^m - 1) or (2^(m+1) - 1),
then compute the optimal mix to maximize the total popcount.
"""

def solve():
    n, k = map(int, input().split())

    # If we have at least n numbers,
    # use n numbers equal to 1 and the remaining numbers as 0.
    if k >= n:
        print(n)
        return

    # Find the largest feasible lower pole
    m = 0
    while k * ((2 ** m) - 1) <= n:
        m += 1
    m -= 1

    # Define the two poles
    lower = (2 ** m) - 1
    upper = (2 ** (m + 1)) - 1

    # Solve:
    # upper * a + lower * (k - a) = n
    a = (n - lower * k) // (upper - lower)

    # Maximum total popcount
    answer = a * (m + 1) + (k - a) * m

    print(answer)


t = int(input())

for _ in range(t):
    solve()


# Status: Accepted
# Notes available in Notion (Project Brightstar)
