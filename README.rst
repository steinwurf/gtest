About
=====

We use Google C++ Testing Framework to test most of our libraries.

We use Waf to cross-compile gtest for the different platforms
we support. For that reason we provide the Waf and wscript files
needed to build the gtest library.

Dependencies
------------

1. Git: A usable git client installed (see the "Set Up Git" guide at 
   the `github help`_ pages)
2. Python: To use Waf you need to install python version 2.7 and up should
   be fine. 
3. C++ compiler: To build the Boost libraries you need C++ compiler we have 
   tested with gcc4.4.5 (Linux) and Visual Studio 10.0 Express (Windows) 

.. _github help: http://help.github.com/

Use
---

Download the source from github by cloning the repository. To do this run
from your terminal (Linux) or  your git bash terminal (Windows)::
  
    git clone git@github.com:steinwurf/external-gtest.git

To build the libraries for your host platform:: 

    cd external-gtest
    ./waf configure
    ./waf build

or equivalently on Windows (depending on how and where you have installed Python)::

    c:\Python27\python.exe waf configure   
    c:\Python27\python.exe waf build


Cross-compile
-------------

Currently it is possible to cross-compile for Android when using Linux. Use 
the toolchain options to cross-compile, see::

    ./waf -h

For more information. 
