toying with the hg api
======================

:date: 2009-08-24
:tags: python, versioncontroll, hg
:category: old


I recently started to write some scripts to help with release-cycles in pida
here is an early version of the tool we'll use as base for version-bumping plugins within the main repo::

  #!/usr/bin/python

  from os import path
  from mercurial.ui import ui as Ui
  from mercurial.localrepo import localrepository as LocalRepo


  ui = Ui()
  repopath = path.dirname(path.dirname(path.abspath(__file__)))

  repo = LocalRepo(ui, repopath)

  wctx = repo['.']

  plugin_files = [file for file in wctx
                  if file.startswith('pida-plugins')]

  for file in plugin_files:
      # we only want plugins
      base, name = file.rsplit('/', 1)
      if name == 'service.pida':
          #XXX: inaccurate, but reasonable
          last_bump = wctx[file].linkrev()

          #XXX: the selection could be smarter
          last_plugin_change = max(wctx[r].linkrev()
                                   for r in plugin_files if r.startswith(base))
          needs_bump = last_bump < last_plugin_change

          print path.basename(base), \
                last_bump, last_plugin_change, \
                'bump' if needs_bump else 'ignore'

For now all the bugger does is get me reasonable accurate version numbers,
for plugin changes versus plugin metadata changes.

The next exercise is to have the script edit the metadata files in the workdir.
