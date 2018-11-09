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


class VoiceReceiver(Model):
    """A voice receiver.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the voice receiver. Names must be
     unique across all receivers within an action group.
    :type name: str
    :param country_code: Required. The country code of the voice receiver.
    :type country_code: str
    :param phone_number: Required. The phone number of the voice receiver.
    :type phone_number: str
    """

    _validation = {
        'name': {'required': True},
        'country_code': {'required': True},
        'phone_number': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'country_code': {'key': 'countryCode', 'type': 'str'},
        'phone_number': {'key': 'phoneNumber', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(VoiceReceiver, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.country_code = kwargs.get('country_code', None)
        self.phone_number = kwargs.get('phone_number', None)
