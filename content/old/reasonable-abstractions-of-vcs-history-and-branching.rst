reasonable abstractions of vcs history and branching
====================================================

:date: 2009-01-12 00:00
:tags: versioncontroll, anyvc

I spend much time on figuring a good pattern,
here is what i came up with so far.
I will ignore the possibility of multiple projects per repo
this is for anyvc_ .

.. _anyvc: http://bitbucket.org/RonnyPfannschmidt/anyvc/

Object types
------------

:repository: stores revisions and metadata
:workingset: set of branches/heads from the repository
             thats located on a different physical location
:branch: a line of development, may have multiple heads
:workdir: connected to a revision in a branch


relations of those for common vcs's
++++++++++++++++++++++++++++++++++++++

mercurial

  normal::

    repo = workingset
    1 workingset - n branches
    1 revision in the dag - the workdir

  store nesting (not yet implemented)::

    1 repo - n workingsets
    1 workingset - n branches
    1 revision in the dag - the workdir


bazaar
  **this might change soon, they will add various improvements**

  normal::

    repo = workingset
    workingset = branch
    tip of the branch = workdir

  with repository::

    1 repo - n workingsets
    workingset = branch
    tip of the branch = workdir</pre>


git
  i'm not entirely understanding the relations of references with git,
  branches are just named pointers that may move,
  tags are just named pointers that don't move,
  this might cause some changes to the abstraction later::

    repo = workingset
    1 workingset - n branches
    wordir = pointing to a rev,
             might not belong to "normal" branches,
             will be the HEAD branch,
             confusing till i dive in more

subversion
  branching patterns are horrible here,
  branches are not real branches, but copies of a tree.
  There might be need for a mapping tool that allows to configure non-default patterns.

  Branch management is rather tricky as even the default ways for branching have messy schemes, common ones are :

  * /trunk, /branch/${branch}
  * /{project}/tunk + /{project}/branches/${branch}
  * /trunk/{project} + /branches/{project}/${branch}

  note that a branches might be more than one level deep::

    repo = workingset
    1 workingset - n branches
    workdir = pointing to subdir + rev of the repo


