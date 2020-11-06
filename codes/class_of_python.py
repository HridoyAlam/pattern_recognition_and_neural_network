SUFFIXES = {1000:['KB','MB','GB','TB','PB','EB','ZB','YB'],
            1024:['KiB','MiB','GiB','TiB','PiB','EiB','ZiB','YiB']}

def approximate_size(size, a_kilobyte_is_1024_bytes=True):

    if(size<0):
        raise ValueError('Number must be non negative number')
    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000

    for sufix in SUFFIXES[multiple]:
        size /=multiple
        if size < multiple:
            return '{0:.3f} {1}'.format(size, sufix)
    raise ValueError('Number too large')
def f(x):
    return x%2 !=0 and x % 3 !=0

class Person:
    species = 'Human'
    #the init method is the constructor of the class
    
    def __init__(self,name,address):
        #self is the this pointer for the class
        self.name = name
        self.address=address

if __name__ == "__main__":

    p = Person('John','Abc/124')
    print(p.name)
    print(p.address)

    '''
    for i in range(2,25):
        print(f(i), end=" ")

    knights = {'gallaha':'The pure', 'robin':'The brave'}

    for k, v in knights.iteritems():
        print(k,v)
    '''
    '''
    print(approximate_size(100000000000,False))
    print(approximate_size(100000000000))
    print(5//2) #integer division
    print(""" a'v'a""")
    print('a', end=' ')
    print('b')
    print('a\nb')
    '''
    '''
    ##reserved word
    and, assert, break, class, continue, def, 
    del, elif, else, except, exec, finally, for, 
    from, global, if, import, in, is, lambda, not,
    or, pass, print, raise, return, try, while
    '''
    '''
    tu =(23, 'abc', 4.56,(2,3),'def')
    li = ["abc", 34, 4.34, 23]
    st = "Hello monami"
    print(tu,li)
    print(tu[1])
    print(st)
    print(st[1])
    #negative index: count from right , starting with -1
    print(tu[-3])
    # return a copy of subset
    print(tu[1:4])
    print(tu[1:-1])
    print(tu[:2])
    print(tu[2:])
    #copying whole sequence
    lis = tu # dependent copies, once changes affects to the others 
    lis = tu[:] #independent copies
    print(list)
    print(23 in lis)
    print(25 not in lis)
    print('m' in st)
    print((1,2,3) + (4,5,6))
    li.append(6)
    print(li)
    li.append([3,4,5])
    print(li)
    li.extend([3,4,6])
    print(li)
    '''
    '''
    a_set={'a',}
    print(type(a_set))
    a_set.add('b')
    print(a_set)
    print('a' in a_set)
    a_set.add('c')
    b_set = a_set.copy()
    c_set={'d','b','a','c'}
    print(a_set == c_set)
    
    print(a_set.intersection(c_set))
    print(a_set.union(c_set))
    print(a_set < c_set)
    print(a_set.issubset(c_set))
    
    c_set.remove('d')
    for i in c_set:
        print(i)
    
    #creating ditionary
    a_map = {}
    a_map = dict()
    #print(type(a_map))
    a_map['key1'] = 'value 1'
    a_map[2]= 'value 2'
    a_map[3.9] = 'value 3'
    a_map[True] = 'value 4'
    #print(a_map)
    #print(a_map[2])
    #print(len(a_map))

    #iterating over dictionary
    for key, value in a_map.items():
        print(f'{key:<4} {value}')

    #iterating over key/value
    for val in a_map.values():
        print(val)
    '''
    