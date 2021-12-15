About
=====

|Linux make-specs| |Windows make-specs| |MacOS make-specs| |Linux CMake| |Windows CMake| |MacOS CMake| |Valgrind| |No Assertions| |Clang Format| |Cppcheck|

.. |Linux make-specs| image:: https://github.com/steinwurf/abacus/actions/workflows/linux_mkspecs.yml/badge.svg
   :target: https://github.com/steinwurf/abacus/actions/workflows/linux_mkspecs.yml
   
.. |Windows make-specs| image:: https://github.com/steinwurf/abacus/actions/workflows/windows_mkspecs.yml/badge.svg
   :target: https://github.com/steinwurf/abacus/actions/workflows/windows_mkspecs.yml

.. |MacOS make-specs| image:: https://github.com/steinwurf/abacus/actions/workflows/macos_mkspecs.yml/badge.svg
   :target: https://github.com/steinwurf/abacus/actions/workflows/macos_mkspecs.yml
   
.. |Linux CMake| image:: https://github.com/steinwurf/abacus/actions/workflows/linux_cmake.yml/badge.svg
   :target: https://github.com/steinwurf/abacus/actions/workflows/linux_cmake.yml

.. |Windows CMake| image:: https://github.com/steinwurf/abacus/actions/workflows/windows_cmake.yml/badge.svg
   :target: https://github.com/steinwurf/abacus/actions/workflows/windows_cmake.yml
   
.. |MacOS CMake| image:: https://github.com/steinwurf/abacus/actions/workflows/macos_cmake.yml/badge.svg
   :target: https://github.com/steinwurf/abacus/actions/workflows/macos_cmake.yml

.. |Clang Format| image:: https://github.com/steinwurf/abacus/actions/workflows/clang-format.yml/badge.svg
   :target: https://github.com/steinwurf/abacus/actions/workflows/clang-format.yml

.. |No Assertions| image:: https://github.com/steinwurf/abacus/actions/workflows/nodebug.yml/badge.svg
   :target: https://github.com/steinwurf/abacus/actions/workflows/nodebug.yml

.. |Valgrind| image:: https://github.com/steinwurf/abacus/actions/workflows/valgrind.yml/badge.svg
   :target: https://github.com/steinwurf/abacus/actions/workflows/valgrind.yml

.. |Cppcheck| image:: https://github.com/steinwurf/abacus/actions/workflows/cppcheck.yml/badge.svg
   :target: https://github.com/steinwurf/abacus/actions/workflows/cppcheck.yml
    
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
