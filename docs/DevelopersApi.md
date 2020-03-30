# swagger_client.DevelopersApi

All URIs are relative to *https://gluu.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_token_by_refresh_token**](DevelopersApi.md#get_access_token_by_refresh_token) | **POST** /get-access-token-by-refresh-token | Get Access Token By Refresh Token
[**get_authorization_url**](DevelopersApi.md#get_authorization_url) | **POST** /get-authorization-url | Get Authorization Url
[**get_client_token**](DevelopersApi.md#get_client_token) | **POST** /get-client-token | Get Client Token
[**get_discovery**](DevelopersApi.md#get_discovery) | **POST** /get-discovery | Get OP Discovery Configuration
[**get_json_web_key_set**](DevelopersApi.md#get_json_web_key_set) | **POST** /get-jwks | Get JSON Web Key Set
[**get_logout_uri**](DevelopersApi.md#get_logout_uri) | **POST** /get-logout-uri | Get Logout URL
[**get_tokens_by_code**](DevelopersApi.md#get_tokens_by_code) | **POST** /get-tokens-by-code | Get Tokens By Code
[**get_user_info**](DevelopersApi.md#get_user_info) | **POST** /get-user-info | Get User Info
[**health_check**](DevelopersApi.md#health_check) | **GET** /health-check | Health Check
[**introspect_access_token**](DevelopersApi.md#introspect_access_token) | **POST** /introspect-access-token | Introspect Access Token
[**introspect_rpt**](DevelopersApi.md#introspect_rpt) | **POST** /introspect-rpt | Introspect RPT
[**register_site**](DevelopersApi.md#register_site) | **POST** /register-site | Register Site
[**remove_site**](DevelopersApi.md#remove_site) | **POST** /remove-site | Remove Site
[**uma_rp_get_claims_gathering_url**](DevelopersApi.md#uma_rp_get_claims_gathering_url) | **POST** /uma-rp-get-claims-gathering-url | UMA RP Get Claims Gathering URL
[**uma_rp_get_rpt**](DevelopersApi.md#uma_rp_get_rpt) | **POST** /uma-rp-get-rpt | UMA RP Get RPT
[**uma_rs_check_access**](DevelopersApi.md#uma_rs_check_access) | **POST** /uma-rs-check-access | UMA RS Check Access
[**uma_rs_protect**](DevelopersApi.md#uma_rs_protect) | **POST** /uma-rs-protect | UMA RS Protect Resources
[**update_site**](DevelopersApi.md#update_site) | **POST** /update-site | Update Site


# **get_access_token_by_refresh_token**
> GetAccessTokenByRefreshTokenResponse get_access_token_by_refresh_token(authorization=authorization, get_access_token_by_refresh_token_params=get_access_token_by_refresh_token_params)

Get Access Token By Refresh Token

Get Access Token By Refresh Token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
authorization = 'authorization_example' # str |  (optional)
get_access_token_by_refresh_token_params = swagger_client.GetAccessTokenByRefreshTokenParams() # GetAccessTokenByRefreshTokenParams |  (optional)

try:
    # Get Access Token By Refresh Token
    api_response = api_instance.get_access_token_by_refresh_token(authorization=authorization, get_access_token_by_refresh_token_params=get_access_token_by_refresh_token_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_access_token_by_refresh_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **get_access_token_by_refresh_token_params** | [**GetAccessTokenByRefreshTokenParams**](GetAccessTokenByRefreshTokenParams.md)|  | [optional] 

### Return type

[**GetAccessTokenByRefreshTokenResponse**](GetAccessTokenByRefreshTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authorization_url**
> GetAuthorizationUrlResponse get_authorization_url(authorization=authorization, get_authorization_url_params=get_authorization_url_params)

Get Authorization Url

Gets authorization url

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
authorization = 'authorization_example' # str |  (optional)
get_authorization_url_params = swagger_client.GetAuthorizationUrlParams() # GetAuthorizationUrlParams |  (optional)

try:
    # Get Authorization Url
    api_response = api_instance.get_authorization_url(authorization=authorization, get_authorization_url_params=get_authorization_url_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_authorization_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **get_authorization_url_params** | [**GetAuthorizationUrlParams**](GetAuthorizationUrlParams.md)|  | [optional] 

### Return type

[**GetAuthorizationUrlResponse**](GetAuthorizationUrlResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_token**
> GetClientTokenResponse get_client_token(get_client_token_params=get_client_token_params)

Get Client Token

Gets Client Token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
get_client_token_params = swagger_client.GetClientTokenParams() # GetClientTokenParams |  (optional)

try:
    # Get Client Token
    api_response = api_instance.get_client_token(get_client_token_params=get_client_token_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_client_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_client_token_params** | [**GetClientTokenParams**](GetClientTokenParams.md)|  | [optional] 

### Return type

[**GetClientTokenResponse**](GetClientTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discovery**
> GetDiscoveryResponse get_discovery(get_discovery_params=get_discovery_params)

Get OP Discovery Configuration

Get OP Discovery Configuration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
get_discovery_params = swagger_client.GetDiscoveryParams() # GetDiscoveryParams |  (optional)

try:
    # Get OP Discovery Configuration
    api_response = api_instance.get_discovery(get_discovery_params=get_discovery_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_discovery: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_discovery_params** | [**GetDiscoveryParams**](GetDiscoveryParams.md)|  | [optional] 

### Return type

[**GetDiscoveryResponse**](GetDiscoveryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_json_web_key_set**
> GetJwksResponse get_json_web_key_set(authorization=authorization, get_jwks_params=get_jwks_params)

Get JSON Web Key Set

Get JSON Web Key Set

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
authorization = 'authorization_example' # str |  (optional)
get_jwks_params = swagger_client.GetJwksParams() # GetJwksParams |  (optional)

try:
    # Get JSON Web Key Set
    api_response = api_instance.get_json_web_key_set(authorization=authorization, get_jwks_params=get_jwks_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_json_web_key_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **get_jwks_params** | [**GetJwksParams**](GetJwksParams.md)|  | [optional] 

### Return type

[**GetJwksResponse**](GetJwksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logout_uri**
> GetLogoutUriResponse get_logout_uri(authorization=authorization, get_logout_uri_params=get_logout_uri_params)

Get Logout URL

Get Logout URL

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
authorization = 'authorization_example' # str |  (optional)
get_logout_uri_params = swagger_client.GetLogoutUriParams() # GetLogoutUriParams |  (optional)

try:
    # Get Logout URL
    api_response = api_instance.get_logout_uri(authorization=authorization, get_logout_uri_params=get_logout_uri_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_logout_uri: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **get_logout_uri_params** | [**GetLogoutUriParams**](GetLogoutUriParams.md)|  | [optional] 

### Return type

[**GetLogoutUriResponse**](GetLogoutUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokens_by_code**
> GetTokensByCodeResponse get_tokens_by_code(authorization=authorization, get_tokens_by_code_params=get_tokens_by_code_params)

Get Tokens By Code

Get tokens by code

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
authorization = 'authorization_example' # str |  (optional)
get_tokens_by_code_params = swagger_client.GetTokensByCodeParams() # GetTokensByCodeParams |  (optional)

try:
    # Get Tokens By Code
    api_response = api_instance.get_tokens_by_code(authorization=authorization, get_tokens_by_code_params=get_tokens_by_code_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_tokens_by_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **get_tokens_by_code_params** | [**GetTokensByCodeParams**](GetTokensByCodeParams.md)|  | [optional] 

### Return type

[**GetTokensByCodeResponse**](GetTokensByCodeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_info**
> dict(str, object) get_user_info(authorization=authorization, get_user_info_params=get_user_info_params)

Get User Info

Get User Info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
authorization = 'authorization_example' # str |  (optional)
get_user_info_params = swagger_client.GetUserInfoParams() # GetUserInfoParams |  (optional)

try:
    # Get User Info
    api_response = api_instance.get_user_info(authorization=authorization, get_user_info_params=get_user_info_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_user_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **get_user_info_params** | [**GetUserInfoParams**](GetUserInfoParams.md)|  | [optional] 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_check**
> health_check()

Health Check

Health Check endpoint is for quick check whether oxd-server is alive.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()

try:
    # Health Check
    api_instance.health_check()
except ApiException as e:
    print("Exception when calling DevelopersApi->health_check: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **introspect_access_token**
> IntrospectAccessTokenResponse introspect_access_token(authorization=authorization, introspect_access_token_params=introspect_access_token_params)

Introspect Access Token

Introspect Access Token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
authorization = 'authorization_example' # str |  (optional)
introspect_access_token_params = swagger_client.IntrospectAccessTokenParams() # IntrospectAccessTokenParams |  (optional)

try:
    # Introspect Access Token
    api_response = api_instance.introspect_access_token(authorization=authorization, introspect_access_token_params=introspect_access_token_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->introspect_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **introspect_access_token_params** | [**IntrospectAccessTokenParams**](IntrospectAccessTokenParams.md)|  | [optional] 

### Return type

[**IntrospectAccessTokenResponse**](IntrospectAccessTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **introspect_rpt**
> IntrospectRptResponse introspect_rpt(authorization=authorization, introspect_rpt_params=introspect_rpt_params)

Introspect RPT

Introspect RPT

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
authorization = 'authorization_example' # str |  (optional)
introspect_rpt_params = swagger_client.IntrospectRptParams() # IntrospectRptParams |  (optional)

try:
    # Introspect RPT
    api_response = api_instance.introspect_rpt(authorization=authorization, introspect_rpt_params=introspect_rpt_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->introspect_rpt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **introspect_rpt_params** | [**IntrospectRptParams**](IntrospectRptParams.md)|  | [optional] 

### Return type

[**IntrospectRptResponse**](IntrospectRptResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_site**
> RegisterSiteResponse register_site(register_site_params=register_site_params)

Register Site

Registers site at oxd-server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
register_site_params = swagger_client.RegisterSiteParams() # RegisterSiteParams |  (optional)

try:
    # Register Site
    api_response = api_instance.register_site(register_site_params=register_site_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->register_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_site_params** | [**RegisterSiteParams**](RegisterSiteParams.md)|  | [optional] 

### Return type

[**RegisterSiteResponse**](RegisterSiteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_site**
> UpdateSiteResponse remove_site(authorization=authorization, remove_site_params=remove_site_params)

Remove Site

Removes site from oxd-server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
authorization = 'authorization_example' # str |  (optional)
remove_site_params = swagger_client.RemoveSiteParams() # RemoveSiteParams |  (optional)

try:
    # Remove Site
    api_response = api_instance.remove_site(authorization=authorization, remove_site_params=remove_site_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->remove_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **remove_site_params** | [**RemoveSiteParams**](RemoveSiteParams.md)|  | [optional] 

### Return type

[**UpdateSiteResponse**](UpdateSiteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uma_rp_get_claims_gathering_url**
> UmaRpGetClaimsGatheringUrlResponse uma_rp_get_claims_gathering_url(authorization=authorization, uma_rp_get_claims_gathering_url_params=uma_rp_get_claims_gathering_url_params)

UMA RP Get Claims Gathering URL

UMA RP Get Claims Gathering URL

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
authorization = 'authorization_example' # str |  (optional)
uma_rp_get_claims_gathering_url_params = swagger_client.UmaRpGetClaimsGatheringUrlParams() # UmaRpGetClaimsGatheringUrlParams |  (optional)

try:
    # UMA RP Get Claims Gathering URL
    api_response = api_instance.uma_rp_get_claims_gathering_url(authorization=authorization, uma_rp_get_claims_gathering_url_params=uma_rp_get_claims_gathering_url_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->uma_rp_get_claims_gathering_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **uma_rp_get_claims_gathering_url_params** | [**UmaRpGetClaimsGatheringUrlParams**](UmaRpGetClaimsGatheringUrlParams.md)|  | [optional] 

### Return type

[**UmaRpGetClaimsGatheringUrlResponse**](UmaRpGetClaimsGatheringUrlResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uma_rp_get_rpt**
> UmaRpGetRptResponse uma_rp_get_rpt(authorization=authorization, uma_rp_get_rpt_params=uma_rp_get_rpt_params)

UMA RP Get RPT

UMA RP Get RPT

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
authorization = 'authorization_example' # str |  (optional)
uma_rp_get_rpt_params = swagger_client.UmaRpGetRptParams() # UmaRpGetRptParams |  (optional)

try:
    # UMA RP Get RPT
    api_response = api_instance.uma_rp_get_rpt(authorization=authorization, uma_rp_get_rpt_params=uma_rp_get_rpt_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->uma_rp_get_rpt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **uma_rp_get_rpt_params** | [**UmaRpGetRptParams**](UmaRpGetRptParams.md)|  | [optional] 

### Return type

[**UmaRpGetRptResponse**](UmaRpGetRptResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uma_rs_check_access**
> UmaRsCheckAccessResponse uma_rs_check_access(authorization=authorization, uma_rs_check_access_params=uma_rs_check_access_params)

UMA RS Check Access

UMA RS Check Access

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
authorization = 'authorization_example' # str |  (optional)
uma_rs_check_access_params = swagger_client.UmaRsCheckAccessParams() # UmaRsCheckAccessParams |  (optional)

try:
    # UMA RS Check Access
    api_response = api_instance.uma_rs_check_access(authorization=authorization, uma_rs_check_access_params=uma_rs_check_access_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->uma_rs_check_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **uma_rs_check_access_params** | [**UmaRsCheckAccessParams**](UmaRsCheckAccessParams.md)|  | [optional] 

### Return type

[**UmaRsCheckAccessResponse**](UmaRsCheckAccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uma_rs_protect**
> UmaRsProtectResponse uma_rs_protect(authorization=authorization, uma_rs_protect_params=uma_rs_protect_params)

UMA RS Protect Resources

UMA RS Protect Resources. It's important to have a single HTTP method, mentioned only once within a given path in JSON, otherwise, the operation will fail.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
authorization = 'authorization_example' # str |  (optional)
uma_rs_protect_params = swagger_client.UmaRsProtectParams() # UmaRsProtectParams |  (optional)

try:
    # UMA RS Protect Resources
    api_response = api_instance.uma_rs_protect(authorization=authorization, uma_rs_protect_params=uma_rs_protect_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->uma_rs_protect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **uma_rs_protect_params** | [**UmaRsProtectParams**](UmaRsProtectParams.md)|  | [optional] 

### Return type

[**UmaRsProtectResponse**](UmaRsProtectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site**
> UpdateSiteResponse update_site(authorization=authorization, update_site_params=update_site_params)

Update Site

Updates site at oxd-server. If something changes in a pre-registered client, you can use this API to update your client in the OP.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
authorization = 'authorization_example' # str |  (optional)
update_site_params = swagger_client.UpdateSiteParams() # UpdateSiteParams |  (optional)

try:
    # Update Site
    api_response = api_instance.update_site(authorization=authorization, update_site_params=update_site_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->update_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **update_site_params** | [**UpdateSiteParams**](UpdateSiteParams.md)|  | [optional] 

### Return type

[**UpdateSiteResponse**](UpdateSiteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

