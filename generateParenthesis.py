
def generate(num):
    if num == 0:
        return [""]
    ans = []
    for i in range(num):
        for left in generate(i):
            for right in generate(num - i -):
                ans.append('('+left+')'+right)
    return ans

if __name__ == "__main__":
    print(generate(2))