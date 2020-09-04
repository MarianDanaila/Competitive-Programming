t = int(input())
for _ in range(t):
    p, f = [int(s) for s in input().split(" ")]
    cnt_s, cnt_w = [int(s) for s in input().split(" ")]
    s, w = [int(s) for s in input().split(" ")]
    if s > w:
        s, w = w, s
        cnt_s, cnt_w = cnt_w, cnt_s
    ans = 0
    for s1 in range(min(p//s, cnt_s)+1):  # how many swords s1 I can take
        w1 = min(cnt_w, (p-s1*s)//w)  # how many axes I can take after I took swords
        s2 = min(cnt_s-s1, f//s)  # how many swords the follower can take
        w2 = min(cnt_w-w1, (f-s2*s)//w)  # how many axes the follower can take
        ans = max(ans, s1+w1+s2+w2)
    print(ans)
