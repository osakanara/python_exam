# coding: UTF-8

from except_noise import except_noise
from analytic import morphological_analysis


except_noise(
    before_text_path='ningen_shikkaku.txt',
    before_moji_code='Shift-JIS',
    after_text_path='after.txt'
)

morphological_analysis(
    file_path='after.txt',
    fontpath='/system/library/Fonts/ヒラギノ明朝 ProN.ttc',
    output_file_path='sample.png'
)

