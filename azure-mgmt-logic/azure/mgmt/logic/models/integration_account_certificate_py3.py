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

from .resource_py3 import Resource


class IntegrationAccountCertificate(Resource):
    """The integration account certificate.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The resource id.
    :vartype id: str
    :ivar name: Gets the resource name.
    :vartype name: str
    :ivar type: Gets the resource type.
    :vartype type: str
    :param location: The resource location.
    :type location: str
    :param tags: The resource tags.
    :type tags: dict[str, str]
    :ivar created_time: The created time.
    :vartype created_time: datetime
    :ivar changed_time: The changed time.
    :vartype changed_time: datetime
    :param metadata: The metadata.
    :type metadata: object
    :param key: The key details in the key vault.
    :type key: ~azure.mgmt.logic.models.KeyVaultKeyReference
    :param public_certificate: The public certificate.
    :type public_certificate: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'created_time': {'readonly': True},
        'changed_time': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'created_time': {'key': 'properties.createdTime', 'type': 'iso-8601'},
        'changed_time': {'key': 'properties.changedTime', 'type': 'iso-8601'},
        'metadata': {'key': 'properties.metadata', 'type': 'object'},
        'key': {'key': 'properties.key', 'type': 'KeyVaultKeyReference'},
        'public_certificate': {'key': 'properties.publicCertificate', 'type': 'str'},
    }

    def __init__(self, *, location: str=None, tags=None, metadata=None, key=None, public_certificate: str=None, **kwargs) -> None:
        super(IntegrationAccountCertificate, self).__init__(location=location, tags=tags, **kwargs)
        self.created_time = None
        self.changed_time = None
        self.metadata = metadata
        self.key = key
        self.public_certificate = public_certificate
