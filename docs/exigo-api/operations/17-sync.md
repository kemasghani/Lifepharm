# Exigo API — Sync

API version v2025.11.7.6. Crawled 2026-11-11 from https://api.exigo.com/3.0/. Back to [index](../README.md).

| Operation | REST | Summary |
|---|---|---|
| [CreateDestination](#createdestination) | `POST /3.0/destination` | Creates a destination. |
| [GetDestinations](#getdestinations) | `GET /3.0/destinationAuthorization:` | Gets destinations. |
| [UpdateDestination](#updatedestination) | `PATCH /3.0/destination` | Updates a destination. |
| [DeleteDestination](#deletedestination) | `DELETE /3.0/destination` | Deletes a destination. |
| [EnableDestination](#enabledestination) | `PUT /3.0/destination/enable` | Enables a destination. |
| [DisableDestination](#disabledestination) | `PUT /3.0/destination/disable` | Disables a destination. |
| [GetFilterGroup](#getfiltergroup) | `GET /3.0/filtergroupAuthorization:` | Gets a filter group. Filtering MUST be enabled first. |
| [EnableFilterGroup](#enablefiltergroup) | `PUT /3.0/filtergroup/enable` | Enables a group for filtering. |
| [DisableFilterGroup](#disablefiltergroup) | `PUT /3.0/filtergroup/disable` | Disables a group for filtering. |
| [EnableFiltering](#enablefiltering) | `PUT /3.0/filtering/enable` | Enables filtering. |
| [DisableFiltering](#disablefiltering) | `PUT /3.0/filtering/disable` | Disables Filtering. |
| [GetAlertSettings](#getalertsettings) | `GET /3.0/alertsettingsAuthorization:` | Gets alert setings information. |
| [UpdateAlertSettings](#updatealertsettings) | `PATCH /3.0/alertsettings` | Updates te alert settings. |
| [GetExtendedDbSettings](#getextendeddbsettings) | `GET /3.0/extendeddbsettingsAuthorization:` | Gets settings for extended DB. |
| [UpdateExtendedDbSettings](#updateextendeddbsettings) | `PATCH /3.0/extendeddbsettings` | Updates settings for extended DB. |
| [GetReIndexSettings](#getreindexsettings) | `GET /3.0/reindexsettingsAuthorization:` | Gets Re-Index settings. |
| [UpdateReIndexSettings](#updatereindexsettings) | `PATCH /3.0/reindexsettings` | Updates Re-Index settings. |
| [GetTableSettings](#gettablesettings) | `GET /3.0/tablesettingsAuthorization:` | Gets a table's settings. |
| [UpdateTableSettings](#updatetablesettings) | `PATCH /3.0/tablesettings` | Updates a table's settings. |
| [GetReIndexHistory](#getreindexhistory) | `GET /3.0/reindexsettings/history?destinationId=1` | Gets ReIndexHistory. |
| [UpdateTableFilterSettings](#updatetablefiltersettings) | `PATCH /3.0/filtergroup/update` | Updates Table Filter Settings. |
| [CreateTableFilterSettings](#createtablefiltersettings) | SOAP only | Creates Table Filter Settings. |
| [SubmitDestinationTest](#submitdestinationtest) | `POST /3.0/destination/submittest` | Begins process for testing a conection. |
| [GetDestinationTest](#getdestinationtest) | `GET /3.0/destination/gettest?requestId=1` | Gets result for testing a conection. |

---
### CreateDestination

> Creates a destination.

| | |
|---|---|
| Category | Sync |
| REST | `POST /3.0/destination` |
| SOAP action | `https://api.exigo.com/CreateDestination` |
| WSDL elements | `CreateDestinationRequest` → `CreateDestinationResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateDestination |

#### Input

**`CreateDestinationRequest`**

| Property | Type | Notes |
|---|---|---|
| `Name` | `String` | Optional. The name for the new destination. |
| `ConnectionString` | `String` | Optional. |

#### Output

**`CreateDestinationResponse`**

| Property | Type | Notes |
|---|---|---|
| `DestinationID` | `Int32` |  |
| `Name` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/destination HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "destinationID": 1,
  "name": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateDestination"

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
    <CreateDestinationRequest xmlns="http://api.exigo.com/">
      <Name>string</Name>
      <ConnectionString>string</ConnectionString>
    </CreateDestinationRequest>
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
    <CreateDestinationResult xmlns="http://api.exigo.com/">
      <DestinationID>int</DestinationID>
      <Name>string</Name>
    </CreateDestinationResult>
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
    var req = new CreateDestinationRequest();

    //Send Request to Server and Get Response
    var res = await api.CreateDestinationAsync(req);

    //Now examine the results:
    Console.WriteLine("DestinationID: {0}", res.DestinationID);
    Console.WriteLine("Name: {0}", res.Name);
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
    CreateDestinationRequest req = new CreateDestinationRequest();

    //Send Request to Server and Get Response
    CreateDestinationResponse res = api.CreateDestination(req);

    //Now examine the results:
    Console.WriteLine("DestinationID: {0}", res.DestinationID);
    Console.WriteLine("Name: {0}", res.Name);
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
    Dim req as new CreateDestinationRequest()

    'Send Request to Server and Get Response
    Dim res As CreateDestinationResponse = api.CreateDestination(req)

    'Now examine the results:
    Console.WriteLine("DestinationID: {0}", res.DestinationID)
    Console.WriteLine("Name: {0}", res.Name)
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
    $res = $api.CreateDestination($req);

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
    CreateDestinationRequest req = new CreateDestinationRequest();

    //Send Request to Server and Get Response
    CreateDestinationResponse res = api.getExigoApiSoap().createDestination(req, auth);

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

### GetDestinations

> Gets destinations.

| | |
|---|---|
| Category | Sync |
| REST | `GET /3.0/destinationAuthorization:` |
| SOAP action | `https://api.exigo.com/GetDestinations` |
| WSDL elements | `GetDestinationsRequest` → `GetDestinationsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetDestinations |

#### Input

**`GetDestinationsRequest`**

| Property | Type | Notes |
|---|---|---|
| `DestinationID` | `Int32` | Optional. Leave empty to fetch all. |

#### Output

**`GetDestinationsResponse`**

| Property | Type | Notes |
|---|---|---|
| `Destinations` | `Destination[]` |  |

**`Destination`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `DestinationID` | `Int32` |  |
| &nbsp;&nbsp;↳ `Name` | `String` |  |
| &nbsp;&nbsp;↳ `Enabled` | `Boolean` |  |
| &nbsp;&nbsp;↳ `ConnectionString` | `String` |  |
| &nbsp;&nbsp;↳ `ModifiedBy` | `String` |  |
| &nbsp;&nbsp;↳ `ModifiedDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `AlertSettings` | `AlertSettings` |  |
| &nbsp;&nbsp;↳ `ReIndexSettings` | `ReIndexSettings` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/destinationAuthorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "destinations": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetDestinations"

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
    <GetDestinationsRequest xmlns="http://api.exigo.com/">
      <DestinationID>int</DestinationID>
    </GetDestinationsRequest>
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
    <GetDestinationsResult xmlns="http://api.exigo.com/">
      <Destinations>
        <Destination>
          <DestinationID>int</DestinationID>
          <Name>string</Name>
          <Enabled>boolean</Enabled>
          <ConnectionString>string</ConnectionString>
          <ModifiedBy>string</ModifiedBy>
          <ModifiedDate>dateTime</ModifiedDate>
          <AlertSettings>
            <AlertOptIn>boolean</AlertOptIn>
            <AlertEmail>
              <string>string</string>
            </AlertEmail>
            <AlertPhone>
              <string>string</string>
            </AlertPhone>
          </AlertSettings>
          <ReIndexSettings>
            <ReIndexStartTime>dateTime</ReIndexStartTime>
            <ReIndexMaxDuration>int</ReIndexMaxDuration>
            <LastReIndexed>dateTime</LastReIndexed>
          </ReIndexSettings>
        </Destination>
      </Destinations>
    </GetDestinationsResult>
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
    var req = new GetDestinationsRequest();

    //Send Request to Server and Get Response
    var res = await api.GetDestinationsAsync(req);

    //Now examine the results:

    foreach (var destination  in res.Destinations)
    {
        Console.WriteLine("DestinationID: {0}", destination.DestinationID);
        Console.WriteLine("Name: {0}", destination.Name);
        Console.WriteLine("Enabled: {0}", destination.Enabled);
        Console.WriteLine("ConnectionString: {0}", destination.ConnectionString);
        Console.WriteLine("ModifiedBy: {0}", destination.ModifiedBy);
        Console.WriteLine("ModifiedDate: {0}", destination.ModifiedDate);
        Console.WriteLine("AlertSettings: {0}", destination.AlertSettings);
        Console.WriteLine("ReIndexSettings: {0}", destination.ReIndexSettings);
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
    GetDestinationsRequest req = new GetDestinationsRequest();

    //Send Request to Server and Get Response
    GetDestinationsResponse res = api.GetDestinations(req);

    //Now examine the results:

    foreach (Destination destination  in res.Destinations)
    {
        Console.WriteLine("DestinationID: {0}", destination.DestinationID);
        Console.WriteLine("Name: {0}", destination.Name);
        Console.WriteLine("Enabled: {0}", destination.Enabled);
        Console.WriteLine("ConnectionString: {0}", destination.ConnectionString);
        Console.WriteLine("ModifiedBy: {0}", destination.ModifiedBy);
        Console.WriteLine("ModifiedDate: {0}", destination.ModifiedDate);
        Console.WriteLine("AlertSettings: {0}", destination.AlertSettings);
        Console.WriteLine("ReIndexSettings: {0}", destination.ReIndexSettings);
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
    Dim req as new GetDestinationsRequest()

    'Send Request to Server and Get Response
    Dim res As GetDestinationsResponse = api.GetDestinations(req)

    'Now examine the results:

    For Each destination As Destination In res.Destinations
        Console.WriteLine("DestinationID: {0}", destination.DestinationID)
        Console.WriteLine("Name: {0}", destination.Name)
        Console.WriteLine("Enabled: {0}", destination.Enabled)
        Console.WriteLine("ConnectionString: {0}", destination.ConnectionString)
        Console.WriteLine("ModifiedBy: {0}", destination.ModifiedBy)
        Console.WriteLine("ModifiedDate: {0}", destination.ModifiedDate)
        Console.WriteLine("AlertSettings: {0}", destination.AlertSettings)
        Console.WriteLine("ReIndexSettings: {0}", destination.ReIndexSettings)
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
    $res = $api.GetDestinations($req);

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
    GetDestinationsRequest req = new GetDestinationsRequest();

    //Send Request to Server and Get Response
    GetDestinationsResponse res = api.getExigoApiSoap().getDestinations(req, auth);

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

### UpdateDestination

> Updates a destination.

| | |
|---|---|
| Category | Sync |
| REST | `PATCH /3.0/destination` |
| SOAP action | `https://api.exigo.com/UpdateDestination` |
| WSDL elements | `UpdateDestinationRequest` → `UpdateDestinationResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateDestination |

#### Input

**`UpdateDestinationRequest`**

| Property | Type | Notes |
|---|---|---|
| `DestinationID` | `Int32` |  |
| `Name` | `String` | Optional. |
| `ConnectionString` | `String` | Optional. |

#### Output

**`UpdateDestinationResponse`**

_No properties._

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/destination HTTP/1.1
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
SOAPAction: "https://api.exigo.com/UpdateDestination"

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
    <UpdateDestinationRequest xmlns="http://api.exigo.com/">
      <DestinationID>int</DestinationID>
      <Name>string</Name>
      <ConnectionString>string</ConnectionString>
    </UpdateDestinationRequest>
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
    <UpdateDestinationResult xmlns="http://api.exigo.com/" />
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
    var req = new UpdateDestinationRequest();

    //Send Request to Server and Get Response
    var res = await api.UpdateDestinationAsync(req);

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
    UpdateDestinationRequest req = new UpdateDestinationRequest();

    //Send Request to Server and Get Response
    UpdateDestinationResponse res = api.UpdateDestination(req);

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
    Dim req as new UpdateDestinationRequest()

    'Send Request to Server and Get Response
    Dim res As UpdateDestinationResponse = api.UpdateDestination(req)

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
    $res = $api.UpdateDestination($req);

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
    UpdateDestinationRequest req = new UpdateDestinationRequest();

    //Send Request to Server and Get Response
    UpdateDestinationResponse res = api.getExigoApiSoap().updateDestination(req, auth);

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

### DeleteDestination

> Deletes a destination.

| | |
|---|---|
| Category | Sync |
| REST | `DELETE /3.0/destination` |
| SOAP action | `https://api.exigo.com/DeleteDestination` |
| WSDL elements | `DeleteDestinationRequest` → `DeleteDestinationResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DeleteDestination |

#### Input

**`DeleteDestinationRequest`**

| Property | Type | Notes |
|---|---|---|
| `DestinationID` | `Int32` |  |

#### Output

**`DeleteDestinationResponse`**

_No properties._

#### REST example

```http
DELETE https://yourcompany-api.exigo.com/3.0/destination HTTP/1.1
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
SOAPAction: "https://api.exigo.com/DeleteDestination"

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
    <DeleteDestinationRequest xmlns="http://api.exigo.com/">
      <DestinationID>int</DestinationID>
    </DeleteDestinationRequest>
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
    <DeleteDestinationResult xmlns="http://api.exigo.com/" />
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
    var req = new DeleteDestinationRequest();

    //Send Request to Server and Get Response
    var res = await api.DeleteDestinationAsync(req);

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
    DeleteDestinationRequest req = new DeleteDestinationRequest();

    //Send Request to Server and Get Response
    DeleteDestinationResponse res = api.DeleteDestination(req);

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
    Dim req as new DeleteDestinationRequest()

    'Send Request to Server and Get Response
    Dim res As DeleteDestinationResponse = api.DeleteDestination(req)

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
    $res = $api.DeleteDestination($req);

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
    DeleteDestinationRequest req = new DeleteDestinationRequest();

    //Send Request to Server and Get Response
    DeleteDestinationResponse res = api.getExigoApiSoap().deleteDestination(req, auth);

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

### EnableDestination

> Enables a destination.

| | |
|---|---|
| Category | Sync |
| REST | `PUT /3.0/destination/enable` |
| SOAP action | `https://api.exigo.com/EnableDestination` |
| WSDL elements | `EnableDestinationRequest` → `EnableDestinationResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=EnableDestination |

#### Input

**`EnableDestinationRequest`**

| Property | Type | Notes |
|---|---|---|
| `DestinationID` | `Int32` |  |

#### Output

**`EnableDestinationResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/destination/enable HTTP/1.1
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
SOAPAction: "https://api.exigo.com/EnableDestination"

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
    <EnableDestinationRequest xmlns="http://api.exigo.com/">
      <DestinationID>int</DestinationID>
    </EnableDestinationRequest>
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
    <EnableDestinationResult xmlns="http://api.exigo.com/" />
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
    var req = new EnableDestinationRequest();

    //Send Request to Server and Get Response
    var res = await api.EnableDestinationAsync(req);

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
    EnableDestinationRequest req = new EnableDestinationRequest();

    //Send Request to Server and Get Response
    EnableDestinationResponse res = api.EnableDestination(req);

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
    Dim req as new EnableDestinationRequest()

    'Send Request to Server and Get Response
    Dim res As EnableDestinationResponse = api.EnableDestination(req)

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
    $res = $api.EnableDestination($req);

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
    EnableDestinationRequest req = new EnableDestinationRequest();

    //Send Request to Server and Get Response
    EnableDestinationResponse res = api.getExigoApiSoap().enableDestination(req, auth);

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

### DisableDestination

> Disables a destination.

| | |
|---|---|
| Category | Sync |
| REST | `PUT /3.0/destination/disable` |
| SOAP action | `https://api.exigo.com/DisableDestination` |
| WSDL elements | `DisableDestinationRequest` → `DisableDestinationResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DisableDestination |

#### Input

**`DisableDestinationRequest`**

| Property | Type | Notes |
|---|---|---|
| `DestinationID` | `Int32` |  |

#### Output

**`DisableDestinationResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/destination/disable HTTP/1.1
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
SOAPAction: "https://api.exigo.com/DisableDestination"

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
    <DisableDestinationRequest xmlns="http://api.exigo.com/">
      <DestinationID>int</DestinationID>
    </DisableDestinationRequest>
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
    <DisableDestinationResult xmlns="http://api.exigo.com/" />
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
    var req = new DisableDestinationRequest();

    //Send Request to Server and Get Response
    var res = await api.DisableDestinationAsync(req);

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
    DisableDestinationRequest req = new DisableDestinationRequest();

    //Send Request to Server and Get Response
    DisableDestinationResponse res = api.DisableDestination(req);

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
    Dim req as new DisableDestinationRequest()

    'Send Request to Server and Get Response
    Dim res As DisableDestinationResponse = api.DisableDestination(req)

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
    $res = $api.DisableDestination($req);

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
    DisableDestinationRequest req = new DisableDestinationRequest();

    //Send Request to Server and Get Response
    DisableDestinationResponse res = api.getExigoApiSoap().disableDestination(req, auth);

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

### GetFilterGroup

> Gets a filter group. Filtering MUST be enabled first.

| | |
|---|---|
| Category | Sync |
| REST | `GET /3.0/filtergroupAuthorization:` |
| SOAP action | `https://api.exigo.com/GetFilterGroup` |
| WSDL elements | `GetFilterGroupRequest` → `GetFilterGroupResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetFilterGroup |

#### Input

**`GetFilterGroupRequest`**

| Property | Type | Notes |
|---|---|---|
| `DestinationID` | `Int32` |  |
| `FilterGroups` | `TableGroupID[]` | **Values:** `Misc`, `AutoOrder`, `Core`, `Commission`, `Customer`, `CustomersExtended`, `Item`, `Log`, `Messaging`, `Order`, `Payout`, `Tree`, `User`, `Image` |

**`TableGroupID`**

_No properties._

#### Output

**`GetFilterGroupResponse`**

| Property | Type | Notes |
|---|---|---|
| `FilterGroups` | `FilterGroup[]` |  |

**`FilterGroup`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `TableGroupId` | `Int32` |  |
| &nbsp;&nbsp;↳ `Enabled` | `Boolean` |  |
| &nbsp;&nbsp;↳ `TrueUp` | `Boolean` |  |
| &nbsp;&nbsp;↳ `Tables` | `TableName[]` |  |
| &nbsp;&nbsp;↳ `TableFilterSettings` | `TableFilterSetting[]` |  |

**`TableName`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `SchemaName` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Name` | `String` |  |

**`TableFilterSetting`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `SchemaName` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `TableName` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `ColumnName` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `FilterType` | `FilterType` | **Values:** `MaxDays`, `InList` |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `FilterValue` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `IsKey` | `Boolean` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/filtergroupAuthorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "filterGroups": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetFilterGroup"

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
    <GetFilterGroupRequest xmlns="http://api.exigo.com/">
      <DestinationID>int</DestinationID>
      <FilterGroups>
        <TableGroupID>Misc or AutoOrder or Core or Commission or Customer or CustomersExtended or Item or Log or Messaging or Order or Payout or Tree or User or Image</TableGroupID>
      </FilterGroups>
    </GetFilterGroupRequest>
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
    <GetFilterGroupResult xmlns="http://api.exigo.com/">
      <FilterGroups>
        <FilterGroup>
          <TableGroupId>int</TableGroupId>
          <Enabled>boolean</Enabled>
          <TrueUp>boolean</TrueUp>
          <Tables>
            <TableName>
              <SchemaName>string</SchemaName>
              <Name>string</Name>
            </TableName>
          </Tables>
          <TableFilterSettings>
            <TableFilterSetting>
              <SchemaName>string</SchemaName>
              <TableName>string</TableName>
              <ColumnName>string</ColumnName>
              <FilterType>MaxDays or InList</FilterType>
              <FilterValue>string</FilterValue>
              <IsKey>boolean</IsKey>
            </TableFilterSetting>
          </TableFilterSettings>
        </FilterGroup>
      </FilterGroups>
    </GetFilterGroupResult>
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
    var req = new GetFilterGroupRequest();

    //Send Request to Server and Get Response
    var res = await api.GetFilterGroupAsync(req);

    //Now examine the results:

    foreach (var filterGroup  in res.FilterGroups)
    {
        Console.WriteLine("TableGroupId: {0}", filterGroup.TableGroupId);
        Console.WriteLine("Enabled: {0}", filterGroup.Enabled);
        Console.WriteLine("TrueUp: {0}", filterGroup.TrueUp);

        foreach (var tableName  in filterGroup.Tables)
        {
            Console.WriteLine("SchemaName: {0}", tableName.SchemaName);
            Console.WriteLine("Name: {0}", tableName.Name);
        }

        foreach (var tableFilterSetting  in filterGroup.TableFilterSettings)
        {
            Console.WriteLine("SchemaName: {0}", tableFilterSetting.SchemaName);
            Console.WriteLine("TableName: {0}", tableFilterSetting.TableName);
            Console.WriteLine("ColumnName: {0}", tableFilterSetting.ColumnName);
            Console.WriteLine("FilterType: {0}", tableFilterSetting.FilterType);
            Console.WriteLine("FilterValue: {0}", tableFilterSetting.FilterValue);
            Console.WriteLine("IsKey: {0}", tableFilterSetting.IsKey);
        }
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
    GetFilterGroupRequest req = new GetFilterGroupRequest();

    //Send Request to Server and Get Response
    GetFilterGroupResponse res = api.GetFilterGroup(req);

    //Now examine the results:

    foreach (FilterGroup filterGroup  in res.FilterGroups)
    {
        Console.WriteLine("TableGroupId: {0}", filterGroup.TableGroupId);
        Console.WriteLine("Enabled: {0}", filterGroup.Enabled);
        Console.WriteLine("TrueUp: {0}", filterGroup.TrueUp);

        foreach (TableName tableName  in filterGroup.Tables)
        {
            Console.WriteLine("SchemaName: {0}", tableName.SchemaName);
            Console.WriteLine("Name: {0}", tableName.Name);
        }

        foreach (TableFilterSetting tableFilterSetting  in filterGroup.TableFilterSettings)
        {
            Console.WriteLine("SchemaName: {0}", tableFilterSetting.SchemaName);
            Console.WriteLine("TableName: {0}", tableFilterSetting.TableName);
            Console.WriteLine("ColumnName: {0}", tableFilterSetting.ColumnName);
            Console.WriteLine("FilterType: {0}", tableFilterSetting.FilterType);
            Console.WriteLine("FilterValue: {0}", tableFilterSetting.FilterValue);
            Console.WriteLine("IsKey: {0}", tableFilterSetting.IsKey);
        }
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
    Dim req as new GetFilterGroupRequest()

    'Send Request to Server and Get Response
    Dim res As GetFilterGroupResponse = api.GetFilterGroup(req)

    'Now examine the results:

    For Each filterGroup As FilterGroup In res.FilterGroups
        Console.WriteLine("TableGroupId: {0}", filterGroup.TableGroupId)
        Console.WriteLine("Enabled: {0}", filterGroup.Enabled)
        Console.WriteLine("TrueUp: {0}", filterGroup.TrueUp)

        For Each tableName As TableName In filterGroup.Tables
            Console.WriteLine("SchemaName: {0}", tableName.SchemaName)
            Console.WriteLine("Name: {0}", tableName.Name)
        Next

        For Each tableFilterSetting As TableFilterSetting In filterGroup.TableFilterSettings
            Console.WriteLine("SchemaName: {0}", tableFilterSetting.SchemaName)
            Console.WriteLine("TableName: {0}", tableFilterSetting.TableName)
            Console.WriteLine("ColumnName: {0}", tableFilterSetting.ColumnName)
            Console.WriteLine("FilterType: {0}", tableFilterSetting.FilterType)
            Console.WriteLine("FilterValue: {0}", tableFilterSetting.FilterValue)
            Console.WriteLine("IsKey: {0}", tableFilterSetting.IsKey)
        Next
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
    $res = $api.GetFilterGroup($req);

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
    GetFilterGroupRequest req = new GetFilterGroupRequest();

    //Send Request to Server and Get Response
    GetFilterGroupResponse res = api.getExigoApiSoap().getFilterGroup(req, auth);

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

### EnableFilterGroup

> Enables a group for filtering.

| | |
|---|---|
| Category | Sync |
| REST | `PUT /3.0/filtergroup/enable` |
| SOAP action | `https://api.exigo.com/EnableFilterGroup` |
| WSDL elements | `EnableFilterGroupRequest` → `EnableFilterGroupResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=EnableFilterGroup |

#### Input

**`EnableFilterGroupRequest`**

| Property | Type | Notes |
|---|---|---|
| `DestinationID` | `Int32` |  |
| `FilterGroupID` | `TableGroupID` | **Values:** `Misc`, `AutoOrder`, `Core`, `Commission`, `Customer`, `CustomersExtended`, `Item`, `Log`, `Messaging`, `Order`, `Payout`, `Tree`, `User`, `Image` |

#### Output

**`EnableFilterGroupResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/filtergroup/enable HTTP/1.1
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
SOAPAction: "https://api.exigo.com/EnableFilterGroup"

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
    <EnableFilterGroupRequest xmlns="http://api.exigo.com/">
      <DestinationID>int</DestinationID>
      <FilterGroupID>Misc or AutoOrder or Core or Commission or Customer or CustomersExtended or Item or Log or Messaging or Order or Payout or Tree or User or Image</FilterGroupID>
    </EnableFilterGroupRequest>
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
    <EnableFilterGroupResult xmlns="http://api.exigo.com/" />
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
    var req = new EnableFilterGroupRequest();

    //Send Request to Server and Get Response
    var res = await api.EnableFilterGroupAsync(req);

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
    EnableFilterGroupRequest req = new EnableFilterGroupRequest();

    //Send Request to Server and Get Response
    EnableFilterGroupResponse res = api.EnableFilterGroup(req);

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
    Dim req as new EnableFilterGroupRequest()

    'Send Request to Server and Get Response
    Dim res As EnableFilterGroupResponse = api.EnableFilterGroup(req)

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
    $res = $api.EnableFilterGroup($req);

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
    EnableFilterGroupRequest req = new EnableFilterGroupRequest();

    //Send Request to Server and Get Response
    EnableFilterGroupResponse res = api.getExigoApiSoap().enableFilterGroup(req, auth);

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

### DisableFilterGroup

> Disables a group for filtering.

| | |
|---|---|
| Category | Sync |
| REST | `PUT /3.0/filtergroup/disable` |
| SOAP action | `https://api.exigo.com/DisableFilterGroup` |
| WSDL elements | `DisableFilterGroupRequest` → `DisableFilterGroupResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DisableFilterGroup |

#### Input

**`DisableFilterGroupRequest`**

| Property | Type | Notes |
|---|---|---|
| `DestinationID` | `Int32` |  |
| `FilterGroupID` | `TableGroupID` | **Values:** `Misc`, `AutoOrder`, `Core`, `Commission`, `Customer`, `CustomersExtended`, `Item`, `Log`, `Messaging`, `Order`, `Payout`, `Tree`, `User`, `Image` |

#### Output

**`DisableFilterGroupResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/filtergroup/disable HTTP/1.1
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
SOAPAction: "https://api.exigo.com/DisableFilterGroup"

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
    <DisableFilterGroupRequest xmlns="http://api.exigo.com/">
      <DestinationID>int</DestinationID>
      <FilterGroupID>Misc or AutoOrder or Core or Commission or Customer or CustomersExtended or Item or Log or Messaging or Order or Payout or Tree or User or Image</FilterGroupID>
    </DisableFilterGroupRequest>
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
    <DisableFilterGroupResult xmlns="http://api.exigo.com/" />
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
    var req = new DisableFilterGroupRequest();

    //Send Request to Server and Get Response
    var res = await api.DisableFilterGroupAsync(req);

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
    DisableFilterGroupRequest req = new DisableFilterGroupRequest();

    //Send Request to Server and Get Response
    DisableFilterGroupResponse res = api.DisableFilterGroup(req);

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
    Dim req as new DisableFilterGroupRequest()

    'Send Request to Server and Get Response
    Dim res As DisableFilterGroupResponse = api.DisableFilterGroup(req)

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
    $res = $api.DisableFilterGroup($req);

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
    DisableFilterGroupRequest req = new DisableFilterGroupRequest();

    //Send Request to Server and Get Response
    DisableFilterGroupResponse res = api.getExigoApiSoap().disableFilterGroup(req, auth);

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

### EnableFiltering

> Enables filtering.

| | |
|---|---|
| Category | Sync |
| REST | `PUT /3.0/filtering/enable` |
| SOAP action | `https://api.exigo.com/EnableFiltering` |
| WSDL elements | `EnableFilteringRequest` → `EnableFilteringResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=EnableFiltering |

#### Input

**`EnableFilteringRequest`**

| Property | Type | Notes |
|---|---|---|
| `DestinationID` | `Int32` |  |

#### Output

**`EnableFilteringResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/filtering/enable HTTP/1.1
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
SOAPAction: "https://api.exigo.com/EnableFiltering"

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
    <EnableFilteringRequest xmlns="http://api.exigo.com/">
      <DestinationID>int</DestinationID>
    </EnableFilteringRequest>
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
    <EnableFilteringResult xmlns="http://api.exigo.com/" />
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
    var req = new EnableFilteringRequest();

    //Send Request to Server and Get Response
    var res = await api.EnableFilteringAsync(req);

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
    EnableFilteringRequest req = new EnableFilteringRequest();

    //Send Request to Server and Get Response
    EnableFilteringResponse res = api.EnableFiltering(req);

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
    Dim req as new EnableFilteringRequest()

    'Send Request to Server and Get Response
    Dim res As EnableFilteringResponse = api.EnableFiltering(req)

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
    $res = $api.EnableFiltering($req);

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
    EnableFilteringRequest req = new EnableFilteringRequest();

    //Send Request to Server and Get Response
    EnableFilteringResponse res = api.getExigoApiSoap().enableFiltering(req, auth);

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

### DisableFiltering

> Disables Filtering.

| | |
|---|---|
| Category | Sync |
| REST | `PUT /3.0/filtering/disable` |
| SOAP action | `https://api.exigo.com/DisableFiltering` |
| WSDL elements | `DisableFilteringRequest` → `DisableFilteringResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DisableFiltering |

#### Input

**`DisableFilteringRequest`**

| Property | Type | Notes |
|---|---|---|
| `DestinationID` | `Int32` |  |

#### Output

**`DisableFilteringResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/filtering/disable HTTP/1.1
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
SOAPAction: "https://api.exigo.com/DisableFiltering"

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
    <DisableFilteringRequest xmlns="http://api.exigo.com/">
      <DestinationID>int</DestinationID>
    </DisableFilteringRequest>
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
    <DisableFilteringResult xmlns="http://api.exigo.com/" />
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
    var req = new DisableFilteringRequest();

    //Send Request to Server and Get Response
    var res = await api.DisableFilteringAsync(req);

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
    DisableFilteringRequest req = new DisableFilteringRequest();

    //Send Request to Server and Get Response
    DisableFilteringResponse res = api.DisableFiltering(req);

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
    Dim req as new DisableFilteringRequest()

    'Send Request to Server and Get Response
    Dim res As DisableFilteringResponse = api.DisableFiltering(req)

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
    $res = $api.DisableFiltering($req);

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
    DisableFilteringRequest req = new DisableFilteringRequest();

    //Send Request to Server and Get Response
    DisableFilteringResponse res = api.getExigoApiSoap().disableFiltering(req, auth);

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

### GetAlertSettings

> Gets alert setings information.

| | |
|---|---|
| Category | Sync |
| REST | `GET /3.0/alertsettingsAuthorization:` |
| SOAP action | `https://api.exigo.com/GetAlertSettings` |
| WSDL elements | `GetAlertSettingsRequest` → `GetAlertSettingsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetAlertSettings |

#### Input

**`GetAlertSettingsRequest`**

| Property | Type | Notes |
|---|---|---|
| `DestinationID` | `Int32` |  |

#### Output

**`GetAlertSettingsResponse`**

| Property | Type | Notes |
|---|---|---|
| `AlertOptIn` | `Boolean` |  |
| `AlertEmail` | `String[]` |  |
| `AlertPhone` | `String[]` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/alertsettingsAuthorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "alertOptIn": true,
  "alertEmail": null,
  "alertPhone": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetAlertSettings"

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
    <GetAlertSettingsRequest xmlns="http://api.exigo.com/">
      <DestinationID>int</DestinationID>
    </GetAlertSettingsRequest>
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
    <GetAlertSettingsResult xmlns="http://api.exigo.com/">
      <AlertOptIn>boolean</AlertOptIn>
      <AlertEmail>
        <string>string</string>
      </AlertEmail>
      <AlertPhone>
        <string>string</string>
      </AlertPhone>
    </GetAlertSettingsResult>
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
    var req = new GetAlertSettingsRequest();

    //Send Request to Server and Get Response
    var res = await api.GetAlertSettingsAsync(req);

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
    GetAlertSettingsRequest req = new GetAlertSettingsRequest();

    //Send Request to Server and Get Response
    GetAlertSettingsResponse res = api.GetAlertSettings(req);

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
    Dim req as new GetAlertSettingsRequest()

    'Send Request to Server and Get Response
    Dim res As GetAlertSettingsResponse = api.GetAlertSettings(req)

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
    $res = $api.GetAlertSettings($req);

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
    GetAlertSettingsRequest req = new GetAlertSettingsRequest();

    //Send Request to Server and Get Response
    GetAlertSettingsResponse res = api.getExigoApiSoap().getAlertSettings(req, auth);

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

### UpdateAlertSettings

> Updates te alert settings.

| | |
|---|---|
| Category | Sync |
| REST | `PATCH /3.0/alertsettings` |
| SOAP action | `https://api.exigo.com/UpdateAlertSettings` |
| WSDL elements | `UpdateAlertSettingsRequest` → `UpdateAlertSettingsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateAlertSettings |

#### Input

**`UpdateAlertSettingsRequest`**

| Property | Type | Notes |
|---|---|---|
| `DestinationID` | `Int32` |  |
| `AlertOptIn` | `Boolean` |  |
| `AlertEmails` | `String[]` |  |
| `AlertPhones` | `String[]` |  |

#### Output

**`UpdateAlertSettingsResponse`**

_No properties._

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/alertsettings HTTP/1.1
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
SOAPAction: "https://api.exigo.com/UpdateAlertSettings"

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
    <UpdateAlertSettingsRequest xmlns="http://api.exigo.com/">
      <DestinationID>int</DestinationID>
      <AlertOptIn>boolean</AlertOptIn>
      <AlertEmails>
        <string>string</string>
      </AlertEmails>
      <AlertPhones>
        <string>string</string>
      </AlertPhones>
    </UpdateAlertSettingsRequest>
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
    <UpdateAlertSettingsResult xmlns="http://api.exigo.com/" />
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
    var req = new UpdateAlertSettingsRequest();

    //Send Request to Server and Get Response
    var res = await api.UpdateAlertSettingsAsync(req);

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
    UpdateAlertSettingsRequest req = new UpdateAlertSettingsRequest();

    //Send Request to Server and Get Response
    UpdateAlertSettingsResponse res = api.UpdateAlertSettings(req);

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
    Dim req as new UpdateAlertSettingsRequest()

    'Send Request to Server and Get Response
    Dim res As UpdateAlertSettingsResponse = api.UpdateAlertSettings(req)

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
    $res = $api.UpdateAlertSettings($req);

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
    UpdateAlertSettingsRequest req = new UpdateAlertSettingsRequest();

    //Send Request to Server and Get Response
    UpdateAlertSettingsResponse res = api.getExigoApiSoap().updateAlertSettings(req, auth);

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

### GetExtendedDbSettings

> Gets settings for extended DB.

| | |
|---|---|
| Category | Sync |
| REST | `GET /3.0/extendeddbsettingsAuthorization:` |
| SOAP action | `https://api.exigo.com/GetExtendedDbSettings` |
| WSDL elements | `GetExtendedDbSettingsRequest` → `GetExtendedDbSettingsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetExtendedDbSettings |

#### Input

**`GetExtendedDbSettingsRequest`**

| Property | Type | Notes |
|---|---|---|
| `DestinationID` | `Int32` |  |

#### Output

**`GetExtendedDbSettingsResponse`**

| Property | Type | Notes |
|---|---|---|
| `ExcludedSchemas` | `String[]` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/extendeddbsettingsAuthorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "excludedSchemas": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetExtendedDbSettings"

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
    <GetExtendedDbSettingsRequest xmlns="http://api.exigo.com/">
      <DestinationID>int</DestinationID>
    </GetExtendedDbSettingsRequest>
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
    <GetExtendedDbSettingsResult xmlns="http://api.exigo.com/">
      <ExcludedSchemas>
        <string>string</string>
      </ExcludedSchemas>
    </GetExtendedDbSettingsResult>
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
    var req = new GetExtendedDbSettingsRequest();

    //Send Request to Server and Get Response
    var res = await api.GetExtendedDbSettingsAsync(req);

    //Now examine the results:

    foreach (var string  in res.ExcludedSchemas)
    {
        Console.WriteLine("Chars: {0}", string.Chars);
        Console.WriteLine("Length: {0}", string.Length);
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
    GetExtendedDbSettingsRequest req = new GetExtendedDbSettingsRequest();

    //Send Request to Server and Get Response
    GetExtendedDbSettingsResponse res = api.GetExtendedDbSettings(req);

    //Now examine the results:

    foreach (String string  in res.ExcludedSchemas)
    {
        Console.WriteLine("Chars: {0}", string.Chars);
        Console.WriteLine("Length: {0}", string.Length);
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
    Dim req as new GetExtendedDbSettingsRequest()

    'Send Request to Server and Get Response
    Dim res As GetExtendedDbSettingsResponse = api.GetExtendedDbSettings(req)

    'Now examine the results:

    For Each string As String In res.ExcludedSchemas
        Console.WriteLine("Chars: {0}", string.Chars)
        Console.WriteLine("Length: {0}", string.Length)
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
    $res = $api.GetExtendedDbSettings($req);

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
    GetExtendedDbSettingsRequest req = new GetExtendedDbSettingsRequest();

    //Send Request to Server and Get Response
    GetExtendedDbSettingsResponse res = api.getExigoApiSoap().getExtendedDbSettings(req, auth);

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

### UpdateExtendedDbSettings

> Updates settings for extended DB.

| | |
|---|---|
| Category | Sync |
| REST | `PATCH /3.0/extendeddbsettings` |
| SOAP action | `https://api.exigo.com/UpdateExtendedDbSettings` |
| WSDL elements | `UpdateExtendedDbSettingsRequest` → `UpdateExtendedDbSettingsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateExtendedDbSettings |

#### Input

**`UpdateExtendedDbSettingsRequest`**

| Property | Type | Notes |
|---|---|---|
| `DestinationID` | `Int32` |  |
| `ExcludedSchemas` | `String[]` |  |

#### Output

**`UpdateExtendedDbSettingsResponse`**

_No properties._

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/extendeddbsettings HTTP/1.1
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
SOAPAction: "https://api.exigo.com/UpdateExtendedDbSettings"

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
    <UpdateExtendedDbSettingsRequest xmlns="http://api.exigo.com/">
      <DestinationID>int</DestinationID>
      <ExcludedSchemas>
        <string>string</string>
      </ExcludedSchemas>
    </UpdateExtendedDbSettingsRequest>
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
    <UpdateExtendedDbSettingsResult xmlns="http://api.exigo.com/" />
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
    var req = new UpdateExtendedDbSettingsRequest();

    //Send Request to Server and Get Response
    var res = await api.UpdateExtendedDbSettingsAsync(req);

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
    UpdateExtendedDbSettingsRequest req = new UpdateExtendedDbSettingsRequest();

    //Send Request to Server and Get Response
    UpdateExtendedDbSettingsResponse res = api.UpdateExtendedDbSettings(req);

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
    Dim req as new UpdateExtendedDbSettingsRequest()

    'Send Request to Server and Get Response
    Dim res As UpdateExtendedDbSettingsResponse = api.UpdateExtendedDbSettings(req)

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
    $res = $api.UpdateExtendedDbSettings($req);

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
    UpdateExtendedDbSettingsRequest req = new UpdateExtendedDbSettingsRequest();

    //Send Request to Server and Get Response
    UpdateExtendedDbSettingsResponse res = api.getExigoApiSoap().updateExtendedDbSettings(req, auth);

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

### GetReIndexSettings

> Gets Re-Index settings.

| | |
|---|---|
| Category | Sync |
| REST | `GET /3.0/reindexsettingsAuthorization:` |
| SOAP action | `https://api.exigo.com/GetReIndexSettings` |
| WSDL elements | `GetReIndexSettingsRequest` → `GetReIndexSettingsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetReIndexSettings |

#### Input

**`GetReIndexSettingsRequest`**

| Property | Type | Notes |
|---|---|---|
| `DestinationID` | `Int32` |  |

#### Output

**`GetReIndexSettingsResponse`**

| Property | Type | Notes |
|---|---|---|
| `ReIndexStartTime` | `DateTime` |  |
| `ReIndexMaxDuration` | `Int32` |  |
| `LastReIndexed` | `DateTime` |  |
| `ReIndexError` | `String` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/reindexsettingsAuthorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "reIndexStartTime": "2026-11-10T00:00:00-06:00",
  "reIndexMaxDuration": 1,
  "lastReIndexed": "2026-11-10T00:00:00-06:00",
  "reIndexError": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetReIndexSettings"

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
    <GetReIndexSettingsRequest xmlns="http://api.exigo.com/">
      <DestinationID>int</DestinationID>
    </GetReIndexSettingsRequest>
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
    <GetReIndexSettingsResult xmlns="http://api.exigo.com/">
      <ReIndexStartTime>dateTime</ReIndexStartTime>
      <ReIndexMaxDuration>int</ReIndexMaxDuration>
      <LastReIndexed>dateTime</LastReIndexed>
      <ReIndexError>string</ReIndexError>
    </GetReIndexSettingsResult>
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
    var req = new GetReIndexSettingsRequest();

    //Send Request to Server and Get Response
    var res = await api.GetReIndexSettingsAsync(req);

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
    GetReIndexSettingsRequest req = new GetReIndexSettingsRequest();

    //Send Request to Server and Get Response
    GetReIndexSettingsResponse res = api.GetReIndexSettings(req);

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
    Dim req as new GetReIndexSettingsRequest()

    'Send Request to Server and Get Response
    Dim res As GetReIndexSettingsResponse = api.GetReIndexSettings(req)

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
    $res = $api.GetReIndexSettings($req);

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
    GetReIndexSettingsRequest req = new GetReIndexSettingsRequest();

    //Send Request to Server and Get Response
    GetReIndexSettingsResponse res = api.getExigoApiSoap().getReIndexSettings(req, auth);

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

### UpdateReIndexSettings

> Updates Re-Index settings.

| | |
|---|---|
| Category | Sync |
| REST | `PATCH /3.0/reindexsettings` |
| SOAP action | `https://api.exigo.com/UpdateReIndexSettings` |
| WSDL elements | `UpdateReIndexSettingsRequest` → `UpdateReIndexSettingsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateReIndexSettings |

#### Input

**`UpdateReIndexSettingsRequest`**

| Property | Type | Notes |
|---|---|---|
| `DestinationID` | `Int32` |  |
| `ReIndexStartTime` | `DateTime` | Optional. |
| `ReIndexMaxDuration` | `Int32` | Optional. |
| `LastReIndexed` | `DateTime` | Optional. |

#### Output

**`UpdateReIndexSettingsResponse`**

_No properties._

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/reindexsettings HTTP/1.1
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
SOAPAction: "https://api.exigo.com/UpdateReIndexSettings"

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
    <UpdateReIndexSettingsRequest xmlns="http://api.exigo.com/">
      <DestinationID>int</DestinationID>
      <ReIndexStartTime>dateTime</ReIndexStartTime>
      <ReIndexMaxDuration>int</ReIndexMaxDuration>
      <LastReIndexed>dateTime</LastReIndexed>
    </UpdateReIndexSettingsRequest>
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
    <UpdateReIndexSettingsResult xmlns="http://api.exigo.com/" />
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
    var req = new UpdateReIndexSettingsRequest();

    //Send Request to Server and Get Response
    var res = await api.UpdateReIndexSettingsAsync(req);

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
    UpdateReIndexSettingsRequest req = new UpdateReIndexSettingsRequest();

    //Send Request to Server and Get Response
    UpdateReIndexSettingsResponse res = api.UpdateReIndexSettings(req);

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
    Dim req as new UpdateReIndexSettingsRequest()

    'Send Request to Server and Get Response
    Dim res As UpdateReIndexSettingsResponse = api.UpdateReIndexSettings(req)

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
    $res = $api.UpdateReIndexSettings($req);

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
    UpdateReIndexSettingsRequest req = new UpdateReIndexSettingsRequest();

    //Send Request to Server and Get Response
    UpdateReIndexSettingsResponse res = api.getExigoApiSoap().updateReIndexSettings(req, auth);

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

### GetTableSettings

> Gets a table's settings.

| | |
|---|---|
| Category | Sync |
| REST | `GET /3.0/tablesettingsAuthorization:` |
| SOAP action | `https://api.exigo.com/GetTableSettings` |
| WSDL elements | `GetTableSettingsRequest` → `GetTableSettingsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetTableSettings |

#### Input

**`GetTableSettingsRequest`**

| Property | Type | Notes |
|---|---|---|
| `DestinationID` | `Int32` |  |

#### Output

**`GetTableSettingsResponse`**

| Property | Type | Notes |
|---|---|---|
| `TableSettings` | `TableSettings[]` |  |

**`TableSettings`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `SchemaName` | `String` |  |
| &nbsp;&nbsp;↳ `TableName` | `String` |  |
| &nbsp;&nbsp;↳ `IsMemoryOptimized` | `Boolean` |  |
| &nbsp;&nbsp;↳ `UseColumnStore` | `Boolean` |  |
| &nbsp;&nbsp;↳ `ModifiedDate` | `DateTime` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/tablesettingsAuthorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "tableSettings": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetTableSettings"

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
    <GetTableSettingsRequest xmlns="http://api.exigo.com/">
      <DestinationID>int</DestinationID>
    </GetTableSettingsRequest>
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
    <GetTableSettingsResult xmlns="http://api.exigo.com/">
      <TableSettings>
        <TableSettings>
          <SchemaName>string</SchemaName>
          <TableName>string</TableName>
          <IsMemoryOptimized>boolean</IsMemoryOptimized>
          <UseColumnStore>boolean</UseColumnStore>
          <ModifiedDate>dateTime</ModifiedDate>
        </TableSettings>
      </TableSettings>
    </GetTableSettingsResult>
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
    var req = new GetTableSettingsRequest();

    //Send Request to Server and Get Response
    var res = await api.GetTableSettingsAsync(req);

    //Now examine the results:

    foreach (var tableSettings  in res.TableSettings)
    {
        Console.WriteLine("SchemaName: {0}", tableSettings.SchemaName);
        Console.WriteLine("TableName: {0}", tableSettings.TableName);
        Console.WriteLine("IsMemoryOptimized: {0}", tableSettings.IsMemoryOptimized);
        Console.WriteLine("UseColumnStore: {0}", tableSettings.UseColumnStore);
        Console.WriteLine("ModifiedDate: {0}", tableSettings.ModifiedDate);
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
    GetTableSettingsRequest req = new GetTableSettingsRequest();

    //Send Request to Server and Get Response
    GetTableSettingsResponse res = api.GetTableSettings(req);

    //Now examine the results:

    foreach (TableSettings tableSettings  in res.TableSettings)
    {
        Console.WriteLine("SchemaName: {0}", tableSettings.SchemaName);
        Console.WriteLine("TableName: {0}", tableSettings.TableName);
        Console.WriteLine("IsMemoryOptimized: {0}", tableSettings.IsMemoryOptimized);
        Console.WriteLine("UseColumnStore: {0}", tableSettings.UseColumnStore);
        Console.WriteLine("ModifiedDate: {0}", tableSettings.ModifiedDate);
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
    Dim req as new GetTableSettingsRequest()

    'Send Request to Server and Get Response
    Dim res As GetTableSettingsResponse = api.GetTableSettings(req)

    'Now examine the results:

    For Each tableSettings As TableSettings In res.TableSettings
        Console.WriteLine("SchemaName: {0}", tableSettings.SchemaName)
        Console.WriteLine("TableName: {0}", tableSettings.TableName)
        Console.WriteLine("IsMemoryOptimized: {0}", tableSettings.IsMemoryOptimized)
        Console.WriteLine("UseColumnStore: {0}", tableSettings.UseColumnStore)
        Console.WriteLine("ModifiedDate: {0}", tableSettings.ModifiedDate)
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
    $res = $api.GetTableSettings($req);

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
    GetTableSettingsRequest req = new GetTableSettingsRequest();

    //Send Request to Server and Get Response
    GetTableSettingsResponse res = api.getExigoApiSoap().getTableSettings(req, auth);

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

### UpdateTableSettings

> Updates a table's settings.

| | |
|---|---|
| Category | Sync |
| REST | `PATCH /3.0/tablesettings` |
| SOAP action | `https://api.exigo.com/UpdateTableSettings` |
| WSDL elements | `UpdateTableSettingsRequest` → `UpdateTableSettingsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateTableSettings |

#### Input

**`UpdateTableSettingsRequest`**

| Property | Type | Notes |
|---|---|---|
| `DestinationID` | `Int32` |  |
| `SchemaName` | `String` | Optional. |
| `TableName` | `String` | Optional. |
| `IsMemoryOptimized` | `Boolean` |  |
| `UseColumnStore` | `Boolean` |  |

#### Output

**`UpdateTableSettingsResponse`**

_No properties._

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/tablesettings HTTP/1.1
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
SOAPAction: "https://api.exigo.com/UpdateTableSettings"

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
    <UpdateTableSettingsRequest xmlns="http://api.exigo.com/">
      <DestinationID>int</DestinationID>
      <SchemaName>string</SchemaName>
      <TableName>string</TableName>
      <IsMemoryOptimized>boolean</IsMemoryOptimized>
      <UseColumnStore>boolean</UseColumnStore>
    </UpdateTableSettingsRequest>
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
    <UpdateTableSettingsResult xmlns="http://api.exigo.com/" />
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
    var req = new UpdateTableSettingsRequest();

    //Send Request to Server and Get Response
    var res = await api.UpdateTableSettingsAsync(req);

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
    UpdateTableSettingsRequest req = new UpdateTableSettingsRequest();

    //Send Request to Server and Get Response
    UpdateTableSettingsResponse res = api.UpdateTableSettings(req);

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
    Dim req as new UpdateTableSettingsRequest()

    'Send Request to Server and Get Response
    Dim res As UpdateTableSettingsResponse = api.UpdateTableSettings(req)

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
    $res = $api.UpdateTableSettings($req);

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
    UpdateTableSettingsRequest req = new UpdateTableSettingsRequest();

    //Send Request to Server and Get Response
    UpdateTableSettingsResponse res = api.getExigoApiSoap().updateTableSettings(req, auth);

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

### GetReIndexHistory

> Gets ReIndexHistory.

| | |
|---|---|
| Category | Sync |
| REST | `GET /3.0/reindexsettings/history?destinationId=1` |
| SOAP action | `https://api.exigo.com/GetReIndexHistory` |
| WSDL elements | `GetReIndexHistoryRequest` → `GetReIndexHistoryResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetReIndexHistory |

#### Input

**`GetReIndexHistoryRequest`**

| Property | Type | Notes |
|---|---|---|
| `DestinationId` | `Int32` | Destination identifier. |
| `PageNumber` | `Int32` | The results are broken into 50 items per page. |

#### Output

**`GetReIndexHistoryResponse`**

| Property | Type | Notes |
|---|---|---|
| `ReIndexHistoryItems` | `ReIndexHistoryItem[]` |  |

**`ReIndexHistoryItem`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `TableName` | `String` |  |
| &nbsp;&nbsp;↳ `IndexName` | `String` |  |
| &nbsp;&nbsp;↳ `Fragmentation` | `Double` |  |
| &nbsp;&nbsp;↳ `PageCount` | `Int64` |  |
| &nbsp;&nbsp;↳ `StartDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `EndDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `ErrorMessage` | `String` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/reindexsettings/history?destinationId=1
  &pageNumber=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "reIndexHistoryItems": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetReIndexHistory"

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
    <GetReIndexHistoryRequest xmlns="http://api.exigo.com/">
      <DestinationId>int</DestinationId>
      <PageNumber>int</PageNumber>
    </GetReIndexHistoryRequest>
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
    <GetReIndexHistoryResult xmlns="http://api.exigo.com/">
      <ReIndexHistoryItems>
        <ReIndexHistoryItem>
          <TableName>string</TableName>
          <IndexName>string</IndexName>
          <Fragmentation>double</Fragmentation>
          <PageCount>long</PageCount>
          <StartDate>dateTime</StartDate>
          <EndDate>dateTime</EndDate>
          <ErrorMessage>string</ErrorMessage>
        </ReIndexHistoryItem>
      </ReIndexHistoryItems>
    </GetReIndexHistoryResult>
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
    var req = new GetReIndexHistoryRequest();

    req.DestinationId = 1;          //Destination identifier
    req.PageNumber = 1;             //The results are broken into 50 items per page.

    //Send Request to Server and Get Response
    var res = await api.GetReIndexHistoryAsync(req);

    //Now examine the results:

    foreach (var reIndexHistoryItem  in res.ReIndexHistoryItems)
    {
        Console.WriteLine("TableName: {0}", reIndexHistoryItem.TableName);
        Console.WriteLine("IndexName: {0}", reIndexHistoryItem.IndexName);
        Console.WriteLine("Fragmentation: {0}", reIndexHistoryItem.Fragmentation);
        Console.WriteLine("PageCount: {0}", reIndexHistoryItem.PageCount);
        Console.WriteLine("StartDate: {0}", reIndexHistoryItem.StartDate);
        Console.WriteLine("EndDate: {0}", reIndexHistoryItem.EndDate);
        Console.WriteLine("ErrorMessage: {0}", reIndexHistoryItem.ErrorMessage);
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
    GetReIndexHistoryRequest req = new GetReIndexHistoryRequest();

    req.DestinationId = 1;          //Destination identifier
    req.PageNumber = 1;             //The results are broken into 50 items per page.

    //Send Request to Server and Get Response
    GetReIndexHistoryResponse res = api.GetReIndexHistory(req);

    //Now examine the results:

    foreach (ReIndexHistoryItem reIndexHistoryItem  in res.ReIndexHistoryItems)
    {
        Console.WriteLine("TableName: {0}", reIndexHistoryItem.TableName);
        Console.WriteLine("IndexName: {0}", reIndexHistoryItem.IndexName);
        Console.WriteLine("Fragmentation: {0}", reIndexHistoryItem.Fragmentation);
        Console.WriteLine("PageCount: {0}", reIndexHistoryItem.PageCount);
        Console.WriteLine("StartDate: {0}", reIndexHistoryItem.StartDate);
        Console.WriteLine("EndDate: {0}", reIndexHistoryItem.EndDate);
        Console.WriteLine("ErrorMessage: {0}", reIndexHistoryItem.ErrorMessage);
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
    Dim req as new GetReIndexHistoryRequest()

    req.DestinationId = 1
    req.PageNumber = 1

    'Send Request to Server and Get Response
    Dim res As GetReIndexHistoryResponse = api.GetReIndexHistory(req)

    'Now examine the results:

    For Each reIndexHistoryItem As ReIndexHistoryItem In res.ReIndexHistoryItems
        Console.WriteLine("TableName: {0}", reIndexHistoryItem.TableName)
        Console.WriteLine("IndexName: {0}", reIndexHistoryItem.IndexName)
        Console.WriteLine("Fragmentation: {0}", reIndexHistoryItem.Fragmentation)
        Console.WriteLine("PageCount: {0}", reIndexHistoryItem.PageCount)
        Console.WriteLine("StartDate: {0}", reIndexHistoryItem.StartDate)
        Console.WriteLine("EndDate: {0}", reIndexHistoryItem.EndDate)
        Console.WriteLine("ErrorMessage: {0}", reIndexHistoryItem.ErrorMessage)
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

    $req->DestinationId = 1;
    $req->PageNumber = 1;

    //Send Request to Server and Get Response
    $res = $api.GetReIndexHistory($req);

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
    GetReIndexHistoryRequest req = new GetReIndexHistoryRequest();

    req.setDestinationId(1);
    req.setPageNumber(1);

    //Send Request to Server and Get Response
    GetReIndexHistoryResponse res = api.getExigoApiSoap().getReIndexHistory(req, auth);

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

### UpdateTableFilterSettings

> Updates Table Filter Settings.

| | |
|---|---|
| Category | Sync |
| REST | `PATCH /3.0/filtergroup/update` |
| SOAP action | `https://api.exigo.com/UpdateTableFilterSettings` |
| WSDL elements | `UpdateTableFilterSettingsRequest` → `UpdateTableFilterSettingsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateTableFilterSettings |

#### Input

**`UpdateTableFilterSettingsRequest`**

| Property | Type | Notes |
|---|---|---|
| `DestinationId` | `Int32` |  |
| `FilterGroupId` | `TableGroupID` | **Values:** `Misc`, `AutoOrder`, `Core`, `Commission`, `Customer`, `CustomersExtended`, `Item`, `Log`, `Messaging`, `Order`, `Payout`, `Tree`, `User`, `Image` |
| `ColumnName` | `String` | Optional. |
| `SchemaName` | `String` | Optional. |
| `TableName` | `String` | Optional. |
| `FilterValue` | `String` | Optional. |

#### Output

**`UpdateTableFilterSettingsResponse`**

_No properties._

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/filtergroup/update HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "destinationId": 1,
  "filterGroupId": null,
  "columnName": "1",
  "schemaName": "1",
  "tableName": "1",
  "filterValue": "1"
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
SOAPAction: "https://api.exigo.com/UpdateTableFilterSettings"

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
    <UpdateTableFilterSettingsRequest xmlns="http://api.exigo.com/">
      <DestinationId>int</DestinationId>
      <FilterGroupId>Misc or AutoOrder or Core or Commission or Customer or CustomersExtended or Item or Log or Messaging or Order or Payout or Tree or User or Image</FilterGroupId>
      <ColumnName>string</ColumnName>
      <SchemaName>string</SchemaName>
      <TableName>string</TableName>
      <FilterValue>string</FilterValue>
    </UpdateTableFilterSettingsRequest>
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
    <UpdateTableFilterSettingsResult xmlns="http://api.exigo.com/" />
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
    var req = new UpdateTableFilterSettingsRequest();

    req.DestinationId = 1;
    req.FilterGroupId = TableGroupID.Misc;
    req.ColumnName = "1";
    req.SchemaName = "1";
    req.TableName = "1";
    req.FilterValue = "1";

    //Send Request to Server and Get Response
    var res = await api.UpdateTableFilterSettingsAsync(req);

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
    UpdateTableFilterSettingsRequest req = new UpdateTableFilterSettingsRequest();

    req.DestinationId = 1;
    req.FilterGroupId = TableGroupID.Misc;
    req.ColumnName = "1";
    req.SchemaName = "1";
    req.TableName = "1";
    req.FilterValue = "1";

    //Send Request to Server and Get Response
    UpdateTableFilterSettingsResponse res = api.UpdateTableFilterSettings(req);

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
    Dim req as new UpdateTableFilterSettingsRequest()

    req.DestinationId = 1
    req.FilterGroupId = TableGroupID.Misc
    req.ColumnName = "1"
    req.SchemaName = "1"
    req.TableName = "1"
    req.FilterValue = "1"

    'Send Request to Server and Get Response
    Dim res As UpdateTableFilterSettingsResponse = api.UpdateTableFilterSettings(req)

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

    $req->DestinationId = 1;
    $req->FilterGroupId = 1;
    $req->ColumnName = "1";
    $req->SchemaName = "1";
    $req->TableName = "1";
    $req->FilterValue = "1";

    //Send Request to Server and Get Response
    $res = $api.UpdateTableFilterSettings($req);

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
    UpdateTableFilterSettingsRequest req = new UpdateTableFilterSettingsRequest();

    req.setDestinationId(1);
    req.setFilterGroupId(1);
    req.setColumnName("1");
    req.setSchemaName("1");
    req.setTableName("1");
    req.setFilterValue("1");

    //Send Request to Server and Get Response
    UpdateTableFilterSettingsResponse res = api.getExigoApiSoap().updateTableFilterSettings(req, auth);

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

### CreateTableFilterSettings

> Creates Table Filter Settings.

| | |
|---|---|
| Category | Sync |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/CreateTableFilterSettings` |
| WSDL elements | `CreateTableFilterSettingsRequest` → `CreateTableFilterSettingsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateTableFilterSettings |

#### Input

**`CreateTableFilterSettingsRequest`**

| Property | Type | Notes |
|---|---|---|
| `DestinationId` | `Int32` |  |
| `FilterGroupId` | `TableGroupID` | **Values:** `Misc`, `AutoOrder`, `Core`, `Commission`, `Customer`, `CustomersExtended`, `Item`, `Log`, `Messaging`, `Order`, `Payout`, `Tree`, `User`, `Image` |
| `ColumnName` | `String` | Optional. |
| `SchemaName` | `String` | Optional. |
| `TableName` | `String` | Optional. |
| `FilterValue` | `String` | Optional. |

#### Output

**`CreateTableFilterSettingsResponse`**

_No properties._

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateTableFilterSettings"

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
    <CreateTableFilterSettingsRequest xmlns="http://api.exigo.com/">
      <DestinationId>int</DestinationId>
      <FilterGroupId>Misc or AutoOrder or Core or Commission or Customer or CustomersExtended or Item or Log or Messaging or Order or Payout or Tree or User or Image</FilterGroupId>
      <ColumnName>string</ColumnName>
      <SchemaName>string</SchemaName>
      <TableName>string</TableName>
      <FilterValue>string</FilterValue>
    </CreateTableFilterSettingsRequest>
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
    <CreateTableFilterSettingsResult xmlns="http://api.exigo.com/" />
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
    var req = new CreateTableFilterSettingsRequest();

    req.DestinationId = 1;
    req.FilterGroupId = TableGroupID.Misc;
    req.ColumnName = "1";
    req.SchemaName = "1";
    req.TableName = "1";
    req.FilterValue = "1";

    //Send Request to Server and Get Response
    var res = await api.CreateTableFilterSettingsAsync(req);

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
    CreateTableFilterSettingsRequest req = new CreateTableFilterSettingsRequest();

    req.DestinationId = 1;
    req.FilterGroupId = TableGroupID.Misc;
    req.ColumnName = "1";
    req.SchemaName = "1";
    req.TableName = "1";
    req.FilterValue = "1";

    //Send Request to Server and Get Response
    CreateTableFilterSettingsResponse res = api.CreateTableFilterSettings(req);

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
    Dim req as new CreateTableFilterSettingsRequest()

    req.DestinationId = 1
    req.FilterGroupId = TableGroupID.Misc
    req.ColumnName = "1"
    req.SchemaName = "1"
    req.TableName = "1"
    req.FilterValue = "1"

    'Send Request to Server and Get Response
    Dim res As CreateTableFilterSettingsResponse = api.CreateTableFilterSettings(req)

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

    $req->DestinationId = 1;
    $req->FilterGroupId = 1;
    $req->ColumnName = "1";
    $req->SchemaName = "1";
    $req->TableName = "1";
    $req->FilterValue = "1";

    //Send Request to Server and Get Response
    $res = $api.CreateTableFilterSettings($req);

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
    CreateTableFilterSettingsRequest req = new CreateTableFilterSettingsRequest();

    req.setDestinationId(1);
    req.setFilterGroupId(1);
    req.setColumnName("1");
    req.setSchemaName("1");
    req.setTableName("1");
    req.setFilterValue("1");

    //Send Request to Server and Get Response
    CreateTableFilterSettingsResponse res = api.getExigoApiSoap().createTableFilterSettings(req, auth);

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

### SubmitDestinationTest

> Begins process for testing a conection.

| | |
|---|---|
| Category | Sync |
| REST | `POST /3.0/destination/submittest` |
| SOAP action | `https://api.exigo.com/SubmitDestinationTest` |
| WSDL elements | `SubmitDestinationTestRequest` → `SubmitDestinationTestResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=SubmitDestinationTest |

#### Input

**`SubmitDestinationTestRequest`**

| Property | Type | Notes |
|---|---|---|
| `ServerName` | `String` |  |
| `DatabaseName` | `String` |  |
| `UserId` | `String` |  |
| `Password` | `String` |  |

#### Output

**`SubmitDestinationTestResponse`**

| Property | Type | Notes |
|---|---|---|
| `RequestId` | `Guid` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/destination/submittest HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "serverName": "1",
  "databaseName": "1",
  "userId": "1",
  "password": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "requestId": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/SubmitDestinationTest"

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
    <SubmitDestinationTestRequest xmlns="http://api.exigo.com/">
      <ServerName>string</ServerName>
      <DatabaseName>string</DatabaseName>
      <UserId>string</UserId>
      <Password>string</Password>
    </SubmitDestinationTestRequest>
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
    <SubmitDestinationTestResult xmlns="http://api.exigo.com/">
      <RequestId>guid</RequestId>
    </SubmitDestinationTestResult>
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
    var req = new SubmitDestinationTestRequest();

    req.ServerName = "1";
    req.DatabaseName = "1";
    req.UserId = "1";
    req.Password = "1";

    //Send Request to Server and Get Response
    var res = await api.SubmitDestinationTestAsync(req);

    //Now examine the results:
    Console.WriteLine("RequestId: {0}", res.RequestId);
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
    SubmitDestinationTestRequest req = new SubmitDestinationTestRequest();

    req.ServerName = "1";
    req.DatabaseName = "1";
    req.UserId = "1";
    req.Password = "1";

    //Send Request to Server and Get Response
    SubmitDestinationTestResponse res = api.SubmitDestinationTest(req);

    //Now examine the results:
    Console.WriteLine("RequestId: {0}", res.RequestId);
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
    Dim req as new SubmitDestinationTestRequest()

    req.ServerName = "1"
    req.DatabaseName = "1"
    req.UserId = "1"
    req.Password = "1"

    'Send Request to Server and Get Response
    Dim res As SubmitDestinationTestResponse = api.SubmitDestinationTest(req)

    'Now examine the results:
    Console.WriteLine("RequestId: {0}", res.RequestId)
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

    $req->ServerName = "1";
    $req->DatabaseName = "1";
    $req->UserId = "1";
    $req->Password = "1";

    //Send Request to Server and Get Response
    $res = $api.SubmitDestinationTest($req);

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
    SubmitDestinationTestRequest req = new SubmitDestinationTestRequest();

    req.setServerName("1");
    req.setDatabaseName("1");
    req.setUserId("1");
    req.setPassword("1");

    //Send Request to Server and Get Response
    SubmitDestinationTestResponse res = api.getExigoApiSoap().submitDestinationTest(req, auth);

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

### GetDestinationTest

> Gets result for testing a conection.

| | |
|---|---|
| Category | Sync |
| REST | `GET /3.0/destination/gettest?requestId=1` |
| SOAP action | `https://api.exigo.com/GetDestinationTest` |
| WSDL elements | `GetDestinationTestRequest` → `GetDestinationTestResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetDestinationTest |

#### Input

**`GetDestinationTestRequest`**

| Property | Type | Notes |
|---|---|---|
| `RequestId` | `Guid` | The request id, from SubmitDestinationTest. |

#### Output

**`GetDestinationTestResponse`**

| Property | Type | Notes |
|---|---|---|
| `Success` | `Boolean` |  |
| `RequestId` | `Guid` |  |
| `Data` | `DestinationTestResponse` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/destination/gettest?requestId=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "success": true,
  "requestId": null,
  "data": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetDestinationTest"

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
    <GetDestinationTestRequest xmlns="http://api.exigo.com/">
      <RequestId>guid</RequestId>
    </GetDestinationTestRequest>
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
    <GetDestinationTestResult xmlns="http://api.exigo.com/">
      <Success>boolean</Success>
      <RequestId>guid</RequestId>
      <Data>
        <CompanyId>int</CompanyId>
        <RequestId>guid</RequestId>
        <RequestDate>dateTime</RequestDate>
        <RequestedBy>string</RequestedBy>
        <ProcessMachine>string</ProcessMachine>
        <ProcessDate>dateTime</ProcessDate>
        <CompleteDate>dateTime</CompleteDate>
        <Exception>string</Exception>
        <Details>
          <DestinationTestResponseDetail>
            <RequestId>guid</RequestId>
            <Success>boolean</Success>
            <Description>string</Description>
            <Exception>string</Exception>
          </DestinationTestResponseDetail>
        </Details>
      </Data>
    </GetDestinationTestResult>
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
    var req = new GetDestinationTestRequest();

    req.RequestId = 1;              //The request id, from SubmitDestinationTest

    //Send Request to Server and Get Response
    var res = await api.GetDestinationTestAsync(req);

    //Now examine the results:
    Console.WriteLine("Success: {0}", res.Success);
    Console.WriteLine("RequestId: {0}", res.RequestId);
    Console.WriteLine("Data: {0}", res.Data);
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
    GetDestinationTestRequest req = new GetDestinationTestRequest();

    req.RequestId = 1;              //The request id, from SubmitDestinationTest

    //Send Request to Server and Get Response
    GetDestinationTestResponse res = api.GetDestinationTest(req);

    //Now examine the results:
    Console.WriteLine("Success: {0}", res.Success);
    Console.WriteLine("RequestId: {0}", res.RequestId);
    Console.WriteLine("Data: {0}", res.Data);
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
    Dim req as new GetDestinationTestRequest()

    req.RequestId = 1

    'Send Request to Server and Get Response
    Dim res As GetDestinationTestResponse = api.GetDestinationTest(req)

    'Now examine the results:
    Console.WriteLine("Success: {0}", res.Success)
    Console.WriteLine("RequestId: {0}", res.RequestId)
    Console.WriteLine("Data: {0}", res.Data)
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

    $req->RequestId = 1;

    //Send Request to Server and Get Response
    $res = $api.GetDestinationTest($req);

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
    GetDestinationTestRequest req = new GetDestinationTestRequest();

    req.setRequestId(1);

    //Send Request to Server and Get Response
    GetDestinationTestResponse res = api.getExigoApiSoap().getDestinationTest(req, auth);

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
