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


class GetAccessTokenByRefreshTokenParams(object):
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
        'oxd_id': 'str',
        'refresh_token': 'str',
        'scope': 'list[str]'
    }

    attribute_map = {
        'oxd_id': 'oxd_id',
        'refresh_token': 'refresh_token',
        'scope': 'scope'
    }

    def __init__(self, oxd_id=None, refresh_token=None, scope=None):  # noqa: E501
        """GetAccessTokenByRefreshTokenParams - a model defined in Swagger"""  # noqa: E501

        self._oxd_id = None
        self._refresh_token = None
        self._scope = None
        self.discriminator = None

        self.oxd_id = oxd_id
        self.refresh_token = refresh_token
        self.scope = scope

    @property
    def oxd_id(self):
        """Gets the oxd_id of this GetAccessTokenByRefreshTokenParams.  # noqa: E501


        :return: The oxd_id of this GetAccessTokenByRefreshTokenParams.  # noqa: E501
        :rtype: str
        """
        return self._oxd_id

    @oxd_id.setter
    def oxd_id(self, oxd_id):
        """Sets the oxd_id of this GetAccessTokenByRefreshTokenParams.


        :param oxd_id: The oxd_id of this GetAccessTokenByRefreshTokenParams.  # noqa: E501
        :type: str
        """
        if oxd_id is None:
            raise ValueError("Invalid value for `oxd_id`, must not be `None`")  # noqa: E501

        self._oxd_id = oxd_id

    @property
    def refresh_token(self):
        """Gets the refresh_token of this GetAccessTokenByRefreshTokenParams.  # noqa: E501


        :return: The refresh_token of this GetAccessTokenByRefreshTokenParams.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this GetAccessTokenByRefreshTokenParams.


        :param refresh_token: The refresh_token of this GetAccessTokenByRefreshTokenParams.  # noqa: E501
        :type: str
        """
        if refresh_token is None:
            raise ValueError("Invalid value for `refresh_token`, must not be `None`")  # noqa: E501

        self._refresh_token = refresh_token

    @property
    def scope(self):
        """Gets the scope of this GetAccessTokenByRefreshTokenParams.  # noqa: E501


        :return: The scope of this GetAccessTokenByRefreshTokenParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this GetAccessTokenByRefreshTokenParams.


        :param scope: The scope of this GetAccessTokenByRefreshTokenParams.  # noqa: E501
        :type: list[str]
        """
        if scope is None:
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501

        self._scope = scope

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
        if issubclass(GetAccessTokenByRefreshTokenParams, dict):
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
        if not isinstance(other, GetAccessTokenByRefreshTokenParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
