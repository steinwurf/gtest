#! /usr/bin/env python
# encoding: utf-8

APPNAME = 'gtest'
VERSION = '2.2.0'


def options(opt):

    import waflib.extras.wurf_dependency_bundle as bundle
    import waflib.extras.wurf_dependency_resolve as resolve

    bundle.add_dependency(opt, resolve.ResolveGitMajorVersion(
        name='waf-tools',
        git_repository='github.com/steinwurf/waf-tools.git',
        major_version=2))

    opt.load('wurf_configure_output')
    opt.load("wurf_dependency_bundle")
    opt.load('wurf_tools')


def configure(conf):

    if conf.is_toplevel():
        conf.load("wurf_dependency_bundle")
        conf.load("wurf_tools")

        conf.load_external_tool('mkspec', 'wurf_cxx_mkspec_tool')
        conf.load_external_tool('runners', 'wurf_runner')
        conf.load_external_tool('install_path', 'wurf_install_path')
        conf.load_external_tool('project_gen', 'wurf_project_generator')

    if conf.is_mkspec_platform('linux'):
        if not conf.env['LIB_PTHREAD']:
            # If we have not looked for pthread yet
            conf.check_cxx(lib='pthread')


def build(bld):

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
        export_includes=['gtest/include', 'src'],
        export_defines=['{}_VERSION="{}"'.format(APPNAME.upper(), VERSION)],
        use=use_flags)

    if bld.is_toplevel():
        bld.recurse('test')
