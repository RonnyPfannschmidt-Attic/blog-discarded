====================================================
Briefly decomposing unittest bad practice
====================================================

:date: 2015-02-03
:category: python
:tags: history, short, rant


Decomposing unittest
=====================

History
-------

First there was SUnit
++++++++++++++++++++++

and it was good

* native sytnax
* no specific assertion methods
* use of language level introspection
* immense introspection cappabilities of the runtime

.. http://sdmeta.gforge.inria.fr/Programmez/OnTheWeb/Eng-Art8-SUnit-V1.pdf

:example:
  .. code:: smalltalk

    TestCase subclass: #ExampleSetTest
      instanceVariableNames: 'full empty'
      classVariableNames: ''
      poolDictionaries: ''
      category: 'SUnit-Tests'
    ExampleSetTest>>setUp
      empty := Set new.
      full := Set with: 5 with: #abc
    ExampleSetTest>>testIncludes
      self assert: (full includes: 5).
      self assert: (full includes: #abc)
    ExampleSetTest>>testOccurrences
      self assert: (empty occurrencesOf: 0) = 0.
      self assert: (full occurrencesOf: 5) = 1.
      full add: 5.
      self assert: (full occurrencesOf: 5) = 1
    ExampleSetTest>>testRemove
      full remove: 5.
      self assert: (full includes: #abc).
      self deny: (full includes: 5)
    ExampleSetTest>>testIllegal
      self should: [empty at: 5] raise: Error.
      self should: [empty at: 5 put: #abc] raise: Error

  .. http://www.xprogramming.com/testfram.htm

Then the Java people Transliterated it
+++++++++++++++++++++++++++++++++++++++
