First post
==========

:date: 2007-09-19
:tags: python, fastcgi, life


After some problems i got the first blog instance running.

It needed some python trickery::

    #!/usr/bin/python
    """
        TextPress FastCGI Runner
        ~~~~~~~~~~~~~~~~~~~~~~~~
    """
    import sys
    from os.path import join

    paths = """
    sqlalchemy/lib
    jinja
    pygments
    textpress
    werkzeug
    """[1:-1].split()

    BASE = '/home/ronny/Projects/web'

    for p in paths:
        sys.path.insert(0, join(BASE, p))

    from textpress import make_app
    from flup.server.fcgi import WSGIServer

    INSTANCE_FOLDER = join(BASE, 'textpress/instance')

    app = make_app(INSTANCE_FOLDER)

    srv = WSGIServer(app,
            bindAddress='/tmp/blog.sock',
            environ={'SCRIPT_NAME':''},
            umask=000,
            )

    if __name__ == '__main__':
        srv.run()

There are still some problems with the MetaBlog api and FileUpload, but i expect to solve them soon :)

*Update:* the problems are solved
