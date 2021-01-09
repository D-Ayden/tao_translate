import os
from typing import Final, Mapping, List

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

YD_URL: Final = "http://fanyi.youdao.com"
YD_RULE: Final = (
    r"http://shared.ydstatic.com/fanyi/newweb/.*?/scripts/newweb/fanyi.min.js"
)
TRANSLATE_URL: Final = (
    "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
)
YD_STATIC_RULE: Final = r'sign:n.md5\("fanyideskweb"\+e\+i\+"(.*?)"\)'


LANGUAGE_MAPPING: Final[Mapping[str, str]] = {
    "中文": "zh-CHS",
    "英语": "en",
    "日语": "ja",
    "韩语": "ko",
    "法语": "fr",
    "德语": "de",
    "俄语": "ru",
}
TRANSLATE_SELECTED: Final[List[str]] = [
    "中文",
    "英语",
    "日语",
    "韩语",
    "法语",
    "德语",
    "俄语",
]