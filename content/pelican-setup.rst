My Pelican Setup
================

:date: 2015-01-19

There is a nice way to combine tox and liveserver to work on and publish
pelican blogs:

:tox.ini:
    .. code:: ini

        [tox]
        skipsdist = true
        envlist = serve
        [testenv]
        whitelist_externals = rsync
        envdir = ./.env
        deps =
            livereload
            pelican
        commands=
            once: pelican
            serve: pelican --ignore-cache
            serve: python devserver.py
            publish: pelican -s publishconf.py --ignore-cache
            publish: rsync output/ bloghost:html/ -raPv

:devserver.py:
    .. code:: python

        import sys
        from livereload import Server
        server = Server()
        server.watch('content', 'pelican')
        server.watch('*.py', 'pelican')
        server.watch('chunk', 'pelican')
        server.serve(
            root='output',
            open_url='open' in sys.argv,
        )

This setup makes creative use of tox env marker,
its up to you to figure the details :)
