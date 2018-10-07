def is_palindromic(k):
    """return True if k is palindromic, False if not"""
    list_k = [int(i) for i in str(k)]
    n=len(list_k)

    for i in range(n//2):

        if list_k[i] != list_k[n-1-i]:
            return False

    return True

assert(is_palindromic(45654))


def reverse(k):
    """create the reverse of k
    example : reverse(456) = 654"""

    list_k = [int(i) for i in str(k)]
    str_rev_k = ''
    n = len(list_k)
    
    for i in range(n):
        str_rev_k += str(list_k[n-1-i])

    return(int(str_rev_k))

assert(reverse(45689)==98654)

def is_lychrel(k):
    """return True if k is a Lychrel number, false if it's not"""
    a = k + reverse(k)
    i = 1
    while i < 51 and not(is_palindromic(a)):
        a = a + reverse(a)
        i += 1
        
    return(not(is_palindromic(a)))

assert(is_lychrel(4994))

def solve():
    """return the number of Lychrel numbers below 10 000 (without it)"""
    nb_lychrel = 0

    for k in range(10000):
        if is_lychrel(k) :
            nb_lychrel +=1

    return nb_lychrel

print('the solution of the 55th euler problem is ' + str(solve()))
