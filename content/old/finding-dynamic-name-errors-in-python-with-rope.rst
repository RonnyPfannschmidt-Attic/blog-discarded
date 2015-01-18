finding dynamic name-errors in python with rope
===============================================

:date: 2008-08-01
:category: old
:tags: python
:slig: find-python-name-errors-with-rope

Im really unhappy with pylint/pyflakes cause their analysis is entirely static.

But thanks to Rope_ by Ali Gholami Rudi thats no longer a Problem.

.. _rope: http://rope.sourceforge.net/

A simple test to show the power of rope
for finding missing names in the context of star-import
and access to non-existing attributes.

My test files are:

:test.py:
    .. code:: python

        def test1():
            return a #error 1

        b = 1

        def test2():
            return b

        def test3():
            c = 1
            return b, a #error 2

        def test4():
            c = 1
            return b, c
:test2.py:
    .. code:: python


        from test import *


        b
        abc #error a


        class Test:
            def __init__(self):
                self.x = 123


        t = Test()
        t.x
        t.abc #error b

While pyflakes/pylint are only able to find the numbered errors
a simple rope script is able to find all of them all.
Its mostly based on a simple example ali gave to me.

.. code:: python

    #!/usr/bin/python
    import glob
    from rope.base.project import Project
    from rope.contrib.finderrors import find_errors

    def scan_test():
        project = Project('/home/ronny/Projects/web/textpress')
        for f in project.get_files():
            if f.name.endswith('py'):
                for error in find_errors(project, f):
                    print f.path, error

    scan_test()


