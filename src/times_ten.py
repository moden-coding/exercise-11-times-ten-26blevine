# Write your solution here
def times_ten(start_index: int, end_index: int):
    vals = {}
    for i in range (start_index, end_index+1):
        vals[i] = 10*i
    return vals


if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)