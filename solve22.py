def extract ():
    """returnthe list of the name in p022_names.txt"""
    name_list=[]
    for line in open('p022_names.txt', 'r'):
        for almost_name in line.split(','):
            name_list.append(almost_name[1:-1])
    return name_list

def value(name):
    """return the value of the name"""
    offset = ord('A') -1
    return sum(ord(c) - offset for c in name)

assert(value('COLIN') == 53)

def solve():
    """return the total of a the names value in the files"""
    ans = 0
    for index in enumerate(sorted(extract())):
        ans += value(index[1]) * (index[0]+1)
    return ans

print('the solution of the 22nd euler problem is ' + str(solve())) 
