simple cached for properties done right
=======================================

:date: 2008-08-12
:tags: python


Since people all over the place seem to get caching properties in python wrong, thus polluting the instance with weird attributes,

here the correct way to do it:
<sourcecode syntax="python">
class cached_property(object):
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        
        result = self.func(obj) 
        setattr(obj, self.name, result)
        return result
</sourcecode>

So, what the heck does this one do.

First, this is a <strong>non-data</strong> property, so an instance slot will <strong>override</strong> the class slot.

Second, on the first access it computes the result via the class slot and puts it into the instance sloth.

Result, after the first access any subsequent access will use the instance-slot and not redo the computation.

Basic usage:
<sourcecode syntax="pycon">
>>> class Test(object):
...     @cached_property
...     def test(self):
...         print 1
...         return 2
...
>>> t = Test()
>>> t.test
1
2
>>> t.test
2
>>> t.test
2
</sourcecode>

For a more powerful cached property, take a look at the utility classes of <a href="http://werkzeug.pocoo.org">Werkzeug</a>.