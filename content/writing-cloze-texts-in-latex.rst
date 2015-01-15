writing cloze texts in latex
=============================

:date: 2008-03-18

..code:: latex

    \newif\ifstudents \newcommand{\cloze}[1]{\ifstudents\underline{\hphantom{#1}}\else #1\fi}

::

	a
    b

