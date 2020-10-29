with open('clasic.in', 'r') as fin:
    with open('clasic.out', 'w') as fout:
        t = int(fin.readline())
        for _ in range(t):
            n = int(fin.readline())
            arr = [int(s) for s in fin.readline().split(" ")]
            xor_sum = arr[0]
            for i in range(1, n):
                xor_sum ^= arr[i]
            fout.write(str(xor_sum))
