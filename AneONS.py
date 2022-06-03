#姉しよONSコンバータ(Qtの覚書き)http://zero975.cocolog-nifty.com/qt_blog/2007/01/post_a3fc.html
#Rubyで書かれたコンバータをPythonに移植しています
import glob
import sys
import os
import re
import unicodedata

for (未定義0) in (未定義1):

    for line in (未定義2):
    
        Comment_line =re.match(r'//',line)

        BGM_line = re.match(r'BG_BGM[0-9]',line)
        Stand_line = re.match(r'CG_KG[0-9]',line)
        CG_line = re.match(r'CG_HG[0-9]',line)
        Back_line = re.match(r'CG_BG[0-9]',line)
        Jump_line = re.match(r'/*/*/*SC',line)
        Rabel_line = re.match(r'/*/*/*SS',line)
        
        #ボイス命令の変換です
        Voice_line =re.match(r'空也||要芽||瀬芦里||巴||雛乃||海||高嶺||いるか||透子||女の子||お嬢様Ａ||お嬢様Ｂ||女子学生Ａ||女子学生Ｂ||女子学生Ｃ　（[０-９]）',line)


        if re.search('^\n', line):
            pass
        
        #コメントアウト命令の変換
        elif Comment_line:
            
            line = line.replace('//',';;\n')

        #BGMの変換
        elif BGM_line:
        
        #STOP命令を捕捉した場合、BGMを止めます
            if re.match('BG_BGM[0-9]_STOP'):
                line = 'bgmstop'
        #STOP命令がなかった場合、BGM再生を行います
            else: 
                line.replace('BG_BGM','BGM')
                line = 'bgm "BGM\\' + BGM_line[1] + '.ogg"\n'
        #CG表示の変換です。
        elif CG_line:

            line.replace('CG_HG','HG')
            line = 'bg "CG\\' + CG_line[1] + '.png",3\n'

        #背景命令の変換です。現時点でCG命令と見かけ上同じですが、後から機能を追加するために分けています。
        elif Back_line:

            line.replace('CG_BG','BG')
            line = 'bg "CG\\' + Back_line[1] + '.png,3\n'
       
        #ここからボイス命令の変換
        elif Voice_line:

            #Unicodedataプラグインを用いて全角数字を半角に変換します
            unicodedata.normalize("NFKC", line)

            #どうしても()が残ってしまうのでrepalceして消します。いい方法あったら教えて。
            line.replace('(','').replace(')','')
           
           #主人公はボイスが無いので、発言主部分だけ残して返します。
            if re.match('空也',line):

                line = '空也\n'
            
            elif re.match('要芽',line):
                
            #発言主表示とボイス命令を切り分けるため、行を数字4桁だけにします。以下CV13女子学生Ｃまでおなじです
                line.replace('要芽　','')

                line = '要芽\n dwave 0 "CV00\\' + Voice_line[1] + '.ogg"\n'

            elif re.match('瀬芦里',line):

                line.replace('瀬芦里　','')

                line = '瀬芦里\n dwave 0 "CV01\\' + Voice_line[1] + '.ogg"\n'

            elif re.match('巴',line):

                line.replace('巴　','')

                line = '巴\n dwave 0 "CV02\\' + Voice_line[1] + '.ogg"\n'

            elif re.match('雛乃',line):

                line.replace('雛乃','')

                line = '雛乃\n dwave 0 "CV03\\' + Voice_line[1] + '.ogg"\n'

            elif re.match('海',line):

                line.replace('海','')

                line = '海\n dwave 0 "CV04\\' + Voice_line[1] + '.ogg"\n'

            elif re.match('高嶺',line):

                line = '高嶺\n dwave 0 "CV05\\' + Voice_line[1] + '.ogg"\n'

            elif re.match('いるか',line):

                line.replace('いるか　','')
                line = 'いるか\n dwave 0 "CV06\\' + Voice_line[1] + '.ogg"\n'

            elif re.match('お嬢様A',line):
                
                line.replace('お嬢様A','')
                line = 'お嬢様Ａ\n dwave 0 "CV09\\' + Voice_line[1] + '.ogg"\n'

            elif re.match('お嬢様B',line):

                line.replace('お嬢様B','')
                line = 'お嬢様Ｂ\n dwave 0 "CV10\\' + Voice_line[1] + '.ogg"\n'

            elif re.match('女子学生A',line):

                line.replace('女子学生A','')
                line = '女子学生Ａ\n dwave 0 "CV11\\' + Voice_line[1] + '.ogg"\n'
            
            elif re.match('女子学生B',line):

                line.replace('女子学生B','')
                line = '女子学生Ｂ\n dwave 0 "CV12\\' + Voice_line[1] + '.ogg"\n'

            elif re.match('女子学生C',line):

                line.replace('女子学生C','')
                line = '女子学生Ｃ\n dwave 0 "CV13\\' + Voice_line[1] + '.ogg"\n'

        elif Jump_line:
            
            line


            



