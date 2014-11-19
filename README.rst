About
=====

We use Google C++ Testing Framework to test most of our libraries.

We use Waf to cross-compile gtest for the different platforms that
we support. We provide the Waf and wscript files needed to build the gtest library.

.. image:: http://buildbot.steinwurf.dk/svgstatus?project=gtest
    :target: http://buildbot.steinwurf.dk/stats?projects=gtest

Dependencies
------------

1. Git: A usable git client installed (see the "Set Up Git" guide at 
   the `github help`_ pages)
2. Python: To use Waf you need to install python version 2.7 and up should
   be fine. 
3. C++ compiler: To build the Boost libraries you need C++ compiler. We have tested with gcc 4.6 (Linux) and Visual Studio 2012 Express (Windows) 

.. _github help: http://help.github.com/

Use
---

Download the source from github by cloning the repository.
Issue this command in your terminal::
  
    git clone git://github.com/steinwurf/external-gtest.git

To build the libraries for your host platform:: 

    cd external-gtest
    python waf configure
    python waf build
