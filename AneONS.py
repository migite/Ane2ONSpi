#姉しよONSコンバータ(Qtの覚書き)http://zero975.cocolog-nifty.com/qt_blog/2007/01/post_a3fc.html
#Rubyで書かれたコンバータをPythonに移植しています

from PIL import Image
import chardet
import glob
import sys
import os
import re


with open(os.path.join(same_hierarchy, '0.txt')) as f:
	txt = f.read()


for line in f:
    #変換の場合分けです
    Kuya_line =re.match(r'空也\[０-９]',line)