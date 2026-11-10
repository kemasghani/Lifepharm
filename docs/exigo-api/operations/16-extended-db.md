# Exigo API — Extended DB

API version v2025.11.7.6. Crawled 2026-11-11 from https://api.exigo.com/3.0/. Back to [index](../README.md).

| Operation | REST | Summary |
|---|---|---|
| [CreateExtendedDbSchema](#createextendeddbschema) | `POST /3.0/extendeddb/schema` | Create new Extended DB schema. |
| [GetExtendedDbSchema](#getextendeddbschema) | `GET /3.0/extendeddb/schema?schemaName=1` | Get Extended DB schema. |
| [DeleteExtendedDbSchema](#deleteextendeddbschema) | `DELETE /3.0/extendeddb/schema` | Delete Extended DB schema. |
| [CreateExtendedDbEntity](#createextendeddbentity) | `POST /3.0/extendeddb` | Create Extended DB Entity. |
| [GetExtendedDbEntity](#getextendeddbentity) | `GET /3.0/extendeddb?schemaName=1` | Get Extended DB Entity. |
| [UpdateExtendedDbEntity](#updateextendeddbentity) | `PATCH /3.0/extendeddb` | Update Extended DB Entity. |
| [DeleteExtendedDbEntity](#deleteextendeddbentity) | `DELETE /3.0/extendeddb` | Delete Extended DB Entity. |

---
### CreateExtendedDbSchema

> Create new Extended DB schema.

| | |
|---|---|
| Category | Extended DB |
| REST | `POST /3.0/extendeddb/schema` |
| SOAP action | `https://api.exigo.com/CreateExtendedDbSchema` |
| WSDL elements | `CreateExtendedDbSchemaRequest` → `CreateExtendedDbSchemaResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateExtendedDbSchema |

#### Input

**`CreateExtendedDbSchemaRequest`**

| Property | Type | Notes |
|---|---|---|
| `SchemaName` | `String` |  |

#### Output

**`CreateExtendedDbSchemaResponse`**

_No properties._

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/extendeddb/schema HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "schemaName": "1"
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
SOAPAction: "https://api.exigo.com/CreateExtendedDbSchema"

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
    <CreateExtendedDbSchemaRequest xmlns="http://api.exigo.com/">
      <SchemaName>string</SchemaName>
    </CreateExtendedDbSchemaRequest>
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
    <CreateExtendedDbSchemaResult xmlns="http://api.exigo.com/" />
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
    var req = new CreateExtendedDbSchemaRequest();

    req.SchemaName = "1";

    //Send Request to Server and Get Response
    var res = await api.CreateExtendedDbSchemaAsync(req);

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
    CreateExtendedDbSchemaRequest req = new CreateExtendedDbSchemaRequest();

    req.SchemaName = "1";

    //Send Request to Server and Get Response
    CreateExtendedDbSchemaResponse res = api.CreateExtendedDbSchema(req);

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
    Dim req as new CreateExtendedDbSchemaRequest()

    req.SchemaName = "1"

    'Send Request to Server and Get Response
    Dim res As CreateExtendedDbSchemaResponse = api.CreateExtendedDbSchema(req)

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

    $req->SchemaName = "1";

    //Send Request to Server and Get Response
    $res = $api.CreateExtendedDbSchema($req);

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
    CreateExtendedDbSchemaRequest req = new CreateExtendedDbSchemaRequest();

    req.setSchemaName("1");

    //Send Request to Server and Get Response
    CreateExtendedDbSchemaResponse res = api.getExigoApiSoap().createExtendedDbSchema(req, auth);

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

### GetExtendedDbSchema

> Get Extended DB schema.

| | |
|---|---|
| Category | Extended DB |
| REST | `GET /3.0/extendeddb/schema?schemaName=1` |
| SOAP action | `https://api.exigo.com/GetExtendedDbSchema` |
| WSDL elements | `GetSchemaRequest` → `GetExtendedDbSchemaResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetExtendedDbSchema |

#### Input

**`GetSchemaRequest`**

| Property | Type | Notes |
|---|---|---|
| `SchemaName` | `String` |  |

#### Output

**`GetSchemaResponse`**

| Property | Type | Notes |
|---|---|---|
| `Schema` | `SchemaDataResponse` |  |

**`SchemaDataResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `Name` | `String` |  |
| &nbsp;&nbsp;↳ `Entities` | `EntityDataResponse[]` |  |

**`EntityDataResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `EntityName` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `EntitySetName` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `SchemaName` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `IsLog` | `Boolean` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `MaxLogDays` | `Int32` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `LogDateField` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Navigations` | `String[]` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Properties` | `PropertyDataResponse[]` |  |

**`PropertyDataResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ `PropertyName` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ `IsKey` | `Boolean` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ `IsNew` | `Boolean` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ `IsAutoNumber` | `Boolean` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ `AllowDbNull` | `Boolean` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ `Type` | `PropertyType` | **Values:** `Guid`, `DateTime2`, `Integer`, `Decimal`, `DateTime`, `Boolean`, `Binary`, `String`, `StringMax` |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ `DefaultValue` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ `Size` | `Int32` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ `MaskType` | `MaskTypeDataResponse` |  |

**`MaskTypeDataResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ `MaskTypeId` | `Int32` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ `Name` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ `Description` | `String` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/extendeddb/schema?schemaName=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "schema": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetExtendedDbSchema"

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
    <GetSchemaRequest xmlns="http://api.exigo.com/">
      <SchemaName>string</SchemaName>
    </GetSchemaRequest>
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
    <GetExtendedDbSchemaResult xmlns="http://api.exigo.com/">
      <Schema>
        <Name>string</Name>
        <Entities>
          <EntityDataResponse>
            <EntityName>string</EntityName>
            <EntitySetName>string</EntitySetName>
            <SchemaName>string</SchemaName>
            <IsLog>boolean</IsLog>
            <MaxLogDays>int</MaxLogDays>
            <LogDateField>string</LogDateField>
            <Navigations>
              <string>string</string>
            </Navigations>
            <Properties>
              <PropertyDataResponse
                xsi:nil="true" />
            </Properties>
          </EntityDataResponse>
        </Entities>
      </Schema>
    </GetExtendedDbSchemaResult>
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
    var req = new GetSchemaRequest();

    req.SchemaName = "1";

    //Send Request to Server and Get Response
    var res = await api.GetExtendedDbSchemaAsync(req);

    //Now examine the results:
    Console.WriteLine("Schema: {0}", res.Schema);
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
    GetSchemaRequest req = new GetSchemaRequest();

    req.SchemaName = "1";

    //Send Request to Server and Get Response
    GetSchemaResponse res = api.GetExtendedDbSchema(req);

    //Now examine the results:
    Console.WriteLine("Schema: {0}", res.Schema);
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
    Dim req as new GetSchemaRequest()

    req.SchemaName = "1"

    'Send Request to Server and Get Response
    Dim res As GetSchemaResponse = api.GetExtendedDbSchema(req)

    'Now examine the results:
    Console.WriteLine("Schema: {0}", res.Schema)
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

    $req->SchemaName = "1";

    //Send Request to Server and Get Response
    $res = $api.GetExtendedDbSchema($req);

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
    GetSchemaRequest req = new GetSchemaRequest();

    req.setSchemaName("1");

    //Send Request to Server and Get Response
    GetSchemaResponse res = api.getExigoApiSoap().getExtendedDbSchema(req, auth);

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

### DeleteExtendedDbSchema

> Delete Extended DB schema.

| | |
|---|---|
| Category | Extended DB |
| REST | `DELETE /3.0/extendeddb/schema` |
| SOAP action | `https://api.exigo.com/DeleteExtendedDbSchema` |
| WSDL elements | `DeleteSchemaRequest` → `DeleteExtendedDbSchemaResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DeleteExtendedDbSchema |

#### Input

**`DeleteSchemaRequest`**

| Property | Type | Notes |
|---|---|---|
| `SchemaName` | `String` |  |

#### Output

**`DeleteSchemaResponse`**

_No properties._

#### REST example

```http
DELETE https://yourcompany-api.exigo.com/3.0/extendeddb/schema HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "schemaName": "1"
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
SOAPAction: "https://api.exigo.com/DeleteExtendedDbSchema"

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
    <DeleteSchemaRequest xmlns="http://api.exigo.com/">
      <SchemaName>string</SchemaName>
    </DeleteSchemaRequest>
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
    <DeleteExtendedDbSchemaResult xmlns="http://api.exigo.com/" />
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
    var req = new DeleteSchemaRequest();

    req.SchemaName = "1";

    //Send Request to Server and Get Response
    var res = await api.DeleteExtendedDbSchemaAsync(req);

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
    DeleteSchemaRequest req = new DeleteSchemaRequest();

    req.SchemaName = "1";

    //Send Request to Server and Get Response
    DeleteSchemaResponse res = api.DeleteExtendedDbSchema(req);

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
    Dim req as new DeleteSchemaRequest()

    req.SchemaName = "1"

    'Send Request to Server and Get Response
    Dim res As DeleteSchemaResponse = api.DeleteExtendedDbSchema(req)

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

    $req->SchemaName = "1";

    //Send Request to Server and Get Response
    $res = $api.DeleteExtendedDbSchema($req);

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
    DeleteSchemaRequest req = new DeleteSchemaRequest();

    req.setSchemaName("1");

    //Send Request to Server and Get Response
    DeleteSchemaResponse res = api.getExigoApiSoap().deleteExtendedDbSchema(req, auth);

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

### CreateExtendedDbEntity

> Create Extended DB Entity.

| | |
|---|---|
| Category | Extended DB |
| REST | `POST /3.0/extendeddb` |
| SOAP action | `https://api.exigo.com/CreateExtendedDbEntity` |
| WSDL elements | `CreateEntityRequest` → `CreateExtendedDbEntityResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateExtendedDbEntity |

#### Input

**`CreateEntityRequest`**

| Property | Type | Notes |
|---|---|---|
| `EntityName` | `String` | An entity is a representational object of something in your database. Think of these as rows in a table in a SQL database. When naming your entities, we recommend you name your set as the singluar form of the name that best describes this object.<br>For example, if you are creating an entity that will represent a blog post in a blog, a good entity name would be BlogPost. |
| `EntitySetName` | `String` | An entity set is a collection of entities found in a schema. Think of them as tables in a SQL database. When naming your entity sets, we recommend you name your set as the plural form representing a collection of it's entities.<br>For example, if you are creating an entity set that will hold a collection of BlogPost entities, a good entity set name would be BlogPosts. |
| `SchemaName` | `String` |  |
| `IsLog` | `Boolean` |  |
| `MaxLogDays` | `Int32` |  |
| `LogDateField` | `String` | Optional. |
| `Navigations` | `String[]` | Optional. Relationships between tables in the same schema. |
| `Properties` | `PropertyDataRequest[]` |  |

**`PropertyDataRequest`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `PropertyName` | `String` |  |
| &nbsp;&nbsp;↳ `IsKey` | `Boolean` |  |
| &nbsp;&nbsp;↳ `IsNew` | `Boolean` |  |
| &nbsp;&nbsp;↳ `IsAutoNumber` | `Boolean` |  |
| &nbsp;&nbsp;↳ `AllowDbNull` | `Boolean` |  |
| &nbsp;&nbsp;↳ `Type` | `PropertyType` | **Values:** `Guid`, `DateTime2`, `Integer`, `Decimal`, `DateTime`, `Boolean`, `Binary`, `String`, `StringMax` |
| &nbsp;&nbsp;↳ `DefaultValue` | `String` | Optional. |
| &nbsp;&nbsp;↳ `Size` | `Int32` | Optional. Only required when PropertyType = String. |
| &nbsp;&nbsp;↳ `MaskTypeId` | `Int32` | Optional. Sandbox Data Masking is the process of masking data elements to the human eye in Sandbox Environments. The masking is primarily applied to PII (Personally Identifiable Information) fields as determined by Exigo, but is also user configurable for Extended Database Tables.<br> The process used by Exigo to perform this is via the Dynamic Data Masking feature of SQL Server.Therefore, the limitations of the feature, are subject to the constraints of SQL Server. |

#### Output

**`CreateEntityResponse`**

| Property | Type | Notes |
|---|---|---|
| `Entity` | `EntityDataResponse` |  |

**`EntityDataResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `EntityName` | `String` |  |
| &nbsp;&nbsp;↳ `EntitySetName` | `String` |  |
| &nbsp;&nbsp;↳ `SchemaName` | `String` |  |
| &nbsp;&nbsp;↳ `IsLog` | `Boolean` |  |
| &nbsp;&nbsp;↳ `MaxLogDays` | `Int32` |  |
| &nbsp;&nbsp;↳ `LogDateField` | `String` |  |
| &nbsp;&nbsp;↳ `Navigations` | `String[]` |  |
| &nbsp;&nbsp;↳ `Properties` | `PropertyDataResponse[]` |  |

**`PropertyDataResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `PropertyName` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `IsKey` | `Boolean` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `IsNew` | `Boolean` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `IsAutoNumber` | `Boolean` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `AllowDbNull` | `Boolean` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Type` | `PropertyType` | **Values:** `Guid`, `DateTime2`, `Integer`, `Decimal`, `DateTime`, `Boolean`, `Binary`, `String`, `StringMax` |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `DefaultValue` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Size` | `Int32` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `MaskType` | `MaskTypeDataResponse` |  |

**`MaskTypeDataResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ `MaskTypeId` | `Int32` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ `Name` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ `Description` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/extendeddb HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "entityName": "1",
  "entitySetName": "1",
  "schemaName": "1",
  "isLog": true,
  "maxLogDays": 1,
  "logDateField": "",
  "navigations": null,
  "properties": null
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "entity": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateExtendedDbEntity"

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
    <CreateEntityRequest xmlns="http://api.exigo.com/">
      <EntityName>string</EntityName>
      <EntitySetName>string</EntitySetName>
      <SchemaName>string</SchemaName>
      <IsLog>boolean</IsLog>
      <MaxLogDays>int</MaxLogDays>
      <LogDateField>string</LogDateField>
      <Navigations>
        <string>string</string>
      </Navigations>
      <Properties>
        <PropertyDataRequest>
          <PropertyName>string</PropertyName>
          <IsKey>boolean</IsKey>
          <IsNew>boolean</IsNew>
          <IsAutoNumber>boolean</IsAutoNumber>
          <AllowDbNull>boolean</AllowDbNull>
          <Type>Integer or DateTime2 or DateTime or Decimal or Boolean or String or StringMax or Binary or Guid</Type>
          <DefaultValue>string</DefaultValue>
          <Size>int</Size>
          <MaskTypeId>int</MaskTypeId>
        </PropertyDataRequest>
      </Properties>
    </CreateEntityRequest>
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
    <CreateExtendedDbEntityResult xmlns="http://api.exigo.com/">
      <Entity>
        <EntityName>string</EntityName>
        <EntitySetName>string</EntitySetName>
        <SchemaName>string</SchemaName>
        <IsLog>boolean</IsLog>
        <MaxLogDays>int</MaxLogDays>
        <LogDateField>string</LogDateField>
        <Navigations>
          <string>string</string>
        </Navigations>
        <Properties>
          <PropertyDataResponse>
            <PropertyName>string</PropertyName>
            <IsKey>boolean</IsKey>
            <IsNew>boolean</IsNew>
            <IsAutoNumber>boolean</IsAutoNumber>
            <AllowDbNull>boolean</AllowDbNull>
            <Type>Integer or DateTime2 or DateTime or Decimal or Boolean or String or StringMax or Binary or Guid</Type>
            <DefaultValue>string</DefaultValue>
            <Size>int</Size>
            <MaskType>
              <MaskTypeId>int</MaskTypeId>
              <Name>string</Name>
              <Description>string</Description>
            </MaskType>
          </PropertyDataResponse>
        </Properties>
      </Entity>
    </CreateExtendedDbEntityResult>
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
    var req = new CreateEntityRequest();

    req.EntityName = "1";           //An entity is a representational object of something in your database. Think of these as rows in a table in a SQL database. When naming your entities, we recommend you name your set as the singluar form of the name that best describes this object.
For example, if you are creating an entity that will represent a blog post in a blog, a good entity name would be BlogPost.
    req.EntitySetName = "1";        //An entity set is a collection of entities found in a schema. Think of them as tables in a SQL database. When naming your entity sets, we recommend you name your set as the plural form representing a collection of it's entities.
For example, if you are creating an entity set that will hold a collection of BlogPost entities, a good entity set name would be BlogPosts.
    req.SchemaName = "1";
    req.IsLog = true;
    req.MaxLogDays = 1;
    req.LogDateField = "1";

    //Add Navigations
    var navigations = new List<String>();
    navigations.Add("1");
    navigations.Add("2");

    //Now attach the list to the request
    req.Navigations = navigations.ToArray();

    //Add Properties
    var properties = new List<PropertyDataRequest>();

    var propertie1 = new PropertyDataRequest();
    propertie1.PropertyName = "1";
    propertie1.IsKey = true;
    propertie1.IsNew = true;
    propertie1.IsAutoNumber = true;
    propertie1.AllowDbNull = true;
    propertie1.Type = PropertyType.Guid;
    propertie1.DefaultValue = "1";
    propertie1.Size = 1;
    propertie1.MaskTypeId = 1;
    properties.Add(propertie1);

    var propertie2 = new PropertyDataRequest();
    propertie2.PropertyName = "2";
    propertie2.IsKey = true;
    propertie2.IsNew = true;
    propertie2.IsAutoNumber = true;
    propertie2.AllowDbNull = true;
    propertie2.Type = PropertyType.Guid;
    propertie2.DefaultValue = "2";
    propertie2.Size = 2;
    propertie2.MaskTypeId = 2;
    properties.Add(propertie2);

    //Now attach the list to the request
    req.Properties = properties.ToArray();

    //Send Request to Server and Get Response
    var res = await api.CreateExtendedDbEntityAsync(req);

    //Now examine the results:
    Console.WriteLine("Entity: {0}", res.Entity);
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
    CreateEntityRequest req = new CreateEntityRequest();

    req.EntityName = "1";           //An entity is a representational object of something in your database. Think of these as rows in a table in a SQL database. When naming your entities, we recommend you name your set as the singluar form of the name that best describes this object.
For example, if you are creating an entity that will represent a blog post in a blog, a good entity name would be BlogPost.
    req.EntitySetName = "1";        //An entity set is a collection of entities found in a schema. Think of them as tables in a SQL database. When naming your entity sets, we recommend you name your set as the plural form representing a collection of it's entities.
For example, if you are creating an entity set that will hold a collection of BlogPost entities, a good entity set name would be BlogPosts.
    req.SchemaName = "1";
    req.IsLog = true;
    req.MaxLogDays = 1;
    req.LogDateField = "1";

    //Add Navigations
    List<String> navigations = new List<String>();
    navigations.Add("1");
    navigations.Add("2");

    //Now attach the list to the request
    req.Navigations = navigations.ToArray();

    //Add Properties
    List<PropertyDataRequest> properties = new List<PropertyDataRequest>();

    PropertyDataRequest propertie1 = new PropertyDataRequest();
    propertie1.PropertyName = "1";
    propertie1.IsKey = true;
    propertie1.IsNew = true;
    propertie1.IsAutoNumber = true;
    propertie1.AllowDbNull = true;
    propertie1.Type = PropertyType.Guid;
    propertie1.DefaultValue = "1";
    propertie1.Size = 1;
    propertie1.MaskTypeId = 1;
    properties.Add(propertie1);

    PropertyDataRequest propertie2 = new PropertyDataRequest();
    propertie2.PropertyName = "2";
    propertie2.IsKey = true;
    propertie2.IsNew = true;
    propertie2.IsAutoNumber = true;
    propertie2.AllowDbNull = true;
    propertie2.Type = PropertyType.Guid;
    propertie2.DefaultValue = "2";
    propertie2.Size = 2;
    propertie2.MaskTypeId = 2;
    properties.Add(propertie2);

    //Now attach the list to the request
    req.Properties = properties.ToArray();

    //Send Request to Server and Get Response
    CreateEntityResponse res = api.CreateExtendedDbEntity(req);

    //Now examine the results:
    Console.WriteLine("Entity: {0}", res.Entity);
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
    Dim req as new CreateEntityRequest()

    req.EntityName = "1"
    req.EntitySetName = "1"
    req.SchemaName = "1"
    req.IsLog = true
    req.MaxLogDays = 1
    req.LogDateField = "1"

    'Add Navigations
    Dim navigations As New List(Of String)()
    navigations.Add("1")
    navigations.Add("2")

    'Now attach the list to the request
    req.Navigations = navigations.ToArray()

    'Add Properties
    Dim properties As New List(Of PropertyDataRequest)()

    Dim propertie1 as new PropertyDataRequest()
    propertie1.PropertyName = "1"
    propertie1.IsKey = true
    propertie1.IsNew = true
    propertie1.IsAutoNumber = true
    propertie1.AllowDbNull = true
    propertie1.Type = PropertyType.Guid
    propertie1.DefaultValue = "1"
    propertie1.Size = 1
    propertie1.MaskTypeId = 1
    properties.Add(propertie1)

    Dim propertie2 as new PropertyDataRequest()
    propertie2.PropertyName = "2"
    propertie2.IsKey = true
    propertie2.IsNew = true
    propertie2.IsAutoNumber = true
    propertie2.AllowDbNull = true
    propertie2.Type = PropertyType.Guid
    propertie2.DefaultValue = "2"
    propertie2.Size = 2
    propertie2.MaskTypeId = 2
    properties.Add(propertie2)

    'Now attach the list to the request
    req.Properties = properties.ToArray()

    'Send Request to Server and Get Response
    Dim res As CreateEntityResponse = api.CreateExtendedDbEntity(req)

    'Now examine the results:
    Console.WriteLine("Entity: {0}", res.Entity)
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

    $req->EntityName = "1";
    $req->EntitySetName = "1";
    $req->SchemaName = "1";
    $req->IsLog = 1;
    $req->MaxLogDays = 1;
    $req->LogDateField = "1";

    //Add Navigations

    $navigation1->Chars = 1;
    $navigation1->Length = 1;

    $navigation2->Chars = 2;
    $navigation2->Length = 2;

    //Now attach the list to the request
    req.Navigations = array(navigation1,navigation2);

    //Add Properties

    $propertie1->PropertyName = "1";
    $propertie1->IsKey = 1;
    $propertie1->IsNew = 1;
    $propertie1->IsAutoNumber = 1;
    $propertie1->AllowDbNull = 1;
    $propertie1->Type = 1;
    $propertie1->DefaultValue = "1";
    $propertie1->Size = 1;
    $propertie1->MaskTypeId = 1;

    $propertie2->PropertyName = "2";
    $propertie2->IsKey = 2;
    $propertie2->IsNew = 2;
    $propertie2->IsAutoNumber = 2;
    $propertie2->AllowDbNull = 2;
    $propertie2->Type = 2;
    $propertie2->DefaultValue = "2";
    $propertie2->Size = 2;
    $propertie2->MaskTypeId = 2;

    //Now attach the list to the request
    req.Properties = array(propertie1,propertie2);

    //Send Request to Server and Get Response
    $res = $api.CreateExtendedDbEntity($req);

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
    CreateEntityRequest req = new CreateEntityRequest();

    req.setEntityName("1");
    req.setEntitySetName("1");
    req.setSchemaName("1");
    req.setIsLog(1);
    req.setMaxLogDays(1);
    req.setLogDateField("1");

    //Add Navigations
    ArrayOfSystem.String navigations = new ArrayOfSystem.String();

    String navigation1 = new String();
    navigation1.setChars(1);
    navigation1.setLength(1);
    navigations.Add(navigation1);

    String navigation2 = new String();
    navigation2.setChars(2);
    navigation2.setLength(2);
    navigations.Add(navigation2);

    //Now attach the list to the request
    req.setNavigations(navigations);

    //Add Properties
    ArrayOfPropertyDataRequest properties = new ArrayOfPropertyDataRequest();

    PropertyDataRequest propertie1 = new PropertyDataRequest();
    propertie1.setPropertyName("1");
    propertie1.setIsKey(1);
    propertie1.setIsNew(1);
    propertie1.setIsAutoNumber(1);
    propertie1.setAllowDbNull(1);
    propertie1.setType(1);
    propertie1.setDefaultValue("1");
    propertie1.setSize(1);
    propertie1.setMaskTypeId(1);
    properties.Add(propertie1);

    PropertyDataRequest propertie2 = new PropertyDataRequest();
    propertie2.setPropertyName("2");
    propertie2.setIsKey(2);
    propertie2.setIsNew(2);
    propertie2.setIsAutoNumber(2);
    propertie2.setAllowDbNull(2);
    propertie2.setType(2);
    propertie2.setDefaultValue("2");
    propertie2.setSize(2);
    propertie2.setMaskTypeId(2);
    properties.Add(propertie2);

    //Now attach the list to the request
    req.setProperties(properties);

    //Send Request to Server and Get Response
    CreateEntityResponse res = api.getExigoApiSoap().createExtendedDbEntity(req, auth);

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

### GetExtendedDbEntity

> Get Extended DB Entity.

| | |
|---|---|
| Category | Extended DB |
| REST | `GET /3.0/extendeddb?schemaName=1` |
| SOAP action | `https://api.exigo.com/GetExtendedDbEntity` |
| WSDL elements | `GetEntityRequest` → `GetExtendedDbEntityResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetExtendedDbEntity |

#### Input

**`GetEntityRequest`**

| Property | Type | Notes |
|---|---|---|
| `SchemaName` | `String` |  |
| `EntityName` | `String` |  |

#### Output

**`GetEntityResponse`**

| Property | Type | Notes |
|---|---|---|
| `Entity` | `EntityDataResponse` |  |

**`EntityDataResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `EntityName` | `String` |  |
| &nbsp;&nbsp;↳ `EntitySetName` | `String` |  |
| &nbsp;&nbsp;↳ `SchemaName` | `String` |  |
| &nbsp;&nbsp;↳ `IsLog` | `Boolean` |  |
| &nbsp;&nbsp;↳ `MaxLogDays` | `Int32` |  |
| &nbsp;&nbsp;↳ `LogDateField` | `String` |  |
| &nbsp;&nbsp;↳ `Navigations` | `String[]` |  |
| &nbsp;&nbsp;↳ `Properties` | `PropertyDataResponse[]` |  |

**`PropertyDataResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `PropertyName` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `IsKey` | `Boolean` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `IsNew` | `Boolean` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `IsAutoNumber` | `Boolean` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `AllowDbNull` | `Boolean` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Type` | `PropertyType` | **Values:** `Guid`, `DateTime2`, `Integer`, `Decimal`, `DateTime`, `Boolean`, `Binary`, `String`, `StringMax` |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `DefaultValue` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Size` | `Int32` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `MaskType` | `MaskTypeDataResponse` |  |

**`MaskTypeDataResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ `MaskTypeId` | `Int32` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ `Name` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ `Description` | `String` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/extendeddb?schemaName=1
  &entityName=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "entity": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetExtendedDbEntity"

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
    <GetEntityRequest xmlns="http://api.exigo.com/">
      <SchemaName>string</SchemaName>
      <EntityName>string</EntityName>
    </GetEntityRequest>
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
    <GetExtendedDbEntityResult xmlns="http://api.exigo.com/">
      <Entity>
        <EntityName>string</EntityName>
        <EntitySetName>string</EntitySetName>
        <SchemaName>string</SchemaName>
        <IsLog>boolean</IsLog>
        <MaxLogDays>int</MaxLogDays>
        <LogDateField>string</LogDateField>
        <Navigations>
          <string>string</string>
        </Navigations>
        <Properties>
          <PropertyDataResponse>
            <PropertyName>string</PropertyName>
            <IsKey>boolean</IsKey>
            <IsNew>boolean</IsNew>
            <IsAutoNumber>boolean</IsAutoNumber>
            <AllowDbNull>boolean</AllowDbNull>
            <Type>Integer or DateTime2 or DateTime or Decimal or Boolean or String or StringMax or Binary or Guid</Type>
            <DefaultValue>string</DefaultValue>
            <Size>int</Size>
            <MaskType>
              <MaskTypeId>int</MaskTypeId>
              <Name>string</Name>
              <Description>string</Description>
            </MaskType>
          </PropertyDataResponse>
        </Properties>
      </Entity>
    </GetExtendedDbEntityResult>
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
    var req = new GetEntityRequest();

    req.SchemaName = "1";
    req.EntityName = "1";

    //Send Request to Server and Get Response
    var res = await api.GetExtendedDbEntityAsync(req);

    //Now examine the results:
    Console.WriteLine("Entity: {0}", res.Entity);
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
    GetEntityRequest req = new GetEntityRequest();

    req.SchemaName = "1";
    req.EntityName = "1";

    //Send Request to Server and Get Response
    GetEntityResponse res = api.GetExtendedDbEntity(req);

    //Now examine the results:
    Console.WriteLine("Entity: {0}", res.Entity);
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
    Dim req as new GetEntityRequest()

    req.SchemaName = "1"
    req.EntityName = "1"

    'Send Request to Server and Get Response
    Dim res As GetEntityResponse = api.GetExtendedDbEntity(req)

    'Now examine the results:
    Console.WriteLine("Entity: {0}", res.Entity)
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

    $req->SchemaName = "1";
    $req->EntityName = "1";

    //Send Request to Server and Get Response
    $res = $api.GetExtendedDbEntity($req);

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
    GetEntityRequest req = new GetEntityRequest();

    req.setSchemaName("1");
    req.setEntityName("1");

    //Send Request to Server and Get Response
    GetEntityResponse res = api.getExigoApiSoap().getExtendedDbEntity(req, auth);

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

### UpdateExtendedDbEntity

> Update Extended DB Entity.

| | |
|---|---|
| Category | Extended DB |
| REST | `PATCH /3.0/extendeddb` |
| SOAP action | `https://api.exigo.com/UpdateExtendedDbEntity` |
| WSDL elements | `UpdateEntityRequest` → `UpdateExtendedDbEntityResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateExtendedDbEntity |

#### Input

**`UpdateEntityRequest`**

| Property | Type | Notes |
|---|---|---|
| `EntityNameToUpdate` | `String` | Name of record to update. |
| `SchemaName` | `String` | Schema Name of the Entity that will be updated. |
| `NewEntityName` | `String` | An entity is a representational object of something in your database. Think of these as rows in a table in a SQL database. When naming your entities, we recommend you name your set as the singluar form of the name that best describes this object.<br>For example, if you are creating an entity that will represent a blog post in a blog, a good entity name would be BlogPost. |
| `NewEntitySetName` | `String` | An entity set is a collection of entities found in a schema. Think of them as tables in a SQL database. When naming your entity sets, we recommend you name your set as the plural form representing a collection of it's entities.<br>For example, if you are creating an entity set that will hold a collection of BlogPost entities, a good entity set name would be BlogPosts. |
| `NewIsLog` | `Boolean` | Optional. |
| `NewMaxLogDays` | `Int32` | Optional. |
| `NewLogDateField` | `String` | Optional. |
| `NewNavigations` | `String[]` | Relationships between tables in the same schema. |
| `NewProperties` | `PropertyDataRequest[]` | Optional. New properties that will be added. |
| `PropertiesToUpdate` | `PropertyDataUpdateRequest[]` | Optional. Properties that will be updated. |
| `PropertiesToDelete` | `String[]` | Optional. Name of the properties that will be deleted. |

**`PropertyDataRequest`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `PropertyName` | `String` |  |
| &nbsp;&nbsp;↳ `IsKey` | `Boolean` |  |
| &nbsp;&nbsp;↳ `IsNew` | `Boolean` |  |
| &nbsp;&nbsp;↳ `IsAutoNumber` | `Boolean` |  |
| &nbsp;&nbsp;↳ `AllowDbNull` | `Boolean` |  |
| &nbsp;&nbsp;↳ `Type` | `PropertyType` | **Values:** `Guid`, `DateTime2`, `Integer`, `Decimal`, `DateTime`, `Boolean`, `Binary`, `String`, `StringMax` |
| &nbsp;&nbsp;↳ `DefaultValue` | `String` | Optional. |
| &nbsp;&nbsp;↳ `Size` | `Int32` | Optional. Only required when PropertyType = String. |
| &nbsp;&nbsp;↳ `MaskTypeId` | `Int32` | Optional. Sandbox Data Masking is the process of masking data elements to the human eye in Sandbox Environments. The masking is primarily applied to PII (Personally Identifiable Information) fields as determined by Exigo, but is also user configurable for Extended Database Tables.<br> The process used by Exigo to perform this is via the Dynamic Data Masking feature of SQL Server.Therefore, the limitations of the feature, are subject to the constraints of SQL Server. |

**`PropertyDataUpdateRequest`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `PropertyName` | `String` |  |
| &nbsp;&nbsp;↳ `AllowDbNull` | `Boolean` |  |
| &nbsp;&nbsp;↳ `Size` | `Int32` | Optional. Only required when PropertyType = String. |
| &nbsp;&nbsp;↳ `MaskTypeId` | `Int32` | Optional. If you want to remove it, send 0. Sandbox Data Masking is the process of masking data elements to the human eye in Sandbox Environments. The masking is primarily applied to PII (Personally Identifiable Information) fields as determined by Exigo, but is also user configurable for Extended Database Tables.<br> The process used by Exigo to perform this is via the Dynamic Data Masking feature of SQL Server.Therefore, the limitations of the feature, are subject to the constraints of SQL Server. |

#### Output

**`UpdateEntityResponse`**

| Property | Type | Notes |
|---|---|---|
| `Entity` | `EntityDataResponse` |  |

**`EntityDataResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `EntityName` | `String` |  |
| &nbsp;&nbsp;↳ `EntitySetName` | `String` |  |
| &nbsp;&nbsp;↳ `SchemaName` | `String` |  |
| &nbsp;&nbsp;↳ `IsLog` | `Boolean` |  |
| &nbsp;&nbsp;↳ `MaxLogDays` | `Int32` |  |
| &nbsp;&nbsp;↳ `LogDateField` | `String` |  |
| &nbsp;&nbsp;↳ `Navigations` | `String[]` |  |
| &nbsp;&nbsp;↳ `Properties` | `PropertyDataResponse[]` |  |

**`PropertyDataResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `PropertyName` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `IsKey` | `Boolean` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `IsNew` | `Boolean` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `IsAutoNumber` | `Boolean` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `AllowDbNull` | `Boolean` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Type` | `PropertyType` | **Values:** `Guid`, `DateTime2`, `Integer`, `Decimal`, `DateTime`, `Boolean`, `Binary`, `String`, `StringMax` |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `DefaultValue` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Size` | `Int32` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `MaskType` | `MaskTypeDataResponse` |  |

**`MaskTypeDataResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ `MaskTypeId` | `Int32` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ `Name` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ `Description` | `String` |  |

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/extendeddb HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "entityNameToUpdate": "1",
  "schemaName": "1",
  "newEntityName": "1",
  "newEntitySetName": "1",
  "newIsLog": true,
  "newMaxLogDays": 1,
  "newLogDateField": "",
  "newNavigations": null,
  "newProperties": null,
  "propertiesToUpdate": null,
  "propertiesToDelete": null
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "entity": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/UpdateExtendedDbEntity"

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
    <UpdateEntityRequest xmlns="http://api.exigo.com/">
      <EntityNameToUpdate>string</EntityNameToUpdate>
      <SchemaName>string</SchemaName>
      <NewEntityName>string</NewEntityName>
      <NewEntitySetName>string</NewEntitySetName>
      <NewIsLog>boolean</NewIsLog>
      <NewMaxLogDays>int</NewMaxLogDays>
      <NewLogDateField>string</NewLogDateField>
      <NewNavigations>
        <string>string</string>
      </NewNavigations>
      <NewProperties>
        <PropertyDataRequest>
          <PropertyName>string</PropertyName>
          <IsKey>boolean</IsKey>
          <IsNew>boolean</IsNew>
          <IsAutoNumber>boolean</IsAutoNumber>
          <AllowDbNull>boolean</AllowDbNull>
          <Type>Integer or DateTime2 or DateTime or Decimal or Boolean or String or StringMax or Binary or Guid</Type>
          <DefaultValue>string</DefaultValue>
          <Size>int</Size>
          <MaskTypeId>int</MaskTypeId>
        </PropertyDataRequest>
      </NewProperties>
      <PropertiesToUpdate>
        <PropertyDataUpdateRequest>
          <PropertyName>string</PropertyName>
          <AllowDbNull>boolean</AllowDbNull>
          <Size>int</Size>
          <MaskTypeId>int</MaskTypeId>
        </PropertyDataUpdateRequest>
      </PropertiesToUpdate>
      <PropertiesToDelete>
        <string>string</string>
      </PropertiesToDelete>
    </UpdateEntityRequest>
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
    <UpdateExtendedDbEntityResult xmlns="http://api.exigo.com/">
      <Entity>
        <EntityName>string</EntityName>
        <EntitySetName>string</EntitySetName>
        <SchemaName>string</SchemaName>
        <IsLog>boolean</IsLog>
        <MaxLogDays>int</MaxLogDays>
        <LogDateField>string</LogDateField>
        <Navigations>
          <string>string</string>
        </Navigations>
        <Properties>
          <PropertyDataResponse>
            <PropertyName>string</PropertyName>
            <IsKey>boolean</IsKey>
            <IsNew>boolean</IsNew>
            <IsAutoNumber>boolean</IsAutoNumber>
            <AllowDbNull>boolean</AllowDbNull>
            <Type>Integer or DateTime2 or DateTime or Decimal or Boolean or String or StringMax or Binary or Guid</Type>
            <DefaultValue>string</DefaultValue>
            <Size>int</Size>
            <MaskType>
              <MaskTypeId>int</MaskTypeId>
              <Name>string</Name>
              <Description>string</Description>
            </MaskType>
          </PropertyDataResponse>
        </Properties>
      </Entity>
    </UpdateExtendedDbEntityResult>
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
    var req = new UpdateEntityRequest();

    req.EntityNameToUpdate = "1";   //Name of record to update.
    req.SchemaName = "1";           //Schema Name of the Entity that will be updated.
    req.NewEntityName = "1";        //An entity is a representational object of something in your database. Think of these as rows in a table in a SQL database. When naming your entities, we recommend you name your set as the singluar form of the name that best describes this object.
For example, if you are creating an entity that will represent a blog post in a blog, a good entity name would be BlogPost.
    req.NewEntitySetName = "1";     //An entity set is a collection of entities found in a schema. Think of them as tables in a SQL database. When naming your entity sets, we recommend you name your set as the plural form representing a collection of it's entities.
For example, if you are creating an entity set that will hold a collection of BlogPost entities, a good entity set name would be BlogPosts.
    req.NewIsLog = true;
    req.NewMaxLogDays = 1;
    req.NewLogDateField = "1";

    //Add NewNavigations
    var newnavigations = new List<String>();
    newnavigations.Add("1");
    newnavigations.Add("2");

    //Now attach the list to the request
    req.NewNavigations = newnavigations.ToArray();

    //Add NewProperties
    var newproperties = new List<PropertyDataRequest>();

    var newPropertie1 = new PropertyDataRequest();
    newPropertie1.PropertyName = "1";
    newPropertie1.IsKey = true;
    newPropertie1.IsNew = true;
    newPropertie1.IsAutoNumber = true;
    newPropertie1.AllowDbNull = true;
    newPropertie1.Type = PropertyType.Guid;
    newPropertie1.DefaultValue = "1";
    newPropertie1.Size = 1;
    newPropertie1.MaskTypeId = 1;
    newproperties.Add(newPropertie1);

    var newPropertie2 = new PropertyDataRequest();
    newPropertie2.PropertyName = "2";
    newPropertie2.IsKey = true;
    newPropertie2.IsNew = true;
    newPropertie2.IsAutoNumber = true;
    newPropertie2.AllowDbNull = true;
    newPropertie2.Type = PropertyType.Guid;
    newPropertie2.DefaultValue = "2";
    newPropertie2.Size = 2;
    newPropertie2.MaskTypeId = 2;
    newproperties.Add(newPropertie2);

    //Now attach the list to the request
    req.NewProperties = newproperties.ToArray();

    //Add PropertiesToUpdate
    var propertiestoupdate = new List<PropertyDataUpdateRequest>();

    var propertiesToUpdat1 = new PropertyDataUpdateRequest();
    propertiesToUpdat1.PropertyName = "1";
    propertiesToUpdat1.AllowDbNull = true;
    propertiesToUpdat1.Size = 1;
    propertiesToUpdat1.MaskTypeId = 1;
    propertiestoupdate.Add(propertiesToUpdat1);

    var propertiesToUpdat2 = new PropertyDataUpdateRequest();
    propertiesToUpdat2.PropertyName = "2";
    propertiesToUpdat2.AllowDbNull = true;
    propertiesToUpdat2.Size = 2;
    propertiesToUpdat2.MaskTypeId = 2;
    propertiestoupdate.Add(propertiesToUpdat2);

    //Now attach the list to the request
    req.PropertiesToUpdate = propertiestoupdate.ToArray();

    //Add PropertiesToDelete
    var propertiestodelete = new List<String>();
    propertiestodelete.Add("1");
    propertiestodelete.Add("2");

    //Now attach the list to the request
    req.PropertiesToDelete = propertiestodelete.ToArray();

    //Send Request to Server and Get Response
    var res = await api.UpdateExtendedDbEntityAsync(req);

    //Now examine the results:
    Console.WriteLine("Entity: {0}", res.Entity);
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
    UpdateEntityRequest req = new UpdateEntityRequest();

    req.EntityNameToUpdate = "1";   //Name of record to update.
    req.SchemaName = "1";           //Schema Name of the Entity that will be updated.
    req.NewEntityName = "1";        //An entity is a representational object of something in your database. Think of these as rows in a table in a SQL database. When naming your entities, we recommend you name your set as the singluar form of the name that best describes this object.
For example, if you are creating an entity that will represent a blog post in a blog, a good entity name would be BlogPost.
    req.NewEntitySetName = "1";     //An entity set is a collection of entities found in a schema. Think of them as tables in a SQL database. When naming your entity sets, we recommend you name your set as the plural form representing a collection of it's entities.
For example, if you are creating an entity set that will hold a collection of BlogPost entities, a good entity set name would be BlogPosts.
    req.NewIsLog = true;
    req.NewMaxLogDays = 1;
    req.NewLogDateField = "1";

    //Add NewNavigations
    List<String> newnavigations = new List<String>();
    newnavigations.Add("1");
    newnavigations.Add("2");

    //Now attach the list to the request
    req.NewNavigations = newnavigations.ToArray();

    //Add NewProperties
    List<PropertyDataRequest> newproperties = new List<PropertyDataRequest>();

    PropertyDataRequest newPropertie1 = new PropertyDataRequest();
    newPropertie1.PropertyName = "1";
    newPropertie1.IsKey = true;
    newPropertie1.IsNew = true;
    newPropertie1.IsAutoNumber = true;
    newPropertie1.AllowDbNull = true;
    newPropertie1.Type = PropertyType.Guid;
    newPropertie1.DefaultValue = "1";
    newPropertie1.Size = 1;
    newPropertie1.MaskTypeId = 1;
    newproperties.Add(newPropertie1);

    PropertyDataRequest newPropertie2 = new PropertyDataRequest();
    newPropertie2.PropertyName = "2";
    newPropertie2.IsKey = true;
    newPropertie2.IsNew = true;
    newPropertie2.IsAutoNumber = true;
    newPropertie2.AllowDbNull = true;
    newPropertie2.Type = PropertyType.Guid;
    newPropertie2.DefaultValue = "2";
    newPropertie2.Size = 2;
    newPropertie2.MaskTypeId = 2;
    newproperties.Add(newPropertie2);

    //Now attach the list to the request
    req.NewProperties = newproperties.ToArray();

    //Add PropertiesToUpdate
    List<PropertyDataUpdateRequest> propertiestoupdate = new List<PropertyDataUpdateRequest>();

    PropertyDataUpdateRequest propertiesToUpdat1 = new PropertyDataUpdateRequest();
    propertiesToUpdat1.PropertyName = "1";
    propertiesToUpdat1.AllowDbNull = true;
    propertiesToUpdat1.Size = 1;
    propertiesToUpdat1.MaskTypeId = 1;
    propertiestoupdate.Add(propertiesToUpdat1);

    PropertyDataUpdateRequest propertiesToUpdat2 = new PropertyDataUpdateRequest();
    propertiesToUpdat2.PropertyName = "2";
    propertiesToUpdat2.AllowDbNull = true;
    propertiesToUpdat2.Size = 2;
    propertiesToUpdat2.MaskTypeId = 2;
    propertiestoupdate.Add(propertiesToUpdat2);

    //Now attach the list to the request
    req.PropertiesToUpdate = propertiestoupdate.ToArray();

    //Add PropertiesToDelete
    List<String> propertiestodelete = new List<String>();
    propertiestodelete.Add("1");
    propertiestodelete.Add("2");

    //Now attach the list to the request
    req.PropertiesToDelete = propertiestodelete.ToArray();

    //Send Request to Server and Get Response
    UpdateEntityResponse res = api.UpdateExtendedDbEntity(req);

    //Now examine the results:
    Console.WriteLine("Entity: {0}", res.Entity);
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
    Dim req as new UpdateEntityRequest()

    req.EntityNameToUpdate = "1"
    req.SchemaName = "1"
    req.NewEntityName = "1"
    req.NewEntitySetName = "1"
    req.NewIsLog = true
    req.NewMaxLogDays = 1
    req.NewLogDateField = "1"

    'Add NewNavigations
    Dim newnavigations As New List(Of String)()
    newnavigations.Add("1")
    newnavigations.Add("2")

    'Now attach the list to the request
    req.NewNavigations = newnavigations.ToArray()

    'Add NewProperties
    Dim newproperties As New List(Of PropertyDataRequest)()

    Dim newPropertie1 as new PropertyDataRequest()
    newPropertie1.PropertyName = "1"
    newPropertie1.IsKey = true
    newPropertie1.IsNew = true
    newPropertie1.IsAutoNumber = true
    newPropertie1.AllowDbNull = true
    newPropertie1.Type = PropertyType.Guid
    newPropertie1.DefaultValue = "1"
    newPropertie1.Size = 1
    newPropertie1.MaskTypeId = 1
    newproperties.Add(newPropertie1)

    Dim newPropertie2 as new PropertyDataRequest()
    newPropertie2.PropertyName = "2"
    newPropertie2.IsKey = true
    newPropertie2.IsNew = true
    newPropertie2.IsAutoNumber = true
    newPropertie2.AllowDbNull = true
    newPropertie2.Type = PropertyType.Guid
    newPropertie2.DefaultValue = "2"
    newPropertie2.Size = 2
    newPropertie2.MaskTypeId = 2
    newproperties.Add(newPropertie2)

    'Now attach the list to the request
    req.NewProperties = newproperties.ToArray()

    'Add PropertiesToUpdate
    Dim propertiestoupdate As New List(Of PropertyDataUpdateRequest)()

    Dim propertiesToUpdat1 as new PropertyDataUpdateRequest()
    propertiesToUpdat1.PropertyName = "1"
    propertiesToUpdat1.AllowDbNull = true
    propertiesToUpdat1.Size = 1
    propertiesToUpdat1.MaskTypeId = 1
    propertiestoupdate.Add(propertiesToUpdat1)

    Dim propertiesToUpdat2 as new PropertyDataUpdateRequest()
    propertiesToUpdat2.PropertyName = "2"
    propertiesToUpdat2.AllowDbNull = true
    propertiesToUpdat2.Size = 2
    propertiesToUpdat2.MaskTypeId = 2
    propertiestoupdate.Add(propertiesToUpdat2)

    'Now attach the list to the request
    req.PropertiesToUpdate = propertiestoupdate.ToArray()

    'Add PropertiesToDelete
    Dim propertiestodelete As New List(Of String)()
    propertiestodelete.Add("1")
    propertiestodelete.Add("2")

    'Now attach the list to the request
    req.PropertiesToDelete = propertiestodelete.ToArray()

    'Send Request to Server and Get Response
    Dim res As UpdateEntityResponse = api.UpdateExtendedDbEntity(req)

    'Now examine the results:
    Console.WriteLine("Entity: {0}", res.Entity)
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

    $req->EntityNameToUpdate = "1";
    $req->SchemaName = "1";
    $req->NewEntityName = "1";
    $req->NewEntitySetName = "1";
    $req->NewIsLog = 1;
    $req->NewMaxLogDays = 1;
    $req->NewLogDateField = "1";

    //Add NewNavigations

    $newNavigation1->Chars = 1;
    $newNavigation1->Length = 1;

    $newNavigation2->Chars = 2;
    $newNavigation2->Length = 2;

    //Now attach the list to the request
    req.NewNavigations = array(newNavigation1,newNavigation2);

    //Add NewProperties

    $newPropertie1->PropertyName = "1";
    $newPropertie1->IsKey = 1;
    $newPropertie1->IsNew = 1;
    $newPropertie1->IsAutoNumber = 1;
    $newPropertie1->AllowDbNull = 1;
    $newPropertie1->Type = 1;
    $newPropertie1->DefaultValue = "1";
    $newPropertie1->Size = 1;
    $newPropertie1->MaskTypeId = 1;

    $newPropertie2->PropertyName = "2";
    $newPropertie2->IsKey = 2;
    $newPropertie2->IsNew = 2;
    $newPropertie2->IsAutoNumber = 2;
    $newPropertie2->AllowDbNull = 2;
    $newPropertie2->Type = 2;
    $newPropertie2->DefaultValue = "2";
    $newPropertie2->Size = 2;
    $newPropertie2->MaskTypeId = 2;

    //Now attach the list to the request
    req.NewProperties = array(newPropertie1,newPropertie2);

    //Add PropertiesToUpdate

    $propertiesToUpdat1->PropertyName = "1";
    $propertiesToUpdat1->AllowDbNull = 1;
    $propertiesToUpdat1->Size = 1;
    $propertiesToUpdat1->MaskTypeId = 1;

    $propertiesToUpdat2->PropertyName = "2";
    $propertiesToUpdat2->AllowDbNull = 2;
    $propertiesToUpdat2->Size = 2;
    $propertiesToUpdat2->MaskTypeId = 2;

    //Now attach the list to the request
    req.PropertiesToUpdate = array(propertiesToUpdat1,propertiesToUpdat2);

    //Add PropertiesToDelete

    $propertiesToDelet1->Chars = 1;
    $propertiesToDelet1->Length = 1;

    $propertiesToDelet2->Chars = 2;
    $propertiesToDelet2->Length = 2;

    //Now attach the list to the request
    req.PropertiesToDelete = array(propertiesToDelet1,propertiesToDelet2);

    //Send Request to Server and Get Response
    $res = $api.UpdateExtendedDbEntity($req);

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
    UpdateEntityRequest req = new UpdateEntityRequest();

    req.setEntityNameToUpdate("1");
    req.setSchemaName("1");
    req.setNewEntityName("1");
    req.setNewEntitySetName("1");
    req.setNewIsLog(1);
    req.setNewMaxLogDays(1);
    req.setNewLogDateField("1");

    //Add NewNavigations
    ArrayOfSystem.String newnavigations = new ArrayOfSystem.String();

    String newNavigation1 = new String();
    newNavigation1.setChars(1);
    newNavigation1.setLength(1);
    newnavigations.Add(newNavigation1);

    String newNavigation2 = new String();
    newNavigation2.setChars(2);
    newNavigation2.setLength(2);
    newnavigations.Add(newNavigation2);

    //Now attach the list to the request
    req.setNewNavigations(newnavigations);

    //Add NewProperties
    ArrayOfPropertyDataRequest newproperties = new ArrayOfPropertyDataRequest();

    PropertyDataRequest newPropertie1 = new PropertyDataRequest();
    newPropertie1.setPropertyName("1");
    newPropertie1.setIsKey(1);
    newPropertie1.setIsNew(1);
    newPropertie1.setIsAutoNumber(1);
    newPropertie1.setAllowDbNull(1);
    newPropertie1.setType(1);
    newPropertie1.setDefaultValue("1");
    newPropertie1.setSize(1);
    newPropertie1.setMaskTypeId(1);
    newproperties.Add(newPropertie1);

    PropertyDataRequest newPropertie2 = new PropertyDataRequest();
    newPropertie2.setPropertyName("2");
    newPropertie2.setIsKey(2);
    newPropertie2.setIsNew(2);
    newPropertie2.setIsAutoNumber(2);
    newPropertie2.setAllowDbNull(2);
    newPropertie2.setType(2);
    newPropertie2.setDefaultValue("2");
    newPropertie2.setSize(2);
    newPropertie2.setMaskTypeId(2);
    newproperties.Add(newPropertie2);

    //Now attach the list to the request
    req.setNewProperties(newproperties);

    //Add PropertiesToUpdate
    ArrayOfPropertyDataUpdateRequest propertiestoupdate = new ArrayOfPropertyDataUpdateRequest();

    PropertyDataUpdateRequest propertiesToUpdat1 = new PropertyDataUpdateRequest();
    propertiesToUpdat1.setPropertyName("1");
    propertiesToUpdat1.setAllowDbNull(1);
    propertiesToUpdat1.setSize(1);
    propertiesToUpdat1.setMaskTypeId(1);
    propertiestoupdate.Add(propertiesToUpdat1);

    PropertyDataUpdateRequest propertiesToUpdat2 = new PropertyDataUpdateRequest();
    propertiesToUpdat2.setPropertyName("2");
    propertiesToUpdat2.setAllowDbNull(2);
    propertiesToUpdat2.setSize(2);
    propertiesToUpdat2.setMaskTypeId(2);
    propertiestoupdate.Add(propertiesToUpdat2);

    //Now attach the list to the request
    req.setPropertiesToUpdate(propertiestoupdate);

    //Add PropertiesToDelete
    ArrayOfSystem.String propertiestodelete = new ArrayOfSystem.String();

    String propertiesToDelet1 = new String();
    propertiesToDelet1.setChars(1);
    propertiesToDelet1.setLength(1);
    propertiestodelete.Add(propertiesToDelet1);

    String propertiesToDelet2 = new String();
    propertiesToDelet2.setChars(2);
    propertiesToDelet2.setLength(2);
    propertiestodelete.Add(propertiesToDelet2);

    //Now attach the list to the request
    req.setPropertiesToDelete(propertiestodelete);

    //Send Request to Server and Get Response
    UpdateEntityResponse res = api.getExigoApiSoap().updateExtendedDbEntity(req, auth);

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

### DeleteExtendedDbEntity

> Delete Extended DB Entity.

| | |
|---|---|
| Category | Extended DB |
| REST | `DELETE /3.0/extendeddb` |
| SOAP action | `https://api.exigo.com/DeleteExtendedDbEntity` |
| WSDL elements | `DeleteEntityRequest` → `DeleteExtendedDbEntityResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DeleteExtendedDbEntity |

#### Input

**`DeleteEntityRequest`**

| Property | Type | Notes |
|---|---|---|
| `SchemaName` | `String` |  |
| `EntityName` | `String` |  |

#### Output

**`DeleteEntityResponse`**

_No properties._

#### REST example

```http
DELETE https://yourcompany-api.exigo.com/3.0/extendeddb HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "schemaName": "1",
  "entityName": "1"
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
SOAPAction: "https://api.exigo.com/DeleteExtendedDbEntity"

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
    <DeleteEntityRequest xmlns="http://api.exigo.com/">
      <SchemaName>string</SchemaName>
      <EntityName>string</EntityName>
    </DeleteEntityRequest>
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
    <DeleteExtendedDbEntityResult xmlns="http://api.exigo.com/" />
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
    var req = new DeleteEntityRequest();

    req.SchemaName = "1";
    req.EntityName = "1";

    //Send Request to Server and Get Response
    var res = await api.DeleteExtendedDbEntityAsync(req);

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
    DeleteEntityRequest req = new DeleteEntityRequest();

    req.SchemaName = "1";
    req.EntityName = "1";

    //Send Request to Server and Get Response
    DeleteEntityResponse res = api.DeleteExtendedDbEntity(req);

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
    Dim req as new DeleteEntityRequest()

    req.SchemaName = "1"
    req.EntityName = "1"

    'Send Request to Server and Get Response
    Dim res As DeleteEntityResponse = api.DeleteExtendedDbEntity(req)

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

    $req->SchemaName = "1";
    $req->EntityName = "1";

    //Send Request to Server and Get Response
    $res = $api.DeleteExtendedDbEntity($req);

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
    DeleteEntityRequest req = new DeleteEntityRequest();

    req.setSchemaName("1");
    req.setEntityName("1");

    //Send Request to Server and Get Response
    DeleteEntityResponse res = api.getExigoApiSoap().deleteExtendedDbEntity(req, auth);

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
