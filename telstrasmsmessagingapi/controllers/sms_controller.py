# -*- coding: utf-8 -*-

"""
    telstrasmsmessagingapi.controllers.sms_controller

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2
from ..models.inbound_poll_response import InboundPollResponse
from ..models.message_sent_response import MessageSentResponse
from ..models.outbound_poll_response import OutboundPollResponse
from ..exceptions.error_error_error_exception import ErrorErrorErrorException

class SMSController(BaseController):

    """A Controller to access Endpoints in the telstrasmsmessagingapi API."""


    def retrieve_messages(self):
        """Does a GET request to /messages/sms.

        Retrieve Messages

        Returns:
            list of InboundPollResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/messages/sms'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorErrorErrorException('Invalid or missing request parameters', _context)
        elif _context.response.status_code == 401:
            raise ErrorErrorErrorException('Invalid or no credentials passed in the request', _context)
        elif _context.response.status_code == 403:
            raise ErrorErrorErrorException('Authorization credentials passed and accepted but account does not have permission', _context)
        elif _context.response.status_code == 404:
            raise ErrorErrorErrorException('The requested URI does not exist', _context)
        elif _context.response.status_code == 405:
            raise ErrorErrorErrorException('The requested resource does not support the supplied verb', _context)
        elif _context.response.status_code == 415:
            raise ErrorErrorErrorException('API does not support the requested content type', _context)
        elif _context.response.status_code == 422:
            raise ErrorErrorErrorException('The request is formed correctly, but due to some condition the request cannot be processed e.g. email is required and it is not provided in the request', _context)
        elif _context.response.status_code == 501:
            raise ErrorErrorErrorException('The HTTP method being used has not yet been implemented for the requested resource', _context)
        elif _context.response.status_code == 503:
            raise ErrorErrorErrorException('The service requested is currently unavailable', _context)
        elif (_context.response.status_code < 200) or (_context.response.status_code > 208): 
            raise ErrorErrorErrorException('An internal error occurred when processing the request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, InboundPollResponse.from_dictionary)

    def create_send_message(self,
                            payload):
        """Does a POST request to /messages/sms.

        Send Message

        Args:
            payload (SendSMSRequest): A JSON or XML payload containing the
                recipient's phone number and text message. The recipient
                number should be in the format '04xxxxxxxx' where x is a
                digit

        Returns:
            list of MessageSentResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/messages/sms'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(payload))
        OAuth2.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorErrorErrorException('Invalid or missing request parameters', _context)
        elif _context.response.status_code == 401:
            raise ErrorErrorErrorException('Invalid or no credentials passed in the request', _context)
        elif _context.response.status_code == 403:
            raise ErrorErrorErrorException('Authorization credentials passed and accepted but account does not have permission', _context)
        elif _context.response.status_code == 404:
            raise ErrorErrorErrorException('The requested URI does not exist', _context)
        elif _context.response.status_code == 405:
            raise ErrorErrorErrorException('The requested resource does not support the supplied verb', _context)
        elif _context.response.status_code == 415:
            raise ErrorErrorErrorException('API does not support the requested content type', _context)
        elif _context.response.status_code == 422:
            raise ErrorErrorErrorException('The request is formed correctly, but due to some condition the request cannot be processed e.g. email is required and it is not provided in the request', _context)
        elif _context.response.status_code == 501:
            raise ErrorErrorErrorException('The HTTP method being used has not yet been implemented for the requested resource', _context)
        elif _context.response.status_code == 503:
            raise ErrorErrorErrorException('The service requested is currently unavailable', _context)
        elif (_context.response.status_code < 200) or (_context.response.status_code > 208): 
            raise ErrorErrorErrorException('An internal error occurred when processing the request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, MessageSentResponse.from_dictionary)

    def get_message_status(self,
                           message_id):
        """Does a GET request to /messages/sms/{messageId}/status.

        Get Message Status

        Args:
            message_id (string): Unique identifier of a message - it is the
                value returned from a previous POST call to
                https://api.telstra.com/v2/messages/sms

        Returns:
            OutboundPollResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/messages/sms/{messageId}/status'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'messageId': message_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorErrorErrorException('Invalid or missing request parameters', _context)
        elif _context.response.status_code == 401:
            raise ErrorErrorErrorException('Invalid or no credentials passed in the request', _context)
        elif _context.response.status_code == 403:
            raise ErrorErrorErrorException('Authorization credentials passed and accepted but account does not have permission', _context)
        elif _context.response.status_code == 404:
            raise ErrorErrorErrorException('The requested URI does not exist', _context)
        elif _context.response.status_code == 405:
            raise ErrorErrorErrorException('The requested resource does not support the supplied verb', _context)
        elif _context.response.status_code == 415:
            raise ErrorErrorErrorException('API does not support the requested content type', _context)
        elif _context.response.status_code == 422:
            raise ErrorErrorErrorException('The request is formed correctly, but due to some condition the request cannot be processed e.g. email is required and it is not provided in the request', _context)
        elif _context.response.status_code == 501:
            raise ErrorErrorErrorException('The HTTP method being used has not yet been implemented for the requested resource', _context)
        elif _context.response.status_code == 503:
            raise ErrorErrorErrorException('The service requested is currently unavailable', _context)
        elif (_context.response.status_code < 200) or (_context.response.status_code > 208): 
            raise ErrorErrorErrorException('An internal error occurred when processing the request', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, OutboundPollResponse.from_dictionary)
