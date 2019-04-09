# coding: UTF-8

import re
import codecs

'''
文章内のノイズを取り除く
before_text_path:変換するファイルのパス
before_moji_code:変換するファイルの文字コード
after_text_path:変換後のファイルのパス（ファイル名）
'''


def except_noise(before_text_path, before_moji_code,  after_text_path):
    noise1 = '《[ぁ-んァ-ン]*》'
    noise2 = '※*［＃.*］'
    try:
        with codecs.open(before_text_path, 'r', before_moji_code, 'ignore') as src, \
                open(after_text_path, 'w') as after:
            for line in src:
                if re.search(noise1, line):
                    line = re.sub(noise1, '', line)
                if re.search(noise2, line):
                    line = re.sub(noise2, '', line)
                # 変換後ファイルに書き出す
                after.write(line)
    except OSError as oe:
        print(oe.strerror)
