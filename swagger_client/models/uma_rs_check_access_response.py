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


class UmaRsCheckAccessResponse(object):
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
        'access': 'str',
        'ticket': 'str'
    }

    attribute_map = {
        'access': 'access',
        'ticket': 'ticket'
    }

    def __init__(self, access=None, ticket=None):  # noqa: E501
        """UmaRsCheckAccessResponse - a model defined in Swagger"""  # noqa: E501

        self._access = None
        self._ticket = None
        self.discriminator = None

        self.access = access
        self.ticket = ticket

    @property
    def access(self):
        """Gets the access of this UmaRsCheckAccessResponse.  # noqa: E501

        Possible values are granted, denied  # noqa: E501

        :return: The access of this UmaRsCheckAccessResponse.  # noqa: E501
        :rtype: str
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this UmaRsCheckAccessResponse.

        Possible values are granted, denied  # noqa: E501

        :param access: The access of this UmaRsCheckAccessResponse.  # noqa: E501
        :type: str
        """
        if access is None:
            raise ValueError("Invalid value for `access`, must not be `None`")  # noqa: E501

        self._access = access

    @property
    def ticket(self):
        """Gets the ticket of this UmaRsCheckAccessResponse.  # noqa: E501


        :return: The ticket of this UmaRsCheckAccessResponse.  # noqa: E501
        :rtype: str
        """
        return self._ticket

    @ticket.setter
    def ticket(self, ticket):
        """Sets the ticket of this UmaRsCheckAccessResponse.


        :param ticket: The ticket of this UmaRsCheckAccessResponse.  # noqa: E501
        :type: str
        """
        if ticket is None:
            raise ValueError("Invalid value for `ticket`, must not be `None`")  # noqa: E501

        self._ticket = ticket

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
        if issubclass(UmaRsCheckAccessResponse, dict):
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
        if not isinstance(other, UmaRsCheckAccessResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
