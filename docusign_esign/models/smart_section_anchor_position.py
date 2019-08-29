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


class SmartSectionAnchorPosition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, page_number=None, x_position=None, y_position=None):
        """
        SmartSectionAnchorPosition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'page_number': 'int',
            'x_position': 'float',
            'y_position': 'float'
        }

        self.attribute_map = {
            'page_number': 'pageNumber',
            'x_position': 'xPosition',
            'y_position': 'yPosition'
        }

        self._page_number = page_number
        self._x_position = x_position
        self._y_position = y_position

    @property
    def page_number(self):
        """
        Gets the page_number of this SmartSectionAnchorPosition.
        Specifies the page number on which the tab is located.

        :return: The page_number of this SmartSectionAnchorPosition.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """
        Sets the page_number of this SmartSectionAnchorPosition.
        Specifies the page number on which the tab is located.

        :param page_number: The page_number of this SmartSectionAnchorPosition.
        :type: int
        """

        self._page_number = page_number

    @property
    def x_position(self):
        """
        Gets the x_position of this SmartSectionAnchorPosition.
        This indicates the horizontal offset of the object on the page. DocuSign uses 72 DPI when determining position.

        :return: The x_position of this SmartSectionAnchorPosition.
        :rtype: float
        """
        return self._x_position

    @x_position.setter
    def x_position(self, x_position):
        """
        Sets the x_position of this SmartSectionAnchorPosition.
        This indicates the horizontal offset of the object on the page. DocuSign uses 72 DPI when determining position.

        :param x_position: The x_position of this SmartSectionAnchorPosition.
        :type: float
        """

        self._x_position = x_position

    @property
    def y_position(self):
        """
        Gets the y_position of this SmartSectionAnchorPosition.
        This indicates the vertical offset of the object on the page. DocuSign uses 72 DPI when determining position.

        :return: The y_position of this SmartSectionAnchorPosition.
        :rtype: float
        """
        return self._y_position

    @y_position.setter
    def y_position(self, y_position):
        """
        Sets the y_position of this SmartSectionAnchorPosition.
        This indicates the vertical offset of the object on the page. DocuSign uses 72 DPI when determining position.

        :param y_position: The y_position of this SmartSectionAnchorPosition.
        :type: float
        """

        self._y_position = y_position

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
