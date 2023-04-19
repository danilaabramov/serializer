def serialize(numbers):
    if not numbers:
        return ""
    prev = numbers[0]
    count = 1
    result = []
    for i in range(1, len(numbers)):
        if numbers[i] == prev:
            count += 1
        else:
            result.append(str(prev) + "x" + str(count))
            prev = numbers[i]
            count = 1
    result.append(str(prev) + "x" + str(count))
    return ",".join(result)


def deserialize(s):
    if not s:
        return []
    result = []
    for x in s.split(","):
        num, count = x.split("x")
        result.extend([int(num)] * int(count))
    return result


tests = [
    [1] * 50 + [2] * 50,  # random sequence 1
    [1] * 1000,  # all 1-digit numbers
    [11] * 1000,  # all 2-digit numbers
    [111] * 1000,  # all 3-digit numbers
    [1] * 300 + [2] * 300 + [3] * 300,  # repeating sequence of 3 numbers
    [1, 2, 3, 4, 5],  # short sequence
    list(range(1, 101)),  # first 100 numbers
    list(range(201, 301)),  # last 100 numbers
]

for numbers in tests:
    s = serialize(numbers)
    assert all(ord(c) < 128 for c in s), "Serialized string contains non-ASCII characters"
    assert len(s) <= len(numbers) * 3, "Serialization not compact enough"
    assert deserialize(s) == numbers, "Deserialization failed"
    print(f"Input: {numbers},\n Serialized: {s},\n Compression ratio: {len(s) / len(numbers):.2f}")
