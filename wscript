#! /usr/bin/env python
# encoding: utf-8

import os

VERSION = '2.0.7'

def options(opt):

    import waflib.extras.wurf_dependency_bundle as bundle
    import waflib.extras.wurf_dependency_resolve as resolve
    import waflib.extras.wurf_configure_output

    bundle.add_dependency(opt,
        resolve.ResolveGitMajorVersion(
            name='waf-tools',
            git_repository = 'git://github.com/steinwurf/external-waf-tools.git',
            major_version = 2))

    opt.load("wurf_dependency_bundle")
    opt.load('wurf_tools')


def configure(conf):

    if conf.is_toplevel():
        conf.load("wurf_dependency_bundle")
        conf.load("wurf_tools")
        conf.load_external_tool('mkspec', 'wurf_cxx_mkspec_tool')
        conf.load_external_tool('runners', 'wurf_runner')
        conf.load_external_tool('install_path', 'wurf_install_path')

    if conf.is_mkspec_platform('linux'):

        if not conf.env['LIB_PTHREAD']:

            # If we have not looked for pthread yet
            conf.check_cxx(lib = 'pthread')

    if conf.is_mkspec_platform('android'):
        conf.env.DEFINES += ['GTEST_OS_LINUX_ANDROID=1']


def build(bld):

    use_flags = []

    if bld.is_mkspec_platform('linux'):
        ext_paths = ['/usr/lib/i386-linux-gnu', '/usr/lib/x86_64-linux-gnu']

        # Check which targets have already been defined
        try:
            bld.get_tgen_by_name('pthread')
        except:
            bld.read_shlib('pthread', paths = ext_paths)

        use_flags += ['pthread']

    # Remove this when msvc supports variadic templates
    if bld.is_mkspec_platform('windows'):
        bld.env['DEFINES_GTEST_SHARED'] = ['GTEST_HAS_TR1_TUPLE=0']

    use_flags += ['GTEST_SHARED']

    bld.stlib(features = 'cxx',
              source   = ['gtest/src/gtest-all.cc'],
              target   = 'gtest',
              includes = ['gtest/include', 'gtest'],
              export_includes = ['gtest/include'],
              use = use_flags)




