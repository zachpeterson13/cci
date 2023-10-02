def is_unique(s: str) -> bool:
    counts = [0] * 26

    for char in s:
        counts[ord(char) - ord('a')] += 1

    for count in counts:
        if count > 1:
            return False

    return True

def is_unique_nlogn(s: str) -> bool:
    sorted_s = sorted(s)

    for i in range(1, len(sorted_s)):
        if sorted_s[i] == sorted_s[i - 1]:
            return False

    return True

tests = [
    ("abcdefg", True),
    ("abcdefga", False),
    ("test", False)
]


print("Optimal Test")
for test, expected in tests:
    actual = is_unique(test)

    print(f"is_unique(\"{test}\") => {actual} == {expected}")

print("Sorted nlogn test")
for test, expected in tests:
    actual = is_unique_nlogn(test)

    print(f"is_unique_nlogn(\"{test}\") => {actual} == {expected}")
