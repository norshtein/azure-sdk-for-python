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

from .resource import Resource
from .location import Location
from .error import Error, ErrorException
from .group_item import GroupItem
from .application import Application
from .iosmam_policy import IOSMAMPolicy
from .android_mam_policy import AndroidMAMPolicy
from .mam_policy_app_id_or_group_id_payload import MAMPolicyAppIdOrGroupIdPayload
from .mam_policy_app_or_group_id_properties import MAMPolicyAppOrGroupIdProperties
from .mam_policy_properties import MAMPolicyProperties
from .device import Device
from .wipe_device_operation_result import WipeDeviceOperationResult
from .operation_result import OperationResult
from .operation_metadata_properties import OperationMetadataProperties
from .statuses_default import StatusesDefault
from .flagged_user import FlaggedUser
from .flagged_enrolled_app import FlaggedEnrolledApp
from .flagged_enrolled_app_error import FlaggedEnrolledAppError
from .location_paged import LocationPaged
from .application_paged import ApplicationPaged
from .iosmam_policy_paged import IOSMAMPolicyPaged
from .android_mam_policy_paged import AndroidMAMPolicyPaged
from .group_item_paged import GroupItemPaged
from .device_paged import DevicePaged
from .operation_result_paged import OperationResultPaged
from .flagged_user_paged import FlaggedUserPaged
from .flagged_enrolled_app_paged import FlaggedEnrolledAppPaged

__all__ = [
    'Resource',
    'Location',
    'Error', 'ErrorException',
    'GroupItem',
    'Application',
    'IOSMAMPolicy',
    'AndroidMAMPolicy',
    'MAMPolicyAppIdOrGroupIdPayload',
    'MAMPolicyAppOrGroupIdProperties',
    'MAMPolicyProperties',
    'Device',
    'WipeDeviceOperationResult',
    'OperationResult',
    'OperationMetadataProperties',
    'StatusesDefault',
    'FlaggedUser',
    'FlaggedEnrolledApp',
    'FlaggedEnrolledAppError',
    'LocationPaged',
    'ApplicationPaged',
    'IOSMAMPolicyPaged',
    'AndroidMAMPolicyPaged',
    'GroupItemPaged',
    'DevicePaged',
    'OperationResultPaged',
    'FlaggedUserPaged',
    'FlaggedEnrolledAppPaged',
]