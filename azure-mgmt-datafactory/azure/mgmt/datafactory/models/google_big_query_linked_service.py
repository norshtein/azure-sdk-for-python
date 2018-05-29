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

from .linked_service import LinkedService


class GoogleBigQueryLinkedService(LinkedService):
    """Google BigQuery service linked service.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param connect_via: The integration runtime reference.
    :type connect_via:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeReference
    :param description: Linked service description.
    :type description: str
    :param parameters: Parameters for linked service.
    :type parameters: dict[str,
     ~azure.mgmt.datafactory.models.ParameterSpecification]
    :param annotations: List of tags that can be used for describing the
     Dataset.
    :type annotations: list[object]
    :param type: Constant filled by server.
    :type type: str
    :param project: The default BigQuery project to query against.
    :type project: object
    :param additional_projects: A comma-separated list of public BigQuery
     projects to access.
    :type additional_projects: object
    :param request_google_drive_scope: Whether to request access to Google
     Drive. Allowing Google Drive access enables support for federated tables
     that combine BigQuery data with data from Google Drive. The default value
     is false.
    :type request_google_drive_scope: object
    :param authentication_type: The OAuth 2.0 authentication mechanism used
     for authentication. ServiceAuthentication can only be used on self-hosted
     IR. Possible values include: 'ServiceAuthentication', 'UserAuthentication'
    :type authentication_type: str or
     ~azure.mgmt.datafactory.models.GoogleBigQueryAuthenticationType
    :param refresh_token: The refresh token obtained from Google for
     authorizing access to BigQuery for UserAuthentication.
    :type refresh_token: ~azure.mgmt.datafactory.models.SecretBase
    :param client_id: The client id of the google application used to acquire
     the refresh token.
    :type client_id: ~azure.mgmt.datafactory.models.SecretBase
    :param client_secret: The client secret of the google application used to
     acquire the refresh token.
    :type client_secret: ~azure.mgmt.datafactory.models.SecretBase
    :param email: The service account email ID that is used for
     ServiceAuthentication and can only be used on self-hosted IR.
    :type email: object
    :param key_file_path: The full path to the .p12 key file that is used to
     authenticate the service account email address and can only be used on
     self-hosted IR.
    :type key_file_path: object
    :param trusted_cert_path: The full path of the .pem file containing
     trusted CA certificates for verifying the server when connecting over SSL.
     This property can only be set when using SSL on self-hosted IR. The
     default value is the cacerts.pem file installed with the IR.
    :type trusted_cert_path: object
    :param use_system_trust_store: Specifies whether to use a CA certificate
     from the system trust store or from a specified PEM file. The default
     value is false.
    :type use_system_trust_store: object
    :param encrypted_credential: The encrypted credential used for
     authentication. Credentials are encrypted using the integration runtime
     credential manager. Type: string (or Expression with resultType string).
    :type encrypted_credential: object
    """

    _validation = {
        'type': {'required': True},
        'project': {'required': True},
        'authentication_type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'connect_via': {'key': 'connectVia', 'type': 'IntegrationRuntimeReference'},
        'description': {'key': 'description', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{ParameterSpecification}'},
        'annotations': {'key': 'annotations', 'type': '[object]'},
        'type': {'key': 'type', 'type': 'str'},
        'project': {'key': 'typeProperties.project', 'type': 'object'},
        'additional_projects': {'key': 'typeProperties.additionalProjects', 'type': 'object'},
        'request_google_drive_scope': {'key': 'typeProperties.requestGoogleDriveScope', 'type': 'object'},
        'authentication_type': {'key': 'typeProperties.authenticationType', 'type': 'str'},
        'refresh_token': {'key': 'typeProperties.refreshToken', 'type': 'SecretBase'},
        'client_id': {'key': 'typeProperties.clientId', 'type': 'SecretBase'},
        'client_secret': {'key': 'typeProperties.clientSecret', 'type': 'SecretBase'},
        'email': {'key': 'typeProperties.email', 'type': 'object'},
        'key_file_path': {'key': 'typeProperties.keyFilePath', 'type': 'object'},
        'trusted_cert_path': {'key': 'typeProperties.trustedCertPath', 'type': 'object'},
        'use_system_trust_store': {'key': 'typeProperties.useSystemTrustStore', 'type': 'object'},
        'encrypted_credential': {'key': 'typeProperties.encryptedCredential', 'type': 'object'},
    }

    def __init__(self, project, authentication_type, additional_properties=None, connect_via=None, description=None, parameters=None, annotations=None, additional_projects=None, request_google_drive_scope=None, refresh_token=None, client_id=None, client_secret=None, email=None, key_file_path=None, trusted_cert_path=None, use_system_trust_store=None, encrypted_credential=None):
        super(GoogleBigQueryLinkedService, self).__init__(additional_properties=additional_properties, connect_via=connect_via, description=description, parameters=parameters, annotations=annotations)
        self.project = project
        self.additional_projects = additional_projects
        self.request_google_drive_scope = request_google_drive_scope
        self.authentication_type = authentication_type
        self.refresh_token = refresh_token
        self.client_id = client_id
        self.client_secret = client_secret
        self.email = email
        self.key_file_path = key_file_path
        self.trusted_cert_path = trusted_cert_path
        self.use_system_trust_store = use_system_trust_store
        self.encrypted_credential = encrypted_credential
        self.type = 'GoogleBigQuery'