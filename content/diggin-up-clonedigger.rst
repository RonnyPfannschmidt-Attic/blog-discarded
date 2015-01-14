diggin up clonedigger
=====================

:date: 2008-06-11
:tags: python, clonedigger


Recently i discovered clonedigger. It looks like a nice toy, but some serious issues pissed me off.

It wont detect clones on:
<ol>
<li> Reordered instruction sequences
<li> Variances between named variables
</ol>

so the following 3 functions simply won't get detected as the same thing

<pre syntax="python">
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
</pre>

So i decided to take a look into 2 things
<ol>
<li>clean the code up to be more pythonic
<li>switch from statement sequences to isomorph graphs in order to get invariant of the variables/temporaries
</ol>