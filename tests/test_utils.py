from datetime import datetime

from back.utils import parse_float, parse_int, parse_number, parse_string, parse_date, parse_list, preprocess_date, \
    replace_field_space, check_if_list, convert_list, get_key_value, process_data


def test_parse_float():

    value = parse_float("10.2")

    assert value == 10.2

    value = parse_float("-810.2")

    assert value == -810.2

    value = parse_float("2")

    assert value == 2

    value = parse_float("ASD10.2")

    assert value == 10.2

    value = parse_float("-810.2DASDA")

    assert value == -810.2

    value = parse_float("dasas2das")

    assert value == 2

    value = parse_float("dasas11.2das1")

    assert value == 11.2


def test_parse_int():
    value = parse_int("10")

    assert value == 10

    value = parse_int("-810")

    assert value == -810

    value = parse_int("ASD102")

    assert value == 102

    value = parse_int("-8102DASDA")

    assert value == -8102

    value = parse_int("dasas2das")

    assert value == 2

    value = parse_int("dasas11das1")

    assert value == 11


def test_parse_number():
    value = parse_number("10.2")

    assert value == '10.2'

    value = parse_number("-810.2")

    assert value == '-810.2'

    value = parse_number("2")

    assert value == '2'

    value = parse_number("ASD10.2")

    assert value == '10.2'

    value = parse_number("-810.2DASDA")

    assert value == '-810.2'

    value = parse_number("dasas2das")

    assert value == '2'

    value = parse_number("dasas11.2das1")

    assert value == '11.2'

def test_parse_string():
    value = parse_string("10.2")

    assert value == "10.2"


def test_parse_date():
    value = parse_date("2017-12-11T12:11:22")

    assert value == datetime(2017, 12, 11, 12, 11, 22)


def test_parse_list():
    value = parse_list(["1", "2"])

    assert value == '["1", "2"]'


def test_preprocess_date():
    value = preprocess_date("UTC_Time: 2016-10-4 16:47:50;")

    assert value == "UTC_Time: 2016-10-4_16__47__50;"


def test_replace_field_space():
    value = replace_field_space("UTC Time FFT Re FFT Img WiFi Strength")

    assert value == 'UTC_Time FFT_Re FFT_Img WiFi_Strength'


def test_check_if_list():

    assert check_if_list("q;t;q")

    assert not check_if_list("1;")


def test_convert_list():
    value = convert_list("3;4;1;2;-43")

    assert value == ["3", "4", "1", "2", "-43"]


def test_get_key_value():
    value = get_key_value("ID=12;")

    assert value == ("ID", "12")

    value = get_key_value("123")

    assert value == ("", "123")


def test_process_data():
    text = """Device: ID=1; Fw=16071801; Evt=1; Alarms: CoilRevesed=OFF; Power: Active=1832W; Reactive=279var; Appearent=403VA; Line: Current=7.50400019; Voltage=230.08V; Phase=-43,841rad; Peaks: 14.3940001;14.420999499999999;14.46;14.505999599999999;14.1499996;13.925999599999999;13.397999800000003;13.0539999;13.020999900000001;13.074000400000001; FFT Re: 10263;13;145;-13;943;-19;798;0;237; FFT Img: 1465;6;-818;13;1115;6;706;19;699; UTC Time: 2016-10-4 16:47:50; hz: 49.87; WiFi Strength: -62; Dummy: 20"""

    value = process_data(text)
    print(value)

    assert value == {
        'WiFi_Strength': '-62',
        'DeviceID': '1',
        'hz': '49.87',
        'DeviceFw': '16071801',
        'UTC_Time': '2016-10-04T16:47:50',
        'PowerActive': '1832W',
        'DeviceEvt': '1',
        'PowerAppearent': '403VA',
        'PowerReactive': '279var',
        'Dummy': '20',
        'LineVoltage': '230.08V',
        'AlarmsCoilRevesed': 'OFF',
        'Peaks': ['14.3940001',
                  '14.420999499999999',
                  '14.46',
                  '14.505999599999999',
                  '14.1499996',
                  '13.925999599999999',
                  '13.397999800000003',
                  '13.0539999',
                  '13.020999900000001',
                  '13.074000400000001'],
        'LineCurrent': '7.50400019',
        'LinePhase': '-43,841rad',
        'FFT_Img': [
            '1465', '6', '-818', '13', '1115', '6', '706', '19', '699'],
        'FFT_Re': ['10263', '13', '145', '-13', '943', '-19', '798', '0', '237']
    }
