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

from msrest.pipeline import ClientRawResponse

from .. import models


class ReviewsOperations(object):
    """ReviewsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar content_type: The content type. Constant value: "text/plain".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config
        self.content_type = "text/plain"

    def get_review(
            self, team_name, review_id, custom_headers=None, raw=False, **operation_config):
        """Returns review details for the review Id passed.

        :param team_name: Your Team Name.
        :type team_name: str
        :param review_id: Id of the review.
        :type review_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Review or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.vision.contentmoderator.models.Review
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = '/contentmoderator/review/v1.0/teams/{teamName}/reviews/{reviewId}'
        path_format_arguments = {
            'baseUrl': self._serialize.url("self.config.base_url", self.config.base_url, 'str', skip_quote=True),
            'teamName': self._serialize.url("team_name", team_name, 'str'),
            'reviewId': self._serialize.url("review_id", review_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Review', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def get_job_details(
            self, team_name, job_id, custom_headers=None, raw=False, **operation_config):
        """Get the Job Details for a Job Id.

        :param team_name: Your Team Name.
        :type team_name: str
        :param job_id: Id of the job.
        :type job_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Job or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.vision.contentmoderator.models.Job or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = '/contentmoderator/review/v1.0/teams/{teamName}/jobs/{JobId}'
        path_format_arguments = {
            'baseUrl': self._serialize.url("self.config.base_url", self.config.base_url, 'str', skip_quote=True),
            'teamName': self._serialize.url("team_name", team_name, 'str'),
            'JobId': self._serialize.url("job_id", job_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Job', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def create_reviews(
            self, url_content_type, team_name, create_review_body, sub_team=None, custom_headers=None, raw=False, **operation_config):
        """The reviews created would show up for Reviewers on your team. As
        Reviewers complete reviewing, results of the Review would be POSTED
        (i.e. HTTP POST) on the specified CallBackEndpoint.
        <h3>CallBack Schemas </h3>
        <h4>Review Completion CallBack Sample</h4>
        <p>
        {<br/>
        "ReviewId": "<Review Id>",<br/>
        "ModifiedOn": "2016-10-11T22:36:32.9934851Z",<br/>
        "ModifiedBy": "<Name of the Reviewer>",<br/>
        "CallBackType": "Review",<br/>
        "ContentId": "<The ContentId that was specified input>",<br/>
        "Metadata": {<br/>
        "adultscore": "0.xxx",<br/>
        "a": "False",<br/>
        "racyscore": "0.xxx",<br/>
        "r": "True"<br/>
        },<br/>
        "ReviewerResultTags": {<br/>
        "a": "False",<br/>
        "r": "True"<br/>
        }<br/>
        }<br/>
        </p>.

        :param url_content_type: The content type.
        :type url_content_type: str
        :param team_name: Your team name.
        :type team_name: str
        :param create_review_body: Body for create reviews API
        :type create_review_body:
         list[~azure.cognitiveservices.vision.contentmoderator.models.CreateReviewBodyItem]
        :param sub_team: SubTeam of your team, you want to assign the created
         review to.
        :type sub_team: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype: list[str] or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = '/contentmoderator/review/v1.0/teams/{teamName}/reviews'
        path_format_arguments = {
            'baseUrl': self._serialize.url("self.config.base_url", self.config.base_url, 'str', skip_quote=True),
            'teamName': self._serialize.url("team_name", team_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if sub_team is not None:
            query_parameters['subTeam'] = self._serialize.query("sub_team", sub_team, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['UrlContentType'] = self._serialize.header("url_content_type", url_content_type, 'str')

        # Construct body
        body_content = self._serialize.body(create_review_body, '[CreateReviewBodyItem]')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('[str]', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def create_job(
            self, team_name, content_type, content_id, workflow_name, job_content_type, content_value, call_back_endpoint=None, custom_headers=None, raw=False, **operation_config):
        """A job Id will be returned for the content posted on this endpoint.
        Once the content is evaluated against the Workflow provided the review
        will be created or ignored based on the workflow expression.
        <h3>CallBack Schemas </h3>
        <p>
        <h4>Job Completion CallBack Sample</h4><br/>
        {<br/>
        "JobId": "<Job Id>,<br/>
        "ReviewId": "<Review Id, if the Job resulted in a Review to be
        created>",<br/>
        "WorkFlowId": "default",<br/>
        "Status": "<This will be one of Complete, InProgress, Error>",<br/>
        "ContentType": "Image",<br/>
        "ContentId": "<This is the ContentId that was specified on
        input>",<br/>
        "CallBackType": "Job",<br/>
        "Metadata": {<br/>
        "adultscore": "0.xxx",<br/>
        "a": "False",<br/>
        "racyscore": "0.xxx",<br/>
        "r": "True"<br/>
        }<br/>
        }<br/>
        </p>
        <p>
        <h4>Review Completion CallBack Sample</h4><br/>
        {
        "ReviewId": "<Review Id>",<br/>
        "ModifiedOn": "2016-10-11T22:36:32.9934851Z",<br/>
        "ModifiedBy": "<Name of the Reviewer>",<br/>
        "CallBackType": "Review",<br/>
        "ContentId": "<The ContentId that was specified input>",<br/>
        "Metadata": {<br/>
        "adultscore": "0.xxx",
        "a": "False",<br/>
        "racyscore": "0.xxx",<br/>
        "r": "True"<br/>
        },<br/>
        "ReviewerResultTags": {<br/>
        "a": "False",<br/>
        "r": "True"<br/>
        }<br/>
        }<br/>
        </p>.

        :param team_name: Your team name.
        :type team_name: str
        :param content_type: Image, Text or Video. Possible values include:
         'Image', 'Text', 'Video'
        :type content_type: str
        :param content_id: Id/Name to identify the content submitted.
        :type content_id: str
        :param workflow_name: Workflow Name that you want to invoke.
        :type workflow_name: str
        :param job_content_type: The content type. Possible values include:
         'application/json', 'image/jpeg'
        :type job_content_type: str
        :param content_value: Content to evaluate for a job.
        :type content_value: str
        :param call_back_endpoint: Callback endpoint for posting the create
         job result.
        :type call_back_endpoint: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: JobId or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.vision.contentmoderator.models.JobId
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        content = models.Content(content_value=content_value)

        # Construct URL
        url = '/contentmoderator/review/v1.0/teams/{teamName}/jobs'
        path_format_arguments = {
            'baseUrl': self._serialize.url("self.config.base_url", self.config.base_url, 'str', skip_quote=True),
            'teamName': self._serialize.url("team_name", team_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['ContentType'] = self._serialize.query("content_type", content_type, 'str')
        query_parameters['ContentId'] = self._serialize.query("content_id", content_id, 'str')
        query_parameters['WorkflowName'] = self._serialize.query("workflow_name", workflow_name, 'str')
        if call_back_endpoint is not None:
            query_parameters['CallBackEndpoint'] = self._serialize.query("call_back_endpoint", call_back_endpoint, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Content-Type'] = self._serialize.header("job_content_type", job_content_type, 'str')

        # Construct body
        body_content = self._serialize.body(content, 'Content')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('JobId', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def add_video_frame(
            self, team_name, review_id, timescale=None, custom_headers=None, raw=False, **operation_config):
        """The reviews created would show up for Reviewers on your team. As
        Reviewers complete reviewing, results of the Review would be POSTED
        (i.e. HTTP POST) on the specified CallBackEndpoint.
        <h3>CallBack Schemas </h3>
        <h4>Review Completion CallBack Sample</h4>
        <p>
        {<br/>
        "ReviewId": "<Review Id>",<br/>
        "ModifiedOn": "2016-10-11T22:36:32.9934851Z",<br/>
        "ModifiedBy": "<Name of the Reviewer>",<br/>
        "CallBackType": "Review",<br/>
        "ContentId": "<The ContentId that was specified input>",<br/>
        "Metadata": {<br/>
        "adultscore": "0.xxx",<br/>
        "a": "False",<br/>
        "racyscore": "0.xxx",<br/>
        "r": "True"<br/>
        },<br/>
        "ReviewerResultTags": {<br/>
        "a": "False",<br/>
        "r": "True"<br/>
        }<br/>
        }<br/>
        </p>.

        :param team_name: Your team name.
        :type team_name: str
        :param review_id: Id of the review.
        :type review_id: str
        :param timescale: Timescale of the video you are adding frames to.
        :type timescale: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = '/contentmoderator/review/v1.0/teams/{teamName}/reviews/{reviewId}/frames'
        path_format_arguments = {
            'baseUrl': self._serialize.url("self.config.base_url", self.config.base_url, 'str', skip_quote=True),
            'teamName': self._serialize.url("team_name", team_name, 'str'),
            'reviewId': self._serialize.url("review_id", review_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if timescale is not None:
            query_parameters['timescale'] = self._serialize.query("timescale", timescale, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def get_video_frames(
            self, team_name, review_id, start_seed=None, no_of_records=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """The reviews created would show up for Reviewers on your team. As
        Reviewers complete reviewing, results of the Review would be POSTED
        (i.e. HTTP POST) on the specified CallBackEndpoint.
        <h3>CallBack Schemas </h3>
        <h4>Review Completion CallBack Sample</h4>
        <p>
        {<br/>
        "ReviewId": "<Review Id>",<br/>
        "ModifiedOn": "2016-10-11T22:36:32.9934851Z",<br/>
        "ModifiedBy": "<Name of the Reviewer>",<br/>
        "CallBackType": "Review",<br/>
        "ContentId": "<The ContentId that was specified input>",<br/>
        "Metadata": {<br/>
        "adultscore": "0.xxx",<br/>
        "a": "False",<br/>
        "racyscore": "0.xxx",<br/>
        "r": "True"<br/>
        },<br/>
        "ReviewerResultTags": {<br/>
        "a": "False",<br/>
        "r": "True"<br/>
        }<br/>
        }<br/>
        </p>.

        :param team_name: Your team name.
        :type team_name: str
        :param review_id: Id of the review.
        :type review_id: str
        :param start_seed: Time stamp of the frame from where you want to
         start fetching the frames.
        :type start_seed: int
        :param no_of_records: Number of frames to fetch.
        :type no_of_records: int
        :param filter: Get frames filtered by tags.
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Frames or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.vision.contentmoderator.models.Frames
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = '/contentmoderator/review/v1.0/teams/{teamName}/reviews/{reviewId}/frames'
        path_format_arguments = {
            'baseUrl': self._serialize.url("self.config.base_url", self.config.base_url, 'str', skip_quote=True),
            'teamName': self._serialize.url("team_name", team_name, 'str'),
            'reviewId': self._serialize.url("review_id", review_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if start_seed is not None:
            query_parameters['startSeed'] = self._serialize.query("start_seed", start_seed, 'int')
        if no_of_records is not None:
            query_parameters['noOfRecords'] = self._serialize.query("no_of_records", no_of_records, 'int')
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Frames', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def publish_video_review(
            self, team_name, review_id, custom_headers=None, raw=False, **operation_config):
        """Publish video review to make it available for review.

        :param team_name: Your team name.
        :type team_name: str
        :param review_id: Id of the review.
        :type review_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = '/contentmoderator/review/v1.0/teams/{teamName}/reviews/{reviewId}/publish'
        path_format_arguments = {
            'baseUrl': self._serialize.url("self.config.base_url", self.config.base_url, 'str', skip_quote=True),
            'teamName': self._serialize.url("team_name", team_name, 'str'),
            'reviewId': self._serialize.url("review_id", review_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [204]:
            raise models.APIErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def add_video_transcript_moderation_result(
            self, content_type, team_name, review_id, transcript_moderation_body, custom_headers=None, raw=False, **operation_config):
        """This API adds a transcript screen text result file for a video review.
        Transcript screen text result file is a result of Screen Text API . In
        order to generate transcript screen text result file , a transcript
        file has to be screened for profanity using Screen Text API.

        :param content_type: The content type.
        :type content_type: str
        :param team_name: Your team name.
        :type team_name: str
        :param review_id: Id of the review.
        :type review_id: str
        :param transcript_moderation_body: Body for add video transcript
         moderation result API
        :type transcript_moderation_body:
         list[~azure.cognitiveservices.vision.contentmoderator.models.TranscriptModerationBodyItem]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = '/contentmoderator/review/v1.0/teams/{teamName}/reviews/{reviewId}/transcriptmoderationresult'
        path_format_arguments = {
            'baseUrl': self._serialize.url("self.config.base_url", self.config.base_url, 'str', skip_quote=True),
            'teamName': self._serialize.url("team_name", team_name, 'str'),
            'reviewId': self._serialize.url("review_id", review_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        # Construct body
        body_content = self._serialize.body(transcript_moderation_body, '[TranscriptModerationBodyItem]')

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [204]:
            raise models.APIErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def add_video_transcript(
            self, team_name, review_id, vt_tfile, custom_headers=None, raw=False, callback=None, **operation_config):
        """This API adds a transcript file (text version of all the words spoken
        in a video) to a video review. The file should be a valid WebVTT
        format.

        :param team_name: Your team name.
        :type team_name: str
        :param review_id: Id of the review.
        :type review_id: str
        :param vt_tfile: Transcript file of the video.
        :type vt_tfile: Generator
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param callback: When specified, will be called with each chunk of
         data that is streamed. The callback should take two arguments, the
         bytes of the current chunk of data and the response object. If the
         data is uploading, response will be None.
        :type callback: Callable[Bytes, response=None]
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = '/contentmoderator/review/v1.0/teams/{teamName}/reviews/{reviewId}/transcript'
        path_format_arguments = {
            'baseUrl': self._serialize.url("self.config.base_url", self.config.base_url, 'str', skip_quote=True),
            'teamName': self._serialize.url("team_name", team_name, 'str'),
            'reviewId': self._serialize.url("review_id", review_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'text/plain'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Content-Type'] = self._serialize.header("self.content_type", self.content_type, 'str')

        # Construct body
        body_content = self._client.stream_upload(vt_tfile, callback)

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [204]:
            raise models.APIErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def create_video_reviews(
            self, content_type, team_name, create_video_reviews_body, sub_team=None, custom_headers=None, raw=False, **operation_config):
        """The reviews created would show up for Reviewers on your team. As
        Reviewers complete reviewing, results of the Review would be POSTED
        (i.e. HTTP POST) on the specified CallBackEndpoint.
        <h3>CallBack Schemas </h3>
        <h4>Review Completion CallBack Sample</h4>
        <p>
        {<br/>
        "ReviewId": "<Review Id>",<br/>
        "ModifiedOn": "2016-10-11T22:36:32.9934851Z",<br/>
        "ModifiedBy": "<Name of the Reviewer>",<br/>
        "CallBackType": "Review",<br/>
        "ContentId": "<The ContentId that was specified input>",<br/>
        "Metadata": {<br/>
        "adultscore": "0.xxx",<br/>
        "a": "False",<br/>
        "racyscore": "0.xxx",<br/>
        "r": "True"<br/>
        },<br/>
        "ReviewerResultTags": {<br/>
        "a": "False",<br/>
        "r": "True"<br/>
        }<br/>
        }<br/>
        </p>.

        :param content_type: The content type.
        :type content_type: str
        :param team_name: Your team name.
        :type team_name: str
        :param create_video_reviews_body: Body for create reviews API
        :type create_video_reviews_body:
         list[~azure.cognitiveservices.vision.contentmoderator.models.CreateVideoReviewsBodyItem]
        :param sub_team: SubTeam of your team, you want to assign the created
         review to.
        :type sub_team: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype: list[str] or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = '/contentmoderator/review/v1.0/teams/{teamName}/reviews'
        path_format_arguments = {
            'baseUrl': self._serialize.url("self.config.base_url", self.config.base_url, 'str', skip_quote=True),
            'teamName': self._serialize.url("team_name", team_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if sub_team is not None:
            query_parameters['subTeam'] = self._serialize.query("sub_team", sub_team, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        # Construct body
        body_content = self._serialize.body(create_video_reviews_body, '[CreateVideoReviewsBodyItem]')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('[str]', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def add_video_frame_url(
            self, content_type, team_name, review_id, video_frame_body, timescale=None, custom_headers=None, raw=False, **operation_config):
        """Use this method to add frames for a video review.Timescale: This
        parameter is a factor which is used to convert the timestamp on a frame
        into milliseconds. Timescale is provided in the output of the Content
        Moderator video media processor on the Azure Media Services
        platform.Timescale in the Video Moderation output is Ticks/Second.

        :param content_type: The content type.
        :type content_type: str
        :param team_name: Your team name.
        :type team_name: str
        :param review_id: Id of the review.
        :type review_id: str
        :param video_frame_body: Body for add video frames API
        :type video_frame_body:
         list[~azure.cognitiveservices.vision.contentmoderator.models.VideoFrameBodyItem]
        :param timescale: Timescale of the video.
        :type timescale: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = '/contentmoderator/review/v1.0/teams/{teamName}/reviews/{reviewId}/frames'
        path_format_arguments = {
            'baseUrl': self._serialize.url("self.config.base_url", self.config.base_url, 'str', skip_quote=True),
            'teamName': self._serialize.url("team_name", team_name, 'str'),
            'reviewId': self._serialize.url("review_id", review_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if timescale is not None:
            query_parameters['timescale'] = self._serialize.query("timescale", timescale, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        # Construct body
        body_content = self._serialize.body(video_frame_body, '[VideoFrameBodyItem]')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [204]:
            raise models.APIErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def add_video_frame_stream(
            self, content_type, team_name, review_id, frame_image_zip, frame_metadata, timescale=None, custom_headers=None, raw=False, **operation_config):
        """Use this method to add frames for a video review.Timescale: This
        parameter is a factor which is used to convert the timestamp on a frame
        into milliseconds. Timescale is provided in the output of the Content
        Moderator video media processor on the Azure Media Services
        platform.Timescale in the Video Moderation output is Ticks/Second.

        :param content_type: The content type.
        :type content_type: str
        :param team_name: Your team name.
        :type team_name: str
        :param review_id: Id of the review.
        :type review_id: str
        :param frame_image_zip: Zip file containing frame images.
        :type frame_image_zip: Generator
        :param frame_metadata: Metadata of the frame.
        :type frame_metadata: str
        :param timescale: Timescale of the video .
        :type timescale: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.contentmoderator.models.APIErrorException>`
        """
        # Construct URL
        url = '/contentmoderator/review/v1.0/teams/{teamName}/reviews/{reviewId}/frames'
        path_format_arguments = {
            'baseUrl': self._serialize.url("self.config.base_url", self.config.base_url, 'str', skip_quote=True),
            'teamName': self._serialize.url("team_name", team_name, 'str'),
            'reviewId': self._serialize.url("review_id", review_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if timescale is not None:
            query_parameters['timescale'] = self._serialize.query("timescale", timescale, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'multipart/form-data'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        # Construct form data
        form_data_content = {
            'frameImageZip': frame_image_zip,
            'frameMetadata': frame_metadata,
        }

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send_formdata(
            request, header_parameters, form_data_content, **operation_config)

        if response.status_code not in [204]:
            raise models.APIErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response