# Exigo API — Users

API version v2025.11.7.6. Crawled 2026-11-11 from https://api.exigo.com/3.0/. Back to [index](../README.md).

| Operation | REST | Summary |
|---|---|---|
| [AuthenticateUser](#authenticateuser) | `POST /3.0/user/authenticate` | Authenticates a corporate user for login using UserName and Password combination. |
| [GetUserPermissions](#getuserpermissions) | `GET /3.0/user/permissions?loginName=1` | Returns permissions associated with the corporate user account. |

---
### AuthenticateUser

> Authenticates a corporate user for login using UserName and Password combination.

| | |
|---|---|
| Category | Users |
| REST | `POST /3.0/user/authenticate` |
| SOAP action | `https://api.exigo.com/AuthenticateUser` |
| WSDL elements | `AuthenticateUserRequest` → `AuthenticateUserResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=AuthenticateUser |

#### Input

**`AuthenticateUserRequest`**

| Property | Type | Notes |
|---|---|---|
| `LoginName` | `String` |  |
| `Password` | `String` |  |

#### Output

**`AuthenticateUserResponse`**

| Property | Type | Notes |
|---|---|---|
| `FirstName` | `String` |  |
| `LastName` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/user/authenticate HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "loginName": "1",
  "password": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "firstName": "",
  "lastName": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/AuthenticateUser"

<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xmlns:xsd="http://www.w3.org/2001/XMLSchema"
      xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <ApiAuthentication xmlns="http://api.exigo.com/">
      <LoginName>string</LoginName>
      <Password>string</Password>
      <Company>string</Company>
      <Identity>string</Identity>
      <RequestTimeUtc>dateTime</RequestTimeUtc>
      <Signature>string</Signature>
    </ApiAuthentication>
  </soap:Header>
  <soap:Body>
    <AuthenticateUserRequest xmlns="http://api.exigo.com/">
      <LoginName>string</LoginName>
      <Password>string</Password>
    </AuthenticateUserRequest>
  </soap:Body>
</soap:Envelope>
```

```xml
HTTP/1.1 200 OK
Content-Type: text/xml; charset=utf-8
Content-Length: length

<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xmlns:xsd="http://www.w3.org/2001/XMLSchema"
      xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <AuthenticateUserResult xmlns="http://api.exigo.com/">
      <FirstName>string</FirstName>
      <LastName>string</LastName>
    </AuthenticateUserResult>
  </soap:Body>
</soap:Envelope>
```

</details>

<details><summary>C# REST client</summary>

_Install Nuget package Exigo.Api.Client_

```csharp
try
{
    //Create Api Client
    var api = new ExigoApiClient("yourcmpany", "yourlogin", "yourpassword");

    //Create Request
    var req = new AuthenticateUserRequest();

    req.LoginName = "1";
    req.Password = "1";

    //Send Request to Server and Get Response
    var res = await api.AuthenticateUserAsync(req);

    //Now examine the results:
    Console.WriteLine("FirstName: {0}", res.FirstName);
    Console.WriteLine("LastName: {0}", res.LastName);
}
catch (Exception ex)
{
    Console.WriteLine("Error: " + ex.Message);
}
```

</details>

<details><summary>C# SOAP client</summary>

```csharp
try
{
    //Create Main API Context Object
    ExigoApi api = new ExigoApi();

    //Create Authentication Header
    ApiAuthentication auth = new ApiAuthentication();
    auth.LoginName = "yourLoginName";
    auth.Password = "yourPassword";
    auth.Company = "yourCompany";
    api.ApiAuthenticationValue = auth;

    //Create Request
    AuthenticateUserRequest req = new AuthenticateUserRequest();

    req.LoginName = "1";
    req.Password = "1";

    //Send Request to Server and Get Response
    AuthenticateUserResponse res = api.AuthenticateUser(req);

    //Now examine the results:
    Console.WriteLine("FirstName: {0}", res.FirstName);
    Console.WriteLine("LastName: {0}", res.LastName);
}
catch (Exception ex)
{
    Console.WriteLine("Error: " + ex.Message);
}
```

</details>

<details><summary>VB.Net</summary>

```vbnet
Try
    'Create Main API Context Object
    Dim api as new ExigoApi()

    'Create Authentication Header
    Dim auth as new ApiAuthentication()
    auth.LoginName = "yourLoginName"
    auth.Password = "yourPassword"
    auth.Company = "yourCompany"
    api.ApiAuthenticationValue = auth

    'Create Request
    Dim req as new AuthenticateUserRequest()

    req.LoginName = "1"
    req.Password = "1"

    'Send Request to Server and Get Response
    Dim res As AuthenticateUserResponse = api.AuthenticateUser(req)

    'Now examine the results:
    Console.WriteLine("FirstName: {0}", res.FirstName)
    Console.WriteLine("LastName: {0}", res.LastName)
Catch ex As Exception
    Console.WriteLine("Error: " & ex.Message)
End Try
```

</details>

<details><summary>PHP</summary>

_Note: PHP is not officially supported._

```php
<?php
try
{
    //Setup the SoapClient and Authentication
    $api = new SoapClient("http://api.exigo.com/3.0/ExigoApi.asmx?WSDL");
    $ns = "http://api.exigo.com/";
    $auth = array()
    $auth["LoginName"] = new SoapVar("yourLoginName",XSD_STRING,null,null,null,$ns);
    $auth["Password"] = new SoapVar("yourPassword",XSD_STRING,null,null,null,$ns);
    $auth["Company"] = new SoapVar("yourCompany",XSD_STRING,null,null,null,$ns);
    $headerBody = new SoapVar($auth, SOAP_ENC_OBJECT);
    $header = new SoapHeader($ns, 'ApiAuthentication', $headerBody);
    $api->__setSoapHeaders(array($header));

    //Create Request

    $req->LoginName = "1";
    $req->Password = "1";

    //Send Request to Server and Get Response
    $res = $api.AuthenticateUser($req);

    //Now examine the results:
}
catch (SoapFault $ex)
{
    echo "Error: ", $ex->getMessage();
}
?>
```

</details>

<details><summary>Java</summary>

_Note: Java is not officially supported._

```java
try
{
    //Create Main API Context Object
    ExigoApi api = new ExigoApi();

    //Create Authentication Header
    ApiAuthentication auth = new ApiAuthentication();
    auth.setLoginName("yourLoginName");
    auth.setPassword("yourPassword");
    auth.setCompany("yourCompany");
    api.setApiAuthenticationValue(auth);

    //Create Request
    AuthenticateUserRequest req = new AuthenticateUserRequest();

    req.setLoginName("1");
    req.setPassword("1");

    //Send Request to Server and Get Response
    AuthenticateUserResponse res = api.getExigoApiSoap().authenticateUser(req, auth);

    //Now examine the results:
}
catch (Exception ex)
{
    System.out.println("Error: " + ex.getMessage());
}
```

</details>

<details><summary>CSV</summary>

_This method does not support csv output._

```text
© 2026 Exigo.
```

</details>

---

### GetUserPermissions

>  Returns permissions associated with the corporate user account.

| | |
|---|---|
| Category | Users |
| REST | `GET /3.0/user/permissions?loginName=1` |
| SOAP action | `https://api.exigo.com/GetUserPermissions` |
| WSDL elements | `GetUserPermissionsRequest` → `GetUserPermissionsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetUserPermissions |

#### Input

**`GetUserPermissionsRequest`**

| Property | Type | Notes |
|---|---|---|
| `LoginName` | `String` |  |

#### Output

**`GetUserPermissionsResponse`**

| Property | Type | Notes |
|---|---|---|
| `RestrictToCustomerTypes` | `Int32[]` | List of any Customer Type Restrictions. |
| `RestrictToCustomerStatuses` | `Int32[]` | List of any Customer Status Restrictions. |
| `RestrictToWarehouses` | `Int32[]` | List of any warehouse Restrictions. |
| `RestrictToCountries` | `String[]` | List of any Country Restrictions. |
| `RestrictToCurrencies` | `String[]` | List of any Currency Code Restrictions. |
| `ViewDeletedCustomers` | `Boolean` |  |
| `AllowRemoteCheckPrint` | `Boolean` |  |
| `AllowOverrideItemPrice` | `Boolean` |  |
| `AllowStatementPrint` | `Boolean` |  |
| `DefaultWarehouseID` | `Int32` | Unique location for orders.<br>**Lookup:** company-specific list (see company-lists.md) |
| `LanguageID` | `Int32` | Customize the web experience by setting this.<br>**Lookup:** company-specific list (see company-lists.md) |
| `CultureCode` | `String` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/user/permissions?loginName=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "restrictToCustomerTypes": null,
  "restrictToCustomerStatuses": null,
  "restrictToWarehouses": null,
  "restrictToCountries": null,
  "restrictToCurrencies": null,
  "viewDeletedCustomers": true,
  "allowRemoteCheckPrint": true,
  "allowOverrideItemPrice": true,
  "allowStatementPrint": true,
  "defaultWarehouseID": 1,
  "languageID": 1,
  "cultureCode": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetUserPermissions"

<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xmlns:xsd="http://www.w3.org/2001/XMLSchema"
      xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <ApiAuthentication xmlns="http://api.exigo.com/">
      <LoginName>string</LoginName>
      <Password>string</Password>
      <Company>string</Company>
      <Identity>string</Identity>
      <RequestTimeUtc>dateTime</RequestTimeUtc>
      <Signature>string</Signature>
    </ApiAuthentication>
  </soap:Header>
  <soap:Body>
    <GetUserPermissionsRequest xmlns="http://api.exigo.com/">
      <LoginName>string</LoginName>
    </GetUserPermissionsRequest>
  </soap:Body>
</soap:Envelope>
```

```xml
HTTP/1.1 200 OK
Content-Type: text/xml; charset=utf-8
Content-Length: length

<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xmlns:xsd="http://www.w3.org/2001/XMLSchema"
      xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <GetUserPermissionsResult xmlns="http://api.exigo.com/">
      <RestrictToCustomerTypes>
        <int>int</int>
      </RestrictToCustomerTypes>
      <RestrictToCustomerStatuses>
        <int>int</int>
      </RestrictToCustomerStatuses>
      <RestrictToWarehouses>
        <int>int</int>
      </RestrictToWarehouses>
      <RestrictToCountries>
        <string>string</string>
      </RestrictToCountries>
      <RestrictToCurrencies>
        <string>string</string>
      </RestrictToCurrencies>
      <ViewDeletedCustomers>boolean</ViewDeletedCustomers>
      <AllowRemoteCheckPrint>boolean</AllowRemoteCheckPrint>
      <AllowOverrideItemPrice>boolean</AllowOverrideItemPrice>
      <AllowStatementPrint>boolean</AllowStatementPrint>
      <DefaultWarehouseID>int</DefaultWarehouseID>
      <LanguageID>int</LanguageID>
      <CultureCode>string</CultureCode>
    </GetUserPermissionsResult>
  </soap:Body>
</soap:Envelope>
```

</details>

<details><summary>C# REST client</summary>

_Install Nuget package Exigo.Api.Client_

```csharp
try
{
    //Create Api Client
    var api = new ExigoApiClient("yourcmpany", "yourlogin", "yourpassword");

    //Create Request
    var req = new GetUserPermissionsRequest();

    req.LoginName = "1";

    //Send Request to Server and Get Response
    var res = await api.GetUserPermissionsAsync(req);

    //Now examine the results:
    Console.WriteLine("ViewDeletedCustomers: {0}", res.ViewDeletedCustomers);
    Console.WriteLine("AllowRemoteCheckPrint: {0}", res.AllowRemoteCheckPrint);
    Console.WriteLine("AllowOverrideItemPrice: {0}", res.AllowOverrideItemPrice);
    Console.WriteLine("AllowStatementPrint: {0}", res.AllowStatementPrint);
    Console.WriteLine("DefaultWarehouseID: {0}", res.DefaultWarehouseID);
    Console.WriteLine("CultureCode: {0}", res.CultureCode);
}
catch (Exception ex)
{
    Console.WriteLine("Error: " + ex.Message);
}
```

</details>

<details><summary>C# SOAP client</summary>

```csharp
try
{
    //Create Main API Context Object
    ExigoApi api = new ExigoApi();

    //Create Authentication Header
    ApiAuthentication auth = new ApiAuthentication();
    auth.LoginName = "yourLoginName";
    auth.Password = "yourPassword";
    auth.Company = "yourCompany";
    api.ApiAuthenticationValue = auth;

    //Create Request
    GetUserPermissionsRequest req = new GetUserPermissionsRequest();

    req.LoginName = "1";

    //Send Request to Server and Get Response
    GetUserPermissionsResponse res = api.GetUserPermissions(req);

    //Now examine the results:
    Console.WriteLine("ViewDeletedCustomers: {0}", res.ViewDeletedCustomers);
    Console.WriteLine("AllowRemoteCheckPrint: {0}", res.AllowRemoteCheckPrint);
    Console.WriteLine("AllowOverrideItemPrice: {0}", res.AllowOverrideItemPrice);
    Console.WriteLine("AllowStatementPrint: {0}", res.AllowStatementPrint);
    Console.WriteLine("DefaultWarehouseID: {0}", res.DefaultWarehouseID);
    Console.WriteLine("CultureCode: {0}", res.CultureCode);
}
catch (Exception ex)
{
    Console.WriteLine("Error: " + ex.Message);
}
```

</details>

<details><summary>VB.Net</summary>

```vbnet
Try
    'Create Main API Context Object
    Dim api as new ExigoApi()

    'Create Authentication Header
    Dim auth as new ApiAuthentication()
    auth.LoginName = "yourLoginName"
    auth.Password = "yourPassword"
    auth.Company = "yourCompany"
    api.ApiAuthenticationValue = auth

    'Create Request
    Dim req as new GetUserPermissionsRequest()

    req.LoginName = "1"

    'Send Request to Server and Get Response
    Dim res As GetUserPermissionsResponse = api.GetUserPermissions(req)

    'Now examine the results:
    Console.WriteLine("ViewDeletedCustomers: {0}", res.ViewDeletedCustomers)
    Console.WriteLine("AllowRemoteCheckPrint: {0}", res.AllowRemoteCheckPrint)
    Console.WriteLine("AllowOverrideItemPrice: {0}", res.AllowOverrideItemPrice)
    Console.WriteLine("AllowStatementPrint: {0}", res.AllowStatementPrint)
    Console.WriteLine("DefaultWarehouseID: {0}", res.DefaultWarehouseID)
    Console.WriteLine("CultureCode: {0}", res.CultureCode)
Catch ex As Exception
    Console.WriteLine("Error: " & ex.Message)
End Try
```

</details>

<details><summary>PHP</summary>

_Note: PHP is not officially supported._

```php
<?php
try
{
    //Setup the SoapClient and Authentication
    $api = new SoapClient("http://api.exigo.com/3.0/ExigoApi.asmx?WSDL");
    $ns = "http://api.exigo.com/";
    $auth = array()
    $auth["LoginName"] = new SoapVar("yourLoginName",XSD_STRING,null,null,null,$ns);
    $auth["Password"] = new SoapVar("yourPassword",XSD_STRING,null,null,null,$ns);
    $auth["Company"] = new SoapVar("yourCompany",XSD_STRING,null,null,null,$ns);
    $headerBody = new SoapVar($auth, SOAP_ENC_OBJECT);
    $header = new SoapHeader($ns, 'ApiAuthentication', $headerBody);
    $api->__setSoapHeaders(array($header));

    //Create Request

    $req->LoginName = "1";

    //Send Request to Server and Get Response
    $res = $api.GetUserPermissions($req);

    //Now examine the results:
}
catch (SoapFault $ex)
{
    echo "Error: ", $ex->getMessage();
}
?>
```

</details>

<details><summary>Java</summary>

_Note: Java is not officially supported._

```java
try
{
    //Create Main API Context Object
    ExigoApi api = new ExigoApi();

    //Create Authentication Header
    ApiAuthentication auth = new ApiAuthentication();
    auth.setLoginName("yourLoginName");
    auth.setPassword("yourPassword");
    auth.setCompany("yourCompany");
    api.setApiAuthenticationValue(auth);

    //Create Request
    GetUserPermissionsRequest req = new GetUserPermissionsRequest();

    req.setLoginName("1");

    //Send Request to Server and Get Response
    GetUserPermissionsResponse res = api.getExigoApiSoap().getUserPermissions(req, auth);

    //Now examine the results:
}
catch (Exception ex)
{
    System.out.println("Error: " + ex.getMessage());
}
```

</details>

<details><summary>CSV</summary>

_This method does not support csv output._

```text
© 2026 Exigo.
```

</details>

---
