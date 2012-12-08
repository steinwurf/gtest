News for external-gtest
=======================

This file lists the major changes between versions. For a more detailed list
of every change, see the Git log.

master
------
* tbd

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


