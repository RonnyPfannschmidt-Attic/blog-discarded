diggin up clonedigger
=====================

:date: 2008-06-11
:tags: python, clonedigger


Recently i discovered clonedigger. It looks like a nice toy, but some serious issues pissed me off.

It wont detect clones on:
* Reordered instruction sequences
* Variances between named variables

so the following 3 functions simply won't get detected as the same thing

..code:: python

    def means_1(l):
        ll = len(l)
        ls = sum(l)
        return ls/ll

    def means_2(x):
        ls = sum(x)
        ll = len(x)
        return ls/ll

    def means_3(x):
        return sum(x)/len(x)

So i decided to take a look into 2 things
1. clean the code up to be more pythonic
2. switch from statement sequences to isomorph graphs in order to get invariant of the variables/temporaries
