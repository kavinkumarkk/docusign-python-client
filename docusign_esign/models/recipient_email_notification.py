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


class RecipientEmailNotification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, email_body=None, email_body_metadata=None, email_subject=None, email_subject_metadata=None, supported_language=None, supported_language_metadata=None):
        """
        RecipientEmailNotification - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'email_body': 'str',
            'email_body_metadata': 'PropertyMetadata',
            'email_subject': 'str',
            'email_subject_metadata': 'PropertyMetadata',
            'supported_language': 'str',
            'supported_language_metadata': 'PropertyMetadata'
        }

        self.attribute_map = {
            'email_body': 'emailBody',
            'email_body_metadata': 'emailBodyMetadata',
            'email_subject': 'emailSubject',
            'email_subject_metadata': 'emailSubjectMetadata',
            'supported_language': 'supportedLanguage',
            'supported_language_metadata': 'supportedLanguageMetadata'
        }

        self._email_body = email_body
        self._email_body_metadata = email_body_metadata
        self._email_subject = email_subject
        self._email_subject_metadata = email_subject_metadata
        self._supported_language = supported_language
        self._supported_language_metadata = supported_language_metadata

    @property
    def email_body(self):
        """
        Gets the email_body of this RecipientEmailNotification.
        Specifies the email body of the message sent to the recipient.   Maximum length: 10000 characters. 

        :return: The email_body of this RecipientEmailNotification.
        :rtype: str
        """
        return self._email_body

    @email_body.setter
    def email_body(self, email_body):
        """
        Sets the email_body of this RecipientEmailNotification.
        Specifies the email body of the message sent to the recipient.   Maximum length: 10000 characters. 

        :param email_body: The email_body of this RecipientEmailNotification.
        :type: str
        """

        self._email_body = email_body

    @property
    def email_body_metadata(self):
        """
        Gets the email_body_metadata of this RecipientEmailNotification.

        :return: The email_body_metadata of this RecipientEmailNotification.
        :rtype: PropertyMetadata
        """
        return self._email_body_metadata

    @email_body_metadata.setter
    def email_body_metadata(self, email_body_metadata):
        """
        Sets the email_body_metadata of this RecipientEmailNotification.

        :param email_body_metadata: The email_body_metadata of this RecipientEmailNotification.
        :type: PropertyMetadata
        """

        self._email_body_metadata = email_body_metadata

    @property
    def email_subject(self):
        """
        Gets the email_subject of this RecipientEmailNotification.
        Specifies the subject of the email that is sent to all recipients.  See [ML:Template Email Subject Merge Fields] for information about adding merge field information to the email subject.

        :return: The email_subject of this RecipientEmailNotification.
        :rtype: str
        """
        return self._email_subject

    @email_subject.setter
    def email_subject(self, email_subject):
        """
        Sets the email_subject of this RecipientEmailNotification.
        Specifies the subject of the email that is sent to all recipients.  See [ML:Template Email Subject Merge Fields] for information about adding merge field information to the email subject.

        :param email_subject: The email_subject of this RecipientEmailNotification.
        :type: str
        """

        self._email_subject = email_subject

    @property
    def email_subject_metadata(self):
        """
        Gets the email_subject_metadata of this RecipientEmailNotification.

        :return: The email_subject_metadata of this RecipientEmailNotification.
        :rtype: PropertyMetadata
        """
        return self._email_subject_metadata

    @email_subject_metadata.setter
    def email_subject_metadata(self, email_subject_metadata):
        """
        Sets the email_subject_metadata of this RecipientEmailNotification.

        :param email_subject_metadata: The email_subject_metadata of this RecipientEmailNotification.
        :type: PropertyMetadata
        """

        self._email_subject_metadata = email_subject_metadata

    @property
    def supported_language(self):
        """
        Gets the supported_language of this RecipientEmailNotification.
        A simple type enumeration of the language used. The supported languages, with the language value shown in parenthesis, are: Arabic (ar), Bahasa Indonesia (id), Bahasa Melayu (ms) Bulgarian (bg), Czech (cs), Chinese Simplified (zh_CN), Chinese Traditional (zh_TW), Croatian (hr), Danish (da), Dutch (nl), English US (en), English UK (en_GB), Estonian (et), Farsi (fa), Finnish (fi), French (fr), French Canada (fr_CA), German (de), Greek (el), Hebrew (he), Hindi (hi), Hungarian (hu), Italian (it), Japanese (ja), Korean (ko), Latvian (lv), Lithuanian (lt), Norwegian (no), Polish (pl), Portuguese (pt), Portuguese Brazil (pt_BR), Romanian (ro),Russian (ru), Serbian (sr), Slovak (sk), Slovenian (sl), Spanish (es),Spanish Latin America (es_MX), Swedish (sv), Thai (th), Turkish (tr), Ukrainian (uk), and Vietnamese (vi).

        :return: The supported_language of this RecipientEmailNotification.
        :rtype: str
        """
        return self._supported_language

    @supported_language.setter
    def supported_language(self, supported_language):
        """
        Sets the supported_language of this RecipientEmailNotification.
        A simple type enumeration of the language used. The supported languages, with the language value shown in parenthesis, are: Arabic (ar), Bahasa Indonesia (id), Bahasa Melayu (ms) Bulgarian (bg), Czech (cs), Chinese Simplified (zh_CN), Chinese Traditional (zh_TW), Croatian (hr), Danish (da), Dutch (nl), English US (en), English UK (en_GB), Estonian (et), Farsi (fa), Finnish (fi), French (fr), French Canada (fr_CA), German (de), Greek (el), Hebrew (he), Hindi (hi), Hungarian (hu), Italian (it), Japanese (ja), Korean (ko), Latvian (lv), Lithuanian (lt), Norwegian (no), Polish (pl), Portuguese (pt), Portuguese Brazil (pt_BR), Romanian (ro),Russian (ru), Serbian (sr), Slovak (sk), Slovenian (sl), Spanish (es),Spanish Latin America (es_MX), Swedish (sv), Thai (th), Turkish (tr), Ukrainian (uk), and Vietnamese (vi).

        :param supported_language: The supported_language of this RecipientEmailNotification.
        :type: str
        """

        self._supported_language = supported_language

    @property
    def supported_language_metadata(self):
        """
        Gets the supported_language_metadata of this RecipientEmailNotification.

        :return: The supported_language_metadata of this RecipientEmailNotification.
        :rtype: PropertyMetadata
        """
        return self._supported_language_metadata

    @supported_language_metadata.setter
    def supported_language_metadata(self, supported_language_metadata):
        """
        Sets the supported_language_metadata of this RecipientEmailNotification.

        :param supported_language_metadata: The supported_language_metadata of this RecipientEmailNotification.
        :type: PropertyMetadata
        """

        self._supported_language_metadata = supported_language_metadata

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
