#!/usr/bin/python3

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" Harnass for fuzzing python-markdown (https://github.com/Python-Markdown/markdown) """

import sys
import struct
import atheris
import markdown

def test_markdown_xhtml(inp):
    """ Testing markdown method with no extensions and xhtml output """
    try:
        markdown.markdown(inp, output_format='xhtml')
    except NotImplementedError:
        return

def test_markdown_html5(inp):
    """ Testing markdown method with no extensions and html5 output """
    try:
        markdown.markdown(inp, output_format='html5')
    except NotImplementedError:
        return

def test_markdown_extra(inp):
    """ Testing markdown method with Extra extension """
    try:
        markdown.markdown(inp, extensions=['extra'])
    except NotImplementedError:
        return

def test_markdown_abbr(inp):
    """ Testing markdown method with Abbreviations extension """
    try:
        markdown.markdown(inp, extensions=['abbr'])
    except NotImplementedError:
        return

def test_markdown_attr_list(inp):
    """ Testing markdown method with Attribute Lists extension """
    try:
        markdown.markdown(inp, extensions=['attr_list'])
    except NotImplementedError:
        return

def test_markdown_def_list(inp):
    """ Testing markdown method with Definition Lists extension """
    try:
        markdown.markdown(inp, extensions=['def_list'])
    except NotImplementedError:
        return

def test_markdown_fenced_code(inp):
    """ Testing markdown method with Fenced Code Blocks extension """
    try:
        markdown.markdown(inp, extensions=['fenced_code'])
    except NotImplementedError:
        return

def test_markdown_footnotes(inp):
    """ Testing markdown method with Footnotes extension """
    try:
        markdown.markdown(inp, extensions=['footnotes'])
    except NotImplementedError:
        return

def test_markdown_md_in_html(inp):
    """ Testing markdown method with Markdown in HTML extension """
    try:
        markdown.markdown(inp, extensions=['md_in_html'])
    except NotImplementedError:
        return

def test_markdown_tables(inp):
    """ Testing markdown method with Tables extension """
    try:
        markdown.markdown(inp, extensions=['tables'])
    except NotImplementedError:
        return

def test_markdown_admonition(inp):
    """ Testing markdown method with Admonition extension """
    try:
        markdown.markdown(inp, extensions=['admonition'])
    except NotImplementedError:
        return

def test_markdown_codehilite(inp):
    """ Testing markdown method with CodeHilite extension """
    try:
        markdown.markdown(inp, extensions=['codehilite'])
    except NotImplementedError:
        return

def test_markdown_legacy_attrs(inp):
    """ Testing markdown method with Legacy Attributes extension """
    try:
        markdown.markdown(inp, extensions=['legacy_attrs'])
    except NotImplementedError:
        return

def test_markdown_legacy_em(inp):
    """ Testing markdown method with Legacy Emphasis extension """
    try:
        markdown.markdown(inp, extensions=['legacy_em'])
    except NotImplementedError:
        return

def test_markdown_meta(inp):
    """ Testing markdown method with Meta-Data extension """
    try:
        markdown.markdown(inp, extensions=['meta'])
    except NotImplementedError:
        return

def test_markdown_nl2br(inp):
    """ Testing markdown method with New Line to Break extension """
    try:
        markdown.markdown(inp, extensions=['nl2br'])
    except NotImplementedError:
        return

def test_markdown_sane_lists(inp):
    """ Testing markdown method with Sane Lists extension """
    try:
        markdown.markdown(inp, extensions=['sane_lists'])
    except NotImplementedError:
        return

def test_markdown_smarty(inp):
    """ Testing markdown method with SmartyPants extension """
    try:
        markdown.markdown(inp, extensions=['smarty'])
    except NotImplementedError:
        return

def test_markdown_toc(inp):
    """ Testing markdown method with Table of Contents extension """
    try:
        markdown.markdown(inp, extensions=['toc'])
    except NotImplementedError:
        return

def test_markdown_wikilinks(inp):
    """ Testing markdown method with WikiLinks extension """
    try:
        markdown.markdown(inp, extensions=['wikilinks'])
    except NotImplementedError:
        return

def test_markdown_all_extensions(inp):
    """ Testing markdown method with all extensions """
    try:
        markdown.markdown(inp, extensions=['extra', 'abbr', 'attr_list', 'def_list', \
            'fenced_code', 'footnotes', 'md_in_html', 'tables', 'admonition', 'codehilite', \
            'legacy_attrs', 'legacy_em', 'meta', 'nl2br', 'sane_lists', 'smarty', 'toc', \
            'wikilinks'])
    except NotImplementedError:
        return

def inp_of_type(fdp, inp_type):
    """ Get input of the right type """
    if inp_type == str:
        return fdp.ConsumeUnicode(sys.maxsize)
    if inp_type == int:
        return fdp.ConsumeInt(sys.maxsize)
    if inp_type == float:
        return fdp.ConsumeFloat()
    return fdp.ConsumeBytes(sys.maxsize)

TESTS = [
    (test_markdown_xhtml, str),
    (test_markdown_html5, str),
    (test_markdown_extra, str),
    (test_markdown_abbr, str),
    (test_markdown_attr_list, str),
    (test_markdown_def_list, str),
    (test_markdown_fenced_code, str),
    (test_markdown_footnotes, str),
    (test_markdown_md_in_html, str),
    (test_markdown_tables, str),
    (test_markdown_admonition, str),
    (test_markdown_codehilite, str),
    (test_markdown_legacy_attrs, str),
    (test_markdown_legacy_em, str),
    (test_markdown_meta, str),
    (test_markdown_nl2br, str),
    (test_markdown_sane_lists, str),
    (test_markdown_smarty, str),
    (test_markdown_toc, str),
    (test_markdown_wikilinks, str),
    (test_markdown_all_extensions, str),
]

def test_one_input(input_bytes):
    """ Fuzzer's entry point """
    if len(input_bytes) < 1:
        return
    choice = struct.unpack('>B', input_bytes[:1])[0]
    if choice >= len(TESTS):
        return

    fdp = atheris.FuzzedDataProvider(input_bytes[1:])
    TESTS[choice][0](inp_of_type(fdp, TESTS[choice][1]))

def main():
    """ main function """
    atheris.Setup(sys.argv, test_one_input, enable_python_coverage=False)
    atheris.Fuzz()


if __name__ == "__main__":
    atheris.instrument_all()
    main()
