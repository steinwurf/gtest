#! /usr/bin/env python
# encoding: utf-8

APPNAME = 'gtest'
VERSION = '2.3.1'


def options(opt):

    opt.load('wurf_common_tools')


def configure(conf):

    import waflib.extras.wurf_dependency_bundle as bundle
    import waflib.extras.wurf_dependency_resolve as resolve

    # waf-tools must be the first dependency
    bundle.add_dependency(conf, resolve.ResolveGitMajorVersion(
        name='waf-tools',
        git_repository='github.com/steinwurf/waf-tools.git',
        major_version=2))

    if conf.is_toplevel():

        # Download and recurse all dependencies
        conf.load("wurf_common_tools")


    if conf.is_mkspec_platform('linux'):
        if not conf.env['LIB_PTHREAD']:
            # If we have not looked for pthread yet
            conf.check_cxx(lib='pthread')


def build(bld):

    bld.env.append_unique(
        'DEFINES_STEINWURF_VERSION',
        'STEINWURF_GTEST_VERSION="{}"'.format(VERSION))

    use_flags = ['GTEST_SHARED']

    if bld.is_mkspec_platform('linux'):
        use_flags += ['PTHREAD']

    # Remove this when msvc supports variadic templates
    if bld.is_mkspec_platform('windows'):
        bld.env['DEFINES_GTEST_SHARED'] += ['GTEST_HAS_TR1_TUPLE=0']

    if bld.is_mkspec_platform('android'):
        bld.env['DEFINES_GTEST_SHARED'] += ['GTEST_OS_LINUX_ANDROID=1']

    bld.stlib(
        features='cxx',
        source=['gtest/src/gtest-all.cc'],
        target='gtest',
        includes=['gtest/include', 'gtest'],
        export_includes=['gtest/include'],
        use=use_flags)

    if bld.is_toplevel():

        bld.load("wurf_common_tools")

        bld.recurse('test')

