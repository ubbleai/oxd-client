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


class GetClientTokenParams(object):
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
        'op_discovery_path': 'str',
        'scope': 'list[str]',
        'client_id': 'str',
        'client_secret': 'str',
        'authentication_method': 'str',
        'algorithm': 'str',
        'key_id': 'str'
    }

    attribute_map = {
        'op_host': 'op_host',
        'op_discovery_path': 'op_discovery_path',
        'scope': 'scope',
        'client_id': 'client_id',
        'client_secret': 'client_secret',
        'authentication_method': 'authentication_method',
        'algorithm': 'algorithm',
        'key_id': 'key_id'
    }

    def __init__(self, op_host=None, op_discovery_path=None, scope=None, client_id=None, client_secret=None, authentication_method=None, algorithm=None, key_id=None):  # noqa: E501
        """GetClientTokenParams - a model defined in Swagger"""  # noqa: E501

        self._op_host = None
        self._op_discovery_path = None
        self._scope = None
        self._client_id = None
        self._client_secret = None
        self._authentication_method = None
        self._algorithm = None
        self._key_id = None
        self.discriminator = None

        self.op_host = op_host
        if op_discovery_path is not None:
            self.op_discovery_path = op_discovery_path
        if scope is not None:
            self.scope = scope
        self.client_id = client_id
        self.client_secret = client_secret
        if authentication_method is not None:
            self.authentication_method = authentication_method
        if algorithm is not None:
            self.algorithm = algorithm
        if key_id is not None:
            self.key_id = key_id

    @property
    def op_host(self):
        """Gets the op_host of this GetClientTokenParams.  # noqa: E501


        :return: The op_host of this GetClientTokenParams.  # noqa: E501
        :rtype: str
        """
        return self._op_host

    @op_host.setter
    def op_host(self, op_host):
        """Sets the op_host of this GetClientTokenParams.


        :param op_host: The op_host of this GetClientTokenParams.  # noqa: E501
        :type: str
        """
        if op_host is None:
            raise ValueError("Invalid value for `op_host`, must not be `None`")  # noqa: E501

        self._op_host = op_host

    @property
    def op_discovery_path(self):
        """Gets the op_discovery_path of this GetClientTokenParams.  # noqa: E501


        :return: The op_discovery_path of this GetClientTokenParams.  # noqa: E501
        :rtype: str
        """
        return self._op_discovery_path

    @op_discovery_path.setter
    def op_discovery_path(self, op_discovery_path):
        """Sets the op_discovery_path of this GetClientTokenParams.


        :param op_discovery_path: The op_discovery_path of this GetClientTokenParams.  # noqa: E501
        :type: str
        """

        self._op_discovery_path = op_discovery_path

    @property
    def scope(self):
        """Gets the scope of this GetClientTokenParams.  # noqa: E501


        :return: The scope of this GetClientTokenParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this GetClientTokenParams.


        :param scope: The scope of this GetClientTokenParams.  # noqa: E501
        :type: list[str]
        """

        self._scope = scope

    @property
    def client_id(self):
        """Gets the client_id of this GetClientTokenParams.  # noqa: E501


        :return: The client_id of this GetClientTokenParams.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this GetClientTokenParams.


        :param client_id: The client_id of this GetClientTokenParams.  # noqa: E501
        :type: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this GetClientTokenParams.  # noqa: E501


        :return: The client_secret of this GetClientTokenParams.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this GetClientTokenParams.


        :param client_secret: The client_secret of this GetClientTokenParams.  # noqa: E501
        :type: str
        """
        if client_secret is None:
            raise ValueError("Invalid value for `client_secret`, must not be `None`")  # noqa: E501

        self._client_secret = client_secret

    @property
    def authentication_method(self):
        """Gets the authentication_method of this GetClientTokenParams.  # noqa: E501

        if value is missed then basic authentication is used. Otherwise it's possible to set `private_key_jwt` value for Private Key authentication.  # noqa: E501

        :return: The authentication_method of this GetClientTokenParams.  # noqa: E501
        :rtype: str
        """
        return self._authentication_method

    @authentication_method.setter
    def authentication_method(self, authentication_method):
        """Sets the authentication_method of this GetClientTokenParams.

        if value is missed then basic authentication is used. Otherwise it's possible to set `private_key_jwt` value for Private Key authentication.  # noqa: E501

        :param authentication_method: The authentication_method of this GetClientTokenParams.  # noqa: E501
        :type: str
        """

        self._authentication_method = authentication_method

    @property
    def algorithm(self):
        """Gets the algorithm of this GetClientTokenParams.  # noqa: E501

        optional but is required if authentication_method=private_key_jwt. Valid values are none, HS256, HS384, HS512, RS256, RS384, RS512, ES256, ES384, ES512  # noqa: E501

        :return: The algorithm of this GetClientTokenParams.  # noqa: E501
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this GetClientTokenParams.

        optional but is required if authentication_method=private_key_jwt. Valid values are none, HS256, HS384, HS512, RS256, RS384, RS512, ES256, ES384, ES512  # noqa: E501

        :param algorithm: The algorithm of this GetClientTokenParams.  # noqa: E501
        :type: str
        """

        self._algorithm = algorithm

    @property
    def key_id(self):
        """Gets the key_id of this GetClientTokenParams.  # noqa: E501

        optional but is required if authentication_method=private_key_jwt. It has to be valid key id from key store.  # noqa: E501

        :return: The key_id of this GetClientTokenParams.  # noqa: E501
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this GetClientTokenParams.

        optional but is required if authentication_method=private_key_jwt. It has to be valid key id from key store.  # noqa: E501

        :param key_id: The key_id of this GetClientTokenParams.  # noqa: E501
        :type: str
        """

        self._key_id = key_id

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
        if issubclass(GetClientTokenParams, dict):
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
        if not isinstance(other, GetClientTokenParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
