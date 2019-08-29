# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RecipientNamesResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, multiple_users=None, recipient_names=None, reserved_recipient_email=None):
        """
        RecipientNamesResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'multiple_users': 'str',
            'recipient_names': 'list[str]',
            'reserved_recipient_email': 'str'
        }

        self.attribute_map = {
            'multiple_users': 'multipleUsers',
            'recipient_names': 'recipientNames',
            'reserved_recipient_email': 'reservedRecipientEmail'
        }

        self._multiple_users = multiple_users
        self._recipient_names = recipient_names
        self._reserved_recipient_email = reserved_recipient_email

    @property
    def multiple_users(self):
        """
        Gets the multiple_users of this RecipientNamesResponse.
        Indicates whether email address is used by more than one user.

        :return: The multiple_users of this RecipientNamesResponse.
        :rtype: str
        """
        return self._multiple_users

    @multiple_users.setter
    def multiple_users(self, multiple_users):
        """
        Sets the multiple_users of this RecipientNamesResponse.
        Indicates whether email address is used by more than one user.

        :param multiple_users: The multiple_users of this RecipientNamesResponse.
        :type: str
        """

        self._multiple_users = multiple_users

    @property
    def recipient_names(self):
        """
        Gets the recipient_names of this RecipientNamesResponse.
        

        :return: The recipient_names of this RecipientNamesResponse.
        :rtype: list[str]
        """
        return self._recipient_names

    @recipient_names.setter
    def recipient_names(self, recipient_names):
        """
        Sets the recipient_names of this RecipientNamesResponse.
        

        :param recipient_names: The recipient_names of this RecipientNamesResponse.
        :type: list[str]
        """

        self._recipient_names = recipient_names

    @property
    def reserved_recipient_email(self):
        """
        Gets the reserved_recipient_email of this RecipientNamesResponse.
        

        :return: The reserved_recipient_email of this RecipientNamesResponse.
        :rtype: str
        """
        return self._reserved_recipient_email

    @reserved_recipient_email.setter
    def reserved_recipient_email(self, reserved_recipient_email):
        """
        Sets the reserved_recipient_email of this RecipientNamesResponse.
        

        :param reserved_recipient_email: The reserved_recipient_email of this RecipientNamesResponse.
        :type: str
        """

        self._reserved_recipient_email = reserved_recipient_email

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
