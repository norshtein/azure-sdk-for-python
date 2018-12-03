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

from .connect_to_source_sql_server_task_output import ConnectToSourceSqlServerTaskOutput


class ConnectToSourceSqlServerTaskOutputLoginLevel(ConnectToSourceSqlServerTaskOutput):
    """Login level output for the task that validates connection to SQL Server and
    also validates source server requirements.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Result identifier
    :vartype id: str
    :param result_type: Required. Constant filled by server.
    :type result_type: str
    :ivar name: Login name.
    :vartype name: str
    :ivar login_type: The type of login. Possible values include:
     'WindowsUser', 'WindowsGroup', 'SqlLogin', 'Certificate', 'AsymmetricKey',
     'ExternalUser', 'ExternalGroup'
    :vartype login_type: str or ~azure.mgmt.datamigration.models.LoginType
    :ivar default_database: The default database for the login.
    :vartype default_database: str
    :ivar is_enabled: The state of the login.
    :vartype is_enabled: bool
    :ivar migration_eligibility: Information about eligibility of login for
     migration.
    :vartype migration_eligibility:
     ~azure.mgmt.datamigration.models.MigrationEligibilityInfo
    """

    _validation = {
        'id': {'readonly': True},
        'result_type': {'required': True},
        'name': {'readonly': True},
        'login_type': {'readonly': True},
        'default_database': {'readonly': True},
        'is_enabled': {'readonly': True},
        'migration_eligibility': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'result_type': {'key': 'resultType', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'login_type': {'key': 'loginType', 'type': 'str'},
        'default_database': {'key': 'defaultDatabase', 'type': 'str'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
        'migration_eligibility': {'key': 'migrationEligibility', 'type': 'MigrationEligibilityInfo'},
    }

    def __init__(self, **kwargs):
        super(ConnectToSourceSqlServerTaskOutputLoginLevel, self).__init__(**kwargs)
        self.name = None
        self.login_type = None
        self.default_database = None
        self.is_enabled = None
        self.migration_eligibility = None
        self.result_type = 'LoginLevelOutput'
