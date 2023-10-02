def perm_pal(s: str) -> bool:
    counts = [0] * 26
    spaces = 0

    for c in s.lower():
        if c == " ":
            spaces += 1
        else:
            counts[ord(c) - ord('a')] += 1

    odd = ( len(s) - spaces ) % 2 == 1

    for count in counts:
        if count % 2 == 0:
            continue

        if count % 2 == 1 and odd == True:
            odd = False
        else:
            return False

    return True

if __name__ == "__main__":
    tests = [
        ("Tact Coa", True),
        ("Tact oa", False),
        ("aabbccd", True),
        ("aabbccda", False),
    ]

    for input, expected in tests:
        actual = perm_pal(input)
        result = ""
        if actual == expected:
            result = "PASSED"
        else:
            result = "FAILED"

        print(f"{result}: {input} -> {actual}, {expected=}")
