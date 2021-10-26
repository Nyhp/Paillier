from random import randint


def xgcd(a,b):

    # algorithme d'euclide etendue
    # resultat donne u = pgcd(a,b), prevx, prevy
    # tel que u = a*prevx+b*prevy

    u, v = a, b    
    prevx, x = 1, 0
    prevy, y = 0, 1
    while v:
        q = u//v
        x, prevx = prevx - q*x, x
        y, prevy = prevy - q*y, y
        u, v = v, u % v
    return u, prevx, prevy


def inverse_mod(a, n):
    return xgcd(a,n)[1]


def fast_exp(x, d, n):
    res = 1
    e = int(d)
    b = x % n
    while e > 0:
        if (e % 2) == 1:
            res = (res * b) % n
        e = e//2
        b = (b*b) % n
    return res


def miller_rabin(n, k):

    # tester la primalité

    a = n-1
    r = 0
    while a % 2 == 0:
        a //= 2
        r += 1

    probably_prime = True
    i = 0
    while probably_prime and i < k:
        x = randint(2, n-2)
        y = fast_exp(x, a, n)
        if y != 1:
            s = 0
            while (y != n-1) and s < r:
                y = (y*y) % n
                s += 1
            if r == s:
                probably_prime = False
        i += 1
    return probably_prime


def keygen(t):
    p = randint(2**t, 2**(t+1)-1)
    q = randint(2**t, 2**(t+1)-1)
    while not(miller_rabin(p, 40)):
        p = randint(2**t, 2**(t+1)-1)
    while not(miller_rabin(q, 40)):
        q = randint(2**t, 2**(t+1)-1)
    n = p*q
    phi = (p-1)*(q-1)
    return n, phi


def encrypt(m, n):
    n2 = n*n
    r = randint(1, n-1)
    while gcd(r, n) != 1:
        r = randint(1, n-1)
    c = ((1+ m*n) * fast_exp(r, n, n2)) % n2
    return c


def decrypt(c, phi, n):
    n2 = n*n
    u = fast_exp(c, phi, n2)
    v = (u-1)//n
    invphi = inverse_mod(phi, n)
    return (v*invphi) % n



#n = 180585254229520806992356330271205057631
#phi = 180585254229520806965353755835724978952
#c = 13981511398366331069700996544253417796286332621182290317515950403624672975049
#m = 314159265358979323846264338327950288

#if m == decrypt(c, phi, n):
#    print("True")



def resultat_vote(n, phi, c, K):
    m = decrypt(c, phi, n)
    #print(m)
    base = K+1
    res = []
    for i in range(5):
        res.append(m % base)
        m //= base
    return res
    

#K = 999
#n = 11782660460700170193881163797977
#phi = 11782660460700163275084254500276
#c = 19074361871670584185726380367241674764948942803394260821772420
#r = [201, 420, 17, 0, 362]

#if r == resultat_vote(n, phi, c, K):
#    print("True")








