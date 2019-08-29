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


class DisplayApplianceEnvelope(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, add_demo_stamp=None, allow_multiple_attachments=None, burn_default_tab_data=None, convert_pdf_fields=None, envelope_id=None, envelope_type=None, include_sigs_before_complete=None, is_concat_mode=None, is_envelope_id_stamping_enabled=None, pdf_form_conversion_font_scale100=None, should_flatten=None, show_envelope_changes=None, sign_online=None, status=None, user_id=None):
        """
        DisplayApplianceEnvelope - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'add_demo_stamp': 'bool',
            'allow_multiple_attachments': 'bool',
            'burn_default_tab_data': 'bool',
            'convert_pdf_fields': 'bool',
            'envelope_id': 'str',
            'envelope_type': 'str',
            'include_sigs_before_complete': 'bool',
            'is_concat_mode': 'bool',
            'is_envelope_id_stamping_enabled': 'bool',
            'pdf_form_conversion_font_scale100': 'bool',
            'should_flatten': 'bool',
            'show_envelope_changes': 'bool',
            'sign_online': 'bool',
            'status': 'str',
            'user_id': 'str'
        }

        self.attribute_map = {
            'add_demo_stamp': 'addDemoStamp',
            'allow_multiple_attachments': 'allowMultipleAttachments',
            'burn_default_tab_data': 'burnDefaultTabData',
            'convert_pdf_fields': 'convertPdfFields',
            'envelope_id': 'envelopeId',
            'envelope_type': 'envelopeType',
            'include_sigs_before_complete': 'includeSigsBeforeComplete',
            'is_concat_mode': 'isConcatMode',
            'is_envelope_id_stamping_enabled': 'isEnvelopeIDStampingEnabled',
            'pdf_form_conversion_font_scale100': 'pdfFormConversionFontScale100',
            'should_flatten': 'shouldFlatten',
            'show_envelope_changes': 'showEnvelopeChanges',
            'sign_online': 'signOnline',
            'status': 'status',
            'user_id': 'userId'
        }

        self._add_demo_stamp = add_demo_stamp
        self._allow_multiple_attachments = allow_multiple_attachments
        self._burn_default_tab_data = burn_default_tab_data
        self._convert_pdf_fields = convert_pdf_fields
        self._envelope_id = envelope_id
        self._envelope_type = envelope_type
        self._include_sigs_before_complete = include_sigs_before_complete
        self._is_concat_mode = is_concat_mode
        self._is_envelope_id_stamping_enabled = is_envelope_id_stamping_enabled
        self._pdf_form_conversion_font_scale100 = pdf_form_conversion_font_scale100
        self._should_flatten = should_flatten
        self._show_envelope_changes = show_envelope_changes
        self._sign_online = sign_online
        self._status = status
        self._user_id = user_id

    @property
    def add_demo_stamp(self):
        """
        Gets the add_demo_stamp of this DisplayApplianceEnvelope.
        

        :return: The add_demo_stamp of this DisplayApplianceEnvelope.
        :rtype: bool
        """
        return self._add_demo_stamp

    @add_demo_stamp.setter
    def add_demo_stamp(self, add_demo_stamp):
        """
        Sets the add_demo_stamp of this DisplayApplianceEnvelope.
        

        :param add_demo_stamp: The add_demo_stamp of this DisplayApplianceEnvelope.
        :type: bool
        """

        self._add_demo_stamp = add_demo_stamp

    @property
    def allow_multiple_attachments(self):
        """
        Gets the allow_multiple_attachments of this DisplayApplianceEnvelope.
        

        :return: The allow_multiple_attachments of this DisplayApplianceEnvelope.
        :rtype: bool
        """
        return self._allow_multiple_attachments

    @allow_multiple_attachments.setter
    def allow_multiple_attachments(self, allow_multiple_attachments):
        """
        Sets the allow_multiple_attachments of this DisplayApplianceEnvelope.
        

        :param allow_multiple_attachments: The allow_multiple_attachments of this DisplayApplianceEnvelope.
        :type: bool
        """

        self._allow_multiple_attachments = allow_multiple_attachments

    @property
    def burn_default_tab_data(self):
        """
        Gets the burn_default_tab_data of this DisplayApplianceEnvelope.
        

        :return: The burn_default_tab_data of this DisplayApplianceEnvelope.
        :rtype: bool
        """
        return self._burn_default_tab_data

    @burn_default_tab_data.setter
    def burn_default_tab_data(self, burn_default_tab_data):
        """
        Sets the burn_default_tab_data of this DisplayApplianceEnvelope.
        

        :param burn_default_tab_data: The burn_default_tab_data of this DisplayApplianceEnvelope.
        :type: bool
        """

        self._burn_default_tab_data = burn_default_tab_data

    @property
    def convert_pdf_fields(self):
        """
        Gets the convert_pdf_fields of this DisplayApplianceEnvelope.
        

        :return: The convert_pdf_fields of this DisplayApplianceEnvelope.
        :rtype: bool
        """
        return self._convert_pdf_fields

    @convert_pdf_fields.setter
    def convert_pdf_fields(self, convert_pdf_fields):
        """
        Sets the convert_pdf_fields of this DisplayApplianceEnvelope.
        

        :param convert_pdf_fields: The convert_pdf_fields of this DisplayApplianceEnvelope.
        :type: bool
        """

        self._convert_pdf_fields = convert_pdf_fields

    @property
    def envelope_id(self):
        """
        Gets the envelope_id of this DisplayApplianceEnvelope.
        The envelope ID of the envelope status that failed to post.

        :return: The envelope_id of this DisplayApplianceEnvelope.
        :rtype: str
        """
        return self._envelope_id

    @envelope_id.setter
    def envelope_id(self, envelope_id):
        """
        Sets the envelope_id of this DisplayApplianceEnvelope.
        The envelope ID of the envelope status that failed to post.

        :param envelope_id: The envelope_id of this DisplayApplianceEnvelope.
        :type: str
        """

        self._envelope_id = envelope_id

    @property
    def envelope_type(self):
        """
        Gets the envelope_type of this DisplayApplianceEnvelope.
        

        :return: The envelope_type of this DisplayApplianceEnvelope.
        :rtype: str
        """
        return self._envelope_type

    @envelope_type.setter
    def envelope_type(self, envelope_type):
        """
        Sets the envelope_type of this DisplayApplianceEnvelope.
        

        :param envelope_type: The envelope_type of this DisplayApplianceEnvelope.
        :type: str
        """

        self._envelope_type = envelope_type

    @property
    def include_sigs_before_complete(self):
        """
        Gets the include_sigs_before_complete of this DisplayApplianceEnvelope.
        

        :return: The include_sigs_before_complete of this DisplayApplianceEnvelope.
        :rtype: bool
        """
        return self._include_sigs_before_complete

    @include_sigs_before_complete.setter
    def include_sigs_before_complete(self, include_sigs_before_complete):
        """
        Sets the include_sigs_before_complete of this DisplayApplianceEnvelope.
        

        :param include_sigs_before_complete: The include_sigs_before_complete of this DisplayApplianceEnvelope.
        :type: bool
        """

        self._include_sigs_before_complete = include_sigs_before_complete

    @property
    def is_concat_mode(self):
        """
        Gets the is_concat_mode of this DisplayApplianceEnvelope.
        

        :return: The is_concat_mode of this DisplayApplianceEnvelope.
        :rtype: bool
        """
        return self._is_concat_mode

    @is_concat_mode.setter
    def is_concat_mode(self, is_concat_mode):
        """
        Sets the is_concat_mode of this DisplayApplianceEnvelope.
        

        :param is_concat_mode: The is_concat_mode of this DisplayApplianceEnvelope.
        :type: bool
        """

        self._is_concat_mode = is_concat_mode

    @property
    def is_envelope_id_stamping_enabled(self):
        """
        Gets the is_envelope_id_stamping_enabled of this DisplayApplianceEnvelope.
        

        :return: The is_envelope_id_stamping_enabled of this DisplayApplianceEnvelope.
        :rtype: bool
        """
        return self._is_envelope_id_stamping_enabled

    @is_envelope_id_stamping_enabled.setter
    def is_envelope_id_stamping_enabled(self, is_envelope_id_stamping_enabled):
        """
        Sets the is_envelope_id_stamping_enabled of this DisplayApplianceEnvelope.
        

        :param is_envelope_id_stamping_enabled: The is_envelope_id_stamping_enabled of this DisplayApplianceEnvelope.
        :type: bool
        """

        self._is_envelope_id_stamping_enabled = is_envelope_id_stamping_enabled

    @property
    def pdf_form_conversion_font_scale100(self):
        """
        Gets the pdf_form_conversion_font_scale100 of this DisplayApplianceEnvelope.
        

        :return: The pdf_form_conversion_font_scale100 of this DisplayApplianceEnvelope.
        :rtype: bool
        """
        return self._pdf_form_conversion_font_scale100

    @pdf_form_conversion_font_scale100.setter
    def pdf_form_conversion_font_scale100(self, pdf_form_conversion_font_scale100):
        """
        Sets the pdf_form_conversion_font_scale100 of this DisplayApplianceEnvelope.
        

        :param pdf_form_conversion_font_scale100: The pdf_form_conversion_font_scale100 of this DisplayApplianceEnvelope.
        :type: bool
        """

        self._pdf_form_conversion_font_scale100 = pdf_form_conversion_font_scale100

    @property
    def should_flatten(self):
        """
        Gets the should_flatten of this DisplayApplianceEnvelope.
        

        :return: The should_flatten of this DisplayApplianceEnvelope.
        :rtype: bool
        """
        return self._should_flatten

    @should_flatten.setter
    def should_flatten(self, should_flatten):
        """
        Sets the should_flatten of this DisplayApplianceEnvelope.
        

        :param should_flatten: The should_flatten of this DisplayApplianceEnvelope.
        :type: bool
        """

        self._should_flatten = should_flatten

    @property
    def show_envelope_changes(self):
        """
        Gets the show_envelope_changes of this DisplayApplianceEnvelope.
        

        :return: The show_envelope_changes of this DisplayApplianceEnvelope.
        :rtype: bool
        """
        return self._show_envelope_changes

    @show_envelope_changes.setter
    def show_envelope_changes(self, show_envelope_changes):
        """
        Sets the show_envelope_changes of this DisplayApplianceEnvelope.
        

        :param show_envelope_changes: The show_envelope_changes of this DisplayApplianceEnvelope.
        :type: bool
        """

        self._show_envelope_changes = show_envelope_changes

    @property
    def sign_online(self):
        """
        Gets the sign_online of this DisplayApplianceEnvelope.
        

        :return: The sign_online of this DisplayApplianceEnvelope.
        :rtype: bool
        """
        return self._sign_online

    @sign_online.setter
    def sign_online(self, sign_online):
        """
        Sets the sign_online of this DisplayApplianceEnvelope.
        

        :param sign_online: The sign_online of this DisplayApplianceEnvelope.
        :type: bool
        """

        self._sign_online = sign_online

    @property
    def status(self):
        """
        Gets the status of this DisplayApplianceEnvelope.
        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.

        :return: The status of this DisplayApplianceEnvelope.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this DisplayApplianceEnvelope.
        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.

        :param status: The status of this DisplayApplianceEnvelope.
        :type: str
        """

        self._status = status

    @property
    def user_id(self):
        """
        Gets the user_id of this DisplayApplianceEnvelope.
        

        :return: The user_id of this DisplayApplianceEnvelope.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this DisplayApplianceEnvelope.
        

        :param user_id: The user_id of this DisplayApplianceEnvelope.
        :type: str
        """

        self._user_id = user_id

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
