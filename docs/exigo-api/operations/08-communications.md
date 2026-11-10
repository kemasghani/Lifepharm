# Exigo API — Communications

API version v2025.11.7.6. Crawled 2026-11-11 from https://api.exigo.com/3.0/. Back to [index](../README.md).

| Operation | REST | Summary |
|---|---|---|
| [OptInEmail](#optinemail) | `POST /3.0/email/optin` | Setup opt in settings for Email by Email address. |
| [OptInSms](#optinsms) | `POST /3.0/sms/optin` | Setup opt in settings for Sms messaging by phone number. |
| [OptInPushNotification](#optinpushnotification) | `POST /3.0/push/optin` | Setup opt in settings for Push Notifications to mobile devices. |
| [OptOutEmail](#optoutemail) | `POST /3.0/email/optout` | Opts out all customers and customer contacts with specified email from receiving broadcast emails. |
| [OptOutSms](#optoutsms) | `POST /3.0/sms/optout` | Opts out all customers and customer contacts with specified phone number from receiving broadcast SMS messages. |
| [OptOutPushNotification](#optoutpushnotification) | `POST /3.0/push/optout` | Setup opt out settings for Push Notifications to mobile devices. |
| [GetCompanyNews](#getcompanynews) | `GET /3.0/companynews?departmentType=1` | Gets a list of company news descriptions. |
| [GetCompanyNewsItem](#getcompanynewsitem) | `GET /3.0/companynews/item?newsID=1` | Gets company news details. |
| [GetRandomMessage](#getrandommessage) | `GET /3.0/randommessage?languageID=1` | Gets a random message (defined in the Exigo Admin). |
| [FireResponder](#fireresponder) | `POST /3.0/autoresponder/fire` | Fires an email responder to customer or order email address on file. |
| [SendSms](#sendsms) | `POST /3.0/sms` | Sends an SMS message. |
| [SendAuthorizationMFACode](#sendauthorizationmfacode) | `POST /3.0/sms/authorizationmfa` | Sends an Authorization MFA Code SMS message. |

---
### OptInEmail

> Setup opt in settings for Email by Email address.

| | |
|---|---|
| Category | Communications |
| REST | `POST /3.0/email/optin` |
| SOAP action | `https://api.exigo.com/OptInEmail` |
| WSDL elements | `OptInEmailRequest` → `OptInEmailResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=OptInEmail |

#### Input

**`OptInEmailRequest`**

| Property | Type | Notes |
|---|---|---|
| `Email` | `String` | Optional. The address you are opting in. |

#### Output

**`OptInEmailResponse`**

| Property | Type | Notes |
|---|---|---|
| `RecordsAffected` | `Int32` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/email/optin HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "email": "johndoe@email.com"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "recordsAffected": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/OptInEmail"

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
    <OptInEmailRequest xmlns="http://api.exigo.com/">
      <Email>string</Email>
    </OptInEmailRequest>
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
    <OptInEmailResult xmlns="http://api.exigo.com/">
      <RecordsAffected>int</RecordsAffected>
    </OptInEmailResult>
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
    var req = new OptInEmailRequest();

    req.Email = "johndoe@email.com";//The address you are opting in.

    //Send Request to Server and Get Response
    var res = await api.OptInEmailAsync(req);

    //Now examine the results:
    Console.WriteLine("RecordsAffected: {0}", res.RecordsAffected);
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
    OptInEmailRequest req = new OptInEmailRequest();

    req.Email = "johndoe@email.com";//The address you are opting in.

    //Send Request to Server and Get Response
    OptInEmailResponse res = api.OptInEmail(req);

    //Now examine the results:
    Console.WriteLine("RecordsAffected: {0}", res.RecordsAffected);
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
    Dim req as new OptInEmailRequest()

    req.Email = "johndoe@email.com"

    'Send Request to Server and Get Response
    Dim res As OptInEmailResponse = api.OptInEmail(req)

    'Now examine the results:
    Console.WriteLine("RecordsAffected: {0}", res.RecordsAffected)
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

    $req->Email = "johndoe@email.com";

    //Send Request to Server and Get Response
    $res = $api.OptInEmail($req);

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
    OptInEmailRequest req = new OptInEmailRequest();

    req.setEmail("johndoe@email.com");

    //Send Request to Server and Get Response
    OptInEmailResponse res = api.getExigoApiSoap().optInEmail(req, auth);

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

### OptInSms

> Setup opt in settings for Sms messaging by phone number.

| | |
|---|---|
| Category | Communications |
| REST | `POST /3.0/sms/optin` |
| SOAP action | `https://api.exigo.com/OptInSms` |
| WSDL elements | `OptInSmsRequest` → `OptInSmsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=OptInSms |

#### Input

**`OptInSmsRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Optional. The CustomerID being opted in. Use either CustomerID or phone number. |
| `PhoneNumber` | `String` | Optional. The phone number you are opting in. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`OptInSmsResponse`**

| Property | Type | Notes |
|---|---|---|
| `RecordsAffected` | `Int32` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/sms/optin HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "phoneNumber": "(888) 555-1234",
  "customerKey": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "recordsAffected": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/OptInSms"

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
    <OptInSmsRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <PhoneNumber>string</PhoneNumber>
      <CustomerKey>string</CustomerKey>
    </OptInSmsRequest>
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
    <OptInSmsResult xmlns="http://api.exigo.com/">
      <RecordsAffected>int</RecordsAffected>
    </OptInSmsResult>
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
    var req = new OptInSmsRequest();

    req.CustomerID = 1;             //The CustomerID being opted in. Use either CustomerID or phone number.
    req.PhoneNumber = "(888) 555-1234";//The phone number you are opting in.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.OptInSmsAsync(req);

    //Now examine the results:
    Console.WriteLine("RecordsAffected: {0}", res.RecordsAffected);
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
    OptInSmsRequest req = new OptInSmsRequest();

    req.CustomerID = 1;             //The CustomerID being opted in. Use either CustomerID or phone number.
    req.PhoneNumber = "(888) 555-1234";//The phone number you are opting in.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    OptInSmsResponse res = api.OptInSms(req);

    //Now examine the results:
    Console.WriteLine("RecordsAffected: {0}", res.RecordsAffected);
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
    Dim req as new OptInSmsRequest()

    req.CustomerID = 1
    req.PhoneNumber = "(888) 555-1234"
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As OptInSmsResponse = api.OptInSms(req)

    'Now examine the results:
    Console.WriteLine("RecordsAffected: {0}", res.RecordsAffected)
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
    $req->PhoneNumber = "(888) 555-1234";
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.OptInSms($req);

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
    OptInSmsRequest req = new OptInSmsRequest();

    req.setCustomerID(1);
    req.setPhoneNumber("(888) 555-1234");
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    OptInSmsResponse res = api.getExigoApiSoap().optInSms(req, auth);

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

### OptInPushNotification

> Setup opt in settings for Push Notifications to mobile devices.

| | |
|---|---|
| Category | Communications |
| REST | `POST /3.0/push/optin` |
| SOAP action | `https://api.exigo.com/OptInPushNotification` |
| WSDL elements | `optInPushNotificationRequest` → `OptInPushNotificationResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=OptInPushNotification |

#### Input

**`OptInPushNotificationRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`OptInPushNotificationResponse`**

| Property | Type | Notes |
|---|---|---|
| `RecordsAffected` | `Int32` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/push/optin HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "customerKey": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "recordsAffected": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/OptInPushNotification"

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
    <optInPushNotificationRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
    </optInPushNotificationRequest>
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
    <OptInPushNotificationResult xmlns="http://api.exigo.com/">
      <RecordsAffected>int</RecordsAffected>
    </OptInPushNotificationResult>
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
    var req = new OptInPushNotificationRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.OptInPushNotificationAsync(req);

    //Now examine the results:
    Console.WriteLine("RecordsAffected: {0}", res.RecordsAffected);
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
    OptInPushNotificationRequest req = new OptInPushNotificationRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    OptInPushNotificationResponse res = api.OptInPushNotification(req);

    //Now examine the results:
    Console.WriteLine("RecordsAffected: {0}", res.RecordsAffected);
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
    Dim req as new OptInPushNotificationRequest()

    req.CustomerID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As OptInPushNotificationResponse = api.OptInPushNotification(req)

    'Now examine the results:
    Console.WriteLine("RecordsAffected: {0}", res.RecordsAffected)
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
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.OptInPushNotification($req);

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
    OptInPushNotificationRequest req = new OptInPushNotificationRequest();

    req.setCustomerID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    OptInPushNotificationResponse res = api.getExigoApiSoap().optInPushNotification(req, auth);

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

### OptOutEmail

>  Opts out all customers and customer contacts with specified email from receiving broadcast emails.

| | |
|---|---|
| Category | Communications |
| REST | `POST /3.0/email/optout` |
| SOAP action | `https://api.exigo.com/OptOutEmail` |
| WSDL elements | `OptOutEmailRequest` → `OptOutEmailResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=OptOutEmail |

#### Input

**`OptOutEmailRequest`**

| Property | Type | Notes |
|---|---|---|
| `Email` | `String` | Optional. The address you are opting out. |

#### Output

**`OptOutEmailResponse`**

| Property | Type | Notes |
|---|---|---|
| `RecordsAffected` | `Int32` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/email/optout HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "email": "johndoe@email.com"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "recordsAffected": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/OptOutEmail"

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
    <OptOutEmailRequest xmlns="http://api.exigo.com/">
      <Email>string</Email>
    </OptOutEmailRequest>
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
    <OptOutEmailResult xmlns="http://api.exigo.com/">
      <RecordsAffected>int</RecordsAffected>
    </OptOutEmailResult>
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
    var req = new OptOutEmailRequest();

    req.Email = "johndoe@email.com";//The address you are opting out.

    //Send Request to Server and Get Response
    var res = await api.OptOutEmailAsync(req);

    //Now examine the results:
    Console.WriteLine("RecordsAffected: {0}", res.RecordsAffected);
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
    OptOutEmailRequest req = new OptOutEmailRequest();

    req.Email = "johndoe@email.com";//The address you are opting out.

    //Send Request to Server and Get Response
    OptOutEmailResponse res = api.OptOutEmail(req);

    //Now examine the results:
    Console.WriteLine("RecordsAffected: {0}", res.RecordsAffected);
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
    Dim req as new OptOutEmailRequest()

    req.Email = "johndoe@email.com"

    'Send Request to Server and Get Response
    Dim res As OptOutEmailResponse = api.OptOutEmail(req)

    'Now examine the results:
    Console.WriteLine("RecordsAffected: {0}", res.RecordsAffected)
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

    $req->Email = "johndoe@email.com";

    //Send Request to Server and Get Response
    $res = $api.OptOutEmail($req);

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
    OptOutEmailRequest req = new OptOutEmailRequest();

    req.setEmail("johndoe@email.com");

    //Send Request to Server and Get Response
    OptOutEmailResponse res = api.getExigoApiSoap().optOutEmail(req, auth);

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

### OptOutSms

> Opts out all customers and customer contacts with specified
>  phone number from receiving broadcast SMS messages.

| | |
|---|---|
| Category | Communications |
| REST | `POST /3.0/sms/optout` |
| SOAP action | `https://api.exigo.com/OptOutSms` |
| WSDL elements | `OptOutSmsRequest` → `OptOutSmsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=OptOutSms |

#### Input

**`OptOutSmsRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Optional. The CustomerID being opted out. Use either CustomerID or phone number. |
| `PhoneNumber` | `String` | Optional. The phone number you are opting out. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`OptOutSmsResponse`**

| Property | Type | Notes |
|---|---|---|
| `RecordsAffected` | `Int32` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/sms/optout HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "phoneNumber": "(888) 555-1234",
  "customerKey": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "recordsAffected": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/OptOutSms"

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
    <OptOutSmsRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <PhoneNumber>string</PhoneNumber>
      <CustomerKey>string</CustomerKey>
    </OptOutSmsRequest>
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
    <OptOutSmsResult xmlns="http://api.exigo.com/">
      <RecordsAffected>int</RecordsAffected>
    </OptOutSmsResult>
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
    var req = new OptOutSmsRequest();

    req.CustomerID = 1;             //The CustomerID being opted out. Use either CustomerID or phone number.
    req.PhoneNumber = "(888) 555-1234";//The phone number you are opting out.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.OptOutSmsAsync(req);

    //Now examine the results:
    Console.WriteLine("RecordsAffected: {0}", res.RecordsAffected);
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
    OptOutSmsRequest req = new OptOutSmsRequest();

    req.CustomerID = 1;             //The CustomerID being opted out. Use either CustomerID or phone number.
    req.PhoneNumber = "(888) 555-1234";//The phone number you are opting out.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    OptOutSmsResponse res = api.OptOutSms(req);

    //Now examine the results:
    Console.WriteLine("RecordsAffected: {0}", res.RecordsAffected);
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
    Dim req as new OptOutSmsRequest()

    req.CustomerID = 1
    req.PhoneNumber = "(888) 555-1234"
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As OptOutSmsResponse = api.OptOutSms(req)

    'Now examine the results:
    Console.WriteLine("RecordsAffected: {0}", res.RecordsAffected)
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
    $req->PhoneNumber = "(888) 555-1234";
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.OptOutSms($req);

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
    OptOutSmsRequest req = new OptOutSmsRequest();

    req.setCustomerID(1);
    req.setPhoneNumber("(888) 555-1234");
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    OptOutSmsResponse res = api.getExigoApiSoap().optOutSms(req, auth);

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

### OptOutPushNotification

> Setup opt out settings for Push Notifications to mobile devices.

| | |
|---|---|
| Category | Communications |
| REST | `POST /3.0/push/optout` |
| SOAP action | `https://api.exigo.com/OptOutPushNotification` |
| WSDL elements | `optOutPushNotificationRequest` → `OptOutPushNotificationResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=OptOutPushNotification |

#### Input

**`OptOutPushNotificationRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`OptOutPushNotificationResponse`**

| Property | Type | Notes |
|---|---|---|
| `RecordsAffected` | `Int32` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/push/optout HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "customerKey": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "recordsAffected": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/OptOutPushNotification"

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
    <optOutPushNotificationRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
    </optOutPushNotificationRequest>
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
    <OptOutPushNotificationResult xmlns="http://api.exigo.com/">
      <RecordsAffected>int</RecordsAffected>
    </OptOutPushNotificationResult>
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
    var req = new OptOutPushNotificationRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.OptOutPushNotificationAsync(req);

    //Now examine the results:
    Console.WriteLine("RecordsAffected: {0}", res.RecordsAffected);
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
    OptOutPushNotificationRequest req = new OptOutPushNotificationRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    OptOutPushNotificationResponse res = api.OptOutPushNotification(req);

    //Now examine the results:
    Console.WriteLine("RecordsAffected: {0}", res.RecordsAffected);
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
    Dim req as new OptOutPushNotificationRequest()

    req.CustomerID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As OptOutPushNotificationResponse = api.OptOutPushNotification(req)

    'Now examine the results:
    Console.WriteLine("RecordsAffected: {0}", res.RecordsAffected)
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
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.OptOutPushNotification($req);

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
    OptOutPushNotificationRequest req = new OptOutPushNotificationRequest();

    req.setCustomerID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    OptOutPushNotificationResponse res = api.getExigoApiSoap().optOutPushNotification(req, auth);

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

### GetCompanyNews

> Gets a list of company news descriptions.

| | |
|---|---|
| Category | Communications |
| REST | `GET /3.0/companynews?departmentType=1` |
| SOAP action | `https://api.exigo.com/GetCompanyNews` |
| WSDL elements | `GetCompanyNewsRequest` → `GetCompanyNewsResult` |
| CSV output | Yes — `GET https://api.exigo.com/3.0/csv/?method=GetCompanyNews&ApiLoginName=…&ApiPassword=…&ApiCompany=…` |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetCompanyNews |

#### Input

**`GetCompanyNewsRequest`**

| Property | Type | Notes |
|---|---|---|
| `StartDate` | `DateTime` | Optional. Use when pulling data in chunks. |
| `EndDate` | `DateTime` | Optional. Use when pulling data in chunks. |
| `DepartmentType` | `Int32` | Optional. Classification of a department as defined by the company.<br>**Lookup:** company-specific list (see company-lists.md) |

#### Output

**`GetCompanyNewsResponse`**

| Property | Type | Notes |
|---|---|---|
| `CompanyNews` | `CompanyNewsResponse[]` |  |

**`CompanyNewsResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `Description` | `String` |  |
| &nbsp;&nbsp;↳ `NewsID` | `Int32` |  |
| &nbsp;&nbsp;↳ `CreatedDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `WebSettings` | `NewsWebSettings` | **Values:** `AccessAvailable`, `AccessNotAvailable` |
| &nbsp;&nbsp;↳ `CompanySettings` | `NewsCompanySettings` | **Values:** `AccessAllUsers`, `AccessByDepartment`, `AccessNotAvailable` |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/companynews?departmentType=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "companyNews": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetCompanyNews"

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
    <GetCompanyNewsRequest xmlns="http://api.exigo.com/">
      <StartDate>dateTime</StartDate>
      <EndDate>dateTime</EndDate>
      <DepartmentType>int</DepartmentType>
    </GetCompanyNewsRequest>
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
    <GetCompanyNewsResult xmlns="http://api.exigo.com/">
      <CompanyNews>
        <CompanyNewsResponse>
          <Description>string</Description>
          <NewsID>int</NewsID>
          <CreatedDate>dateTime</CreatedDate>
          <WebSettings>AccessAvailable or AccessNotAvailable</WebSettings>
          <CompanySettings>AccessAllUsers or AccessByDepartment or AccessNotAvailable</CompanySettings>
        </CompanyNewsResponse>
      </CompanyNews>
    </GetCompanyNewsResult>
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
    var req = new GetCompanyNewsRequest();

    req.DepartmentType = 1;         //Classification of a department as defined by the company

    //Send Request to Server and Get Response
    var res = await api.GetCompanyNewsAsync(req);

    //Now examine the results:

    foreach (var companyNews  in res.CompanyNews)
    {
        Console.WriteLine("Description: {0}", companyNews.Description);
        Console.WriteLine("NewsID: {0}", companyNews.NewsID);
        Console.WriteLine("CreatedDate: {0}", companyNews.CreatedDate);
        Console.WriteLine("WebSettings: {0}", companyNews.WebSettings);
        Console.WriteLine("CompanySettings: {0}", companyNews.CompanySettings);
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
    GetCompanyNewsRequest req = new GetCompanyNewsRequest();

    req.DepartmentType = 1;         //Classification of a department as defined by the company

    //Send Request to Server and Get Response
    GetCompanyNewsResponse res = api.GetCompanyNews(req);

    //Now examine the results:

    foreach (CompanyNewsResponse companyNews  in res.CompanyNews)
    {
        Console.WriteLine("Description: {0}", companyNews.Description);
        Console.WriteLine("NewsID: {0}", companyNews.NewsID);
        Console.WriteLine("CreatedDate: {0}", companyNews.CreatedDate);
        Console.WriteLine("WebSettings: {0}", companyNews.WebSettings);
        Console.WriteLine("CompanySettings: {0}", companyNews.CompanySettings);
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
    Dim req as new GetCompanyNewsRequest()

    req.DepartmentType = 1

    'Send Request to Server and Get Response
    Dim res As GetCompanyNewsResponse = api.GetCompanyNews(req)

    'Now examine the results:

    For Each companyNews As CompanyNewsResponse In res.CompanyNews
        Console.WriteLine("Description: {0}", companyNews.Description)
        Console.WriteLine("NewsID: {0}", companyNews.NewsID)
        Console.WriteLine("CreatedDate: {0}", companyNews.CreatedDate)
        Console.WriteLine("WebSettings: {0}", companyNews.WebSettings)
        Console.WriteLine("CompanySettings: {0}", companyNews.CompanySettings)
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

    $req->DepartmentType = 1;

    //Send Request to Server and Get Response
    $res = $api.GetCompanyNews($req);

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
    GetCompanyNewsRequest req = new GetCompanyNewsRequest();

    req.setDepartmentType(1);

    //Send Request to Server and Get Response
    GetCompanyNewsResponse res = api.getExigoApiSoap().getCompanyNews(req, auth);

    //Now examine the results:
}
catch (Exception ex)
{
    System.out.println("Error: " + ex.getMessage());
}
```

</details>

<details><summary>CSV</summary>

_This method supports CSV output._

```text
HTTP Get Request:
https://api.exigo.com/3.0/csv/?method=GetCompanyNews
&ApiLoginName=String
&ApiPassword=String
&ApiCompany=String
&StartDate=Nullable`1
&EndDate=Nullable`1
&DepartmentType=Nullable`1
Response FieldsDescription,NewsID,CreatedDate,WebSettings,CompanySettings
String,Int32,DateTime,NewsWebSettings,NewsCompanySettings

                    © 2026 Exigo.
```

</details>

---

### GetCompanyNewsItem

>  Gets company news details.

| | |
|---|---|
| Category | Communications |
| REST | `GET /3.0/companynews/item?newsID=1` |
| SOAP action | `https://api.exigo.com/GetCompanyNewsItem` |
| WSDL elements | `GetCompanyNewsItemRequest` → `GetCompanyNewsItemResult` |
| CSV output | Yes — `GET https://api.exigo.com/3.0/csv/?method=GetCompanyNewsItem&ApiLoginName=…&ApiPassword=…&ApiCompany=…` |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetCompanyNewsItem |

#### Input

**`GetCompanyNewsItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `NewsID` | `Int32` |  |

#### Output

**`GetCompanyNewsItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `Description` | `String` |  |
| `NewsID` | `Int32` |  |
| `CreatedDate` | `DateTime` |  |
| `WebSettings` | `NewsWebSettings` | **Values:** `AccessAvailable`, `AccessNotAvailable` |
| `CompanySettings` | `NewsCompanySettings` | **Values:** `AccessAllUsers`, `AccessByDepartment`, `AccessNotAvailable` |
| `Content` | `String` |  |
| `Departments` | `DepartmentInfo[]` |  |

**`DepartmentInfo`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `Description` | `String` |  |
| &nbsp;&nbsp;↳ `DepartmentType` | `Int32` | Classification of a department as defined by the company.<br>**Lookup:** company-specific list (see company-lists.md) |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/companynews/item?newsID=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "description": "",
  "newsID": 1,
  "createdDate": "2026-11-10T00:00:00-06:00",
  "webSettings": null,
  "companySettings": null,
  "content": "",
  "departments": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetCompanyNewsItem"

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
    <GetCompanyNewsItemRequest xmlns="http://api.exigo.com/">
      <NewsID>int</NewsID>
    </GetCompanyNewsItemRequest>
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
    <GetCompanyNewsItemResult xmlns="http://api.exigo.com/">
      <Description>string</Description>
      <NewsID>int</NewsID>
      <CreatedDate>dateTime</CreatedDate>
      <WebSettings>AccessAvailable or AccessNotAvailable</WebSettings>
      <CompanySettings>AccessAllUsers or AccessByDepartment or AccessNotAvailable</CompanySettings>
      <Content>string</Content>
      <Departments>
        <DepartmentInfo>
          <Description>string</Description>
          <DepartmentType>int</DepartmentType>
        </DepartmentInfo>
      </Departments>
    </GetCompanyNewsItemResult>
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
    var req = new GetCompanyNewsItemRequest();

    req.NewsID = 1;

    //Send Request to Server and Get Response
    var res = await api.GetCompanyNewsItemAsync(req);

    //Now examine the results:
    Console.WriteLine("Description: {0}", res.Description);
    Console.WriteLine("NewsID: {0}", res.NewsID);
    Console.WriteLine("CreatedDate: {0}", res.CreatedDate);
    Console.WriteLine("WebSettings: {0}", res.WebSettings);
    Console.WriteLine("CompanySettings: {0}", res.CompanySettings);
    Console.WriteLine("Content: {0}", res.Content);

    foreach (var departmentInfo  in res.Departments)
    {
        Console.WriteLine("Description: {0}", departmentInfo.Description);
        Console.WriteLine("DepartmentType: {0}", departmentInfo.DepartmentType);
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
    GetCompanyNewsItemRequest req = new GetCompanyNewsItemRequest();

    req.NewsID = 1;

    //Send Request to Server and Get Response
    GetCompanyNewsItemResponse res = api.GetCompanyNewsItem(req);

    //Now examine the results:
    Console.WriteLine("Description: {0}", res.Description);
    Console.WriteLine("NewsID: {0}", res.NewsID);
    Console.WriteLine("CreatedDate: {0}", res.CreatedDate);
    Console.WriteLine("WebSettings: {0}", res.WebSettings);
    Console.WriteLine("CompanySettings: {0}", res.CompanySettings);
    Console.WriteLine("Content: {0}", res.Content);

    foreach (DepartmentInfo departmentInfo  in res.Departments)
    {
        Console.WriteLine("Description: {0}", departmentInfo.Description);
        Console.WriteLine("DepartmentType: {0}", departmentInfo.DepartmentType);
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
    Dim req as new GetCompanyNewsItemRequest()

    req.NewsID = 1

    'Send Request to Server and Get Response
    Dim res As GetCompanyNewsItemResponse = api.GetCompanyNewsItem(req)

    'Now examine the results:
    Console.WriteLine("Description: {0}", res.Description)
    Console.WriteLine("NewsID: {0}", res.NewsID)
    Console.WriteLine("CreatedDate: {0}", res.CreatedDate)
    Console.WriteLine("WebSettings: {0}", res.WebSettings)
    Console.WriteLine("CompanySettings: {0}", res.CompanySettings)
    Console.WriteLine("Content: {0}", res.Content)

    For Each departmentInfo As DepartmentInfo In res.Departments
        Console.WriteLine("Description: {0}", departmentInfo.Description)
        Console.WriteLine("DepartmentType: {0}", departmentInfo.DepartmentType)
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

    $req->NewsID = 1;

    //Send Request to Server and Get Response
    $res = $api.GetCompanyNewsItem($req);

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
    GetCompanyNewsItemRequest req = new GetCompanyNewsItemRequest();

    req.setNewsID(1);

    //Send Request to Server and Get Response
    GetCompanyNewsItemResponse res = api.getExigoApiSoap().getCompanyNewsItem(req, auth);

    //Now examine the results:
}
catch (Exception ex)
{
    System.out.println("Error: " + ex.getMessage());
}
```

</details>

<details><summary>CSV</summary>

_This method supports CSV output._

```text
HTTP Get Request:
https://api.exigo.com/3.0/csv/?method=GetCompanyNewsItem
&ApiLoginName=String
&ApiPassword=String
&ApiCompany=String
&NewsID=Int32
Response FieldsDescription,NewsID,CreatedDate,WebSettings,CompanySettings,Content,Description,DepartmentType
String,Int32,DateTime,NewsWebSettings,NewsCompanySettings,String,String,Int32

                    © 2026 Exigo.
```

</details>

---

### GetRandomMessage

>  Gets a random message (defined in the Exigo Admin).

| | |
|---|---|
| Category | Communications |
| REST | `GET /3.0/randommessage?languageID=1` |
| SOAP action | `https://api.exigo.com/GetRandomMessage` |
| WSDL elements | `GetRandomMessageRequest` → `GetRandomMessageResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetRandomMessage |

#### Input

**`GetRandomMessageRequest`**

| Property | Type | Notes |
|---|---|---|
| `LanguageID` | `Int32` | Optional. The language of the random message. Defaults to 0 (English). Defaults to 0. |

#### Output

**`GetRandomMessageResponse`**

| Property | Type | Notes |
|---|---|---|
| `RandomMessageID` | `Int32` | The unique identifier for the random message. |
| `Content` | `String` | The content of the random message. |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/randommessage?languageID=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "randomMessageID": 1,
  "content": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetRandomMessage"

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
    <GetRandomMessageRequest xmlns="http://api.exigo.com/">
      <LanguageID>int</LanguageID>
    </GetRandomMessageRequest>
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
    <GetRandomMessageResult xmlns="http://api.exigo.com/">
      <RandomMessageID>int</RandomMessageID>
      <Content>string</Content>
    </GetRandomMessageResult>
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
    var req = new GetRandomMessageRequest();

    req.LanguageID = 1;             // The language of the random message. Defaults to 0 (English).

    //Send Request to Server and Get Response
    var res = await api.GetRandomMessageAsync(req);

    //Now examine the results:
    Console.WriteLine("RandomMessageID: {0}", res.RandomMessageID);
    Console.WriteLine("Content: {0}", res.Content);
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
    GetRandomMessageRequest req = new GetRandomMessageRequest();

    req.LanguageID = 1;             // The language of the random message. Defaults to 0 (English).

    //Send Request to Server and Get Response
    GetRandomMessageResponse res = api.GetRandomMessage(req);

    //Now examine the results:
    Console.WriteLine("RandomMessageID: {0}", res.RandomMessageID);
    Console.WriteLine("Content: {0}", res.Content);
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
    Dim req as new GetRandomMessageRequest()

    req.LanguageID = 1

    'Send Request to Server and Get Response
    Dim res As GetRandomMessageResponse = api.GetRandomMessage(req)

    'Now examine the results:
    Console.WriteLine("RandomMessageID: {0}", res.RandomMessageID)
    Console.WriteLine("Content: {0}", res.Content)
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

    $req->LanguageID = 1;

    //Send Request to Server and Get Response
    $res = $api.GetRandomMessage($req);

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
    GetRandomMessageRequest req = new GetRandomMessageRequest();

    req.setLanguageID(1);

    //Send Request to Server and Get Response
    GetRandomMessageResponse res = api.getExigoApiSoap().getRandomMessage(req, auth);

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

### FireResponder

> Fires an email responder to customer or order email address on file.

| | |
|---|---|
| Category | Communications |
| REST | `POST /3.0/autoresponder/fire` |
| SOAP action | `https://api.exigo.com/FireResponder` |
| WSDL elements | `FireResponderRequest` → `FireResponderResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=FireResponder |

#### Input

**`FireResponderRequest`**

| Property | Type | Notes |
|---|---|---|
| `ResponderID` | `Int32` | Unique Email ResponderID.<br>**Lookup:** company-specific list (see company-lists.md) |
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `OrderID` | `Int32` | Optional. Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exception will occur if CustomerID & CustomerKey are provided. |
| `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exception will occur if OrderID & OrderKey are provided. |

#### Output

**`FireResponderResponse`**

_No properties._

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/autoresponder/fire HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "orderID": 1,
  "customerKey": "1",
  "orderKey": "1"
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
SOAPAction: "https://api.exigo.com/FireResponder"

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
    <FireResponderRequest xmlns="http://api.exigo.com/">
      <ResponderID>int</ResponderID>
      <CustomerID>int</CustomerID>
      <OrderID>int</OrderID>
      <CustomerKey>string</CustomerKey>
      <OrderKey>string</OrderKey>
    </FireResponderRequest>
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
    <FireResponderResult xmlns="http://api.exigo.com/" />
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
    var req = new FireResponderRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.OrderID = 1;                //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for order record. Exception will occur if CustomerID & CustomerKey are provided.
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exception will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    var res = await api.FireResponderAsync(req);

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
    FireResponderRequest req = new FireResponderRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.OrderID = 1;                //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for order record. Exception will occur if CustomerID & CustomerKey are provided.
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exception will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    FireResponderResponse res = api.FireResponder(req);

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
    Dim req as new FireResponderRequest()

    req.CustomerID = 1
    req.OrderID = 1
    req.CustomerKey = "1"
    req.OrderKey = "1"

    'Send Request to Server and Get Response
    Dim res As FireResponderResponse = api.FireResponder(req)

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
    $req->OrderID = 1;
    $req->CustomerKey = "1";
    $req->OrderKey = "1";

    //Send Request to Server and Get Response
    $res = $api.FireResponder($req);

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
    FireResponderRequest req = new FireResponderRequest();

    req.setCustomerID(1);
    req.setOrderID(1);
    req.setCustomerKey("1");
    req.setOrderKey("1");

    //Send Request to Server and Get Response
    FireResponderResponse res = api.getExigoApiSoap().fireResponder(req, auth);

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

### SendSms

> Sends an SMS message.

| | |
|---|---|
| Category | Communications |
| REST | `POST /3.0/sms` |
| SOAP action | `https://api.exigo.com/SendSms` |
| WSDL elements | `SendSmsRequest` → `SendSmsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=SendSms |

#### Input

**`SendSmsRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `Message` | `String` | Optional. |
| `Phone` | `String` | Optional. Will send to Customer Phone(s) if omitted. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`SendSmsResponse`**

_No properties._

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/sms HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "message": "",
  "phone": "1",
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
SOAPAction: "https://api.exigo.com/SendSms"

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
    <SendSmsRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <Message>string</Message>
      <Phone>string</Phone>
      <CustomerKey>string</CustomerKey>
    </SendSmsRequest>
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
    <SendSmsResult xmlns="http://api.exigo.com/" />
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
    var req = new SendSmsRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.Message = "1";
    req.Phone = "1";                //Will send to Customer Phone(s) if omitted
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.SendSmsAsync(req);

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
    SendSmsRequest req = new SendSmsRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.Message = "1";
    req.Phone = "1";                //Will send to Customer Phone(s) if omitted
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    SendSmsResponse res = api.SendSms(req);

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
    Dim req as new SendSmsRequest()

    req.CustomerID = 1
    req.Message = "1"
    req.Phone = "1"
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As SendSmsResponse = api.SendSms(req)

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
    $req->Message = "1";
    $req->Phone = "1";
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.SendSms($req);

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
    SendSmsRequest req = new SendSmsRequest();

    req.setCustomerID(1);
    req.setMessage("1");
    req.setPhone("1");
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    SendSmsResponse res = api.getExigoApiSoap().sendSms(req, auth);

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

### SendAuthorizationMFACode

> Sends an Authorization MFA Code SMS message.

| | |
|---|---|
| Category | Communications |
| REST | `POST /3.0/sms/authorizationmfa` |
| SOAP action | `https://api.exigo.com/SendAuthorizationMFACode` |
| WSDL elements | `SendAuthorizationMFACodeRequest` → `SendAuthorizationMFACodeResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=SendAuthorizationMFACode |

#### Input

**`SendAuthorizationMFACodeRequest`**

| Property | Type | Notes |
|---|---|---|
| `ToNumber` | `String` | Phone Number that will receive the SMS. |
| `Message` | `String` | Optional. Default value is "Backoffice Authentication code:". |
| `Code` | `String` |  |

#### Output

**`SendAuthorizationMFACodeResponse`**

_No properties._

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/sms/authorizationmfa HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "toNumber": "1",
  "message": "1",
  "code": "1"
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
SOAPAction: "https://api.exigo.com/SendAuthorizationMFACode"

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
    <SendAuthorizationMFACodeRequest xmlns="http://api.exigo.com/">
      <ToNumber>string</ToNumber>
      <Message>string</Message>
      <Code>string</Code>
    </SendAuthorizationMFACodeRequest>
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
    <SendAuthorizationMFACodeResult xmlns="http://api.exigo.com/" />
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
    var req = new SendAuthorizationMFACodeRequest();

    req.ToNumber = "1";             //Phone Number that will receive the SMS
    req.Message = "1";              //Default value is "Backoffice Authentication code:"
    req.Code = "1";

    //Send Request to Server and Get Response
    var res = await api.SendAuthorizationMFACodeAsync(req);

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
    SendAuthorizationMFACodeRequest req = new SendAuthorizationMFACodeRequest();

    req.ToNumber = "1";             //Phone Number that will receive the SMS
    req.Message = "1";              //Default value is "Backoffice Authentication code:"
    req.Code = "1";

    //Send Request to Server and Get Response
    SendAuthorizationMFACodeResponse res = api.SendAuthorizationMFACode(req);

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
    Dim req as new SendAuthorizationMFACodeRequest()

    req.ToNumber = "1"
    req.Message = "1"
    req.Code = "1"

    'Send Request to Server and Get Response
    Dim res As SendAuthorizationMFACodeResponse = api.SendAuthorizationMFACode(req)

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

    $req->ToNumber = "1";
    $req->Message = "1";
    $req->Code = "1";

    //Send Request to Server and Get Response
    $res = $api.SendAuthorizationMFACode($req);

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
    SendAuthorizationMFACodeRequest req = new SendAuthorizationMFACodeRequest();

    req.setToNumber("1");
    req.setMessage("1");
    req.setCode("1");

    //Send Request to Server and Get Response
    SendAuthorizationMFACodeResponse res = api.getExigoApiSoap().sendAuthorizationMFACode(req, auth);

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
