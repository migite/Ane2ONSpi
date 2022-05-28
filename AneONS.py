#姉しよONSコンバータ(Qtの覚書き)http://zero975.cocolog-nifty.com/qt_blog/2007/01/post_a3fc.html
#Rubyで書かれたコンバータをPythonに移植しています
import chardet
import glob
import sys
import os
import re

scenario_dir = os.path.join(same_hierarchy,'txt','txt')
se_dir = os.path.join(same_hierarchy,'SE')

stand_dir = os.path.join(same_hierarchy,'','stand')
other_dir = os.path.join(same_hierarchy,'Chip','other')
parts_dir = os.path.join(same_hierarchy,'grp','parts')
gebg_dir = os.path.join(same_hierarchy,'grp','gebg')
evcg_dir = os.path.join(same_hierarchy,'grp','evcg')


pathlist = glob.glob(os.path.join(scenario_dir, 'Data', '*.txt'))
pathlist.extend(glob.glob(os.path.join(scenario_dir, '*.txt')))

for snr_path in pathlist:

    for line in f:
    

        #ボイス命令の変換です

        Kuya_line =re.match(r'空也　（[０-９]）',line)
        Kaname_line =re.match(r'要芽　（[０-９]）',line)
        Serori_line =re.match(r'瀬芦里 （[０-９]）',line)
        Hinano_line =re.match(r'雛乃　（[０-９]）',line)


        if re.search('^\n', line):
            pass

        elif Kaname_line:

            line = line.replace('（[０-９]）',[0-9])
            line = 'dwave 0 "CV00\\' + kaname_line[1] + '.ogg"\n'

        elif Serori_line:

            line = line.replace('（[０-９]）',[0-9])
            line = 'dwave 0 "CV01\\' + Serori_line[1] + '.ogg"\n'

        elif Hinano_line:
        
            line = line.replace('（[０-９]）',[0-9])


