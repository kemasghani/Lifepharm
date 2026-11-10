# Exigo API — Calendar

API version v2025.11.7.6. Crawled 2026-11-11 from https://api.exigo.com/3.0/. Back to [index](../README.md).

| Operation | REST | Summary |
|---|---|---|
| [CreateCalendarItem](#createcalendaritem) | `POST /3.0/calendar/item` | Creates a new calendar item. Note: This request can participate in a transaction. Learn more about transactions. |
| [UpdateCalendarItem](#updatecalendaritem) | `PATCH /3.0/calendar/item` | Updates calendar item information. Note: This request can participate in a transaction. Learn more about transactions. |
| [DeleteCalendarItem](#deletecalendaritem) | `DELETE /3.0/calendar/item` | Deletes a calendar item. Note: This request can participate in a transaction. Learn more about transactions. |

---
### CreateCalendarItem

>  Creates a new calendar item.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Calendar |
| REST | `POST /3.0/calendar/item` |
| SOAP action | `https://api.exigo.com/CreateCalendarItem` |
| WSDL elements | `CreateCalendarItemRequest` → `CreateCalendarItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateCalendarItem |

#### Input

**`CreateCalendarItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `UserID` | `Int32` |  |
| `CalendarID` | `Int32` |  |
| `CalendarItemType` | `CalendarItemType` | **Values:** `Appointment`, `ToDo`, `Anniversary` |
| `CalendarItemStatusType` | `CalendarItemStatusType` | **Values:** `Open`, `Closed` |
| `CalendarItemPriorityType` | `CalendarItemPriorityType` | **Values:** `None`, `High`, `Medium`, `Low` |
| `Subject` | `String` | Optional. |
| `Location` | `String` | Optional. |
| `Notes` | `String` | Optional. |
| `StartDate` | `DateTime` |  |
| `EndDate` | `DateTime` |  |
| `TimeZone` | `Int32` |  |
| `Address1` | `String` | Optional. |
| `Address2` | `String` | Optional. |
| `City` | `String` | Optional. |
| `State` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Country` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `PostalCode` | `String` | Optional. |
| `ContactInfo` | `String` | Optional. |
| `ContactPhone` | `String` | Optional. |
| `ContactPhoneType` | `ContactPhoneType` | **Values:** `Office`, `Mobile`, `Home` |
| `ContactEmail` | `String` | Optional. |
| `EventHost` | `String` | Optional. |
| `SpecialGuests` | `String` | Optional. |
| `EventFlyer` | `String` | Optional. |
| `EventCostInfo` | `String` | Optional. |
| `EventConferenceCallOrWebinar` | `String` | Optional. |
| `EventRegistrationInfo` | `String` | Optional. |
| `EventTags` | `String` | Optional. |
| `IsShared` | `Boolean` |  |

#### Output

**`CreateCalendarItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `CalendarID` | `Int32` |  |
| `CalendarItemID` | `Int32` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/calendar/item HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "userID": 1,
  "calendarID": 1,
  "calendarItemType": null,
  "calendarItemStatusType": null,
  "calendarItemPriorityType": null,
  "subject": "",
  "location": "",
  "notes": "",
  "startDate": "2026-11-10T00:00:00-06:00",
  "endDate": "2026-11-10T00:00:00-06:00",
  "timeZone": 1,
  "address1": "",
  "address2": "",
  "city": "",
  "postalCode": "",
  "contactInfo": "",
  "contactPhone": "",
  "contactPhoneType": null,
  "contactEmail": "",
  "eventHost": "",
  "specialGuests": "",
  "eventFlyer": "",
  "eventCostInfo": "",
  "eventConferenceCallOrWebinar": "",
  "eventRegistrationInfo": "",
  "eventTags": "",
  "isShared": true
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "calendarID": 1,
  "calendarItemID": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateCalendarItem"

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
    <CreateCalendarItemRequest xmlns="http://api.exigo.com/">
      <UserID>int</UserID>
      <CalendarID>int</CalendarID>
      <CalendarItemType>Appointment or ToDo or Anniversary</CalendarItemType>
      <CalendarItemStatusType>Open or Closed</CalendarItemStatusType>
      <CalendarItemPriorityType>None or High or Medium or Low</CalendarItemPriorityType>
      <Subject>string</Subject>
      <Location>string</Location>
      <Notes>string</Notes>
      <StartDate>dateTime</StartDate>
      <EndDate>dateTime</EndDate>
      <TimeZone>int</TimeZone>
      <Address1>string</Address1>
      <Address2>string</Address2>
      <City>string</City>
      <State>string</State>
      <Country>string</Country>
      <PostalCode>string</PostalCode>
      <ContactInfo>string</ContactInfo>
      <ContactPhone>string</ContactPhone>
      <ContactPhoneType>Office or Mobile or Home</ContactPhoneType>
      <ContactEmail>string</ContactEmail>
      <EventHost>string</EventHost>
      <SpecialGuests>string</SpecialGuests>
      <EventFlyer>string</EventFlyer>
      <EventCostInfo>string</EventCostInfo>
      <EventConferenceCallOrWebinar>string</EventConferenceCallOrWebinar>
      <EventRegistrationInfo>string</EventRegistrationInfo>
      <EventTags>string</EventTags>
      <IsShared>boolean</IsShared>
    </CreateCalendarItemRequest>
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
    <CreateCalendarItemResult xmlns="http://api.exigo.com/">
      <CalendarID>int</CalendarID>
      <CalendarItemID>int</CalendarItemID>
    </CreateCalendarItemResult>
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
    var req = new CreateCalendarItemRequest();

    req.UserID = 1;
    req.CalendarID = 1;
    req.CalendarItemType = CalendarItemType.Appointment;
    req.CalendarItemStatusType = CalendarItemStatusType.Open;
    req.CalendarItemPriorityType = CalendarItemPriorityType.None;
    req.Subject = "1";
    req.Location = "1";
    req.Notes = "1";
    req.StartDate = DateTime.Today;
    req.EndDate = DateTime.Today;
    req.TimeZone = 1;
    req.Address1 = "1";
    req.Address2 = "1";
    req.City = "1";
    req.PostalCode = "1";
    req.ContactInfo = "1";
    req.ContactPhone = "1";
    req.ContactPhoneType = ContactPhoneType.Office;
    req.ContactEmail = "1";
    req.EventHost = "1";
    req.SpecialGuests = "1";
    req.EventFlyer = "1";
    req.EventCostInfo = "1";
    req.EventConferenceCallOrWebinar = "1";
    req.EventRegistrationInfo = "1";
    req.EventTags = "1";
    req.IsShared = true;

    //Send Request to Server and Get Response
    var res = await api.CreateCalendarItemAsync(req);

    //Now examine the results:
    Console.WriteLine("CalendarID: {0}", res.CalendarID);
    Console.WriteLine("CalendarItemID: {0}", res.CalendarItemID);
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
    CreateCalendarItemRequest req = new CreateCalendarItemRequest();

    req.UserID = 1;
    req.CalendarID = 1;
    req.CalendarItemType = CalendarItemType.Appointment;
    req.CalendarItemStatusType = CalendarItemStatusType.Open;
    req.CalendarItemPriorityType = CalendarItemPriorityType.None;
    req.Subject = "1";
    req.Location = "1";
    req.Notes = "1";
    req.StartDate = DateTime.Today;
    req.EndDate = DateTime.Today;
    req.TimeZone = 1;
    req.Address1 = "1";
    req.Address2 = "1";
    req.City = "1";
    req.PostalCode = "1";
    req.ContactInfo = "1";
    req.ContactPhone = "1";
    req.ContactPhoneType = ContactPhoneType.Office;
    req.ContactEmail = "1";
    req.EventHost = "1";
    req.SpecialGuests = "1";
    req.EventFlyer = "1";
    req.EventCostInfo = "1";
    req.EventConferenceCallOrWebinar = "1";
    req.EventRegistrationInfo = "1";
    req.EventTags = "1";
    req.IsShared = true;

    //Send Request to Server and Get Response
    CreateCalendarItemResponse res = api.CreateCalendarItem(req);

    //Now examine the results:
    Console.WriteLine("CalendarID: {0}", res.CalendarID);
    Console.WriteLine("CalendarItemID: {0}", res.CalendarItemID);
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
    Dim req as new CreateCalendarItemRequest()

    req.UserID = 1
    req.CalendarID = 1
    req.CalendarItemType = CalendarItemType.Appointment
    req.CalendarItemStatusType = CalendarItemStatusType.Open
    req.CalendarItemPriorityType = CalendarItemPriorityType.None
    req.Subject = "1"
    req.Location = "1"
    req.Notes = "1"
    req.StartDate = DateTime.Today
    req.EndDate = DateTime.Today
    req.TimeZone = 1
    req.Address1 = "1"
    req.Address2 = "1"
    req.City = "1"
    req.PostalCode = "1"
    req.ContactInfo = "1"
    req.ContactPhone = "1"
    req.ContactPhoneType = ContactPhoneType.Office
    req.ContactEmail = "1"
    req.EventHost = "1"
    req.SpecialGuests = "1"
    req.EventFlyer = "1"
    req.EventCostInfo = "1"
    req.EventConferenceCallOrWebinar = "1"
    req.EventRegistrationInfo = "1"
    req.EventTags = "1"
    req.IsShared = true

    'Send Request to Server and Get Response
    Dim res As CreateCalendarItemResponse = api.CreateCalendarItem(req)

    'Now examine the results:
    Console.WriteLine("CalendarID: {0}", res.CalendarID)
    Console.WriteLine("CalendarItemID: {0}", res.CalendarItemID)
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

    $req->UserID = 1;
    $req->CalendarID = 1;
    $req->CalendarItemType = 1;
    $req->CalendarItemStatusType = 1;
    $req->CalendarItemPriorityType = 1;
    $req->Subject = "1";
    $req->Location = "1";
    $req->Notes = "1";
    $req->StartDate = 1;
    $req->EndDate = 1;
    $req->TimeZone = 1;
    $req->Address1 = "1";
    $req->Address2 = "1";
    $req->City = "1";
    $req->PostalCode = "1";
    $req->ContactInfo = "1";
    $req->ContactPhone = "1";
    $req->ContactPhoneType = 1;
    $req->ContactEmail = "1";
    $req->EventHost = "1";
    $req->SpecialGuests = "1";
    $req->EventFlyer = "1";
    $req->EventCostInfo = "1";
    $req->EventConferenceCallOrWebinar = "1";
    $req->EventRegistrationInfo = "1";
    $req->EventTags = "1";
    $req->IsShared = 1;

    //Send Request to Server and Get Response
    $res = $api.CreateCalendarItem($req);

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
    CreateCalendarItemRequest req = new CreateCalendarItemRequest();

    req.setUserID(1);
    req.setCalendarID(1);
    req.setCalendarItemType(1);
    req.setCalendarItemStatusType(1);
    req.setCalendarItemPriorityType(1);
    req.setSubject("1");
    req.setLocation("1");
    req.setNotes("1");
    req.setStartDate(1);
    req.setEndDate(1);
    req.setTimeZone(1);
    req.setAddress1("1");
    req.setAddress2("1");
    req.setCity("1");
    req.setPostalCode("1");
    req.setContactInfo("1");
    req.setContactPhone("1");
    req.setContactPhoneType(1);
    req.setContactEmail("1");
    req.setEventHost("1");
    req.setSpecialGuests("1");
    req.setEventFlyer("1");
    req.setEventCostInfo("1");
    req.setEventConferenceCallOrWebinar("1");
    req.setEventRegistrationInfo("1");
    req.setEventTags("1");
    req.setIsShared(1);

    //Send Request to Server and Get Response
    CreateCalendarItemResponse res = api.getExigoApiSoap().createCalendarItem(req, auth);

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

### UpdateCalendarItem

> Updates calendar item information.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Calendar |
| REST | `PATCH /3.0/calendar/item` |
| SOAP action | `https://api.exigo.com/UpdateCalendarItem` |
| WSDL elements | `UpdateCalendarItemRequest` → `UpdateCalendarItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateCalendarItem |

#### Input

**`UpdateCalendarItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `UserID` | `Int32` |  |
| `CalendarID` | `Int32` |  |
| `CalendarItemID` | `Int32` |  |
| `CalendarItemType` | `CalendarItemType` | **Values:** `Appointment`, `ToDo`, `Anniversary` |
| `CalendarItemStatusType` | `CalendarItemStatusType` | Optional.<br>**Values:** `Open`, `Closed` |
| `CalendarItemPriorityType` | `CalendarItemPriorityType` | Optional.<br>**Values:** `None`, `High`, `Medium`, `Low` |
| `Subject` | `String` | Optional. |
| `Location` | `String` | Optional. |
| `Notes` | `String` | Optional. |
| `StartDate` | `DateTime` |  |
| `EndDate` | `DateTime` |  |
| `TimeZone` | `Int32` |  |
| `Address1` | `String` | Optional. |
| `Address2` | `String` | Optional. |
| `City` | `String` | Optional. |
| `State` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Country` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `PostalCode` | `String` | Optional. |
| `ContactInfo` | `String` | Optional. |
| `ContactPhone` | `String` | Optional. |
| `ContactPhoneType` | `ContactPhoneType` | **Values:** `Office`, `Mobile`, `Home` |
| `ContactEmail` | `String` | Optional. |
| `EventHost` | `String` | Optional. |
| `SpecialGuests` | `String` | Optional. |
| `EventFlyer` | `String` | Optional. |
| `EventCostInfo` | `String` | Optional. |
| `EventConferenceCallOrWebinar` | `String` | Optional. |
| `EventRegistrationInfo` | `String` | Optional. |
| `EventTags` | `String` | Optional. |
| `IsShared` | `Boolean` |  |

#### Output

**`UpdateCalendarItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `CalendarID` | `Int32` |  |
| `CalendarItemID` | `Int32` |  |

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/calendar/item HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "userID": 1,
  "calendarID": 1,
  "calendarItemID": 1,
  "calendarItemType": null,
  "calendarItemStatusType": null,
  "calendarItemPriorityType": null,
  "subject": "",
  "location": "",
  "notes": "",
  "startDate": "2026-11-10T00:00:00-06:00",
  "endDate": "2026-11-10T00:00:00-06:00",
  "timeZone": 1,
  "address1": "",
  "address2": "",
  "city": "",
  "postalCode": "",
  "contactInfo": "",
  "contactPhone": "",
  "contactPhoneType": null,
  "contactEmail": "",
  "eventHost": "",
  "specialGuests": "",
  "eventFlyer": "",
  "eventCostInfo": "",
  "eventConferenceCallOrWebinar": "",
  "eventRegistrationInfo": "",
  "eventTags": "",
  "isShared": true
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "calendarID": 1,
  "calendarItemID": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/UpdateCalendarItem"

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
    <UpdateCalendarItemRequest xmlns="http://api.exigo.com/">
      <UserID>int</UserID>
      <CalendarID>int</CalendarID>
      <CalendarItemID>int</CalendarItemID>
      <CalendarItemType>Appointment or ToDo or Anniversary</CalendarItemType>
      <CalendarItemStatusType>Open or Closed</CalendarItemStatusType>
      <CalendarItemPriorityType>None or High or Medium or Low</CalendarItemPriorityType>
      <Subject>string</Subject>
      <Location>string</Location>
      <Notes>string</Notes>
      <StartDate>dateTime</StartDate>
      <EndDate>dateTime</EndDate>
      <TimeZone>int</TimeZone>
      <Address1>string</Address1>
      <Address2>string</Address2>
      <City>string</City>
      <State>string</State>
      <Country>string</Country>
      <PostalCode>string</PostalCode>
      <ContactInfo>string</ContactInfo>
      <ContactPhone>string</ContactPhone>
      <ContactPhoneType>Office or Mobile or Home</ContactPhoneType>
      <ContactEmail>string</ContactEmail>
      <EventHost>string</EventHost>
      <SpecialGuests>string</SpecialGuests>
      <EventFlyer>string</EventFlyer>
      <EventCostInfo>string</EventCostInfo>
      <EventConferenceCallOrWebinar>string</EventConferenceCallOrWebinar>
      <EventRegistrationInfo>string</EventRegistrationInfo>
      <EventTags>string</EventTags>
      <IsShared>boolean</IsShared>
    </UpdateCalendarItemRequest>
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
    <UpdateCalendarItemResult xmlns="http://api.exigo.com/">
      <CalendarID>int</CalendarID>
      <CalendarItemID>int</CalendarItemID>
    </UpdateCalendarItemResult>
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
    var req = new UpdateCalendarItemRequest();

    req.UserID = 1;
    req.CalendarID = 1;
    req.CalendarItemID = 1;
    req.CalendarItemType = CalendarItemType.Appointment;
    req.CalendarItemStatusType = CalendarItemStatusType.Open;
    req.CalendarItemPriorityType = CalendarItemPriorityType.None;
    req.Subject = "1";
    req.Location = "1";
    req.Notes = "1";
    req.StartDate = DateTime.Today;
    req.EndDate = DateTime.Today;
    req.TimeZone = 1;
    req.Address1 = "1";
    req.Address2 = "1";
    req.City = "1";
    req.PostalCode = "1";
    req.ContactInfo = "1";
    req.ContactPhone = "1";
    req.ContactPhoneType = ContactPhoneType.Office;
    req.ContactEmail = "1";
    req.EventHost = "1";
    req.SpecialGuests = "1";
    req.EventFlyer = "1";
    req.EventCostInfo = "1";
    req.EventConferenceCallOrWebinar = "1";
    req.EventRegistrationInfo = "1";
    req.EventTags = "1";
    req.IsShared = true;

    //Send Request to Server and Get Response
    var res = await api.UpdateCalendarItemAsync(req);

    //Now examine the results:
    Console.WriteLine("CalendarID: {0}", res.CalendarID);
    Console.WriteLine("CalendarItemID: {0}", res.CalendarItemID);
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
    UpdateCalendarItemRequest req = new UpdateCalendarItemRequest();

    req.UserID = 1;
    req.CalendarID = 1;
    req.CalendarItemID = 1;
    req.CalendarItemType = CalendarItemType.Appointment;
    req.CalendarItemStatusType = CalendarItemStatusType.Open;
    req.CalendarItemPriorityType = CalendarItemPriorityType.None;
    req.Subject = "1";
    req.Location = "1";
    req.Notes = "1";
    req.StartDate = DateTime.Today;
    req.EndDate = DateTime.Today;
    req.TimeZone = 1;
    req.Address1 = "1";
    req.Address2 = "1";
    req.City = "1";
    req.PostalCode = "1";
    req.ContactInfo = "1";
    req.ContactPhone = "1";
    req.ContactPhoneType = ContactPhoneType.Office;
    req.ContactEmail = "1";
    req.EventHost = "1";
    req.SpecialGuests = "1";
    req.EventFlyer = "1";
    req.EventCostInfo = "1";
    req.EventConferenceCallOrWebinar = "1";
    req.EventRegistrationInfo = "1";
    req.EventTags = "1";
    req.IsShared = true;

    //Send Request to Server and Get Response
    UpdateCalendarItemResponse res = api.UpdateCalendarItem(req);

    //Now examine the results:
    Console.WriteLine("CalendarID: {0}", res.CalendarID);
    Console.WriteLine("CalendarItemID: {0}", res.CalendarItemID);
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
    Dim req as new UpdateCalendarItemRequest()

    req.UserID = 1
    req.CalendarID = 1
    req.CalendarItemID = 1
    req.CalendarItemType = CalendarItemType.Appointment
    req.CalendarItemStatusType = CalendarItemStatusType.Open
    req.CalendarItemPriorityType = CalendarItemPriorityType.None
    req.Subject = "1"
    req.Location = "1"
    req.Notes = "1"
    req.StartDate = DateTime.Today
    req.EndDate = DateTime.Today
    req.TimeZone = 1
    req.Address1 = "1"
    req.Address2 = "1"
    req.City = "1"
    req.PostalCode = "1"
    req.ContactInfo = "1"
    req.ContactPhone = "1"
    req.ContactPhoneType = ContactPhoneType.Office
    req.ContactEmail = "1"
    req.EventHost = "1"
    req.SpecialGuests = "1"
    req.EventFlyer = "1"
    req.EventCostInfo = "1"
    req.EventConferenceCallOrWebinar = "1"
    req.EventRegistrationInfo = "1"
    req.EventTags = "1"
    req.IsShared = true

    'Send Request to Server and Get Response
    Dim res As UpdateCalendarItemResponse = api.UpdateCalendarItem(req)

    'Now examine the results:
    Console.WriteLine("CalendarID: {0}", res.CalendarID)
    Console.WriteLine("CalendarItemID: {0}", res.CalendarItemID)
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

    $req->UserID = 1;
    $req->CalendarID = 1;
    $req->CalendarItemID = 1;
    $req->CalendarItemType = 1;
    $req->CalendarItemStatusType = 1;
    $req->CalendarItemPriorityType = 1;
    $req->Subject = "1";
    $req->Location = "1";
    $req->Notes = "1";
    $req->StartDate = 1;
    $req->EndDate = 1;
    $req->TimeZone = 1;
    $req->Address1 = "1";
    $req->Address2 = "1";
    $req->City = "1";
    $req->PostalCode = "1";
    $req->ContactInfo = "1";
    $req->ContactPhone = "1";
    $req->ContactPhoneType = 1;
    $req->ContactEmail = "1";
    $req->EventHost = "1";
    $req->SpecialGuests = "1";
    $req->EventFlyer = "1";
    $req->EventCostInfo = "1";
    $req->EventConferenceCallOrWebinar = "1";
    $req->EventRegistrationInfo = "1";
    $req->EventTags = "1";
    $req->IsShared = 1;

    //Send Request to Server and Get Response
    $res = $api.UpdateCalendarItem($req);

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
    UpdateCalendarItemRequest req = new UpdateCalendarItemRequest();

    req.setUserID(1);
    req.setCalendarID(1);
    req.setCalendarItemID(1);
    req.setCalendarItemType(1);
    req.setCalendarItemStatusType(1);
    req.setCalendarItemPriorityType(1);
    req.setSubject("1");
    req.setLocation("1");
    req.setNotes("1");
    req.setStartDate(1);
    req.setEndDate(1);
    req.setTimeZone(1);
    req.setAddress1("1");
    req.setAddress2("1");
    req.setCity("1");
    req.setPostalCode("1");
    req.setContactInfo("1");
    req.setContactPhone("1");
    req.setContactPhoneType(1);
    req.setContactEmail("1");
    req.setEventHost("1");
    req.setSpecialGuests("1");
    req.setEventFlyer("1");
    req.setEventCostInfo("1");
    req.setEventConferenceCallOrWebinar("1");
    req.setEventRegistrationInfo("1");
    req.setEventTags("1");
    req.setIsShared(1);

    //Send Request to Server and Get Response
    UpdateCalendarItemResponse res = api.getExigoApiSoap().updateCalendarItem(req, auth);

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

### DeleteCalendarItem

>  Deletes a calendar item.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Calendar |
| REST | `DELETE /3.0/calendar/item` |
| SOAP action | `https://api.exigo.com/DeleteCalendarItem` |
| WSDL elements | `DeleteCalendarItemRequest` → `DeleteCalendarItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DeleteCalendarItem |

#### Input

**`DeleteCalendarItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `UserID` | `Int32` |  |
| `CalendarID` | `Int32` |  |
| `CalendarItemID` | `Int32` |  |

#### Output

**`DeleteCalendarItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `CalendarID` | `Int32` |  |
| `CalendarItemID` | `Int32` |  |

#### REST example

```http
DELETE https://yourcompany-api.exigo.com/3.0/calendar/item HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "userID": 1,
  "calendarID": 1,
  "calendarItemID": 1
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "calendarID": 1,
  "calendarItemID": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/DeleteCalendarItem"

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
    <DeleteCalendarItemRequest xmlns="http://api.exigo.com/">
      <UserID>int</UserID>
      <CalendarID>int</CalendarID>
      <CalendarItemID>int</CalendarItemID>
    </DeleteCalendarItemRequest>
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
    <DeleteCalendarItemResult xmlns="http://api.exigo.com/">
      <CalendarID>int</CalendarID>
      <CalendarItemID>int</CalendarItemID>
    </DeleteCalendarItemResult>
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
    var req = new DeleteCalendarItemRequest();

    req.UserID = 1;
    req.CalendarID = 1;
    req.CalendarItemID = 1;

    //Send Request to Server and Get Response
    var res = await api.DeleteCalendarItemAsync(req);

    //Now examine the results:
    Console.WriteLine("CalendarID: {0}", res.CalendarID);
    Console.WriteLine("CalendarItemID: {0}", res.CalendarItemID);
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
    DeleteCalendarItemRequest req = new DeleteCalendarItemRequest();

    req.UserID = 1;
    req.CalendarID = 1;
    req.CalendarItemID = 1;

    //Send Request to Server and Get Response
    DeleteCalendarItemResponse res = api.DeleteCalendarItem(req);

    //Now examine the results:
    Console.WriteLine("CalendarID: {0}", res.CalendarID);
    Console.WriteLine("CalendarItemID: {0}", res.CalendarItemID);
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
    Dim req as new DeleteCalendarItemRequest()

    req.UserID = 1
    req.CalendarID = 1
    req.CalendarItemID = 1

    'Send Request to Server and Get Response
    Dim res As DeleteCalendarItemResponse = api.DeleteCalendarItem(req)

    'Now examine the results:
    Console.WriteLine("CalendarID: {0}", res.CalendarID)
    Console.WriteLine("CalendarItemID: {0}", res.CalendarItemID)
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

    $req->UserID = 1;
    $req->CalendarID = 1;
    $req->CalendarItemID = 1;

    //Send Request to Server and Get Response
    $res = $api.DeleteCalendarItem($req);

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
    DeleteCalendarItemRequest req = new DeleteCalendarItemRequest();

    req.setUserID(1);
    req.setCalendarID(1);
    req.setCalendarItemID(1);

    //Send Request to Server and Get Response
    DeleteCalendarItemResponse res = api.getExigoApiSoap().deleteCalendarItem(req, auth);

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
