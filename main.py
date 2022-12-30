if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=set(arr)
    arr=list(arr)
    assert n>=2 and n<=10
    for i in arr:
        assert i >=-100 and i<=100
    arr.sort()
    print(arr[-2])
