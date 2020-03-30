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


class UpdateSiteResponse(object):
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
        'oxd_id': 'OxdId'
    }

    attribute_map = {
        'oxd_id': 'oxd_id'
    }

    def __init__(self, oxd_id=None):  # noqa: E501
        """UpdateSiteResponse - a model defined in Swagger"""  # noqa: E501

        self._oxd_id = None
        self.discriminator = None

        self.oxd_id = oxd_id

    @property
    def oxd_id(self):
        """Gets the oxd_id of this UpdateSiteResponse.  # noqa: E501


        :return: The oxd_id of this UpdateSiteResponse.  # noqa: E501
        :rtype: OxdId
        """
        return self._oxd_id

    @oxd_id.setter
    def oxd_id(self, oxd_id):
        """Sets the oxd_id of this UpdateSiteResponse.


        :param oxd_id: The oxd_id of this UpdateSiteResponse.  # noqa: E501
        :type: OxdId
        """
        if oxd_id is None:
            raise ValueError("Invalid value for `oxd_id`, must not be `None`")  # noqa: E501

        self._oxd_id = oxd_id

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
        if issubclass(UpdateSiteResponse, dict):
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
        if not isinstance(other, UpdateSiteResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
