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


class ListEnvironmentsResponse(Model):
    """Represents the list of environments owned by a user.

    :param environments: List of all the evironments
    :type environments:
     list[~azure.mgmt.labservices.models.EnvironmentDetails]
    """

    _attribute_map = {
        'environments': {'key': 'environments', 'type': '[EnvironmentDetails]'},
    }

    def __init__(self, **kwargs):
        super(ListEnvironmentsResponse, self).__init__(**kwargs)
        self.environments = kwargs.get('environments', None)
