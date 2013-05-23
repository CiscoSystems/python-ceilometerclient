# -*- encoding: utf-8 -*-
#
# Copyright © 2013 Red Hat, Inc
#
# Author:  Eoghan Glynn <eglynn@redhat.com>
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from ceilometerclient.common import base
from ceilometerclient.v2 import options


class Alarm(base.Resource):
    def __repr__(self):
        return "<Alarm %s>" % self._info


class AlarmManager(base.Manager):
    resource_class = Alarm

    @staticmethod
    def _path(id=None):
        return '/v2/alarms/%s' % id if id else '/v2/alarms'

    def list(self, q=None):
        return self._list(options.build_url(self._path(), q))

    def get(self, alarm_id):
        try:
            return self._list(self._path(alarm_id), expect_single=True)[0]
        except IndexError:
            return None

    def delete(self, alarm_id):
        return self._delete(self._path(alarm_id))