def urlify_1(input: str) -> str:
    list = input.split()

    return "%20".join(list)

def urlify_2(input: str, length: int) -> str:
    c_list = [*input]

    end = len(input)  - 1

    for i in range(length - 1, -1, -1):
        if c_list[i] != " ":
            c_list[end] = c_list[i]
            end -= 1
        else:
            c_list[end] = "0"
            end -= 1
            c_list[end] = "2"
            end -= 1
            c_list[end] = "%"
            end -= 1

    return "".join(c_list)

tests = [
    ("Mr John Smith    ", 13, "Mr%20John%20Smith"),
]

print("Non-inplace urlify")
for input, _, expected in tests:
    actual = urlify_1(input)
    result = (actual == expected)

    print(f"{input=}, {actual=}, {result=}")

print("Inplace urlify")
for input, length, expected in tests:
    actual = urlify_2(input, length)
    result = (actual == expected)

    print(f"{input=}, {actual=}, {result=}")
