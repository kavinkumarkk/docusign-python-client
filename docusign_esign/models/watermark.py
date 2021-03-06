# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Watermark(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'display_angle': 'str',
        'enabled': 'str',
        'font': 'str',
        'font_color': 'str',
        'font_size': 'str',
        'id': 'str',
        'image_base64': 'str',
        'transparency': 'str',
        'watermark_text': 'str'
    }

    attribute_map = {
        'display_angle': 'displayAngle',
        'enabled': 'enabled',
        'font': 'font',
        'font_color': 'fontColor',
        'font_size': 'fontSize',
        'id': 'id',
        'image_base64': 'imageBase64',
        'transparency': 'transparency',
        'watermark_text': 'watermarkText'
    }

    def __init__(self, display_angle=None, enabled=None, font=None, font_color=None, font_size=None, id=None, image_base64=None, transparency=None, watermark_text=None):  # noqa: E501
        """Watermark - a model defined in Swagger"""  # noqa: E501

        self._display_angle = None
        self._enabled = None
        self._font = None
        self._font_color = None
        self._font_size = None
        self._id = None
        self._image_base64 = None
        self._transparency = None
        self._watermark_text = None
        self.discriminator = None

        if display_angle is not None:
            self.display_angle = display_angle
        if enabled is not None:
            self.enabled = enabled
        if font is not None:
            self.font = font
        if font_color is not None:
            self.font_color = font_color
        if font_size is not None:
            self.font_size = font_size
        if id is not None:
            self.id = id
        if image_base64 is not None:
            self.image_base64 = image_base64
        if transparency is not None:
            self.transparency = transparency
        if watermark_text is not None:
            self.watermark_text = watermark_text

    @property
    def display_angle(self):
        """Gets the display_angle of this Watermark.  # noqa: E501

          # noqa: E501

        :return: The display_angle of this Watermark.  # noqa: E501
        :rtype: str
        """
        return self._display_angle

    @display_angle.setter
    def display_angle(self, display_angle):
        """Sets the display_angle of this Watermark.

          # noqa: E501

        :param display_angle: The display_angle of this Watermark.  # noqa: E501
        :type: str
        """

        self._display_angle = display_angle

    @property
    def enabled(self):
        """Gets the enabled of this Watermark.  # noqa: E501

          # noqa: E501

        :return: The enabled of this Watermark.  # noqa: E501
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Watermark.

          # noqa: E501

        :param enabled: The enabled of this Watermark.  # noqa: E501
        :type: str
        """

        self._enabled = enabled

    @property
    def font(self):
        """Gets the font of this Watermark.  # noqa: E501

        The font to be used for the tab value. Supported Fonts: Arial, Arial, ArialNarrow, Calibri, CourierNew, Garamond, Georgia, Helvetica,   LucidaConsole, Tahoma, TimesNewRoman, Trebuchet, Verdana, MSGothic, MSMincho, Default.  # noqa: E501

        :return: The font of this Watermark.  # noqa: E501
        :rtype: str
        """
        return self._font

    @font.setter
    def font(self, font):
        """Sets the font of this Watermark.

        The font to be used for the tab value. Supported Fonts: Arial, Arial, ArialNarrow, Calibri, CourierNew, Garamond, Georgia, Helvetica,   LucidaConsole, Tahoma, TimesNewRoman, Trebuchet, Verdana, MSGothic, MSMincho, Default.  # noqa: E501

        :param font: The font of this Watermark.  # noqa: E501
        :type: str
        """

        self._font = font

    @property
    def font_color(self):
        """Gets the font_color of this Watermark.  # noqa: E501

        The font color used for the information in the tab.  Possible values are: Black, BrightBlue, BrightRed, DarkGreen, DarkRed, Gold, Green, NavyBlue, Purple, or White.  # noqa: E501

        :return: The font_color of this Watermark.  # noqa: E501
        :rtype: str
        """
        return self._font_color

    @font_color.setter
    def font_color(self, font_color):
        """Sets the font_color of this Watermark.

        The font color used for the information in the tab.  Possible values are: Black, BrightBlue, BrightRed, DarkGreen, DarkRed, Gold, Green, NavyBlue, Purple, or White.  # noqa: E501

        :param font_color: The font_color of this Watermark.  # noqa: E501
        :type: str
        """

        self._font_color = font_color

    @property
    def font_size(self):
        """Gets the font_size of this Watermark.  # noqa: E501

        The font size used for the information in the tab.  Possible values are: Size7, Size8, Size9, Size10, Size11, Size12, Size14, Size16, Size18, Size20, Size22, Size24, Size26, Size28, Size36, Size48, or Size72.  # noqa: E501

        :return: The font_size of this Watermark.  # noqa: E501
        :rtype: str
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        """Sets the font_size of this Watermark.

        The font size used for the information in the tab.  Possible values are: Size7, Size8, Size9, Size10, Size11, Size12, Size14, Size16, Size18, Size20, Size22, Size24, Size26, Size28, Size36, Size48, or Size72.  # noqa: E501

        :param font_size: The font_size of this Watermark.  # noqa: E501
        :type: str
        """

        self._font_size = font_size

    @property
    def id(self):
        """Gets the id of this Watermark.  # noqa: E501

          # noqa: E501

        :return: The id of this Watermark.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Watermark.

          # noqa: E501

        :param id: The id of this Watermark.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def image_base64(self):
        """Gets the image_base64 of this Watermark.  # noqa: E501

          # noqa: E501

        :return: The image_base64 of this Watermark.  # noqa: E501
        :rtype: str
        """
        return self._image_base64

    @image_base64.setter
    def image_base64(self, image_base64):
        """Sets the image_base64 of this Watermark.

          # noqa: E501

        :param image_base64: The image_base64 of this Watermark.  # noqa: E501
        :type: str
        """

        self._image_base64 = image_base64

    @property
    def transparency(self):
        """Gets the transparency of this Watermark.  # noqa: E501

          # noqa: E501

        :return: The transparency of this Watermark.  # noqa: E501
        :rtype: str
        """
        return self._transparency

    @transparency.setter
    def transparency(self, transparency):
        """Sets the transparency of this Watermark.

          # noqa: E501

        :param transparency: The transparency of this Watermark.  # noqa: E501
        :type: str
        """

        self._transparency = transparency

    @property
    def watermark_text(self):
        """Gets the watermark_text of this Watermark.  # noqa: E501

          # noqa: E501

        :return: The watermark_text of this Watermark.  # noqa: E501
        :rtype: str
        """
        return self._watermark_text

    @watermark_text.setter
    def watermark_text(self, watermark_text):
        """Sets the watermark_text of this Watermark.

          # noqa: E501

        :param watermark_text: The watermark_text of this Watermark.  # noqa: E501
        :type: str
        """

        self._watermark_text = watermark_text

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Watermark, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Watermark):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
