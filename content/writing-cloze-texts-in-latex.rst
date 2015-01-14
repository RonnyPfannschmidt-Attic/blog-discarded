writing cloze texts in latex 
=============================

:date: 2008-03-18


<pre syntax="latex">
\newif\ifstudents \newcommand{\cloze}[1]{\ifstudents\underline{\hphantom{#1}}\else #1\fi}
</pre>

<pre syntax="bash" tabsize="4">
	a
    b
</pre>