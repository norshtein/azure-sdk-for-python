# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PowerShellCommandParameters(Model):
    """The parameters to a PowerShell script execution command.

    :param command: Script to execute.
    :type command: str
    """

    _attribute_map = {
        'command': {'key': 'properties.command', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PowerShellCommandParameters, self).__init__(**kwargs)
        self.command = kwargs.get('command', None)
