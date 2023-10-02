def compress(s: str) -> str:
    result = []
    prev = ""
    count = 0

    for c in s:
        if c == prev:
            count += 1
        else:
            if prev != "" and count != 0:
                result.append(prev)
                result.append(str(count))

            prev = c
            count = 1

    result.append(prev) 
    result.append(str(count))

    return "".join(result)

if __name__ == "__main__":
    tests = [
        ("aabcccccaaa", "a2b1c5a3"),
    ]

    for input, expected in tests:
        actual = compress(input)
        print(f"{actual=}")
        print(actual == expected)
