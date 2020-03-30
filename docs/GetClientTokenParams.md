# GetClientTokenParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op_host** | **str** |  | 
**op_discovery_path** | **str** |  | [optional] 
**scope** | **list[str]** |  | [optional] 
**client_id** | **str** |  | 
**client_secret** | **str** |  | 
**authentication_method** | **str** | if value is missed then basic authentication is used. Otherwise it&#39;s possible to set &#x60;private_key_jwt&#x60; value for Private Key authentication. | [optional] 
**algorithm** | **str** | optional but is required if authentication_method&#x3D;private_key_jwt. Valid values are none, HS256, HS384, HS512, RS256, RS384, RS512, ES256, ES384, ES512 | [optional] 
**key_id** | **str** | optional but is required if authentication_method&#x3D;private_key_jwt. It has to be valid key id from key store. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


