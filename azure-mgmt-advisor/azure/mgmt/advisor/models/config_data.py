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


class ConfigData(Model):
    """The Advisor configuration data structure.

    :param id: The resource Id of the configuration resource.
    :type id: str
    :param type: The type of the configuration resource.
    :type type: str
    :param name: The name of the configuration resource.
    :type name: str
    :param properties: The list of property name/value pairs.
    :type properties: ~azure.mgmt.advisor.models.ConfigDataProperties
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'ConfigDataProperties'},
    }

    def __init__(self, id=None, type=None, name=None, properties=None):
        super(ConfigData, self).__init__()
        self.id = id
        self.type = type
        self.name = name
        self.properties = properties