About
=====

We use Google C++ Testing Framework to test most of our libraries.

We use Waf to cross-compile boost for the different platforms
we support. For that reason we provide the waf and wscript files
needed to build the gtest library.

Use
---


Run:: 

    ./waf configure build

Use the toolchain options to cross-compile, see::

    ./waf -h

For more information. 

