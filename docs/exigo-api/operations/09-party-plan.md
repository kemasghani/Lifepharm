# Exigo API — Party Plan

API version v2025.11.7.6. Crawled 2026-11-11 from https://api.exigo.com/3.0/. Back to [index](../README.md).

| Operation | REST | Summary |
|---|---|---|
| [CreateParty](#createparty) | `POST /3.0/party` | Creates a new Party |
| [UpdateParty](#updateparty) | `PUT /3.0/party` | Updates selected Party instance |
| [GetParties](#getparties) | `GET /3.0/party?partyID=1` | Gets Parties list |
| [GetPartyGuests](#getpartyguests) | `GET /3.0/party/guest?partyID=1` | Gets a list of guests belonging to a party |
| [AddPartyGuests](#addpartyguests) | `POST /3.0/party/guest` | Adds one or more guests to a party. |
| [RemovePartyGuests](#removepartyguests) | `DELETE /3.0/party/guest` | Removes one or more guests from a party. |
| [CreateGuest](#createguest) | `POST /3.0/guest` | Creates a new guest. Can optionally be put in a party. |
| [UpdateGuest](#updateguest) | `PATCH /3.0/guest` | Updates one or more fields on an existing guest. |
| [GetGuests](#getguests) | `GET /3.0/guestAuthorization:` | Gets a list of guests |
| [GetGuestSocialNetworks](#getguestsocialnetworks) | `GET /3.0/guest/socialnetwork?guestID=1` | Returns a list of social network(s) for the guest. |
| [SetGuestSocialNetworks](#setguestsocialnetworks) | `PUT /3.0/guest/socialnetwork` | Deletes all existing social network(s) for the guest, then inserts the provided list of social network(s) for the guest. |

---
### CreateParty

> Creates a new Party

| | |
|---|---|
| Category | Party Plan |
| REST | `POST /3.0/party` |
| SOAP action | `https://api.exigo.com/CreateParty` |
| WSDL elements | `CreatePartyRequest` → `CreatePartyResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateParty |

#### Input

**`CreatePartyRequest`**

| Property | Type | Notes |
|---|---|---|
| `PartyType` | `Int32` | Party type.<br>**Lookup:** company-specific list (see company-lists.md) |
| `PartyStatusType` | `Int32` | Party Status.<br>**Lookup:** company-specific list (see company-lists.md) |
| `HostID` | `Int32` |  |
| `DistributorID` | `Int32` |  |
| `StartDate` | `DateTime` |  |
| `CloseDate` | `DateTime` | Optional. Close Date. |
| `Description` | `String` | Optional. Description. Must be 100 characters or less. |
| `EventStart` | `DateTime` | Optional. Event Start date. |
| `EventEnd` | `DateTime` | Optional. Event End date. |
| `LanguageID` | `Int32` | Optional. Language ID. Defaults to 0. |
| `Information` | `String` | Optional. Information. |
| `Address` | `PartyAddress` | Optional. Information. |
| `BookingPartyID` | `Int32` | Optional. BookingPartyID. |
| `Field1` | `String` | Optional. Field1. |
| `Field2` | `String` | Optional. Field2. |
| `Field3` | `String` | Optional. Field3. |
| `Field4` | `String` | Optional. Field4. |
| `Field5` | `String` | Optional. Field5. |
| `TimeZoneID` | `String` | Optional. TimeZoneID. |
| `VirtualMeetingLink` | `String` | Optional. VirtualMeetingLink. |
| `PartyShoppingUrl` | `String` | Optional. PartyShoppingUrl. |
| `PartyExternalID` | `Guid` | Optional. PartyShoppingUrl. |

#### Output

**`CreatePartyResponse`**

| Property | Type | Notes |
|---|---|---|
| `PartyID` | `Int32` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/party HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "partyType": 1,
  "partyStatusType": 1,
  "hostID": 1,
  "distributorID": 1,
  "startDate": "2026-11-10T00:00:00-06:00",
  "closeDate": "2026-11-10T00:00:00-06:00",
  "description": "1",
  "eventStart": "2026-11-10T00:00:00-06:00",
  "eventEnd": "2026-11-10T00:00:00-06:00",
  "languageID": 1,
  "information": "1",
  "bookingPartyID": 1,
  "field1": "1",
  "field2": "1",
  "field3": "1",
  "field4": "1",
  "field5": "1",
  "timeZoneID": "1",
  "virtualMeetingLink": "1",
  "partyShoppingUrl": "1",
  "partyExternalID": null
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "partyID": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateParty"

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
    <CreatePartyRequest xmlns="http://api.exigo.com/">
      <PartyType>int</PartyType>
      <PartyStatusType>int</PartyStatusType>
      <HostID>int</HostID>
      <DistributorID>int</DistributorID>
      <StartDate>dateTime</StartDate>
      <CloseDate>dateTime</CloseDate>
      <Description>string</Description>
      <EventStart>dateTime</EventStart>
      <EventEnd>dateTime</EventEnd>
      <LanguageID>int</LanguageID>
      <Information>string</Information>
      <Address>
        <Address1>string</Address1>
        <Address2>string</Address2>
        <City>string</City>
        <State>string</State>
        <Zip>string</Zip>
        <Country>string</Country>
      </Address>
      <BookingPartyID>int</BookingPartyID>
      <Field1>string</Field1>
      <Field2>string</Field2>
      <Field3>string</Field3>
      <Field4>string</Field4>
      <Field5>string</Field5>
      <TimeZoneID>string</TimeZoneID>
      <VirtualMeetingLink>string</VirtualMeetingLink>
      <PartyShoppingUrl>string</PartyShoppingUrl>
      <PartyExternalID>guid</PartyExternalID>
    </CreatePartyRequest>
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
    <CreatePartyResult xmlns="http://api.exigo.com/">
      <PartyID>int</PartyID>
    </CreatePartyResult>
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
    var req = new CreatePartyRequest();

    req.PartyType = 1;              //Party type
    req.PartyStatusType = 1;        //Party Status
    req.HostID = 1;
    req.DistributorID = 1;
    req.StartDate = DateTime.Today;
    req.CloseDate = DateTime.Today;              //Close Date
    req.Description = "1";          //Description. Must be 100 characters or less.
    req.EventStart = DateTime.Today;             //Event Start date
    req.EventEnd = DateTime.Today;               //Event End date
    req.LanguageID = 1;             //Language ID
    req.Information = "1";          //Information
    req.BookingPartyID = 1;         //BookingPartyID
    req.Field1 = "1";               //Field1
    req.Field2 = "1";               //Field2
    req.Field3 = "1";               //Field3
    req.Field4 = "1";               //Field4
    req.Field5 = "1";               //Field5
    req.TimeZoneID = "1";           //TimeZoneID
    req.VirtualMeetingLink = "1";   //VirtualMeetingLink
    req.PartyShoppingUrl = "1";     //PartyShoppingUrl
    req.PartyExternalID = 1;        //PartyShoppingUrl

    //Send Request to Server and Get Response
    var res = await api.CreatePartyAsync(req);

    //Now examine the results:
    Console.WriteLine("PartyID: {0}", res.PartyID);
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
    CreatePartyRequest req = new CreatePartyRequest();

    req.PartyType = 1;              //Party type
    req.PartyStatusType = 1;        //Party Status
    req.HostID = 1;
    req.DistributorID = 1;
    req.StartDate = DateTime.Today;
    req.CloseDate = DateTime.Today;              //Close Date
    req.Description = "1";          //Description. Must be 100 characters or less.
    req.EventStart = DateTime.Today;             //Event Start date
    req.EventEnd = DateTime.Today;               //Event End date
    req.LanguageID = 1;             //Language ID
    req.Information = "1";          //Information
    req.BookingPartyID = 1;         //BookingPartyID
    req.Field1 = "1";               //Field1
    req.Field2 = "1";               //Field2
    req.Field3 = "1";               //Field3
    req.Field4 = "1";               //Field4
    req.Field5 = "1";               //Field5
    req.TimeZoneID = "1";           //TimeZoneID
    req.VirtualMeetingLink = "1";   //VirtualMeetingLink
    req.PartyShoppingUrl = "1";     //PartyShoppingUrl
    req.PartyExternalID = 1;        //PartyShoppingUrl

    //Send Request to Server and Get Response
    CreatePartyResponse res = api.CreateParty(req);

    //Now examine the results:
    Console.WriteLine("PartyID: {0}", res.PartyID);
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
    Dim req as new CreatePartyRequest()

    req.PartyType = 1
    req.PartyStatusType = 1
    req.HostID = 1
    req.DistributorID = 1
    req.StartDate = DateTime.Today
    req.CloseDate = DateTime.Today
    req.Description = "1"
    req.EventStart = DateTime.Today
    req.EventEnd = DateTime.Today
    req.LanguageID = 1
    req.Information = "1"
    req.BookingPartyID = 1
    req.Field1 = "1"
    req.Field2 = "1"
    req.Field3 = "1"
    req.Field4 = "1"
    req.Field5 = "1"
    req.TimeZoneID = "1"
    req.VirtualMeetingLink = "1"
    req.PartyShoppingUrl = "1"
    req.PartyExternalID = 1

    'Send Request to Server and Get Response
    Dim res As CreatePartyResponse = api.CreateParty(req)

    'Now examine the results:
    Console.WriteLine("PartyID: {0}", res.PartyID)
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

    $req->PartyType = 1;
    $req->PartyStatusType = 1;
    $req->HostID = 1;
    $req->DistributorID = 1;
    $req->StartDate = 1;
    $req->CloseDate = 1;
    $req->Description = "1";
    $req->EventStart = 1;
    $req->EventEnd = 1;
    $req->LanguageID = 1;
    $req->Information = "1";
    $req->BookingPartyID = 1;
    $req->Field1 = "1";
    $req->Field2 = "1";
    $req->Field3 = "1";
    $req->Field4 = "1";
    $req->Field5 = "1";
    $req->TimeZoneID = "1";
    $req->VirtualMeetingLink = "1";
    $req->PartyShoppingUrl = "1";
    $req->PartyExternalID = 1;

    //Send Request to Server and Get Response
    $res = $api.CreateParty($req);

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
    CreatePartyRequest req = new CreatePartyRequest();

    req.setPartyType(1);
    req.setPartyStatusType(1);
    req.setHostID(1);
    req.setDistributorID(1);
    req.setStartDate(1);
    req.setCloseDate(1);
    req.setDescription("1");
    req.setEventStart(1);
    req.setEventEnd(1);
    req.setLanguageID(1);
    req.setInformation("1");
    req.setBookingPartyID(1);
    req.setField1("1");
    req.setField2("1");
    req.setField3("1");
    req.setField4("1");
    req.setField5("1");
    req.setTimeZoneID("1");
    req.setVirtualMeetingLink("1");
    req.setPartyShoppingUrl("1");
    req.setPartyExternalID(1);

    //Send Request to Server and Get Response
    CreatePartyResponse res = api.getExigoApiSoap().createParty(req, auth);

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

### UpdateParty

> Updates selected Party instance

| | |
|---|---|
| Category | Party Plan |
| REST | `PUT /3.0/party` |
| SOAP action | `https://api.exigo.com/UpdateParty` |
| WSDL elements | `UpdatePartyRequest` → `UpdatePartyResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateParty |

#### Input

**`UpdatePartyRequest`**

| Property | Type | Notes |
|---|---|---|
| `PartyID` | `Int32` |  |
| `PartyType` | `Int32` | Optional. PartyTy. |
| `PartyStatusType` | `Int32` | Optional. PartyStatusTy. |
| `HostID` | `Int32` | Optional. HostID. |
| `DistributorID` | `Int32` | Optional. DistributorID. |
| `StartDate` | `DateTime` | Optional. StartDate. |
| `CloseDate` | `DateTime` | Optional. Close Date. |
| `Description` | `String` | Optional. Description. |
| `EventStart` | `DateTime` | Optional. Event Start date. |
| `EventEnd` | `DateTime` | Optional. Event End date. |
| `LanguageID` | `Int32` | Optional. Language ID. |
| `Information` | `String` | Optional. Information. |
| `Address` | `PartyAddress` | Optional. Information. |
| `BookingPartyID` | `Int32` | Optional. BookingPartyID. |
| `Field1` | `String` | Optional. Field1. |
| `Field2` | `String` | Optional. Field2. |
| `Field3` | `String` | Optional. Field3. |
| `Field4` | `String` | Optional. Field4. |
| `Field5` | `String` | Optional. Field5. |
| `TimeZoneID` | `String` | Optional. TimeZoneID. |
| `VirtualMeetingLink` | `String` | Optional. VirtualMeetingLink. |
| `PartyShoppingUrl` | `String` | Optional. PartyShoppingUrl. |
| `PartyExternalID` | `Guid` | Optional. PartyExternalID. |

#### Output

**`UpdatePartyResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/party HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "partyID": 1,
  "partyType": 1,
  "partyStatusType": 1,
  "hostID": 1,
  "distributorID": 1,
  "startDate": "2026-11-10T00:00:00-06:00",
  "closeDate": "2026-11-10T00:00:00-06:00",
  "description": "1",
  "eventStart": "2026-11-10T00:00:00-06:00",
  "eventEnd": "2026-11-10T00:00:00-06:00",
  "languageID": 1,
  "information": "1",
  "bookingPartyID": 1,
  "field1": "1",
  "field2": "1",
  "field3": "1",
  "field4": "1",
  "field5": "1",
  "timeZoneID": "1",
  "virtualMeetingLink": "1",
  "partyShoppingUrl": "1",
  "partyExternalID": null
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
SOAPAction: "https://api.exigo.com/UpdateParty"

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
    <UpdatePartyRequest xmlns="http://api.exigo.com/">
      <PartyID>int</PartyID>
      <PartyType>int</PartyType>
      <PartyStatusType>int</PartyStatusType>
      <HostID>int</HostID>
      <DistributorID>int</DistributorID>
      <StartDate>dateTime</StartDate>
      <CloseDate>dateTime</CloseDate>
      <Description>string</Description>
      <EventStart>dateTime</EventStart>
      <EventEnd>dateTime</EventEnd>
      <LanguageID>int</LanguageID>
      <Information>string</Information>
      <Address>
        <Address1>string</Address1>
        <Address2>string</Address2>
        <City>string</City>
        <State>string</State>
        <Zip>string</Zip>
        <Country>string</Country>
      </Address>
      <BookingPartyID>int</BookingPartyID>
      <Field1>string</Field1>
      <Field2>string</Field2>
      <Field3>string</Field3>
      <Field4>string</Field4>
      <Field5>string</Field5>
      <TimeZoneID>string</TimeZoneID>
      <VirtualMeetingLink>string</VirtualMeetingLink>
      <PartyShoppingUrl>string</PartyShoppingUrl>
      <PartyExternalID>guid</PartyExternalID>
    </UpdatePartyRequest>
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
    <UpdatePartyResult xmlns="http://api.exigo.com/" />
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
    var req = new UpdatePartyRequest();

    req.PartyID = 1;
    req.PartyType = 1;              //PartyTy
    req.PartyStatusType = 1;        //PartyStatusTy
    req.HostID = 1;                 //HostID
    req.DistributorID = 1;          //DistributorID
    req.StartDate = DateTime.Today;              //StartDate
    req.CloseDate = DateTime.Today;              //Close Date
    req.Description = "1";          //Description
    req.EventStart = DateTime.Today;             //Event Start date
    req.EventEnd = DateTime.Today;               //Event End date
    req.LanguageID = 1;             //Language ID
    req.Information = "1";          //Information
    req.BookingPartyID = 1;         //BookingPartyID
    req.Field1 = "1";               //Field1
    req.Field2 = "1";               //Field2
    req.Field3 = "1";               //Field3
    req.Field4 = "1";               //Field4
    req.Field5 = "1";               //Field5
    req.TimeZoneID = "1";           //TimeZoneID
    req.VirtualMeetingLink = "1";   //VirtualMeetingLink
    req.PartyShoppingUrl = "1";     //PartyShoppingUrl
    req.PartyExternalID = 1;        //PartyExternalID

    //Send Request to Server and Get Response
    var res = await api.UpdatePartyAsync(req);

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
    UpdatePartyRequest req = new UpdatePartyRequest();

    req.PartyID = 1;
    req.PartyType = 1;              //PartyTy
    req.PartyStatusType = 1;        //PartyStatusTy
    req.HostID = 1;                 //HostID
    req.DistributorID = 1;          //DistributorID
    req.StartDate = DateTime.Today;              //StartDate
    req.CloseDate = DateTime.Today;              //Close Date
    req.Description = "1";          //Description
    req.EventStart = DateTime.Today;             //Event Start date
    req.EventEnd = DateTime.Today;               //Event End date
    req.LanguageID = 1;             //Language ID
    req.Information = "1";          //Information
    req.BookingPartyID = 1;         //BookingPartyID
    req.Field1 = "1";               //Field1
    req.Field2 = "1";               //Field2
    req.Field3 = "1";               //Field3
    req.Field4 = "1";               //Field4
    req.Field5 = "1";               //Field5
    req.TimeZoneID = "1";           //TimeZoneID
    req.VirtualMeetingLink = "1";   //VirtualMeetingLink
    req.PartyShoppingUrl = "1";     //PartyShoppingUrl
    req.PartyExternalID = 1;        //PartyExternalID

    //Send Request to Server and Get Response
    UpdatePartyResponse res = api.UpdateParty(req);

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
    Dim req as new UpdatePartyRequest()

    req.PartyID = 1
    req.PartyType = 1
    req.PartyStatusType = 1
    req.HostID = 1
    req.DistributorID = 1
    req.StartDate = DateTime.Today
    req.CloseDate = DateTime.Today
    req.Description = "1"
    req.EventStart = DateTime.Today
    req.EventEnd = DateTime.Today
    req.LanguageID = 1
    req.Information = "1"
    req.BookingPartyID = 1
    req.Field1 = "1"
    req.Field2 = "1"
    req.Field3 = "1"
    req.Field4 = "1"
    req.Field5 = "1"
    req.TimeZoneID = "1"
    req.VirtualMeetingLink = "1"
    req.PartyShoppingUrl = "1"
    req.PartyExternalID = 1

    'Send Request to Server and Get Response
    Dim res As UpdatePartyResponse = api.UpdateParty(req)

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

    $req->PartyID = 1;
    $req->PartyType = 1;
    $req->PartyStatusType = 1;
    $req->HostID = 1;
    $req->DistributorID = 1;
    $req->StartDate = 1;
    $req->CloseDate = 1;
    $req->Description = "1";
    $req->EventStart = 1;
    $req->EventEnd = 1;
    $req->LanguageID = 1;
    $req->Information = "1";
    $req->BookingPartyID = 1;
    $req->Field1 = "1";
    $req->Field2 = "1";
    $req->Field3 = "1";
    $req->Field4 = "1";
    $req->Field5 = "1";
    $req->TimeZoneID = "1";
    $req->VirtualMeetingLink = "1";
    $req->PartyShoppingUrl = "1";
    $req->PartyExternalID = 1;

    //Send Request to Server and Get Response
    $res = $api.UpdateParty($req);

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
    UpdatePartyRequest req = new UpdatePartyRequest();

    req.setPartyID(1);
    req.setPartyType(1);
    req.setPartyStatusType(1);
    req.setHostID(1);
    req.setDistributorID(1);
    req.setStartDate(1);
    req.setCloseDate(1);
    req.setDescription("1");
    req.setEventStart(1);
    req.setEventEnd(1);
    req.setLanguageID(1);
    req.setInformation("1");
    req.setBookingPartyID(1);
    req.setField1("1");
    req.setField2("1");
    req.setField3("1");
    req.setField4("1");
    req.setField5("1");
    req.setTimeZoneID("1");
    req.setVirtualMeetingLink("1");
    req.setPartyShoppingUrl("1");
    req.setPartyExternalID(1);

    //Send Request to Server and Get Response
    UpdatePartyResponse res = api.getExigoApiSoap().updateParty(req, auth);

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

### GetParties

> Gets Parties list

| | |
|---|---|
| Category | Party Plan |
| REST | `GET /3.0/party?partyID=1` |
| SOAP action | `https://api.exigo.com/GetParties` |
| WSDL elements | `GetPartiesRequest` → `GetPartiesResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetParties |

#### Input

**`GetPartiesRequest`**

| Property | Type | Notes |
|---|---|---|
| `PartyID` | `Int32` | Optional. |
| `HostID` | `Int32` | Optional. |
| `DistributorID` | `Int32` | Optional. |
| `PartyStatusType` | `Int32` | Optional. Party Status.<br>**Lookup:** company-specific list (see company-lists.md) |
| `BookingPartyID` | `Int32` | Optional. BookingPartyID. |
| `Field1` | `String` | Optional. Field1. |
| `Field2` | `String` | Optional. Field2. |
| `Field3` | `String` | Optional. Field3. |
| `Field4` | `String` | Optional. Field4. |
| `Field5` | `String` | Optional. Field5. |
| `PartyExternalID` | `Guid` | Optional. PartyExternalID. |

#### Output

**`GetPartiesResponse`**

| Property | Type | Notes |
|---|---|---|
| `Parties` | `PartyResponse[]` |  |

**`PartyResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `PartyID` | `Int32` |  |
| &nbsp;&nbsp;↳ `PartyType` | `Int32` | Party type.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `PartyStatusType` | `Int32` | Party Status.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `HostID` | `Int32` |  |
| &nbsp;&nbsp;↳ `DistributorID` | `Int32` |  |
| &nbsp;&nbsp;↳ `StartDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `CloseDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `Description` | `String` |  |
| &nbsp;&nbsp;↳ `EventStart` | `DateTime` |  |
| &nbsp;&nbsp;↳ `EventEnd` | `DateTime` |  |
| &nbsp;&nbsp;↳ `LanguageID` | `Int32` | Customize the web experience by setting this.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Information` | `String` |  |
| &nbsp;&nbsp;↳ `Address` | `PartyAddress` |  |
| &nbsp;&nbsp;↳ `BookingPartyID` | `Int32` |  |
| &nbsp;&nbsp;↳ `Field1` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field2` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field3` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field4` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field5` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `PartyShoppingUrl` | `String` |  |
| &nbsp;&nbsp;↳ `PartyExternalID` | `Guid` |  |
| &nbsp;&nbsp;↳ `TimeZoneID` | `String` |  |
| &nbsp;&nbsp;↳ `VirtualMeetingLink` | `String` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/party?partyID=1
  &hostID=1
  &distributorID=1
  &partyStatusType=1
  &bookingPartyID=1
  &field1=1
  &field2=1
  &field3=1
  &field4=1
  &field5=1
  &partyExternalID=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "parties": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetParties"

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
    <GetPartiesRequest xmlns="http://api.exigo.com/">
      <PartyID>int</PartyID>
      <HostID>int</HostID>
      <DistributorID>int</DistributorID>
      <PartyStatusType>int</PartyStatusType>
      <BookingPartyID>int</BookingPartyID>
      <Field1>string</Field1>
      <Field2>string</Field2>
      <Field3>string</Field3>
      <Field4>string</Field4>
      <Field5>string</Field5>
      <PartyExternalID>guid</PartyExternalID>
    </GetPartiesRequest>
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
    <GetPartiesResult xmlns="http://api.exigo.com/">
      <Parties>
        <PartyResponse>
          <PartyID>int</PartyID>
          <PartyType>int</PartyType>
          <PartyStatusType>int</PartyStatusType>
          <HostID>int</HostID>
          <DistributorID>int</DistributorID>
          <StartDate>dateTime</StartDate>
          <CloseDate>dateTime</CloseDate>
          <Description>string</Description>
          <EventStart>dateTime</EventStart>
          <EventEnd>dateTime</EventEnd>
          <LanguageID>int</LanguageID>
          <Information>string</Information>
          <Address>
            <Address1>string</Address1>
            <Address2>string</Address2>
            <City>string</City>
            <State>string</State>
            <Zip>string</Zip>
            <Country>string</Country>
          </Address>
          <BookingPartyID>int</BookingPartyID>
          <Field1>string</Field1>
          <Field2>string</Field2>
          <Field3>string</Field3>
          <Field4>string</Field4>
          <Field5>string</Field5>
          <PartyShoppingUrl>string</PartyShoppingUrl>
          <PartyExternalID>guid</PartyExternalID>
          <TimeZoneID>string</TimeZoneID>
          <VirtualMeetingLink>string</VirtualMeetingLink>
        </PartyResponse>
      </Parties>
    </GetPartiesResult>
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
    var req = new GetPartiesRequest();

    req.PartyID = 1;
    req.HostID = 1;
    req.DistributorID = 1;
    req.PartyStatusType = 1;        //Party Status
    req.BookingPartyID = 1;         //BookingPartyID
    req.Field1 = "1";               //Field1
    req.Field2 = "1";               //Field2
    req.Field3 = "1";               //Field3
    req.Field4 = "1";               //Field4
    req.Field5 = "1";               //Field5
    req.PartyExternalID = 1;        //PartyExternalID

    //Send Request to Server and Get Response
    var res = await api.GetPartiesAsync(req);

    //Now examine the results:

    foreach (var party  in res.Parties)
    {
        Console.WriteLine("PartyID: {0}", party.PartyID);
        Console.WriteLine("PartyType: {0}", party.PartyType);
        Console.WriteLine("PartyStatusType: {0}", party.PartyStatusType);
        Console.WriteLine("HostID: {0}", party.HostID);
        Console.WriteLine("DistributorID: {0}", party.DistributorID);
        Console.WriteLine("StartDate: {0}", party.StartDate);
        Console.WriteLine("CloseDate: {0}", party.CloseDate);
        Console.WriteLine("Description: {0}", party.Description);
        Console.WriteLine("EventStart: {0}", party.EventStart);
        Console.WriteLine("EventEnd: {0}", party.EventEnd);
        Console.WriteLine("Information: {0}", party.Information);
        Console.WriteLine("Address: {0}", party.Address);
        Console.WriteLine("BookingPartyID: {0}", party.BookingPartyID);
        Console.WriteLine("PartyShoppingUrl: {0}", party.PartyShoppingUrl);
        Console.WriteLine("PartyExternalID: {0}", party.PartyExternalID);
        Console.WriteLine("TimeZoneID: {0}", party.TimeZoneID);
        Console.WriteLine("VirtualMeetingLink: {0}", party.VirtualMeetingLink);
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
    GetPartiesRequest req = new GetPartiesRequest();

    req.PartyID = 1;
    req.HostID = 1;
    req.DistributorID = 1;
    req.PartyStatusType = 1;        //Party Status
    req.BookingPartyID = 1;         //BookingPartyID
    req.Field1 = "1";               //Field1
    req.Field2 = "1";               //Field2
    req.Field3 = "1";               //Field3
    req.Field4 = "1";               //Field4
    req.Field5 = "1";               //Field5
    req.PartyExternalID = 1;        //PartyExternalID

    //Send Request to Server and Get Response
    GetPartiesResponse res = api.GetParties(req);

    //Now examine the results:

    foreach (PartyResponse party  in res.Parties)
    {
        Console.WriteLine("PartyID: {0}", party.PartyID);
        Console.WriteLine("PartyType: {0}", party.PartyType);
        Console.WriteLine("PartyStatusType: {0}", party.PartyStatusType);
        Console.WriteLine("HostID: {0}", party.HostID);
        Console.WriteLine("DistributorID: {0}", party.DistributorID);
        Console.WriteLine("StartDate: {0}", party.StartDate);
        Console.WriteLine("CloseDate: {0}", party.CloseDate);
        Console.WriteLine("Description: {0}", party.Description);
        Console.WriteLine("EventStart: {0}", party.EventStart);
        Console.WriteLine("EventEnd: {0}", party.EventEnd);
        Console.WriteLine("Information: {0}", party.Information);
        Console.WriteLine("Address: {0}", party.Address);
        Console.WriteLine("BookingPartyID: {0}", party.BookingPartyID);
        Console.WriteLine("PartyShoppingUrl: {0}", party.PartyShoppingUrl);
        Console.WriteLine("PartyExternalID: {0}", party.PartyExternalID);
        Console.WriteLine("TimeZoneID: {0}", party.TimeZoneID);
        Console.WriteLine("VirtualMeetingLink: {0}", party.VirtualMeetingLink);
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
    Dim req as new GetPartiesRequest()

    req.PartyID = 1
    req.HostID = 1
    req.DistributorID = 1
    req.PartyStatusType = 1
    req.BookingPartyID = 1
    req.Field1 = "1"
    req.Field2 = "1"
    req.Field3 = "1"
    req.Field4 = "1"
    req.Field5 = "1"
    req.PartyExternalID = 1

    'Send Request to Server and Get Response
    Dim res As GetPartiesResponse = api.GetParties(req)

    'Now examine the results:

    For Each party As PartyResponse In res.Parties
        Console.WriteLine("PartyID: {0}", party.PartyID)
        Console.WriteLine("PartyType: {0}", party.PartyType)
        Console.WriteLine("PartyStatusType: {0}", party.PartyStatusType)
        Console.WriteLine("HostID: {0}", party.HostID)
        Console.WriteLine("DistributorID: {0}", party.DistributorID)
        Console.WriteLine("StartDate: {0}", party.StartDate)
        Console.WriteLine("CloseDate: {0}", party.CloseDate)
        Console.WriteLine("Description: {0}", party.Description)
        Console.WriteLine("EventStart: {0}", party.EventStart)
        Console.WriteLine("EventEnd: {0}", party.EventEnd)
        Console.WriteLine("Information: {0}", party.Information)
        Console.WriteLine("Address: {0}", party.Address)
        Console.WriteLine("BookingPartyID: {0}", party.BookingPartyID)
        Console.WriteLine("PartyShoppingUrl: {0}", party.PartyShoppingUrl)
        Console.WriteLine("PartyExternalID: {0}", party.PartyExternalID)
        Console.WriteLine("TimeZoneID: {0}", party.TimeZoneID)
        Console.WriteLine("VirtualMeetingLink: {0}", party.VirtualMeetingLink)
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

    $req->PartyID = 1;
    $req->HostID = 1;
    $req->DistributorID = 1;
    $req->PartyStatusType = 1;
    $req->BookingPartyID = 1;
    $req->Field1 = "1";
    $req->Field2 = "1";
    $req->Field3 = "1";
    $req->Field4 = "1";
    $req->Field5 = "1";
    $req->PartyExternalID = 1;

    //Send Request to Server and Get Response
    $res = $api.GetParties($req);

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
    GetPartiesRequest req = new GetPartiesRequest();

    req.setPartyID(1);
    req.setHostID(1);
    req.setDistributorID(1);
    req.setPartyStatusType(1);
    req.setBookingPartyID(1);
    req.setField1("1");
    req.setField2("1");
    req.setField3("1");
    req.setField4("1");
    req.setField5("1");
    req.setPartyExternalID(1);

    //Send Request to Server and Get Response
    GetPartiesResponse res = api.getExigoApiSoap().getParties(req, auth);

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

### GetPartyGuests

> Gets a list of guests belonging to a party

| | |
|---|---|
| Category | Party Plan |
| REST | `GET /3.0/party/guest?partyID=1` |
| SOAP action | `https://api.exigo.com/GetPartyGuests` |
| WSDL elements | `GetPartyGuestsRequest` → `GetPartyGuestsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetPartyGuests |

#### Input

**`GetPartyGuestsRequest`**

| Property | Type | Notes |
|---|---|---|
| `PartyID` | `Int32` | The party's unique identifier. |

#### Output

**`GetPartyGuestsResponse`**

| Property | Type | Notes |
|---|---|---|
| `Guests` | `GuestResponse[]` |  |

**`GuestResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `GuestID` | `Int32` |  |
| &nbsp;&nbsp;↳ `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| &nbsp;&nbsp;↳ `HostID` | `Int32` |  |
| &nbsp;&nbsp;↳ `FirstName` | `String` |  |
| &nbsp;&nbsp;↳ `MiddleName` | `String` |  |
| &nbsp;&nbsp;↳ `LastName` | `String` |  |
| &nbsp;&nbsp;↳ `NameSuffix` | `String` |  |
| &nbsp;&nbsp;↳ `Company` | `String` |  |
| &nbsp;&nbsp;↳ `Gender` | `Gender` | Obsolete field. Please consider upgrading to GenderID.<br>**Values:** `Unknown`, `Male`, `Female` |
| &nbsp;&nbsp;↳ `GuestStatus` | `Int32` |  |
| &nbsp;&nbsp;↳ `LanguageID` | `Int32` | Customize the web experience by setting this.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Address1` | `String` |  |
| &nbsp;&nbsp;↳ `Address2` | `String` |  |
| &nbsp;&nbsp;↳ `Address3` | `String` |  |
| &nbsp;&nbsp;↳ `City` | `String` |  |
| &nbsp;&nbsp;↳ `County` | `String` |  |
| &nbsp;&nbsp;↳ `State` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Zip` | `String` |  |
| &nbsp;&nbsp;↳ `Country` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Phone` | `String` |  |
| &nbsp;&nbsp;↳ `Phone2` | `String` |  |
| &nbsp;&nbsp;↳ `MobilePhone` | `String` |  |
| &nbsp;&nbsp;↳ `Email` | `String` |  |
| &nbsp;&nbsp;↳ `Field1` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field2` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field3` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field4` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field5` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field6` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field7` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field8` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field9` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field10` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field11` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field12` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field13` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field14` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field15` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Date1` | `DateTime` |  |
| &nbsp;&nbsp;↳ `Date2` | `DateTime` |  |
| &nbsp;&nbsp;↳ `Date3` | `DateTime` |  |
| &nbsp;&nbsp;↳ `Date4` | `DateTime` |  |
| &nbsp;&nbsp;↳ `Date5` | `DateTime` |  |
| &nbsp;&nbsp;↳ `CreatedDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `ModifiedDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `CustomerKey` | `String` | Unique alpha numeric identifier for customer record . |
| &nbsp;&nbsp;↳ `GenderID` | `String` | The customer's gender.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `GenderDescription` | `String` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/party/guest?partyID=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "guests": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetPartyGuests"

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
    <GetPartyGuestsRequest xmlns="http://api.exigo.com/">
      <PartyID>int</PartyID>
    </GetPartyGuestsRequest>
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
    <GetPartyGuestsResult xmlns="http://api.exigo.com/">
      <Guests>
        <GuestResponse>
          <GuestID>int</GuestID>
          <CustomerID>int</CustomerID>
          <HostID>int</HostID>
          <FirstName>string</FirstName>
          <MiddleName>string</MiddleName>
          <LastName>string</LastName>
          <NameSuffix>string</NameSuffix>
          <Company>string</Company>
          <Gender>Unknown or Male or Female</Gender>
          <GuestStatus>int</GuestStatus>
          <LanguageID>int</LanguageID>
          <Address1>string</Address1>
          <Address2>string</Address2>
          <Address3>string</Address3>
          <City>string</City>
          <County>string</County>
          <State>string</State>
          <Zip>string</Zip>
          <Country>string</Country>
          <Phone>string</Phone>
          <Phone2>string</Phone2>
          <MobilePhone>string</MobilePhone>
          <Email>string</Email>
          <Field1>string</Field1>
          <Field2>string</Field2>
          <Field3>string</Field3>
          <Field4>string</Field4>
          <Field5>string</Field5>
          <Field6>string</Field6>
          <Field7>string</Field7>
          <Field8>string</Field8>
          <Field9>string</Field9>
          <Field10>string</Field10>
          <Field11>string</Field11>
          <Field12>string</Field12>
          <Field13>string</Field13>
          <Field14>string</Field14>
          <Field15>string</Field15>
          <Date1>dateTime</Date1>
          <Date2>dateTime</Date2>
          <Date3>dateTime</Date3>
          <Date4>dateTime</Date4>
          <Date5>dateTime</Date5>
          <CreatedDate>dateTime</CreatedDate>
          <ModifiedDate>dateTime</ModifiedDate>
          <CustomerKey>string</CustomerKey>
          <GenderID>string</GenderID>
          <GenderDescription>string</GenderDescription>
        </GuestResponse>
      </Guests>
    </GetPartyGuestsResult>
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
    var req = new GetPartyGuestsRequest();

    req.PartyID = 1;                //The party's unique identifier

    //Send Request to Server and Get Response
    var res = await api.GetPartyGuestsAsync(req);

    //Now examine the results:

    foreach (var guest  in res.Guests)
    {
        Console.WriteLine("GuestID: {0}", guest.GuestID);
        Console.WriteLine("CustomerID: {0}", guest.CustomerID);
        Console.WriteLine("HostID: {0}", guest.HostID);
        Console.WriteLine("FirstName: {0}", guest.FirstName);
        Console.WriteLine("MiddleName: {0}", guest.MiddleName);
        Console.WriteLine("LastName: {0}", guest.LastName);
        Console.WriteLine("NameSuffix: {0}", guest.NameSuffix);
        Console.WriteLine("Company: {0}", guest.Company);
        Console.WriteLine("GuestStatus: {0}", guest.GuestStatus);
        Console.WriteLine("Address1: {0}", guest.Address1);
        Console.WriteLine("Address2: {0}", guest.Address2);
        Console.WriteLine("Address3: {0}", guest.Address3);
        Console.WriteLine("City: {0}", guest.City);
        Console.WriteLine("County: {0}", guest.County);
        Console.WriteLine("Zip: {0}", guest.Zip);
        Console.WriteLine("Phone: {0}", guest.Phone);
        Console.WriteLine("Phone2: {0}", guest.Phone2);
        Console.WriteLine("MobilePhone: {0}", guest.MobilePhone);
        Console.WriteLine("Email: {0}", guest.Email);
        Console.WriteLine("Date1: {0}", guest.Date1);
        Console.WriteLine("Date2: {0}", guest.Date2);
        Console.WriteLine("Date3: {0}", guest.Date3);
        Console.WriteLine("Date4: {0}", guest.Date4);
        Console.WriteLine("Date5: {0}", guest.Date5);
        Console.WriteLine("CreatedDate: {0}", guest.CreatedDate);
        Console.WriteLine("ModifiedDate: {0}", guest.ModifiedDate);
        Console.WriteLine("CustomerKey: {0}", guest.CustomerKey);
        Console.WriteLine("GenderDescription: {0}", guest.GenderDescription);
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
    GetPartyGuestsRequest req = new GetPartyGuestsRequest();

    req.PartyID = 1;                //The party's unique identifier

    //Send Request to Server and Get Response
    GetPartyGuestsResponse res = api.GetPartyGuests(req);

    //Now examine the results:

    foreach (GuestResponse guest  in res.Guests)
    {
        Console.WriteLine("GuestID: {0}", guest.GuestID);
        Console.WriteLine("CustomerID: {0}", guest.CustomerID);
        Console.WriteLine("HostID: {0}", guest.HostID);
        Console.WriteLine("FirstName: {0}", guest.FirstName);
        Console.WriteLine("MiddleName: {0}", guest.MiddleName);
        Console.WriteLine("LastName: {0}", guest.LastName);
        Console.WriteLine("NameSuffix: {0}", guest.NameSuffix);
        Console.WriteLine("Company: {0}", guest.Company);
        Console.WriteLine("GuestStatus: {0}", guest.GuestStatus);
        Console.WriteLine("Address1: {0}", guest.Address1);
        Console.WriteLine("Address2: {0}", guest.Address2);
        Console.WriteLine("Address3: {0}", guest.Address3);
        Console.WriteLine("City: {0}", guest.City);
        Console.WriteLine("County: {0}", guest.County);
        Console.WriteLine("Zip: {0}", guest.Zip);
        Console.WriteLine("Phone: {0}", guest.Phone);
        Console.WriteLine("Phone2: {0}", guest.Phone2);
        Console.WriteLine("MobilePhone: {0}", guest.MobilePhone);
        Console.WriteLine("Email: {0}", guest.Email);
        Console.WriteLine("Date1: {0}", guest.Date1);
        Console.WriteLine("Date2: {0}", guest.Date2);
        Console.WriteLine("Date3: {0}", guest.Date3);
        Console.WriteLine("Date4: {0}", guest.Date4);
        Console.WriteLine("Date5: {0}", guest.Date5);
        Console.WriteLine("CreatedDate: {0}", guest.CreatedDate);
        Console.WriteLine("ModifiedDate: {0}", guest.ModifiedDate);
        Console.WriteLine("CustomerKey: {0}", guest.CustomerKey);
        Console.WriteLine("GenderDescription: {0}", guest.GenderDescription);
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
    Dim req as new GetPartyGuestsRequest()

    req.PartyID = 1

    'Send Request to Server and Get Response
    Dim res As GetPartyGuestsResponse = api.GetPartyGuests(req)

    'Now examine the results:

    For Each guest As GuestResponse In res.Guests
        Console.WriteLine("GuestID: {0}", guest.GuestID)
        Console.WriteLine("CustomerID: {0}", guest.CustomerID)
        Console.WriteLine("HostID: {0}", guest.HostID)
        Console.WriteLine("FirstName: {0}", guest.FirstName)
        Console.WriteLine("MiddleName: {0}", guest.MiddleName)
        Console.WriteLine("LastName: {0}", guest.LastName)
        Console.WriteLine("NameSuffix: {0}", guest.NameSuffix)
        Console.WriteLine("Company: {0}", guest.Company)
        Console.WriteLine("GuestStatus: {0}", guest.GuestStatus)
        Console.WriteLine("Address1: {0}", guest.Address1)
        Console.WriteLine("Address2: {0}", guest.Address2)
        Console.WriteLine("Address3: {0}", guest.Address3)
        Console.WriteLine("City: {0}", guest.City)
        Console.WriteLine("County: {0}", guest.County)
        Console.WriteLine("Zip: {0}", guest.Zip)
        Console.WriteLine("Phone: {0}", guest.Phone)
        Console.WriteLine("Phone2: {0}", guest.Phone2)
        Console.WriteLine("MobilePhone: {0}", guest.MobilePhone)
        Console.WriteLine("Email: {0}", guest.Email)
        Console.WriteLine("Date1: {0}", guest.Date1)
        Console.WriteLine("Date2: {0}", guest.Date2)
        Console.WriteLine("Date3: {0}", guest.Date3)
        Console.WriteLine("Date4: {0}", guest.Date4)
        Console.WriteLine("Date5: {0}", guest.Date5)
        Console.WriteLine("CreatedDate: {0}", guest.CreatedDate)
        Console.WriteLine("ModifiedDate: {0}", guest.ModifiedDate)
        Console.WriteLine("CustomerKey: {0}", guest.CustomerKey)
        Console.WriteLine("GenderDescription: {0}", guest.GenderDescription)
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

    $req->PartyID = 1;

    //Send Request to Server and Get Response
    $res = $api.GetPartyGuests($req);

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
    GetPartyGuestsRequest req = new GetPartyGuestsRequest();

    req.setPartyID(1);

    //Send Request to Server and Get Response
    GetPartyGuestsResponse res = api.getExigoApiSoap().getPartyGuests(req, auth);

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

### AddPartyGuests

> Adds one or more guests to a party.

| | |
|---|---|
| Category | Party Plan |
| REST | `POST /3.0/party/guest` |
| SOAP action | `https://api.exigo.com/AddPartyGuests` |
| WSDL elements | `AddPartyGuestsRequest` → `AddPartyGuestsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=AddPartyGuests |

#### Input

**`AddPartyGuestsRequest`**

| Property | Type | Notes |
|---|---|---|
| `PartyID` | `Int32` | The unique identifier of the party. |
| `GuestIDs` | `Int32[]` | The unique identifiers of the guests you want to add to the party. |

#### Output

**`AddPartyGuestsResponse`**

_No properties._

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/party/guest HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "partyID": 1,
  "guestIDs": null
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
SOAPAction: "https://api.exigo.com/AddPartyGuests"

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
    <AddPartyGuestsRequest xmlns="http://api.exigo.com/">
      <PartyID>int</PartyID>
      <GuestIDs>
        <int>int</int>
      </GuestIDs>
    </AddPartyGuestsRequest>
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
    <AddPartyGuestsResult xmlns="http://api.exigo.com/" />
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
    var req = new AddPartyGuestsRequest();

    req.PartyID = 1;                //The unique identifier of the party

    //Add GuestIDs
    var guestids = new List<Int32>();
    guestids.Add(1);
    guestids.Add(2);

    //Now attach the list to the request
    req.GuestIDs = guestids.ToArray();

    //Send Request to Server and Get Response
    var res = await api.AddPartyGuestsAsync(req);

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
    AddPartyGuestsRequest req = new AddPartyGuestsRequest();

    req.PartyID = 1;                //The unique identifier of the party

    //Add GuestIDs
    List<Int32> guestids = new List<Int32>();
    guestids.Add(1);
    guestids.Add(2);

    //Now attach the list to the request
    req.GuestIDs = guestids.ToArray();

    //Send Request to Server and Get Response
    AddPartyGuestsResponse res = api.AddPartyGuests(req);

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
    Dim req as new AddPartyGuestsRequest()

    req.PartyID = 1

    'Add GuestIDs
    Dim guestids As New List(Of Int32)()
    guestids.Add(1)
    guestids.Add(2)

    'Now attach the list to the request
    req.GuestIDs = guestids.ToArray()

    'Send Request to Server and Get Response
    Dim res As AddPartyGuestsResponse = api.AddPartyGuests(req)

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

    $req->PartyID = 1;

    //Add GuestIDs

    //Now attach the list to the request
    req.GuestIDs = array(guestID1,guestID2);

    //Send Request to Server and Get Response
    $res = $api.AddPartyGuests($req);

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
    AddPartyGuestsRequest req = new AddPartyGuestsRequest();

    req.setPartyID(1);

    //Add GuestIDs
    ArrayOfSystem.Int32 guestids = new ArrayOfSystem.Int32();

    Int32 guestID1 = new Int32();
    guestids.Add(guestID1);

    Int32 guestID2 = new Int32();
    guestids.Add(guestID2);

    //Now attach the list to the request
    req.setGuestIDs(guestids);

    //Send Request to Server and Get Response
    AddPartyGuestsResponse res = api.getExigoApiSoap().addPartyGuests(req, auth);

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

### RemovePartyGuests

> Removes one or more guests from a party.

| | |
|---|---|
| Category | Party Plan |
| REST | `DELETE /3.0/party/guest` |
| SOAP action | `https://api.exigo.com/RemovePartyGuests` |
| WSDL elements | `RemovePartyGuestsRequest` → `RemovePartyGuestsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=RemovePartyGuests |

#### Input

**`RemovePartyGuestsRequest`**

| Property | Type | Notes |
|---|---|---|
| `PartyID` | `Int32` | The unique identifier of the party. |
| `GuestIDs` | `Int32[]` | Optional. The unique identifiers of the guests you want to add to the party. Leave this field empty to delete all guests from a party. |

#### Output

**`RemovePartyGuestsResponse`**

_No properties._

#### REST example

```http
DELETE https://yourcompany-api.exigo.com/3.0/party/guest HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "partyID": 1,
  "guestIDs": null
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
SOAPAction: "https://api.exigo.com/RemovePartyGuests"

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
    <RemovePartyGuestsRequest xmlns="http://api.exigo.com/">
      <PartyID>int</PartyID>
      <GuestIDs>
        <int>int</int>
      </GuestIDs>
    </RemovePartyGuestsRequest>
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
    <RemovePartyGuestsResult xmlns="http://api.exigo.com/" />
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
    var req = new RemovePartyGuestsRequest();

    req.PartyID = 1;                //The unique identifier of the party

    //Add GuestIDs
    var guestids = new List<Int32>();
    guestids.Add(1);
    guestids.Add(2);

    //Now attach the list to the request
    req.GuestIDs = guestids.ToArray();

    //Send Request to Server and Get Response
    var res = await api.RemovePartyGuestsAsync(req);

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
    RemovePartyGuestsRequest req = new RemovePartyGuestsRequest();

    req.PartyID = 1;                //The unique identifier of the party

    //Add GuestIDs
    List<Int32> guestids = new List<Int32>();
    guestids.Add(1);
    guestids.Add(2);

    //Now attach the list to the request
    req.GuestIDs = guestids.ToArray();

    //Send Request to Server and Get Response
    RemovePartyGuestsResponse res = api.RemovePartyGuests(req);

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
    Dim req as new RemovePartyGuestsRequest()

    req.PartyID = 1

    'Add GuestIDs
    Dim guestids As New List(Of Int32)()
    guestids.Add(1)
    guestids.Add(2)

    'Now attach the list to the request
    req.GuestIDs = guestids.ToArray()

    'Send Request to Server and Get Response
    Dim res As RemovePartyGuestsResponse = api.RemovePartyGuests(req)

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

    $req->PartyID = 1;

    //Add GuestIDs

    //Now attach the list to the request
    req.GuestIDs = array(guestID1,guestID2);

    //Send Request to Server and Get Response
    $res = $api.RemovePartyGuests($req);

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
    RemovePartyGuestsRequest req = new RemovePartyGuestsRequest();

    req.setPartyID(1);

    //Add GuestIDs
    ArrayOfSystem.Int32 guestids = new ArrayOfSystem.Int32();

    Int32 guestID1 = new Int32();
    guestids.Add(guestID1);

    Int32 guestID2 = new Int32();
    guestids.Add(guestID2);

    //Now attach the list to the request
    req.setGuestIDs(guestids);

    //Send Request to Server and Get Response
    RemovePartyGuestsResponse res = api.getExigoApiSoap().removePartyGuests(req, auth);

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

### CreateGuest

> Creates a new guest. Can optionally be put in a party.

| | |
|---|---|
| Category | Party Plan |
| REST | `POST /3.0/guest` |
| SOAP action | `https://api.exigo.com/CreateGuest` |
| WSDL elements | `CreateGuestRequest` → `CreateGuestResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateGuest |

#### Input

**`CreateGuestRequest`**

| Property | Type | Notes |
|---|---|---|
| `HostID` | `Int32` | The unique identifier of the host that the guest was created/referred by. |
| `PartyID` | `Int32` | Optional. If set, the guest will be placed in the provided party. |
| `CustomerID` | `Int32` | Optional. If set, the guest will be linked to the provided customer account. |
| `FirstName` | `String` | Optional. The guest's first name. |
| `MiddleName` | `String` | Optional. The guest's middle name. |
| `LastName` | `String` | Optional. The guest's last name. |
| `NameSuffix` | `String` | Optional. The guest's name suffix. |
| `Company` | `String` | Optional. The guest's company name. |
| `Gender` | `Gender` | Optional. Obsolete field. Please consider upgrading to GenderID.<br>**Values:** `Unknown`, `Male`, `Female` |
| `LanguageID` | `Int32` | Optional. The guest's preferred language. Defaults to 0. |
| `GuestStatus` | `Int32` | Optional. The guest's status as defined by the company. Defaults to 1. |
| `Address1` | `String` | Optional. |
| `Address2` | `String` | Optional. |
| `Address3` | `String` | Optional. |
| `City` | `String` | Optional. |
| `County` | `String` | Optional. |
| `State` | `String` | Optional. The state of the guest's address. This field is required if Address1 is provided. |
| `Zip` | `String` | Optional. |
| `Country` | `String` | Optional. The country of the guest's address. This field is required if Address1 is provided. |
| `Phone` | `String` | Optional. |
| `Phone2` | `String` | Optional. |
| `MobilePhone` | `String` | Optional. |
| `Email` | `String` | Optional. |
| `Field1` | `String` | Optional. |
| `Field2` | `String` | Optional. |
| `Field3` | `String` | Optional. |
| `Field4` | `String` | Optional. |
| `Field5` | `String` | Optional. |
| `Field6` | `String` | Optional. |
| `Field7` | `String` | Optional. |
| `Field8` | `String` | Optional. |
| `Field9` | `String` | Optional. |
| `Field10` | `String` | Optional. |
| `Field11` | `String` | Optional. |
| `Field12` | `String` | Optional. |
| `Field13` | `String` | Optional. |
| `Field14` | `String` | Optional. |
| `Field15` | `String` | Optional. |
| `Notes` | `String` | Optional. Any additional notes about the guest. |
| `EntryDate` | `DateTime` | The date the guest was created. The provided date must be greater than 1/1/1900. |
| `CustomerKey` | `String` | Optional. If set, the guest will be linked to the provided customer account. |
| `GenderID` | `String` | Optional. The customer's gender.<br>**Lookup:** company-specific list (see company-lists.md) |

#### Output

**`CreateGuestResponse`**

| Property | Type | Notes |
|---|---|---|
| `GuestID` | `Int32` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/guest HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "hostID": 1,
  "partyID": 1,
  "customerID": 1,
  "firstName": "John",
  "lastName": "Doe",
  "company": "ACME, Inc.",
  "guestStatus": 1,
  "address1": "123 Some Street",
  "state": "TX",
  "country": "US",
  "email": "joecool@me.com",
  "customerKey": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "guestID": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateGuest"

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
    <CreateGuestRequest xmlns="http://api.exigo.com/">
      <Date1>dateTime</Date1>
      <Date2>dateTime</Date2>
      <Date3>dateTime</Date3>
      <Date4>dateTime</Date4>
      <Date5>dateTime</Date5>
      <HostID>int</HostID>
      <PartyID>int</PartyID>
      <CustomerID>int</CustomerID>
      <FirstName>string</FirstName>
      <MiddleName>string</MiddleName>
      <LastName>string</LastName>
      <NameSuffix>string</NameSuffix>
      <Company>string</Company>
      <Gender>Unknown or Male or Female</Gender>
      <LanguageID>int</LanguageID>
      <GuestStatus>int</GuestStatus>
      <Address1>string</Address1>
      <Address2>string</Address2>
      <Address3>string</Address3>
      <City>string</City>
      <County>string</County>
      <State>string</State>
      <Zip>string</Zip>
      <Country>string</Country>
      <Phone>string</Phone>
      <Phone2>string</Phone2>
      <MobilePhone>string</MobilePhone>
      <Email>string</Email>
      <Field1>string</Field1>
      <Field2>string</Field2>
      <Field3>string</Field3>
      <Field4>string</Field4>
      <Field5>string</Field5>
      <Field6>string</Field6>
      <Field7>string</Field7>
      <Field8>string</Field8>
      <Field9>string</Field9>
      <Field10>string</Field10>
      <Field11>string</Field11>
      <Field12>string</Field12>
      <Field13>string</Field13>
      <Field14>string</Field14>
      <Field15>string</Field15>
      <Notes>string</Notes>
      <EntryDate>dateTime</EntryDate>
      <CustomerKey>string</CustomerKey>
      <GenderID>string</GenderID>
    </CreateGuestRequest>
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
    <CreateGuestResult xmlns="http://api.exigo.com/">
      <GuestID>int</GuestID>
    </CreateGuestResult>
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
    var req = new CreateGuestRequest();

    req.HostID = 1;                 //The unique identifier of the host that the guest was created/referred by
    req.PartyID = 1;                //If set, the guest will be placed in the provided party
    req.CustomerID = 1;             //If set, the guest will be linked to the provided customer account
    req.FirstName = "John";         //The guest's first name
    req.LastName = "Doe";           //The guest's last name
    req.Company = "ACME, Inc.";     //The guest's company name
    req.GuestStatus = 1;            //The guest's status as defined by the company. Defaults to 1.
    req.Address1 = "123 Some Street";
    req.State = "TX";               //The state of the guest's address. This field is required if Address1 is provided.
    req.Country = "US";             //The country of the guest's address. This field is required if Address1 is provided.
    req.Email = "joecool@me.com";
    req.CustomerKey = "1";          // If set, the guest will be linked to the provided customer account

    //Send Request to Server and Get Response
    var res = await api.CreateGuestAsync(req);

    //Now examine the results:
    Console.WriteLine("GuestID: {0}", res.GuestID);
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
    CreateGuestRequest req = new CreateGuestRequest();

    req.HostID = 1;                 //The unique identifier of the host that the guest was created/referred by
    req.PartyID = 1;                //If set, the guest will be placed in the provided party
    req.CustomerID = 1;             //If set, the guest will be linked to the provided customer account
    req.FirstName = "John";         //The guest's first name
    req.LastName = "Doe";           //The guest's last name
    req.Company = "ACME, Inc.";     //The guest's company name
    req.GuestStatus = 1;            //The guest's status as defined by the company. Defaults to 1.
    req.Address1 = "123 Some Street";
    req.State = "TX";               //The state of the guest's address. This field is required if Address1 is provided.
    req.Country = "US";             //The country of the guest's address. This field is required if Address1 is provided.
    req.Email = "joecool@me.com";
    req.CustomerKey = "1";          // If set, the guest will be linked to the provided customer account

    //Send Request to Server and Get Response
    CreateGuestResponse res = api.CreateGuest(req);

    //Now examine the results:
    Console.WriteLine("GuestID: {0}", res.GuestID);
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
    Dim req as new CreateGuestRequest()

    req.HostID = 1
    req.PartyID = 1
    req.CustomerID = 1
    req.FirstName = "John"
    req.LastName = "Doe"
    req.Company = "ACME, Inc."
    req.GuestStatus = 1
    req.Address1 = "123 Some Street"
    req.State = "TX"
    req.Country = "US"
    req.Email = "joecool@me.com"
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As CreateGuestResponse = api.CreateGuest(req)

    'Now examine the results:
    Console.WriteLine("GuestID: {0}", res.GuestID)
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

    $req->HostID = 1;
    $req->PartyID = 1;
    $req->CustomerID = 1;
    $req->FirstName = "John";
    $req->LastName = "Doe";
    $req->Company = "ACME, Inc.";
    $req->GuestStatus = 1;
    $req->Address1 = "123 Some Street";
    $req->State = "TX";
    $req->Country = "US";
    $req->Email = "joecool@me.com";
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.CreateGuest($req);

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
    CreateGuestRequest req = new CreateGuestRequest();

    req.setHostID(1);
    req.setPartyID(1);
    req.setCustomerID(1);
    req.setFirstName("John");
    req.setLastName("Doe");
    req.setCompany("ACME, Inc.");
    req.setGuestStatus(1);
    req.setAddress1("123 Some Street");
    req.setState("TX");
    req.setCountry("US");
    req.setEmail("joecool@me.com");
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    CreateGuestResponse res = api.getExigoApiSoap().createGuest(req, auth);

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

### UpdateGuest

> Updates one or more fields on an existing guest.

| | |
|---|---|
| Category | Party Plan |
| REST | `PATCH /3.0/guest` |
| SOAP action | `https://api.exigo.com/UpdateGuest` |
| WSDL elements | `UpdateGuestRequest` → `UpdateGuestResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateGuest |

#### Input

**`UpdateGuestRequest`**

| Property | Type | Notes |
|---|---|---|
| `GuestID` | `Int32` | The unique identifier of the guest. |
| `CustomerID` | `Int32` | Optional. Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |
| `FirstName` | `String` | Optional. |
| `MiddleName` | `String` | Optional. |
| `LastName` | `String` | Optional. |
| `NameSuffix` | `String` | Optional. |
| `Company` | `String` | Optional. |
| `Gender` | `Gender` | Optional. Obsolete field. Please consider upgrading to GenderID. Defaults to Unknown.<br>**Values:** `Unknown`, `Male`, `Female` |
| `GuestStatus` | `Int32` | Optional. |
| `LanguageID` | `Int32` | Optional. Customize the web experience by setting this.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Address1` | `String` | Optional. |
| `Address2` | `String` | Optional. |
| `Address3` | `String` | Optional. |
| `City` | `String` | Optional. |
| `County` | `String` | Optional. |
| `State` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Zip` | `String` | Optional. |
| `Country` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Phone` | `String` | Optional. |
| `Phone2` | `String` | Optional. |
| `MobilePhone` | `String` | Optional. |
| `Email` | `String` | Optional. |
| `Field1` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Field2` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Field3` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Field4` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Field5` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Field6` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Field7` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Field8` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Field9` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Field10` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Field11` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Field12` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Field13` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Field14` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Field15` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Date1` | `DateTime` | Optional. |
| `Date2` | `DateTime` | Optional. |
| `Date3` | `DateTime` | Optional. |
| `Date4` | `DateTime` | Optional. |
| `Date5` | `DateTime` | Optional. |
| `Notes` | `String` | Optional. |
| `GenderID` | `String` | Optional. The customer's gender.<br>**Lookup:** company-specific list (see company-lists.md) |

#### Output

**`UpdateGuestResponse`**

_No properties._

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/guest HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "guestID": 1,
  "customerID": 1,
  "customerKey": "1",
  "firstName": null,
  "middleName": null,
  "lastName": null,
  "nameSuffix": null,
  "company": null,
  "guestStatus": 1,
  "address1": null,
  "address2": null,
  "address3": null,
  "city": null,
  "county": null,
  "zip": null,
  "phone": null,
  "phone2": null,
  "mobilePhone": null,
  "email": null,
  "date1": "2026-11-10T00:00:00-06:00",
  "date2": "2026-11-10T00:00:00-06:00",
  "date3": "2026-11-10T00:00:00-06:00",
  "date4": "2026-11-10T00:00:00-06:00",
  "date5": "2026-11-10T00:00:00-06:00",
  "notes": null
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
SOAPAction: "https://api.exigo.com/UpdateGuest"

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
    <UpdateGuestRequest xmlns="http://api.exigo.com/">
      <GuestID>int</GuestID>
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
      <FirstName>string</FirstName>
      <MiddleName>string</MiddleName>
      <LastName>string</LastName>
      <NameSuffix>string</NameSuffix>
      <Company>string</Company>
      <Gender>Unknown or Male or Female</Gender>
      <GuestStatus>int</GuestStatus>
      <LanguageID>int</LanguageID>
      <Address1>string</Address1>
      <Address2>string</Address2>
      <Address3>string</Address3>
      <City>string</City>
      <County>string</County>
      <State>string</State>
      <Zip>string</Zip>
      <Country>string</Country>
      <Phone>string</Phone>
      <Phone2>string</Phone2>
      <MobilePhone>string</MobilePhone>
      <Email>string</Email>
      <Field1>string</Field1>
      <Field2>string</Field2>
      <Field3>string</Field3>
      <Field4>string</Field4>
      <Field5>string</Field5>
      <Field6>string</Field6>
      <Field7>string</Field7>
      <Field8>string</Field8>
      <Field9>string</Field9>
      <Field10>string</Field10>
      <Field11>string</Field11>
      <Field12>string</Field12>
      <Field13>string</Field13>
      <Field14>string</Field14>
      <Field15>string</Field15>
      <Date1>dateTime</Date1>
      <Date2>dateTime</Date2>
      <Date3>dateTime</Date3>
      <Date4>dateTime</Date4>
      <Date5>dateTime</Date5>
      <Notes>string</Notes>
      <GenderID>string</GenderID>
    </UpdateGuestRequest>
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
    <UpdateGuestResult xmlns="http://api.exigo.com/" />
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
    var req = new UpdateGuestRequest();

    req.GuestID = 1;                //The unique identifier of the guest
    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.FirstName = 1;
    req.MiddleName = 1;
    req.LastName = 1;
    req.NameSuffix = 1;
    req.Company = 1;
    req.GuestStatus = 1;
    req.Address1 = 1;
    req.Address2 = 1;
    req.Address3 = 1;
    req.City = 1;
    req.County = 1;
    req.Zip = 1;
    req.Phone = 1;
    req.Phone2 = 1;
    req.MobilePhone = 1;
    req.Email = 1;
    req.Date1 = DateTime.Today;
    req.Date2 = DateTime.Today;
    req.Date3 = DateTime.Today;
    req.Date4 = DateTime.Today;
    req.Date5 = DateTime.Today;
    req.Notes = 1;

    //Send Request to Server and Get Response
    var res = await api.UpdateGuestAsync(req);

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
    UpdateGuestRequest req = new UpdateGuestRequest();

    req.GuestID = 1;                //The unique identifier of the guest
    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.FirstName = 1;
    req.MiddleName = 1;
    req.LastName = 1;
    req.NameSuffix = 1;
    req.Company = 1;
    req.GuestStatus = 1;
    req.Address1 = 1;
    req.Address2 = 1;
    req.Address3 = 1;
    req.City = 1;
    req.County = 1;
    req.Zip = 1;
    req.Phone = 1;
    req.Phone2 = 1;
    req.MobilePhone = 1;
    req.Email = 1;
    req.Date1 = DateTime.Today;
    req.Date2 = DateTime.Today;
    req.Date3 = DateTime.Today;
    req.Date4 = DateTime.Today;
    req.Date5 = DateTime.Today;
    req.Notes = 1;

    //Send Request to Server and Get Response
    UpdateGuestResponse res = api.UpdateGuest(req);

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
    Dim req as new UpdateGuestRequest()

    req.GuestID = 1
    req.CustomerID = 1
    req.CustomerKey = "1"
    req.FirstName = 1
    req.MiddleName = 1
    req.LastName = 1
    req.NameSuffix = 1
    req.Company = 1
    req.GuestStatus = 1
    req.Address1 = 1
    req.Address2 = 1
    req.Address3 = 1
    req.City = 1
    req.County = 1
    req.Zip = 1
    req.Phone = 1
    req.Phone2 = 1
    req.MobilePhone = 1
    req.Email = 1
    req.Date1 = DateTime.Today
    req.Date2 = DateTime.Today
    req.Date3 = DateTime.Today
    req.Date4 = DateTime.Today
    req.Date5 = DateTime.Today
    req.Notes = 1

    'Send Request to Server and Get Response
    Dim res As UpdateGuestResponse = api.UpdateGuest(req)

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

    $req->GuestID = 1;
    $req->CustomerID = 1;
    $req->CustomerKey = "1";
    $req->FirstName = 1;
    $req->MiddleName = 1;
    $req->LastName = 1;
    $req->NameSuffix = 1;
    $req->Company = 1;
    $req->GuestStatus = 1;
    $req->Address1 = 1;
    $req->Address2 = 1;
    $req->Address3 = 1;
    $req->City = 1;
    $req->County = 1;
    $req->Zip = 1;
    $req->Phone = 1;
    $req->Phone2 = 1;
    $req->MobilePhone = 1;
    $req->Email = 1;
    $req->Date1 = 1;
    $req->Date2 = 1;
    $req->Date3 = 1;
    $req->Date4 = 1;
    $req->Date5 = 1;
    $req->Notes = 1;

    //Send Request to Server and Get Response
    $res = $api.UpdateGuest($req);

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
    UpdateGuestRequest req = new UpdateGuestRequest();

    req.setGuestID(1);
    req.setCustomerID(1);
    req.setCustomerKey("1");
    req.setFirstName(1);
    req.setMiddleName(1);
    req.setLastName(1);
    req.setNameSuffix(1);
    req.setCompany(1);
    req.setGuestStatus(1);
    req.setAddress1(1);
    req.setAddress2(1);
    req.setAddress3(1);
    req.setCity(1);
    req.setCounty(1);
    req.setZip(1);
    req.setPhone(1);
    req.setPhone2(1);
    req.setMobilePhone(1);
    req.setEmail(1);
    req.setDate1(1);
    req.setDate2(1);
    req.setDate3(1);
    req.setDate4(1);
    req.setDate5(1);
    req.setNotes(1);

    //Send Request to Server and Get Response
    UpdateGuestResponse res = api.getExigoApiSoap().updateGuest(req, auth);

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

### GetGuests

> Gets a list of guests

| | |
|---|---|
| Category | Party Plan |
| REST | `GET /3.0/guestAuthorization:` |
| SOAP action | `https://api.exigo.com/GetGuests` |
| WSDL elements | `GetGuestsRequest` → `GetGuestsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetGuests |

#### Input

**`GetGuestsRequest`**

| Property | Type | Notes |
|---|---|---|
| `GuestID` | `Int32` | Optional. If set, guests with this unique identifier will be returned. |
| `CustomerID` | `Int32` | Optional. If set, guests with, this customer ID will be returned. Customer IDs are assigned only if they have a corresponding customer account. |
| `HostID` | `Int32` | Optional. If set, guests tied to this host will be returned. |
| `GuestStatuses` | `Int32[]` | Optional. If set, guests with any of these statuses will be returned. |
| `LanguageID` | `Int32` | Optional. The language ID the guests should have. |
| `FirstName` | `String` | Optional. The guest's first name. |
| `MiddleName` | `String` | Optional. The guest's middle name. |
| `LastName` | `String` | Optional. The guest's last name. |
| `NameSuffix` | `String` | Optional. The guest's name suffix. |
| `Company` | `String` | Optional. The guest's company name. |
| `Email` | `String` | Optional. The guest's email address. |
| `Phone` | `String` | Optional. |
| `Phone2` | `String` | Optional. |
| `MobilePhone` | `String` | Optional. |
| `Address1` | `String` | Optional. |
| `Address2` | `String` | Optional. |
| `Address3` | `String` | Optional. |
| `City` | `String` | Optional. |
| `County` | `String` | Optional. |
| `State` | `String` | Optional. |
| `Zip` | `String` | Optional. |
| `Country` | `String` | Optional. |
| `Field1` | `String` | Optional. |
| `Field2` | `String` | Optional. |
| `Field3` | `String` | Optional. |
| `Field4` | `String` | Optional. |
| `Field5` | `String` | Optional. |
| `Field6` | `String` | Optional. |
| `Field7` | `String` | Optional. |
| `Field8` | `String` | Optional. |
| `Field9` | `String` | Optional. |
| `Field10` | `String` | Optional. |
| `Field11` | `String` | Optional. |
| `Field12` | `String` | Optional. |
| `Field13` | `String` | Optional. |
| `Field14` | `String` | Optional. |
| `Field15` | `String` | Optional. |
| `Date1` | `DateTime` | Optional. |
| `Date2` | `DateTime` | Optional. |
| `Date3` | `DateTime` | Optional. |
| `Date4` | `DateTime` | Optional. |
| `Date5` | `DateTime` | Optional. |
| `CreatedDateStart` | `DateTime` | Optional. |
| `CreatedDateEnd` | `DateTime` | Optional. |
| `CustomerKey` | `String` | Optional. If set, guests with, this customer Key will be returned. Customer IDs are assigned only if they have a corresponding customer account. |

#### Output

**`GetGuestsResponse`**

| Property | Type | Notes |
|---|---|---|
| `Guests` | `GuestResponse[]` |  |

**`GuestResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `GuestID` | `Int32` |  |
| &nbsp;&nbsp;↳ `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| &nbsp;&nbsp;↳ `HostID` | `Int32` |  |
| &nbsp;&nbsp;↳ `FirstName` | `String` |  |
| &nbsp;&nbsp;↳ `MiddleName` | `String` |  |
| &nbsp;&nbsp;↳ `LastName` | `String` |  |
| &nbsp;&nbsp;↳ `NameSuffix` | `String` |  |
| &nbsp;&nbsp;↳ `Company` | `String` |  |
| &nbsp;&nbsp;↳ `Gender` | `Gender` | Obsolete field. Please consider upgrading to GenderID.<br>**Values:** `Unknown`, `Male`, `Female` |
| &nbsp;&nbsp;↳ `GuestStatus` | `Int32` |  |
| &nbsp;&nbsp;↳ `LanguageID` | `Int32` | Customize the web experience by setting this.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Address1` | `String` |  |
| &nbsp;&nbsp;↳ `Address2` | `String` |  |
| &nbsp;&nbsp;↳ `Address3` | `String` |  |
| &nbsp;&nbsp;↳ `City` | `String` |  |
| &nbsp;&nbsp;↳ `County` | `String` |  |
| &nbsp;&nbsp;↳ `State` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Zip` | `String` |  |
| &nbsp;&nbsp;↳ `Country` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Phone` | `String` |  |
| &nbsp;&nbsp;↳ `Phone2` | `String` |  |
| &nbsp;&nbsp;↳ `MobilePhone` | `String` |  |
| &nbsp;&nbsp;↳ `Email` | `String` |  |
| &nbsp;&nbsp;↳ `Field1` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field2` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field3` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field4` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field5` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field6` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field7` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field8` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field9` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field10` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field11` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field12` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field13` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field14` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Field15` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Date1` | `DateTime` |  |
| &nbsp;&nbsp;↳ `Date2` | `DateTime` |  |
| &nbsp;&nbsp;↳ `Date3` | `DateTime` |  |
| &nbsp;&nbsp;↳ `Date4` | `DateTime` |  |
| &nbsp;&nbsp;↳ `Date5` | `DateTime` |  |
| &nbsp;&nbsp;↳ `CreatedDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `ModifiedDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `CustomerKey` | `String` | Unique alpha numeric identifier for customer record . |
| &nbsp;&nbsp;↳ `GenderID` | `String` | The customer's gender.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `GenderDescription` | `String` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/guestAuthorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "guests": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetGuests"

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
    <GetGuestsRequest xmlns="http://api.exigo.com/">
      <GuestID>int</GuestID>
      <CustomerID>int</CustomerID>
      <HostID>int</HostID>
      <GuestStatuses>
        <int>int</int>
      </GuestStatuses>
      <LanguageID>int</LanguageID>
      <FirstName>string</FirstName>
      <MiddleName>string</MiddleName>
      <LastName>string</LastName>
      <NameSuffix>string</NameSuffix>
      <Company>string</Company>
      <Email>string</Email>
      <Phone>string</Phone>
      <Phone2>string</Phone2>
      <MobilePhone>string</MobilePhone>
      <Address1>string</Address1>
      <Address2>string</Address2>
      <Address3>string</Address3>
      <City>string</City>
      <County>string</County>
      <State>string</State>
      <Zip>string</Zip>
      <Country>string</Country>
      <Field1>string</Field1>
      <Field2>string</Field2>
      <Field3>string</Field3>
      <Field4>string</Field4>
      <Field5>string</Field5>
      <Field6>string</Field6>
      <Field7>string</Field7>
      <Field8>string</Field8>
      <Field9>string</Field9>
      <Field10>string</Field10>
      <Field11>string</Field11>
      <Field12>string</Field12>
      <Field13>string</Field13>
      <Field14>string</Field14>
      <Field15>string</Field15>
      <Date1>dateTime</Date1>
      <Date2>dateTime</Date2>
      <Date3>dateTime</Date3>
      <Date4>dateTime</Date4>
      <Date5>dateTime</Date5>
      <CreatedDateStart>dateTime</CreatedDateStart>
      <CreatedDateEnd>dateTime</CreatedDateEnd>
      <CustomerKey>string</CustomerKey>
    </GetGuestsRequest>
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
    <GetGuestsResult xmlns="http://api.exigo.com/">
      <Guests>
        <GuestResponse>
          <GuestID>int</GuestID>
          <CustomerID>int</CustomerID>
          <HostID>int</HostID>
          <FirstName>string</FirstName>
          <MiddleName>string</MiddleName>
          <LastName>string</LastName>
          <NameSuffix>string</NameSuffix>
          <Company>string</Company>
          <Gender>Unknown or Male or Female</Gender>
          <GuestStatus>int</GuestStatus>
          <LanguageID>int</LanguageID>
          <Address1>string</Address1>
          <Address2>string</Address2>
          <Address3>string</Address3>
          <City>string</City>
          <County>string</County>
          <State>string</State>
          <Zip>string</Zip>
          <Country>string</Country>
          <Phone>string</Phone>
          <Phone2>string</Phone2>
          <MobilePhone>string</MobilePhone>
          <Email>string</Email>
          <Field1>string</Field1>
          <Field2>string</Field2>
          <Field3>string</Field3>
          <Field4>string</Field4>
          <Field5>string</Field5>
          <Field6>string</Field6>
          <Field7>string</Field7>
          <Field8>string</Field8>
          <Field9>string</Field9>
          <Field10>string</Field10>
          <Field11>string</Field11>
          <Field12>string</Field12>
          <Field13>string</Field13>
          <Field14>string</Field14>
          <Field15>string</Field15>
          <Date1>dateTime</Date1>
          <Date2>dateTime</Date2>
          <Date3>dateTime</Date3>
          <Date4>dateTime</Date4>
          <Date5>dateTime</Date5>
          <CreatedDate>dateTime</CreatedDate>
          <ModifiedDate>dateTime</ModifiedDate>
          <CustomerKey>string</CustomerKey>
          <GenderID>string</GenderID>
          <GenderDescription>string</GenderDescription>
        </GuestResponse>
      </Guests>
    </GetGuestsResult>
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
    var req = new GetGuestsRequest();

    //Send Request to Server and Get Response
    var res = await api.GetGuestsAsync(req);

    //Now examine the results:

    foreach (var guest  in res.Guests)
    {
        Console.WriteLine("GuestID: {0}", guest.GuestID);
        Console.WriteLine("CustomerID: {0}", guest.CustomerID);
        Console.WriteLine("HostID: {0}", guest.HostID);
        Console.WriteLine("FirstName: {0}", guest.FirstName);
        Console.WriteLine("MiddleName: {0}", guest.MiddleName);
        Console.WriteLine("LastName: {0}", guest.LastName);
        Console.WriteLine("NameSuffix: {0}", guest.NameSuffix);
        Console.WriteLine("Company: {0}", guest.Company);
        Console.WriteLine("GuestStatus: {0}", guest.GuestStatus);
        Console.WriteLine("Address1: {0}", guest.Address1);
        Console.WriteLine("Address2: {0}", guest.Address2);
        Console.WriteLine("Address3: {0}", guest.Address3);
        Console.WriteLine("City: {0}", guest.City);
        Console.WriteLine("County: {0}", guest.County);
        Console.WriteLine("Zip: {0}", guest.Zip);
        Console.WriteLine("Phone: {0}", guest.Phone);
        Console.WriteLine("Phone2: {0}", guest.Phone2);
        Console.WriteLine("MobilePhone: {0}", guest.MobilePhone);
        Console.WriteLine("Email: {0}", guest.Email);
        Console.WriteLine("Date1: {0}", guest.Date1);
        Console.WriteLine("Date2: {0}", guest.Date2);
        Console.WriteLine("Date3: {0}", guest.Date3);
        Console.WriteLine("Date4: {0}", guest.Date4);
        Console.WriteLine("Date5: {0}", guest.Date5);
        Console.WriteLine("CreatedDate: {0}", guest.CreatedDate);
        Console.WriteLine("ModifiedDate: {0}", guest.ModifiedDate);
        Console.WriteLine("CustomerKey: {0}", guest.CustomerKey);
        Console.WriteLine("GenderDescription: {0}", guest.GenderDescription);
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
    GetGuestsRequest req = new GetGuestsRequest();

    //Send Request to Server and Get Response
    GetGuestsResponse res = api.GetGuests(req);

    //Now examine the results:

    foreach (GuestResponse guest  in res.Guests)
    {
        Console.WriteLine("GuestID: {0}", guest.GuestID);
        Console.WriteLine("CustomerID: {0}", guest.CustomerID);
        Console.WriteLine("HostID: {0}", guest.HostID);
        Console.WriteLine("FirstName: {0}", guest.FirstName);
        Console.WriteLine("MiddleName: {0}", guest.MiddleName);
        Console.WriteLine("LastName: {0}", guest.LastName);
        Console.WriteLine("NameSuffix: {0}", guest.NameSuffix);
        Console.WriteLine("Company: {0}", guest.Company);
        Console.WriteLine("GuestStatus: {0}", guest.GuestStatus);
        Console.WriteLine("Address1: {0}", guest.Address1);
        Console.WriteLine("Address2: {0}", guest.Address2);
        Console.WriteLine("Address3: {0}", guest.Address3);
        Console.WriteLine("City: {0}", guest.City);
        Console.WriteLine("County: {0}", guest.County);
        Console.WriteLine("Zip: {0}", guest.Zip);
        Console.WriteLine("Phone: {0}", guest.Phone);
        Console.WriteLine("Phone2: {0}", guest.Phone2);
        Console.WriteLine("MobilePhone: {0}", guest.MobilePhone);
        Console.WriteLine("Email: {0}", guest.Email);
        Console.WriteLine("Date1: {0}", guest.Date1);
        Console.WriteLine("Date2: {0}", guest.Date2);
        Console.WriteLine("Date3: {0}", guest.Date3);
        Console.WriteLine("Date4: {0}", guest.Date4);
        Console.WriteLine("Date5: {0}", guest.Date5);
        Console.WriteLine("CreatedDate: {0}", guest.CreatedDate);
        Console.WriteLine("ModifiedDate: {0}", guest.ModifiedDate);
        Console.WriteLine("CustomerKey: {0}", guest.CustomerKey);
        Console.WriteLine("GenderDescription: {0}", guest.GenderDescription);
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
    Dim req as new GetGuestsRequest()

    'Send Request to Server and Get Response
    Dim res As GetGuestsResponse = api.GetGuests(req)

    'Now examine the results:

    For Each guest As GuestResponse In res.Guests
        Console.WriteLine("GuestID: {0}", guest.GuestID)
        Console.WriteLine("CustomerID: {0}", guest.CustomerID)
        Console.WriteLine("HostID: {0}", guest.HostID)
        Console.WriteLine("FirstName: {0}", guest.FirstName)
        Console.WriteLine("MiddleName: {0}", guest.MiddleName)
        Console.WriteLine("LastName: {0}", guest.LastName)
        Console.WriteLine("NameSuffix: {0}", guest.NameSuffix)
        Console.WriteLine("Company: {0}", guest.Company)
        Console.WriteLine("GuestStatus: {0}", guest.GuestStatus)
        Console.WriteLine("Address1: {0}", guest.Address1)
        Console.WriteLine("Address2: {0}", guest.Address2)
        Console.WriteLine("Address3: {0}", guest.Address3)
        Console.WriteLine("City: {0}", guest.City)
        Console.WriteLine("County: {0}", guest.County)
        Console.WriteLine("Zip: {0}", guest.Zip)
        Console.WriteLine("Phone: {0}", guest.Phone)
        Console.WriteLine("Phone2: {0}", guest.Phone2)
        Console.WriteLine("MobilePhone: {0}", guest.MobilePhone)
        Console.WriteLine("Email: {0}", guest.Email)
        Console.WriteLine("Date1: {0}", guest.Date1)
        Console.WriteLine("Date2: {0}", guest.Date2)
        Console.WriteLine("Date3: {0}", guest.Date3)
        Console.WriteLine("Date4: {0}", guest.Date4)
        Console.WriteLine("Date5: {0}", guest.Date5)
        Console.WriteLine("CreatedDate: {0}", guest.CreatedDate)
        Console.WriteLine("ModifiedDate: {0}", guest.ModifiedDate)
        Console.WriteLine("CustomerKey: {0}", guest.CustomerKey)
        Console.WriteLine("GenderDescription: {0}", guest.GenderDescription)
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
    $res = $api.GetGuests($req);

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
    GetGuestsRequest req = new GetGuestsRequest();

    //Send Request to Server and Get Response
    GetGuestsResponse res = api.getExigoApiSoap().getGuests(req, auth);

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

### GetGuestSocialNetworks

> Returns a list of social network(s) for the guest.

| | |
|---|---|
| Category | Party Plan |
| REST | `GET /3.0/guest/socialnetwork?guestID=1` |
| SOAP action | `https://api.exigo.com/GetGuestSocialNetworks` |
| WSDL elements | `GetGuestSocialNetworksRequest` → `GetGuestSocialNetworksResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetGuestSocialNetworks |

#### Input

**`GetGuestSocialNetworksRequest`**

| Property | Type | Notes |
|---|---|---|
| `GuestID` | `Int32` |  |

#### Output

**`GetGuestSocialNetworksResponse`**

| Property | Type | Notes |
|---|---|---|
| `GuestSocialNetworks` | `GuestSocialNetworksResponse[]` |  |

**`GuestSocialNetworksResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `SocialNetworkID` | `Int32` | Unique Social Network ID.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `SocialNetworkDescription` | `String` |  |
| &nbsp;&nbsp;↳ `Url` | `String` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/guest/socialnetwork?guestID=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "guestSocialNetworks": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetGuestSocialNetworks"

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
    <GetGuestSocialNetworksRequest xmlns="http://api.exigo.com/">
      <GuestID>int</GuestID>
    </GetGuestSocialNetworksRequest>
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
    <GetGuestSocialNetworksResult xmlns="http://api.exigo.com/">
      <GuestSocialNetworks>
        <GuestSocialNetworksResponse>
          <SocialNetworkID>int</SocialNetworkID>
          <SocialNetworkDescription>string</SocialNetworkDescription>
          <Url>string</Url>
        </GuestSocialNetworksResponse>
      </GuestSocialNetworks>
    </GetGuestSocialNetworksResult>
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
    var req = new GetGuestSocialNetworksRequest();

    req.GuestID = 1;

    //Send Request to Server and Get Response
    var res = await api.GetGuestSocialNetworksAsync(req);

    //Now examine the results:

    foreach (var guestSocialNetworks  in res.GuestSocialNetworks)
    {
        Console.WriteLine("SocialNetworkDescription: {0}", guestSocialNetworks.SocialNetworkDescription);
        Console.WriteLine("Url: {0}", guestSocialNetworks.Url);
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
    GetGuestSocialNetworksRequest req = new GetGuestSocialNetworksRequest();

    req.GuestID = 1;

    //Send Request to Server and Get Response
    GetGuestSocialNetworksResponse res = api.GetGuestSocialNetworks(req);

    //Now examine the results:

    foreach (GuestSocialNetworksResponse guestSocialNetworks  in res.GuestSocialNetworks)
    {
        Console.WriteLine("SocialNetworkDescription: {0}", guestSocialNetworks.SocialNetworkDescription);
        Console.WriteLine("Url: {0}", guestSocialNetworks.Url);
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
    Dim req as new GetGuestSocialNetworksRequest()

    req.GuestID = 1

    'Send Request to Server and Get Response
    Dim res As GetGuestSocialNetworksResponse = api.GetGuestSocialNetworks(req)

    'Now examine the results:

    For Each guestSocialNetworks As GuestSocialNetworksResponse In res.GuestSocialNetworks
        Console.WriteLine("SocialNetworkDescription: {0}", guestSocialNetworks.SocialNetworkDescription)
        Console.WriteLine("Url: {0}", guestSocialNetworks.Url)
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

    $req->GuestID = 1;

    //Send Request to Server and Get Response
    $res = $api.GetGuestSocialNetworks($req);

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
    GetGuestSocialNetworksRequest req = new GetGuestSocialNetworksRequest();

    req.setGuestID(1);

    //Send Request to Server and Get Response
    GetGuestSocialNetworksResponse res = api.getExigoApiSoap().getGuestSocialNetworks(req, auth);

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

### SetGuestSocialNetworks

> Deletes all existing social network(s) for the guest,
>  then inserts the provided list of social network(s) for the guest.

| | |
|---|---|
| Category | Party Plan |
| REST | `PUT /3.0/guest/socialnetwork` |
| SOAP action | `https://api.exigo.com/SetGuestSocialNetworks` |
| WSDL elements | `SetGuestSocialNetworksRequest` → `SetGuestSocialNetworksResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=SetGuestSocialNetworks |

#### Input

**`SetGuestSocialNetworksRequest`**

| Property | Type | Notes |
|---|---|---|
| `GuestID` | `Int32` |  |
| `GuestSocialNetworks` | `GuestSocialNetworkRequest[]` |  |

**`GuestSocialNetworkRequest`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `SocialNetworkID` | `Int32` |  |
| &nbsp;&nbsp;↳ `Url` | `String` | Optional. |

#### Output

**`SetGuestSocialNetworksResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/guest/socialnetwork HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "guestID": 1,
  "guestSocialNetworks": null
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
SOAPAction: "https://api.exigo.com/SetGuestSocialNetworks"

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
    <SetGuestSocialNetworksRequest xmlns="http://api.exigo.com/">
      <GuestID>int</GuestID>
      <GuestSocialNetworks>
        <GuestSocialNetworkRequest>
          <SocialNetworkID>int</SocialNetworkID>
          <Url>string</Url>
        </GuestSocialNetworkRequest>
      </GuestSocialNetworks>
    </SetGuestSocialNetworksRequest>
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
    <SetGuestSocialNetworksResult xmlns="http://api.exigo.com/" />
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
    var req = new SetGuestSocialNetworksRequest();

    req.GuestID = 1;

    //Add GuestSocialNetworks
    var guestsocialnetworks = new List<GuestSocialNetworkRequest>();

    var guestSocialNetwork1 = new GuestSocialNetworkRequest();
    guestSocialNetwork1.SocialNetworkID = 1;
    guestSocialNetwork1.Url = "1";
    guestsocialnetworks.Add(guestSocialNetwork1);

    var guestSocialNetwork2 = new GuestSocialNetworkRequest();
    guestSocialNetwork2.SocialNetworkID = 2;
    guestSocialNetwork2.Url = "2";
    guestsocialnetworks.Add(guestSocialNetwork2);

    //Now attach the list to the request
    req.GuestSocialNetworks = guestsocialnetworks.ToArray();

    //Send Request to Server and Get Response
    var res = await api.SetGuestSocialNetworksAsync(req);

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
    SetGuestSocialNetworksRequest req = new SetGuestSocialNetworksRequest();

    req.GuestID = 1;

    //Add GuestSocialNetworks
    List<GuestSocialNetworkRequest> guestsocialnetworks = new List<GuestSocialNetworkRequest>();

    GuestSocialNetworkRequest guestSocialNetwork1 = new GuestSocialNetworkRequest();
    guestSocialNetwork1.SocialNetworkID = 1;
    guestSocialNetwork1.Url = "1";
    guestsocialnetworks.Add(guestSocialNetwork1);

    GuestSocialNetworkRequest guestSocialNetwork2 = new GuestSocialNetworkRequest();
    guestSocialNetwork2.SocialNetworkID = 2;
    guestSocialNetwork2.Url = "2";
    guestsocialnetworks.Add(guestSocialNetwork2);

    //Now attach the list to the request
    req.GuestSocialNetworks = guestsocialnetworks.ToArray();

    //Send Request to Server and Get Response
    SetGuestSocialNetworksResponse res = api.SetGuestSocialNetworks(req);

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
    Dim req as new SetGuestSocialNetworksRequest()

    req.GuestID = 1

    'Add GuestSocialNetworks
    Dim guestsocialnetworks As New List(Of GuestSocialNetworkRequest)()

    Dim guestSocialNetwork1 as new GuestSocialNetworkRequest()
    guestSocialNetwork1.SocialNetworkID = 1
    guestSocialNetwork1.Url = "1"
    guestsocialnetworks.Add(guestSocialNetwork1)

    Dim guestSocialNetwork2 as new GuestSocialNetworkRequest()
    guestSocialNetwork2.SocialNetworkID = 2
    guestSocialNetwork2.Url = "2"
    guestsocialnetworks.Add(guestSocialNetwork2)

    'Now attach the list to the request
    req.GuestSocialNetworks = guestsocialnetworks.ToArray()

    'Send Request to Server and Get Response
    Dim res As SetGuestSocialNetworksResponse = api.SetGuestSocialNetworks(req)

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

    $req->GuestID = 1;

    //Add GuestSocialNetworks

    $guestSocialNetwork1->SocialNetworkID = 1;
    $guestSocialNetwork1->Url = "1";

    $guestSocialNetwork2->SocialNetworkID = 2;
    $guestSocialNetwork2->Url = "2";

    //Now attach the list to the request
    req.GuestSocialNetworks = array(guestSocialNetwork1,guestSocialNetwork2);

    //Send Request to Server and Get Response
    $res = $api.SetGuestSocialNetworks($req);

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
    SetGuestSocialNetworksRequest req = new SetGuestSocialNetworksRequest();

    req.setGuestID(1);

    //Add GuestSocialNetworks
    ArrayOfGuestSocialNetworkRequest guestsocialnetworks = new ArrayOfGuestSocialNetworkRequest();

    GuestSocialNetworkRequest guestSocialNetwork1 = new GuestSocialNetworkRequest();
    guestSocialNetwork1.setSocialNetworkID(1);
    guestSocialNetwork1.setUrl("1");
    guestsocialnetworks.Add(guestSocialNetwork1);

    GuestSocialNetworkRequest guestSocialNetwork2 = new GuestSocialNetworkRequest();
    guestSocialNetwork2.setSocialNetworkID(2);
    guestSocialNetwork2.setUrl("2");
    guestsocialnetworks.Add(guestSocialNetwork2);

    //Now attach the list to the request
    req.setGuestSocialNetworks(guestsocialnetworks);

    //Send Request to Server and Get Response
    SetGuestSocialNetworksResponse res = api.getExigoApiSoap().setGuestSocialNetworks(req, auth);

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
