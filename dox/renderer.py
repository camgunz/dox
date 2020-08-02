import os.path

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments.util import ClassNotFound as LexerNotFound

import commonmark

class Renderer:
    def __init__(self, folders, resources):
        self.folders = folders
        self.resources = resources
        self.parser = commonmark.Parser()
        self.formatter = HtmlFormatter(linenos=False, cssclass='source')
        self.renderer = commonmark.HtmlRenderer()
        self.renderer.escape = lambda s, preserve_entities=None: s

    def highlight_codeblocks(self, ast):
        for node, start in ast.walker():
            if not (start and node.t == 'code_block' and node.literal):
                continue
            try:
                lexer = get_lexer_by_name(node.info)
            except LexerNotFound:
                print(f'No lexer for language "{node.info}"')
                continue
            node.literal = highlight(node.literal, lexer, self.formatter)

    def render(self, markdown_source):
        ast = self.parser.parse(markdown_source)
        self.highlight_codeblocks(ast)
        return self.renderer.render(ast)

    def render_file(self, src_file):
        src_file_path = os.path.join(self.folders.src_dir, src_file)
        dst_file_path = os.path.join(
            self.folders.doc_dir,
            '.'.join((src_file[:-3], 'html'))
        )
        print('Rendering {}'.format(src_file_path))
        with open(dst_file_path, 'w', encoding='utf-8') as out_fobj:
            out_fobj.write(self.resources.header)
            with open(src_file_path, 'r', encoding='utf-8') as in_fobj:
                out_fobj.write(self.render(in_fobj.read()))
            out_fobj.write(self.resources.footer)

    def render_all(self):
        list(map(self.render_file, filter(
            lambda sf: sf.endswith('.md'),
            os.listdir(self.folders.src_dir)
        )))
