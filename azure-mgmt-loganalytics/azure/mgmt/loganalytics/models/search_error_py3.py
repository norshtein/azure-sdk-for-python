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


class SearchError(Model):
    """Details for a search error.

    :param type: The error type.
    :type type: str
    :param message: The error message.
    :type message: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, type: str=None, message: str=None, **kwargs) -> None:
        super(SearchError, self).__init__(**kwargs)
        self.type = type
        self.message = message