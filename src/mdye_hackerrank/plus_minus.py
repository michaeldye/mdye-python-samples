"""."""

if __name__ == "__main__":
    size = int(input())
    values = map(int, input().split())

    pos = neg = 0
    for v in values:
        if v > 0:
            pos += 1
        elif v < 0:
            neg += 1
    zer = size - (pos + neg)

    for ratio in [pos / size, neg / size, zer / size]:
        print(f"{ratio:.6f}")
