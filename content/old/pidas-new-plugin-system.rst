================================
pida's new plugin system - draft
================================

:date: 2008-08-08
:tags: python, pida, old, draft


this is a draft, feel free to report anything that looks plain wrong.


For the upcoming pida release i did a larger refactoring
 which includes some nice changes in the api.

Basic Structure
===============

There are 3 Kinds of loadable Entity

:Editors: Currently there is Vim, Emacs and medit,
          usually only one of them is loaded
:Services: They define pida's core functionalities,
           all of them are always loaded
:Plugins: They contain all optional components,
          they are reloadable and updatable.


All of those are startable and stoppable.
(services/editors get only stopped when exiting pida).


Also each of those may have one or more of the following:

Featuresconfig
    defines feature entry points of the plugin,
    registers features to the entry points
    (for example vcs integration is done by registering anyvc vcs's
    to the entrypoint 'workdir-manager' of the versioncontrol service)
OptionConfig
    defines that configuration options
EventsConfig
    defines named events a plugin may fire,
    other plugin's may register callbacks
ActionsConfig
    defines toolbar actions and keyboard shortcuts


The changes
------------
* Plugins/Services are real packages now
* pida.core.plugins is gone (nobody understood that, nobody could fix it)

  Most of its use is implemented by pida.core.base.SubscriberConfig

* various weird constants are gone, type instances are used instead


**to be continued**
