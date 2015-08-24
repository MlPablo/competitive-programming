n, m = list(map(int, open('input.txt', 'r').readline().split(' ')[0:2]))
# A181245
res = [
    [    2,      4,         8,          16,             32,               64],
    [    4,     14,        50,         178,            634,             2258],
    [    8,     50,       322,        2066,          13262,            85126],
    [   16,    178,      2066,       23858,         275690,          3185462],
    [   32,    634,     13262,      275690,        5735478,        119310334],
    [   64,   2258,     85126,     3185462,      119310334,       4468252414],
    [  128,   8042,    546410,    36806846,     2481942354,     167341334542],
    [  256,  28642,   3507314,   425288998,    51630303190,    6267120468434],
    [  512, 102010,  22512862,  4914052362,  1074033301458,  234710735573170],
    [ 1024, 363314, 144506294, 56780001474, 22342450688162, 8790181730741270]
]


def a(n, m):
    if n < m:
        m,n = n,m
    # m <= n
    if n <= 10 and m <= 6:
        return res[n-1][m-1]
    if m == 1: return 2**n
    if m == 2: return 3*a(n-1,m)+2*a(n-2,m)
    if m == 3: return 6*a(n-1,m)+3*a(n-2,m)-2*a(n-3,m)


open('output.txt', 'w').write(str(a(n,m)))
