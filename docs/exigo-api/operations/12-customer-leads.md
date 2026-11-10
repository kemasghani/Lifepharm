# Exigo API — Customer Leads

API version v2025.11.7.6. Crawled 2026-11-11 from https://api.exigo.com/3.0/. Back to [index](../README.md).

| Operation | REST | Summary |
|---|---|---|
| [GetCustomerLeads](#getcustomerleads) | `GET /3.0/customerlead?customerID=1` | Gets a list of customer leads. |
| [CreateCustomerLead](#createcustomerlead) | `POST /3.0/customerlead` | Creates a new customer lead. Note: This request can participate in a transaction. Learn more about transactions. |
| [UpdateCustomerLead](#updatecustomerlead) | `PATCH /3.0/customerlead` | Updates a customer leads. Note: This request can participate in a transaction. Learn more about transactions. |
| [DeleteCustomerLead](#deletecustomerlead) | `DELETE /3.0/customerlead` | Deletes a customer lead. |
| [SetCustomerLeadSocialNetworks](#setcustomerleadsocialnetworks) | `PUT /3.0/customerlead/socialnetworks` | Deletes all existing social network(s) for the customer lead, then inserts the provided list of social network(s) for the customer lead. Note: This request can participate in a… |
| [GetCustomerLeadSocialNetworks](#getcustomerleadsocialnetworks) | `GET /3.0/customerlead/socialnetworks?customerID=1` | Returns a list of social network(s) for the customer lead. |

---
### GetCustomerLeads

> Gets a list of customer leads.

| | |
|---|---|
| Category | Customer Leads |
| REST | `GET /3.0/customerlead?customerID=1` |
| SOAP action | `https://api.exigo.com/GetCustomerLeads` |
| WSDL elements | `GetCustomerLeadsRequest` → `GetCustomerLeadsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetCustomerLeads |

#### Input

**`GetCustomerLeadsRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerLeadID` | `Int32` | Optional. Optionally pull just one customer lead by ID. |
| `GreaterThanCustomerLeadID` | `Int32` | Optional. Paging controller. |
| `BatchSize` | `Int32` | Optional. Defaults to 100 at a time. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`GetCustomerLeadsResponse`**

| Property | Type | Notes |
|---|---|---|
| `CustomerLeads` | `CustomerLeadsResponse[]` |  |

**`CustomerLeadsResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| &nbsp;&nbsp;↳ `CustomerLeadID` | `Int32` | Unique identifier for a customer lead record. |
| &nbsp;&nbsp;↳ `FirstName` | `String` |  |
| &nbsp;&nbsp;↳ `LastName` | `String` |  |
| &nbsp;&nbsp;↳ `MiddleName` | `String` |  |
| &nbsp;&nbsp;↳ `Company` | `String` |  |
| &nbsp;&nbsp;↳ `Phone` | `String` |  |
| &nbsp;&nbsp;↳ `Phone2` | `String` |  |
| &nbsp;&nbsp;↳ `MobilePhone` | `String` |  |
| &nbsp;&nbsp;↳ `Fax` | `String` |  |
| &nbsp;&nbsp;↳ `Email` | `String` |  |
| &nbsp;&nbsp;↳ `Address1` | `String` |  |
| &nbsp;&nbsp;↳ `Address2` | `String` |  |
| &nbsp;&nbsp;↳ `City` | `String` |  |
| &nbsp;&nbsp;↳ `State` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Zip` | `String` |  |
| &nbsp;&nbsp;↳ `Country` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `BirthDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `Notes` | `String` |  |
| &nbsp;&nbsp;↳ `CustomerKey` | `String` | Unique alpha numeric identifier for customer record . |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/customerlead?customerID=1
  &customerLeadID=1
  &greaterThanCustomerLeadID=1
  &batchSize=1
  &customerKey=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "customerLeads": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetCustomerLeads"

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
    <GetCustomerLeadsRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerLeadID>int</CustomerLeadID>
      <GreaterThanCustomerLeadID>int</GreaterThanCustomerLeadID>
      <BatchSize>int</BatchSize>
      <CustomerKey>string</CustomerKey>
    </GetCustomerLeadsRequest>
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
    <GetCustomerLeadsResult xmlns="http://api.exigo.com/">
      <CustomerLeads>
        <CustomerLeadsResponse>
          <CustomerID>int</CustomerID>
          <CustomerLeadID>int</CustomerLeadID>
          <FirstName>string</FirstName>
          <LastName>string</LastName>
          <MiddleName>string</MiddleName>
          <Company>string</Company>
          <Phone>string</Phone>
          <Phone2>string</Phone2>
          <MobilePhone>string</MobilePhone>
          <Fax>string</Fax>
          <Email>string</Email>
          <Address1>string</Address1>
          <Address2>string</Address2>
          <City>string</City>
          <State>string</State>
          <Zip>string</Zip>
          <Country>string</Country>
          <BirthDate>dateTime</BirthDate>
          <Notes>string</Notes>
          <CustomerKey>string</CustomerKey>
        </CustomerLeadsResponse>
      </CustomerLeads>
    </GetCustomerLeadsResult>
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
    var req = new GetCustomerLeadsRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerLeadID = 1;         //Optionally pull just one customer lead by ID
    req.GreaterThanCustomerLeadID = 1;//Paging controller
    req.BatchSize = 1;              //Defaults to 100 at a time
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.GetCustomerLeadsAsync(req);

    //Now examine the results:

    foreach (var customerLeads  in res.CustomerLeads)
    {
        Console.WriteLine("CustomerID: {0}", customerLeads.CustomerID);
        Console.WriteLine("CustomerLeadID: {0}", customerLeads.CustomerLeadID);
        Console.WriteLine("FirstName: {0}", customerLeads.FirstName);
        Console.WriteLine("LastName: {0}", customerLeads.LastName);
        Console.WriteLine("MiddleName: {0}", customerLeads.MiddleName);
        Console.WriteLine("Company: {0}", customerLeads.Company);
        Console.WriteLine("Phone: {0}", customerLeads.Phone);
        Console.WriteLine("Phone2: {0}", customerLeads.Phone2);
        Console.WriteLine("MobilePhone: {0}", customerLeads.MobilePhone);
        Console.WriteLine("Fax: {0}", customerLeads.Fax);
        Console.WriteLine("Email: {0}", customerLeads.Email);
        Console.WriteLine("Address1: {0}", customerLeads.Address1);
        Console.WriteLine("Address2: {0}", customerLeads.Address2);
        Console.WriteLine("City: {0}", customerLeads.City);
        Console.WriteLine("Zip: {0}", customerLeads.Zip);
        Console.WriteLine("BirthDate: {0}", customerLeads.BirthDate);
        Console.WriteLine("Notes: {0}", customerLeads.Notes);
        Console.WriteLine("CustomerKey: {0}", customerLeads.CustomerKey);
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
    GetCustomerLeadsRequest req = new GetCustomerLeadsRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerLeadID = 1;         //Optionally pull just one customer lead by ID
    req.GreaterThanCustomerLeadID = 1;//Paging controller
    req.BatchSize = 1;              //Defaults to 100 at a time
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    GetCustomerLeadsResponse res = api.GetCustomerLeads(req);

    //Now examine the results:

    foreach (CustomerLeadsResponse customerLeads  in res.CustomerLeads)
    {
        Console.WriteLine("CustomerID: {0}", customerLeads.CustomerID);
        Console.WriteLine("CustomerLeadID: {0}", customerLeads.CustomerLeadID);
        Console.WriteLine("FirstName: {0}", customerLeads.FirstName);
        Console.WriteLine("LastName: {0}", customerLeads.LastName);
        Console.WriteLine("MiddleName: {0}", customerLeads.MiddleName);
        Console.WriteLine("Company: {0}", customerLeads.Company);
        Console.WriteLine("Phone: {0}", customerLeads.Phone);
        Console.WriteLine("Phone2: {0}", customerLeads.Phone2);
        Console.WriteLine("MobilePhone: {0}", customerLeads.MobilePhone);
        Console.WriteLine("Fax: {0}", customerLeads.Fax);
        Console.WriteLine("Email: {0}", customerLeads.Email);
        Console.WriteLine("Address1: {0}", customerLeads.Address1);
        Console.WriteLine("Address2: {0}", customerLeads.Address2);
        Console.WriteLine("City: {0}", customerLeads.City);
        Console.WriteLine("Zip: {0}", customerLeads.Zip);
        Console.WriteLine("BirthDate: {0}", customerLeads.BirthDate);
        Console.WriteLine("Notes: {0}", customerLeads.Notes);
        Console.WriteLine("CustomerKey: {0}", customerLeads.CustomerKey);
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
    Dim req as new GetCustomerLeadsRequest()

    req.CustomerID = 1
    req.CustomerLeadID = 1
    req.GreaterThanCustomerLeadID = 1
    req.BatchSize = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As GetCustomerLeadsResponse = api.GetCustomerLeads(req)

    'Now examine the results:

    For Each customerLeads As CustomerLeadsResponse In res.CustomerLeads
        Console.WriteLine("CustomerID: {0}", customerLeads.CustomerID)
        Console.WriteLine("CustomerLeadID: {0}", customerLeads.CustomerLeadID)
        Console.WriteLine("FirstName: {0}", customerLeads.FirstName)
        Console.WriteLine("LastName: {0}", customerLeads.LastName)
        Console.WriteLine("MiddleName: {0}", customerLeads.MiddleName)
        Console.WriteLine("Company: {0}", customerLeads.Company)
        Console.WriteLine("Phone: {0}", customerLeads.Phone)
        Console.WriteLine("Phone2: {0}", customerLeads.Phone2)
        Console.WriteLine("MobilePhone: {0}", customerLeads.MobilePhone)
        Console.WriteLine("Fax: {0}", customerLeads.Fax)
        Console.WriteLine("Email: {0}", customerLeads.Email)
        Console.WriteLine("Address1: {0}", customerLeads.Address1)
        Console.WriteLine("Address2: {0}", customerLeads.Address2)
        Console.WriteLine("City: {0}", customerLeads.City)
        Console.WriteLine("Zip: {0}", customerLeads.Zip)
        Console.WriteLine("BirthDate: {0}", customerLeads.BirthDate)
        Console.WriteLine("Notes: {0}", customerLeads.Notes)
        Console.WriteLine("CustomerKey: {0}", customerLeads.CustomerKey)
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

    $req->CustomerID = 1;
    $req->CustomerLeadID = 1;
    $req->GreaterThanCustomerLeadID = 1;
    $req->BatchSize = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.GetCustomerLeads($req);

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
    GetCustomerLeadsRequest req = new GetCustomerLeadsRequest();

    req.setCustomerID(1);
    req.setCustomerLeadID(1);
    req.setGreaterThanCustomerLeadID(1);
    req.setBatchSize(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    GetCustomerLeadsResponse res = api.getExigoApiSoap().getCustomerLeads(req, auth);

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

### CreateCustomerLead

> Creates a new customer lead.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Customer Leads |
| REST | `POST /3.0/customerlead` |
| SOAP action | `https://api.exigo.com/CreateCustomerLead` |
| WSDL elements | `CreateCustomerLeadRequest` → `CreateCustomerLeadResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateCustomerLead |

#### Input

**`CreateCustomerLeadRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `FirstName` | `String` | Optional. |
| `LastName` | `String` | Optional. |
| `MiddleName` | `String` | Optional. |
| `Company` | `String` | Optional. |
| `Phone` | `String` | Optional. |
| `Phone2` | `String` | Optional. |
| `MobilePhone` | `String` | Optional. |
| `Fax` | `String` | Optional. |
| `Email` | `String` | Optional. |
| `Address1` | `String` | Optional. |
| `Address2` | `String` | Optional. |
| `City` | `String` | Optional. |
| `State` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Zip` | `String` | Optional. |
| `Country` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `BirthDate` | `DateTime` | Optional. |
| `Notes` | `String` | Optional. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`CreateCustomerLeadResponse`**

| Property | Type | Notes |
|---|---|---|
| `CustomerLeadID` | `Int32` | Unique identifier for a customer lead record. |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/customerlead HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "firstName": "",
  "lastName": "",
  "middleName": "",
  "company": "",
  "phone": "",
  "phone2": "",
  "mobilePhone": "",
  "fax": "",
  "email": "",
  "address1": "",
  "address2": "",
  "city": "",
  "zip": "",
  "birthDate": "2026-11-10T00:00:00-06:00",
  "notes": "",
  "customerKey": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "customerLeadID": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateCustomerLead"

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
    <CreateCustomerLeadRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <FirstName>string</FirstName>
      <LastName>string</LastName>
      <MiddleName>string</MiddleName>
      <Company>string</Company>
      <Phone>string</Phone>
      <Phone2>string</Phone2>
      <MobilePhone>string</MobilePhone>
      <Fax>string</Fax>
      <Email>string</Email>
      <Address1>string</Address1>
      <Address2>string</Address2>
      <City>string</City>
      <State>string</State>
      <Zip>string</Zip>
      <Country>string</Country>
      <BirthDate>dateTime</BirthDate>
      <Notes>string</Notes>
      <CustomerKey>string</CustomerKey>
    </CreateCustomerLeadRequest>
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
    <CreateCustomerLeadResult xmlns="http://api.exigo.com/">
      <CustomerLeadID>int</CustomerLeadID>
    </CreateCustomerLeadResult>
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
    var req = new CreateCustomerLeadRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.FirstName = "1";
    req.LastName = "1";
    req.MiddleName = "1";
    req.Company = "1";
    req.Phone = "1";
    req.Phone2 = "1";
    req.MobilePhone = "1";
    req.Fax = "1";
    req.Email = "1";
    req.Address1 = "1";
    req.Address2 = "1";
    req.City = "1";
    req.Zip = "1";
    req.BirthDate = DateTime.Today;
    req.Notes = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.CreateCustomerLeadAsync(req);

    //Now examine the results:
    Console.WriteLine("CustomerLeadID: {0}", res.CustomerLeadID);
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
    CreateCustomerLeadRequest req = new CreateCustomerLeadRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.FirstName = "1";
    req.LastName = "1";
    req.MiddleName = "1";
    req.Company = "1";
    req.Phone = "1";
    req.Phone2 = "1";
    req.MobilePhone = "1";
    req.Fax = "1";
    req.Email = "1";
    req.Address1 = "1";
    req.Address2 = "1";
    req.City = "1";
    req.Zip = "1";
    req.BirthDate = DateTime.Today;
    req.Notes = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    CreateCustomerLeadResponse res = api.CreateCustomerLead(req);

    //Now examine the results:
    Console.WriteLine("CustomerLeadID: {0}", res.CustomerLeadID);
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
    Dim req as new CreateCustomerLeadRequest()

    req.CustomerID = 1
    req.FirstName = "1"
    req.LastName = "1"
    req.MiddleName = "1"
    req.Company = "1"
    req.Phone = "1"
    req.Phone2 = "1"
    req.MobilePhone = "1"
    req.Fax = "1"
    req.Email = "1"
    req.Address1 = "1"
    req.Address2 = "1"
    req.City = "1"
    req.Zip = "1"
    req.BirthDate = DateTime.Today
    req.Notes = "1"
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As CreateCustomerLeadResponse = api.CreateCustomerLead(req)

    'Now examine the results:
    Console.WriteLine("CustomerLeadID: {0}", res.CustomerLeadID)
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
    $req->FirstName = "1";
    $req->LastName = "1";
    $req->MiddleName = "1";
    $req->Company = "1";
    $req->Phone = "1";
    $req->Phone2 = "1";
    $req->MobilePhone = "1";
    $req->Fax = "1";
    $req->Email = "1";
    $req->Address1 = "1";
    $req->Address2 = "1";
    $req->City = "1";
    $req->Zip = "1";
    $req->BirthDate = 1;
    $req->Notes = "1";
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.CreateCustomerLead($req);

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
    CreateCustomerLeadRequest req = new CreateCustomerLeadRequest();

    req.setCustomerID(1);
    req.setFirstName("1");
    req.setLastName("1");
    req.setMiddleName("1");
    req.setCompany("1");
    req.setPhone("1");
    req.setPhone2("1");
    req.setMobilePhone("1");
    req.setFax("1");
    req.setEmail("1");
    req.setAddress1("1");
    req.setAddress2("1");
    req.setCity("1");
    req.setZip("1");
    req.setBirthDate(1);
    req.setNotes("1");
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    CreateCustomerLeadResponse res = api.getExigoApiSoap().createCustomerLead(req, auth);

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

### UpdateCustomerLead

> Updates a customer leads.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Customer Leads |
| REST | `PATCH /3.0/customerlead` |
| SOAP action | `https://api.exigo.com/UpdateCustomerLead` |
| WSDL elements | `UpdateCustomerLeadRequest` → `UpdateCustomerLeadResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateCustomerLead |

#### Input

**`UpdateCustomerLeadRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerLeadID` | `Int32` | Unique identifier for a customer lead record. |
| `FirstName` | `String` | Optional. |
| `LastName` | `String` | Optional. |
| `MiddleName` | `String` | Optional. |
| `Company` | `String` | Optional. |
| `Phone` | `String` | Optional. |
| `Phone2` | `String` | Optional. |
| `MobilePhone` | `String` | Optional. |
| `Fax` | `String` | Optional. |
| `Email` | `String` | Optional. |
| `Address1` | `String` | Optional. |
| `Address2` | `String` | Optional. |
| `City` | `String` | Optional. |
| `State` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Zip` | `String` | Optional. |
| `Country` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `BirthDate` | `DateTime` | Optional. |
| `Notes` | `String` | Optional. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`UpdateCustomerLeadResponse`**

_No properties._

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/customerlead HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "customerLeadID": 1,
  "firstName": "",
  "lastName": "",
  "middleName": "",
  "company": "",
  "phone": "",
  "phone2": "",
  "mobilePhone": "",
  "fax": "",
  "email": "",
  "address1": "",
  "address2": "",
  "city": "",
  "zip": "",
  "birthDate": "2026-11-10T00:00:00-06:00",
  "notes": "",
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
SOAPAction: "https://api.exigo.com/UpdateCustomerLead"

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
    <UpdateCustomerLeadRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerLeadID>int</CustomerLeadID>
      <FirstName>string</FirstName>
      <LastName>string</LastName>
      <MiddleName>string</MiddleName>
      <Company>string</Company>
      <Phone>string</Phone>
      <Phone2>string</Phone2>
      <MobilePhone>string</MobilePhone>
      <Fax>string</Fax>
      <Email>string</Email>
      <Address1>string</Address1>
      <Address2>string</Address2>
      <City>string</City>
      <State>string</State>
      <Zip>string</Zip>
      <Country>string</Country>
      <BirthDate>dateTime</BirthDate>
      <Notes>string</Notes>
      <CustomerKey>string</CustomerKey>
    </UpdateCustomerLeadRequest>
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
    <UpdateCustomerLeadResult xmlns="http://api.exigo.com/" />
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
    var req = new UpdateCustomerLeadRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerLeadID = 1;         //Unique identifier for a customer lead record.
    req.FirstName = "1";
    req.LastName = "1";
    req.MiddleName = "1";
    req.Company = "1";
    req.Phone = "1";
    req.Phone2 = "1";
    req.MobilePhone = "1";
    req.Fax = "1";
    req.Email = "1";
    req.Address1 = "1";
    req.Address2 = "1";
    req.City = "1";
    req.Zip = "1";
    req.BirthDate = DateTime.Today;
    req.Notes = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.UpdateCustomerLeadAsync(req);

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
    UpdateCustomerLeadRequest req = new UpdateCustomerLeadRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerLeadID = 1;         //Unique identifier for a customer lead record.
    req.FirstName = "1";
    req.LastName = "1";
    req.MiddleName = "1";
    req.Company = "1";
    req.Phone = "1";
    req.Phone2 = "1";
    req.MobilePhone = "1";
    req.Fax = "1";
    req.Email = "1";
    req.Address1 = "1";
    req.Address2 = "1";
    req.City = "1";
    req.Zip = "1";
    req.BirthDate = DateTime.Today;
    req.Notes = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    UpdateCustomerLeadResponse res = api.UpdateCustomerLead(req);

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
    Dim req as new UpdateCustomerLeadRequest()

    req.CustomerID = 1
    req.CustomerLeadID = 1
    req.FirstName = "1"
    req.LastName = "1"
    req.MiddleName = "1"
    req.Company = "1"
    req.Phone = "1"
    req.Phone2 = "1"
    req.MobilePhone = "1"
    req.Fax = "1"
    req.Email = "1"
    req.Address1 = "1"
    req.Address2 = "1"
    req.City = "1"
    req.Zip = "1"
    req.BirthDate = DateTime.Today
    req.Notes = "1"
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As UpdateCustomerLeadResponse = api.UpdateCustomerLead(req)

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
    $req->CustomerLeadID = 1;
    $req->FirstName = "1";
    $req->LastName = "1";
    $req->MiddleName = "1";
    $req->Company = "1";
    $req->Phone = "1";
    $req->Phone2 = "1";
    $req->MobilePhone = "1";
    $req->Fax = "1";
    $req->Email = "1";
    $req->Address1 = "1";
    $req->Address2 = "1";
    $req->City = "1";
    $req->Zip = "1";
    $req->BirthDate = 1;
    $req->Notes = "1";
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.UpdateCustomerLead($req);

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
    UpdateCustomerLeadRequest req = new UpdateCustomerLeadRequest();

    req.setCustomerID(1);
    req.setCustomerLeadID(1);
    req.setFirstName("1");
    req.setLastName("1");
    req.setMiddleName("1");
    req.setCompany("1");
    req.setPhone("1");
    req.setPhone2("1");
    req.setMobilePhone("1");
    req.setFax("1");
    req.setEmail("1");
    req.setAddress1("1");
    req.setAddress2("1");
    req.setCity("1");
    req.setZip("1");
    req.setBirthDate(1);
    req.setNotes("1");
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    UpdateCustomerLeadResponse res = api.getExigoApiSoap().updateCustomerLead(req, auth);

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

### DeleteCustomerLead

>  Deletes a customer lead.

| | |
|---|---|
| Category | Customer Leads |
| REST | `DELETE /3.0/customerlead` |
| SOAP action | `https://api.exigo.com/DeleteCustomerLead` |
| WSDL elements | `DeleteCustomerLeadRequest` → `DeleteCustomerLeadResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DeleteCustomerLead |

#### Input

**`DeleteCustomerLeadRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerLeadID` | `Int32` | Unique identifier for a customer lead record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`DeleteCustomerLeadResponse`**

_No properties._

#### REST example

```http
DELETE https://yourcompany-api.exigo.com/3.0/customerlead HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "customerLeadID": 1,
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
SOAPAction: "https://api.exigo.com/DeleteCustomerLead"

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
    <DeleteCustomerLeadRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerLeadID>int</CustomerLeadID>
      <CustomerKey>string</CustomerKey>
    </DeleteCustomerLeadRequest>
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
    <DeleteCustomerLeadResult xmlns="http://api.exigo.com/" />
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
    var req = new DeleteCustomerLeadRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerLeadID = 1;         //Unique identifier for a customer lead record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.DeleteCustomerLeadAsync(req);

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
    DeleteCustomerLeadRequest req = new DeleteCustomerLeadRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerLeadID = 1;         //Unique identifier for a customer lead record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    DeleteCustomerLeadResponse res = api.DeleteCustomerLead(req);

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
    Dim req as new DeleteCustomerLeadRequest()

    req.CustomerID = 1
    req.CustomerLeadID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As DeleteCustomerLeadResponse = api.DeleteCustomerLead(req)

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
    $req->CustomerLeadID = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.DeleteCustomerLead($req);

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
    DeleteCustomerLeadRequest req = new DeleteCustomerLeadRequest();

    req.setCustomerID(1);
    req.setCustomerLeadID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    DeleteCustomerLeadResponse res = api.getExigoApiSoap().deleteCustomerLead(req, auth);

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

### SetCustomerLeadSocialNetworks

> Deletes all existing social network(s) for the customer lead, then inserts
>  the provided list of social network(s) for the customer lead.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Customer Leads |
| REST | `PUT /3.0/customerlead/socialnetworks` |
| SOAP action | `https://api.exigo.com/SetCustomerLeadSocialNetworks` |
| WSDL elements | `SetCustomerLeadSocialNetworksRequest` → `SetCustomerLeadSocialNetworksResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=SetCustomerLeadSocialNetworks |

#### Input

**`SetCustomerLeadSocialNetworksRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerLeadID` | `Int32` | Unique identifier for a customer lead record. |
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerLeadSocialNetworks` | `CustomerLeadSocialNetworkRequest[]` |  |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

**`CustomerLeadSocialNetworkRequest`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `SocialNetworkID` | `Int32` | Unique Social Network ID.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Url` | `String` | Optional. |

#### Output

**`SetCustomerLeadSocialNetworksResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/customerlead/socialnetworks HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerLeadID": 1,
  "customerID": 1,
  "customerLeadSocialNetworks": null,
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
SOAPAction: "https://api.exigo.com/SetCustomerLeadSocialNetworks"

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
    <SetCustomerLeadSocialNetworksRequest xmlns="http://api.exigo.com/">
      <CustomerLeadID>int</CustomerLeadID>
      <CustomerID>int</CustomerID>
      <CustomerLeadSocialNetworks>
        <CustomerLeadSocialNetworkRequest>
          <SocialNetworkID>int</SocialNetworkID>
          <Url>string</Url>
        </CustomerLeadSocialNetworkRequest>
      </CustomerLeadSocialNetworks>
      <CustomerKey>string</CustomerKey>
    </SetCustomerLeadSocialNetworksRequest>
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
    <SetCustomerLeadSocialNetworksResult xmlns="http://api.exigo.com/" />
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
    var req = new SetCustomerLeadSocialNetworksRequest();

    req.CustomerLeadID = 1;         //Unique identifier for a customer lead record.
    req.CustomerID = 1;             //Unique numeric identifier for customer record.

    //Add CustomerLeadSocialNetworks
    var customerleadsocialnetworks = new List<CustomerLeadSocialNetworkRequest>();

    var customerLeadSocialNetwork1 = new CustomerLeadSocialNetworkRequest();
    customerLeadSocialNetwork1.Url = "1";
    customerleadsocialnetworks.Add(customerLeadSocialNetwork1);

    var customerLeadSocialNetwork2 = new CustomerLeadSocialNetworkRequest();
    customerLeadSocialNetwork2.Url = "2";
    customerleadsocialnetworks.Add(customerLeadSocialNetwork2);

    //Now attach the list to the request
    req.CustomerLeadSocialNetworks = customerleadsocialnetworks.ToArray();
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.SetCustomerLeadSocialNetworksAsync(req);

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
    SetCustomerLeadSocialNetworksRequest req = new SetCustomerLeadSocialNetworksRequest();

    req.CustomerLeadID = 1;         //Unique identifier for a customer lead record.
    req.CustomerID = 1;             //Unique numeric identifier for customer record.

    //Add CustomerLeadSocialNetworks
    List<CustomerLeadSocialNetworkRequest> customerleadsocialnetworks = new List<CustomerLeadSocialNetworkRequest>();

    CustomerLeadSocialNetworkRequest customerLeadSocialNetwork1 = new CustomerLeadSocialNetworkRequest();
    customerLeadSocialNetwork1.Url = "1";
    customerleadsocialnetworks.Add(customerLeadSocialNetwork1);

    CustomerLeadSocialNetworkRequest customerLeadSocialNetwork2 = new CustomerLeadSocialNetworkRequest();
    customerLeadSocialNetwork2.Url = "2";
    customerleadsocialnetworks.Add(customerLeadSocialNetwork2);

    //Now attach the list to the request
    req.CustomerLeadSocialNetworks = customerleadsocialnetworks.ToArray();
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    SetCustomerLeadSocialNetworksResponse res = api.SetCustomerLeadSocialNetworks(req);

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
    Dim req as new SetCustomerLeadSocialNetworksRequest()

    req.CustomerLeadID = 1
    req.CustomerID = 1

    'Add CustomerLeadSocialNetworks
    Dim customerleadsocialnetworks As New List(Of CustomerLeadSocialNetworkRequest)()

    Dim customerLeadSocialNetwork1 as new CustomerLeadSocialNetworkRequest()
    customerLeadSocialNetwork1.Url = "1"
    customerleadsocialnetworks.Add(customerLeadSocialNetwork1)

    Dim customerLeadSocialNetwork2 as new CustomerLeadSocialNetworkRequest()
    customerLeadSocialNetwork2.Url = "2"
    customerleadsocialnetworks.Add(customerLeadSocialNetwork2)

    'Now attach the list to the request
    req.CustomerLeadSocialNetworks = customerleadsocialnetworks.ToArray()
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As SetCustomerLeadSocialNetworksResponse = api.SetCustomerLeadSocialNetworks(req)

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

    $req->CustomerLeadID = 1;
    $req->CustomerID = 1;

    //Add CustomerLeadSocialNetworks

    $customerLeadSocialNetwork1->Url = "1";

    $customerLeadSocialNetwork2->Url = "2";

    //Now attach the list to the request
    req.CustomerLeadSocialNetworks = array(customerLeadSocialNetwork1,customerLeadSocialNetwork2);
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.SetCustomerLeadSocialNetworks($req);

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
    SetCustomerLeadSocialNetworksRequest req = new SetCustomerLeadSocialNetworksRequest();

    req.setCustomerLeadID(1);
    req.setCustomerID(1);

    //Add CustomerLeadSocialNetworks
    ArrayOfCustomerLeadSocialNetworkRequest customerleadsocialnetworks = new ArrayOfCustomerLeadSocialNetworkRequest();

    CustomerLeadSocialNetworkRequest customerLeadSocialNetwork1 = new CustomerLeadSocialNetworkRequest();
    customerLeadSocialNetwork1.setUrl("1");
    customerleadsocialnetworks.Add(customerLeadSocialNetwork1);

    CustomerLeadSocialNetworkRequest customerLeadSocialNetwork2 = new CustomerLeadSocialNetworkRequest();
    customerLeadSocialNetwork2.setUrl("2");
    customerleadsocialnetworks.Add(customerLeadSocialNetwork2);

    //Now attach the list to the request
    req.setCustomerLeadSocialNetworks(customerleadsocialnetworks);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    SetCustomerLeadSocialNetworksResponse res = api.getExigoApiSoap().setCustomerLeadSocialNetworks(req, auth);

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

### GetCustomerLeadSocialNetworks

> Returns a list of social network(s) for the customer lead.

| | |
|---|---|
| Category | Customer Leads |
| REST | `GET /3.0/customerlead/socialnetworks?customerID=1` |
| SOAP action | `https://api.exigo.com/GetCustomerLeadSocialNetworks` |
| WSDL elements | `GetCustomerLeadSocialNetworksRequest` → `GetCustomerLeadSocialNetworksResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetCustomerLeadSocialNetworks |

#### Input

**`GetCustomerLeadSocialNetworksRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerLeadID` | `Int32` | Unique identifier for a customer lead record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`GetCustomerLeadSocialNetworksResponse`**

| Property | Type | Notes |
|---|---|---|
| `CustomerLeadSocialNetwork` | `CustomerLeadSocialNetworksResponse[]` |  |

**`CustomerLeadSocialNetworksResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `SocialNetworkID` | `Int32` | Unique Social Network ID.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `SocialNetworkDescription` | `String` |  |
| &nbsp;&nbsp;↳ `Url` | `String` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/customerlead/socialnetworks?customerID=1
  &customerLeadID=1
  &customerKey=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "customerLeadSocialNetwork": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetCustomerLeadSocialNetworks"

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
    <GetCustomerLeadSocialNetworksRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerLeadID>int</CustomerLeadID>
      <CustomerKey>string</CustomerKey>
    </GetCustomerLeadSocialNetworksRequest>
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
    <GetCustomerLeadSocialNetworksResult xmlns="http://api.exigo.com/">
      <CustomerLeadSocialNetwork>
        <CustomerLeadSocialNetworksResponse>
          <SocialNetworkID>int</SocialNetworkID>
          <SocialNetworkDescription>string</SocialNetworkDescription>
          <Url>string</Url>
        </CustomerLeadSocialNetworksResponse>
      </CustomerLeadSocialNetwork>
    </GetCustomerLeadSocialNetworksResult>
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
    var req = new GetCustomerLeadSocialNetworksRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerLeadID = 1;         //Unique identifier for a customer lead record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.GetCustomerLeadSocialNetworksAsync(req);

    //Now examine the results:

    foreach (var customerLeadSocialNetworks  in res.CustomerLeadSocialNetwork)
    {
        Console.WriteLine("SocialNetworkDescription: {0}", customerLeadSocialNetworks.SocialNetworkDescription);
        Console.WriteLine("Url: {0}", customerLeadSocialNetworks.Url);
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
    GetCustomerLeadSocialNetworksRequest req = new GetCustomerLeadSocialNetworksRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerLeadID = 1;         //Unique identifier for a customer lead record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    GetCustomerLeadSocialNetworksResponse res = api.GetCustomerLeadSocialNetworks(req);

    //Now examine the results:

    foreach (CustomerLeadSocialNetworksResponse customerLeadSocialNetworks  in res.CustomerLeadSocialNetwork)
    {
        Console.WriteLine("SocialNetworkDescription: {0}", customerLeadSocialNetworks.SocialNetworkDescription);
        Console.WriteLine("Url: {0}", customerLeadSocialNetworks.Url);
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
    Dim req as new GetCustomerLeadSocialNetworksRequest()

    req.CustomerID = 1
    req.CustomerLeadID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As GetCustomerLeadSocialNetworksResponse = api.GetCustomerLeadSocialNetworks(req)

    'Now examine the results:

    For Each customerLeadSocialNetworks As CustomerLeadSocialNetworksResponse In res.CustomerLeadSocialNetwork
        Console.WriteLine("SocialNetworkDescription: {0}", customerLeadSocialNetworks.SocialNetworkDescription)
        Console.WriteLine("Url: {0}", customerLeadSocialNetworks.Url)
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

    $req->CustomerID = 1;
    $req->CustomerLeadID = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.GetCustomerLeadSocialNetworks($req);

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
    GetCustomerLeadSocialNetworksRequest req = new GetCustomerLeadSocialNetworksRequest();

    req.setCustomerID(1);
    req.setCustomerLeadID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    GetCustomerLeadSocialNetworksResponse res = api.getExigoApiSoap().getCustomerLeadSocialNetworks(req, auth);

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
