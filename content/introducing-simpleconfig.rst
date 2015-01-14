introducing simpleconfig
========================

:date: 2008-04-22
:tags: python, pida


<p>
  After some analysis of the current usage of ConfigObj 
  and our needs on configuration/project files in PIDA 
  i decided ConfigObj won't meet our needs and the same goes for ConfigParser.
</p>

<p>
  So i started a new lib with some unique features.
  <ul>
    <li>Inheritance</li>
    <li>
      merging/unmerging of config data <br />
      (this is the basis for inheritance and <br />
       keeping duplicate/default data out of config files)</li>
    <li>Simple alteration of section handling</li>
    <li>simlicity</li>
  </ul>
</p>

<h4>How does it look</h4>
<p>
 Here is a example based on the future project files for pida
</p>
<pre>
#inherit = make, make-test, execute, doxygen

[controller: execute]
executable = my_tool
</pre>  
<h5>Desription:</h5>
<dl>
  <dt><strong>#inherit</strong></dt>
  <dd>handles loading default data and merging it into the project config</dd>

  <dt><strong>[controller: execute]</strong></dt>
  <dd>
    creates the local section ('controller', 'execute'), 
    will be merged to the inherited one
  </dd>
  <dt><strong>executable = my_tool</strong></dt>
  <dd>prepare the value named executable in the controller execute to be replaced by my_tool</dd>
</dl>
<h4>Drawbacks</h4>
<ul>
  <li>the files wont be self-documenting</li>
  <li>its yet another lib</li>
</ul>
<h4>Benefits</h4>
<ul>
  <li>it does what we need the "right" way for us</li>
  <li>it will do exactly and only what its supposed to</li>
</ul>
<h4>Fazit</h4>
<p>
  I think is a good thing to get simpleconfig,
  anyone who doesn't, prove me wrong :), <br />
  however keep in mind that none of the common lib 
  is useful at the stuff i have in mind
</p>

<p>
  <strong>*update*</strong>
  <a href="http://ronny.uberhost.de/hg/simpleconfig/">development hg repo</a>
  - keep in mind its still really new
</p>