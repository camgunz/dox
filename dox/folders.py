import os
import shutil

class Folders:
    def __init__(self, base_dir):
        self.base_dir = os.path.abspath(os.path.expanduser(base_dir))
        self.src_dir = os.path.join(self.base_dir, 'src')
        self.res_dir = os.path.join(self.base_dir, 'res')
        self.doc_dir = os.path.join(self.base_dir, 'doc')
        self.img_src = os.path.join(self.res_dir, 'img')
        self.style_src = os.path.join(self.res_dir, 'styles')
        self.font_src = os.path.join(self.res_dir, 'fonts')
        self.img_dest = os.path.join(self.doc_dir, 'img')
        self.style_dest = os.path.join(self.doc_dir, 'styles')
        self.font_dest = os.path.join(self.doc_dir, 'fonts')
        self.header_file = os.path.join(self.res_dir, 'header.html')
        self.footer_file = os.path.join(self.res_dir, 'footer.html')

    def clear_doc_dir(self):
        if os.path.isdir(self.doc_dir):
            shutil.rmtree(self.doc_dir)

    def create_all(self):
        os.mkdir(self.doc_dir)
        os.mkdir(self.img_dest)
        os.mkdir(self.style_dest)
        os.mkdir(self.font_dest)
