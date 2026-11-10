# Exigo API — Other

API version v2025.11.7.6. Crawled 2026-11-11 from https://api.exigo.com/3.0/. Back to [index](../README.md).

| Operation | REST | Summary |
|---|---|---|
| [Validate](#validate) | SOAP only | Validates Business Rules. |
| [VerifyAddress](#verifyaddress) | `POST /3.0/address/verify` | Verifies and cleans up an address. |
| [GetSession](#getsession) | `GET /3.0/session?sessionID=1` | Gets a generic session string for a unique sessionID. |
| [SetSession](#setsession) | `PUT /3.0/session` | Sets a generic session string for a unique sessionID. |
| [CreateWarehouse](#createwarehouse) | `POST /3.0/warehouse` | Creates a new Warehouse |
| [SendEmail](#sendemail) | `POST /3.0/email` | Sends a specified Email using SendGrid |
| [GetBankAccountTypes](#getbankaccounttypes) | `GET /3.0/settings/bankaccounttypes?bankAccountTyId=1` | Gets the existing Bank Account Types. |
| [AddBankAccountType](#addbankaccounttype) | `POST /3.0/settings/bankaccounttype` | Adds a Bank Account Type. |
| [DeleteBankAccountType](#deletebankaccounttype) | `DELETE /3.0/settings/bankaccounttype` | Deletes a Bank Account Type. |
| [EditBankAccountType](#editbankaccounttype) | `PUT /3.0/settings/bankaccounttype` | Edits an existing Bank Account Type. |
| [GetApiWhitelist](#getapiwhitelist) | `GET /3.0/whitelist/api?ipRangeID=1` | Get List of Whitelisted IP ranges |
| [CreateApiWhitelist](#createapiwhitelist) | `POST /3.0/whitelist/api` | Create a new Whitelisted IP range |
| [RemoveApiWhitelist](#removeapiwhitelist) | `DELETE /3.0/whitelist/api` | Remove an existing Whitelisted IP range |
| [CreateAdminWhitelist](#createadminwhitelist) | `POST /3.0/whitelist/admin` | Create a new Whitelisted IP range for Admin |
| [GetAdminWhitelist](#getadminwhitelist) | `GET /3.0/whitelist/adminAuthorization:` | Get List of Whitelisted IP ranges for Admin |
| [RemoveAdminWhitelist](#removeadminwhitelist) | `DELETE /3.0/whitelist/admin` | Remove an existing Whitelisted IP range from Admin |

---
### Validate

>  Validates Business Rules.

| | |
|---|---|
| Category | Other |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/Validate` |
| WSDL elements | `ValidateRequest` → `ValidateResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=Validate |

#### Input

**`ValidateRequest`**

_No properties._

#### Output

**`ValidateResponse`**

| Property | Type | Notes |
|---|---|---|
| `IsValid` | `Boolean` |  |

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/Validate"

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
    <ValidateRequest xmlns="http://api.exigo.com/" />
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
    <ValidateResult xmlns="http://api.exigo.com/">
      <IsValid>boolean</IsValid>
    </ValidateResult>
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
    var req = new ValidateRequest();

    //Send Request to Server and Get Response
    var res = await api.ValidateAsync(req);

    //Now examine the results:
    Console.WriteLine("IsValid: {0}", res.IsValid);
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
    ValidateRequest req = new ValidateRequest();

    //Send Request to Server and Get Response
    ValidateResponse res = api.Validate(req);

    //Now examine the results:
    Console.WriteLine("IsValid: {0}", res.IsValid);
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
    Dim req as new ValidateRequest()

    'Send Request to Server and Get Response
    Dim res As ValidateResponse = api.Validate(req)

    'Now examine the results:
    Console.WriteLine("IsValid: {0}", res.IsValid)
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

    //Send Request to Server and Get Response
    $res = $api.Validate($req);

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
    ValidateRequest req = new ValidateRequest();

    //Send Request to Server and Get Response
    ValidateResponse res = api.getExigoApiSoap().validate(req, auth);

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

### VerifyAddress

> Verifies and cleans up an address.

| | |
|---|---|
| Category | Other |
| REST | `POST /3.0/address/verify` |
| SOAP action | `https://api.exigo.com/VerifyAddress` |
| WSDL elements | `VerifyAddressRequest` → `VerifyAddressResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=VerifyAddress |

#### Input

**`VerifyAddressRequest`**

| Property | Type | Notes |
|---|---|---|
| `Address` | `String` | Optional. |
| `City` | `String` | Optional. |
| `State` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Zip` | `String` | Optional. |
| `Country` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |

#### Output

**`VerifyAddressResponse`**

| Property | Type | Notes |
|---|---|---|
| `Address` | `String` |  |
| `City` | `String` |  |
| `County` | `String` |  |
| `State` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| `Zip` | `String` |  |
| `Country` | `String` | **Lookup:** company-specific list (see company-lists.md) |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/address/verify HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "address": "",
  "city": "",
  "zip": ""
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "address": "",
  "city": "",
  "county": "",
  "state": "",
  "zip": "",
  "country": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/VerifyAddress"

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
    <VerifyAddressRequest xmlns="http://api.exigo.com/">
      <Address>string</Address>
      <City>string</City>
      <State>string</State>
      <Zip>string</Zip>
      <Country>string</Country>
    </VerifyAddressRequest>
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
    <VerifyAddressResult xmlns="http://api.exigo.com/">
      <Address>string</Address>
      <City>string</City>
      <County>string</County>
      <State>string</State>
      <Zip>string</Zip>
      <Country>string</Country>
    </VerifyAddressResult>
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
    var req = new VerifyAddressRequest();

    req.Address = "1";
    req.City = "1";
    req.Zip = "1";

    //Send Request to Server and Get Response
    var res = await api.VerifyAddressAsync(req);

    //Now examine the results:
    Console.WriteLine("Address: {0}", res.Address);
    Console.WriteLine("City: {0}", res.City);
    Console.WriteLine("County: {0}", res.County);
    Console.WriteLine("Zip: {0}", res.Zip);
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
    VerifyAddressRequest req = new VerifyAddressRequest();

    req.Address = "1";
    req.City = "1";
    req.Zip = "1";

    //Send Request to Server and Get Response
    VerifyAddressResponse res = api.VerifyAddress(req);

    //Now examine the results:
    Console.WriteLine("Address: {0}", res.Address);
    Console.WriteLine("City: {0}", res.City);
    Console.WriteLine("County: {0}", res.County);
    Console.WriteLine("Zip: {0}", res.Zip);
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
    Dim req as new VerifyAddressRequest()

    req.Address = "1"
    req.City = "1"
    req.Zip = "1"

    'Send Request to Server and Get Response
    Dim res As VerifyAddressResponse = api.VerifyAddress(req)

    'Now examine the results:
    Console.WriteLine("Address: {0}", res.Address)
    Console.WriteLine("City: {0}", res.City)
    Console.WriteLine("County: {0}", res.County)
    Console.WriteLine("Zip: {0}", res.Zip)
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

    $req->Address = "1";
    $req->City = "1";
    $req->Zip = "1";

    //Send Request to Server and Get Response
    $res = $api.VerifyAddress($req);

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
    VerifyAddressRequest req = new VerifyAddressRequest();

    req.setAddress("1");
    req.setCity("1");
    req.setZip("1");

    //Send Request to Server and Get Response
    VerifyAddressResponse res = api.getExigoApiSoap().verifyAddress(req, auth);

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

### GetSession

> Gets a generic session string for a unique sessionID.

| | |
|---|---|
| Category | Other |
| REST | `GET /3.0/session?sessionID=1` |
| SOAP action | `https://api.exigo.com/GetSession` |
| WSDL elements | `GetSessionRequest` → `GetSessionResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetSession |

#### Input

**`GetSessionRequest`**

| Property | Type | Notes |
|---|---|---|
| `SessionID` | `String` | Optional. |

#### Output

**`GetSessionResponse`**

| Property | Type | Notes |
|---|---|---|
| `SessionData` | `String` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/session?sessionID=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "sessionData": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetSession"

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
    <GetSessionRequest xmlns="http://api.exigo.com/">
      <SessionID>string</SessionID>
    </GetSessionRequest>
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
    <GetSessionResult xmlns="http://api.exigo.com/">
      <SessionData>string</SessionData>
    </GetSessionResult>
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
    var req = new GetSessionRequest();

    req.SessionID = "1";

    //Send Request to Server and Get Response
    var res = await api.GetSessionAsync(req);

    //Now examine the results:
    Console.WriteLine("SessionData: {0}", res.SessionData);
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
    GetSessionRequest req = new GetSessionRequest();

    req.SessionID = "1";

    //Send Request to Server and Get Response
    GetSessionResponse res = api.GetSession(req);

    //Now examine the results:
    Console.WriteLine("SessionData: {0}", res.SessionData);
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
    Dim req as new GetSessionRequest()

    req.SessionID = "1"

    'Send Request to Server and Get Response
    Dim res As GetSessionResponse = api.GetSession(req)

    'Now examine the results:
    Console.WriteLine("SessionData: {0}", res.SessionData)
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

    $req->SessionID = "1";

    //Send Request to Server and Get Response
    $res = $api.GetSession($req);

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
    GetSessionRequest req = new GetSessionRequest();

    req.setSessionID("1");

    //Send Request to Server and Get Response
    GetSessionResponse res = api.getExigoApiSoap().getSession(req, auth);

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

### SetSession

> Sets a generic session string for a unique sessionID.

| | |
|---|---|
| Category | Other |
| REST | `PUT /3.0/session` |
| SOAP action | `https://api.exigo.com/SetSession` |
| WSDL elements | `SetSessionRequest` → `SetSessionResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=SetSession |

#### Input

**`SetSessionRequest`**

| Property | Type | Notes |
|---|---|---|
| `SessionID` | `String` | Optional. |
| `SessionData` | `String` | Optional. |

#### Output

**`SetSessionResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/session HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "sessionID": "",
  "sessionData": ""
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/SetSession"

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
    <SetSessionRequest xmlns="http://api.exigo.com/">
      <SessionID>string</SessionID>
      <SessionData>string</SessionData>
    </SetSessionRequest>
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
    <SetSessionResult xmlns="http://api.exigo.com/" />
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
    var req = new SetSessionRequest();

    req.SessionID = "1";
    req.SessionData = "1";

    //Send Request to Server and Get Response
    var res = await api.SetSessionAsync(req);

    //Now examine the results:
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
    SetSessionRequest req = new SetSessionRequest();

    req.SessionID = "1";
    req.SessionData = "1";

    //Send Request to Server and Get Response
    SetSessionResponse res = api.SetSession(req);

    //Now examine the results:
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
    Dim req as new SetSessionRequest()

    req.SessionID = "1"
    req.SessionData = "1"

    'Send Request to Server and Get Response
    Dim res As SetSessionResponse = api.SetSession(req)

    'Now examine the results:
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

    $req->SessionID = "1";
    $req->SessionData = "1";

    //Send Request to Server and Get Response
    $res = $api.SetSession($req);

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
    SetSessionRequest req = new SetSessionRequest();

    req.setSessionID("1");
    req.setSessionData("1");

    //Send Request to Server and Get Response
    SetSessionResponse res = api.getExigoApiSoap().setSession(req, auth);

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

### CreateWarehouse

> Creates a new Warehouse

| | |
|---|---|
| Category | Other |
| REST | `POST /3.0/warehouse` |
| SOAP action | `https://api.exigo.com/CreateWarehouse` |
| WSDL elements | `CreateWarehouseRequest` → `CreateWarehouseResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateWarehouse |

#### Input

**`CreateWarehouseRequest`**

| Property | Type | Notes |
|---|---|---|
| `Description` | `String` | Optional. |
| `Address1` | `String` | Optional. |
| `Address2` | `String` | Optional. |
| `City` | `String` | Optional. |
| `State` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Zip` | `String` | Optional. |
| `Country` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Currencies` | `String[]` |  |

#### Output

**`CreateWarehouseResponse`**

| Property | Type | Notes |
|---|---|---|
| `Warehouse` | `WarehouseResponse` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/warehouse HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "description": "",
  "address1": "",
  "address2": "",
  "city": "",
  "zip": "",
  "currencies": null
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "warehouse": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateWarehouse"

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
    <CreateWarehouseRequest xmlns="http://api.exigo.com/">
      <Description>string</Description>
      <Address1>string</Address1>
      <Address2>string</Address2>
      <City>string</City>
      <State>string</State>
      <Zip>string</Zip>
      <Country>string</Country>
      <Currencies>
        <string>string</string>
      </Currencies>
    </CreateWarehouseRequest>
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
    <CreateWarehouseResult xmlns="http://api.exigo.com/">
      <Warehouse>
        <WarehouseID>int</WarehouseID>
        <Description>string</Description>
        <Address1>string</Address1>
        <Address2>string</Address2>
        <City>string</City>
        <State>string</State>
        <Zip>string</Zip>
        <Country>string</Country>
      </Warehouse>
    </CreateWarehouseResult>
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
    var req = new CreateWarehouseRequest();

    req.Description = "1";
    req.Address1 = "1";
    req.Address2 = "1";
    req.City = "1";
    req.Zip = "1";

    //Add Currencies
    var currencies = new List<String>();
    currencies.Add("1");
    currencies.Add("2");

    //Now attach the list to the request
    req.Currencies = currencies.ToArray();

    //Send Request to Server and Get Response
    var res = await api.CreateWarehouseAsync(req);

    //Now examine the results:
    Console.WriteLine("Warehouse: {0}", res.Warehouse);
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
    CreateWarehouseRequest req = new CreateWarehouseRequest();

    req.Description = "1";
    req.Address1 = "1";
    req.Address2 = "1";
    req.City = "1";
    req.Zip = "1";

    //Add Currencies
    List<String> currencies = new List<String>();
    currencies.Add("1");
    currencies.Add("2");

    //Now attach the list to the request
    req.Currencies = currencies.ToArray();

    //Send Request to Server and Get Response
    CreateWarehouseResponse res = api.CreateWarehouse(req);

    //Now examine the results:
    Console.WriteLine("Warehouse: {0}", res.Warehouse);
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
    Dim req as new CreateWarehouseRequest()

    req.Description = "1"
    req.Address1 = "1"
    req.Address2 = "1"
    req.City = "1"
    req.Zip = "1"

    'Add Currencies
    Dim currencies As New List(Of String)()
    currencies.Add("1")
    currencies.Add("2")

    'Now attach the list to the request
    req.Currencies = currencies.ToArray()

    'Send Request to Server and Get Response
    Dim res As CreateWarehouseResponse = api.CreateWarehouse(req)

    'Now examine the results:
    Console.WriteLine("Warehouse: {0}", res.Warehouse)
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

    $req->Description = "1";
    $req->Address1 = "1";
    $req->Address2 = "1";
    $req->City = "1";
    $req->Zip = "1";

    //Add Currencies

    $currencie1->Chars = 1;
    $currencie1->Length = 1;

    $currencie2->Chars = 2;
    $currencie2->Length = 2;

    //Now attach the list to the request
    req.Currencies = array(currencie1,currencie2);

    //Send Request to Server and Get Response
    $res = $api.CreateWarehouse($req);

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
    CreateWarehouseRequest req = new CreateWarehouseRequest();

    req.setDescription("1");
    req.setAddress1("1");
    req.setAddress2("1");
    req.setCity("1");
    req.setZip("1");

    //Add Currencies
    ArrayOfSystem.String currencies = new ArrayOfSystem.String();

    String currencie1 = new String();
    currencie1.setChars(1);
    currencie1.setLength(1);
    currencies.Add(currencie1);

    String currencie2 = new String();
    currencie2.setChars(2);
    currencie2.setLength(2);
    currencies.Add(currencie2);

    //Now attach the list to the request
    req.setCurrencies(currencies);

    //Send Request to Server and Get Response
    CreateWarehouseResponse res = api.getExigoApiSoap().createWarehouse(req, auth);

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

### SendEmail

>  Sends a specified Email using SendGrid

| | |
|---|---|
| Category | Other |
| REST | `POST /3.0/email` |
| SOAP action | `https://api.exigo.com/SendEmail` |
| WSDL elements | `SendEmailRequest` → `SendEmailResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=SendEmail |

#### Input

**`SendEmailRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Optional. CustomerID the email will be logged as being sent to. |
| `MailFrom` | `String` | Mail Address the email will be sent from. |
| `MailTo` | `String` | Mail Address the email will be sent to, will use customer email is not specified. |
| `Subject` | `String` | Email Subject line. |
| `Body` | `String` | Email Body. |
| `CustomerKey` | `String` | Optional. CustomerKey the email will be logged as being sent to. |

#### Output

**`SendEmailResponse`**

_No properties._

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/email HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "mailFrom": "company@test.com",
  "mailTo": "customer@test.com",
  "subject": "1",
  "body": "1",
  "customerKey": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/SendEmail"

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
    <SendEmailRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <MailFrom>string</MailFrom>
      <MailTo>string</MailTo>
      <Subject>string</Subject>
      <Body>string</Body>
      <CustomerKey>string</CustomerKey>
    </SendEmailRequest>
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
    <SendEmailResult xmlns="http://api.exigo.com/" />
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
    var req = new SendEmailRequest();

    req.CustomerID = 1;             //CustomerID the email will be logged as being sent to
    req.MailFrom = "company@test.com";//Mail Address the email will be sent from
    req.MailTo = "customer@test.com";//Mail Address the email will be sent to, will use customer email is not specified
    req.Subject = "1";              //Email Subject line
    req.Body = "1";                 //Email Body
    req.CustomerKey = "1";          //CustomerKey the email will be logged as being sent to

    //Send Request to Server and Get Response
    var res = await api.SendEmailAsync(req);

    //Now examine the results:
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
    SendEmailRequest req = new SendEmailRequest();

    req.CustomerID = 1;             //CustomerID the email will be logged as being sent to
    req.MailFrom = "company@test.com";//Mail Address the email will be sent from
    req.MailTo = "customer@test.com";//Mail Address the email will be sent to, will use customer email is not specified
    req.Subject = "1";              //Email Subject line
    req.Body = "1";                 //Email Body
    req.CustomerKey = "1";          //CustomerKey the email will be logged as being sent to

    //Send Request to Server and Get Response
    SendEmailResponse res = api.SendEmail(req);

    //Now examine the results:
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
    Dim req as new SendEmailRequest()

    req.CustomerID = 1
    req.MailFrom = "company@test.com"
    req.MailTo = "customer@test.com"
    req.Subject = "1"
    req.Body = "1"
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As SendEmailResponse = api.SendEmail(req)

    'Now examine the results:
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

    $req->CustomerID = 1;
    $req->MailFrom = "company@test.com";
    $req->MailTo = "customer@test.com";
    $req->Subject = "1";
    $req->Body = "1";
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.SendEmail($req);

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
    SendEmailRequest req = new SendEmailRequest();

    req.setCustomerID(1);
    req.setMailFrom("company@test.com");
    req.setMailTo("customer@test.com");
    req.setSubject("1");
    req.setBody("1");
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    SendEmailResponse res = api.getExigoApiSoap().sendEmail(req, auth);

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

### GetBankAccountTypes

> Gets the existing Bank Account Types.

| | |
|---|---|
| Category | Other |
| REST | `GET /3.0/settings/bankaccounttypes?bankAccountTyId=1` |
| SOAP action | `https://api.exigo.com/GetBankAccountTypes` |
| WSDL elements | `GetBankAccountTypesRequest` → `GetBankAccountTypesResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetBankAccountTypes |

#### Input

**`GetBankAccountTypesRequest`**

| Property | Type | Notes |
|---|---|---|
| `BankAccountTyId` | `Int32` | Optional. |
| `Description` | `String` | Optional. |

#### Output

**`GetBankAccountTypesResponse`**

| Property | Type | Notes |
|---|---|---|
| `BankAccountTypes` | `BankAccountTypeResponse[]` |  |

**`BankAccountTypeResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `BankAccountTyId` | `Int32` |  |
| &nbsp;&nbsp;↳ `Description` | `String` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/settings/bankaccounttypes?bankAccountTyId=1
  &description=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "bankAccountTypes": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetBankAccountTypes"

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
    <GetBankAccountTypesRequest xmlns="http://api.exigo.com/">
      <BankAccountTyId>int</BankAccountTyId>
      <Description>string</Description>
    </GetBankAccountTypesRequest>
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
    <GetBankAccountTypesResult xmlns="http://api.exigo.com/">
      <BankAccountTypes>
        <BankAccountTypeResponse>
          <BankAccountTyId>int</BankAccountTyId>
          <Description>string</Description>
        </BankAccountTypeResponse>
      </BankAccountTypes>
    </GetBankAccountTypesResult>
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
    var req = new GetBankAccountTypesRequest();

    req.BankAccountTyId = 1;
    req.Description = "1";

    //Send Request to Server and Get Response
    var res = await api.GetBankAccountTypesAsync(req);

    //Now examine the results:

    foreach (var bankAccountType  in res.BankAccountTypes)
    {
        Console.WriteLine("BankAccountTyId: {0}", bankAccountType.BankAccountTyId);
        Console.WriteLine("Description: {0}", bankAccountType.Description);
    }
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
    GetBankAccountTypesRequest req = new GetBankAccountTypesRequest();

    req.BankAccountTyId = 1;
    req.Description = "1";

    //Send Request to Server and Get Response
    GetBankAccountTypesResponse res = api.GetBankAccountTypes(req);

    //Now examine the results:

    foreach (BankAccountTypeResponse bankAccountType  in res.BankAccountTypes)
    {
        Console.WriteLine("BankAccountTyId: {0}", bankAccountType.BankAccountTyId);
        Console.WriteLine("Description: {0}", bankAccountType.Description);
    }
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
    Dim req as new GetBankAccountTypesRequest()

    req.BankAccountTyId = 1
    req.Description = "1"

    'Send Request to Server and Get Response
    Dim res As GetBankAccountTypesResponse = api.GetBankAccountTypes(req)

    'Now examine the results:

    For Each bankAccountType As BankAccountTypeResponse In res.BankAccountTypes
        Console.WriteLine("BankAccountTyId: {0}", bankAccountType.BankAccountTyId)
        Console.WriteLine("Description: {0}", bankAccountType.Description)
    Next
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

    $req->BankAccountTyId = 1;
    $req->Description = "1";

    //Send Request to Server and Get Response
    $res = $api.GetBankAccountTypes($req);

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
    GetBankAccountTypesRequest req = new GetBankAccountTypesRequest();

    req.setBankAccountTyId(1);
    req.setDescription("1");

    //Send Request to Server and Get Response
    GetBankAccountTypesResponse res = api.getExigoApiSoap().getBankAccountTypes(req, auth);

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

### AddBankAccountType

> Adds a Bank Account Type.

| | |
|---|---|
| Category | Other |
| REST | `POST /3.0/settings/bankaccounttype` |
| SOAP action | `https://api.exigo.com/AddBankAccountType` |
| WSDL elements | `AddBankAccountTypeRequest` → `AddBankAccountTypeResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=AddBankAccountType |

#### Input

**`AddBankAccountTypeRequest`**

| Property | Type | Notes |
|---|---|---|
| `Description` | `String` | Optional. |

#### Output

**`AddBankAccountTypeResponse`**

| Property | Type | Notes |
|---|---|---|
| `BankAccountTyId` | `Int32` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/settings/bankaccounttype HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "description": ""
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "bankAccountTyId": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/AddBankAccountType"

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
    <AddBankAccountTypeRequest xmlns="http://api.exigo.com/">
      <Description>string</Description>
    </AddBankAccountTypeRequest>
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
    <AddBankAccountTypeResult xmlns="http://api.exigo.com/">
      <BankAccountTyId>int</BankAccountTyId>
    </AddBankAccountTypeResult>
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
    var req = new AddBankAccountTypeRequest();

    req.Description = "1";

    //Send Request to Server and Get Response
    var res = await api.AddBankAccountTypeAsync(req);

    //Now examine the results:
    Console.WriteLine("BankAccountTyId: {0}", res.BankAccountTyId);
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
    AddBankAccountTypeRequest req = new AddBankAccountTypeRequest();

    req.Description = "1";

    //Send Request to Server and Get Response
    AddBankAccountTypeResponse res = api.AddBankAccountType(req);

    //Now examine the results:
    Console.WriteLine("BankAccountTyId: {0}", res.BankAccountTyId);
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
    Dim req as new AddBankAccountTypeRequest()

    req.Description = "1"

    'Send Request to Server and Get Response
    Dim res As AddBankAccountTypeResponse = api.AddBankAccountType(req)

    'Now examine the results:
    Console.WriteLine("BankAccountTyId: {0}", res.BankAccountTyId)
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

    $req->Description = "1";

    //Send Request to Server and Get Response
    $res = $api.AddBankAccountType($req);

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
    AddBankAccountTypeRequest req = new AddBankAccountTypeRequest();

    req.setDescription("1");

    //Send Request to Server and Get Response
    AddBankAccountTypeResponse res = api.getExigoApiSoap().addBankAccountType(req, auth);

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

### DeleteBankAccountType

> Deletes a Bank Account Type.

| | |
|---|---|
| Category | Other |
| REST | `DELETE /3.0/settings/bankaccounttype` |
| SOAP action | `https://api.exigo.com/DeleteBankAccountType` |
| WSDL elements | `DeleteBankAccountTypeRequest` → `DeleteBankAccountTypeResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DeleteBankAccountType |

#### Input

**`DeleteBankAccountTypeRequest`**

| Property | Type | Notes |
|---|---|---|
| `BankAccountTyId` | `Int32` |  |

#### Output

**`DeleteBankAccountTypeResponse`**

_No properties._

#### REST example

```http
DELETE https://yourcompany-api.exigo.com/3.0/settings/bankaccounttype HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "bankAccountTyId": 1
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/DeleteBankAccountType"

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
    <DeleteBankAccountTypeRequest xmlns="http://api.exigo.com/">
      <BankAccountTyId>int</BankAccountTyId>
    </DeleteBankAccountTypeRequest>
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
    <DeleteBankAccountTypeResult xmlns="http://api.exigo.com/" />
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
    var req = new DeleteBankAccountTypeRequest();

    req.BankAccountTyId = 1;

    //Send Request to Server and Get Response
    var res = await api.DeleteBankAccountTypeAsync(req);

    //Now examine the results:
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
    DeleteBankAccountTypeRequest req = new DeleteBankAccountTypeRequest();

    req.BankAccountTyId = 1;

    //Send Request to Server and Get Response
    DeleteBankAccountTypeResponse res = api.DeleteBankAccountType(req);

    //Now examine the results:
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
    Dim req as new DeleteBankAccountTypeRequest()

    req.BankAccountTyId = 1

    'Send Request to Server and Get Response
    Dim res As DeleteBankAccountTypeResponse = api.DeleteBankAccountType(req)

    'Now examine the results:
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

    $req->BankAccountTyId = 1;

    //Send Request to Server and Get Response
    $res = $api.DeleteBankAccountType($req);

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
    DeleteBankAccountTypeRequest req = new DeleteBankAccountTypeRequest();

    req.setBankAccountTyId(1);

    //Send Request to Server and Get Response
    DeleteBankAccountTypeResponse res = api.getExigoApiSoap().deleteBankAccountType(req, auth);

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

### EditBankAccountType

> Edits an existing Bank Account Type.

| | |
|---|---|
| Category | Other |
| REST | `PUT /3.0/settings/bankaccounttype` |
| SOAP action | `https://api.exigo.com/EditBankAccountType` |
| WSDL elements | `EditBankAccountTypeRequest` → `EditBankAccountTypeResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=EditBankAccountType |

#### Input

**`EditBankAccountTypeRequest`**

| Property | Type | Notes |
|---|---|---|
| `BankAccountTyId` | `Int32` |  |
| `Description` | `String` | Optional. |

#### Output

**`EditBankAccountTypeResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/settings/bankaccounttype HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "bankAccountTyId": 1,
  "description": ""
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/EditBankAccountType"

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
    <EditBankAccountTypeRequest xmlns="http://api.exigo.com/">
      <BankAccountTyId>int</BankAccountTyId>
      <Description>string</Description>
    </EditBankAccountTypeRequest>
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
    <EditBankAccountTypeResult xmlns="http://api.exigo.com/" />
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
    var req = new EditBankAccountTypeRequest();

    req.BankAccountTyId = 1;
    req.Description = "1";

    //Send Request to Server and Get Response
    var res = await api.EditBankAccountTypeAsync(req);

    //Now examine the results:
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
    EditBankAccountTypeRequest req = new EditBankAccountTypeRequest();

    req.BankAccountTyId = 1;
    req.Description = "1";

    //Send Request to Server and Get Response
    EditBankAccountTypeResponse res = api.EditBankAccountType(req);

    //Now examine the results:
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
    Dim req as new EditBankAccountTypeRequest()

    req.BankAccountTyId = 1
    req.Description = "1"

    'Send Request to Server and Get Response
    Dim res As EditBankAccountTypeResponse = api.EditBankAccountType(req)

    'Now examine the results:
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

    $req->BankAccountTyId = 1;
    $req->Description = "1";

    //Send Request to Server and Get Response
    $res = $api.EditBankAccountType($req);

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
    EditBankAccountTypeRequest req = new EditBankAccountTypeRequest();

    req.setBankAccountTyId(1);
    req.setDescription("1");

    //Send Request to Server and Get Response
    EditBankAccountTypeResponse res = api.getExigoApiSoap().editBankAccountType(req, auth);

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

### GetApiWhitelist

> Get List of Whitelisted IP ranges

| | |
|---|---|
| Category | Other |
| REST | `GET /3.0/whitelist/api?ipRangeID=1` |
| SOAP action | `https://api.exigo.com/GetApiWhitelist` |
| WSDL elements | `GetApiWhitelistRequest` → `GetApiWhitelistResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetApiWhitelist |

#### Input

**`GetApiWhitelistRequest`**

| Property | Type | Notes |
|---|---|---|
| `IpRangeID` | `Int32` | Optional. Optionally provide an IpRangeID to return only that range. |

#### Output

**`GetApiWhitelistResponse`**

| Property | Type | Notes |
|---|---|---|
| `WhitelistRanges` | `ApiWhitelistResponse[]` |  |

**`ApiWhitelistResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `IpRangeID` | `Int32` |  |
| &nbsp;&nbsp;↳ `Description` | `String` |  |
| &nbsp;&nbsp;↳ `MinIP` | `String` |  |
| &nbsp;&nbsp;↳ `MaxIP` | `String` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/whitelist/api?ipRangeID=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "whitelistRanges": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetApiWhitelist"

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
    <GetApiWhitelistRequest xmlns="http://api.exigo.com/">
      <IpRangeID>int</IpRangeID>
    </GetApiWhitelistRequest>
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
    <GetApiWhitelistResult xmlns="http://api.exigo.com/">
      <WhitelistRanges>
        <ApiWhitelistResponse>
          <IpRangeID>int</IpRangeID>
          <Description>string</Description>
          <MinIP>string</MinIP>
          <MaxIP>string</MaxIP>
        </ApiWhitelistResponse>
      </WhitelistRanges>
    </GetApiWhitelistResult>
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
    var req = new GetApiWhitelistRequest();

    req.IpRangeID = 1;              //Optionally provide an IpRangeID to return only that range

    //Send Request to Server and Get Response
    var res = await api.GetApiWhitelistAsync(req);

    //Now examine the results:

    foreach (var apiWhitelist  in res.WhitelistRanges)
    {
        Console.WriteLine("IpRangeID: {0}", apiWhitelist.IpRangeID);
        Console.WriteLine("Description: {0}", apiWhitelist.Description);
        Console.WriteLine("MinIP: {0}", apiWhitelist.MinIP);
        Console.WriteLine("MaxIP: {0}", apiWhitelist.MaxIP);
    }
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
    GetApiWhitelistRequest req = new GetApiWhitelistRequest();

    req.IpRangeID = 1;              //Optionally provide an IpRangeID to return only that range

    //Send Request to Server and Get Response
    GetApiWhitelistResponse res = api.GetApiWhitelist(req);

    //Now examine the results:

    foreach (ApiWhitelistResponse apiWhitelist  in res.WhitelistRanges)
    {
        Console.WriteLine("IpRangeID: {0}", apiWhitelist.IpRangeID);
        Console.WriteLine("Description: {0}", apiWhitelist.Description);
        Console.WriteLine("MinIP: {0}", apiWhitelist.MinIP);
        Console.WriteLine("MaxIP: {0}", apiWhitelist.MaxIP);
    }
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
    Dim req as new GetApiWhitelistRequest()

    req.IpRangeID = 1

    'Send Request to Server and Get Response
    Dim res As GetApiWhitelistResponse = api.GetApiWhitelist(req)

    'Now examine the results:

    For Each apiWhitelist As ApiWhitelistResponse In res.WhitelistRanges
        Console.WriteLine("IpRangeID: {0}", apiWhitelist.IpRangeID)
        Console.WriteLine("Description: {0}", apiWhitelist.Description)
        Console.WriteLine("MinIP: {0}", apiWhitelist.MinIP)
        Console.WriteLine("MaxIP: {0}", apiWhitelist.MaxIP)
    Next
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

    $req->IpRangeID = 1;

    //Send Request to Server and Get Response
    $res = $api.GetApiWhitelist($req);

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
    GetApiWhitelistRequest req = new GetApiWhitelistRequest();

    req.setIpRangeID(1);

    //Send Request to Server and Get Response
    GetApiWhitelistResponse res = api.getExigoApiSoap().getApiWhitelist(req, auth);

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

### CreateApiWhitelist

> Create a new Whitelisted IP range

| | |
|---|---|
| Category | Other |
| REST | `POST /3.0/whitelist/api` |
| SOAP action | `https://api.exigo.com/CreateApiWhitelist` |
| WSDL elements | `CreateApiWhitelistRequest` → `CreateApiWhitelistResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateApiWhitelist |

#### Input

**`CreateApiWhitelistRequest`**

| Property | Type | Notes |
|---|---|---|
| `Description` | `String` |  |
| `MinIP` | `String` |  |
| `MaxIP` | `String` | Optional. Can be provided for whitelisting a range, if not provided only the MinIP address will be whitelisted. |

#### Output

**`CreateApiWhitelistResponse`**

| Property | Type | Notes |
|---|---|---|
| `IPRangeID` | `Int32` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/whitelist/api HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "description": "1",
  "minIP": "1",
  "maxIP": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "iPRangeID": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateApiWhitelist"

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
    <CreateApiWhitelistRequest xmlns="http://api.exigo.com/">
      <Description>string</Description>
      <MinIP>string</MinIP>
      <MaxIP>string</MaxIP>
    </CreateApiWhitelistRequest>
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
    <CreateApiWhitelistResult xmlns="http://api.exigo.com/">
      <IPRangeID>int</IPRangeID>
    </CreateApiWhitelistResult>
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
    var req = new CreateApiWhitelistRequest();

    req.Description = "1";
    req.MinIP = "1";
    req.MaxIP = "1";                //Can be provided for whitelisting a range, if not provided only the MinIP address will be whitelisted

    //Send Request to Server and Get Response
    var res = await api.CreateApiWhitelistAsync(req);

    //Now examine the results:
    Console.WriteLine("IPRangeID: {0}", res.IPRangeID);
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
    CreateApiWhitelistRequest req = new CreateApiWhitelistRequest();

    req.Description = "1";
    req.MinIP = "1";
    req.MaxIP = "1";                //Can be provided for whitelisting a range, if not provided only the MinIP address will be whitelisted

    //Send Request to Server and Get Response
    CreateApiWhitelistResponse res = api.CreateApiWhitelist(req);

    //Now examine the results:
    Console.WriteLine("IPRangeID: {0}", res.IPRangeID);
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
    Dim req as new CreateApiWhitelistRequest()

    req.Description = "1"
    req.MinIP = "1"
    req.MaxIP = "1"

    'Send Request to Server and Get Response
    Dim res As CreateApiWhitelistResponse = api.CreateApiWhitelist(req)

    'Now examine the results:
    Console.WriteLine("IPRangeID: {0}", res.IPRangeID)
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

    $req->Description = "1";
    $req->MinIP = "1";
    $req->MaxIP = "1";

    //Send Request to Server and Get Response
    $res = $api.CreateApiWhitelist($req);

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
    CreateApiWhitelistRequest req = new CreateApiWhitelistRequest();

    req.setDescription("1");
    req.setMinIP("1");
    req.setMaxIP("1");

    //Send Request to Server and Get Response
    CreateApiWhitelistResponse res = api.getExigoApiSoap().createApiWhitelist(req, auth);

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

### RemoveApiWhitelist

> Remove an existing Whitelisted IP range

| | |
|---|---|
| Category | Other |
| REST | `DELETE /3.0/whitelist/api` |
| SOAP action | `https://api.exigo.com/RemoveApiWhitelist` |
| WSDL elements | `RemoveApiWhitelistRequest` → `RemoveApiWhitelistResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=RemoveApiWhitelist |

#### Input

**`RemoveApiWhitelistRequest`**

| Property | Type | Notes |
|---|---|---|
| `IPRangeID` | `Int32` |  |

#### Output

**`RemoveApiWhitelistResponse`**

_No properties._

#### REST example

```http
DELETE https://yourcompany-api.exigo.com/3.0/whitelist/api HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "iPRangeID": 1
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/RemoveApiWhitelist"

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
    <RemoveApiWhitelistRequest xmlns="http://api.exigo.com/">
      <IPRangeID>int</IPRangeID>
    </RemoveApiWhitelistRequest>
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
    <RemoveApiWhitelistResult xmlns="http://api.exigo.com/" />
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
    var req = new RemoveApiWhitelistRequest();

    req.IPRangeID = 1;

    //Send Request to Server and Get Response
    var res = await api.RemoveApiWhitelistAsync(req);

    //Now examine the results:
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
    RemoveApiWhitelistRequest req = new RemoveApiWhitelistRequest();

    req.IPRangeID = 1;

    //Send Request to Server and Get Response
    RemoveApiWhitelistResponse res = api.RemoveApiWhitelist(req);

    //Now examine the results:
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
    Dim req as new RemoveApiWhitelistRequest()

    req.IPRangeID = 1

    'Send Request to Server and Get Response
    Dim res As RemoveApiWhitelistResponse = api.RemoveApiWhitelist(req)

    'Now examine the results:
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

    $req->IPRangeID = 1;

    //Send Request to Server and Get Response
    $res = $api.RemoveApiWhitelist($req);

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
    RemoveApiWhitelistRequest req = new RemoveApiWhitelistRequest();

    req.setIPRangeID(1);

    //Send Request to Server and Get Response
    RemoveApiWhitelistResponse res = api.getExigoApiSoap().removeApiWhitelist(req, auth);

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

### CreateAdminWhitelist

> Create a new Whitelisted IP range for Admin

| | |
|---|---|
| Category | Other |
| REST | `POST /3.0/whitelist/admin` |
| SOAP action | `https://api.exigo.com/CreateAdminWhitelist` |
| WSDL elements | `CreateAdminWhitelistRequest` → `CreateAdminWhitelistResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateAdminWhitelist |

#### Input

**`CreateAdminWhitelistRequest`**

| Property | Type | Notes |
|---|---|---|
| `Description` | `String` | Optional. |
| `MinIP` | `String` |  |
| `MaxIP` | `String` | Optional. Can be provided for whitelisting a range, if not provided only the MinIP address will be whitelisted. |

#### Output

**`CreateAdminWhitelistResponse`**

| Property | Type | Notes |
|---|---|---|
| `IPRangeID` | `Int32` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/whitelist/admin HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "description": "",
  "maxIP": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "iPRangeID": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateAdminWhitelist"

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
    <CreateAdminWhitelistRequest xmlns="http://api.exigo.com/">
      <Description>string</Description>
      <MinIP>string</MinIP>
      <MaxIP>string</MaxIP>
    </CreateAdminWhitelistRequest>
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
    <CreateAdminWhitelistResult xmlns="http://api.exigo.com/">
      <IPRangeID>int</IPRangeID>
    </CreateAdminWhitelistResult>
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
    var req = new CreateAdminWhitelistRequest();

    req.Description = "1";
    req.MaxIP = "1";                //Can be provided for whitelisting a range, if not provided only the MinIP address will be whitelisted

    //Send Request to Server and Get Response
    var res = await api.CreateAdminWhitelistAsync(req);

    //Now examine the results:
    Console.WriteLine("IPRangeID: {0}", res.IPRangeID);
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
    CreateAdminWhitelistRequest req = new CreateAdminWhitelistRequest();

    req.Description = "1";
    req.MaxIP = "1";                //Can be provided for whitelisting a range, if not provided only the MinIP address will be whitelisted

    //Send Request to Server and Get Response
    CreateAdminWhitelistResponse res = api.CreateAdminWhitelist(req);

    //Now examine the results:
    Console.WriteLine("IPRangeID: {0}", res.IPRangeID);
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
    Dim req as new CreateAdminWhitelistRequest()

    req.Description = "1"
    req.MaxIP = "1"

    'Send Request to Server and Get Response
    Dim res As CreateAdminWhitelistResponse = api.CreateAdminWhitelist(req)

    'Now examine the results:
    Console.WriteLine("IPRangeID: {0}", res.IPRangeID)
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

    $req->Description = "1";
    $req->MaxIP = "1";

    //Send Request to Server and Get Response
    $res = $api.CreateAdminWhitelist($req);

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
    CreateAdminWhitelistRequest req = new CreateAdminWhitelistRequest();

    req.setDescription("1");
    req.setMaxIP("1");

    //Send Request to Server and Get Response
    CreateAdminWhitelistResponse res = api.getExigoApiSoap().createAdminWhitelist(req, auth);

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

### GetAdminWhitelist

> Get List of Whitelisted IP ranges for Admin

| | |
|---|---|
| Category | Other |
| REST | `GET /3.0/whitelist/adminAuthorization:` |
| SOAP action | `https://api.exigo.com/GetAdminWhitelist` |
| WSDL elements | `GetAdminWhitelistRequest` → `GetAdminWhitelistResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetAdminWhitelist |

#### Input

**`GetAdminWhitelistRequest`**

| Property | Type | Notes |
|---|---|---|
| `IpRangeID` | `Int32` | Optional. Optionally provide an IpRangeID to return only that range. |

#### Output

**`GetAdminWhitelistResponse`**

| Property | Type | Notes |
|---|---|---|
| `WhitelistRanges` | `AdminWhitelistResponse[]` |  |

**`AdminWhitelistResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `IpRangeID` | `Int32` |  |
| &nbsp;&nbsp;↳ `MinIP` | `String` |  |
| &nbsp;&nbsp;↳ `MaxIP` | `String` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/whitelist/adminAuthorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "whitelistRanges": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetAdminWhitelist"

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
    <GetAdminWhitelistRequest xmlns="http://api.exigo.com/">
      <IpRangeID>int</IpRangeID>
    </GetAdminWhitelistRequest>
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
    <GetAdminWhitelistResult xmlns="http://api.exigo.com/">
      <WhitelistRanges>
        <AdminWhitelistResponse>
          <IpRangeID>int</IpRangeID>
          <MinIP>string</MinIP>
          <MaxIP>string</MaxIP>
        </AdminWhitelistResponse>
      </WhitelistRanges>
    </GetAdminWhitelistResult>
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
    var req = new GetAdminWhitelistRequest();

    //Send Request to Server and Get Response
    var res = await api.GetAdminWhitelistAsync(req);

    //Now examine the results:

    foreach (var adminWhitelist  in res.WhitelistRanges)
    {
        Console.WriteLine("IpRangeID: {0}", adminWhitelist.IpRangeID);
        Console.WriteLine("MinIP: {0}", adminWhitelist.MinIP);
        Console.WriteLine("MaxIP: {0}", adminWhitelist.MaxIP);
    }
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
    GetAdminWhitelistRequest req = new GetAdminWhitelistRequest();

    //Send Request to Server and Get Response
    GetAdminWhitelistResponse res = api.GetAdminWhitelist(req);

    //Now examine the results:

    foreach (AdminWhitelistResponse adminWhitelist  in res.WhitelistRanges)
    {
        Console.WriteLine("IpRangeID: {0}", adminWhitelist.IpRangeID);
        Console.WriteLine("MinIP: {0}", adminWhitelist.MinIP);
        Console.WriteLine("MaxIP: {0}", adminWhitelist.MaxIP);
    }
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
    Dim req as new GetAdminWhitelistRequest()

    'Send Request to Server and Get Response
    Dim res As GetAdminWhitelistResponse = api.GetAdminWhitelist(req)

    'Now examine the results:

    For Each adminWhitelist As AdminWhitelistResponse In res.WhitelistRanges
        Console.WriteLine("IpRangeID: {0}", adminWhitelist.IpRangeID)
        Console.WriteLine("MinIP: {0}", adminWhitelist.MinIP)
        Console.WriteLine("MaxIP: {0}", adminWhitelist.MaxIP)
    Next
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

    //Send Request to Server and Get Response
    $res = $api.GetAdminWhitelist($req);

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
    GetAdminWhitelistRequest req = new GetAdminWhitelistRequest();

    //Send Request to Server and Get Response
    GetAdminWhitelistResponse res = api.getExigoApiSoap().getAdminWhitelist(req, auth);

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

### RemoveAdminWhitelist

> Remove an existing Whitelisted IP range from Admin

| | |
|---|---|
| Category | Other |
| REST | `DELETE /3.0/whitelist/admin` |
| SOAP action | `https://api.exigo.com/RemoveAdminWhitelist` |
| WSDL elements | `RemoveAdminWhitelistRequest` → `RemoveAdminWhitelistResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=RemoveAdminWhitelist |

#### Input

**`RemoveAdminWhitelistRequest`**

| Property | Type | Notes |
|---|---|---|
| `IPRangeID` | `Int32` |  |

#### Output

**`RemoveAdminWhitelistResponse`**

_No properties._

#### REST example

```http
DELETE https://yourcompany-api.exigo.com/3.0/whitelist/admin HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/RemoveAdminWhitelist"

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
    <RemoveAdminWhitelistRequest xmlns="http://api.exigo.com/">
      <IPRangeID>int</IPRangeID>
    </RemoveAdminWhitelistRequest>
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
    <RemoveAdminWhitelistResult xmlns="http://api.exigo.com/" />
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
    var req = new RemoveAdminWhitelistRequest();

    //Send Request to Server and Get Response
    var res = await api.RemoveAdminWhitelistAsync(req);

    //Now examine the results:
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
    RemoveAdminWhitelistRequest req = new RemoveAdminWhitelistRequest();

    //Send Request to Server and Get Response
    RemoveAdminWhitelistResponse res = api.RemoveAdminWhitelist(req);

    //Now examine the results:
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
    Dim req as new RemoveAdminWhitelistRequest()

    'Send Request to Server and Get Response
    Dim res As RemoveAdminWhitelistResponse = api.RemoveAdminWhitelist(req)

    'Now examine the results:
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

    //Send Request to Server and Get Response
    $res = $api.RemoveAdminWhitelist($req);

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
    RemoveAdminWhitelistRequest req = new RemoveAdminWhitelistRequest();

    //Send Request to Server and Get Response
    RemoveAdminWhitelistResponse res = api.getExigoApiSoap().removeAdminWhitelist(req, auth);

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
