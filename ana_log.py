# 処理概要
# ・時刻から処理時間を差分で計測する
# ・カラムごとに値を拾う

# 対象：apache_log_sample.log

import datetime

# 変数の初期化
past_divlist = []
file = 'apache_log_sample.log'


def main():
    global file
    read_log(file)

def read_log(file):
    global past_divlist
    with open(file) as file:
        for line in file:
            # 一行を要素ごとに分割してリスト化する
            # divlistは一行を要素ごとに分割したリスト
            divlist = line.split()
            
            # 各要素を取得
            date = get_date(divlist[0])
            request_method = get_request_method(divlist[7])
            request_body = get_request_body(divlist[8])
            status_code = get_status_code(divlist[10])

            # 処理時間の差分を計算
            if past_divlist == []:
                # 次の行で参照する為に、行データを格納する
                past_divlist = divlist
                continue
            else:
                past_date = get_date(past_divlist[0])
                delta_date = date - past_date
                # 次の行で参照する為に、行データを格納する
                past_divlist = divlist

            # データの出力形式の設定
            print('日時', '処理時間', 'リクエストメソッド', 'ステータスコード', 'リクエストボディ')
            print(date, delta_date, request_method, status_code, request_body)

        
def get_date(data):            
    year = int(data[:4], 10)
    month = int(data[5:7], 10)
    day = int(data[8:10], 10)
    hour = int(data[11:13], 10)
    minute = int(data[14:16], 10)
    second = int(data[17:19], 10)
    microsecond = int(data[20:22], 10)

    date = datetime.datetime(year=year, month= month, day= day, hour=hour, \
        minute=minute, second=second, microsecond=microsecond)
    
    # print(year, month, day, hour, minute, second, microsecond)
    # print(date)
    return date

def get_request_method(data):
    request_method = data[2:]
    return request_method


def get_request_body(data):
    request_body = data
    return request_body


def get_status_code(data):
    status_code = data
    return status_code





if __name__=='__main__':
    main()






