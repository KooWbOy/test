t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    suma = sum(a)
    if suma < s:
        print(-1)
    elif suma == s:
        print(0)
    else:
        curs = 0
        i = 0
        while curs < s:
            curs += a[i]
            # print(curs)
            i += 1
        ln = i + 1
        maxln = ln
        right = i
        left = 1
        while True:
            Break = False
            while a[right] == 0:
                right += 1
                if right == len(a):
                    Break = True
                    break
            if Break:
                break
            ln = right + 1
            while a[left] == 0:
                left += 1
            ln -= left
            if ln > maxln:
                maxln = ln
        print(n - maxln)
