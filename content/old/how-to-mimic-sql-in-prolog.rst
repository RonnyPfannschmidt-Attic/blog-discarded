how to mimic sql dql in prolog
==============================

:date: 2009-01-07 21:21


i just made up a prolog dsl for entering pseudo-sql queries.

the basic needs to get that done are this op defs::

    :- op(1080, fx, select).
    :- op(1070, yfy, where).
    :- op(1060, yfy, from).
    :- op( 900, yfy, join).
    :- op( 850, yfy, on).
    :- op( 800, xfx, [or, and]).
    :- op( 100, yfy, like).

so how do those work?
=====================



:select:          will just take a from/where expression - just for readablility
:where:           takes a from expression and a constraint expression
:from:            takes column listing and a table listing
:join:            takes a table name and a on expression/second table name
:on:              takes a table name and a join condition using normal prolog expressions
:like, and, or:   just normal operators to make expressions more nice


an example expression::

    select
        users(id, name),
        permission(name)
    from
        users
        join user_permissions
            on user(id) = user_permissions(user_id)
        join permissions
            on permissions(id) = user_permissions(permission_id)
    where
        users(id) = 1
        or users(name) like 'M?yer'.



whats missing?
==============

* an "as" operator for aliasing
* ddl stuff
* query analyis
