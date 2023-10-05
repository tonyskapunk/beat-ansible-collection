#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2023 Tony Garcia
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

DOCUMENTATION = r"""
---
module: beat

short_description: Beat time module

version_added: "1.0.0"

description: Beat time module is a module that returns the current time using internet time (beats).

options:
    centibeats:
        description: Whether to return centibeats or not.
        default: false
        type: bool

author:
    - Tony Garcia (@tonyskapunk)
"""

EXAMPLES = r"""
# Use centibeats
- name: Use centibeats
  tonyskapunk.beat.beat:
    centibeats: true

# Do not use centibeats
- name: Do not use centibeats
  tonyskapunk.beat.beat:
"""

RETURN = r"""
beats:
    description: The current time in beats.
    type: str
    returned: always
    sample: '@123.456'
centibeats:
    description: Whether centibeats were used or not.
    type: bool
    returned: always
    sample: true
"""

from ansible.module_utils.basic import AnsibleModule

from datetime import datetime


def internettime(hours, minutes, seconds, tzone, centibeats=False):
    """Returns time(Swatch Internet Time) in beats."""
    itime = ((seconds + (minutes * 60) + ((hours + tzone + 1) * 3600)) / 86.4) % 1000
    beats = int(itime)
    cbeats = str(itime).split(".")[1][0:3]
    if centibeats:
        return "@{0}.{1}".format(beats, cbeats)
    return "@{0}".format(beats)


def now(use_centibeats=False):
    """Gets the current time in beats."""
    utc_now = datetime.utcnow()
    beats = internettime(
        utc_now.hour, utc_now.minute, utc_now.second, 0, use_centibeats
    )
    return beats


def run_module():
    module_args = dict(
        centibeats=dict(type="bool", required=False, default=False),
    )
    result = dict(changed=True, centibeats=False, beats="")
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    err = ""
    try:
        beats = now(module.params["centibeats"])
    except Exception as e:
        beats = ""
        err = str(e)

    if beats:
        result["beats"] = beats
        result["changed"] = True
    else:
        module.fail_json(msg=err, **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()
