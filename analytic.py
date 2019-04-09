from janome.tokenizer import Tokenizer
from wordcloud import WordCloud
from os import path

'''
形態素解析を行い、画像として出力する
file_path:対象ファイルパス
fontpath:表示するときのフォントの保存場所
'''


def morphological_analysis(file_path, fontpath):
    try:
        with open(file_path) as src:
            tokenizer = Tokenizer()

            # 形態素解析した文字列のリスト
            tokens = []

            for line in src:
                tokens += tokenizer.tokenize(line)

            # 品詞が名詞の単語だけを抽出したリストを作成
            nouns = [noun.base_form for noun in tokens if noun.part_of_speech.startswith('名詞')]

            # リストを文字列に変換
            text = ' '.join(nouns)

            try:
                wordcloud = WordCloud(background_color="white", font_path=fontpath, width=900, height=500).generate(text)
                # ファイルに書き出し
                wordcloud.to_file(path.join(path.dirname(__file__), 'sample.png'))
            except Exception as e:
                print(e.__str__())

    except Exception as e:
        print(e.__str__())
