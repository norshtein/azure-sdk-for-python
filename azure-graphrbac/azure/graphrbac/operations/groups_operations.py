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

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class GroupsOperations(object):
    """GroupsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Client API version. Constant value: "1.6".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "1.6"

        self.config = config

    def is_member_of(
            self, parameters, custom_headers=None, raw=False, **operation_config):
        """Checks whether the specified user, group, contact, or service principal
        is a direct or transitive member of the specified group.

        :param parameters: The check group membership parameters.
        :type parameters:
         ~azure.graphrbac.models.CheckGroupMembershipParameters
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: CheckGroupMembershipResult or ClientRawResponse if raw=true
        :rtype: ~azure.graphrbac.models.CheckGroupMembershipResult or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        # Construct URL
        url = self.is_member_of.metadata['url']
        path_format_arguments = {
            'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'CheckGroupMembershipParameters')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.GraphErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('CheckGroupMembershipResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    is_member_of.metadata = {'url': '/{tenantID}/isMemberOf'}

    def remove_member(
            self, group_object_id, member_object_id, custom_headers=None, raw=False, **operation_config):
        """Remove a member from a group.

        :param group_object_id: The object ID of the group from which to
         remove the member.
        :type group_object_id: str
        :param member_object_id: Member object id
        :type member_object_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        # Construct URL
        url = self.remove_member.metadata['url']
        path_format_arguments = {
            'groupObjectId': self._serialize.url("group_object_id", group_object_id, 'str'),
            'memberObjectId': self._serialize.url("member_object_id", member_object_id, 'str'),
            'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.GraphErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    remove_member.metadata = {'url': '/{tenantID}/groups/{groupObjectId}/$links/members/{memberObjectId}'}

    def add_member(
            self, group_object_id, url, additional_properties=None, custom_headers=None, raw=False, **operation_config):
        """Add a member to a group.

        :param group_object_id: The object ID of the group to which to add the
         member.
        :type group_object_id: str
        :param url: A member object URL, such as
         "https://graph.windows.net/0b1f9851-1bf0-433f-aec3-cb9272f093dc/directoryObjects/f260bbc4-c254-447b-94cf-293b5ec434dd",
         where "0b1f9851-1bf0-433f-aec3-cb9272f093dc" is the tenantId and
         "f260bbc4-c254-447b-94cf-293b5ec434dd" is the objectId of the member
         (user, application, servicePrincipal, group) to be added.
        :type url: str
        :param additional_properties: Unmatched properties from the message
         are deserialized this collection
        :type additional_properties: dict[str, object]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        parameters = models.GroupAddMemberParameters(additional_properties=additional_properties, url=url)

        # Construct URL
        url = self.add_member.metadata['url']
        path_format_arguments = {
            'groupObjectId': self._serialize.url("group_object_id", group_object_id, 'str'),
            'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'GroupAddMemberParameters')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.GraphErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    add_member.metadata = {'url': '/{tenantID}/groups/{groupObjectId}/$links/members'}

    def create(
            self, parameters, custom_headers=None, raw=False, **operation_config):
        """Create a group in the directory.

        :param parameters: The parameters for the group to create.
        :type parameters: ~azure.graphrbac.models.GroupCreateParameters
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ADGroup or ClientRawResponse if raw=true
        :rtype: ~azure.graphrbac.models.ADGroup or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'GroupCreateParameters')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.GraphErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('ADGroup', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create.metadata = {'url': '/{tenantID}/groups'}

    def list(
            self, filter=None, custom_headers=None, raw=False, **operation_config):
        """Gets list of groups for the current tenant.

        :param filter: The filter to apply to the operation.
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of ADGroup
        :rtype:
         ~azure.graphrbac.models.ADGroupPaged[~azure.graphrbac.models.ADGroup]
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = '/{tenantID}/{nextLink}'
                path_format_arguments = {
                    'nextLink': self._serialize.url("next_link", next_link, 'str', skip_quote=True),
                    'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.GraphErrorException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.ADGroupPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.ADGroupPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list.metadata = {'url': '/{tenantID}/groups'}

    def get_group_members(
            self, object_id, custom_headers=None, raw=False, **operation_config):
        """Gets the members of a group.

        :param object_id: The object ID of the group whose members should be
         retrieved.
        :type object_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of DirectoryObject
        :rtype:
         ~azure.graphrbac.models.DirectoryObjectPaged[~azure.graphrbac.models.DirectoryObject]
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.get_group_members.metadata['url']
                path_format_arguments = {
                    'objectId': self._serialize.url("object_id", object_id, 'str'),
                    'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = '/{tenantID}/{nextLink}'
                path_format_arguments = {
                    'nextLink': self._serialize.url("next_link", next_link, 'str', skip_quote=True),
                    'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.GraphErrorException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.DirectoryObjectPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.DirectoryObjectPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    get_group_members.metadata = {'url': '/{tenantID}/groups/{objectId}/members'}

    def get(
            self, object_id, custom_headers=None, raw=False, **operation_config):
        """Gets group information from the directory.

        :param object_id: The object ID of the user for which to get group
         information.
        :type object_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ADGroup or ClientRawResponse if raw=true
        :rtype: ~azure.graphrbac.models.ADGroup or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'objectId': self._serialize.url("object_id", object_id, 'str'),
            'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.GraphErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ADGroup', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/{tenantID}/groups/{objectId}'}

    def delete(
            self, object_id, custom_headers=None, raw=False, **operation_config):
        """Delete a group from the directory.

        :param object_id: The object ID of the group to delete.
        :type object_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'objectId': self._serialize.url("object_id", object_id, 'str'),
            'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.GraphErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete.metadata = {'url': '/{tenantID}/groups/{objectId}'}

    def get_member_groups(
            self, object_id, security_enabled_only, additional_properties=None, custom_headers=None, raw=False, **operation_config):
        """Gets a collection of object IDs of groups of which the specified group
        is a member.

        :param object_id: The object ID of the group for which to get group
         membership.
        :type object_id: str
        :param security_enabled_only: If true, only membership in
         security-enabled groups should be checked. Otherwise, membership in
         all groups should be checked.
        :type security_enabled_only: bool
        :param additional_properties: Unmatched properties from the message
         are deserialized this collection
        :type additional_properties: dict[str, object]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of str
        :rtype: ~azure.graphrbac.models.StrPaged[str]
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        parameters = models.GroupGetMemberGroupsParameters(additional_properties=additional_properties, security_enabled_only=security_enabled_only)

        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.get_member_groups.metadata['url']
                path_format_arguments = {
                    'objectId': self._serialize.url("object_id", object_id, 'str'),
                    'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct body
            body_content = self._serialize.body(parameters, 'GroupGetMemberGroupsParameters')

            # Construct and send request
            request = self._client.post(url, query_parameters, header_parameters, body_content)
            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.GraphErrorException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.StrPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.StrPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    get_member_groups.metadata = {'url': '/{tenantID}/groups/{objectId}/getMemberGroups'}

    def list_owners(
            self, object_id, custom_headers=None, raw=False, **operation_config):
        """Directory objects that are owners of the group.

        The owners are a set of non-admin users who are allowed to modify this
        object.

        :param object_id: The object ID of the group for which to get owners.
        :type object_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of DirectoryObject
        :rtype:
         ~azure.graphrbac.models.DirectoryObjectPaged[~azure.graphrbac.models.DirectoryObject]
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list_owners.metadata['url']
                path_format_arguments = {
                    'objectId': self._serialize.url("object_id", object_id, 'str'),
                    'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.GraphErrorException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.DirectoryObjectPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.DirectoryObjectPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list_owners.metadata = {'url': '/{tenantID}/groups/{objectId}/owners'}

    def add_owner(
            self, object_id, url, additional_properties=None, custom_headers=None, raw=False, **operation_config):
        """Add an owner to a group.

        :param object_id: The object ID of the application to which to add the
         owner.
        :type object_id: str
        :param url: A owner object URL, such as
         "https://graph.windows.net/0b1f9851-1bf0-433f-aec3-cb9272f093dc/directoryObjects/f260bbc4-c254-447b-94cf-293b5ec434dd",
         where "0b1f9851-1bf0-433f-aec3-cb9272f093dc" is the tenantId and
         "f260bbc4-c254-447b-94cf-293b5ec434dd" is the objectId of the owner
         (user, application, servicePrincipal, group) to be added.
        :type url: str
        :param additional_properties: Unmatched properties from the message
         are deserialized this collection
        :type additional_properties: dict[str, object]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        parameters = models.AddOwnerParameters(additional_properties=additional_properties, url=url)

        # Construct URL
        url = self.add_owner.metadata['url']
        path_format_arguments = {
            'objectId': self._serialize.url("object_id", object_id, 'str'),
            'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'AddOwnerParameters')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.GraphErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    add_owner.metadata = {'url': '/{tenantID}/groups/{objectId}/$links/owners'}

    def remove_owner(
            self, object_id, owner_object_id, custom_headers=None, raw=False, **operation_config):
        """Remove a member from owners.

        :param object_id: The object ID of the group from which to remove the
         owner.
        :type object_id: str
        :param owner_object_id: Owner object id
        :type owner_object_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        # Construct URL
        url = self.remove_owner.metadata['url']
        path_format_arguments = {
            'objectId': self._serialize.url("object_id", object_id, 'str'),
            'ownerObjectId': self._serialize.url("owner_object_id", owner_object_id, 'str'),
            'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.GraphErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    remove_owner.metadata = {'url': '/{tenantID}/groups/{objectId}/$links/owners/{ownerObjectId}'}
