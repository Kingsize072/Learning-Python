foo = 'hello'
def title():
    a = foo.title()
    return a
def upper( ):
    global foo
    a = foo.upper()
    return a
a = title( )
a = upper( )
print(a)