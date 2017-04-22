# -*- coding: utf-8 -*-

import json
from .database import db
from .models import ClusterLogs
import numpy as np

from sklearn.cluster import MeanShift, estimate_bandwidth

__author__ = 'wesleywwerneck'


def train_cluster():
    rows, data = get_train_data()

    data_set = np.array(data)

    bandwidth = estimate_bandwidth(data_set, quantile=0.2, n_samples=200)
    ms = MeanShift(bandwidth=bandwidth, cluster_all=False, bin_seeding=True)
    labels = ms.fit_predict(data_set)
    print(labels)

    for row, label in zip(rows, labels):
        row.label = int(label)
    db.session.commit()

    return labels


def get_train_data():
    data = []
    rows = ClusterLogs.query.filter_by(label=None)

    for log in rows:
        formated_data = format_data_set_peaks(log)
        data.append(formated_data[1::])
    return rows, data


def format_data_set_peaks(data):
    selected = [
        'PowerActive',
        'PowerReactive',
        'PowerAppearent',
        'LineCurrent',
        'LineVoltage',
        'Peaks'
    ]

    clean = [getattr(data, s) for s in selected]

    list_peaks = [float(l) for l in json.loads(clean[5])[:3]]
    clean_list = clean[:5] + list_peaks
    return clean_list
