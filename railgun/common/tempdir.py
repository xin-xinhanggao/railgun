#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @file: railgun/common/tempdir.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Contributors:
#   public@korepwx.com   <public@korepwx.com>
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This file is released under BSD 2-clause license.

import os
import uuid
import config
import shutil

from .fileutil import remove_firstdir


class TempDir(object):

    def __init__(self, name=None):
        self.name = name if name else uuid.uuid4().get_hex()
        self.path = os.path.join(config.TEMPORARY_DIR, self.name)

    def open(self, mode=0700):
        """Create target directory"""
        if (not os.path.isdir(self.path)):
            os.makedirs(self.path, mode)

    def close(self):
        """Delete target directory"""
        if (os.path.isdir(self.path)):
            shutil.rmtree(self.path)

    def fullpath(self, subpath):
        """Get the fullpath for `subpath`"""
        return os.path.join(self.path, subpath)

    def copyfiles(self, srcdir, filelist):
        """Copy `filelist` in `srcdir` into this directory."""

        for f in filelist:
            srcpath = os.path.join(srcdir, f)
            dstpath = os.path.join(self.path, f)

            if (not os.path.isdir(srcpath)):
                parent_path = os.path.dirname(dstpath)
                if (not os.path.isdir(parent_path)):
                    os.makedirs(parent_path, 0700)
                shutil.copyfile(srcpath, dstpath)

    def extract(self, extractor, should_skip=None):
        """Extract all files in `extractor` into this directory.

        should_skip: None or callable `path` -> bool. If it returns True for
        given `path`, such files will be ignored.
        """
        # check the arguments
        should_skip = should_skip or (lambda p: False)
        canonical_path = remove_firstdir \
            if extractor.onedir() else (lambda p: p)

        for fname, fobj in extractor.extract():
            fpath = canonical_path(fname)
            dstpath = os.path.join(self.path, fpath)

            # check whether the file should skip
            if (should_skip(fpath)):
                continue

            # create the parent directory if not exist
            parent_path = os.path.dirname(dstpath)
            if (not os.path.isdir(parent_path)):
                os.makedirs(parent_path, 0700)

            with open(dstpath, 'wb') as f:
                f.write(fobj.read())
            os.chmod(dstpath, 0700)

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, ignore1, ignore2, ignore3):
        self.close()