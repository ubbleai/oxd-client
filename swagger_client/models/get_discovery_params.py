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


class GetDiscoveryParams(object):
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
        'op_host': 'str',
        'op_discovery_path': 'str'
    }

    attribute_map = {
        'op_host': 'op_host',
        'op_discovery_path': 'op_discovery_path'
    }

    def __init__(self, op_host=None, op_discovery_path=None):  # noqa: E501
        """GetDiscoveryParams - a model defined in Swagger"""  # noqa: E501

        self._op_host = None
        self._op_discovery_path = None
        self.discriminator = None

        self.op_host = op_host
        if op_discovery_path is not None:
            self.op_discovery_path = op_discovery_path

    @property
    def op_host(self):
        """Gets the op_host of this GetDiscoveryParams.  # noqa: E501


        :return: The op_host of this GetDiscoveryParams.  # noqa: E501
        :rtype: str
        """
        return self._op_host

    @op_host.setter
    def op_host(self, op_host):
        """Sets the op_host of this GetDiscoveryParams.


        :param op_host: The op_host of this GetDiscoveryParams.  # noqa: E501
        :type: str
        """
        if op_host is None:
            raise ValueError("Invalid value for `op_host`, must not be `None`")  # noqa: E501

        self._op_host = op_host

    @property
    def op_discovery_path(self):
        """Gets the op_discovery_path of this GetDiscoveryParams.  # noqa: E501


        :return: The op_discovery_path of this GetDiscoveryParams.  # noqa: E501
        :rtype: str
        """
        return self._op_discovery_path

    @op_discovery_path.setter
    def op_discovery_path(self, op_discovery_path):
        """Sets the op_discovery_path of this GetDiscoveryParams.


        :param op_discovery_path: The op_discovery_path of this GetDiscoveryParams.  # noqa: E501
        :type: str
        """

        self._op_discovery_path = op_discovery_path

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
        if issubclass(GetDiscoveryParams, dict):
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
        if not isinstance(other, GetDiscoveryParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
