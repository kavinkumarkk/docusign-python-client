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


class ConsumerDisclosure(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, account_esign_id=None, allow_cd_withdraw=None, allow_cd_withdraw_metadata=None, change_email=None, change_email_other=None, company_name=None, company_phone=None, copy_cost_per_page=None, copy_fee_collection_method=None, copy_request_email=None, custom=None, enable_esign=None, esign_agreement=None, esign_text=None, language_code=None, must_agree_to_esign=None, pdf_id=None, use_brand=None, use_consumer_disclosure_within_account=None, use_consumer_disclosure_within_account_metadata=None, withdraw_address_line1=None, withdraw_address_line2=None, withdraw_by_email=None, withdraw_by_mail=None, withdraw_by_phone=None, withdraw_city=None, withdraw_consequences=None, withdraw_email=None, withdraw_other=None, withdraw_phone=None, withdraw_postal_code=None, withdraw_state=None):
        """
        ConsumerDisclosure - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'account_esign_id': 'str',
            'allow_cd_withdraw': 'str',
            'allow_cd_withdraw_metadata': 'SettingsMetadata',
            'change_email': 'str',
            'change_email_other': 'str',
            'company_name': 'str',
            'company_phone': 'str',
            'copy_cost_per_page': 'str',
            'copy_fee_collection_method': 'str',
            'copy_request_email': 'str',
            'custom': 'str',
            'enable_esign': 'str',
            'esign_agreement': 'str',
            'esign_text': 'str',
            'language_code': 'str',
            'must_agree_to_esign': 'str',
            'pdf_id': 'str',
            'use_brand': 'str',
            'use_consumer_disclosure_within_account': 'str',
            'use_consumer_disclosure_within_account_metadata': 'SettingsMetadata',
            'withdraw_address_line1': 'str',
            'withdraw_address_line2': 'str',
            'withdraw_by_email': 'str',
            'withdraw_by_mail': 'str',
            'withdraw_by_phone': 'str',
            'withdraw_city': 'str',
            'withdraw_consequences': 'str',
            'withdraw_email': 'str',
            'withdraw_other': 'str',
            'withdraw_phone': 'str',
            'withdraw_postal_code': 'str',
            'withdraw_state': 'str'
        }

        self.attribute_map = {
            'account_esign_id': 'accountEsignId',
            'allow_cd_withdraw': 'allowCDWithdraw',
            'allow_cd_withdraw_metadata': 'allowCDWithdrawMetadata',
            'change_email': 'changeEmail',
            'change_email_other': 'changeEmailOther',
            'company_name': 'companyName',
            'company_phone': 'companyPhone',
            'copy_cost_per_page': 'copyCostPerPage',
            'copy_fee_collection_method': 'copyFeeCollectionMethod',
            'copy_request_email': 'copyRequestEmail',
            'custom': 'custom',
            'enable_esign': 'enableEsign',
            'esign_agreement': 'esignAgreement',
            'esign_text': 'esignText',
            'language_code': 'languageCode',
            'must_agree_to_esign': 'mustAgreeToEsign',
            'pdf_id': 'pdfId',
            'use_brand': 'useBrand',
            'use_consumer_disclosure_within_account': 'useConsumerDisclosureWithinAccount',
            'use_consumer_disclosure_within_account_metadata': 'useConsumerDisclosureWithinAccountMetadata',
            'withdraw_address_line1': 'withdrawAddressLine1',
            'withdraw_address_line2': 'withdrawAddressLine2',
            'withdraw_by_email': 'withdrawByEmail',
            'withdraw_by_mail': 'withdrawByMail',
            'withdraw_by_phone': 'withdrawByPhone',
            'withdraw_city': 'withdrawCity',
            'withdraw_consequences': 'withdrawConsequences',
            'withdraw_email': 'withdrawEmail',
            'withdraw_other': 'withdrawOther',
            'withdraw_phone': 'withdrawPhone',
            'withdraw_postal_code': 'withdrawPostalCode',
            'withdraw_state': 'withdrawState'
        }

        self._account_esign_id = account_esign_id
        self._allow_cd_withdraw = allow_cd_withdraw
        self._allow_cd_withdraw_metadata = allow_cd_withdraw_metadata
        self._change_email = change_email
        self._change_email_other = change_email_other
        self._company_name = company_name
        self._company_phone = company_phone
        self._copy_cost_per_page = copy_cost_per_page
        self._copy_fee_collection_method = copy_fee_collection_method
        self._copy_request_email = copy_request_email
        self._custom = custom
        self._enable_esign = enable_esign
        self._esign_agreement = esign_agreement
        self._esign_text = esign_text
        self._language_code = language_code
        self._must_agree_to_esign = must_agree_to_esign
        self._pdf_id = pdf_id
        self._use_brand = use_brand
        self._use_consumer_disclosure_within_account = use_consumer_disclosure_within_account
        self._use_consumer_disclosure_within_account_metadata = use_consumer_disclosure_within_account_metadata
        self._withdraw_address_line1 = withdraw_address_line1
        self._withdraw_address_line2 = withdraw_address_line2
        self._withdraw_by_email = withdraw_by_email
        self._withdraw_by_mail = withdraw_by_mail
        self._withdraw_by_phone = withdraw_by_phone
        self._withdraw_city = withdraw_city
        self._withdraw_consequences = withdraw_consequences
        self._withdraw_email = withdraw_email
        self._withdraw_other = withdraw_other
        self._withdraw_phone = withdraw_phone
        self._withdraw_postal_code = withdraw_postal_code
        self._withdraw_state = withdraw_state

    @property
    def account_esign_id(self):
        """
        Gets the account_esign_id of this ConsumerDisclosure.
        A GUID identifying the account associated with the consumer disclosure

        :return: The account_esign_id of this ConsumerDisclosure.
        :rtype: str
        """
        return self._account_esign_id

    @account_esign_id.setter
    def account_esign_id(self, account_esign_id):
        """
        Sets the account_esign_id of this ConsumerDisclosure.
        A GUID identifying the account associated with the consumer disclosure

        :param account_esign_id: The account_esign_id of this ConsumerDisclosure.
        :type: str
        """

        self._account_esign_id = account_esign_id

    @property
    def allow_cd_withdraw(self):
        """
        Gets the allow_cd_withdraw of this ConsumerDisclosure.
        Indicates whether the customer can withdraw their acceptance of the consumer disclosure.

        :return: The allow_cd_withdraw of this ConsumerDisclosure.
        :rtype: str
        """
        return self._allow_cd_withdraw

    @allow_cd_withdraw.setter
    def allow_cd_withdraw(self, allow_cd_withdraw):
        """
        Sets the allow_cd_withdraw of this ConsumerDisclosure.
        Indicates whether the customer can withdraw their acceptance of the consumer disclosure.

        :param allow_cd_withdraw: The allow_cd_withdraw of this ConsumerDisclosure.
        :type: str
        """

        self._allow_cd_withdraw = allow_cd_withdraw

    @property
    def allow_cd_withdraw_metadata(self):
        """
        Gets the allow_cd_withdraw_metadata of this ConsumerDisclosure.

        :return: The allow_cd_withdraw_metadata of this ConsumerDisclosure.
        :rtype: SettingsMetadata
        """
        return self._allow_cd_withdraw_metadata

    @allow_cd_withdraw_metadata.setter
    def allow_cd_withdraw_metadata(self, allow_cd_withdraw_metadata):
        """
        Sets the allow_cd_withdraw_metadata of this ConsumerDisclosure.

        :param allow_cd_withdraw_metadata: The allow_cd_withdraw_metadata of this ConsumerDisclosure.
        :type: SettingsMetadata
        """

        self._allow_cd_withdraw_metadata = allow_cd_withdraw_metadata

    @property
    def change_email(self):
        """
        Gets the change_email of this ConsumerDisclosure.
        

        :return: The change_email of this ConsumerDisclosure.
        :rtype: str
        """
        return self._change_email

    @change_email.setter
    def change_email(self, change_email):
        """
        Sets the change_email of this ConsumerDisclosure.
        

        :param change_email: The change_email of this ConsumerDisclosure.
        :type: str
        """

        self._change_email = change_email

    @property
    def change_email_other(self):
        """
        Gets the change_email_other of this ConsumerDisclosure.
        

        :return: The change_email_other of this ConsumerDisclosure.
        :rtype: str
        """
        return self._change_email_other

    @change_email_other.setter
    def change_email_other(self, change_email_other):
        """
        Sets the change_email_other of this ConsumerDisclosure.
        

        :param change_email_other: The change_email_other of this ConsumerDisclosure.
        :type: str
        """

        self._change_email_other = change_email_other

    @property
    def company_name(self):
        """
        Gets the company_name of this ConsumerDisclosure.
        The name of the company associated with the consumer disclosure.

        :return: The company_name of this ConsumerDisclosure.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """
        Sets the company_name of this ConsumerDisclosure.
        The name of the company associated with the consumer disclosure.

        :param company_name: The company_name of this ConsumerDisclosure.
        :type: str
        """

        self._company_name = company_name

    @property
    def company_phone(self):
        """
        Gets the company_phone of this ConsumerDisclosure.
        The phone number of the company associated with the consumer disclosure.

        :return: The company_phone of this ConsumerDisclosure.
        :rtype: str
        """
        return self._company_phone

    @company_phone.setter
    def company_phone(self, company_phone):
        """
        Sets the company_phone of this ConsumerDisclosure.
        The phone number of the company associated with the consumer disclosure.

        :param company_phone: The company_phone of this ConsumerDisclosure.
        :type: str
        """

        self._company_phone = company_phone

    @property
    def copy_cost_per_page(self):
        """
        Gets the copy_cost_per_page of this ConsumerDisclosure.
        

        :return: The copy_cost_per_page of this ConsumerDisclosure.
        :rtype: str
        """
        return self._copy_cost_per_page

    @copy_cost_per_page.setter
    def copy_cost_per_page(self, copy_cost_per_page):
        """
        Sets the copy_cost_per_page of this ConsumerDisclosure.
        

        :param copy_cost_per_page: The copy_cost_per_page of this ConsumerDisclosure.
        :type: str
        """

        self._copy_cost_per_page = copy_cost_per_page

    @property
    def copy_fee_collection_method(self):
        """
        Gets the copy_fee_collection_method of this ConsumerDisclosure.
        Specifies the fee collection method for cases in which the customer requires paper copies of the document.  Maximum Length: 255 characters

        :return: The copy_fee_collection_method of this ConsumerDisclosure.
        :rtype: str
        """
        return self._copy_fee_collection_method

    @copy_fee_collection_method.setter
    def copy_fee_collection_method(self, copy_fee_collection_method):
        """
        Sets the copy_fee_collection_method of this ConsumerDisclosure.
        Specifies the fee collection method for cases in which the customer requires paper copies of the document.  Maximum Length: 255 characters

        :param copy_fee_collection_method: The copy_fee_collection_method of this ConsumerDisclosure.
        :type: str
        """

        self._copy_fee_collection_method = copy_fee_collection_method

    @property
    def copy_request_email(self):
        """
        Gets the copy_request_email of this ConsumerDisclosure.
        

        :return: The copy_request_email of this ConsumerDisclosure.
        :rtype: str
        """
        return self._copy_request_email

    @copy_request_email.setter
    def copy_request_email(self, copy_request_email):
        """
        Sets the copy_request_email of this ConsumerDisclosure.
        

        :param copy_request_email: The copy_request_email of this ConsumerDisclosure.
        :type: str
        """

        self._copy_request_email = copy_request_email

    @property
    def custom(self):
        """
        Gets the custom of this ConsumerDisclosure.
        

        :return: The custom of this ConsumerDisclosure.
        :rtype: str
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """
        Sets the custom of this ConsumerDisclosure.
        

        :param custom: The custom of this ConsumerDisclosure.
        :type: str
        """

        self._custom = custom

    @property
    def enable_esign(self):
        """
        Gets the enable_esign of this ConsumerDisclosure.
        

        :return: The enable_esign of this ConsumerDisclosure.
        :rtype: str
        """
        return self._enable_esign

    @enable_esign.setter
    def enable_esign(self, enable_esign):
        """
        Sets the enable_esign of this ConsumerDisclosure.
        

        :param enable_esign: The enable_esign of this ConsumerDisclosure.
        :type: str
        """

        self._enable_esign = enable_esign

    @property
    def esign_agreement(self):
        """
        Gets the esign_agreement of this ConsumerDisclosure.
        The Electronic Record and Signature Disclosure text. The disclosure text includes the html formatting.

        :return: The esign_agreement of this ConsumerDisclosure.
        :rtype: str
        """
        return self._esign_agreement

    @esign_agreement.setter
    def esign_agreement(self, esign_agreement):
        """
        Sets the esign_agreement of this ConsumerDisclosure.
        The Electronic Record and Signature Disclosure text. The disclosure text includes the html formatting.

        :param esign_agreement: The esign_agreement of this ConsumerDisclosure.
        :type: str
        """

        self._esign_agreement = esign_agreement

    @property
    def esign_text(self):
        """
        Gets the esign_text of this ConsumerDisclosure.
        

        :return: The esign_text of this ConsumerDisclosure.
        :rtype: str
        """
        return self._esign_text

    @esign_text.setter
    def esign_text(self, esign_text):
        """
        Sets the esign_text of this ConsumerDisclosure.
        

        :param esign_text: The esign_text of this ConsumerDisclosure.
        :type: str
        """

        self._esign_text = esign_text

    @property
    def language_code(self):
        """
        Gets the language_code of this ConsumerDisclosure.
        

        :return: The language_code of this ConsumerDisclosure.
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """
        Sets the language_code of this ConsumerDisclosure.
        

        :param language_code: The language_code of this ConsumerDisclosure.
        :type: str
        """

        self._language_code = language_code

    @property
    def must_agree_to_esign(self):
        """
        Gets the must_agree_to_esign of this ConsumerDisclosure.
        

        :return: The must_agree_to_esign of this ConsumerDisclosure.
        :rtype: str
        """
        return self._must_agree_to_esign

    @must_agree_to_esign.setter
    def must_agree_to_esign(self, must_agree_to_esign):
        """
        Sets the must_agree_to_esign of this ConsumerDisclosure.
        

        :param must_agree_to_esign: The must_agree_to_esign of this ConsumerDisclosure.
        :type: str
        """

        self._must_agree_to_esign = must_agree_to_esign

    @property
    def pdf_id(self):
        """
        Gets the pdf_id of this ConsumerDisclosure.
        

        :return: The pdf_id of this ConsumerDisclosure.
        :rtype: str
        """
        return self._pdf_id

    @pdf_id.setter
    def pdf_id(self, pdf_id):
        """
        Sets the pdf_id of this ConsumerDisclosure.
        

        :param pdf_id: The pdf_id of this ConsumerDisclosure.
        :type: str
        """

        self._pdf_id = pdf_id

    @property
    def use_brand(self):
        """
        Gets the use_brand of this ConsumerDisclosure.
        

        :return: The use_brand of this ConsumerDisclosure.
        :rtype: str
        """
        return self._use_brand

    @use_brand.setter
    def use_brand(self, use_brand):
        """
        Sets the use_brand of this ConsumerDisclosure.
        

        :param use_brand: The use_brand of this ConsumerDisclosure.
        :type: str
        """

        self._use_brand = use_brand

    @property
    def use_consumer_disclosure_within_account(self):
        """
        Gets the use_consumer_disclosure_within_account of this ConsumerDisclosure.
        

        :return: The use_consumer_disclosure_within_account of this ConsumerDisclosure.
        :rtype: str
        """
        return self._use_consumer_disclosure_within_account

    @use_consumer_disclosure_within_account.setter
    def use_consumer_disclosure_within_account(self, use_consumer_disclosure_within_account):
        """
        Sets the use_consumer_disclosure_within_account of this ConsumerDisclosure.
        

        :param use_consumer_disclosure_within_account: The use_consumer_disclosure_within_account of this ConsumerDisclosure.
        :type: str
        """

        self._use_consumer_disclosure_within_account = use_consumer_disclosure_within_account

    @property
    def use_consumer_disclosure_within_account_metadata(self):
        """
        Gets the use_consumer_disclosure_within_account_metadata of this ConsumerDisclosure.

        :return: The use_consumer_disclosure_within_account_metadata of this ConsumerDisclosure.
        :rtype: SettingsMetadata
        """
        return self._use_consumer_disclosure_within_account_metadata

    @use_consumer_disclosure_within_account_metadata.setter
    def use_consumer_disclosure_within_account_metadata(self, use_consumer_disclosure_within_account_metadata):
        """
        Sets the use_consumer_disclosure_within_account_metadata of this ConsumerDisclosure.

        :param use_consumer_disclosure_within_account_metadata: The use_consumer_disclosure_within_account_metadata of this ConsumerDisclosure.
        :type: SettingsMetadata
        """

        self._use_consumer_disclosure_within_account_metadata = use_consumer_disclosure_within_account_metadata

    @property
    def withdraw_address_line1(self):
        """
        Gets the withdraw_address_line1 of this ConsumerDisclosure.
        Contains the first address line of the postal address to which a customer can send a consent withdrawal notification.  Maximum length: 100 characters. 

        :return: The withdraw_address_line1 of this ConsumerDisclosure.
        :rtype: str
        """
        return self._withdraw_address_line1

    @withdraw_address_line1.setter
    def withdraw_address_line1(self, withdraw_address_line1):
        """
        Sets the withdraw_address_line1 of this ConsumerDisclosure.
        Contains the first address line of the postal address to which a customer can send a consent withdrawal notification.  Maximum length: 100 characters. 

        :param withdraw_address_line1: The withdraw_address_line1 of this ConsumerDisclosure.
        :type: str
        """

        self._withdraw_address_line1 = withdraw_address_line1

    @property
    def withdraw_address_line2(self):
        """
        Gets the withdraw_address_line2 of this ConsumerDisclosure.
        Contains the second address line of the postal address to which a customer can send a consent withdrawal notification.  Maximum length: 100 characters. 

        :return: The withdraw_address_line2 of this ConsumerDisclosure.
        :rtype: str
        """
        return self._withdraw_address_line2

    @withdraw_address_line2.setter
    def withdraw_address_line2(self, withdraw_address_line2):
        """
        Sets the withdraw_address_line2 of this ConsumerDisclosure.
        Contains the second address line of the postal address to which a customer can send a consent withdrawal notification.  Maximum length: 100 characters. 

        :param withdraw_address_line2: The withdraw_address_line2 of this ConsumerDisclosure.
        :type: str
        """

        self._withdraw_address_line2 = withdraw_address_line2

    @property
    def withdraw_by_email(self):
        """
        Gets the withdraw_by_email of this ConsumerDisclosure.
        Indicates whether the customer can withdraw consent by email.

        :return: The withdraw_by_email of this ConsumerDisclosure.
        :rtype: str
        """
        return self._withdraw_by_email

    @withdraw_by_email.setter
    def withdraw_by_email(self, withdraw_by_email):
        """
        Sets the withdraw_by_email of this ConsumerDisclosure.
        Indicates whether the customer can withdraw consent by email.

        :param withdraw_by_email: The withdraw_by_email of this ConsumerDisclosure.
        :type: str
        """

        self._withdraw_by_email = withdraw_by_email

    @property
    def withdraw_by_mail(self):
        """
        Gets the withdraw_by_mail of this ConsumerDisclosure.
        Indicates whether the customer can withdraw consent by postal mail.

        :return: The withdraw_by_mail of this ConsumerDisclosure.
        :rtype: str
        """
        return self._withdraw_by_mail

    @withdraw_by_mail.setter
    def withdraw_by_mail(self, withdraw_by_mail):
        """
        Sets the withdraw_by_mail of this ConsumerDisclosure.
        Indicates whether the customer can withdraw consent by postal mail.

        :param withdraw_by_mail: The withdraw_by_mail of this ConsumerDisclosure.
        :type: str
        """

        self._withdraw_by_mail = withdraw_by_mail

    @property
    def withdraw_by_phone(self):
        """
        Gets the withdraw_by_phone of this ConsumerDisclosure.
        Indicates whether the customer can withdraw consent by phone.

        :return: The withdraw_by_phone of this ConsumerDisclosure.
        :rtype: str
        """
        return self._withdraw_by_phone

    @withdraw_by_phone.setter
    def withdraw_by_phone(self, withdraw_by_phone):
        """
        Sets the withdraw_by_phone of this ConsumerDisclosure.
        Indicates whether the customer can withdraw consent by phone.

        :param withdraw_by_phone: The withdraw_by_phone of this ConsumerDisclosure.
        :type: str
        """

        self._withdraw_by_phone = withdraw_by_phone

    @property
    def withdraw_city(self):
        """
        Gets the withdraw_city of this ConsumerDisclosure.
        Contains the city of the postal address to which a customer can send a consent withdrawal notification.  Maximum length: 50 characters. 

        :return: The withdraw_city of this ConsumerDisclosure.
        :rtype: str
        """
        return self._withdraw_city

    @withdraw_city.setter
    def withdraw_city(self, withdraw_city):
        """
        Sets the withdraw_city of this ConsumerDisclosure.
        Contains the city of the postal address to which a customer can send a consent withdrawal notification.  Maximum length: 50 characters. 

        :param withdraw_city: The withdraw_city of this ConsumerDisclosure.
        :type: str
        """

        self._withdraw_city = withdraw_city

    @property
    def withdraw_consequences(self):
        """
        Gets the withdraw_consequences of this ConsumerDisclosure.
        Indicates the consequences of withdrawing consent.

        :return: The withdraw_consequences of this ConsumerDisclosure.
        :rtype: str
        """
        return self._withdraw_consequences

    @withdraw_consequences.setter
    def withdraw_consequences(self, withdraw_consequences):
        """
        Sets the withdraw_consequences of this ConsumerDisclosure.
        Indicates the consequences of withdrawing consent.

        :param withdraw_consequences: The withdraw_consequences of this ConsumerDisclosure.
        :type: str
        """

        self._withdraw_consequences = withdraw_consequences

    @property
    def withdraw_email(self):
        """
        Gets the withdraw_email of this ConsumerDisclosure.
        Contains the email address to which a customer can send a consent withdrawal notification.  Maximum length: 100 characters. 

        :return: The withdraw_email of this ConsumerDisclosure.
        :rtype: str
        """
        return self._withdraw_email

    @withdraw_email.setter
    def withdraw_email(self, withdraw_email):
        """
        Sets the withdraw_email of this ConsumerDisclosure.
        Contains the email address to which a customer can send a consent withdrawal notification.  Maximum length: 100 characters. 

        :param withdraw_email: The withdraw_email of this ConsumerDisclosure.
        :type: str
        """

        self._withdraw_email = withdraw_email

    @property
    def withdraw_other(self):
        """
        Gets the withdraw_other of this ConsumerDisclosure.
        Indicates other information need to withdraw consent.  Maximum length: 255 characters.

        :return: The withdraw_other of this ConsumerDisclosure.
        :rtype: str
        """
        return self._withdraw_other

    @withdraw_other.setter
    def withdraw_other(self, withdraw_other):
        """
        Sets the withdraw_other of this ConsumerDisclosure.
        Indicates other information need to withdraw consent.  Maximum length: 255 characters.

        :param withdraw_other: The withdraw_other of this ConsumerDisclosure.
        :type: str
        """

        self._withdraw_other = withdraw_other

    @property
    def withdraw_phone(self):
        """
        Gets the withdraw_phone of this ConsumerDisclosure.
        Contains the phone number which a customer can call to register consent withdrawal notification.  Maximum length: 20 characters. 

        :return: The withdraw_phone of this ConsumerDisclosure.
        :rtype: str
        """
        return self._withdraw_phone

    @withdraw_phone.setter
    def withdraw_phone(self, withdraw_phone):
        """
        Sets the withdraw_phone of this ConsumerDisclosure.
        Contains the phone number which a customer can call to register consent withdrawal notification.  Maximum length: 20 characters. 

        :param withdraw_phone: The withdraw_phone of this ConsumerDisclosure.
        :type: str
        """

        self._withdraw_phone = withdraw_phone

    @property
    def withdraw_postal_code(self):
        """
        Gets the withdraw_postal_code of this ConsumerDisclosure.
        Contains the postal code of the postal address to which a customer can send a consent withdrawal notification.  Maximum length: 20 characters. 

        :return: The withdraw_postal_code of this ConsumerDisclosure.
        :rtype: str
        """
        return self._withdraw_postal_code

    @withdraw_postal_code.setter
    def withdraw_postal_code(self, withdraw_postal_code):
        """
        Sets the withdraw_postal_code of this ConsumerDisclosure.
        Contains the postal code of the postal address to which a customer can send a consent withdrawal notification.  Maximum length: 20 characters. 

        :param withdraw_postal_code: The withdraw_postal_code of this ConsumerDisclosure.
        :type: str
        """

        self._withdraw_postal_code = withdraw_postal_code

    @property
    def withdraw_state(self):
        """
        Gets the withdraw_state of this ConsumerDisclosure.
        Contains the state of the postal address to which a customer can send a consent withdrawal notification.

        :return: The withdraw_state of this ConsumerDisclosure.
        :rtype: str
        """
        return self._withdraw_state

    @withdraw_state.setter
    def withdraw_state(self, withdraw_state):
        """
        Sets the withdraw_state of this ConsumerDisclosure.
        Contains the state of the postal address to which a customer can send a consent withdrawal notification.

        :param withdraw_state: The withdraw_state of this ConsumerDisclosure.
        :type: str
        """

        self._withdraw_state = withdraw_state

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
