#! /usr/bin/env python
# encoding: utf-8

import os

VERSION = '2.0.3'

def options(opt):

    opt.load("dependency_bundle")

    import waflib.extras.dependency_bundle as bundle
    import waflib.extras.dependency_resolve as resolve

    bundle.add_dependency(opt,
        resolve.ResolveGitMajorVersion(
            name='mkspec',
            git_repository = 'git://github.com/steinwurf/external-waf-mkspec.git',
            major_version = 2))

    opt.load('wurf_cxx_mkspec')


def configure(conf):

    if conf.is_toplevel():
        conf.load("dependency_bundle")
        conf.load("wurf_cxx_mkspec")

    if conf.is_mkspec_platform('linux'):

        if not conf.env['LIB_PTHREAD']:

            # If we have not looked for pthread yet
            conf.check_cxx(lib = 'pthread')

    if conf.is_mkspec_platform('android'):
        conf.env.DEFINES += ['GTEST_OS_LINUX_ANDROID=1']


def build(bld):

    use_flags = []

    platform = bld.get_mkspec_platform()

    if bld.is_mkspec_platform('linux'):
        ext_paths = ['/usr/lib/i386-linux-gnu', '/usr/lib/x86_64-linux-gnu']

        bld.read_shlib('pthread', paths = ext_paths)
        use_flags += ['pthread']

    # Change this when we hit c++11
    bld.env['DEFINES_GTEST_SHARED'] = ['GTEST_HAS_TR1_TUPLE=0']

    use_flags += ['GTEST_SHARED']

    bld.stlib(features = 'cxx',
	      source   = ['gtest/src/gtest-all.cc'],
	      target   = 'gtest',
	      includes = ['gtest/include', 'gtest'],
              export_includes = ['gtest/include'],
              use = use_flags)



