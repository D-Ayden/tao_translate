"""
Author: your name
Date: 2020-12-18 00:58:21
LastEditTime: 2020-12-18 00:58:36
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\GUI\_simpleGui\\translate.py
"""

import hashlib
import json
import re
import random
import time
from typing import Any, TypeVar, MutableMapping, Final, Match, Union

import requests
from log import logger
from fake_useragent import UserAgent


AnyStr = TypeVar("AnyStr", str, bytes, None)
TranslateStr = Union[str, bool, None]


YD_URL: Final = "http://fanyi.youdao.com"
YD_RULE: Final = (
    r"http://shared.ydstatic.com/fanyi/newweb/.*?/scripts/newweb/fanyi.min.js"
)
TRANSLATE_URL: Final = (
    "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
)
YD_STATIC_RULE: Final = r'sign:n.md5\("fanyideskweb"\+e\+i\+"(.*?)"\)'

ua = UserAgent()
yd_headers: MutableMapping[str, str] = {
    "User-Agent": ua.random,
    "Host": "fanyi.youdao.com",
    "Origin": "http://fanyi.youdao.com",
    "Referer": "http://fanyi.youdao.com",
}
yd_static_headers: MutableMapping[str, str] = {
    "User-Agent": ua.random,
    "Host": "shared.ydstatic.com",
}


@logger.catch
def yd_translate(
    key: str,
    sugar: str,
    headers: MutableMapping[str, str] = yd_headers,
    from_lang: str = "zh-CHS",
    to_lang: str = "en",
) -> TranslateStr:

    # if key == "\n":
    #     return key

    lts: str = str(time.time() * 1000)
    salt: str = lts + str(random.randint(0, 10))

    before_md5_sign: str = "fanyideskweb" + key + salt + sugar
    md5 = hashlib.md5()
    md5.update(before_md5_sign.encode("utf-8"))
    sign: str = md5.hexdigest()

    headers.update(
        {
            "Cookie": "OUTFOX_SEARCH_USER_ID=929711230@10.169.0.102; \
                    OUTFOX_SEARCH_USER_ID_NCOO=925183201.3282317; \
                    _ntes_nnid=39a06059f232f05b5fe36d520b593d22,1608185560954; \
                    JSESSIONID=aaaMPIVPwNPKl7yaRHVzx; \
                    JSESSIONID=abc2fwegYO4Pq557QHVzx; \
                    ___rl__test__cookies="
            + lts
        }
    )

    form_data: MutableMapping[str, str] = {
        "i": key,
        "from": from_lang,
        "to": to_lang,
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign,
        "lts": lts,
        "bv": "5504a5c7c19867a06038cf79d29f756a",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME",
    }

    try:
        response = requests.post(url=TRANSLATE_URL, headers=headers, data=form_data)

    except requests.exceptions.ConnectionError:
        raise ConnectionError("网络连接错误，请检查你的网络")

    except Exception as e:
        raise e
    else:
        translation_result_json: Any = response.json()
        if translation_result_json["errorCode"] == 50:
            raise ValueError("errorCode is 50, please update data...")

        translation_result: dict = translation_result_json["translateResult"][0][0]
        return translation_result["tgt"]


@logger.catch
def mathching_result(url: str, rule: str, headers: MutableMapping[str, str]) -> Match:
    try:
        response = requests.get(url, headers=headers)
    except requests.exceptions.ConnectionError:
        raise ConnectionError
    except Exception as e:
        raise e
    else:
        search_result = re.search(rule, response.text)
        if not search_result:
            raise ValueError("返回值为空...")

        return search_result


def update_sugar() -> None:
    last_url = mathching_result(url=YD_URL, rule=YD_RULE, headers=yd_headers).group()
    sugar = mathching_result(
        url=last_url, rule=YD_STATIC_RULE, headers=yd_static_headers
    ).group(1)

    with open("sugar.json", "w", encoding="utf-8") as f:
        json.dump({"sugar": sugar}, f)


def get_sugar() -> str:
    with open("sugar.json", "r", encoding="utf-8") as f:
        sugar = json.load(f)["sugar"]
    return sugar


if __name__ == "__main__":
    update_sugar()