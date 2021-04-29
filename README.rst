About
=====

.. image:: https://travis-ci.org/steinwurf/gtest.svg?branch=master
    :target: https://travis-ci.org/steinwurf/gtest
    
We use the Google C++ Testing Framework to test most of our libraries.

We use Waf to compile gtest for various platforms. We provide the Waf and
wscript files needed to build the gtest library.

Dependencies
------------

1. Git: A usable git client installed (see the "Set Up Git" guide at
   the `github help`_ pages)
2. Python: To use Waf you need to install Python (2.7 or newer).
3. C++14 compiler: This can be g++, clang or msvc.

.. _github help: http://help.github.com/

Usage
-----

Clone this repository to a suitable folder::

Download the source from github by cloning the repository.
Issue this command in your terminal::
  
    git clone git://github.com/steinwurf/gtest.git

Configure and build the project::

    cd gtest
    python waf configure
    python waf build

Run the unit tests::

    python waf --run_tests
