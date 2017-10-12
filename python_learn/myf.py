def myfunc(*args,**kwargs):
    for i in range(40,100,3):
        print i
    print kwargs['name']


#myfunc(2,3,4,5,6,7,name='Dima', surname='Petrov') 

def say():
    what = 'Hello'
    print what

    def inner():
        foo = 'Foooooo'
        print foo
    return inner


#say()()

def wrap(func):
    print '<h1>'
    def inwrap():
        out = func()
        print out+'</h1>'
    return inwrap

@wrap
def add():
    return 'inner'


add()

#print what + ' ' + foo
   