def one_away(s1: str, s2: str) -> bool:
    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    elif len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)
    elif len(s1) - 1 == len(s2):
        return one_edit_insert(s2, s1)
    else:
        return False

def one_edit_replace(s1: str, s2: str):
    found_diff = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if found_diff == True:
                return False
            
            found_diff = True

    return True

def one_edit_insert(s1: str, s2: str):
    idx1 = 0
    idx2 = 0

    while(idx1 < len(s1) and idx2 < len(s2)):
        if s1[idx1] != s2[idx2]:
            if idx1 != idx2:
                return False
            else:
                idx2 += 1
        else:
            idx1 += 1
            idx2 += 1

    return True

if __name__ == "__main__":
    tests = [
        ("pale", "ple", True),
        ("pales", "pale", True),
        ("pale", "bale", True),
        ("pale", "bake", False),
    ]

    for s1, s2, expected in tests:
        actual = one_away(s1, s2)

        result = ""
        if actual == expected:
            result = "PASSED"
        else:
            result = "FAILED"

        print(f"{result}: {s1}, {s2} => {actual}, {expected=}")
