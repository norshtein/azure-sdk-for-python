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

from .base_job_parameters_py3 import BaseJobParameters


class BuildJobParameters(BaseJobParameters):
    """The parameters used to build a new Data Lake Analytics job.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. The job type of the current job (Hive, USql, or
     Scope (for internal use only)). Possible values include: 'USql', 'Hive',
     'Scope'
    :type type: str or ~azure.mgmt.datalake.analytics.job.models.JobType
    :param properties: Required. The job specific properties.
    :type properties:
     ~azure.mgmt.datalake.analytics.job.models.CreateJobProperties
    :param name: The friendly name of the job to build.
    :type name: str
    """

    _validation = {
        'type': {'required': True},
        'properties': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'JobType'},
        'properties': {'key': 'properties', 'type': 'CreateJobProperties'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, *, type, properties, name: str=None, **kwargs) -> None:
        super(BuildJobParameters, self).__init__(type=type, properties=properties, **kwargs)
        self.name = name
