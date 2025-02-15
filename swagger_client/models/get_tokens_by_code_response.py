# coding: utf-8

"""
    oxd-server

    oxd-server  # noqa: E501

    OpenAPI spec version: 4.0
    Contact: yuriyz@gluu.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetTokensByCodeResponse(object):
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
        'access_token': 'str',
        'expires_in': 'int',
        'id_token': 'str',
        'refresh_token': 'str',
        'id_token_claims': 'object'
    }

    attribute_map = {
        'access_token': 'access_token',
        'expires_in': 'expires_in',
        'id_token': 'id_token',
        'refresh_token': 'refresh_token',
        'id_token_claims': 'id_token_claims'
    }

    def __init__(self, access_token=None, expires_in=None, id_token=None, refresh_token=None, id_token_claims=None):  # noqa: E501
        """GetTokensByCodeResponse - a model defined in Swagger"""  # noqa: E501

        self._access_token = None
        self._expires_in = None
        self._id_token = None
        self._refresh_token = None
        self._id_token_claims = None
        self.discriminator = None

        self.access_token = access_token
        self.expires_in = expires_in
        self.id_token = id_token
        self.refresh_token = refresh_token
        self.id_token_claims = id_token_claims

    @property
    def access_token(self):
        """Gets the access_token of this GetTokensByCodeResponse.  # noqa: E501


        :return: The access_token of this GetTokensByCodeResponse.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this GetTokensByCodeResponse.


        :param access_token: The access_token of this GetTokensByCodeResponse.  # noqa: E501
        :type: str
        """
        if access_token is None:
            raise ValueError("Invalid value for `access_token`, must not be `None`")  # noqa: E501

        self._access_token = access_token

    @property
    def expires_in(self):
        """Gets the expires_in of this GetTokensByCodeResponse.  # noqa: E501


        :return: The expires_in of this GetTokensByCodeResponse.  # noqa: E501
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this GetTokensByCodeResponse.


        :param expires_in: The expires_in of this GetTokensByCodeResponse.  # noqa: E501
        :type: int
        """
        if expires_in is None:
            raise ValueError("Invalid value for `expires_in`, must not be `None`")  # noqa: E501

        self._expires_in = expires_in

    @property
    def id_token(self):
        """Gets the id_token of this GetTokensByCodeResponse.  # noqa: E501


        :return: The id_token of this GetTokensByCodeResponse.  # noqa: E501
        :rtype: str
        """
        return self._id_token

    @id_token.setter
    def id_token(self, id_token):
        """Sets the id_token of this GetTokensByCodeResponse.


        :param id_token: The id_token of this GetTokensByCodeResponse.  # noqa: E501
        :type: str
        """
        if id_token is None:
            raise ValueError("Invalid value for `id_token`, must not be `None`")  # noqa: E501

        self._id_token = id_token

    @property
    def refresh_token(self):
        """Gets the refresh_token of this GetTokensByCodeResponse.  # noqa: E501


        :return: The refresh_token of this GetTokensByCodeResponse.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this GetTokensByCodeResponse.


        :param refresh_token: The refresh_token of this GetTokensByCodeResponse.  # noqa: E501
        :type: str
        """
        if refresh_token is None:
            raise ValueError("Invalid value for `refresh_token`, must not be `None`")  # noqa: E501

        self._refresh_token = refresh_token

    @property
    def id_token_claims(self):
        """Gets the id_token_claims of this GetTokensByCodeResponse.  # noqa: E501


        :return: The id_token_claims of this GetTokensByCodeResponse.  # noqa: E501
        :rtype: object
        """
        return self._id_token_claims

    @id_token_claims.setter
    def id_token_claims(self, id_token_claims):
        """Sets the id_token_claims of this GetTokensByCodeResponse.


        :param id_token_claims: The id_token_claims of this GetTokensByCodeResponse.  # noqa: E501
        :type: object
        """
        if id_token_claims is None:
            raise ValueError("Invalid value for `id_token_claims`, must not be `None`")  # noqa: E501

        self._id_token_claims = id_token_claims

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
        if issubclass(GetTokensByCodeResponse, dict):
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
        if not isinstance(other, GetTokensByCodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
