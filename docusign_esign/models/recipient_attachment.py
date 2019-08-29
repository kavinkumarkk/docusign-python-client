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


class RecipientAttachment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, attachment_id=None, attachment_type=None, data=None, label=None, name=None, remote_url=None):
        """
        RecipientAttachment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'attachment_id': 'str',
            'attachment_type': 'str',
            'data': 'str',
            'label': 'str',
            'name': 'str',
            'remote_url': 'str'
        }

        self.attribute_map = {
            'attachment_id': 'attachmentId',
            'attachment_type': 'attachmentType',
            'data': 'data',
            'label': 'label',
            'name': 'name',
            'remote_url': 'remoteUrl'
        }

        self._attachment_id = attachment_id
        self._attachment_type = attachment_type
        self._data = data
        self._label = label
        self._name = name
        self._remote_url = remote_url

    @property
    def attachment_id(self):
        """
        Gets the attachment_id of this RecipientAttachment.
        

        :return: The attachment_id of this RecipientAttachment.
        :rtype: str
        """
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        """
        Sets the attachment_id of this RecipientAttachment.
        

        :param attachment_id: The attachment_id of this RecipientAttachment.
        :type: str
        """

        self._attachment_id = attachment_id

    @property
    def attachment_type(self):
        """
        Gets the attachment_type of this RecipientAttachment.
        

        :return: The attachment_type of this RecipientAttachment.
        :rtype: str
        """
        return self._attachment_type

    @attachment_type.setter
    def attachment_type(self, attachment_type):
        """
        Sets the attachment_type of this RecipientAttachment.
        

        :param attachment_type: The attachment_type of this RecipientAttachment.
        :type: str
        """

        self._attachment_type = attachment_type

    @property
    def data(self):
        """
        Gets the data of this RecipientAttachment.
        

        :return: The data of this RecipientAttachment.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this RecipientAttachment.
        

        :param data: The data of this RecipientAttachment.
        :type: str
        """

        self._data = data

    @property
    def label(self):
        """
        Gets the label of this RecipientAttachment.
        

        :return: The label of this RecipientAttachment.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this RecipientAttachment.
        

        :param label: The label of this RecipientAttachment.
        :type: str
        """

        self._label = label

    @property
    def name(self):
        """
        Gets the name of this RecipientAttachment.
        

        :return: The name of this RecipientAttachment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RecipientAttachment.
        

        :param name: The name of this RecipientAttachment.
        :type: str
        """

        self._name = name

    @property
    def remote_url(self):
        """
        Gets the remote_url of this RecipientAttachment.
        

        :return: The remote_url of this RecipientAttachment.
        :rtype: str
        """
        return self._remote_url

    @remote_url.setter
    def remote_url(self, remote_url):
        """
        Sets the remote_url of this RecipientAttachment.
        

        :param remote_url: The remote_url of this RecipientAttachment.
        :type: str
        """

        self._remote_url = remote_url

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
