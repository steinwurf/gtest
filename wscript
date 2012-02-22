#! /usr/bin/env python
# encoding: utf-8

import os

# Necessary since we override different Contexts 
import waflib.extras.wurftools as wt

def options(opt):
    opt.load('wurftools')

def configure(conf):

    conf.load('wurftools')

    if conf.env.TOOLCHAIN != 'android':
        conf.check_cxx(lib = 'pthread')

    if conf.env['TOOLCHAIN'] == 'android':
	    conf.env.DEFINES += ['GTEST_OS_LINUX_ANDROID=1']


def build(bld):

    if bld.env.TOOLCHAIN != 'android':

        ext_paths = ['/usr/lib/i386-linux-gnu', '/usr/lib/x86_64-linux-gnu']
        
        bld.read_shlib('pthread', paths = ext_paths)

    
    bld.stlib(features = 'cxx',
	      source   = ['gtest/src/gtest-all.cc'],
	      target   = 'gtest',
	      includes = ['gtest/include',
                          'gtest'],
              export_includes = ['gtest/include'],
              use = ['pthread'])
    


