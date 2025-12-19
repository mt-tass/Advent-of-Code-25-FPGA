def get_joltage(line : str) -> int:
    num1 = line[0]
    num2 = "0"
    count = 0
    for char in line[1:] :
        count += 1
        if (char > num1) and (count != len(line) - 1):
            num1 = char
            num2 = "0"
            continue
        elif (char > num2):
            num2 = char
    ans = 10*int(num1) + int(num2)
    return ans

def get_joltage2(line: str, digits: int = 12) -> int:
    n = len(line)
    result = ["0"] * digits
    last_position = -1
    for i in range(digits):
        remaining_needed=digits-(i+1)
        search_end=n - remaining_needed
        search_start=last_position+1
        max_digit = line[search_start]
        max_position = search_start
        for j in range(search_start + 1, search_end):
            if line[j] > max_digit:
                max_digit = line[j]
                max_position = j
        result[i] = max_digit
        last_position = max_position

    return int("".join(result))
num = 0
numtwo = 0
with open("data.txt") as f:
    for line in f:
        line = line.strip()
        #num = num+get_joltage(line)
        num = num+get_joltage2(line,2)
        numtwo=numtwo+get_joltage2(line,12)

print(num)
print(numtwo)
