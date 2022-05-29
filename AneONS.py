#姉しよONSコンバータ(Qtの覚書き)http://zero975.cocolog-nifty.com/qt_blog/2007/01/post_a3fc.html
#Rubyで書かれたコンバータをPythonに移植しています
import glob
import sys
import os
import re

same_hierarchy = (os.path.dirname(sys.argv[0]))

txt = f.read()

pathlist = glob.glob(os.path.join(scenario_dir, 'general', '*.snr'))

for snr_path in pathlist:

    for line in f:
    
        Comment_line =re.match(r'//',line)

        BGM_line =re.match(r'BG_BGM[0-9]',line)
        Stand_line =re.match(r'CG_KG[0-9]',line)
        CG_line = re.match(r'CG_HG[0-9]',line)
        Back_line = re.match(r'CG_BG[0-9]',line)
        
        #ボイス命令の変換です
        Kuya_line =re.match(r'空也　（[０-９]）',line)
        Kaname_line =re.match(r'要芽　（[０-９]）',line)
        Serori_line =re.match(r'瀬芦里　（[０-９]）',line)
        Tomoe_line =re.match(r'巴　（[０-９]）',line)
        Hinano_line =re.match(r'雛乃　（[０-９]）',line)
        Umi_line =re.match(r'海　（[０-９]）',line)


        if re.search('^\n', line):
            pass
        
        elif Comment_line:
            
            line = line.replace('//',';;\n')

        elif BGM_line:

            if re.match('BG_BGM[0-9]_STOP'):
            line = 'bgmstop'

            else: 
            line = line.replace('BG_BGM[0-9]','bgm[0-9]')
            line = 'bgm "BGM\\' + BGM_line[1] + '.ogg"\n'

        elif Stand_line:

            if re.match('_0$'):
            line = 

        #ここからボイス命令の変換

        elif Kaname_line:

            line = line.replace('要芽　（[０-９]）','[0-9]')
            line = '要芽\n dwave 0 "CV00\\' + Kaname_line[1] + '.ogg"\n'

        elif Serori_line:

            line = line.replace('瀬芦里　（[０-９]）','[0-9]')
            line = '瀬芦里\n dwave 0 "CV01\\' + Serori_line[1] + '.ogg"\n'

        elif Tomoe_line:
            
            line = line.replace('巴　（[０-９]）','[0-9]')
            line = '巴\n dwave 0 "CV02\\' + Tomoe_line[1] + '.ogg"\n'

        elif Hinano_line:
        
            line = line.replace('雛乃　（[０-９]）','[0-9]')
            line = '雛乃\n dwave 0 "CV03\\' + Hinano_line[1] + '.ogg"\n'

        elif Umi_line:
        
            line = line.replace('（[０-９]）',[0-9])
            line = '海\n dwave 0 "CV04\\' + Umi_line[1] + '.ogg"\n'


        txt += line


