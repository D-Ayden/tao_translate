import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


from translate_gui.crawler import mathching_result, yd_translate


def test_yd_translate():
    test_result = "Hello, World"
    result = yd_translate(key="你好，世界", sugar="Tbh5E8=q6U3EXe+&L[4c@")
    assert test_result == result


def test_matching_result():
    test_result = "百度一下"

    result = mathching_result(
        "http://www.baidu.com/",
        rule=r"<input type=submit id=su value=(.*?) class=\"bg s_btn\">",
        headers=None,
    ).group(1)
    print(result)
    assert test_result == result


def test_update_sugar():
    pass


def test_get_sugar():
    pass


if __name__ == "__main__":
    test_matching_result()
