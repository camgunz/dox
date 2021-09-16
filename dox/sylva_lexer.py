# -*- coding: utf-8 -*-
"""
    pygments.lexers.sy
    ~~~~~~~~~~~~~~~~~~~~

    Lexers for the Sylva language.

    :copyright: Copyright 2020 Charles Gunyon
    :license: BSD, see LICENSE for details.
"""

from pygments.lexer import RegexLexer, bygroups, words
from pygments.token import (
    Text, Comment, Operator, Keyword, Name, String, Number, Punctuation,
    Whitespace
)

__all__ = ['SylvaLexer']


NUM_REGEX = (
    r'[+-]?'
    r'('
    r'('
      r'(\d+)'
      r'(([iu])(8|16|32|64|128|256))'
      r'([cw])?'
    r')'
    r'|'
    r'('
      r'('
        r'(((\d+\.\d+)|(\d+\.)|(\.\d+))([Ee][+-]?\d+)?)|'
        r'(\d+[Ee][+-]?\d+)|'
        r'(\d+)'
      r')'
      r'(f(16|32|64|128|256))?'
      r'(ra|rd|ru|rz)?'
    r')'
    r')'
)

class SylvaLexer(RegexLexer):
    """
    Lexer for the Sylva programming language

    .. versionadded:: 2.0.2
    """
    name = 'Sylva'
    filenames = ['*.sy']
    aliases = ['sy', 'sylva']
    mimetypes = ['text/sy']

    tokens = {
        'root': [
            # Whitespace and Comments
            (r'( |\t)+', Whitespace),
            (r'(\r\n|\r|\n)', Whitespace),
            (r'#(.*)(\r\n|\r|\n)', Comment.Single),

            # Importing
            (r'(requirement)((?:\s|\\\s)+)', bygroups(Keyword.Namespace, Text)),

            # Keywords
            (r'(var)\b', Keyword.Declaration),
            (words((
                'alias', 'break', 'case', 'continue', 'default', 'else',
                'enum', 'exit', 'for', 'fn', 'fntype', 'if', 'implementation',
                'interface', 'loop', 'match', 'range', 'return', 'struct',
                'switch', 'while'
            ), suffix=r'\b'),
             Keyword),
            (r'module\b', Keyword.Namespace),
            (r'(true|false)\b', Keyword.Constant),
            (words((
                'bool',
                'rune',
                'num',
                'integer', 'int', 'i8', 'i16', 'i32', 'i64', 'i128', 'i256',
                'uint', 'u8', 'u16', 'u32', 'u64', 'u128', 'u256',
                'float', 'f16', 'f32', 'f64', 'f128', 'f256',
                'complex', 'c16', 'c32', 'c64', 'c128', 'c256',
                'dec',
                'str',
                'array',
                'struct',
                'variant',
                'fn',
                'fntype',
                'range',
                'enum',
                'cfn',
                'cfntype',
                'cptr',
                'cstr',
                'cstruct',
                'cunion',
                'cvoid'
            ), suffix=r'\b'),
             Keyword.Type),

            # Character Literal
            (r"""'(\\['"\\nrt]|\\x[0-7][0-9a-fA-F]|\\0"""
             r"""|\\u\{[0-9a-fA-F]{1,6}\}|.)'""",
             String.Char),

            # Numeric Literals
            (NUM_REGEX, Number.Integer),
            (NUM_REGEX, Number.Float),

            # Binary Integer Literal
            (r'0[bB][01_]+[iu](8|16|32|64|128|256)', Number.Bin),

            # Octal Integer Literal
            (r'0[oO][0-7_]+[iu](8|16|32|64|128|256)', Number.Oct),

            # Hexadecimal Integer Literal
            (r'0[xX][0-9a-fA-F_]+[iu](8|16|32|64|128|256)', Number.Hex),

            # String Literal
            (r'"(.*?)"', String),

            # Operators and Punctuation
            (r'[{}()\[\]:,.]', Punctuation),
            (r'[+\-*/%&|<>^!~=]', Operator),

            # Identifier
            (r'[\@]*\w+', Name),
        ],
        'string': [
            (r'"', String, '#pop'),
            (r"""\\['"\\nrt]|\\x[0-7][0-9a-fA-F]|\\0"""
             r"""|\\u\{[0-9a-fA-F]{1,6}\}""", String.Escape),
            (r'[^\\"]+', String),
            (r'\\', String),
        ],
    }
