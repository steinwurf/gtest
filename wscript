#! /usr/bin/env python
# encoding: utf-8

APPNAME = "gtest"
VERSION = "5.0.0"


def options(ctx):
    ctx.load("cmake")


def configure(ctx):

    ctx.load("cmake")


def build(ctx):

    ctx.load("cmake")


def clean(ctx):

    ctx.load("cmake")

    # Set the default clean paths
    ctx.clean_paths = ["build", "build_current"]
