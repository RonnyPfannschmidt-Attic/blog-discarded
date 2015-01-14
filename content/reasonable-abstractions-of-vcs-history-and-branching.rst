reasonable abstractions of vcs history and branching
====================================================

:date: 2009-01-12
:tags: versioncontroll, anyvc


<p> I spend much time on figuring a good pattern, here is what i came up with so far.</p>
<p> i will ignore the possibility of multiple projects per repo </p>
<p> this is for <a href="http://www.bitbucket.org/RonnyPfannschmidt/anyvc/">anyvc</a></p>

<h3> Object types </h3>
<dl>
<dt> repository
<dd> stores revisions and metadata

<dt> workingset 
<dd> set of branches/heads from the repository thats located on a different physical location

<dt> branch
<dd> a line of development, may have multiple heads

<dt> workdir 
<dd> connected to a revision in a branch
</dl>

<h3> relations of those for common vcs's </h3>

<h4> mercurial </h4>

<h5> normal </h5>
<pre>
 repo = workingset
 1 workingset - n branches
 1 revision in the dag - the workdir
</pre>

<h5> store nesting </h5>
<small><b> warning: not yet implemented, don't try finding it </b></small>
<pre>
 1 repo - n workingsets
 1 workingset - n branches
 1 revision in the dag - the workdir
</pre>   


<h4> bazaar </h4>
<small><b> this might change soon, they will add various improvements </b></small>

<h5> normal </h5>
<pre>
 repo = workingset
 workingset = branch
 tip of the branch = workdir
</pre>

<h5> with repository </h5>
<pre>
 1 repo - n workingsets
 workingset = branch
 tip of the branch = workdir</pre>
</pre>


<h4> git </h4>
<p>
  i'm not entirely understanding the relations of references with git, <br>
  branches are just named pointers that may move, <br>
  tags are just named pointers that don't move, <br>
  this might cause some changes to the abstraction later
</p>
<pre>
  repo = workingset
  1 workingset - n branches
  wordir = pointing to a rev, 
           might not belong to "normal" branches,
           will be the HEAD branch, 
           confusing till i dive in more
</pre>

<h4> subversion </h4>
<p>
  branching patterns are horrible here, <br> 
  branches are not real branches, but copies of a tree. <br>
  There might be need for a mapping tool that allows to configure non-default patterns.
</p>
<p>
  Branch management is rather tricky as even the default ways for branching have messy schemes, common ones are :
  <ul>
  <li> /trunk + /branch/*
  <li> /{project}/tunk + /{project}/branches/*
  <li> /trunk/{project} + /branches/{project}/*
  </ul>
  note that a * might be more than one level deep (ie nested structures for branches)
</p>
<pre>
  repo = workingset
  1 workingset - n branches
  workdir = pointing to subdir + rev of the repo
</pre>

   
