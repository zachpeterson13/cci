def check_permutation_nlogn(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    sorted1 = sorted(s1)
    sorted2 = sorted(s2)

    for i in range(len(sorted1)):
        if sorted1[i] != sorted2[i]:
            return False

    return True

def check_permutation_optimal(s1: str, s2: str) -> bool:
    counts = [0] * 256

    for char in s1:
        counts[ord(char)] += 1

    for char in s2:
        if counts[ord(char)] < 1:
            return False

        counts[ord(char)] -= 1

    return True


tests = [
    ("abc", "abc", True),
    ("abc", "acb", True),
    ("abc", "bac", True),
    ("abc", "bca", True),
    ("abc", "cba", True),
    ("abc", "cab", True),
    ("abc", "acb", True),
    ("abc", "bac", True),
    ("abc", "fds", False),
    ("abc", "fds", False),
    ("gokart", "kratog", True),
]

print("Test nlogn solution")
for s1, s2, expected in tests:
    actual = check_permutation_nlogn(s1, s2)

    print(f"{s1=}, {s2=}, {actual=}, {expected=}")

print("\nTest optimal solution")
for s1, s2, expected in tests:
    actual = check_permutation_optimal(s1, s2)

    print(f"{s1=}, {s2=}, {actual=}, {expected=}")
