# -*- coding: utf-8 -*-
import json
from flask import request, Blueprint
from sqlalchemy import func
from .models import ClusterLogs
from .utils import process_data
from .trainning import train_cluster

from .database import db

__author__ = 'wesleywwerneck'

main = Blueprint("main", __name__)


@main.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        data = request.get_data()
        if not data:
            return "Invalid Request", 400
        result = process_data(str(data.decode("utf-8")))
        clusterlog = ClusterLogs(**result)
        db.session.add(clusterlog)
        db.session.commit()

        row_count = ClusterLogs.query.filter_by(label=None).count()

        if row_count >= 1000:
            train_cluster()

        clusterlog = ClusterLogs.query.filter_by(id=clusterlog.id).first()

        response_dict = clusterlog.__dict__
        response_dict.pop('_sa_instance_state', None)
        response_dict['UTC_Time'] = response_dict['UTC_Time'].isoformat()

        return json.dumps(response_dict)

    elif request.method == 'GET':
        result_dict = {}
        result = db.session.query(ClusterLogs.label,
                                  func.count(ClusterLogs.label).label('count'),
                                  func.avg(ClusterLogs.PowerActive).label('average')
                                  ).group_by(ClusterLogs.label).all()
        for k, count, avg in result:
            result_dict[k] = {"cluster_count": count,
                              "Power_Active_Average": avg}
        return json.dumps(result_dict)
