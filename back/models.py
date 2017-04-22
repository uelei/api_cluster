# -*- coding: utf-8 -*-
from .database import db
from .utils import parse_int, parse_float, parse_string, parse_date, parse_list

__author__ = 'wesleywwerneck'


FIELDS_PARSE = {
    'label': parse_int,
    'DeviceID': parse_int,
    'DeviceFw': parse_int,
    'DeviceEvt': parse_int,
    'AlarmsCoilRevesed': parse_string,
    'PowerActive': parse_int,
    'PowerReactive': parse_int,
    'PowerAppearent': parse_int,
    'LineCurrent': parse_float,
    'LineVoltage': parse_float,
    'LinePhase': parse_float,
    'Peaks': parse_list,
    'FFT_Re': parse_list,
    'FFT_Img': parse_list,
    'UTC_Time': parse_date,
    'hz': parse_float,
    'WiFi_Strength' : parse_int,
    'Dummy': parse_int,
}


class ClusterLogs(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.Integer)
    DeviceID = db.Column(db.Integer)
    DeviceFw = db.Column(db.Integer)
    DeviceEvt = db.Column(db.Integer)
    AlarmsCoilRevesed = db.Column(db.String)
    PowerActive = db.Column(db.Integer)
    PowerReactive = db.Column(db.Integer)
    PowerAppearent = db.Column(db.Integer)
    LineCurrent = db.Column(db.Float)
    LineVoltage = db.Column(db.Float)
    LinePhase = db.Column(db.Float)
    Peaks = db.Column(db.String)
    FFT_Re = db.Column(db.String)
    FFT_Img = db.Column(db.String)
    UTC_Time = db.Column(db.DateTime)
    hz = db.Column(db.Float)
    WiFi_Strength = db.Column(db.Integer)
    Dummy = db.Column(db.Integer)

    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            parsed_value = FIELDS_PARSE[name](value)
            self.__setattr__(name, parsed_value)

