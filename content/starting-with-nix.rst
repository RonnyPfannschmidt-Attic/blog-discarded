=================
Starting with Nix
=================

:date: 2015-02-03
:category: ops
:status: draft

.. contents::
    :backlinks: top

Intro
------

Nix_ is a functional package manager which allows
to easily create reproducible environments.

Is is the base for NixOs_ and uses the Nix_ language
to declare packages.

However in my oppinion the documentation is unclear about going
from examples to nice and well defined packages.

.. _NixOs: https://nixos.org/
.. _Nix: https://nixos.org/nix


A basic naive well-defined package
----------------------------------

In the practical sense a nix package is a **function** that
takes its **dependencies** as an argument and
returns a **specification** for constructing the actual package
based on those arguments.

This style of declaration makes it very easy to replace dependensics
and build special variants of packages or to override dependencies.

A basic naive example would be:

.. code:: nix

    {stdenv, fetchurl, openssl, makeWrapper, bzip2, patchelf}:
    stdenv.mkDerivation {
        name = "pypy-bin";
        installPhase = ''
            . $stdenv/setup
            cp -r . $out
            wrapProgram $out/bin/pypy \
                --suffix LD_LIBRARY_PATH : "${openssl}/lib" \
                --suffix LD_LIBRARY_PATH : "${bzip2}/lib"
        '';
        dontStrip = true;
        src = fetchurl {
            url = http://buildbot.pypy.org/nightly/trunk/pypy-c-nojit-75590-9e7b2bbd471c-linux64.tar.bz2;
            md5 = "fa63ab587fb58e81a9963271962ffa19";
        };

        buildInputs = [openssl makeWrapper bzip2 patchelf];
    }


This Package is just barely building a pypy-bin build
that works on a 64 bit linux.
it serves as starting point to demonstrate
going from something barely working to something more general.


Using and Building a Package
----------------------------

To build/use that package,
there is need for a surrounding system definition


.. code:: nix

    with import <nixpkgs> {};

    rec {
        pypy = import ./pypy.nix {
            inherit stdenv fetchurl bzip2 openssl makeWrapper patchelf;
        };

        pypy_libre = import ./pypy.nix {
            openssl = libressl;
            inherit stdenv fetchurl bzip2 makeWrapper patchelf;
        };
    }


In my experimentation i stored the definition
for the pypy package in `pypy.nix`
and the surounding system definition in pypy-build.nix

For experientation i created 2 variants,
one using openssl, one overriding openssl with libressl.
After using `nix-build pypy-build.nix` a number of folders
linking the results is availiable.


Handling More variants
-----------------------

