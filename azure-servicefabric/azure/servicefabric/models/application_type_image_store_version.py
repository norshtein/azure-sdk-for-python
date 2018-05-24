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


class ApplicationTypeImageStoreVersion(Model):
    """A version description for the application type.

    :param application_type_version:
    :type application_type_version: str
    """

    _validation = {
        'application_type_version': {'required': True},
    }

    _attribute_map = {
        'application_type_version': {'key': 'ApplicationTypeVersion', 'type': 'str'},
    }

    def __init__(self, application_type_version):
        self.application_type_version = application_type_version