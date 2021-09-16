import os
import shutil

class Resources:
    def __init__(self, folders):
        self.folders = folders
        with open(folders.header_file, 'r', encoding='utf-8') as fobj:
            self.header = fobj.read()
        with open(folders.footer_file, 'r', encoding='utf-8') as fobj:
            self.footer = fobj.read()

    def install(self):
        print('Installing images')
        for img_file in os.listdir(self.folders.img_src):
            image_path = os.path.join(self.folders.img_src, img_file)
            shutil.copy2(image_path, self.folders.img_dest)

        print('Installing stylesheets')
        for style_file in os.listdir(self.folders.style_src):
            style_path = os.path.join(self.folders.style_src, style_file)
            shutil.copy2(style_path, self.folders.style_dest)

        print('Installing fonts')
        for font_file in os.listdir(self.folders.font_src):
            font_path = os.path.join(self.folders.font_src, font_file)
            shutil.copy2(font_path, self.folders.font_dest)
