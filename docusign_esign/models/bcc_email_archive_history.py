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


class BccEmailArchiveHistory(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, account_id=None, action=None, email=None, modified=None, modified_by=None, status=None):
        """
        BccEmailArchiveHistory - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'account_id': 'str',
            'action': 'str',
            'email': 'str',
            'modified': 'str',
            'modified_by': 'UserInfo',
            'status': 'str'
        }

        self.attribute_map = {
            'account_id': 'accountId',
            'action': 'action',
            'email': 'email',
            'modified': 'modified',
            'modified_by': 'modifiedBy',
            'status': 'status'
        }

        self._account_id = account_id
        self._action = action
        self._email = email
        self._modified = modified
        self._modified_by = modified_by
        self._status = status

    @property
    def account_id(self):
        """
        Gets the account_id of this BccEmailArchiveHistory.
        The account ID associated with the envelope.

        :return: The account_id of this BccEmailArchiveHistory.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this BccEmailArchiveHistory.
        The account ID associated with the envelope.

        :param account_id: The account_id of this BccEmailArchiveHistory.
        :type: str
        """

        self._account_id = account_id

    @property
    def action(self):
        """
        Gets the action of this BccEmailArchiveHistory.
        

        :return: The action of this BccEmailArchiveHistory.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this BccEmailArchiveHistory.
        

        :param action: The action of this BccEmailArchiveHistory.
        :type: str
        """

        self._action = action

    @property
    def email(self):
        """
        Gets the email of this BccEmailArchiveHistory.
        

        :return: The email of this BccEmailArchiveHistory.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this BccEmailArchiveHistory.
        

        :param email: The email of this BccEmailArchiveHistory.
        :type: str
        """

        self._email = email

    @property
    def modified(self):
        """
        Gets the modified of this BccEmailArchiveHistory.
        

        :return: The modified of this BccEmailArchiveHistory.
        :rtype: str
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """
        Sets the modified of this BccEmailArchiveHistory.
        

        :param modified: The modified of this BccEmailArchiveHistory.
        :type: str
        """

        self._modified = modified

    @property
    def modified_by(self):
        """
        Gets the modified_by of this BccEmailArchiveHistory.

        :return: The modified_by of this BccEmailArchiveHistory.
        :rtype: UserInfo
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """
        Sets the modified_by of this BccEmailArchiveHistory.

        :param modified_by: The modified_by of this BccEmailArchiveHistory.
        :type: UserInfo
        """

        self._modified_by = modified_by

    @property
    def status(self):
        """
        Gets the status of this BccEmailArchiveHistory.
        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.

        :return: The status of this BccEmailArchiveHistory.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this BccEmailArchiveHistory.
        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.

        :param status: The status of this BccEmailArchiveHistory.
        :type: str
        """

        self._status = status

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
