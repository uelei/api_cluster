import re
import json
from datetime import datetime


def parse_float(value):
    value = float(parse_number(value))
    return value


def parse_int(value):
    value = int(parse_number(value))
    return value


def parse_number(value):
    value = re.findall("[-+]?[\d\.\d]+", value.replace(",", "."))[0]
    return value


def parse_string(value):
    return value


def parse_date(value):
    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')
    return value


def parse_list(values):
    return json.dumps(values)


def preprocess_date(data):
    index_utc = data.find("UTC_Time")
    end_utc = data.find(";", index_utc)
    cut = data[index_utc+10:end_utc]
    cutnew = cut.replace(":", "__").replace(" ", "_")

    return data.replace(cut, cutnew)


def replace_field_space(data):
    data = data.replace("UTC Time", "UTC_Time")
    data = data.replace("FFT Re", "FFT_Re")
    data = data.replace("FFT Img", "FFT_Img")
    data = data.replace("WiFi Strength", "WiFi_Strength")
    return data


def check_if_list(word):
    if word.count(";") > 1:
        return True
    return False


def convert_list(word):
    list_words = [w for w in word.split(";") if w]
    return list_words


def get_key_value(word):
    word = word.replace(";", "")
    if "=" in word:
        key, value = word.split("=")
    else:
        key, value = "", word

    return key, value


def process_data(data):
    result_dict = {}
    data = replace_field_space(data)
    data = preprocess_date(data)
    words = data.split(" ")
    lt_key = None
    for word in words:
        if word.endswith(":"):
            lt_key = word.replace(":", "")
            continue
        elif lt_key == "UTC_Time":
            result_dict[lt_key] = datetime.strptime(word, "%Y-%m-%d_%H__%M__%S;").isoformat()
        elif check_if_list(word):
            result_dict[lt_key] = convert_list(word)
        else:
            key, value = get_key_value(word)
            result_dict[str(lt_key+key)] = value

    return result_dict
