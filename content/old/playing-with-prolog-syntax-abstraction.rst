playing with prolog syntax abstraction
======================================

:date: 2009-01-07
:tags: prolog


i just feel in love :)

.. code:: prolog

    :- op(1070, fx, build).
    :- op(1100, fx, tool).
    :- op(1050, yfx, from).

    :- op(1060, xfx, by).
    :- op(1050, fx, executing).
    :- op(1090, xfx, will).
    :- op(900, fx, [lib, bin, pkg, glob]).
    :- dynamic build_implicit/2.

    build
        lib util
        from
            glob 'src/lib/*.c',
            pkg 'gtk+'>='2.10.0'.
    build
        bin test
        from
            lib util,
            glob 'src/bin/*.c',
            pkg 'gtk+'>='2.10.0'.


    tool 'gcc' will
        build '%.o'
        from '%.c'
        by executing 'gcc -c -o %.o %.c'.


    target(X, D) :- build X from D.
    targets(XL) :- findall(X, target(X, _), XL).

    comma2l(X,[X]) :- (_,_) \= X.
    comma2l((X, C), [X|R]) :- comma2l(C,R).

    :- findall(dt(X,D), (target(X,T), comma2l(T,D)), L), write(L).
    :- targets(XL), write(XL), nl.
    depends( X, Y ) :- target(X, D), comma2l(D, DL), member(Y, DL).

    depends_target(X,Y) :- depends( X,Y), target(Y,_).

It's valid prolog code, but mostly a toy.

Next thing i'll try to do is a small forward/backward inference machine thats supposed to be able to deal with simple c and vala deps

