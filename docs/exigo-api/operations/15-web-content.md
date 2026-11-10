# Exigo API — Web Content

API version v2025.11.7.6. Crawled 2026-11-11 from https://api.exigo.com/3.0/. Back to [index](../README.md).

Language translations, content and resource set management operations

| Operation | REST | Summary |
|---|---|---|
| [ResourceSetCheckIn](#resourcesetcheckin) | `POST /3.0/resourceset/checkin` | Keeps the client's version of the resource set up to date to the environment it is subscribed to. |
| [CreateResourceSet](#createresourceset) | `POST /3.0/resourceset` | Create a new ResourceSet |
| [RetireResourceSet](#retireresourceset) | `DELETE /3.0/resourceset` | Retire an existing ResourceSet |
| [GetResourceSets](#getresourcesets) | `GET /3.0/resourcesetAuthorization:` | Get an existing Resource Set |
| [UpdateResourceSet](#updateresourceset) | `PATCH /3.0/resourceset` | Update an existing ResourceSet |
| [CreateResourceSetIntItem](#createresourcesetintitem) | `POST /3.0/resourceitem/int` | Adds a ResourceSet Number Item to the ResourceSet |
| [CreateResourceSetDecimalItem](#createresourcesetdecimalitem) | `POST /3.0/resourceitem/decimal` | Adds a ResourceSet Decimal Item to the ResourceSet |
| [CreateResourceSetTextItem](#createresourcesettextitem) | `POST /3.0/resourceitem/text` | Adds a ResourceSet Text Item to the ResourceSet |
| [CreateResourceSetBooleanItem](#createresourcesetbooleanitem) | `POST /3.0/resourceitem/bool` | Adds a ResourceSet CheckBox Item to the ResourceSet |
| [CreateResourceSetDateItem](#createresourcesetdateitem) | `POST /3.0/resourceitem/date` | Adds a ResourceSet Date Item to the ResourceSet |
| [CreateResourceSetImageItem](#createresourcesetimageitem) | `POST /3.0/resourceitem/image` | Adds a ResourceSet Image Item to the ResourceSet |
| [CreateResourceSetDataSetItem](#createresourcesetdatasetitem) | `POST /3.0/resourceitem/dataset` | Adds a ResourceSet DataSet Item to the ResourceSet |
| [CreateResourceSetBannerItem](#createresourcesetbanneritem) | `POST /3.0/resourceitem/banner` | Adds a ResourceSet Banner Item to the ResourceSet |
| [CreateResourceSetCarouselItem](#createresourcesetcarouselitem) | `POST /3.0/resourceitem/carousel` | Adds a ResourceSet Carousel Item to the ResourceSet |
| [CreateResourceSetWidgetItem](#createresourcesetwidgetitem) | `POST /3.0/resourceitem/widget` | Adds a ResourceSet Widget Item to the ResourceSet |
| [CreateResourceSetDropDownItem](#createresourcesetdropdownitem) | `POST /3.0/resourceitem/dropdown` | Adds a ResourceSet DropDown Item to the ResourceSet |
| [DeleteResourceSetItem](#deleteresourcesetitem) | `DELETE /3.0/resourceitem` | Deletes a ResourceSet Item |
| [GetResourceSetItems](#getresourcesetitems) | `GET /3.0/resourceitemAuthorization:` | Gets ResourceSet Items |
| [UpdateResourceSetIntItem](#updateresourcesetintitem) | `PATCH /3.0/resourceitem/int` | Updates a ResourceSet Int Item |
| [UpdateResourceSetDecimalItem](#updateresourcesetdecimalitem) | `PATCH /3.0/resourceitem/decimal` | Updates a ResourceSet Decimal Item |
| [UpdateResourceSetTextItem](#updateresourcesettextitem) | `PATCH /3.0/resourceitem/text` | Updates a ResourceSet Text Item |
| [UpdateResourceSetBooleanItem](#updateresourcesetbooleanitem) | `PATCH /3.0/resourceitem/bool` | Updates a ResourceSet Boolean Item |
| [UpdateResourceSetDateItem](#updateresourcesetdateitem) | `PATCH /3.0/resourceitem/date` | Updates a ResourceSet Date Item |
| [UpdateResourceSetImageItem](#updateresourcesetimageitem) | `PATCH /3.0/resourceitem/image` | Updates a ResourceSet Image Item |
| [UpdateResourceSetDataSetItem](#updateresourcesetdatasetitem) | `PATCH /3.0/resourceitem/dataset` | Updates a ResourceSet DataSet Item |
| [UpdateResourceSetBannerItem](#updateresourcesetbanneritem) | `PATCH /3.0/resourceitem/banner` | Updates a ResourceSet Banner Item |
| [UpdateResourceSetCarouselItem](#updateresourcesetcarouselitem) | `PATCH /3.0/resourceitem/carousel` | Updates a ResourceSet Carousel Item |
| [UpdateResourceSetWidgetItem](#updateresourcesetwidgetitem) | `PATCH /3.0/resourceitem/widget` | Updates a ResourceSet Widget Item |
| [UpdateResourceSetDropDownItem](#updateresourcesetdropdownitem) | `PATCH /3.0/resourceitem/dropdown` | Updates a ResourceSet DropDown Item |
| [CreateResourceSetCulture](#createresourcesetculture) | `POST /3.0/resourceset/culture` | Adds a culture to a Resource Set |
| [DeleteResourceSetCulture](#deleteresourcesetculture) | `DELETE /3.0/resourceset/culture` | Removes a cultue from a Resource Set |
| [GetResourceSetCultures](#getresourcesetcultures) | `GET /3.0/resourceset/cultureAuthorization:` | Determines the cultures available in the resource set, environment, and version the client server is subscribed to. |
| [CreateResourceSetEnvironment](#createresourcesetenvironment) | `POST /3.0/resourceset/environment` | Creates a ResourceSet Environment |
| [DeleteResourceSetEnvironment](#deleteresourcesetenvironment) | `DELETE /3.0/resourceset/environment` | Deletes a ResourceSet Environment |
| [GetResourceSetEnvironments](#getresourcesetenvironments) | `GET /3.0/resourceset/environmentAuthorization:` | Gets ResourceSet Environments |
| [UpdateResourceSetEnvironment](#updateresourcesetenvironment) | `PATCH /3.0/resourceset/environment` | Updates a ResourceSet Environment |
| [CreateResourceSetGroup](#createresourcesetgroup) | `POST /3.0/resourceset/group` | Creates a ResourceSet Group |
| [DeleteResourceSetGroup](#deleteresourcesetgroup) | `DELETE /3.0/resourceset/group` | Deletes a ResourceSet Group |
| [GetResourceSetGroups](#getresourcesetgroups) | `GET /3.0/resourceset/groupAuthorization:` | Gets ResourceSet Groups |
| [UpdateResourceSetGroup](#updateresourcesetgroup) | `PATCH /3.0/resourceset/group` | Updates a ResourceSet Group |
| [CreateRelease](#createrelease) | `POST /3.0/resourceset/release` | Creates a Resource Set release |
| [DeleteRelease](#deleterelease) | `DELETE /3.0/resourceset/release` | Deletes a Resource Set release |
| [GetReleases](#getreleases) | `GET /3.0/resourceset/releaseAuthorization:` | Gets Resource Set releases |
| [DeployRelease](#deployrelease) | `POST /3.0/resourceset/release/deploy` | Deploys a Resource Set Release |
| [RevertToRecentRelease](#reverttorecentrelease) | `POST /3.0/resourceset/release/revert` | Reverts to most recent Resource Set Release |

---
### ResourceSetCheckIn

> Keeps the client's version of the resource set up to date to the environment it is subscribed to.

| | |
|---|---|
| Category | Web Content |
| REST | `POST /3.0/resourceset/checkin` |
| SOAP action | `https://api.exigo.com/ResourceSetCheckIn` |
| WSDL elements | `ResourceSetCheckInRequest` → `ResourceSetCheckInResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=ResourceSetCheckIn |

#### Input

**`ResourceSetCheckInRequest`**

| Property | Type | Notes |
|---|---|---|
| `SubscriptionKey` | `String` |  |
| `EnvironmentCode` | `String` |  |
| `InstalledVersion` | `String` |  |
| `InstalledReleaseDate` | `DateTime` |  |
| `MachineName` | `String` |  |
| `HostAssemblyName` | `String` |  |
| `ComponentVersion` | `String` |  |

#### Output

**`ResourceSetCheckInResponse`**

| Property | Type | Notes |
|---|---|---|
| `SubscriptionKey` | `String` |  |
| `EnvironmentCode` | `String` |  |
| `Version` | `String` |  |
| `ReleaseDate` | `DateTime` |  |
| `ClassName` | `String` |  |
| `Namespace` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/resourceset/checkin HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "subscriptionKey": "",
  "environmentCode": "",
  "version": "",
  "releaseDate": "2026-11-10T00:00:00-06:00",
  "className": "",
  "namespace": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/ResourceSetCheckIn"

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
    <ResourceSetCheckInRequest xmlns="http://api.exigo.com/">
      <SubscriptionKey>string</SubscriptionKey>
      <EnvironmentCode>string</EnvironmentCode>
      <InstalledVersion>string</InstalledVersion>
      <InstalledReleaseDate>dateTime</InstalledReleaseDate>
      <MachineName>string</MachineName>
      <HostAssemblyName>string</HostAssemblyName>
      <ComponentVersion>string</ComponentVersion>
    </ResourceSetCheckInRequest>
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
    <ResourceSetCheckInResult xmlns="http://api.exigo.com/">
      <SubscriptionKey>string</SubscriptionKey>
      <EnvironmentCode>string</EnvironmentCode>
      <Version>string</Version>
      <ReleaseDate>dateTime</ReleaseDate>
      <ClassName>string</ClassName>
      <Namespace>string</Namespace>
    </ResourceSetCheckInResult>
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
    var req = new ResourceSetCheckInRequest();

    //Send Request to Server and Get Response
    var res = await api.ResourceSetCheckInAsync(req);

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
    ResourceSetCheckInRequest req = new ResourceSetCheckInRequest();

    //Send Request to Server and Get Response
    ResourceSetCheckInResponse res = api.ResourceSetCheckIn(req);

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
    Dim req as new ResourceSetCheckInRequest()

    'Send Request to Server and Get Response
    Dim res As ResourceSetCheckInResponse = api.ResourceSetCheckIn(req)

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
    $res = $api.ResourceSetCheckIn($req);

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
    ResourceSetCheckInRequest req = new ResourceSetCheckInRequest();

    //Send Request to Server and Get Response
    ResourceSetCheckInResponse res = api.getExigoApiSoap().resourceSetCheckIn(req, auth);

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

### CreateResourceSet

> Create a new ResourceSet

| | |
|---|---|
| Category | Web Content |
| REST | `POST /3.0/resourceset` |
| SOAP action | `https://api.exigo.com/CreateResourceSet` |
| WSDL elements | `CreateResourceSetRequest` → `CreateResourceSetResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateResourceSet |

#### Input

**`CreateResourceSetRequest`**

| Property | Type | Notes |
|---|---|---|
| `ClassName` | `String` | The class name of the new resource set. Must be unique, valid identifier. |
| `Description` | `String` | The description of the new resource set. All characters allowed. Must be unique. |
| `Namespace` | `String` | The namespace that will be used for the class file generated with the new resource set. Must be unique, valid identifier. |
| `SubscriptionKey` | `String` | The reference key for the new resource set. Must be unique, valid identifier. |

#### Output

**`CreateResourceSetResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` | The unique ID of the new resource set. |
| `ClassName` | `String` |  |
| `Description` | `String` |  |
| `Namespace` | `String` |  |
| `SubscriptionKey` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/resourceset HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "className": "",
  "description": "",
  "namespace": "",
  "subscriptionKey": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateResourceSet"

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
    <CreateResourceSetRequest xmlns="http://api.exigo.com/">
      <ClassName>string</ClassName>
      <Description>string</Description>
      <Namespace>string</Namespace>
      <SubscriptionKey>string</SubscriptionKey>
    </CreateResourceSetRequest>
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
    <CreateResourceSetResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <ClassName>string</ClassName>
      <Description>string</Description>
      <Namespace>string</Namespace>
      <SubscriptionKey>string</SubscriptionKey>
    </CreateResourceSetResult>
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
    var req = new CreateResourceSetRequest();

    //Send Request to Server and Get Response
    var res = await api.CreateResourceSetAsync(req);

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
    CreateResourceSetRequest req = new CreateResourceSetRequest();

    //Send Request to Server and Get Response
    CreateResourceSetResponse res = api.CreateResourceSet(req);

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
    Dim req as new CreateResourceSetRequest()

    'Send Request to Server and Get Response
    Dim res As CreateResourceSetResponse = api.CreateResourceSet(req)

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
    $res = $api.CreateResourceSet($req);

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
    CreateResourceSetRequest req = new CreateResourceSetRequest();

    //Send Request to Server and Get Response
    CreateResourceSetResponse res = api.getExigoApiSoap().createResourceSet(req, auth);

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

### RetireResourceSet

> Retire an existing ResourceSet

| | |
|---|---|
| Category | Web Content |
| REST | `DELETE /3.0/resourceset` |
| SOAP action | `https://api.exigo.com/RetireResourceSet` |
| WSDL elements | `RetireResourceSetRequest` → `RetireResourceSetResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=RetireResourceSet |

#### Input

**`RetireResourceSetRequest`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` | The unique numerical ID of the resource to retire. |

#### Output

**`RetireResourceSetResponse`**

_No properties._

#### REST example

```http
DELETE https://yourcompany-api.exigo.com/3.0/resourceset HTTP/1.1
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
SOAPAction: "https://api.exigo.com/RetireResourceSet"

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
    <RetireResourceSetRequest xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
    </RetireResourceSetRequest>
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
    <RetireResourceSetResult xmlns="http://api.exigo.com/" />
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
    var req = new RetireResourceSetRequest();

    //Send Request to Server and Get Response
    var res = await api.RetireResourceSetAsync(req);

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
    RetireResourceSetRequest req = new RetireResourceSetRequest();

    //Send Request to Server and Get Response
    RetireResourceSetResponse res = api.RetireResourceSet(req);

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
    Dim req as new RetireResourceSetRequest()

    'Send Request to Server and Get Response
    Dim res As RetireResourceSetResponse = api.RetireResourceSet(req)

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
    $res = $api.RetireResourceSet($req);

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
    RetireResourceSetRequest req = new RetireResourceSetRequest();

    //Send Request to Server and Get Response
    RetireResourceSetResponse res = api.getExigoApiSoap().retireResourceSet(req, auth);

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

### GetResourceSets

> Get an existing Resource Set

| | |
|---|---|
| Category | Web Content |
| REST | `GET /3.0/resourcesetAuthorization:` |
| SOAP action | `https://api.exigo.com/GetResourceSets` |
| WSDL elements | `GetResourceSetsRequest` → `GetResourceSetsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetResourceSets |

#### Input

**`GetResourceSetsRequest`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` | Optional. The unique numeric ID of the ResourceSet to get. If empty all ResourceSets will be fetched. |

#### Output

**`GetResourceSetsResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSets` | `ResourceSet[]` |  |

**`ResourceSet`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `ResourceSetID` | `Int32` |  |
| &nbsp;&nbsp;↳ `Description` | `String` |  |
| &nbsp;&nbsp;↳ `ClassName` | `String` |  |
| &nbsp;&nbsp;↳ `Namespace` | `String` |  |
| &nbsp;&nbsp;↳ `SubscriptionKey` | `String` |  |
| &nbsp;&nbsp;↳ `IsDeleted` | `Boolean` |  |
| &nbsp;&nbsp;↳ `ModifiedDate` | `DateTimeOffset` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/resourcesetAuthorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSets": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetResourceSets"

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
    <GetResourceSetsRequest xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
    </GetResourceSetsRequest>
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
    <GetResourceSetsResult xmlns="http://api.exigo.com/">
      <ResourceSets>
        <ResourceSet>
          <ResourceSetID>int</ResourceSetID>
          <Description>string</Description>
          <ClassName>string</ClassName>
          <Namespace>string</Namespace>
          <SubscriptionKey>string</SubscriptionKey>
          <IsDeleted>boolean</IsDeleted>
          <ModifiedDate />
        </ResourceSet>
      </ResourceSets>
    </GetResourceSetsResult>
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
    var req = new GetResourceSetsRequest();

    //Send Request to Server and Get Response
    var res = await api.GetResourceSetsAsync(req);

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
    GetResourceSetsRequest req = new GetResourceSetsRequest();

    //Send Request to Server and Get Response
    GetResourceSetsResponse res = api.GetResourceSets(req);

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
    Dim req as new GetResourceSetsRequest()

    'Send Request to Server and Get Response
    Dim res As GetResourceSetsResponse = api.GetResourceSets(req)

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
    $res = $api.GetResourceSets($req);

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
    GetResourceSetsRequest req = new GetResourceSetsRequest();

    //Send Request to Server and Get Response
    GetResourceSetsResponse res = api.getExigoApiSoap().getResourceSets(req, auth);

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

### UpdateResourceSet

> Update an existing ResourceSet

| | |
|---|---|
| Category | Web Content |
| REST | `PATCH /3.0/resourceset` |
| SOAP action | `https://api.exigo.com/UpdateResourceSet` |
| WSDL elements | `UpdateResourceSetRequest` → `UpdateResourceSetResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateResourceSet |

#### Input

**`UpdateResourceSetRequest`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` | The unique numeric ID of the resource set to update. |
| `ClassName` | `String` | Optional. The new class name for the existing resource set. Must be unique, valid identifier. |
| `Description` | `String` | Optional. The new description for the existing resource set. All characters allowed. Must be unique. |
| `Namespace` | `String` | Optional. The new namespace that will be used for the class file generated with the existing resource set. Must be valid identifier. |
| `SubscriptionKey` | `String` | Optional. The new reference key for the existing resource set. Must be unique, valid identifier. |

#### Output

**`UpdateResourceSetResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` | The unique ID of the updated resource set. |
| `ClassName` | `String` |  |
| `Description` | `String` |  |
| `Namespace` | `String` |  |
| `SubscriptionKey` | `String` |  |

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/resourceset HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "className": "",
  "description": "",
  "namespace": "",
  "subscriptionKey": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/UpdateResourceSet"

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
    <UpdateResourceSetRequest xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <ClassName>string</ClassName>
      <Description>string</Description>
      <Namespace>string</Namespace>
      <SubscriptionKey>string</SubscriptionKey>
    </UpdateResourceSetRequest>
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
    <UpdateResourceSetResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <ClassName>string</ClassName>
      <Description>string</Description>
      <Namespace>string</Namespace>
      <SubscriptionKey>string</SubscriptionKey>
    </UpdateResourceSetResult>
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
    var req = new UpdateResourceSetRequest();

    //Send Request to Server and Get Response
    var res = await api.UpdateResourceSetAsync(req);

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
    UpdateResourceSetRequest req = new UpdateResourceSetRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetResponse res = api.UpdateResourceSet(req);

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
    Dim req as new UpdateResourceSetRequest()

    'Send Request to Server and Get Response
    Dim res As UpdateResourceSetResponse = api.UpdateResourceSet(req)

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
    $res = $api.UpdateResourceSet($req);

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
    UpdateResourceSetRequest req = new UpdateResourceSetRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetResponse res = api.getExigoApiSoap().updateResourceSet(req, auth);

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

### CreateResourceSetIntItem

> Adds a ResourceSet Number Item to the ResourceSet

| | |
|---|---|
| Category | Web Content |
| REST | `POST /3.0/resourceitem/int` |
| SOAP action | `https://api.exigo.com/CreateResourceSetIntItem` |
| WSDL elements | `CreateResourceSetIntItemRequest` → `CreateResourceSetIntItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateResourceSetIntItem |

#### Input

**`CreateResourceSetIntItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `IntegerValue` | `Int32` |  |
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `ResourceType` | `ResourceType` | **Values:** `Text`, `Int`, `Decimal`, `Date`, `Boolean`, `DropDown`, `Image`, `Widget`, `Banner`, `DataSet`, `Carousel` |
| `CultureCode` | `String` | Optional. Defaults to Default CultureCode. |
| `ResourceGroupID` | `Int32` | Optional. |
| `Comment` | `String` | Optional. |
| `Enabled` | `Boolean` | Optional. . Defaults to True. |
| `EnabledStartDate` | `DateTime` | Optional. Value must be provided in UTC. |
| `EnabledEndDate` | `DateTime` | Optional. Value must be provided in UTC. |

#### Output

**`CreateResourceSetIntItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `CultureCode` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/resourceitem/int HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "resourceName": "",
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
SOAPAction: "https://api.exigo.com/CreateResourceSetIntItem"

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
    <CreateResourceSetIntItemRequest xmlns="http://api.exigo.com/">
      <IntegerValue>int</IntegerValue>
    </CreateResourceSetIntItemRequest>
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
    <CreateResourceSetIntItemResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <ResourceName>string</ResourceName>
      <CultureCode>string</CultureCode>
    </CreateResourceSetIntItemResult>
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
    var req = new CreateResourceSetIntItemRequest();

    //Send Request to Server and Get Response
    var res = await api.CreateResourceSetIntItemAsync(req);

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
    CreateResourceSetIntItemRequest req = new CreateResourceSetIntItemRequest();

    //Send Request to Server and Get Response
    CreateResourceSetIntItemResponse res = api.CreateResourceSetIntItem(req);

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
    Dim req as new CreateResourceSetIntItemRequest()

    'Send Request to Server and Get Response
    Dim res As CreateResourceSetIntItemResponse = api.CreateResourceSetIntItem(req)

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
    $res = $api.CreateResourceSetIntItem($req);

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
    CreateResourceSetIntItemRequest req = new CreateResourceSetIntItemRequest();

    //Send Request to Server and Get Response
    CreateResourceSetIntItemResponse res = api.getExigoApiSoap().createResourceSetIntItem(req, auth);

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

### CreateResourceSetDecimalItem

> Adds a ResourceSet Decimal Item to the ResourceSet

| | |
|---|---|
| Category | Web Content |
| REST | `POST /3.0/resourceitem/decimal` |
| SOAP action | `https://api.exigo.com/CreateResourceSetDecimalItem` |
| WSDL elements | `CreateResourceSetDecimalItemRequest` → `CreateResourceSetDecimalItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateResourceSetDecimalItem |

#### Input

**`CreateResourceSetDecimalItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `DecimalValue` | `Decimal` |  |
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `ResourceType` | `ResourceType` | **Values:** `Text`, `Int`, `Decimal`, `Date`, `Boolean`, `DropDown`, `Image`, `Widget`, `Banner`, `DataSet`, `Carousel` |
| `CultureCode` | `String` | Optional. Defaults to Default CultureCode. |
| `ResourceGroupID` | `Int32` | Optional. |
| `Comment` | `String` | Optional. |
| `Enabled` | `Boolean` | Optional. . Defaults to True. |
| `EnabledStartDate` | `DateTime` | Optional. Value must be provided in UTC. |
| `EnabledEndDate` | `DateTime` | Optional. Value must be provided in UTC. |

#### Output

**`CreateResourceSetDecimalItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `CultureCode` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/resourceitem/decimal HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "resourceName": "",
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
SOAPAction: "https://api.exigo.com/CreateResourceSetDecimalItem"

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
    <CreateResourceSetDecimalItemRequest xmlns="http://api.exigo.com/">
      <DecimalValue>decimal</DecimalValue>
    </CreateResourceSetDecimalItemRequest>
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
    <CreateResourceSetDecimalItemResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <ResourceName>string</ResourceName>
      <CultureCode>string</CultureCode>
    </CreateResourceSetDecimalItemResult>
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
    var req = new CreateResourceSetDecimalItemRequest();

    //Send Request to Server and Get Response
    var res = await api.CreateResourceSetDecimalItemAsync(req);

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
    CreateResourceSetDecimalItemRequest req = new CreateResourceSetDecimalItemRequest();

    //Send Request to Server and Get Response
    CreateResourceSetDecimalItemResponse res = api.CreateResourceSetDecimalItem(req);

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
    Dim req as new CreateResourceSetDecimalItemRequest()

    'Send Request to Server and Get Response
    Dim res As CreateResourceSetDecimalItemResponse = api.CreateResourceSetDecimalItem(req)

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
    $res = $api.CreateResourceSetDecimalItem($req);

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
    CreateResourceSetDecimalItemRequest req = new CreateResourceSetDecimalItemRequest();

    //Send Request to Server and Get Response
    CreateResourceSetDecimalItemResponse res = api.getExigoApiSoap().createResourceSetDecimalItem(req, auth);

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

### CreateResourceSetTextItem

> Adds a ResourceSet Text Item to the ResourceSet

| | |
|---|---|
| Category | Web Content |
| REST | `POST /3.0/resourceitem/text` |
| SOAP action | `https://api.exigo.com/CreateResourceSetTextItem` |
| WSDL elements | `CreateResourceSetTextItemRequest` → `CreateResourceSetTextItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateResourceSetTextItem |

#### Input

**`CreateResourceSetTextItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `Text` | `String` |  |
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `ResourceType` | `ResourceType` | **Values:** `Text`, `Int`, `Decimal`, `Date`, `Boolean`, `DropDown`, `Image`, `Widget`, `Banner`, `DataSet`, `Carousel` |
| `CultureCode` | `String` | Optional. Defaults to Default CultureCode. |
| `ResourceGroupID` | `Int32` | Optional. |
| `Comment` | `String` | Optional. |
| `Enabled` | `Boolean` | Optional. . Defaults to True. |
| `EnabledStartDate` | `DateTime` | Optional. Value must be provided in UTC. |
| `EnabledEndDate` | `DateTime` | Optional. Value must be provided in UTC. |

#### Output

**`CreateResourceSetTextItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `CultureCode` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/resourceitem/text HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "resourceName": "",
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
SOAPAction: "https://api.exigo.com/CreateResourceSetTextItem"

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
    <CreateResourceSetTextItemRequest xmlns="http://api.exigo.com/">
      <Text>string</Text>
    </CreateResourceSetTextItemRequest>
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
    <CreateResourceSetTextItemResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <ResourceName>string</ResourceName>
      <CultureCode>string</CultureCode>
    </CreateResourceSetTextItemResult>
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
    var req = new CreateResourceSetTextItemRequest();

    //Send Request to Server and Get Response
    var res = await api.CreateResourceSetTextItemAsync(req);

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
    CreateResourceSetTextItemRequest req = new CreateResourceSetTextItemRequest();

    //Send Request to Server and Get Response
    CreateResourceSetTextItemResponse res = api.CreateResourceSetTextItem(req);

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
    Dim req as new CreateResourceSetTextItemRequest()

    'Send Request to Server and Get Response
    Dim res As CreateResourceSetTextItemResponse = api.CreateResourceSetTextItem(req)

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
    $res = $api.CreateResourceSetTextItem($req);

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
    CreateResourceSetTextItemRequest req = new CreateResourceSetTextItemRequest();

    //Send Request to Server and Get Response
    CreateResourceSetTextItemResponse res = api.getExigoApiSoap().createResourceSetTextItem(req, auth);

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

### CreateResourceSetBooleanItem

> Adds a ResourceSet CheckBox Item to the ResourceSet

| | |
|---|---|
| Category | Web Content |
| REST | `POST /3.0/resourceitem/bool` |
| SOAP action | `https://api.exigo.com/CreateResourceSetBooleanItem` |
| WSDL elements | `CreateResourceSetBooleanItemRequest` → `CreateResourceSetBooleanItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateResourceSetBooleanItem |

#### Input

**`CreateResourceSetBooleanItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `BooleanValue` | `Boolean` |  |
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `ResourceType` | `ResourceType` | **Values:** `Text`, `Int`, `Decimal`, `Date`, `Boolean`, `DropDown`, `Image`, `Widget`, `Banner`, `DataSet`, `Carousel` |
| `CultureCode` | `String` | Optional. Defaults to Default CultureCode. |
| `ResourceGroupID` | `Int32` | Optional. |
| `Comment` | `String` | Optional. |
| `Enabled` | `Boolean` | Optional. . Defaults to True. |
| `EnabledStartDate` | `DateTime` | Optional. Value must be provided in UTC. |
| `EnabledEndDate` | `DateTime` | Optional. Value must be provided in UTC. |

#### Output

**`CreateResourceSetBooleanItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `CultureCode` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/resourceitem/bool HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "resourceName": "",
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
SOAPAction: "https://api.exigo.com/CreateResourceSetBooleanItem"

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
    <CreateResourceSetBooleanItemRequest xmlns="http://api.exigo.com/">
      <BooleanValue>boolean</BooleanValue>
    </CreateResourceSetBooleanItemRequest>
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
    <CreateResourceSetBooleanItemResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <ResourceName>string</ResourceName>
      <CultureCode>string</CultureCode>
    </CreateResourceSetBooleanItemResult>
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
    var req = new CreateResourceSetBooleanItemRequest();

    //Send Request to Server and Get Response
    var res = await api.CreateResourceSetBooleanItemAsync(req);

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
    CreateResourceSetBooleanItemRequest req = new CreateResourceSetBooleanItemRequest();

    //Send Request to Server and Get Response
    CreateResourceSetBooleanItemResponse res = api.CreateResourceSetBooleanItem(req);

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
    Dim req as new CreateResourceSetBooleanItemRequest()

    'Send Request to Server and Get Response
    Dim res As CreateResourceSetBooleanItemResponse = api.CreateResourceSetBooleanItem(req)

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
    $res = $api.CreateResourceSetBooleanItem($req);

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
    CreateResourceSetBooleanItemRequest req = new CreateResourceSetBooleanItemRequest();

    //Send Request to Server and Get Response
    CreateResourceSetBooleanItemResponse res = api.getExigoApiSoap().createResourceSetBooleanItem(req, auth);

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

### CreateResourceSetDateItem

> Adds a ResourceSet Date Item to the ResourceSet

| | |
|---|---|
| Category | Web Content |
| REST | `POST /3.0/resourceitem/date` |
| SOAP action | `https://api.exigo.com/CreateResourceSetDateItem` |
| WSDL elements | `CreateResourceSetDateItemRequest` → `CreateResourceSetDateItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateResourceSetDateItem |

#### Input

**`CreateResourceSetDateItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `Date` | `DateTime` |  |
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `ResourceType` | `ResourceType` | **Values:** `Text`, `Int`, `Decimal`, `Date`, `Boolean`, `DropDown`, `Image`, `Widget`, `Banner`, `DataSet`, `Carousel` |
| `CultureCode` | `String` | Optional. Defaults to Default CultureCode. |
| `ResourceGroupID` | `Int32` | Optional. |
| `Comment` | `String` | Optional. |
| `Enabled` | `Boolean` | Optional. . Defaults to True. |
| `EnabledStartDate` | `DateTime` | Optional. Value must be provided in UTC. |
| `EnabledEndDate` | `DateTime` | Optional. Value must be provided in UTC. |

#### Output

**`CreateResourceSetDateItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `CultureCode` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/resourceitem/date HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "resourceName": "",
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
SOAPAction: "https://api.exigo.com/CreateResourceSetDateItem"

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
    <CreateResourceSetDateItemRequest xmlns="http://api.exigo.com/">
      <Date>dateTime</Date>
    </CreateResourceSetDateItemRequest>
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
    <CreateResourceSetDateItemResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <ResourceName>string</ResourceName>
      <CultureCode>string</CultureCode>
    </CreateResourceSetDateItemResult>
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
    var req = new CreateResourceSetDateItemRequest();

    //Send Request to Server and Get Response
    var res = await api.CreateResourceSetDateItemAsync(req);

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
    CreateResourceSetDateItemRequest req = new CreateResourceSetDateItemRequest();

    //Send Request to Server and Get Response
    CreateResourceSetDateItemResponse res = api.CreateResourceSetDateItem(req);

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
    Dim req as new CreateResourceSetDateItemRequest()

    'Send Request to Server and Get Response
    Dim res As CreateResourceSetDateItemResponse = api.CreateResourceSetDateItem(req)

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
    $res = $api.CreateResourceSetDateItem($req);

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
    CreateResourceSetDateItemRequest req = new CreateResourceSetDateItemRequest();

    //Send Request to Server and Get Response
    CreateResourceSetDateItemResponse res = api.getExigoApiSoap().createResourceSetDateItem(req, auth);

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

### CreateResourceSetImageItem

> Adds a ResourceSet Image Item to the ResourceSet

| | |
|---|---|
| Category | Web Content |
| REST | `POST /3.0/resourceitem/image` |
| SOAP action | `https://api.exigo.com/CreateResourceSetImageItem` |
| WSDL elements | `CreateResourceSetImageItemRequest` → `CreateResourceSetImageItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateResourceSetImageItem |

#### Input

**`CreateResourceSetImageItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `Base64ImageData` | `String` | Must be valid Base64 image data. |
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `ResourceType` | `ResourceType` | **Values:** `Text`, `Int`, `Decimal`, `Date`, `Boolean`, `DropDown`, `Image`, `Widget`, `Banner`, `DataSet`, `Carousel` |
| `CultureCode` | `String` | Optional. Defaults to Default CultureCode. |
| `ResourceGroupID` | `Int32` | Optional. |
| `Comment` | `String` | Optional. |
| `Enabled` | `Boolean` | Optional. . Defaults to True. |
| `EnabledStartDate` | `DateTime` | Optional. Value must be provided in UTC. |
| `EnabledEndDate` | `DateTime` | Optional. Value must be provided in UTC. |

#### Output

**`CreateResourceSetImageItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `CultureCode` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/resourceitem/image HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "resourceName": "",
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
SOAPAction: "https://api.exigo.com/CreateResourceSetImageItem"

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
    <CreateResourceSetImageItemRequest xmlns="http://api.exigo.com/">
      <Base64ImageData>string</Base64ImageData>
    </CreateResourceSetImageItemRequest>
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
    <CreateResourceSetImageItemResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <ResourceName>string</ResourceName>
      <CultureCode>string</CultureCode>
    </CreateResourceSetImageItemResult>
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
    var req = new CreateResourceSetImageItemRequest();

    //Send Request to Server and Get Response
    var res = await api.CreateResourceSetImageItemAsync(req);

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
    CreateResourceSetImageItemRequest req = new CreateResourceSetImageItemRequest();

    //Send Request to Server and Get Response
    CreateResourceSetImageItemResponse res = api.CreateResourceSetImageItem(req);

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
    Dim req as new CreateResourceSetImageItemRequest()

    'Send Request to Server and Get Response
    Dim res As CreateResourceSetImageItemResponse = api.CreateResourceSetImageItem(req)

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
    $res = $api.CreateResourceSetImageItem($req);

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
    CreateResourceSetImageItemRequest req = new CreateResourceSetImageItemRequest();

    //Send Request to Server and Get Response
    CreateResourceSetImageItemResponse res = api.getExigoApiSoap().createResourceSetImageItem(req, auth);

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

### CreateResourceSetDataSetItem

> Adds a ResourceSet DataSet Item to the ResourceSet

| | |
|---|---|
| Category | Web Content |
| REST | `POST /3.0/resourceitem/dataset` |
| SOAP action | `https://api.exigo.com/CreateResourceSetDataSetItem` |
| WSDL elements | `CreateResourceSetDataSetItemRequest` → `CreateResourceSetDataSetItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateResourceSetDataSetItem |

#### Input

**`CreateResourceSetDataSetItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `DataSetType` | `String` |  |
| `DataSetValues` | `String[]` |  |
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `ResourceType` | `ResourceType` | **Values:** `Text`, `Int`, `Decimal`, `Date`, `Boolean`, `DropDown`, `Image`, `Widget`, `Banner`, `DataSet`, `Carousel` |
| `CultureCode` | `String` | Optional. Defaults to Default CultureCode. |
| `ResourceGroupID` | `Int32` | Optional. |
| `Comment` | `String` | Optional. |
| `Enabled` | `Boolean` | Optional. . Defaults to True. |
| `EnabledStartDate` | `DateTime` | Optional. Value must be provided in UTC. |
| `EnabledEndDate` | `DateTime` | Optional. Value must be provided in UTC. |

#### Output

**`CreateResourceSetDataSetItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `CultureCode` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/resourceitem/dataset HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "resourceName": "",
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
SOAPAction: "https://api.exigo.com/CreateResourceSetDataSetItem"

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
    <CreateResourceSetDataSetItemRequest xmlns="http://api.exigo.com/">
      <DataSetType>string</DataSetType>
      <DataSetValues>
        <string>string</string>
      </DataSetValues>
    </CreateResourceSetDataSetItemRequest>
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
    <CreateResourceSetDataSetItemResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <ResourceName>string</ResourceName>
      <CultureCode>string</CultureCode>
    </CreateResourceSetDataSetItemResult>
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
    var req = new CreateResourceSetDataSetItemRequest();

    //Send Request to Server and Get Response
    var res = await api.CreateResourceSetDataSetItemAsync(req);

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
    CreateResourceSetDataSetItemRequest req = new CreateResourceSetDataSetItemRequest();

    //Send Request to Server and Get Response
    CreateResourceSetDataSetItemResponse res = api.CreateResourceSetDataSetItem(req);

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
    Dim req as new CreateResourceSetDataSetItemRequest()

    'Send Request to Server and Get Response
    Dim res As CreateResourceSetDataSetItemResponse = api.CreateResourceSetDataSetItem(req)

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
    $res = $api.CreateResourceSetDataSetItem($req);

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
    CreateResourceSetDataSetItemRequest req = new CreateResourceSetDataSetItemRequest();

    //Send Request to Server and Get Response
    CreateResourceSetDataSetItemResponse res = api.getExigoApiSoap().createResourceSetDataSetItem(req, auth);

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

### CreateResourceSetBannerItem

> Adds a ResourceSet Banner Item to the ResourceSet

| | |
|---|---|
| Category | Web Content |
| REST | `POST /3.0/resourceitem/banner` |
| SOAP action | `https://api.exigo.com/CreateResourceSetBannerItem` |
| WSDL elements | `CreateResourceSetBannerItemRequest` → `CreateResourceSetBannerItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateResourceSetBannerItem |

#### Input

**`CreateResourceSetBannerItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `Title` | `String` | The main header message for your banner. |
| `Description` | `String` | The sub-header message for your banner. |
| `BannerImageBase64` | `String` | The Base64 representation of the image for your banner. |
| `BannerHoverText` | `String` | ResourceBanner field. |
| `BannerURL` | `String` | The URL the user is navigated to when clicking the banner. |
| `BannerClickEvent` | `BannerClickEvent` | How the url attached to the banner is navigated to when the banner is clicked.<br>**Values:** `OpenInNewTab`, `OpenInCurrentWindow`, `None` |
| `BannerType` | `BannerType` | BannerTypes dictate the formatting for a banner.<br>**Values:** `TextOnImage`, `ImageTop`, `InvalidType` |
| `AssociatedDataSets` | `String[]` | List of the DataSets by ResourceName associated with this banner. |
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `ResourceType` | `ResourceType` | **Values:** `Text`, `Int`, `Decimal`, `Date`, `Boolean`, `DropDown`, `Image`, `Widget`, `Banner`, `DataSet`, `Carousel` |
| `CultureCode` | `String` | Optional. Defaults to Default CultureCode. |
| `ResourceGroupID` | `Int32` | Optional. |
| `Comment` | `String` | Optional. |
| `Enabled` | `Boolean` | Optional. . Defaults to True. |
| `EnabledStartDate` | `DateTime` | Optional. Value must be provided in UTC. |
| `EnabledEndDate` | `DateTime` | Optional. Value must be provided in UTC. |

#### Output

**`CreateResourceSetBannerItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `CultureCode` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/resourceitem/banner HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "resourceName": "",
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
SOAPAction: "https://api.exigo.com/CreateResourceSetBannerItem"

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
    <CreateResourceSetBannerItemRequest xmlns="http://api.exigo.com/">
      <Title>string</Title>
      <Description>string</Description>
      <BannerImageBase64>string</BannerImageBase64>
      <BannerHoverText>string</BannerHoverText>
      <BannerURL>string</BannerURL>
      <BannerClickEvent>OpenInNewTab or OpenInCurrentWindow or None</BannerClickEvent>
      <BannerType>TextOnImage or ImageTop or InvalidType</BannerType>
      <AssociatedDataSets>
        <string>string</string>
      </AssociatedDataSets>
    </CreateResourceSetBannerItemRequest>
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
    <CreateResourceSetBannerItemResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <ResourceName>string</ResourceName>
      <CultureCode>string</CultureCode>
    </CreateResourceSetBannerItemResult>
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
    var req = new CreateResourceSetBannerItemRequest();

    //Send Request to Server and Get Response
    var res = await api.CreateResourceSetBannerItemAsync(req);

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
    CreateResourceSetBannerItemRequest req = new CreateResourceSetBannerItemRequest();

    //Send Request to Server and Get Response
    CreateResourceSetBannerItemResponse res = api.CreateResourceSetBannerItem(req);

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
    Dim req as new CreateResourceSetBannerItemRequest()

    'Send Request to Server and Get Response
    Dim res As CreateResourceSetBannerItemResponse = api.CreateResourceSetBannerItem(req)

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
    $res = $api.CreateResourceSetBannerItem($req);

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
    CreateResourceSetBannerItemRequest req = new CreateResourceSetBannerItemRequest();

    //Send Request to Server and Get Response
    CreateResourceSetBannerItemResponse res = api.getExigoApiSoap().createResourceSetBannerItem(req, auth);

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

### CreateResourceSetCarouselItem

> Adds a ResourceSet Carousel Item to the ResourceSet

| | |
|---|---|
| Category | Web Content |
| REST | `POST /3.0/resourceitem/carousel` |
| SOAP action | `https://api.exigo.com/CreateResourceSetCarouselItem` |
| WSDL elements | `CreateResourceSetCarouselItemRequest` → `CreateResourceSetCarouselItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateResourceSetCarouselItem |

#### Input

**`CreateResourceSetCarouselItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `CarouselSlides` | `String[]` | List of the banners by ResourceName associated with this carousel. |
| `CarouselType` | `CarouselType` | Dictates what bootstrap version to display the carousel as.<br>**Values:** `Bootstrap3`, `Bootstrap4`, `Bootstrap5` |
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `ResourceType` | `ResourceType` | **Values:** `Text`, `Int`, `Decimal`, `Date`, `Boolean`, `DropDown`, `Image`, `Widget`, `Banner`, `DataSet`, `Carousel` |
| `CultureCode` | `String` | Optional. Defaults to Default CultureCode. |
| `ResourceGroupID` | `Int32` | Optional. |
| `Comment` | `String` | Optional. |
| `Enabled` | `Boolean` | Optional. . Defaults to True. |
| `EnabledStartDate` | `DateTime` | Optional. Value must be provided in UTC. |
| `EnabledEndDate` | `DateTime` | Optional. Value must be provided in UTC. |

#### Output

**`CreateResourceSetCarouselItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `CultureCode` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/resourceitem/carousel HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "resourceName": "",
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
SOAPAction: "https://api.exigo.com/CreateResourceSetCarouselItem"

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
    <CreateResourceSetCarouselItemRequest xmlns="http://api.exigo.com/">
      <CarouselSlides>
        <string>string</string>
      </CarouselSlides>
      <CarouselType>Bootstrap3 or Bootstrap4 or Bootstrap5</CarouselType>
    </CreateResourceSetCarouselItemRequest>
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
    <CreateResourceSetCarouselItemResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <ResourceName>string</ResourceName>
      <CultureCode>string</CultureCode>
    </CreateResourceSetCarouselItemResult>
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
    var req = new CreateResourceSetCarouselItemRequest();

    //Send Request to Server and Get Response
    var res = await api.CreateResourceSetCarouselItemAsync(req);

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
    CreateResourceSetCarouselItemRequest req = new CreateResourceSetCarouselItemRequest();

    //Send Request to Server and Get Response
    CreateResourceSetCarouselItemResponse res = api.CreateResourceSetCarouselItem(req);

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
    Dim req as new CreateResourceSetCarouselItemRequest()

    'Send Request to Server and Get Response
    Dim res As CreateResourceSetCarouselItemResponse = api.CreateResourceSetCarouselItem(req)

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
    $res = $api.CreateResourceSetCarouselItem($req);

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
    CreateResourceSetCarouselItemRequest req = new CreateResourceSetCarouselItemRequest();

    //Send Request to Server and Get Response
    CreateResourceSetCarouselItemResponse res = api.getExigoApiSoap().createResourceSetCarouselItem(req, auth);

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

### CreateResourceSetWidgetItem

> Adds a ResourceSet Widget Item to the ResourceSet

| | |
|---|---|
| Category | Web Content |
| REST | `POST /3.0/resourceitem/widget` |
| SOAP action | `https://api.exigo.com/CreateResourceSetWidgetItem` |
| WSDL elements | `CreateResourceSetWidgetItemRequest` → `CreateResourceSetWidgetItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateResourceSetWidgetItem |

#### Input

**`CreateResourceSetWidgetItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `Html` | `String` |  |
| `Javascript` | `String` |  |
| `Css` | `String` |  |
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `ResourceType` | `ResourceType` | **Values:** `Text`, `Int`, `Decimal`, `Date`, `Boolean`, `DropDown`, `Image`, `Widget`, `Banner`, `DataSet`, `Carousel` |
| `CultureCode` | `String` | Optional. Defaults to Default CultureCode. |
| `ResourceGroupID` | `Int32` | Optional. |
| `Comment` | `String` | Optional. |
| `Enabled` | `Boolean` | Optional. . Defaults to True. |
| `EnabledStartDate` | `DateTime` | Optional. Value must be provided in UTC. |
| `EnabledEndDate` | `DateTime` | Optional. Value must be provided in UTC. |

#### Output

**`CreateResourceSetWidgetItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `CultureCode` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/resourceitem/widget HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "resourceName": "",
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
SOAPAction: "https://api.exigo.com/CreateResourceSetWidgetItem"

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
    <CreateResourceSetWidgetItemRequest xmlns="http://api.exigo.com/">
      <Html>string</Html>
      <Javascript>string</Javascript>
      <Css>string</Css>
    </CreateResourceSetWidgetItemRequest>
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
    <CreateResourceSetWidgetItemResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <ResourceName>string</ResourceName>
      <CultureCode>string</CultureCode>
    </CreateResourceSetWidgetItemResult>
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
    var req = new CreateResourceSetWidgetItemRequest();

    //Send Request to Server and Get Response
    var res = await api.CreateResourceSetWidgetItemAsync(req);

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
    CreateResourceSetWidgetItemRequest req = new CreateResourceSetWidgetItemRequest();

    //Send Request to Server and Get Response
    CreateResourceSetWidgetItemResponse res = api.CreateResourceSetWidgetItem(req);

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
    Dim req as new CreateResourceSetWidgetItemRequest()

    'Send Request to Server and Get Response
    Dim res As CreateResourceSetWidgetItemResponse = api.CreateResourceSetWidgetItem(req)

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
    $res = $api.CreateResourceSetWidgetItem($req);

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
    CreateResourceSetWidgetItemRequest req = new CreateResourceSetWidgetItemRequest();

    //Send Request to Server and Get Response
    CreateResourceSetWidgetItemResponse res = api.getExigoApiSoap().createResourceSetWidgetItem(req, auth);

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

### CreateResourceSetDropDownItem

> Adds a ResourceSet DropDown Item to the ResourceSet

| | |
|---|---|
| Category | Web Content |
| REST | `POST /3.0/resourceitem/dropdown` |
| SOAP action | `https://api.exigo.com/CreateResourceSetDropDownItem` |
| WSDL elements | `CreateResourceSetDropDownItemRequest` → `CreateResourceSetDropDownItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateResourceSetDropDownItem |

#### Input

**`CreateResourceSetDropDownItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `DropDownValues` | `String` | Comma separated DropDown values. |
| `DefaultSelectedValue` | `String` | Must be one of the DropDownValues. |
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `ResourceType` | `ResourceType` | **Values:** `Text`, `Int`, `Decimal`, `Date`, `Boolean`, `DropDown`, `Image`, `Widget`, `Banner`, `DataSet`, `Carousel` |
| `CultureCode` | `String` | Optional. Defaults to Default CultureCode. |
| `ResourceGroupID` | `Int32` | Optional. |
| `Comment` | `String` | Optional. |
| `Enabled` | `Boolean` | Optional. . Defaults to True. |
| `EnabledStartDate` | `DateTime` | Optional. Value must be provided in UTC. |
| `EnabledEndDate` | `DateTime` | Optional. Value must be provided in UTC. |

#### Output

**`CreateResourceSetDropDownItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `CultureCode` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/resourceitem/dropdown HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "resourceName": "",
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
SOAPAction: "https://api.exigo.com/CreateResourceSetDropDownItem"

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
    <CreateResourceSetDropDownItemRequest xmlns="http://api.exigo.com/">
      <DropDownValues>string</DropDownValues>
      <DefaultSelectedValue>string</DefaultSelectedValue>
    </CreateResourceSetDropDownItemRequest>
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
    <CreateResourceSetDropDownItemResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <ResourceName>string</ResourceName>
      <CultureCode>string</CultureCode>
    </CreateResourceSetDropDownItemResult>
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
    var req = new CreateResourceSetDropDownItemRequest();

    //Send Request to Server and Get Response
    var res = await api.CreateResourceSetDropDownItemAsync(req);

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
    CreateResourceSetDropDownItemRequest req = new CreateResourceSetDropDownItemRequest();

    //Send Request to Server and Get Response
    CreateResourceSetDropDownItemResponse res = api.CreateResourceSetDropDownItem(req);

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
    Dim req as new CreateResourceSetDropDownItemRequest()

    'Send Request to Server and Get Response
    Dim res As CreateResourceSetDropDownItemResponse = api.CreateResourceSetDropDownItem(req)

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
    $res = $api.CreateResourceSetDropDownItem($req);

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
    CreateResourceSetDropDownItemRequest req = new CreateResourceSetDropDownItemRequest();

    //Send Request to Server and Get Response
    CreateResourceSetDropDownItemResponse res = api.getExigoApiSoap().createResourceSetDropDownItem(req, auth);

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

### DeleteResourceSetItem

> Deletes a ResourceSet Item

| | |
|---|---|
| Category | Web Content |
| REST | `DELETE /3.0/resourceitem` |
| SOAP action | `https://api.exigo.com/DeleteResourceSetItem` |
| WSDL elements | `DeleteResourceSetItemRequest` → `DeleteResourceSetItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DeleteResourceSetItem |

#### Input

**`DeleteResourceSetItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `CultureCode` | `String` | Optional. Warning, if CultureCode is not provided, ResourceItem will be deleted for default culture and all children. |

#### Output

**`DeleteResourceSetItemResponse`**

_No properties._

#### REST example

```http
DELETE https://yourcompany-api.exigo.com/3.0/resourceitem HTTP/1.1
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
SOAPAction: "https://api.exigo.com/DeleteResourceSetItem"

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
    <DeleteResourceSetItemRequest xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <ResourceName>string</ResourceName>
      <CultureCode>string</CultureCode>
    </DeleteResourceSetItemRequest>
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
    <DeleteResourceSetItemResult xmlns="http://api.exigo.com/" />
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
    var req = new DeleteResourceSetItemRequest();

    //Send Request to Server and Get Response
    var res = await api.DeleteResourceSetItemAsync(req);

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
    DeleteResourceSetItemRequest req = new DeleteResourceSetItemRequest();

    //Send Request to Server and Get Response
    DeleteResourceSetItemResponse res = api.DeleteResourceSetItem(req);

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
    Dim req as new DeleteResourceSetItemRequest()

    'Send Request to Server and Get Response
    Dim res As DeleteResourceSetItemResponse = api.DeleteResourceSetItem(req)

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
    $res = $api.DeleteResourceSetItem($req);

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
    DeleteResourceSetItemRequest req = new DeleteResourceSetItemRequest();

    //Send Request to Server and Get Response
    DeleteResourceSetItemResponse res = api.getExigoApiSoap().deleteResourceSetItem(req, auth);

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

### GetResourceSetItems

> Gets ResourceSet Items

| | |
|---|---|
| Category | Web Content |
| REST | `GET /3.0/resourceitemAuthorization:` |
| SOAP action | `https://api.exigo.com/GetResourceSetItems` |
| WSDL elements | `GetResourceSetItemsRequest` → `GetResourceSetItemsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetResourceSetItems |

#### Input

**`GetResourceSetItemsRequest`**

| Property | Type | Notes |
|---|---|---|
| `SubscriptionKey` | `String` | Optional. Pass in either SubscriptionKey or ResourceSetID. |
| `Version` | `String` | Optional. If Version is null, the items in the most recent changes are returned. |
| `CultureCode` | `String` | Optional. If CultureCode is null, the items in the default language are returned. |
| `ResourceSetID` | `Int32` | Optional. |

#### Output

**`GetResourceSetItemsResponse`**

| Property | Type | Notes |
|---|---|---|
| `Items` | `ResourceItem[]` |  |

**`ResourceItem`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `ResourceName` | `String` |  |
| &nbsp;&nbsp;↳ `InvariantValue` | `String` |  |
| &nbsp;&nbsp;↳ `Comment` | `String` |  |
| &nbsp;&nbsp;↳ `Enabled` | `Boolean` |  |
| &nbsp;&nbsp;↳ `EnabledStartDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `EnabledEndDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `ModifiedDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `ResourceTypeID` | `ResourceType` | **Values:** `Text`, `Int`, `Decimal`, `Date`, `Boolean`, `DropDown`, `Image`, `Widget`, `Banner`, `DataSet`, `Carousel` |
| &nbsp;&nbsp;↳ `ResourceSetID` | `Int32` |  |
| &nbsp;&nbsp;↳ `CultureCode` | `String` |  |
| &nbsp;&nbsp;↳ `ResourceGroupID` | `Int32` |  |
| &nbsp;&nbsp;↳ `DropDownValues` | `String` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/resourceitemAuthorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "items": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetResourceSetItems"

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
    <GetResourceSetItemsRequest xmlns="http://api.exigo.com/">
      <SubscriptionKey>string</SubscriptionKey>
      <Version>string</Version>
      <CultureCode>string</CultureCode>
      <ResourceSetID>int</ResourceSetID>
    </GetResourceSetItemsRequest>
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
    <GetResourceSetItemsResult xmlns="http://api.exigo.com/">
      <Items>
        <ResourceItem>
          <ResourceName>string</ResourceName>
          <InvariantValue>string</InvariantValue>
          <Comment>string</Comment>
          <Enabled>boolean</Enabled>
          <EnabledStartDate>dateTime</EnabledStartDate>
          <EnabledEndDate>dateTime</EnabledEndDate>
          <ModifiedDate>dateTime</ModifiedDate>
          <ResourceTypeID>Text or Int or Decimal or Date or Boolean or DropDown or Image or Widget or Banner or DataSet or Carousel</ResourceTypeID>
          <ResourceSetID>int</ResourceSetID>
          <CultureCode>string</CultureCode>
          <ResourceGroupID>int</ResourceGroupID>
          <DropDownValues>string</DropDownValues>
        </ResourceItem>
      </Items>
    </GetResourceSetItemsResult>
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
    var req = new GetResourceSetItemsRequest();

    //Send Request to Server and Get Response
    var res = await api.GetResourceSetItemsAsync(req);

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
    GetResourceSetItemsRequest req = new GetResourceSetItemsRequest();

    //Send Request to Server and Get Response
    GetResourceSetItemsResponse res = api.GetResourceSetItems(req);

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
    Dim req as new GetResourceSetItemsRequest()

    'Send Request to Server and Get Response
    Dim res As GetResourceSetItemsResponse = api.GetResourceSetItems(req)

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
    $res = $api.GetResourceSetItems($req);

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
    GetResourceSetItemsRequest req = new GetResourceSetItemsRequest();

    //Send Request to Server and Get Response
    GetResourceSetItemsResponse res = api.getExigoApiSoap().getResourceSetItems(req, auth);

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

### UpdateResourceSetIntItem

> Updates a ResourceSet Int Item

| | |
|---|---|
| Category | Web Content |
| REST | `PATCH /3.0/resourceitem/int` |
| SOAP action | `https://api.exigo.com/UpdateResourceSetIntItem` |
| WSDL elements | `UpdateResourceSetIntItemRequest` → `UpdateResourceSetIntItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateResourceSetIntItem |

#### Input

**`UpdateResourceSetIntItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `NewIntegerValue` | `Int32` | Optional. Fill to update, otherwise leave empty. |
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `CultureCode` | `String` | Optional. Defaults to Default CultureCode. |
| `NewResourceName` | `String` | Optional. Fill to update, otherwise leave empty. |
| `NewResourceGroupID` | `Int32` | Optional. Fill to update, otherwise leave empty. |
| `NewComment` | `String` | Optional. Fill to update, otherwise leave empty. |
| `NewEnabled` | `Boolean` | Optional. Fill to update, otherwise leave empty. |
| `NewEnabledStartDate` | `DateTime` | Optional. Fill to update, otherwise leave empty. Value must be provided in UTC. |
| `NewEnabledEndDate` | `DateTime` | Optional. Fill to update, otherwise leave empty. Value must be provided in UTC. |

#### Output

**`UpdateResourceSetIntItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `CultureCode` | `String` |  |
| `ResourceName` | `String` |  |

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/resourceitem/int HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "cultureCode": "",
  "resourceName": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/UpdateResourceSetIntItem"

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
    <UpdateResourceSetIntItemRequest xmlns="http://api.exigo.com/">
      <NewIntegerValue>int</NewIntegerValue>
    </UpdateResourceSetIntItemRequest>
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
    <UpdateResourceSetIntItemResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <CultureCode>string</CultureCode>
      <ResourceName>string</ResourceName>
    </UpdateResourceSetIntItemResult>
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
    var req = new UpdateResourceSetIntItemRequest();

    //Send Request to Server and Get Response
    var res = await api.UpdateResourceSetIntItemAsync(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("CultureCode: {0}", res.CultureCode);
    Console.WriteLine("ResourceName: {0}", res.ResourceName);
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
    UpdateResourceSetIntItemRequest req = new UpdateResourceSetIntItemRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetIntItemResponse res = api.UpdateResourceSetIntItem(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("CultureCode: {0}", res.CultureCode);
    Console.WriteLine("ResourceName: {0}", res.ResourceName);
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
    Dim req as new UpdateResourceSetIntItemRequest()

    'Send Request to Server and Get Response
    Dim res As UpdateResourceSetIntItemResponse = api.UpdateResourceSetIntItem(req)

    'Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID)
    Console.WriteLine("CultureCode: {0}", res.CultureCode)
    Console.WriteLine("ResourceName: {0}", res.ResourceName)
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
    $res = $api.UpdateResourceSetIntItem($req);

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
    UpdateResourceSetIntItemRequest req = new UpdateResourceSetIntItemRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetIntItemResponse res = api.getExigoApiSoap().updateResourceSetIntItem(req, auth);

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

### UpdateResourceSetDecimalItem

> Updates a ResourceSet Decimal Item

| | |
|---|---|
| Category | Web Content |
| REST | `PATCH /3.0/resourceitem/decimal` |
| SOAP action | `https://api.exigo.com/UpdateResourceSetDecimalItem` |
| WSDL elements | `UpdateResourceSetDecimalItemRequest` → `UpdateResourceSetDecimalItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateResourceSetDecimalItem |

#### Input

**`UpdateResourceSetDecimalItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `NewDecimalValue` | `Decimal` | Optional. Fill to update, otherwise leave empty. |
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `CultureCode` | `String` | Optional. Defaults to Default CultureCode. |
| `NewResourceName` | `String` | Optional. Fill to update, otherwise leave empty. |
| `NewResourceGroupID` | `Int32` | Optional. Fill to update, otherwise leave empty. |
| `NewComment` | `String` | Optional. Fill to update, otherwise leave empty. |
| `NewEnabled` | `Boolean` | Optional. Fill to update, otherwise leave empty. |
| `NewEnabledStartDate` | `DateTime` | Optional. Fill to update, otherwise leave empty. Value must be provided in UTC. |
| `NewEnabledEndDate` | `DateTime` | Optional. Fill to update, otherwise leave empty. Value must be provided in UTC. |

#### Output

**`UpdateResourceSetDecimalItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `CultureCode` | `String` |  |
| `ResourceName` | `String` |  |

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/resourceitem/decimal HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "cultureCode": "",
  "resourceName": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/UpdateResourceSetDecimalItem"

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
    <UpdateResourceSetDecimalItemRequest xmlns="http://api.exigo.com/">
      <NewDecimalValue>decimal</NewDecimalValue>
    </UpdateResourceSetDecimalItemRequest>
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
    <UpdateResourceSetDecimalItemResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <CultureCode>string</CultureCode>
      <ResourceName>string</ResourceName>
    </UpdateResourceSetDecimalItemResult>
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
    var req = new UpdateResourceSetDecimalItemRequest();

    //Send Request to Server and Get Response
    var res = await api.UpdateResourceSetDecimalItemAsync(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("CultureCode: {0}", res.CultureCode);
    Console.WriteLine("ResourceName: {0}", res.ResourceName);
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
    UpdateResourceSetDecimalItemRequest req = new UpdateResourceSetDecimalItemRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetDecimalItemResponse res = api.UpdateResourceSetDecimalItem(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("CultureCode: {0}", res.CultureCode);
    Console.WriteLine("ResourceName: {0}", res.ResourceName);
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
    Dim req as new UpdateResourceSetDecimalItemRequest()

    'Send Request to Server and Get Response
    Dim res As UpdateResourceSetDecimalItemResponse = api.UpdateResourceSetDecimalItem(req)

    'Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID)
    Console.WriteLine("CultureCode: {0}", res.CultureCode)
    Console.WriteLine("ResourceName: {0}", res.ResourceName)
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
    $res = $api.UpdateResourceSetDecimalItem($req);

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
    UpdateResourceSetDecimalItemRequest req = new UpdateResourceSetDecimalItemRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetDecimalItemResponse res = api.getExigoApiSoap().updateResourceSetDecimalItem(req, auth);

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

### UpdateResourceSetTextItem

> Updates a ResourceSet Text Item

| | |
|---|---|
| Category | Web Content |
| REST | `PATCH /3.0/resourceitem/text` |
| SOAP action | `https://api.exigo.com/UpdateResourceSetTextItem` |
| WSDL elements | `UpdateResourceSetTextItemRequest` → `UpdateResourceSetTextItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateResourceSetTextItem |

#### Input

**`UpdateResourceSetTextItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `NewText` | `String` | Optional. Fill to update, otherwise leave empty. |
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `CultureCode` | `String` | Optional. Defaults to Default CultureCode. |
| `NewResourceName` | `String` | Optional. Fill to update, otherwise leave empty. |
| `NewResourceGroupID` | `Int32` | Optional. Fill to update, otherwise leave empty. |
| `NewComment` | `String` | Optional. Fill to update, otherwise leave empty. |
| `NewEnabled` | `Boolean` | Optional. Fill to update, otherwise leave empty. |
| `NewEnabledStartDate` | `DateTime` | Optional. Fill to update, otherwise leave empty. Value must be provided in UTC. |
| `NewEnabledEndDate` | `DateTime` | Optional. Fill to update, otherwise leave empty. Value must be provided in UTC. |

#### Output

**`UpdateResourceSetTextItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `CultureCode` | `String` |  |
| `ResourceName` | `String` |  |

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/resourceitem/text HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "cultureCode": "",
  "resourceName": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/UpdateResourceSetTextItem"

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
    <UpdateResourceSetTextItemRequest xmlns="http://api.exigo.com/">
      <NewText>string</NewText>
    </UpdateResourceSetTextItemRequest>
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
    <UpdateResourceSetTextItemResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <CultureCode>string</CultureCode>
      <ResourceName>string</ResourceName>
    </UpdateResourceSetTextItemResult>
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
    var req = new UpdateResourceSetTextItemRequest();

    //Send Request to Server and Get Response
    var res = await api.UpdateResourceSetTextItemAsync(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("CultureCode: {0}", res.CultureCode);
    Console.WriteLine("ResourceName: {0}", res.ResourceName);
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
    UpdateResourceSetTextItemRequest req = new UpdateResourceSetTextItemRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetTextItemResponse res = api.UpdateResourceSetTextItem(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("CultureCode: {0}", res.CultureCode);
    Console.WriteLine("ResourceName: {0}", res.ResourceName);
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
    Dim req as new UpdateResourceSetTextItemRequest()

    'Send Request to Server and Get Response
    Dim res As UpdateResourceSetTextItemResponse = api.UpdateResourceSetTextItem(req)

    'Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID)
    Console.WriteLine("CultureCode: {0}", res.CultureCode)
    Console.WriteLine("ResourceName: {0}", res.ResourceName)
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
    $res = $api.UpdateResourceSetTextItem($req);

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
    UpdateResourceSetTextItemRequest req = new UpdateResourceSetTextItemRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetTextItemResponse res = api.getExigoApiSoap().updateResourceSetTextItem(req, auth);

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

### UpdateResourceSetBooleanItem

> Updates a ResourceSet Boolean Item

| | |
|---|---|
| Category | Web Content |
| REST | `PATCH /3.0/resourceitem/bool` |
| SOAP action | `https://api.exigo.com/UpdateResourceSetBooleanItem` |
| WSDL elements | `UpdateResourceSetBooleanItemRequest` → `UpdateResourceSetBooleanItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateResourceSetBooleanItem |

#### Input

**`UpdateResourceSetBooleanItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `NewBooleanValue` | `Boolean` | Optional. Fill to update, otherwise leave empty. |
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `CultureCode` | `String` | Optional. Defaults to Default CultureCode. |
| `NewResourceName` | `String` | Optional. Fill to update, otherwise leave empty. |
| `NewResourceGroupID` | `Int32` | Optional. Fill to update, otherwise leave empty. |
| `NewComment` | `String` | Optional. Fill to update, otherwise leave empty. |
| `NewEnabled` | `Boolean` | Optional. Fill to update, otherwise leave empty. |
| `NewEnabledStartDate` | `DateTime` | Optional. Fill to update, otherwise leave empty. Value must be provided in UTC. |
| `NewEnabledEndDate` | `DateTime` | Optional. Fill to update, otherwise leave empty. Value must be provided in UTC. |

#### Output

**`UpdateResourceSetBooleanItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `CultureCode` | `String` |  |
| `ResourceName` | `String` |  |

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/resourceitem/bool HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "cultureCode": "",
  "resourceName": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/UpdateResourceSetBooleanItem"

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
    <UpdateResourceSetBooleanItemRequest xmlns="http://api.exigo.com/">
      <NewBooleanValue>boolean</NewBooleanValue>
    </UpdateResourceSetBooleanItemRequest>
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
    <UpdateResourceSetBooleanItemResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <CultureCode>string</CultureCode>
      <ResourceName>string</ResourceName>
    </UpdateResourceSetBooleanItemResult>
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
    var req = new UpdateResourceSetBooleanItemRequest();

    //Send Request to Server and Get Response
    var res = await api.UpdateResourceSetBooleanItemAsync(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("CultureCode: {0}", res.CultureCode);
    Console.WriteLine("ResourceName: {0}", res.ResourceName);
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
    UpdateResourceSetBooleanItemRequest req = new UpdateResourceSetBooleanItemRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetBooleanItemResponse res = api.UpdateResourceSetBooleanItem(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("CultureCode: {0}", res.CultureCode);
    Console.WriteLine("ResourceName: {0}", res.ResourceName);
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
    Dim req as new UpdateResourceSetBooleanItemRequest()

    'Send Request to Server and Get Response
    Dim res As UpdateResourceSetBooleanItemResponse = api.UpdateResourceSetBooleanItem(req)

    'Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID)
    Console.WriteLine("CultureCode: {0}", res.CultureCode)
    Console.WriteLine("ResourceName: {0}", res.ResourceName)
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
    $res = $api.UpdateResourceSetBooleanItem($req);

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
    UpdateResourceSetBooleanItemRequest req = new UpdateResourceSetBooleanItemRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetBooleanItemResponse res = api.getExigoApiSoap().updateResourceSetBooleanItem(req, auth);

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

### UpdateResourceSetDateItem

> Updates a ResourceSet Date Item

| | |
|---|---|
| Category | Web Content |
| REST | `PATCH /3.0/resourceitem/date` |
| SOAP action | `https://api.exigo.com/UpdateResourceSetDateItem` |
| WSDL elements | `UpdateResourceSetDateItemRequest` → `UpdateResourceSetDateItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateResourceSetDateItem |

#### Input

**`UpdateResourceSetDateItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `NewDate` | `DateTime` | Optional. Fill to update, otherwise leave empty. |
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `CultureCode` | `String` | Optional. Defaults to Default CultureCode. |
| `NewResourceName` | `String` | Optional. Fill to update, otherwise leave empty. |
| `NewResourceGroupID` | `Int32` | Optional. Fill to update, otherwise leave empty. |
| `NewComment` | `String` | Optional. Fill to update, otherwise leave empty. |
| `NewEnabled` | `Boolean` | Optional. Fill to update, otherwise leave empty. |
| `NewEnabledStartDate` | `DateTime` | Optional. Fill to update, otherwise leave empty. Value must be provided in UTC. |
| `NewEnabledEndDate` | `DateTime` | Optional. Fill to update, otherwise leave empty. Value must be provided in UTC. |

#### Output

**`UpdateResourceSetDateItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `CultureCode` | `String` |  |
| `ResourceName` | `String` |  |

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/resourceitem/date HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "cultureCode": "",
  "resourceName": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/UpdateResourceSetDateItem"

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
    <UpdateResourceSetDateItemRequest xmlns="http://api.exigo.com/">
      <NewDate>dateTime</NewDate>
    </UpdateResourceSetDateItemRequest>
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
    <UpdateResourceSetDateItemResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <CultureCode>string</CultureCode>
      <ResourceName>string</ResourceName>
    </UpdateResourceSetDateItemResult>
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
    var req = new UpdateResourceSetDateItemRequest();

    //Send Request to Server and Get Response
    var res = await api.UpdateResourceSetDateItemAsync(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("CultureCode: {0}", res.CultureCode);
    Console.WriteLine("ResourceName: {0}", res.ResourceName);
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
    UpdateResourceSetDateItemRequest req = new UpdateResourceSetDateItemRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetDateItemResponse res = api.UpdateResourceSetDateItem(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("CultureCode: {0}", res.CultureCode);
    Console.WriteLine("ResourceName: {0}", res.ResourceName);
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
    Dim req as new UpdateResourceSetDateItemRequest()

    'Send Request to Server and Get Response
    Dim res As UpdateResourceSetDateItemResponse = api.UpdateResourceSetDateItem(req)

    'Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID)
    Console.WriteLine("CultureCode: {0}", res.CultureCode)
    Console.WriteLine("ResourceName: {0}", res.ResourceName)
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
    $res = $api.UpdateResourceSetDateItem($req);

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
    UpdateResourceSetDateItemRequest req = new UpdateResourceSetDateItemRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetDateItemResponse res = api.getExigoApiSoap().updateResourceSetDateItem(req, auth);

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

### UpdateResourceSetImageItem

> Updates a ResourceSet Image Item

| | |
|---|---|
| Category | Web Content |
| REST | `PATCH /3.0/resourceitem/image` |
| SOAP action | `https://api.exigo.com/UpdateResourceSetImageItem` |
| WSDL elements | `UpdateResourceSetImageItemRequest` → `UpdateResourceSetImageItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateResourceSetImageItem |

#### Input

**`UpdateResourceSetImageItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `CultureCode` | `String` | Optional. Defaults to Default CultureCode. |
| `NewResourceName` | `String` | Optional. Fill to update, otherwise leave empty. |
| `NewResourceGroupID` | `Int32` | Optional. Fill to update, otherwise leave empty. |
| `NewComment` | `String` | Optional. Fill to update, otherwise leave empty. |
| `NewEnabled` | `Boolean` | Optional. Fill to update, otherwise leave empty. |
| `NewEnabledStartDate` | `DateTime` | Optional. Fill to update, otherwise leave empty. Value must be provided in UTC. |
| `NewEnabledEndDate` | `DateTime` | Optional. Fill to update, otherwise leave empty. Value must be provided in UTC. |

#### Output

**`UpdateResourceSetImageItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `CultureCode` | `String` |  |
| `ResourceName` | `String` |  |

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/resourceitem/image HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "cultureCode": "",
  "resourceName": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/UpdateResourceSetImageItem"

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
    <UpdateResourceSetImageItemRequest xmlns="http://api.exigo.com/" />
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
    <UpdateResourceSetImageItemResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <CultureCode>string</CultureCode>
      <ResourceName>string</ResourceName>
    </UpdateResourceSetImageItemResult>
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
    var req = new UpdateResourceSetImageItemRequest();

    //Send Request to Server and Get Response
    var res = await api.UpdateResourceSetImageItemAsync(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("CultureCode: {0}", res.CultureCode);
    Console.WriteLine("ResourceName: {0}", res.ResourceName);
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
    UpdateResourceSetImageItemRequest req = new UpdateResourceSetImageItemRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetImageItemResponse res = api.UpdateResourceSetImageItem(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("CultureCode: {0}", res.CultureCode);
    Console.WriteLine("ResourceName: {0}", res.ResourceName);
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
    Dim req as new UpdateResourceSetImageItemRequest()

    'Send Request to Server and Get Response
    Dim res As UpdateResourceSetImageItemResponse = api.UpdateResourceSetImageItem(req)

    'Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID)
    Console.WriteLine("CultureCode: {0}", res.CultureCode)
    Console.WriteLine("ResourceName: {0}", res.ResourceName)
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
    $res = $api.UpdateResourceSetImageItem($req);

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
    UpdateResourceSetImageItemRequest req = new UpdateResourceSetImageItemRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetImageItemResponse res = api.getExigoApiSoap().updateResourceSetImageItem(req, auth);

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

### UpdateResourceSetDataSetItem

> Updates a ResourceSet DataSet Item

| | |
|---|---|
| Category | Web Content |
| REST | `PATCH /3.0/resourceitem/dataset` |
| SOAP action | `https://api.exigo.com/UpdateResourceSetDataSetItem` |
| WSDL elements | `UpdateResourceSetDataSetItemRequest` → `UpdateResourceSetDataSetItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateResourceSetDataSetItem |

#### Input

**`UpdateResourceSetDataSetItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `NewDataSetType` | `String` | Optional. Fill to update, otherwise leave empty. |
| `NewDataSetValues` | `String[]` | Optional. Fill to update, otherwise leave empty. |
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `CultureCode` | `String` | Optional. Defaults to Default CultureCode. |
| `NewResourceName` | `String` | Optional. Fill to update, otherwise leave empty. |
| `NewResourceGroupID` | `Int32` | Optional. Fill to update, otherwise leave empty. |
| `NewComment` | `String` | Optional. Fill to update, otherwise leave empty. |
| `NewEnabled` | `Boolean` | Optional. Fill to update, otherwise leave empty. |
| `NewEnabledStartDate` | `DateTime` | Optional. Fill to update, otherwise leave empty. Value must be provided in UTC. |
| `NewEnabledEndDate` | `DateTime` | Optional. Fill to update, otherwise leave empty. Value must be provided in UTC. |

#### Output

**`UpdateResourceSetDataSetItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `CultureCode` | `String` |  |
| `ResourceName` | `String` |  |

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/resourceitem/dataset HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "cultureCode": "",
  "resourceName": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/UpdateResourceSetDataSetItem"

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
    <UpdateResourceSetDataSetItemRequest xmlns="http://api.exigo.com/">
      <NewDataSetType>string</NewDataSetType>
      <NewDataSetValues>
        <string>string</string>
      </NewDataSetValues>
    </UpdateResourceSetDataSetItemRequest>
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
    <UpdateResourceSetDataSetItemResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <CultureCode>string</CultureCode>
      <ResourceName>string</ResourceName>
    </UpdateResourceSetDataSetItemResult>
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
    var req = new UpdateResourceSetDataSetItemRequest();

    //Send Request to Server and Get Response
    var res = await api.UpdateResourceSetDataSetItemAsync(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("CultureCode: {0}", res.CultureCode);
    Console.WriteLine("ResourceName: {0}", res.ResourceName);
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
    UpdateResourceSetDataSetItemRequest req = new UpdateResourceSetDataSetItemRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetDataSetItemResponse res = api.UpdateResourceSetDataSetItem(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("CultureCode: {0}", res.CultureCode);
    Console.WriteLine("ResourceName: {0}", res.ResourceName);
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
    Dim req as new UpdateResourceSetDataSetItemRequest()

    'Send Request to Server and Get Response
    Dim res As UpdateResourceSetDataSetItemResponse = api.UpdateResourceSetDataSetItem(req)

    'Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID)
    Console.WriteLine("CultureCode: {0}", res.CultureCode)
    Console.WriteLine("ResourceName: {0}", res.ResourceName)
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
    $res = $api.UpdateResourceSetDataSetItem($req);

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
    UpdateResourceSetDataSetItemRequest req = new UpdateResourceSetDataSetItemRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetDataSetItemResponse res = api.getExigoApiSoap().updateResourceSetDataSetItem(req, auth);

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

### UpdateResourceSetBannerItem

> Updates a ResourceSet Banner Item

| | |
|---|---|
| Category | Web Content |
| REST | `PATCH /3.0/resourceitem/banner` |
| SOAP action | `https://api.exigo.com/UpdateResourceSetBannerItem` |
| WSDL elements | `UpdateResourceSetBannerItemRequest` → `UpdateResourceSetBannerItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateResourceSetBannerItem |

#### Input

**`UpdateResourceSetBannerItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `NewTitle` | `String` | Optional. The main header message for your banner. |
| `NewDescription` | `String` | Optional. The sub-header message for your banner. |
| `NewBannerImageBase64` | `String` | Optional. The Base64 representation of the image for your banner. |
| `NewBannerHoverText` | `String` | Optional. ResourceBanner field. |
| `NewBannerURL` | `String` | Optional. The URL the user is navigated to when clicking the banner. |
| `NewBannerClickEvent` | `BannerClickEvent` | Optional. How the url attached to the banner is navigated to when the banner is clicked.<br>**Values:** `OpenInNewTab`, `OpenInCurrentWindow`, `None` |
| `NewBannerType` | `BannerType` | Optional. BannerTypes dictate the formatting for a banner.<br>**Values:** `TextOnImage`, `ImageTop`, `InvalidType` |
| `NewAssociatedDataSets` | `String[]` | Optional. List of the DataSets by ResourceName associated with this banner. |
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `CultureCode` | `String` | Optional. Defaults to Default CultureCode. |
| `NewResourceName` | `String` | Optional. Fill to update, otherwise leave empty. |
| `NewResourceGroupID` | `Int32` | Optional. Fill to update, otherwise leave empty. |
| `NewComment` | `String` | Optional. Fill to update, otherwise leave empty. |
| `NewEnabled` | `Boolean` | Optional. Fill to update, otherwise leave empty. |
| `NewEnabledStartDate` | `DateTime` | Optional. Fill to update, otherwise leave empty. Value must be provided in UTC. |
| `NewEnabledEndDate` | `DateTime` | Optional. Fill to update, otherwise leave empty. Value must be provided in UTC. |

#### Output

**`UpdateResourceSetBannerItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `CultureCode` | `String` |  |
| `ResourceName` | `String` |  |

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/resourceitem/banner HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "cultureCode": "",
  "resourceName": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/UpdateResourceSetBannerItem"

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
    <UpdateResourceSetBannerItemRequest xmlns="http://api.exigo.com/">
      <NewTitle>string</NewTitle>
      <NewDescription>string</NewDescription>
      <NewBannerImageBase64>string</NewBannerImageBase64>
      <NewBannerHoverText>string</NewBannerHoverText>
      <NewBannerURL>string</NewBannerURL>
      <NewBannerClickEvent>OpenInNewTab or OpenInCurrentWindow or None</NewBannerClickEvent>
      <NewBannerType>TextOnImage or ImageTop or InvalidType</NewBannerType>
      <NewAssociatedDataSets>
        <string>string</string>
      </NewAssociatedDataSets>
    </UpdateResourceSetBannerItemRequest>
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
    <UpdateResourceSetBannerItemResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <CultureCode>string</CultureCode>
      <ResourceName>string</ResourceName>
    </UpdateResourceSetBannerItemResult>
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
    var req = new UpdateResourceSetBannerItemRequest();

    //Send Request to Server and Get Response
    var res = await api.UpdateResourceSetBannerItemAsync(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("CultureCode: {0}", res.CultureCode);
    Console.WriteLine("ResourceName: {0}", res.ResourceName);
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
    UpdateResourceSetBannerItemRequest req = new UpdateResourceSetBannerItemRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetBannerItemResponse res = api.UpdateResourceSetBannerItem(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("CultureCode: {0}", res.CultureCode);
    Console.WriteLine("ResourceName: {0}", res.ResourceName);
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
    Dim req as new UpdateResourceSetBannerItemRequest()

    'Send Request to Server and Get Response
    Dim res As UpdateResourceSetBannerItemResponse = api.UpdateResourceSetBannerItem(req)

    'Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID)
    Console.WriteLine("CultureCode: {0}", res.CultureCode)
    Console.WriteLine("ResourceName: {0}", res.ResourceName)
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
    $res = $api.UpdateResourceSetBannerItem($req);

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
    UpdateResourceSetBannerItemRequest req = new UpdateResourceSetBannerItemRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetBannerItemResponse res = api.getExigoApiSoap().updateResourceSetBannerItem(req, auth);

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

### UpdateResourceSetCarouselItem

> Updates a ResourceSet Carousel Item

| | |
|---|---|
| Category | Web Content |
| REST | `PATCH /3.0/resourceitem/carousel` |
| SOAP action | `https://api.exigo.com/UpdateResourceSetCarouselItem` |
| WSDL elements | `UpdateResourceSetCarouselItemRequest` → `UpdateResourceSetCarouselItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateResourceSetCarouselItem |

#### Input

**`UpdateResourceSetCarouselItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `NewCarouselSlides` | `String[]` | Optional. List of the banners by ResourceName associated with this carousel. |
| `NewCarouselType` | `CarouselType` | Optional. Dictates what bootstrap version to display the carousel as.<br>**Values:** `Bootstrap3`, `Bootstrap4`, `Bootstrap5` |
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `CultureCode` | `String` | Optional. Defaults to Default CultureCode. |
| `NewResourceName` | `String` | Optional. Fill to update, otherwise leave empty. |
| `NewResourceGroupID` | `Int32` | Optional. Fill to update, otherwise leave empty. |
| `NewComment` | `String` | Optional. Fill to update, otherwise leave empty. |
| `NewEnabled` | `Boolean` | Optional. Fill to update, otherwise leave empty. |
| `NewEnabledStartDate` | `DateTime` | Optional. Fill to update, otherwise leave empty. Value must be provided in UTC. |
| `NewEnabledEndDate` | `DateTime` | Optional. Fill to update, otherwise leave empty. Value must be provided in UTC. |

#### Output

**`UpdateResourceSetCarouselItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `CultureCode` | `String` |  |
| `ResourceName` | `String` |  |

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/resourceitem/carousel HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "cultureCode": "",
  "resourceName": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/UpdateResourceSetCarouselItem"

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
    <UpdateResourceSetCarouselItemRequest xmlns="http://api.exigo.com/">
      <NewCarouselSlides>
        <string>string</string>
      </NewCarouselSlides>
      <NewCarouselType>Bootstrap3 or Bootstrap4 or Bootstrap5</NewCarouselType>
    </UpdateResourceSetCarouselItemRequest>
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
    <UpdateResourceSetCarouselItemResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <CultureCode>string</CultureCode>
      <ResourceName>string</ResourceName>
    </UpdateResourceSetCarouselItemResult>
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
    var req = new UpdateResourceSetCarouselItemRequest();

    //Send Request to Server and Get Response
    var res = await api.UpdateResourceSetCarouselItemAsync(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("CultureCode: {0}", res.CultureCode);
    Console.WriteLine("ResourceName: {0}", res.ResourceName);
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
    UpdateResourceSetCarouselItemRequest req = new UpdateResourceSetCarouselItemRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetCarouselItemResponse res = api.UpdateResourceSetCarouselItem(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("CultureCode: {0}", res.CultureCode);
    Console.WriteLine("ResourceName: {0}", res.ResourceName);
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
    Dim req as new UpdateResourceSetCarouselItemRequest()

    'Send Request to Server and Get Response
    Dim res As UpdateResourceSetCarouselItemResponse = api.UpdateResourceSetCarouselItem(req)

    'Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID)
    Console.WriteLine("CultureCode: {0}", res.CultureCode)
    Console.WriteLine("ResourceName: {0}", res.ResourceName)
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
    $res = $api.UpdateResourceSetCarouselItem($req);

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
    UpdateResourceSetCarouselItemRequest req = new UpdateResourceSetCarouselItemRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetCarouselItemResponse res = api.getExigoApiSoap().updateResourceSetCarouselItem(req, auth);

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

### UpdateResourceSetWidgetItem

> Updates a ResourceSet Widget Item

| | |
|---|---|
| Category | Web Content |
| REST | `PATCH /3.0/resourceitem/widget` |
| SOAP action | `https://api.exigo.com/UpdateResourceSetWidgetItem` |
| WSDL elements | `UpdateResourceSetWidgetItemRequest` → `UpdateResourceSetWidgetItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateResourceSetWidgetItem |

#### Input

**`UpdateResourceSetWidgetItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `NewHtml` | `String` | Optional. Fill to update, otherwise leave empty. |
| `NewJavascript` | `String` | Optional. Fill to update, otherwise leave empty. |
| `NewCss` | `String` | Optional. Fill to update, otherwise leave empty. |
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `CultureCode` | `String` | Optional. Defaults to Default CultureCode. |
| `NewResourceName` | `String` | Optional. Fill to update, otherwise leave empty. |
| `NewResourceGroupID` | `Int32` | Optional. Fill to update, otherwise leave empty. |
| `NewComment` | `String` | Optional. Fill to update, otherwise leave empty. |
| `NewEnabled` | `Boolean` | Optional. Fill to update, otherwise leave empty. |
| `NewEnabledStartDate` | `DateTime` | Optional. Fill to update, otherwise leave empty. Value must be provided in UTC. |
| `NewEnabledEndDate` | `DateTime` | Optional. Fill to update, otherwise leave empty. Value must be provided in UTC. |

#### Output

**`UpdateResourceSetWidgetItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `CultureCode` | `String` |  |
| `ResourceName` | `String` |  |

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/resourceitem/widget HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "cultureCode": "",
  "resourceName": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/UpdateResourceSetWidgetItem"

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
    <UpdateResourceSetWidgetItemRequest xmlns="http://api.exigo.com/">
      <NewHtml>string</NewHtml>
      <NewJavascript>string</NewJavascript>
      <NewCss>string</NewCss>
    </UpdateResourceSetWidgetItemRequest>
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
    <UpdateResourceSetWidgetItemResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <CultureCode>string</CultureCode>
      <ResourceName>string</ResourceName>
    </UpdateResourceSetWidgetItemResult>
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
    var req = new UpdateResourceSetWidgetItemRequest();

    //Send Request to Server and Get Response
    var res = await api.UpdateResourceSetWidgetItemAsync(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("CultureCode: {0}", res.CultureCode);
    Console.WriteLine("ResourceName: {0}", res.ResourceName);
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
    UpdateResourceSetWidgetItemRequest req = new UpdateResourceSetWidgetItemRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetWidgetItemResponse res = api.UpdateResourceSetWidgetItem(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("CultureCode: {0}", res.CultureCode);
    Console.WriteLine("ResourceName: {0}", res.ResourceName);
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
    Dim req as new UpdateResourceSetWidgetItemRequest()

    'Send Request to Server and Get Response
    Dim res As UpdateResourceSetWidgetItemResponse = api.UpdateResourceSetWidgetItem(req)

    'Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID)
    Console.WriteLine("CultureCode: {0}", res.CultureCode)
    Console.WriteLine("ResourceName: {0}", res.ResourceName)
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
    $res = $api.UpdateResourceSetWidgetItem($req);

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
    UpdateResourceSetWidgetItemRequest req = new UpdateResourceSetWidgetItemRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetWidgetItemResponse res = api.getExigoApiSoap().updateResourceSetWidgetItem(req, auth);

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

### UpdateResourceSetDropDownItem

> Updates a ResourceSet DropDown Item

| | |
|---|---|
| Category | Web Content |
| REST | `PATCH /3.0/resourceitem/dropdown` |
| SOAP action | `https://api.exigo.com/UpdateResourceSetDropDownItem` |
| WSDL elements | `UpdateResourceSetDropDownItemRequest` → `UpdateResourceSetDropDownItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateResourceSetDropDownItem |

#### Input

**`UpdateResourceSetDropDownItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `NewDropDownValues` | `String` | Optional. Comma separated DropDown values. |
| `NewDefaultSelectedValue` | `String` | Must be one of the DropDownValues. |
| `ResourceSetID` | `Int32` |  |
| `ResourceName` | `String` |  |
| `CultureCode` | `String` | Optional. Defaults to Default CultureCode. |
| `NewResourceName` | `String` | Optional. Fill to update, otherwise leave empty. |
| `NewResourceGroupID` | `Int32` | Optional. Fill to update, otherwise leave empty. |
| `NewComment` | `String` | Optional. Fill to update, otherwise leave empty. |
| `NewEnabled` | `Boolean` | Optional. Fill to update, otherwise leave empty. |
| `NewEnabledStartDate` | `DateTime` | Optional. Fill to update, otherwise leave empty. Value must be provided in UTC. |
| `NewEnabledEndDate` | `DateTime` | Optional. Fill to update, otherwise leave empty. Value must be provided in UTC. |

#### Output

**`UpdateResourceSetDropDownItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `CultureCode` | `String` |  |
| `ResourceName` | `String` |  |

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/resourceitem/dropdown HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "cultureCode": "",
  "resourceName": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/UpdateResourceSetDropDownItem"

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
    <UpdateResourceSetDropDownItemRequest xmlns="http://api.exigo.com/">
      <NewDropDownValues>string</NewDropDownValues>
      <NewDefaultSelectedValue>string</NewDefaultSelectedValue>
    </UpdateResourceSetDropDownItemRequest>
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
    <UpdateResourceSetDropDownItemResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <CultureCode>string</CultureCode>
      <ResourceName>string</ResourceName>
    </UpdateResourceSetDropDownItemResult>
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
    var req = new UpdateResourceSetDropDownItemRequest();

    //Send Request to Server and Get Response
    var res = await api.UpdateResourceSetDropDownItemAsync(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("CultureCode: {0}", res.CultureCode);
    Console.WriteLine("ResourceName: {0}", res.ResourceName);
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
    UpdateResourceSetDropDownItemRequest req = new UpdateResourceSetDropDownItemRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetDropDownItemResponse res = api.UpdateResourceSetDropDownItem(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("CultureCode: {0}", res.CultureCode);
    Console.WriteLine("ResourceName: {0}", res.ResourceName);
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
    Dim req as new UpdateResourceSetDropDownItemRequest()

    'Send Request to Server and Get Response
    Dim res As UpdateResourceSetDropDownItemResponse = api.UpdateResourceSetDropDownItem(req)

    'Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID)
    Console.WriteLine("CultureCode: {0}", res.CultureCode)
    Console.WriteLine("ResourceName: {0}", res.ResourceName)
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
    $res = $api.UpdateResourceSetDropDownItem($req);

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
    UpdateResourceSetDropDownItemRequest req = new UpdateResourceSetDropDownItemRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetDropDownItemResponse res = api.getExigoApiSoap().updateResourceSetDropDownItem(req, auth);

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

### CreateResourceSetCulture

> Adds a culture to a Resource Set

| | |
|---|---|
| Category | Web Content |
| REST | `POST /3.0/resourceset/culture` |
| SOAP action | `https://api.exigo.com/CreateResourceSetCulture` |
| WSDL elements | `CreateResourceSetCultureRequest` → `CreateResourceSetCultureResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateResourceSetCulture |

#### Input

**`CreateResourceSetCultureRequest`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` | The unique numerical ID of the resource to add a culture to. |
| `CultureCode` | `String` | Must be an existing culture within System.Globalization.CultureInfo. |

#### Output

**`CreateResourceSetCultureResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `CultureCode` | `String` |  |
| `Description` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/resourceset/culture HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "cultureCode": "",
  "description": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateResourceSetCulture"

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
    <CreateResourceSetCultureRequest xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <CultureCode>string</CultureCode>
    </CreateResourceSetCultureRequest>
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
    <CreateResourceSetCultureResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <CultureCode>string</CultureCode>
      <Description>string</Description>
    </CreateResourceSetCultureResult>
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
    var req = new CreateResourceSetCultureRequest();

    //Send Request to Server and Get Response
    var res = await api.CreateResourceSetCultureAsync(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("CultureCode: {0}", res.CultureCode);
    Console.WriteLine("Description: {0}", res.Description);
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
    CreateResourceSetCultureRequest req = new CreateResourceSetCultureRequest();

    //Send Request to Server and Get Response
    CreateResourceSetCultureResponse res = api.CreateResourceSetCulture(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("CultureCode: {0}", res.CultureCode);
    Console.WriteLine("Description: {0}", res.Description);
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
    Dim req as new CreateResourceSetCultureRequest()

    'Send Request to Server and Get Response
    Dim res As CreateResourceSetCultureResponse = api.CreateResourceSetCulture(req)

    'Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID)
    Console.WriteLine("CultureCode: {0}", res.CultureCode)
    Console.WriteLine("Description: {0}", res.Description)
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
    $res = $api.CreateResourceSetCulture($req);

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
    CreateResourceSetCultureRequest req = new CreateResourceSetCultureRequest();

    //Send Request to Server and Get Response
    CreateResourceSetCultureResponse res = api.getExigoApiSoap().createResourceSetCulture(req, auth);

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

### DeleteResourceSetCulture

> Removes a cultue from a Resource Set

| | |
|---|---|
| Category | Web Content |
| REST | `DELETE /3.0/resourceset/culture` |
| SOAP action | `https://api.exigo.com/DeleteResourceSetCulture` |
| WSDL elements | `DeleteResourceSetCultureRequest` → `DeleteResourceSetCultureResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DeleteResourceSetCulture |

#### Input

**`DeleteResourceSetCultureRequest`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` | The unique numerical ID of the resource to add a culture to. |
| `CultureCode` | `String` | Must be an existing culture within System.Globalization.CultureInfo. |

#### Output

**`DeleteResourceSetCultureResponse`**

_No properties._

#### REST example

```http
DELETE https://yourcompany-api.exigo.com/3.0/resourceset/culture HTTP/1.1
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
SOAPAction: "https://api.exigo.com/DeleteResourceSetCulture"

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
    <DeleteResourceSetCultureRequest xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <CultureCode>string</CultureCode>
    </DeleteResourceSetCultureRequest>
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
    <DeleteResourceSetCultureResult xmlns="http://api.exigo.com/" />
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
    var req = new DeleteResourceSetCultureRequest();

    //Send Request to Server and Get Response
    var res = await api.DeleteResourceSetCultureAsync(req);

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
    DeleteResourceSetCultureRequest req = new DeleteResourceSetCultureRequest();

    //Send Request to Server and Get Response
    DeleteResourceSetCultureResponse res = api.DeleteResourceSetCulture(req);

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
    Dim req as new DeleteResourceSetCultureRequest()

    'Send Request to Server and Get Response
    Dim res As DeleteResourceSetCultureResponse = api.DeleteResourceSetCulture(req)

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
    $res = $api.DeleteResourceSetCulture($req);

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
    DeleteResourceSetCultureRequest req = new DeleteResourceSetCultureRequest();

    //Send Request to Server and Get Response
    DeleteResourceSetCultureResponse res = api.getExigoApiSoap().deleteResourceSetCulture(req, auth);

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

### GetResourceSetCultures

> Determines the cultures available in the resource set, environment, and version the client server is subscribed to.

| | |
|---|---|
| Category | Web Content |
| REST | `GET /3.0/resourceset/cultureAuthorization:` |
| SOAP action | `https://api.exigo.com/GetResourceSetCultures` |
| WSDL elements | `GetResourceSetCulturesRequest` → `GetResourceSetCulturesResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetResourceSetCultures |

#### Input

**`GetResourceSetCulturesRequest`**

| Property | Type | Notes |
|---|---|---|
| `SubscriptionKey` | `String` | Optional. Either pass in SubscriptionKey with optional Version, or ResourceSetID. |
| `Version` | `String` | Optional. Version is only used if SubscriptionKey is filled. If Version is null, the items in the most recent changes are returned. |
| `ResourceSetID` | `Int32` | Optional. Either pass in only ResourceSetID, or SubscriptionKey and optional Version. |

#### Output

**`GetResourceSetCulturesResponse`**

| Property | Type | Notes |
|---|---|---|
| `Cultures` | `ResourceSetCulture[]` |  |

**`ResourceSetCulture`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `ResourceSetID` | `Int32` |  |
| &nbsp;&nbsp;↳ `CultureCode` | `String` |  |
| &nbsp;&nbsp;↳ `Description` | `String` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/resourceset/cultureAuthorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "cultures": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetResourceSetCultures"

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
    <GetResourceSetCulturesRequest xmlns="http://api.exigo.com/">
      <SubscriptionKey>string</SubscriptionKey>
      <Version>string</Version>
      <ResourceSetID>int</ResourceSetID>
    </GetResourceSetCulturesRequest>
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
    <GetResourceSetCulturesResult xmlns="http://api.exigo.com/">
      <Cultures>
        <ResourceSetCulture>
          <ResourceSetID>int</ResourceSetID>
          <CultureCode>string</CultureCode>
          <Description>string</Description>
        </ResourceSetCulture>
      </Cultures>
    </GetResourceSetCulturesResult>
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
    var req = new GetResourceSetCulturesRequest();

    //Send Request to Server and Get Response
    var res = await api.GetResourceSetCulturesAsync(req);

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
    GetResourceSetCulturesRequest req = new GetResourceSetCulturesRequest();

    //Send Request to Server and Get Response
    GetResourceSetCulturesResponse res = api.GetResourceSetCultures(req);

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
    Dim req as new GetResourceSetCulturesRequest()

    'Send Request to Server and Get Response
    Dim res As GetResourceSetCulturesResponse = api.GetResourceSetCultures(req)

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
    $res = $api.GetResourceSetCultures($req);

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
    GetResourceSetCulturesRequest req = new GetResourceSetCulturesRequest();

    //Send Request to Server and Get Response
    GetResourceSetCulturesResponse res = api.getExigoApiSoap().getResourceSetCultures(req, auth);

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

### CreateResourceSetEnvironment

> Creates a ResourceSet Environment

| | |
|---|---|
| Category | Web Content |
| REST | `POST /3.0/resourceset/environment` |
| SOAP action | `https://api.exigo.com/CreateResourceSetEnvironment` |
| WSDL elements | `CreateResourceSetEnvironmentRequest` → `CreateResourceSetEnvironmentResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateResourceSetEnvironment |

#### Input

**`CreateResourceSetEnvironmentRequest`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `EnvironmentCode` | `String` |  |
| `Description` | `String` |  |
| `Version` | `String` | Optional. If provided, must be the version of an existing release. |
| `ScheduledVersion` | `String` | Optional. If provided, must be the version of an existing release. |
| `ScheduledVersionDate` | `DateTime` | Optional. |

#### Output

**`CreateResourceSetEnvironmentResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `EnvironmentCode` | `String` |  |
| `Description` | `String` |  |
| `Version` | `String` |  |
| `ScheduledVersion` | `String` |  |
| `ScheduledVersionDate` | `DateTime` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/resourceset/environment HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "environmentCode": "",
  "description": "",
  "version": "",
  "scheduledVersion": "",
  "scheduledVersionDate": "2026-11-10T00:00:00-06:00",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateResourceSetEnvironment"

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
    <CreateResourceSetEnvironmentRequest xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <EnvironmentCode>string</EnvironmentCode>
      <Description>string</Description>
      <Version>string</Version>
      <ScheduledVersion>string</ScheduledVersion>
      <ScheduledVersionDate>dateTime</ScheduledVersionDate>
    </CreateResourceSetEnvironmentRequest>
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
    <CreateResourceSetEnvironmentResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <EnvironmentCode>string</EnvironmentCode>
      <Description>string</Description>
      <Version>string</Version>
      <ScheduledVersion>string</ScheduledVersion>
      <ScheduledVersionDate>dateTime</ScheduledVersionDate>
    </CreateResourceSetEnvironmentResult>
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
    var req = new CreateResourceSetEnvironmentRequest();

    //Send Request to Server and Get Response
    var res = await api.CreateResourceSetEnvironmentAsync(req);

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
    CreateResourceSetEnvironmentRequest req = new CreateResourceSetEnvironmentRequest();

    //Send Request to Server and Get Response
    CreateResourceSetEnvironmentResponse res = api.CreateResourceSetEnvironment(req);

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
    Dim req as new CreateResourceSetEnvironmentRequest()

    'Send Request to Server and Get Response
    Dim res As CreateResourceSetEnvironmentResponse = api.CreateResourceSetEnvironment(req)

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
    $res = $api.CreateResourceSetEnvironment($req);

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
    CreateResourceSetEnvironmentRequest req = new CreateResourceSetEnvironmentRequest();

    //Send Request to Server and Get Response
    CreateResourceSetEnvironmentResponse res = api.getExigoApiSoap().createResourceSetEnvironment(req, auth);

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

### DeleteResourceSetEnvironment

> Deletes a ResourceSet Environment

| | |
|---|---|
| Category | Web Content |
| REST | `DELETE /3.0/resourceset/environment` |
| SOAP action | `https://api.exigo.com/DeleteResourceSetEnvironment` |
| WSDL elements | `DeleteResourceSetEnvironmentRequest` → `DeleteResourceSetEnvironmentResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DeleteResourceSetEnvironment |

#### Input

**`DeleteResourceSetEnvironmentRequest`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `EnvironmentCode` | `String` |  |

#### Output

**`DeleteResourceSetEnvironmentResponse`**

_No properties._

#### REST example

```http
DELETE https://yourcompany-api.exigo.com/3.0/resourceset/environment HTTP/1.1
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
SOAPAction: "https://api.exigo.com/DeleteResourceSetEnvironment"

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
    <DeleteResourceSetEnvironmentRequest xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <EnvironmentCode>string</EnvironmentCode>
    </DeleteResourceSetEnvironmentRequest>
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
    <DeleteResourceSetEnvironmentResult xmlns="http://api.exigo.com/" />
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
    var req = new DeleteResourceSetEnvironmentRequest();

    //Send Request to Server and Get Response
    var res = await api.DeleteResourceSetEnvironmentAsync(req);

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
    DeleteResourceSetEnvironmentRequest req = new DeleteResourceSetEnvironmentRequest();

    //Send Request to Server and Get Response
    DeleteResourceSetEnvironmentResponse res = api.DeleteResourceSetEnvironment(req);

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
    Dim req as new DeleteResourceSetEnvironmentRequest()

    'Send Request to Server and Get Response
    Dim res As DeleteResourceSetEnvironmentResponse = api.DeleteResourceSetEnvironment(req)

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
    $res = $api.DeleteResourceSetEnvironment($req);

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
    DeleteResourceSetEnvironmentRequest req = new DeleteResourceSetEnvironmentRequest();

    //Send Request to Server and Get Response
    DeleteResourceSetEnvironmentResponse res = api.getExigoApiSoap().deleteResourceSetEnvironment(req, auth);

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

### GetResourceSetEnvironments

> Gets ResourceSet Environments

| | |
|---|---|
| Category | Web Content |
| REST | `GET /3.0/resourceset/environmentAuthorization:` |
| SOAP action | `https://api.exigo.com/GetResourceSetEnvironments` |
| WSDL elements | `GetResourceSetEnvironmentsRequest` → `GetResourceSetEnvironmentsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetResourceSetEnvironments |

#### Input

**`GetResourceSetEnvironmentsRequest`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |

#### Output

**`GetResourceSetEnvironmentsResponse`**

| Property | Type | Notes |
|---|---|---|
| `Environments` | `ResourceSetEnvironment[]` |  |

**`ResourceSetEnvironment`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `ResourceSetID` | `Int32` |  |
| &nbsp;&nbsp;↳ `EnvironmentCode` | `String` |  |
| &nbsp;&nbsp;↳ `Description` | `String` |  |
| &nbsp;&nbsp;↳ `Version` | `String` |  |
| &nbsp;&nbsp;↳ `ScheduledVersion` | `String` |  |
| &nbsp;&nbsp;↳ `ScheduledVersionDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `ModifiedDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `ModifiedBy` | `String` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/resourceset/environmentAuthorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "environments": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetResourceSetEnvironments"

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
    <GetResourceSetEnvironmentsRequest xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
    </GetResourceSetEnvironmentsRequest>
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
    <GetResourceSetEnvironmentsResult xmlns="http://api.exigo.com/">
      <Environments>
        <ResourceSetEnvironment>
          <ResourceSetID>int</ResourceSetID>
          <EnvironmentCode>string</EnvironmentCode>
          <Description>string</Description>
          <Version>string</Version>
          <ScheduledVersion>string</ScheduledVersion>
          <ScheduledVersionDate>dateTime</ScheduledVersionDate>
          <ModifiedDate>dateTime</ModifiedDate>
          <ModifiedBy>string</ModifiedBy>
        </ResourceSetEnvironment>
      </Environments>
    </GetResourceSetEnvironmentsResult>
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
    var req = new GetResourceSetEnvironmentsRequest();

    //Send Request to Server and Get Response
    var res = await api.GetResourceSetEnvironmentsAsync(req);

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
    GetResourceSetEnvironmentsRequest req = new GetResourceSetEnvironmentsRequest();

    //Send Request to Server and Get Response
    GetResourceSetEnvironmentsResponse res = api.GetResourceSetEnvironments(req);

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
    Dim req as new GetResourceSetEnvironmentsRequest()

    'Send Request to Server and Get Response
    Dim res As GetResourceSetEnvironmentsResponse = api.GetResourceSetEnvironments(req)

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
    $res = $api.GetResourceSetEnvironments($req);

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
    GetResourceSetEnvironmentsRequest req = new GetResourceSetEnvironmentsRequest();

    //Send Request to Server and Get Response
    GetResourceSetEnvironmentsResponse res = api.getExigoApiSoap().getResourceSetEnvironments(req, auth);

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

### UpdateResourceSetEnvironment

> Updates a ResourceSet Environment

| | |
|---|---|
| Category | Web Content |
| REST | `PATCH /3.0/resourceset/environment` |
| SOAP action | `https://api.exigo.com/UpdateResourceSetEnvironment` |
| WSDL elements | `UpdateResourceSetEnvironmentRequest` → `UpdateResourceSetEnvironmentResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateResourceSetEnvironment |

#### Input

**`UpdateResourceSetEnvironmentRequest`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `EnvironmentCode` | `String` |  |
| `NewEnvironmentCode` | `String` |  |
| `NewDescription` | `String` |  |
| `NewVersion` | `String` | Optional. If provided, must be the version of an existing release. |
| `NewScheduledVersion` | `String` | Optional. If provided, must be the version of an existing release. |
| `NewScheduledVersionDate` | `DateTime` | Optional. |

#### Output

**`UpdateResourceSetEnvironmentResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `EnvironmentCode` | `String` |  |
| `Description` | `String` |  |
| `Version` | `String` |  |
| `ScheduledVersion` | `String` |  |
| `ScheduledVersionDate` | `DateTime` |  |

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/resourceset/environment HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "environmentCode": "",
  "description": "",
  "version": "",
  "scheduledVersion": "",
  "scheduledVersionDate": "2026-11-10T00:00:00-06:00",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/UpdateResourceSetEnvironment"

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
    <UpdateResourceSetEnvironmentRequest xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <EnvironmentCode>string</EnvironmentCode>
      <NewEnvironmentCode>string</NewEnvironmentCode>
      <NewDescription>string</NewDescription>
      <NewVersion>string</NewVersion>
      <NewScheduledVersion>string</NewScheduledVersion>
      <NewScheduledVersionDate>dateTime</NewScheduledVersionDate>
    </UpdateResourceSetEnvironmentRequest>
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
    <UpdateResourceSetEnvironmentResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <EnvironmentCode>string</EnvironmentCode>
      <Description>string</Description>
      <Version>string</Version>
      <ScheduledVersion>string</ScheduledVersion>
      <ScheduledVersionDate>dateTime</ScheduledVersionDate>
    </UpdateResourceSetEnvironmentResult>
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
    var req = new UpdateResourceSetEnvironmentRequest();

    //Send Request to Server and Get Response
    var res = await api.UpdateResourceSetEnvironmentAsync(req);

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
    UpdateResourceSetEnvironmentRequest req = new UpdateResourceSetEnvironmentRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetEnvironmentResponse res = api.UpdateResourceSetEnvironment(req);

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
    Dim req as new UpdateResourceSetEnvironmentRequest()

    'Send Request to Server and Get Response
    Dim res As UpdateResourceSetEnvironmentResponse = api.UpdateResourceSetEnvironment(req)

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
    $res = $api.UpdateResourceSetEnvironment($req);

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
    UpdateResourceSetEnvironmentRequest req = new UpdateResourceSetEnvironmentRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetEnvironmentResponse res = api.getExigoApiSoap().updateResourceSetEnvironment(req, auth);

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

### CreateResourceSetGroup

> Creates a ResourceSet Group

| | |
|---|---|
| Category | Web Content |
| REST | `POST /3.0/resourceset/group` |
| SOAP action | `https://api.exigo.com/CreateResourceSetGroup` |
| WSDL elements | `CreateResourceSetGroupRequest` → `CreateResourceSetGroupResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateResourceSetGroup |

#### Input

**`CreateResourceSetGroupRequest`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `Description` | `String` |  |

#### Output

**`CreateResourceSetGroupResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `ResourceGroupID` | `Int32` |  |
| `Decription` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/resourceset/group HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "resourceGroupID": 1,
  "decription": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateResourceSetGroup"

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
    <CreateResourceSetGroupRequest xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <Description>string</Description>
    </CreateResourceSetGroupRequest>
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
    <CreateResourceSetGroupResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <ResourceGroupID>int</ResourceGroupID>
      <Decription>string</Decription>
    </CreateResourceSetGroupResult>
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
    var req = new CreateResourceSetGroupRequest();

    //Send Request to Server and Get Response
    var res = await api.CreateResourceSetGroupAsync(req);

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
    CreateResourceSetGroupRequest req = new CreateResourceSetGroupRequest();

    //Send Request to Server and Get Response
    CreateResourceSetGroupResponse res = api.CreateResourceSetGroup(req);

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
    Dim req as new CreateResourceSetGroupRequest()

    'Send Request to Server and Get Response
    Dim res As CreateResourceSetGroupResponse = api.CreateResourceSetGroup(req)

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
    $res = $api.CreateResourceSetGroup($req);

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
    CreateResourceSetGroupRequest req = new CreateResourceSetGroupRequest();

    //Send Request to Server and Get Response
    CreateResourceSetGroupResponse res = api.getExigoApiSoap().createResourceSetGroup(req, auth);

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

### DeleteResourceSetGroup

> Deletes a ResourceSet Group

| | |
|---|---|
| Category | Web Content |
| REST | `DELETE /3.0/resourceset/group` |
| SOAP action | `https://api.exigo.com/DeleteResourceSetGroup` |
| WSDL elements | `DeleteResourceSetGroupRequest` → `DeleteResourceSetGroupResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DeleteResourceSetGroup |

#### Input

**`DeleteResourceSetGroupRequest`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `ResourceGroupID` | `Int32` |  |
| `DeleteResources` | `Boolean` | Warning, if DeleteResources is set to true all affiliated ResourceItems will be deleted. |

#### Output

**`DeleteResourceSetGroupResponse`**

_No properties._

#### REST example

```http
DELETE https://yourcompany-api.exigo.com/3.0/resourceset/group HTTP/1.1
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
SOAPAction: "https://api.exigo.com/DeleteResourceSetGroup"

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
    <DeleteResourceSetGroupRequest xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <ResourceGroupID>int</ResourceGroupID>
      <DeleteResources>boolean</DeleteResources>
    </DeleteResourceSetGroupRequest>
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
    <DeleteResourceSetGroupResult xmlns="http://api.exigo.com/" />
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
    var req = new DeleteResourceSetGroupRequest();

    //Send Request to Server and Get Response
    var res = await api.DeleteResourceSetGroupAsync(req);

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
    DeleteResourceSetGroupRequest req = new DeleteResourceSetGroupRequest();

    //Send Request to Server and Get Response
    DeleteResourceSetGroupResponse res = api.DeleteResourceSetGroup(req);

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
    Dim req as new DeleteResourceSetGroupRequest()

    'Send Request to Server and Get Response
    Dim res As DeleteResourceSetGroupResponse = api.DeleteResourceSetGroup(req)

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
    $res = $api.DeleteResourceSetGroup($req);

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
    DeleteResourceSetGroupRequest req = new DeleteResourceSetGroupRequest();

    //Send Request to Server and Get Response
    DeleteResourceSetGroupResponse res = api.getExigoApiSoap().deleteResourceSetGroup(req, auth);

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

### GetResourceSetGroups

> Gets ResourceSet Groups

| | |
|---|---|
| Category | Web Content |
| REST | `GET /3.0/resourceset/groupAuthorization:` |
| SOAP action | `https://api.exigo.com/GetResourceSetGroups` |
| WSDL elements | `GetResourceSetGroupsRequest` → `GetResourceSetGroupsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetResourceSetGroups |

#### Input

**`GetResourceSetGroupsRequest`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |

#### Output

**`GetResourceSetGroupsResponse`**

| Property | Type | Notes |
|---|---|---|
| `Groups` | `ResourceGroup[]` |  |

**`ResourceGroup`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `ResourceSetID` | `Int32` |  |
| &nbsp;&nbsp;↳ `ResourceGroupID` | `Int32` |  |
| &nbsp;&nbsp;↳ `Description` | `String` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/resourceset/groupAuthorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "groups": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetResourceSetGroups"

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
    <GetResourceSetGroupsRequest xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
    </GetResourceSetGroupsRequest>
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
    <GetResourceSetGroupsResult xmlns="http://api.exigo.com/">
      <Groups>
        <ResourceGroup>
          <ResourceSetID>int</ResourceSetID>
          <ResourceGroupID>int</ResourceGroupID>
          <Description>string</Description>
        </ResourceGroup>
      </Groups>
    </GetResourceSetGroupsResult>
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
    var req = new GetResourceSetGroupsRequest();

    //Send Request to Server and Get Response
    var res = await api.GetResourceSetGroupsAsync(req);

    //Now examine the results:

    foreach (var resourceGroup  in res.Groups)
    {
        Console.WriteLine("ResourceSetID: {0}", resourceGroup.ResourceSetID);
        Console.WriteLine("ResourceGroupID: {0}", resourceGroup.ResourceGroupID);
        Console.WriteLine("Description: {0}", resourceGroup.Description);
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
    GetResourceSetGroupsRequest req = new GetResourceSetGroupsRequest();

    //Send Request to Server and Get Response
    GetResourceSetGroupsResponse res = api.GetResourceSetGroups(req);

    //Now examine the results:

    foreach (ResourceGroup resourceGroup  in res.Groups)
    {
        Console.WriteLine("ResourceSetID: {0}", resourceGroup.ResourceSetID);
        Console.WriteLine("ResourceGroupID: {0}", resourceGroup.ResourceGroupID);
        Console.WriteLine("Description: {0}", resourceGroup.Description);
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
    Dim req as new GetResourceSetGroupsRequest()

    'Send Request to Server and Get Response
    Dim res As GetResourceSetGroupsResponse = api.GetResourceSetGroups(req)

    'Now examine the results:

    For Each resourceGroup As ResourceGroup In res.Groups
        Console.WriteLine("ResourceSetID: {0}", resourceGroup.ResourceSetID)
        Console.WriteLine("ResourceGroupID: {0}", resourceGroup.ResourceGroupID)
        Console.WriteLine("Description: {0}", resourceGroup.Description)
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
    $res = $api.GetResourceSetGroups($req);

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
    GetResourceSetGroupsRequest req = new GetResourceSetGroupsRequest();

    //Send Request to Server and Get Response
    GetResourceSetGroupsResponse res = api.getExigoApiSoap().getResourceSetGroups(req, auth);

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

### UpdateResourceSetGroup

> Updates a ResourceSet Group

| | |
|---|---|
| Category | Web Content |
| REST | `PATCH /3.0/resourceset/group` |
| SOAP action | `https://api.exigo.com/UpdateResourceSetGroup` |
| WSDL elements | `UpdateResourceSetGroupRequest` → `UpdateResourceSetGroupResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateResourceSetGroup |

#### Input

**`UpdateResourceSetGroupRequest`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `ResourceGroupID` | `Int32` |  |
| `NewDescription` | `String` |  |

#### Output

**`UpdateResourceSetGroupResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `ResourceGroupID` | `Int32` |  |
| `Decription` | `String` |  |

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/resourceset/group HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "resourceGroupID": 1,
  "decription": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/UpdateResourceSetGroup"

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
    <UpdateResourceSetGroupRequest xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <ResourceGroupID>int</ResourceGroupID>
      <NewDescription>string</NewDescription>
    </UpdateResourceSetGroupRequest>
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
    <UpdateResourceSetGroupResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <ResourceGroupID>int</ResourceGroupID>
      <Decription>string</Decription>
    </UpdateResourceSetGroupResult>
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
    var req = new UpdateResourceSetGroupRequest();

    //Send Request to Server and Get Response
    var res = await api.UpdateResourceSetGroupAsync(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("ResourceGroupID: {0}", res.ResourceGroupID);
    Console.WriteLine("Decription: {0}", res.Decription);
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
    UpdateResourceSetGroupRequest req = new UpdateResourceSetGroupRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetGroupResponse res = api.UpdateResourceSetGroup(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("ResourceGroupID: {0}", res.ResourceGroupID);
    Console.WriteLine("Decription: {0}", res.Decription);
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
    Dim req as new UpdateResourceSetGroupRequest()

    'Send Request to Server and Get Response
    Dim res As UpdateResourceSetGroupResponse = api.UpdateResourceSetGroup(req)

    'Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID)
    Console.WriteLine("ResourceGroupID: {0}", res.ResourceGroupID)
    Console.WriteLine("Decription: {0}", res.Decription)
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
    $res = $api.UpdateResourceSetGroup($req);

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
    UpdateResourceSetGroupRequest req = new UpdateResourceSetGroupRequest();

    //Send Request to Server and Get Response
    UpdateResourceSetGroupResponse res = api.getExigoApiSoap().updateResourceSetGroup(req, auth);

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

### CreateRelease

> Creates a Resource Set release

| | |
|---|---|
| Category | Web Content |
| REST | `POST /3.0/resourceset/release` |
| SOAP action | `https://api.exigo.com/CreateRelease` |
| WSDL elements | `CreateReleaseRequest` → `CreateReleaseResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateRelease |

#### Input

**`CreateReleaseRequest`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` | The unique numerical ID of the resource to create a release for. |

#### Output

**`CreateReleaseResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `ReleaseDate` | `DateTime` |  |
| `Version` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/resourceset/release HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "releaseDate": "2026-11-10T00:00:00-06:00",
  "version": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateRelease"

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
    <CreateReleaseRequest xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
    </CreateReleaseRequest>
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
    <CreateReleaseResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <ReleaseDate>dateTime</ReleaseDate>
      <Version>string</Version>
    </CreateReleaseResult>
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
    var req = new CreateReleaseRequest();

    //Send Request to Server and Get Response
    var res = await api.CreateReleaseAsync(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("ReleaseDate: {0}", res.ReleaseDate);
    Console.WriteLine("Version: {0}", res.Version);
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
    CreateReleaseRequest req = new CreateReleaseRequest();

    //Send Request to Server and Get Response
    CreateReleaseResponse res = api.CreateRelease(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("ReleaseDate: {0}", res.ReleaseDate);
    Console.WriteLine("Version: {0}", res.Version);
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
    Dim req as new CreateReleaseRequest()

    'Send Request to Server and Get Response
    Dim res As CreateReleaseResponse = api.CreateRelease(req)

    'Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID)
    Console.WriteLine("ReleaseDate: {0}", res.ReleaseDate)
    Console.WriteLine("Version: {0}", res.Version)
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
    $res = $api.CreateRelease($req);

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
    CreateReleaseRequest req = new CreateReleaseRequest();

    //Send Request to Server and Get Response
    CreateReleaseResponse res = api.getExigoApiSoap().createRelease(req, auth);

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

### DeleteRelease

> Deletes a Resource Set release

| | |
|---|---|
| Category | Web Content |
| REST | `DELETE /3.0/resourceset/release` |
| SOAP action | `https://api.exigo.com/DeleteRelease` |
| WSDL elements | `DeleteReleaseRequest` → `DeleteReleaseResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DeleteRelease |

#### Input

**`DeleteReleaseRequest`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` | The unique numerical ID of the resource containing the version to delete. |
| `Version` | `String` | The version to delete. |

#### Output

**`DeleteReleaseResponse`**

_No properties._

#### REST example

```http
DELETE https://yourcompany-api.exigo.com/3.0/resourceset/release HTTP/1.1
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
SOAPAction: "https://api.exigo.com/DeleteRelease"

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
    <DeleteReleaseRequest xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <Version>string</Version>
    </DeleteReleaseRequest>
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
    <DeleteReleaseResult xmlns="http://api.exigo.com/" />
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
    var req = new DeleteReleaseRequest();

    //Send Request to Server and Get Response
    var res = await api.DeleteReleaseAsync(req);

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
    DeleteReleaseRequest req = new DeleteReleaseRequest();

    //Send Request to Server and Get Response
    DeleteReleaseResponse res = api.DeleteRelease(req);

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
    Dim req as new DeleteReleaseRequest()

    'Send Request to Server and Get Response
    Dim res As DeleteReleaseResponse = api.DeleteRelease(req)

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
    $res = $api.DeleteRelease($req);

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
    DeleteReleaseRequest req = new DeleteReleaseRequest();

    //Send Request to Server and Get Response
    DeleteReleaseResponse res = api.getExigoApiSoap().deleteRelease(req, auth);

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

### GetReleases

> Gets Resource Set releases

| | |
|---|---|
| Category | Web Content |
| REST | `GET /3.0/resourceset/releaseAuthorization:` |
| SOAP action | `https://api.exigo.com/GetReleases` |
| WSDL elements | `GetReleasesRequest` → `GetReleasesResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetReleases |

#### Input

**`GetReleasesRequest`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` | The unique numerical ID of the resource to fetch releases from. |

#### Output

**`GetReleasesResponse`**

| Property | Type | Notes |
|---|---|---|
| `Releases` | `ResourceSetRelease[]` |  |

**`ResourceSetRelease`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `ResourceSetID` | `Int32` |  |
| &nbsp;&nbsp;↳ `Version` | `String` |  |
| &nbsp;&nbsp;↳ `ReleaseDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `IsArchived` | `Boolean` |  |
| &nbsp;&nbsp;↳ `HasArchiveStarted` | `Boolean` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/resourceset/releaseAuthorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "releases": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetReleases"

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
    <GetReleasesRequest xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
    </GetReleasesRequest>
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
    <GetReleasesResult xmlns="http://api.exigo.com/">
      <Releases>
        <ResourceSetRelease>
          <ResourceSetID>int</ResourceSetID>
          <Version>string</Version>
          <ReleaseDate>dateTime</ReleaseDate>
          <IsArchived>boolean</IsArchived>
          <HasArchiveStarted>boolean</HasArchiveStarted>
        </ResourceSetRelease>
      </Releases>
    </GetReleasesResult>
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
    var req = new GetReleasesRequest();

    //Send Request to Server and Get Response
    var res = await api.GetReleasesAsync(req);

    //Now examine the results:

    foreach (var resourceSetRelease  in res.Releases)
    {
        Console.WriteLine("ResourceSetID: {0}", resourceSetRelease.ResourceSetID);
        Console.WriteLine("Version: {0}", resourceSetRelease.Version);
        Console.WriteLine("ReleaseDate: {0}", resourceSetRelease.ReleaseDate);
        Console.WriteLine("IsArchived: {0}", resourceSetRelease.IsArchived);
        Console.WriteLine("HasArchiveStarted: {0}", resourceSetRelease.HasArchiveStarted);
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
    GetReleasesRequest req = new GetReleasesRequest();

    //Send Request to Server and Get Response
    GetReleasesResponse res = api.GetReleases(req);

    //Now examine the results:

    foreach (ResourceSetRelease resourceSetRelease  in res.Releases)
    {
        Console.WriteLine("ResourceSetID: {0}", resourceSetRelease.ResourceSetID);
        Console.WriteLine("Version: {0}", resourceSetRelease.Version);
        Console.WriteLine("ReleaseDate: {0}", resourceSetRelease.ReleaseDate);
        Console.WriteLine("IsArchived: {0}", resourceSetRelease.IsArchived);
        Console.WriteLine("HasArchiveStarted: {0}", resourceSetRelease.HasArchiveStarted);
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
    Dim req as new GetReleasesRequest()

    'Send Request to Server and Get Response
    Dim res As GetReleasesResponse = api.GetReleases(req)

    'Now examine the results:

    For Each resourceSetRelease As ResourceSetRelease In res.Releases
        Console.WriteLine("ResourceSetID: {0}", resourceSetRelease.ResourceSetID)
        Console.WriteLine("Version: {0}", resourceSetRelease.Version)
        Console.WriteLine("ReleaseDate: {0}", resourceSetRelease.ReleaseDate)
        Console.WriteLine("IsArchived: {0}", resourceSetRelease.IsArchived)
        Console.WriteLine("HasArchiveStarted: {0}", resourceSetRelease.HasArchiveStarted)
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
    $res = $api.GetReleases($req);

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
    GetReleasesRequest req = new GetReleasesRequest();

    //Send Request to Server and Get Response
    GetReleasesResponse res = api.getExigoApiSoap().getReleases(req, auth);

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

### DeployRelease

> Deploys a Resource Set Release

| | |
|---|---|
| Category | Web Content |
| REST | `POST /3.0/resourceset/release/deploy` |
| SOAP action | `https://api.exigo.com/DeployRelease` |
| WSDL elements | `DeployReleaseRequest` → `DeployReleaseResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DeployRelease |

#### Input

**`DeployReleaseRequest`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` | The unique numerical ID of the resource to deploy a release for. |
| `EnvironmentCode` | `String` |  |
| `Version` | `String` | Optional. |

#### Output

**`DeployReleaseResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `Version` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/resourceset/release/deploy HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "version": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/DeployRelease"

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
    <DeployReleaseRequest xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <EnvironmentCode>string</EnvironmentCode>
      <Version>string</Version>
    </DeployReleaseRequest>
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
    <DeployReleaseResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <Version>string</Version>
    </DeployReleaseResult>
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
    var req = new DeployReleaseRequest();

    //Send Request to Server and Get Response
    var res = await api.DeployReleaseAsync(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("Version: {0}", res.Version);
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
    DeployReleaseRequest req = new DeployReleaseRequest();

    //Send Request to Server and Get Response
    DeployReleaseResponse res = api.DeployRelease(req);

    //Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID);
    Console.WriteLine("Version: {0}", res.Version);
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
    Dim req as new DeployReleaseRequest()

    'Send Request to Server and Get Response
    Dim res As DeployReleaseResponse = api.DeployRelease(req)

    'Now examine the results:
    Console.WriteLine("ResourceSetID: {0}", res.ResourceSetID)
    Console.WriteLine("Version: {0}", res.Version)
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
    $res = $api.DeployRelease($req);

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
    DeployReleaseRequest req = new DeployReleaseRequest();

    //Send Request to Server and Get Response
    DeployReleaseResponse res = api.getExigoApiSoap().deployRelease(req, auth);

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

### RevertToRecentRelease

> Reverts to most recent Resource Set Release

| | |
|---|---|
| Category | Web Content |
| REST | `POST /3.0/resourceset/release/revert` |
| SOAP action | `https://api.exigo.com/RevertToRecentRelease` |
| WSDL elements | `RevertToRecentReleaseRequest` → `RevertToRecentReleaseResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=RevertToRecentRelease |

#### Input

**`RevertToRecentReleaseRequest`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` | The ResourceSet that will be reverted to its most recent release. |

#### Output

**`RevertToRecentReleaseResponse`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSetID` | `Int32` |  |
| `ReleaseDate` | `DateTime` |  |
| `Version` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/resourceset/release/revert HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "resourceSetID": 1,
  "releaseDate": "2026-11-10T00:00:00-06:00",
  "version": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/RevertToRecentRelease"

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
    <RevertToRecentReleaseRequest xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
    </RevertToRecentReleaseRequest>
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
    <RevertToRecentReleaseResult xmlns="http://api.exigo.com/">
      <ResourceSetID>int</ResourceSetID>
      <ReleaseDate>dateTime</ReleaseDate>
      <Version>string</Version>
    </RevertToRecentReleaseResult>
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
    var req = new RevertToRecentReleaseRequest();

    //Send Request to Server and Get Response
    var res = await api.RevertToRecentReleaseAsync(req);

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
    RevertToRecentReleaseRequest req = new RevertToRecentReleaseRequest();

    //Send Request to Server and Get Response
    RevertToRecentReleaseResponse res = api.RevertToRecentRelease(req);

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
    Dim req as new RevertToRecentReleaseRequest()

    'Send Request to Server and Get Response
    Dim res As RevertToRecentReleaseResponse = api.RevertToRecentRelease(req)

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
    $res = $api.RevertToRecentRelease($req);

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
    RevertToRecentReleaseRequest req = new RevertToRecentReleaseRequest();

    //Send Request to Server and Get Response
    RevertToRecentReleaseResponse res = api.getExigoApiSoap().revertToRecentRelease(req, auth);

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
