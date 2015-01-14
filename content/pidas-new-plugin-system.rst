pida's new plugin system - draft
================================

:date: 2008-08-08
:tags: python, pida


<b>this is a draft, feel free to report anything that looks plain wrong</b>


For the upcoming pida release i did a larger refactoring
 which includes some nice changes in the api.

<h4>Basic Structure</h4>

There are 3 Kinds of loadable Entity
<dl>
<dt>Editors</dt>
<dd>Currently there is Vim, Emacs and medit, usually only one of them is loaded</dd>
<dt>Services</dt>
<dd>They define pida's core functionalities, all of them are always loaded<dd>
<dt>Plugins</dt>
<dd>They contain all optional components, they are reloadable and updatable.</dd>
</dl>


All of those are startable and stoppable. (services/editors get only stopped when exiting pida).


Also each of those may have one or more of the following:
<dl>
<dt>Featuresconfig</dt>
<dd>defines feature entry points of the plugin, registers features to the entry points (for example vcs integration is done by registering anyvc vcs's to the entrypoint 'workdir-manager' of the versioncontrol service)</dd>
<dt>OptionConfig</dt>
<dd>defines that configuration options</dd>
<dt>EventsConfig<dt>
<dd>defines named events a plugin may fire, other plugin's may register callbacks</dd>
<dt>ActionsConfig</dt>
<dd>defines toolbar actions and keyboard shortcuts</dd>

</dl>

<h4>The changes</h4>
<ul>
<li> Plugins/Services are real packages now
<li> pida.core.plugins is gone (nobody understood that, nobody could fix it)
  <p>
    Most of its use is implemented by pida.core.base.SubscriberConfig
  </p>

<li> various weird constants are gone, type instances are used instead
</ul>


<b>to be continued</b>