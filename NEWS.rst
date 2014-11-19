News for external-gtest
=======================

This file lists the major changes between versions. For a more detailed list
of every change, see the Git log.

Latest
------
* Minor: Update to gtest 1.7.0
* Minor: Update to waf 1.8.0-pre1
* Minor: Made python files comply with pep8

2.1.3
-----
* Bugfix: Simplify pthread shared library usage on Linux

2.1.2
-----
* Bugfix: Allow compilation without using a makespec

2.1.1
-----
* Bugfix: Compile gtest without pthread support for crosslinux builds to avoid
  compatibility issues with the system pthread library

2.1.0
-----
* Minor: Updated to waf-tools 2
* Minor: Updated to waf 1.7.10
* Bugfix: Replaced _NSGetEnviron() call on Mac and iOS with POSIX 'environ' variable

2.0.7
-----
* Bugfix: Always include std::tuple from <tuple> in order to compile
  with clang's C++ library.
* Minor: Removed all binary files

2.0.6
-----
* Updated waf to include bundle_use_master option, and fixed an issue present
  only without full c++11 support.
* Updated to waf 1.7.9 and started using the wurf_install_path tool.

2.0.5
-----
* Added check on whether the pthread target already exists before doing
  issuing a read_shlib. This removes a waf warning about multiple defines for
  the pthread library.

2.0.4
-----
* Removed unnecessary use of get_mkspec_option
* Support waf unit test options to make handling different projects
  easier in build automation.

2.0.3
-----
* Updated waf

2.0.2
-----
* Updated waf

2.0.1
-----
* Updated platform information in mkspec

2.0.0
-----
* Switched to new mkspec based builds

1.0.4
-----
* Added defines needed for clang
* Updated waf to support clang cxx flags

1.0.3
-----
* Updated Waf build tool


