# Exigo API — Tree Movement

API version v2025.11.7.6. Crawled 2026-11-11 from https://api.exigo.com/3.0/. Back to [index](../README.md).

| Operation | REST | Summary |
|---|---|---|
| [PlaceEnrollerNode](#placeenrollernode) | `POST /3.0/tree/enroller` | Inserts/Moves a customer within the Enroller Tree. |
| [PlaceUniLevelNode](#placeunilevelnode) | `POST /3.0/tree/unilevel` | Inserts/Moves a customer within the UniLevel (Sponsor) Tree. |
| [PlaceMatrixNode](#placematrixnode) | `POST /3.0/tree/matrix` | Inserts/Moves a customer within the Matrix Tree. |
| [PlaceBinaryNode](#placebinarynode) | `POST /3.0/tree/binary` | Inserts/Moves a customer within the Binary Tree. |
| [GetBinaryPreference](#getbinarypreference) | `GET /3.0/tree/binary?customerID=1` | Returns the currently configured placement preference for new placements under a customer. |
| [SetBinaryPreference](#setbinarypreference) | `PUT /3.0/tree/binary` | Sets the placement preference for new placements under a customer. |

---
### PlaceEnrollerNode

> Inserts/Moves a customer within the Enroller Tree.

| | |
|---|---|
| Category | Tree Movement |
| REST | `POST /3.0/tree/enroller` |
| SOAP action | `https://api.exigo.com/PlaceEnrollerNode` |
| WSDL elements | `PlaceEnrollerNodeRequest` → `PlaceEnrollerNodeResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=PlaceEnrollerNode |

#### Input

**`PlaceEnrollerNodeRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `ToEnrollerID` | `Int32` | Unique numeric identifier for customer enroller record. |
| `Reason` | `String` | Optional. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |
| `ToEnrollerKey` | `String` | Optional. Unique numeric identifier for customer enroller record. Exeption will occur if EnrollerID & EnrollerKey are provided. |

#### Output

**`PlaceEnrollerNodeResponse`**

_No properties._

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/tree/enroller HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "toEnrollerID": 1,
  "reason": "",
  "customerKey": "1",
  "toEnrollerKey": "1"
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
SOAPAction: "https://api.exigo.com/PlaceEnrollerNode"

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
    <PlaceEnrollerNodeRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <ToEnrollerID>int</ToEnrollerID>
      <Reason>string</Reason>
      <CustomerKey>string</CustomerKey>
      <ToEnrollerKey>string</ToEnrollerKey>
    </PlaceEnrollerNodeRequest>
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
    <PlaceEnrollerNodeResult xmlns="http://api.exigo.com/" />
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
    var req = new PlaceEnrollerNodeRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.ToEnrollerID = 1;           //Unique numeric identifier for customer enroller record.
    req.Reason = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.ToEnrollerKey = "1";        //Unique numeric identifier for customer enroller record. Exeption will occur if EnrollerID & EnrollerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.PlaceEnrollerNodeAsync(req);

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
    PlaceEnrollerNodeRequest req = new PlaceEnrollerNodeRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.ToEnrollerID = 1;           //Unique numeric identifier for customer enroller record.
    req.Reason = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.ToEnrollerKey = "1";        //Unique numeric identifier for customer enroller record. Exeption will occur if EnrollerID & EnrollerKey are provided.

    //Send Request to Server and Get Response
    PlaceEnrollerNodeResponse res = api.PlaceEnrollerNode(req);

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
    Dim req as new PlaceEnrollerNodeRequest()

    req.CustomerID = 1
    req.ToEnrollerID = 1
    req.Reason = "1"
    req.CustomerKey = "1"
    req.ToEnrollerKey = "1"

    'Send Request to Server and Get Response
    Dim res As PlaceEnrollerNodeResponse = api.PlaceEnrollerNode(req)

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
    $req->ToEnrollerID = 1;
    $req->Reason = "1";
    $req->CustomerKey = "1";
    $req->ToEnrollerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.PlaceEnrollerNode($req);

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
    PlaceEnrollerNodeRequest req = new PlaceEnrollerNodeRequest();

    req.setCustomerID(1);
    req.setToEnrollerID(1);
    req.setReason("1");
    req.setCustomerKey("1");
    req.setToEnrollerKey("1");

    //Send Request to Server and Get Response
    PlaceEnrollerNodeResponse res = api.getExigoApiSoap().placeEnrollerNode(req, auth);

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

### PlaceUniLevelNode

> Inserts/Moves a customer within the UniLevel (Sponsor) Tree.

| | |
|---|---|
| Category | Tree Movement |
| REST | `POST /3.0/tree/unilevel` |
| SOAP action | `https://api.exigo.com/PlaceUniLevelNode` |
| WSDL elements | `PlaceUniLevelNodeRequest` → `PlaceUniLevelNodeResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=PlaceUniLevelNode |

#### Input

**`PlaceUniLevelNodeRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `ToSponsorID` | `Int32` | Unique numeric identifier fpr customer sponsor record. |
| `Reason` | `String` | Optional. |
| `OptionalPlacement` | `Int32` |  |
| `OptionalFindAvailable` | `Boolean` |  |
| `OptionalUnilevelBuildTypeID` | `Int32` |  |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |
| `ToSponsorKey` | `String` | Optional. Unique alpha numeric identifier for customer sponsor record. Exeption will occur if ToSponsorID & ToSponsorKey are provided. |

#### Output

**`PlaceUniLevelNodeResponse`**

_No properties._

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/tree/unilevel HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "toSponsorID": 1,
  "reason": "",
  "optionalPlacement": 1,
  "optionalFindAvailable": true,
  "optionalUnilevelBuildTypeID": 1,
  "customerKey": "1",
  "toSponsorKey": "1"
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
SOAPAction: "https://api.exigo.com/PlaceUniLevelNode"

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
    <PlaceUniLevelNodeRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <ToSponsorID>int</ToSponsorID>
      <Reason>string</Reason>
      <OptionalPlacement>int</OptionalPlacement>
      <OptionalFindAvailable>boolean</OptionalFindAvailable>
      <OptionalUnilevelBuildTypeID>int</OptionalUnilevelBuildTypeID>
      <CustomerKey>string</CustomerKey>
      <ToSponsorKey>string</ToSponsorKey>
    </PlaceUniLevelNodeRequest>
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
    <PlaceUniLevelNodeResult xmlns="http://api.exigo.com/" />
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
    var req = new PlaceUniLevelNodeRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.ToSponsorID = 1;            //Unique numeric identifier fpr customer sponsor record.
    req.Reason = "1";
    req.OptionalPlacement = 1;
    req.OptionalFindAvailable = true;
    req.OptionalUnilevelBuildTypeID = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.ToSponsorKey = "1";         //Unique alpha numeric identifier for customer sponsor record. Exeption will occur if ToSponsorID & ToSponsorKey are provided.

    //Send Request to Server and Get Response
    var res = await api.PlaceUniLevelNodeAsync(req);

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
    PlaceUniLevelNodeRequest req = new PlaceUniLevelNodeRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.ToSponsorID = 1;            //Unique numeric identifier fpr customer sponsor record.
    req.Reason = "1";
    req.OptionalPlacement = 1;
    req.OptionalFindAvailable = true;
    req.OptionalUnilevelBuildTypeID = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.ToSponsorKey = "1";         //Unique alpha numeric identifier for customer sponsor record. Exeption will occur if ToSponsorID & ToSponsorKey are provided.

    //Send Request to Server and Get Response
    PlaceUniLevelNodeResponse res = api.PlaceUniLevelNode(req);

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
    Dim req as new PlaceUniLevelNodeRequest()

    req.CustomerID = 1
    req.ToSponsorID = 1
    req.Reason = "1"
    req.OptionalPlacement = 1
    req.OptionalFindAvailable = true
    req.OptionalUnilevelBuildTypeID = 1
    req.CustomerKey = "1"
    req.ToSponsorKey = "1"

    'Send Request to Server and Get Response
    Dim res As PlaceUniLevelNodeResponse = api.PlaceUniLevelNode(req)

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
    $req->ToSponsorID = 1;
    $req->Reason = "1";
    $req->OptionalPlacement = 1;
    $req->OptionalFindAvailable = 1;
    $req->OptionalUnilevelBuildTypeID = 1;
    $req->CustomerKey = "1";
    $req->ToSponsorKey = "1";

    //Send Request to Server and Get Response
    $res = $api.PlaceUniLevelNode($req);

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
    PlaceUniLevelNodeRequest req = new PlaceUniLevelNodeRequest();

    req.setCustomerID(1);
    req.setToSponsorID(1);
    req.setReason("1");
    req.setOptionalPlacement(1);
    req.setOptionalFindAvailable(1);
    req.setOptionalUnilevelBuildTypeID(1);
    req.setCustomerKey("1");
    req.setToSponsorKey("1");

    //Send Request to Server and Get Response
    PlaceUniLevelNodeResponse res = api.getExigoApiSoap().placeUniLevelNode(req, auth);

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

### PlaceMatrixNode

> Inserts/Moves a customer within the Matrix Tree.

| | |
|---|---|
| Category | Tree Movement |
| REST | `POST /3.0/tree/matrix` |
| SOAP action | `https://api.exigo.com/PlaceMatrixNode` |
| WSDL elements | `PlaceMatrixNodeRequest` → `PlaceMatrixNodeResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=PlaceMatrixNode |

#### Input

**`PlaceMatrixNodeRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `ToParentCustomerID` | `Int32` | Unique numeric identifier for transfer to customer record. |
| `ToParentMatrixID` | `Int32` | Optional. Unique numeric identifier for transfer to matrix parent customer record. |
| `Reason` | `String` | Optional. |
| `Placement` | `Int32` |  |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |
| `ToParentCustomerKey` | `String` | Optional. Unique alpha numeric identifier for transfer to customer record. Exeption will occur if ToParentCustomerID & ToParentCustomerKey are provided. |
| `ToParentMatrixKey` | `String` | Optional. Unique alpha numeric identifier for transfer to customer record. Exeption will occur if ToParentMatrixID & ToParentMatrixKey are provided. |

#### Output

**`PlaceMatrixNodeResponse`**

_No properties._

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/tree/matrix HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "toParentCustomerID": 1,
  "toParentMatrixID": 1,
  "reason": "",
  "placement": 1,
  "customerKey": "1",
  "toParentCustomerKey": "1",
  "toParentMatrixKey": "1"
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
SOAPAction: "https://api.exigo.com/PlaceMatrixNode"

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
    <PlaceMatrixNodeRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <ToParentCustomerID>int</ToParentCustomerID>
      <ToParentMatrixID>int</ToParentMatrixID>
      <Reason>string</Reason>
      <Placement>int</Placement>
      <CustomerKey>string</CustomerKey>
      <ToParentCustomerKey>string</ToParentCustomerKey>
      <ToParentMatrixKey>string</ToParentMatrixKey>
    </PlaceMatrixNodeRequest>
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
    <PlaceMatrixNodeResult xmlns="http://api.exigo.com/" />
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
    var req = new PlaceMatrixNodeRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.ToParentCustomerID = 1;     //Unique numeric identifier for transfer to customer record.
    req.ToParentMatrixID = 1;       //Unique numeric identifier for transfer to matrix parent customer record.
    req.Reason = "1";
    req.Placement = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.ToParentCustomerKey = "1";  //Unique alpha numeric identifier for transfer to customer record. Exeption will occur if ToParentCustomerID & ToParentCustomerKey are provided.
    req.ToParentMatrixKey = "1";    //Unique alpha numeric identifier for transfer to customer record. Exeption will occur if ToParentMatrixID & ToParentMatrixKey are provided.

    //Send Request to Server and Get Response
    var res = await api.PlaceMatrixNodeAsync(req);

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
    PlaceMatrixNodeRequest req = new PlaceMatrixNodeRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.ToParentCustomerID = 1;     //Unique numeric identifier for transfer to customer record.
    req.ToParentMatrixID = 1;       //Unique numeric identifier for transfer to matrix parent customer record.
    req.Reason = "1";
    req.Placement = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.ToParentCustomerKey = "1";  //Unique alpha numeric identifier for transfer to customer record. Exeption will occur if ToParentCustomerID & ToParentCustomerKey are provided.
    req.ToParentMatrixKey = "1";    //Unique alpha numeric identifier for transfer to customer record. Exeption will occur if ToParentMatrixID & ToParentMatrixKey are provided.

    //Send Request to Server and Get Response
    PlaceMatrixNodeResponse res = api.PlaceMatrixNode(req);

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
    Dim req as new PlaceMatrixNodeRequest()

    req.CustomerID = 1
    req.ToParentCustomerID = 1
    req.ToParentMatrixID = 1
    req.Reason = "1"
    req.Placement = 1
    req.CustomerKey = "1"
    req.ToParentCustomerKey = "1"
    req.ToParentMatrixKey = "1"

    'Send Request to Server and Get Response
    Dim res As PlaceMatrixNodeResponse = api.PlaceMatrixNode(req)

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
    $req->ToParentCustomerID = 1;
    $req->ToParentMatrixID = 1;
    $req->Reason = "1";
    $req->Placement = 1;
    $req->CustomerKey = "1";
    $req->ToParentCustomerKey = "1";
    $req->ToParentMatrixKey = "1";

    //Send Request to Server and Get Response
    $res = $api.PlaceMatrixNode($req);

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
    PlaceMatrixNodeRequest req = new PlaceMatrixNodeRequest();

    req.setCustomerID(1);
    req.setToParentCustomerID(1);
    req.setToParentMatrixID(1);
    req.setReason("1");
    req.setPlacement(1);
    req.setCustomerKey("1");
    req.setToParentCustomerKey("1");
    req.setToParentMatrixKey("1");

    //Send Request to Server and Get Response
    PlaceMatrixNodeResponse res = api.getExigoApiSoap().placeMatrixNode(req, auth);

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

### PlaceBinaryNode

> Inserts/Moves a customer within the Binary Tree.

| | |
|---|---|
| Category | Tree Movement |
| REST | `POST /3.0/tree/binary` |
| SOAP action | `https://api.exigo.com/PlaceBinaryNode` |
| WSDL elements | `PlaceBinaryNodeRequest` → `PlaceBinaryNodeResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=PlaceBinaryNode |

#### Input

**`PlaceBinaryNodeRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `ToParentID` | `Int32` | Unique numeric identifier for transfer to customer record. |
| `PlacementType` | `BinaryPlacementType` | **Values:** `StrategicPlacement`, `BuildLeft`, `BuildRight`, `BalancedBuild`, `EvenFill`, `WeakLeg`, `EnrollerPreference`, `LeftEvenFill`, `RightEvenFill`, `LesserVolumeLeg`, `LesserVolumeLegOutside`, `StrongLegOutside`, `LesserVolumeLegEvenFill`, `GreaterVolumeLegEvenFill`, `InsertRightMoveDownline`, `InsertLeftMoveDownline`, `BuildTeamLeg` |
| `Reason` | `String` | Optional. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |
| `ToParentKey` | `String` | Optional. Unique alpha numeric identifier for transfer to customer record. Exeption will occur if ToParentID & ToParentKey are provided. |

#### Output

**`PlaceBinaryNodeResponse`**

_No properties._

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/tree/binary HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "toParentID": 1,
  "placementType": null,
  "reason": "",
  "customerKey": "1",
  "toParentKey": "1"
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
SOAPAction: "https://api.exigo.com/PlaceBinaryNode"

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
    <PlaceBinaryNodeRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <ToParentID>int</ToParentID>
      <PlacementType>StrategicPlacement or BuildLeft or BuildRight or BalancedBuild or EvenFill or WeakLeg or EnrollerPreference or LeftEvenFill or RightEvenFill or LesserVolumeLeg or LesserVolumeLegOutside or StrongLegOutside or LesserVolumeLegEvenFill or GreaterVolumeLegEvenFill or InsertRightMoveDownline or InsertLeftMoveDownline or BuildTeamLeg</PlacementType>
      <Reason>string</Reason>
      <CustomerKey>string</CustomerKey>
      <ToParentKey>string</ToParentKey>
    </PlaceBinaryNodeRequest>
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
    <PlaceBinaryNodeResult xmlns="http://api.exigo.com/" />
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
    var req = new PlaceBinaryNodeRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.ToParentID = 1;             //Unique numeric identifier for transfer to customer record.
    req.PlacementType = BinaryPlacementType.StrategicPlacement;
    req.Reason = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.ToParentKey = "1";          //Unique alpha numeric identifier for transfer to customer record. Exeption will occur if ToParentID & ToParentKey are provided.

    //Send Request to Server and Get Response
    var res = await api.PlaceBinaryNodeAsync(req);

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
    PlaceBinaryNodeRequest req = new PlaceBinaryNodeRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.ToParentID = 1;             //Unique numeric identifier for transfer to customer record.
    req.PlacementType = BinaryPlacementType.StrategicPlacement;
    req.Reason = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.ToParentKey = "1";          //Unique alpha numeric identifier for transfer to customer record. Exeption will occur if ToParentID & ToParentKey are provided.

    //Send Request to Server and Get Response
    PlaceBinaryNodeResponse res = api.PlaceBinaryNode(req);

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
    Dim req as new PlaceBinaryNodeRequest()

    req.CustomerID = 1
    req.ToParentID = 1
    req.PlacementType = BinaryPlacementType.StrategicPlacement
    req.Reason = "1"
    req.CustomerKey = "1"
    req.ToParentKey = "1"

    'Send Request to Server and Get Response
    Dim res As PlaceBinaryNodeResponse = api.PlaceBinaryNode(req)

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
    $req->ToParentID = 1;
    $req->PlacementType = 1;
    $req->Reason = "1";
    $req->CustomerKey = "1";
    $req->ToParentKey = "1";

    //Send Request to Server and Get Response
    $res = $api.PlaceBinaryNode($req);

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
    PlaceBinaryNodeRequest req = new PlaceBinaryNodeRequest();

    req.setCustomerID(1);
    req.setToParentID(1);
    req.setPlacementType(1);
    req.setReason("1");
    req.setCustomerKey("1");
    req.setToParentKey("1");

    //Send Request to Server and Get Response
    PlaceBinaryNodeResponse res = api.getExigoApiSoap().placeBinaryNode(req, auth);

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

### GetBinaryPreference

>  Returns the currently configured placement preference for new placements under a customer.

| | |
|---|---|
| Category | Tree Movement |
| REST | `GET /3.0/tree/binary?customerID=1` |
| SOAP action | `https://api.exigo.com/GetBinaryPreference` |
| WSDL elements | `GetBinaryPreferenceRequest` → `GetBinaryPreferenceResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetBinaryPreference |

#### Input

**`GetBinaryPreferenceRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`GetBinaryPreferenceResponse`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `PlacementType` | `BinaryPlacementType` | **Values:** `StrategicPlacement`, `BuildLeft`, `BuildRight`, `BalancedBuild`, `EvenFill`, `WeakLeg`, `EnrollerPreference`, `LeftEvenFill`, `RightEvenFill`, `LesserVolumeLeg`, `LesserVolumeLegOutside`, `StrongLegOutside`, `LesserVolumeLegEvenFill`, `GreaterVolumeLegEvenFill`, `InsertRightMoveDownline`, `InsertLeftMoveDownline`, `BuildTeamLeg` |
| `CustomerKey` | `String` | Unique alpha numeric identifier for customer record . |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/tree/binary?customerID=1
  &customerKey=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "customerID": 1,
  "placementType": null,
  "customerKey": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetBinaryPreference"

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
    <GetBinaryPreferenceRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
    </GetBinaryPreferenceRequest>
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
    <GetBinaryPreferenceResult xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <PlacementType>StrategicPlacement or BuildLeft or BuildRight or BalancedBuild or EvenFill or WeakLeg or EnrollerPreference or LeftEvenFill or RightEvenFill or LesserVolumeLeg or LesserVolumeLegOutside or StrongLegOutside or LesserVolumeLegEvenFill or GreaterVolumeLegEvenFill or InsertRightMoveDownline or InsertLeftMoveDownline or BuildTeamLeg</PlacementType>
      <CustomerKey>string</CustomerKey>
    </GetBinaryPreferenceResult>
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
    var req = new GetBinaryPreferenceRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.GetBinaryPreferenceAsync(req);

    //Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID);
    Console.WriteLine("PlacementType: {0}", res.PlacementType);
    Console.WriteLine("CustomerKey: {0}", res.CustomerKey);
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
    GetBinaryPreferenceRequest req = new GetBinaryPreferenceRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    GetBinaryPreferenceResponse res = api.GetBinaryPreference(req);

    //Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID);
    Console.WriteLine("PlacementType: {0}", res.PlacementType);
    Console.WriteLine("CustomerKey: {0}", res.CustomerKey);
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
    Dim req as new GetBinaryPreferenceRequest()

    req.CustomerID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As GetBinaryPreferenceResponse = api.GetBinaryPreference(req)

    'Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID)
    Console.WriteLine("PlacementType: {0}", res.PlacementType)
    Console.WriteLine("CustomerKey: {0}", res.CustomerKey)
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
    $res = $api.GetBinaryPreference($req);

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
    GetBinaryPreferenceRequest req = new GetBinaryPreferenceRequest();

    req.setCustomerID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    GetBinaryPreferenceResponse res = api.getExigoApiSoap().getBinaryPreference(req, auth);

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

### SetBinaryPreference

>  Sets the placement preference for new placements under a customer.

| | |
|---|---|
| Category | Tree Movement |
| REST | `PUT /3.0/tree/binary` |
| SOAP action | `https://api.exigo.com/SetBinaryPreference` |
| WSDL elements | `SetBinaryPreferenceRequest` → `SetBinaryPreferenceResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=SetBinaryPreference |

#### Input

**`SetBinaryPreferenceRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `PlacementType` | `BinaryPlacementType` | **Values:** `StrategicPlacement`, `BuildLeft`, `BuildRight`, `BalancedBuild`, `EvenFill`, `WeakLeg`, `EnrollerPreference`, `LeftEvenFill`, `RightEvenFill`, `LesserVolumeLeg`, `LesserVolumeLegOutside`, `StrongLegOutside`, `LesserVolumeLegEvenFill`, `GreaterVolumeLegEvenFill`, `InsertRightMoveDownline`, `InsertLeftMoveDownline`, `BuildTeamLeg` |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`SetBinaryPreferenceResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/tree/binary HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "placementType": null,
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
SOAPAction: "https://api.exigo.com/SetBinaryPreference"

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
    <SetBinaryPreferenceRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <PlacementType>StrategicPlacement or BuildLeft or BuildRight or BalancedBuild or EvenFill or WeakLeg or EnrollerPreference or LeftEvenFill or RightEvenFill or LesserVolumeLeg or LesserVolumeLegOutside or StrongLegOutside or LesserVolumeLegEvenFill or GreaterVolumeLegEvenFill or InsertRightMoveDownline or InsertLeftMoveDownline or BuildTeamLeg</PlacementType>
      <CustomerKey>string</CustomerKey>
    </SetBinaryPreferenceRequest>
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
    <SetBinaryPreferenceResult xmlns="http://api.exigo.com/" />
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
    var req = new SetBinaryPreferenceRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.PlacementType = BinaryPlacementType.StrategicPlacement;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.SetBinaryPreferenceAsync(req);

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
    SetBinaryPreferenceRequest req = new SetBinaryPreferenceRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.PlacementType = BinaryPlacementType.StrategicPlacement;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    SetBinaryPreferenceResponse res = api.SetBinaryPreference(req);

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
    Dim req as new SetBinaryPreferenceRequest()

    req.CustomerID = 1
    req.PlacementType = BinaryPlacementType.StrategicPlacement
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As SetBinaryPreferenceResponse = api.SetBinaryPreference(req)

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
    $req->PlacementType = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.SetBinaryPreference($req);

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
    SetBinaryPreferenceRequest req = new SetBinaryPreferenceRequest();

    req.setCustomerID(1);
    req.setPlacementType(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    SetBinaryPreferenceResponse res = api.getExigoApiSoap().setBinaryPreference(req, auth);

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
