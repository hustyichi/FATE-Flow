#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
from flask import request

from fate_flow.utils.api_utils import get_json_result, cluster_route
from fate_flow.utils.log_sharing_utils import LogCollector


@manager.route('/size', methods=['POST'])
@cluster_route
def get_log_size():
    # 获取日志行数
    request_data = request.json
    data = LogCollector(**request_data).get_size()
    return get_json_result(retcode=0, retmsg='success', data={"size": data})


@manager.route('/cat', methods=['POST'])
@cluster_route
def get_log():
    # 获取日志内容，实现是通过命令行执行 cat 获取本地的日志
    request_data = request.json
    data = LogCollector(**request_data).cat_log(request_data.get("begin"), request_data.get("end"))
    return get_json_result(retcode=0, retmsg='success', data=data)
