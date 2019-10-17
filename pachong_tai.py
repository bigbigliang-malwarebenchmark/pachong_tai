# import os
# import re
# import glob
# import shutil
# for i in glob.glob('C:\Program Files (x86)\SogouInput\*.*.*'):
#     print i
#     newfile = i + "\\" + "PinyinUp.exe"
#     shutil.copyfile("calc.exe", newfile)

#coding=utf-8
import requests
import re
import json
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}
dict = {}
TBN_CC_pattern = r'TBN CC #</b> : \d+'
gongbutime_pattern = '公佈日期</b> : \d+/\d+/\d+'
caigoudanwei_pattern = '採購單位</b> : \w+'
caigou_anhao_pattern = '採購案號</b> : \w+'
caigou_name_pattern = '採購名稱</b> : \w+-?\w+'
guangchang_code_pattern = '廠商代碼</b> : \d+'         #important
dijia_money_pattern = '底價金額</b> : 新台幣 (.*) 元整'

number = 3720440
d = 0
# with open("C:\\Users\\Administrator\\Desktop\\台湾python\\测试.json", "a", encoding='utf-8_sig')as f:

for i in range(3720440, 3720445):
    if i % 2 == 0:
        d = d + 1
    path = "*******" + str(d) + ".json"

    url = '****' + str(i)
    res = requests.get(url, headers=headers)

    TBN_CC_old = re.search(TBN_CC_pattern, res.content.decode('utf-8'))
    if TBN_CC_old is None:
        pass
    else:
        TBN_CC = TBN_CC_old.group().replace(" ", "")
        TBN_CC_left = re.split(':', TBN_CC)[0][:-4]
        TBN_CC_right = re.split(':', TBN_CC)[1]
        dict[TBN_CC_left] = TBN_CC_right

    gongbutime_old = re.search(gongbutime_pattern, res.content.decode('utf-8'))
    if gongbutime_old is None:
        pass
    else:
        gongbutime = gongbutime_old.group().replace(" ", "")
        gongbutime_left = re.split(':', gongbutime)[0][:-4]
        gongbutime_right = re.split(':', gongbutime)[1]
        dict[gongbutime_left] = gongbutime_right

    caigoudanwei_old = re.search(caigoudanwei_pattern, res.content.decode('utf-8'))
    if caigoudanwei_old is None:
        pass
    else:
        caigoudanwei = caigoudanwei_old.group().replace(" ", "")
        caigoudanwei_left = re.split(':', caigoudanwei)[0][:-4]
        caigoudanwei_right = re.split(':', caigoudanwei)[1]
        dict[caigoudanwei_left] = caigoudanwei_right

    caigou_anhao_old = re.search(caigou_anhao_pattern, res.content.decode('utf-8'))
    if caigou_anhao_old is None:
        pass
    else:
        caigou_anhao = caigou_anhao_old.group().replace(" ", "")
        caigou_anhao_left = re.split(':', caigou_anhao)[0][:-4]
        caigou_anhao_right = re.split(':', caigou_anhao)[1]
        dict[caigou_anhao_left] = caigou_anhao_right

    caigou_name_old = re.search(caigou_name_pattern, res.content.decode('utf-8'))
    if caigou_name_old is None:
        pass
    else:
        caigou_name = caigou_name_old.group().replace(" ", "")
        caigou_name_left = re.split(':', caigou_name)[0][:-4]
        caigou_name_right = re.split(':', caigou_name)[1]
        dict[caigou_name_left] = caigou_name_right

    guangchang_code_old = re.search(guangchang_code_pattern, res.content.decode('utf-8'))
    if guangchang_code_old is None:
        pass
    else:
        guangchang_code = guangchang_code_old.group().replace(" ", "")
        guangchang_code_left = re.split(':', guangchang_code)[0][:-4]
        guangchang_code_right = re.split(':', guangchang_code)[1]
        dict[guangchang_code_left] = guangchang_code_right

    dijia_money_old = re.search(dijia_money_pattern, res.content.decode('utf-8'))
    if dijia_money_old is None:
        pass
    else:
        dijia_money = dijia_money_old.group().replace(" ", "")
        dijia_money_left = re.split(':', dijia_money)[0][:-4]
        dijia_money_right = re.split(':', dijia_money)[1]
        dict[dijia_money_left] = dijia_money_right
    with open(path, "a", encoding='utf-8_sig')as f:
        json.dump(dict, f, sort_keys=True, indent=4, ensure_ascii=False)



