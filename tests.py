# coding: utf-8
"""
    test
    ~~~~

    :copyright: 2014 by Daniel Neuhäuser
    :license: BSD, see LICENSE.rst for details
"""
import os
import shutil

from sphinx.application import Sphinx

from pytest import yield_fixture, mark


TEST_DOCUMENTATION_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'testdocs'
)
TEST_DOCUMENTATION_BUILD_DIR = os.path.join(TEST_DOCUMENTATION_DIR, '_build')
TEST_DOCUMENTATION_OUT_DIR = os.path.join(TEST_DOCUMENTATION_BUILD_DIR, 'html')


@yield_fixture(scope='session')
def sphinx():
    shutil.rmtree(TEST_DOCUMENTATION_BUILD_DIR)
    os.mkdir(TEST_DOCUMENTATION_BUILD_DIR)
    app = Sphinx(
        srcdir=TEST_DOCUMENTATION_DIR,
        confdir=TEST_DOCUMENTATION_DIR,
        outdir=TEST_DOCUMENTATION_OUT_DIR,
        doctreedir=os.path.join(TEST_DOCUMENTATION_OUT_DIR, '.doctrees'),
        buildername='html',
        freshenv=True,
        warningiserror=True
    )
    app.build()
    yield


@mark.usefixtures('sphinx')
def test():
    content = open(os.path.join(TEST_DOCUMENTATION_OUT_DIR, 'index.html')).read()
    assert 'MACRO_DEFINITION' in content
    assert 'This describes the macro.' in content

    assert 'MACRO_FUNCTION' in content
    assert 'This described the function macro.'

    assert 'global' in content
    assert 'This is a globally declared integer.'

    assert 'function' in content
    assert 'This is a function.' in content

    assert 'a_struct' in content
    assert 'This describes a_struct.'
    assert 'spam' in content
    assert 'Describes spam.' in content
    assert 'eggs' in content
    assert 'Describes eggs.' in content
