import os
from PIL import Image
import pyocr
import requests

#OCRの環境設定
pyocr.tesseract.TESSERACT_CMD = r'OCR-PATH'
tools = pyocr.get_available_tools()
tool = tools[0]

#OCR対象の決定
#:TODO スクショしたファイルを指定できるようする
img = Image.open("test.png")

#画像から文字を抽出する
builder = pyocr.builders.TextBuilder(tesseract_layout=6)
text = tool.image_to_string(img, lang="eng", builder=builder)
print(text)

#DeepLパラメータ
deepl_token = "TOKEN"
source_lang = 'EN'  # 翻訳対象の言語
target_lang = 'JA'  # 翻訳後の言語
param = {
            'auth_key' : deepl_token,
            'text' : text,
            'source_lang' : source_lang,
            "target_lang": target_lang
}

#DeepLに文字列をPOST
request = requests.post("https://api-free.deepl.com/v2/translate", data=param)
result = request.json()
print(result)
