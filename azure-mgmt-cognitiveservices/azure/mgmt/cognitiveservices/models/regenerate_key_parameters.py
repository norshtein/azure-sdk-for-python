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


class RegenerateKeyParameters(Model):
    """Regenerate key parameters.

    All required parameters must be populated in order to send to Azure.

    :param key_name: Required. key name to generate (Key1|Key2). Possible
     values include: 'Key1', 'Key2'
    :type key_name: str or ~azure.mgmt.cognitiveservices.models.KeyName
    """

    _validation = {
        'key_name': {'required': True},
    }

    _attribute_map = {
        'key_name': {'key': 'keyName', 'type': 'KeyName'},
    }

    def __init__(self, **kwargs):
        super(RegenerateKeyParameters, self).__init__(**kwargs)
        self.key_name = kwargs.get('key_name', None)
