# Exigo API — Customers

API version v2025.11.7.6. Crawled 2026-11-11 from https://api.exigo.com/3.0/. Back to [index](../README.md).

Customer management protocols for creating, updating, and administering customer entitys. This section also contains tools for tree placement, billing, and social media integration, along with customer site management.

| Operation | REST | Summary |
|---|---|---|
| [CreateCustomer](#createcustomer) | `POST /3.0/customers` | Creates a new Customer. Can optionally be put in one or more trees. |
| [UpdateCustomer](#updatecustomer) | `PATCH /3.0/customers` | Updates one or more fields on an existing customer. Can participate in a transaction. |
| [AuthenticateCustomer](#authenticatecustomer) | `POST /3.0/customers/authenticate` | Authenticates a customer for login using UserName and Password combination. |
| [SetAccountCreditCardToken](#setaccountcreditcardtoken) | `PUT /3.0/account/cctoken` | Setup primary or secondary credit card token on file for an existing customer, or new customer in a transaction. Note: This request can participate in a transaction. Learn more… |
| [SetAccountChecking](#setaccountchecking) | `PUT /3.0/account/checking` | Setup bank account on file an existing customer, or new customer in a transaction. You can also empty the account settings by simply leaving everything but CustomerID empty. Note:… |
| [SetAccountDirectDeposit](#setaccountdirectdeposit) | `PUT /3.0/account/directdeposit` | Setup direct deposit info for an existing customer, or new customer in a transaction. You can also empty the account settings by simply leaving everything but CustomerID empty.… |
| [SetAccountWallet](#setaccountwallet) | `PUT /3.0/account/wallet` | Setup primary or secondary wallet account on file for an existing customer, or new customer in a transaction. Note: This request can participate in a transaction. Learn more about… |
| [SetCustomerSite](#setcustomersite) | `PUT /3.0/customers/site` | Setup public web site info for an existing customer, or new customer in a transaction. |
| [SetCustomerSiteImage](#setcustomersiteimage) | `PUT /3.0/customers/site/image` | Setup public web site image for an existing customer. |
| [GetCustomers](#getcustomers) | `GET /3.0/customers?customerID=1` | Returns one or more customers that match the filter critera passed in. |
| [GetCustomerSite](#getcustomersite) | `GET /3.0/customers/site?webAlias=1` | Returns the public web site info setup for a customer. Pass in CustomerID or WebAlias. If the customer's type has enabled Create Web Info and a record does not exist a customer… |
| [GetCustomerBilling](#getcustomerbilling) | `GET /3.0/account?customerID=1` | Returns billing accounts on file for a customer. Only => s last four digits of a credit card. |
| [GetCustomerNotes](#getcustomernotes) | `GET /3.0/customers/notes?customerID=1` | Returns the notes field for one or more customers that match the filter critera passed in. |
| [AppendCustomerNotes](#appendcustomernotes) | `PATCH /3.0/customers/notes` | Appends a specified value to the specified Customer's Notes record Note: This request can participate in a transaction. Learn more about transactions. |
| [GetAccountDirectDeposit](#getaccountdirectdeposit) | `GET /3.0/account/directdeposit?customerID=1` | Returns direct deposit info for an existing customer. |
| [CreateCustomerExtended](#createcustomerextended) | `POST /3.0/customers/extended` | Creates a new customer extended record. Note: This request can participate in a transaction. Learn more about transactions. |
| [UpdateCustomerExtended](#updatecustomerextended) | `PATCH /3.0/customers/extended` | Updates one customer extended record. Note: This request can participate in a transaction. Learn more about transactions. |
| [GetCustomerExtended](#getcustomerextended) | `GET /3.0/customers/extended?extendedGroupID=1` | Returns extended properties setup for a customer. |
| [DeleteCustomerExtended](#deletecustomerextended) | `DELETE /3.0/customers/extended` | Removes one customer extended record. Note: This request can participate in a transaction. Learn more about transactions. |
| [SetCustomerSocialNetworks](#setcustomersocialnetworks) | `PUT /3.0/customers/socialnetworks` | Deletes all existing social network(s) for the customer, then inserts the provided list of social network(s) for the customer. Note: This request can participate in a transaction.… |
| [GetCustomerSocialNetworks](#getcustomersocialnetworks) | `GET /3.0/customers/socialnetworks?customerID=1` | Returns a list of social network(s) for the customer. |
| [GetCustomerWall](#getcustomerwall) | `GET /3.0/customers/wall?customerID=1` | Get wall item(s) from CustomerWall table. |
| [CreateCustomerWallItem](#createcustomerwallitem) | `POST /3.0/customers/wall` | Create new wall item in CustomerWall table. Note: This request can participate in a transaction. Learn more about transactions. |
| [DeleteCustomerWallItem](#deletecustomerwallitem) | `DELETE /3.0/customers/wall` | Delete wall item(s) from CustomerWall table. |
| [CreateCustomerInquiry](#createcustomerinquiry) | `POST /3.0/customers/inquiry` | Creates a customer history record. |
| [DequeueCustomerEvents](#dequeuecustomerevents) | `POST /3.0/customers/events` | This will 'pop' the oldest 100 customer events off the event queue. |
| [CreateSilentLoginCipher](#createsilentlogincipher) | `GET /3.0/customers/createsilentlogincipher?silentLoginKey=1` | Creates backoffice silent login authentication cipher |
| [TerminateCustomer](#terminatecustomer) | `POST /3.0/customers/terminate` | Terminates a Customer |

---
### CreateCustomer

> Creates a new Customer. Can optionally be put in one or more trees.

| | |
|---|---|
| Category | Customers |
| REST | `POST /3.0/customers` |
| SOAP action | `https://api.exigo.com/CreateCustomer` |
| WSDL elements | `CreateCustomerRequest` → `CreateCustomerResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateCustomer |

#### Input

**`CreateCustomerRequest`**

| Property | Type | Notes |
|---|---|---|
| `FirstName` | `String` | Optional. The customer's first name. |
| `LastName` | `String` | Optional. The customer's last name. |
| `Company` | `String` | Optional. The customer's company name. |
| `CustomerType` | `Int32` | The customer's type as defined by the company. |
| `CustomerStatus` | `Int32` | Optional. The customer's status as defined by the company. Defaults to 1. |
| `Email` | `String` | Optional. |
| `Phone` | `String` | Optional. |
| `Phone2` | `String` | Optional. |
| `MobilePhone` | `String` | Optional. |
| `Fax` | `String` | Optional. |
| `Notes` | `String` | Optional. |
| `MainAddress1` | `String` | Optional. |
| `MainAddress2` | `String` | Optional. |
| `MainAddress3` | `String` | Optional. |
| `MainCity` | `String` | Optional. |
| `MainState` | `String` | Optional. The state of the customer's primary address. This field is required if MainAddress1 is provided. |
| `MainZip` | `String` | Optional. |
| `MainCountry` | `String` | Optional. The country of the customer's primary address. This field is required if MainAddress1 is provided. |
| `MainCounty` | `String` | Optional. |
| `MailAddress1` | `String` | Optional. |
| `MailAddress2` | `String` | Optional. |
| `MailAddress3` | `String` | Optional. |
| `MailCity` | `String` | Optional. |
| `MailState` | `String` | Optional. The state of the customer's mailing address. This field is required if MailAddress1 is provided. |
| `MailZip` | `String` | Optional. |
| `MailCountry` | `String` | Optional. The country of the customer's mailing address. This field is required if MailAddress1 is provided. |
| `MailCounty` | `String` | Optional. |
| `OtherAddress1` | `String` | Optional. |
| `OtherAddress2` | `String` | Optional. |
| `OtherAddress3` | `String` | Optional. |
| `OtherCity` | `String` | Optional. |
| `OtherState` | `String` | Optional. The state of the customer's other address. This field is required if OtherAddress1 is provided. |
| `OtherZip` | `String` | Optional. |
| `OtherCountry` | `String` | Optional. The country of the customer's other address. This field is required if OtherAddress1 is provided. |
| `OtherCounty` | `String` | Optional. |
| `CanLogin` | `Boolean` | Optional. If true, the customer will be able to be authenticated using their login name and password. Defaults to False. |
| `LoginName` | `String` | Optional. The customer's desired login name. |
| `LoginPassword` | `String` | Optional. The customer's desired password. |
| `InsertEnrollerTree` | `Boolean` | Optional. If true, the customer will be inserted into the Enroller tree using the provided EnrollerID. Defaults to False. |
| `EnrollerID` | `Int32` | The customer's enroller's unique identifier. Required only when InsertEnrollerTree is true. |
| `InsertUnilevelTree` | `Boolean` | Optional. If true, the customer will be inserted into the UniLevel tree using the provided SponsorID. Defaults to False. |
| `SponsorID` | `Int32` | The customer's UniLevel sponsor's unique identifier. Required only when InsertSponsorTree is true. |
| `UseManualCustomerID` | `Boolean` | Optional. If true, the customer's ID will be set to the ID provided in the ManualCustomerID or ManualCustomerKeyfield. Defaults to False. |
| `ManualCustomerID` | `Int32` | Unique numeric identifier for new customer record. If set, UseManualCustomerID must also be set to true. |
| `TaxID` | `String` | Optional. The customer's tax ID. |
| `SalesTaxID` | `String` | Optional. The customer's sales tax ID. |
| `SalesTaxExemptExpireDate` | `DateTime` | Optional. |
| `IsSalesTaxExempt` | `Boolean` | Optional. If true, the customer will be considered exempt from sales tax. |
| `BirthDate` | `DateTime` | Optional. The customer's birth date. The provided date must be greater than 1/1/1900. |
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
| `SubscribeToBroadcasts` | `Boolean` | If true, the customer will be opted in to receive email broadcasts. Note that the SubscribeFromIPAddress field must also be provided. |
| `SubscribeFromIPAddress` | `String` | Optional. The IP address the customer is being subscribed from. |
| `CurrencyCode` | `String` | Optional. The default currency code this customer will use in future transactions. Defaults to 'usd'. |
| `PayableToName` | `String` | Optional. |
| `EntryDate` | `DateTime` | The date the customer was created. The provided date must be greater than 1/1/1900. |
| `DefaultWarehouseID` | `Int32` | Optional. The default warehouse this customer will use in future transactions. |
| `PayableType` | `PayableType` | Optional. Obsolete field. Please consider upgrading to PayableTy.<br>**Values:** `Check`, `WireTransfer`, `PaymentCard`, `DirectDeposit`, `OnHold`, `BankWire`, `DebitCardHold`, `Other100` |
| `CheckThreshold` | `Decimal` | Optional. |
| `TaxIDType` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `LanguageID` | `Int32` | Optional. The customer's preferred language. Defaults to 0. |
| `Gender` | `Gender` | Optional. Obsolete field. Please consider upgrading to GenderID.<br>**Values:** `Unknown`, `Male`, `Female` |
| `VatRegistration` | `String` | Optional. |
| `Date1` | `DateTime` | Optional. |
| `Date2` | `DateTime` | Optional. |
| `Date3` | `DateTime` | Optional. |
| `Date4` | `DateTime` | Optional. |
| `Date5` | `DateTime` | Optional. |
| `MiddleName` | `String` | Optional. The customer's middle name. |
| `NameSuffix` | `String` | Optional. The customer's name suffix. |
| `BinaryPlacementPreference` | `Int32` | Optional. |
| `UseBinaryHoldingTank` | `Boolean` | Optional. |
| `MainAddressVerified` | `Boolean` | Optional. |
| `MailAddressVerified` | `Boolean` | Optional. |
| `OtherAddressVerified` | `Boolean` | Optional. |
| `SponsorKey` | `String` | Optional. The customer's uniLevel sponsor's unique alpha numeric identifier. Required only when InsertSponsorTree is true. |
| `EnrollerKey` | `String` | Optional. The customer's enroller's unique alpha numeric identifier. Required only when InsertEnrollerTree is true. |
| `ManualCustomerKey` | `String` | Optional. Unique alpha numeric identifier for new customer record. If set, UseManualCustomerID must also be set to true. Exception will occur if ManualCustomerID & ManualCustomerKey are provided. |
| `PayableTy` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `GenderID` | `String` | Optional. The customer's gender.<br>**Lookup:** company-specific list (see company-lists.md) |

#### Output

**`CreateCustomerResponse`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Unique alpha numeric identifier for customer record . |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/customers HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "firstName": "John",
  "lastName": "Doe",
  "company": "ACME, Inc.",
  "customerType": 1,
  "customerStatus": 1,
  "email": "joecool@me.com",
  "phone": "555-555-5555",
  "mainAddress1": "123 Some Street",
  "mainCity": "Dallas",
  "mainState": "TX",
  "mainZip": "75207",
  "mailState": "1",
  "mailCountry": "1",
  "otherState": "1",
  "otherCountry": "1",
  "taxIDType": "SSN",
  "middleName": "1",
  "nameSuffix": "1",
  "binaryPlacementPreference": 1,
  "useBinaryHoldingTank": true,
  "mainAddressVerified": true,
  "mailAddressVerified": true,
  "otherAddressVerified": true,
  "payableTy": "Check"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "customerID": 1,
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
SOAPAction: "https://api.exigo.com/CreateCustomer"

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
    <CreateCustomerRequest xmlns="http://api.exigo.com/">
      <FirstName>string</FirstName>
      <LastName>string</LastName>
      <Company>string</Company>
      <CustomerType>int</CustomerType>
      <CustomerStatus>int</CustomerStatus>
      <Email>string</Email>
      <Phone>string</Phone>
      <Phone2>string</Phone2>
      <MobilePhone>string</MobilePhone>
      <Fax>string</Fax>
      <Notes>string</Notes>
      <MainAddress1>string</MainAddress1>
      <MainAddress2>string</MainAddress2>
      <MainAddress3>string</MainAddress3>
      <MainCity>string</MainCity>
      <MainState>string</MainState>
      <MainZip>string</MainZip>
      <MainCountry>string</MainCountry>
      <MainCounty>string</MainCounty>
      <MailAddress1>string</MailAddress1>
      <MailAddress2>string</MailAddress2>
      <MailAddress3>string</MailAddress3>
      <MailCity>string</MailCity>
      <MailState>string</MailState>
      <MailZip>string</MailZip>
      <MailCountry>string</MailCountry>
      <MailCounty>string</MailCounty>
      <OtherAddress1>string</OtherAddress1>
      <OtherAddress2>string</OtherAddress2>
      <OtherAddress3>string</OtherAddress3>
      <OtherCity>string</OtherCity>
      <OtherState>string</OtherState>
      <OtherZip>string</OtherZip>
      <OtherCountry>string</OtherCountry>
      <OtherCounty>string</OtherCounty>
      <CanLogin>boolean</CanLogin>
      <LoginName>string</LoginName>
      <LoginPassword>string</LoginPassword>
      <InsertEnrollerTree>boolean</InsertEnrollerTree>
      <EnrollerID>int</EnrollerID>
      <InsertUnilevelTree>boolean</InsertUnilevelTree>
      <SponsorID>int</SponsorID>
      <UseManualCustomerID>boolean</UseManualCustomerID>
      <ManualCustomerID>int</ManualCustomerID>
      <TaxID>string</TaxID>
      <SalesTaxID>string</SalesTaxID>
      <SalesTaxExemptExpireDate>dateTime</SalesTaxExemptExpireDate>
      <IsSalesTaxExempt>boolean</IsSalesTaxExempt>
      <BirthDate>dateTime</BirthDate>
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
      <SubscribeToBroadcasts>boolean</SubscribeToBroadcasts>
      <SubscribeFromIPAddress>string</SubscribeFromIPAddress>
      <CurrencyCode>string</CurrencyCode>
      <PayableToName>string</PayableToName>
      <EntryDate>dateTime</EntryDate>
      <DefaultWarehouseID>int</DefaultWarehouseID>
      <PayableType>Check or WireTransfer or PaymentCard or DirectDeposit or OnHold or BankWire or DebitCardHold or Other100</PayableType>
      <CheckThreshold>decimal</CheckThreshold>
      <TaxIDType>string</TaxIDType>
      <LanguageID>int</LanguageID>
      <Gender>Unknown or Male or Female</Gender>
      <VatRegistration>string</VatRegistration>
      <Date1>dateTime</Date1>
      <Date2>dateTime</Date2>
      <Date3>dateTime</Date3>
      <Date4>dateTime</Date4>
      <Date5>dateTime</Date5>
      <MiddleName>string</MiddleName>
      <NameSuffix>string</NameSuffix>
      <BinaryPlacementPreference>int</BinaryPlacementPreference>
      <UseBinaryHoldingTank>boolean</UseBinaryHoldingTank>
      <MainAddressVerified>boolean</MainAddressVerified>
      <MailAddressVerified>boolean</MailAddressVerified>
      <OtherAddressVerified>boolean</OtherAddressVerified>
      <SponsorKey>string</SponsorKey>
      <EnrollerKey>string</EnrollerKey>
      <ManualCustomerKey>string</ManualCustomerKey>
      <PayableTy>string</PayableTy>
      <GenderID>string</GenderID>
    </CreateCustomerRequest>
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
    <CreateCustomerResult xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
    </CreateCustomerResult>
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
    var req = new CreateCustomerRequest();

    req.FirstName = "John";         //The customer's first name
    req.LastName = "Doe";           //The customer's last name
    req.Company = "ACME, Inc.";     //The customer's company name
    req.CustomerType = 1;           //The customer's type as defined by the company
    req.CustomerStatus = 1;         //The customer's status as defined by the company. Defaults to 1.
    req.Email = "joecool@me.com";
    req.Phone = "555-555-5555";
    req.MainAddress1 = "123 Some Street";
    req.MainCity = "Dallas";
    req.MainState = "TX";           //The state of the customer's primary address. This field is required if MainAddress1 is provided.
    req.MainZip = "75207";
    req.MailState = "1";            //The state of the customer's mailing address. This field is required if MailAddress1 is provided.
    req.MailCountry = "1";          //The country of the customer's mailing address. This field is required if MailAddress1 is provided.
    req.OtherState = "1";           //The state of the customer's other address. This field is required if OtherAddress1 is provided.
    req.OtherCountry = "1";         //The country of the customer's other address. This field is required if OtherAddress1 is provided.
    req.TaxIDType = "SSN";
    req.MiddleName = "1";           //The customer's middle name
    req.NameSuffix = "1";           //The customer's name suffix
    req.BinaryPlacementPreference = 1;
    req.UseBinaryHoldingTank = true;
    req.MainAddressVerified = true;
    req.MailAddressVerified = true;
    req.OtherAddressVerified = true;
    req.PayableTy = "Check";

    //Send Request to Server and Get Response
    var res = await api.CreateCustomerAsync(req);

    //Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID);
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
    CreateCustomerRequest req = new CreateCustomerRequest();

    req.FirstName = "John";         //The customer's first name
    req.LastName = "Doe";           //The customer's last name
    req.Company = "ACME, Inc.";     //The customer's company name
    req.CustomerType = 1;           //The customer's type as defined by the company
    req.CustomerStatus = 1;         //The customer's status as defined by the company. Defaults to 1.
    req.Email = "joecool@me.com";
    req.Phone = "555-555-5555";
    req.MainAddress1 = "123 Some Street";
    req.MainCity = "Dallas";
    req.MainState = "TX";           //The state of the customer's primary address. This field is required if MainAddress1 is provided.
    req.MainZip = "75207";
    req.MailState = "1";            //The state of the customer's mailing address. This field is required if MailAddress1 is provided.
    req.MailCountry = "1";          //The country of the customer's mailing address. This field is required if MailAddress1 is provided.
    req.OtherState = "1";           //The state of the customer's other address. This field is required if OtherAddress1 is provided.
    req.OtherCountry = "1";         //The country of the customer's other address. This field is required if OtherAddress1 is provided.
    req.TaxIDType = "SSN";
    req.MiddleName = "1";           //The customer's middle name
    req.NameSuffix = "1";           //The customer's name suffix
    req.BinaryPlacementPreference = 1;
    req.UseBinaryHoldingTank = true;
    req.MainAddressVerified = true;
    req.MailAddressVerified = true;
    req.OtherAddressVerified = true;
    req.PayableTy = "Check";

    //Send Request to Server and Get Response
    CreateCustomerResponse res = api.CreateCustomer(req);

    //Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID);
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
    Dim req as new CreateCustomerRequest()

    req.FirstName = "John"
    req.LastName = "Doe"
    req.Company = "ACME, Inc."
    req.CustomerType = 1
    req.CustomerStatus = 1
    req.Email = "joecool@me.com"
    req.Phone = "555-555-5555"
    req.MainAddress1 = "123 Some Street"
    req.MainCity = "Dallas"
    req.MainState = "TX"
    req.MainZip = "75207"
    req.MailState = "1"
    req.MailCountry = "1"
    req.OtherState = "1"
    req.OtherCountry = "1"
    req.TaxIDType = "SSN"
    req.MiddleName = "1"
    req.NameSuffix = "1"
    req.BinaryPlacementPreference = 1
    req.UseBinaryHoldingTank = true
    req.MainAddressVerified = true
    req.MailAddressVerified = true
    req.OtherAddressVerified = true
    req.PayableTy = "Check"

    'Send Request to Server and Get Response
    Dim res As CreateCustomerResponse = api.CreateCustomer(req)

    'Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID)
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

    $req->FirstName = "John";
    $req->LastName = "Doe";
    $req->Company = "ACME, Inc.";
    $req->CustomerType = 1;
    $req->CustomerStatus = 1;
    $req->Email = "joecool@me.com";
    $req->Phone = "555-555-5555";
    $req->MainAddress1 = "123 Some Street";
    $req->MainCity = "Dallas";
    $req->MainState = "TX";
    $req->MainZip = "75207";
    $req->MailState = "1";
    $req->MailCountry = "1";
    $req->OtherState = "1";
    $req->OtherCountry = "1";
    $req->TaxIDType = "SSN";
    $req->MiddleName = "1";
    $req->NameSuffix = "1";
    $req->BinaryPlacementPreference = 1;
    $req->UseBinaryHoldingTank = 1;
    $req->MainAddressVerified = 1;
    $req->MailAddressVerified = 1;
    $req->OtherAddressVerified = 1;
    $req->PayableTy = "Check";

    //Send Request to Server and Get Response
    $res = $api.CreateCustomer($req);

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
    CreateCustomerRequest req = new CreateCustomerRequest();

    req.setFirstName("John");
    req.setLastName("Doe");
    req.setCompany("ACME, Inc.");
    req.setCustomerType(1);
    req.setCustomerStatus(1);
    req.setEmail("joecool@me.com");
    req.setPhone("555-555-5555");
    req.setMainAddress1("123 Some Street");
    req.setMainCity("Dallas");
    req.setMainState("TX");
    req.setMainZip("75207");
    req.setMailState("1");
    req.setMailCountry("1");
    req.setOtherState("1");
    req.setOtherCountry("1");
    req.setTaxIDType("SSN");
    req.setMiddleName("1");
    req.setNameSuffix("1");
    req.setBinaryPlacementPreference(1);
    req.setUseBinaryHoldingTank(1);
    req.setMainAddressVerified(1);
    req.setMailAddressVerified(1);
    req.setOtherAddressVerified(1);
    req.setPayableTy("Check");

    //Send Request to Server and Get Response
    CreateCustomerResponse res = api.getExigoApiSoap().createCustomer(req, auth);

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

### UpdateCustomer

> Updates one or more fields on an existing customer.
>  Can participate in a transaction.

| | |
|---|---|
| Category | Customers |
| REST | `PATCH /3.0/customers` |
| SOAP action | `https://api.exigo.com/UpdateCustomer` |
| WSDL elements | `UpdateCustomerRequest` → `UpdateCustomerResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateCustomer |

#### Input

**`UpdateCustomerRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `FirstName` | `String` | Optional. |
| `LastName` | `String` | Optional. |
| `Company` | `String` | Optional. |
| `CustomerType` | `Int32` | Optional. Classification of a customer as defined by the company.<br>**Lookup:** company-specific list (see company-lists.md) |
| `CustomerStatus` | `Int32` | Optional. Current status of a customer as defined by the company.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Email` | `String` | Optional. |
| `Phone` | `String` | Optional. |
| `Phone2` | `String` | Optional. |
| `MobilePhone` | `String` | Optional. |
| `Fax` | `String` | Optional. |
| `MainAddress1` | `String` | Optional. |
| `MainAddress2` | `String` | Optional. |
| `MainAddress3` | `String` | Optional. |
| `MainCity` | `String` | Optional. |
| `MainState` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `MainZip` | `String` | Optional. |
| `MainCountry` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `MainCounty` | `String` | Optional. |
| `MailAddress1` | `String` | Optional. |
| `MailAddress2` | `String` | Optional. |
| `MailAddress3` | `String` | Optional. |
| `MailCity` | `String` | Optional. |
| `MailState` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `MailZip` | `String` | Optional. |
| `MailCountry` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `MailCounty` | `String` | Optional. |
| `OtherAddress1` | `String` | Optional. |
| `OtherAddress2` | `String` | Optional. |
| `OtherAddress3` | `String` | Optional. |
| `OtherCity` | `String` | Optional. |
| `OtherState` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `OtherZip` | `String` | Optional. |
| `OtherCountry` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `OtherCounty` | `String` | Optional. |
| `CanLogin` | `Boolean` | Optional. |
| `LoginName` | `String` | Optional. |
| `LoginPassword` | `String` | Optional. |
| `TaxID` | `String` | Optional. |
| `SalesTaxID` | `String` | Optional. |
| `SalesTaxExemptExpireDate` | `DateTime` | Optional. |
| `IsSalesTaxExempt` | `Boolean` | Optional. |
| `BirthDate` | `DateTime` | Optional. |
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
| `SubscribeToBroadcasts` | `Boolean` | Optional. |
| `SubscribeFromIPAddress` | `String` | Optional. |
| `CurrencyCode` | `String` | Optional. |
| `PayableToName` | `String` | Optional. |
| `PayableType` | `PayableType` | Optional. Obsolete field. Please consider upgrading to PayableTy.<br>**Values:** `Check`, `WireTransfer`, `PaymentCard`, `DirectDeposit`, `OnHold`, `BankWire`, `DebitCardHold`, `Other100` |
| `DefaultWarehouseID` | `Int32` | Optional. Unique location for orders.<br>**Lookup:** company-specific list (see company-lists.md) |
| `CheckThreshold` | `Decimal` | Optional. |
| `CreatedDate` | `DateTime` | Optional. |
| `TaxIDType` | `TaxIDType` | Optional. Obsolete field. Please consider upgrading to TaxIDTy.<br>**Values:** `SSN`, `EIN`, `OtherType3`, `OtherType4`, `OtherType5`, `OtherType6`, `OtherType7`, `OtherType8`, `OtherType9`, `OtherType10`, `OtherType11`, `OtherType12`, `OtherType13`, `OtherType14`, `OtherType15`, `OtherType16`, `OtherType17`, `OtherType18`, `OtherType19`, `OtherType20` |
| `LanguageID` | `Int32` | Optional. Customize the web experience by setting this.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Gender` | `Gender` | Optional. Obsolete field. Please consider upgrading to GenderID.<br>**Values:** `Unknown`, `Male`, `Female` |
| `VatRegistration` | `String` | Optional. |
| `Date1` | `DateTime` | Optional. |
| `Date2` | `DateTime` | Optional. |
| `Date3` | `DateTime` | Optional. |
| `Date4` | `DateTime` | Optional. |
| `Date5` | `DateTime` | Optional. |
| `MiddleName` | `String` | Optional. |
| `NameSuffix` | `String` | Optional. |
| `BinaryPlacementPreference` | `Int32` | Optional. |
| `UseBinaryHoldingTank` | `Boolean` | Optional. |
| `MainAddressVerified` | `Boolean` | Optional. |
| `MailAddressVerified` | `Boolean` | Optional. |
| `OtherAddressVerified` | `Boolean` | Optional. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |
| `PayableTy` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `TaxIDTy` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `GenderID` | `String` | Optional. The customer's gender.<br>**Lookup:** company-specific list (see company-lists.md) |
| `EntryDate` | `DateTime` | Optional. |

#### Output

**`UpdateCustomerResponse`**

_No properties._

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/customers HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "firstName": null,
  "lastName": null,
  "company": null,
  "customerType": null,
  "customerStatus": null,
  "email": null,
  "phone": null,
  "phone2": null,
  "mobilePhone": null,
  "fax": null,
  "mainAddress1": null,
  "mainAddress2": null,
  "mainAddress3": null,
  "mainCity": null,
  "mainState": null,
  "mainZip": null,
  "mainCountry": null,
  "mainCounty": null,
  "mailAddress1": null,
  "mailAddress2": null,
  "mailAddress3": null,
  "mailCity": null,
  "mailZip": null,
  "mailCounty": null,
  "otherAddress1": null,
  "otherAddress2": null,
  "otherAddress3": null,
  "otherCity": null,
  "otherZip": null,
  "otherCounty": null,
  "canLogin": null,
  "loginName": null,
  "loginPassword": null,
  "taxID": null,
  "salesTaxID": null,
  "salesTaxExemptExpireDate": "2026-11-10T00:00:00-06:00",
  "birthDate": null,
  "payableToName": null,
  "defaultWarehouseID": 1,
  "date1": "2026-11-10T00:00:00-06:00",
  "date2": "2026-11-10T00:00:00-06:00",
  "date3": "2026-11-10T00:00:00-06:00",
  "date4": "2026-11-10T00:00:00-06:00",
  "date5": "2026-11-10T00:00:00-06:00",
  "middleName": null,
  "nameSuffix": null,
  "binaryPlacementPreference": 1,
  "useBinaryHoldingTank": true,
  "mainAddressVerified": true,
  "mailAddressVerified": true,
  "otherAddressVerified": true,
  "customerKey": "1",
  "payableTy": "Check",
  "taxIDTy": "SSN",
  "entryDate": "2026-11-10T00:00:00-06:00"
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
SOAPAction: "https://api.exigo.com/UpdateCustomer"

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
    <UpdateCustomerRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <FirstName>string</FirstName>
      <LastName>string</LastName>
      <Company>string</Company>
      <CustomerType>int</CustomerType>
      <CustomerStatus>int</CustomerStatus>
      <Email>string</Email>
      <Phone>string</Phone>
      <Phone2>string</Phone2>
      <MobilePhone>string</MobilePhone>
      <Fax>string</Fax>
      <MainAddress1>string</MainAddress1>
      <MainAddress2>string</MainAddress2>
      <MainAddress3>string</MainAddress3>
      <MainCity>string</MainCity>
      <MainState>string</MainState>
      <MainZip>string</MainZip>
      <MainCountry>string</MainCountry>
      <MainCounty>string</MainCounty>
      <MailAddress1>string</MailAddress1>
      <MailAddress2>string</MailAddress2>
      <MailAddress3>string</MailAddress3>
      <MailCity>string</MailCity>
      <MailState>string</MailState>
      <MailZip>string</MailZip>
      <MailCountry>string</MailCountry>
      <MailCounty>string</MailCounty>
      <OtherAddress1>string</OtherAddress1>
      <OtherAddress2>string</OtherAddress2>
      <OtherAddress3>string</OtherAddress3>
      <OtherCity>string</OtherCity>
      <OtherState>string</OtherState>
      <OtherZip>string</OtherZip>
      <OtherCountry>string</OtherCountry>
      <OtherCounty>string</OtherCounty>
      <CanLogin>boolean</CanLogin>
      <LoginName>string</LoginName>
      <LoginPassword>string</LoginPassword>
      <TaxID>string</TaxID>
      <SalesTaxID>string</SalesTaxID>
      <SalesTaxExemptExpireDate>dateTime</SalesTaxExemptExpireDate>
      <IsSalesTaxExempt>boolean</IsSalesTaxExempt>
      <BirthDate>dateTime</BirthDate>
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
      <SubscribeToBroadcasts>boolean</SubscribeToBroadcasts>
      <SubscribeFromIPAddress>string</SubscribeFromIPAddress>
      <CurrencyCode>string</CurrencyCode>
      <PayableToName>string</PayableToName>
      <PayableType>Check or WireTransfer or PaymentCard or DirectDeposit or OnHold or BankWire or DebitCardHold or Other100</PayableType>
      <DefaultWarehouseID>int</DefaultWarehouseID>
      <CheckThreshold>decimal</CheckThreshold>
      <CreatedDate>dateTime</CreatedDate>
      <TaxIDType>SSN or EIN or OtherType3 or OtherType4 or OtherType5 or OtherType6 or OtherType7 or OtherType8 or OtherType9 or OtherType10 or OtherType11 or OtherType12 or OtherType13 or OtherType14 or OtherType15 or OtherType16 or OtherType17 or OtherType18 or OtherType19 or OtherType20</TaxIDType>
      <LanguageID>int</LanguageID>
      <Gender>Unknown or Male or Female</Gender>
      <VatRegistration>string</VatRegistration>
      <Date1>dateTime</Date1>
      <Date2>dateTime</Date2>
      <Date3>dateTime</Date3>
      <Date4>dateTime</Date4>
      <Date5>dateTime</Date5>
      <MiddleName>string</MiddleName>
      <NameSuffix>string</NameSuffix>
      <BinaryPlacementPreference>int</BinaryPlacementPreference>
      <UseBinaryHoldingTank>boolean</UseBinaryHoldingTank>
      <MainAddressVerified>boolean</MainAddressVerified>
      <MailAddressVerified>boolean</MailAddressVerified>
      <OtherAddressVerified>boolean</OtherAddressVerified>
      <CustomerKey>string</CustomerKey>
      <PayableTy>string</PayableTy>
      <TaxIDTy>string</TaxIDTy>
      <GenderID>string</GenderID>
      <EntryDate>dateTime</EntryDate>
    </UpdateCustomerRequest>
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
    <UpdateCustomerResult xmlns="http://api.exigo.com/" />
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
    var req = new UpdateCustomerRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.FirstName = 1;
    req.LastName = 1;
    req.Company = 1;
    req.CustomerType = 1;           //Classification of a customer as defined by the company
    req.CustomerStatus = 1;         //Current status of a customer as defined by the company
    req.Email = 1;
    req.Phone = 1;
    req.Phone2 = 1;
    req.MobilePhone = 1;
    req.Fax = 1;
    req.MainAddress1 = 1;
    req.MainAddress2 = 1;
    req.MainAddress3 = 1;
    req.MainCity = 1;
    req.MainState = TX;
    req.MainZip = 1;
    req.MainCountry = US;
    req.MainCounty = 1;
    req.MailAddress1 = 1;
    req.MailAddress2 = 1;
    req.MailAddress3 = 1;
    req.MailCity = 1;
    req.MailZip = 1;
    req.MailCounty = 1;
    req.OtherAddress1 = 1;
    req.OtherAddress2 = 1;
    req.OtherAddress3 = 1;
    req.OtherCity = 1;
    req.OtherZip = 1;
    req.OtherCounty = 1;
    req.CanLogin = 1;
    req.LoginName = 1;
    req.LoginPassword = 1;
    req.TaxID = 1;
    req.SalesTaxID = 1;
    req.SalesTaxExemptExpireDate = DateTime.Today;
    req.BirthDate = 1;
    req.PayableToName = 1;
    req.DefaultWarehouseID = 1;     //Unique location for orders
    req.Date1 = DateTime.Today;
    req.Date2 = DateTime.Today;
    req.Date3 = DateTime.Today;
    req.Date4 = DateTime.Today;
    req.Date5 = DateTime.Today;
    req.MiddleName = 1;
    req.NameSuffix = 1;
    req.BinaryPlacementPreference = 1;
    req.UseBinaryHoldingTank = true;
    req.MainAddressVerified = true;
    req.MailAddressVerified = true;
    req.OtherAddressVerified = true;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.PayableTy = "Check";
    req.TaxIDTy = "SSN";
    req.EntryDate = DateTime.Today;

    //Send Request to Server and Get Response
    var res = await api.UpdateCustomerAsync(req);

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
    UpdateCustomerRequest req = new UpdateCustomerRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.FirstName = 1;
    req.LastName = 1;
    req.Company = 1;
    req.CustomerType = 1;           //Classification of a customer as defined by the company
    req.CustomerStatus = 1;         //Current status of a customer as defined by the company
    req.Email = 1;
    req.Phone = 1;
    req.Phone2 = 1;
    req.MobilePhone = 1;
    req.Fax = 1;
    req.MainAddress1 = 1;
    req.MainAddress2 = 1;
    req.MainAddress3 = 1;
    req.MainCity = 1;
    req.MainState = TX;
    req.MainZip = 1;
    req.MainCountry = US;
    req.MainCounty = 1;
    req.MailAddress1 = 1;
    req.MailAddress2 = 1;
    req.MailAddress3 = 1;
    req.MailCity = 1;
    req.MailZip = 1;
    req.MailCounty = 1;
    req.OtherAddress1 = 1;
    req.OtherAddress2 = 1;
    req.OtherAddress3 = 1;
    req.OtherCity = 1;
    req.OtherZip = 1;
    req.OtherCounty = 1;
    req.CanLogin = 1;
    req.LoginName = 1;
    req.LoginPassword = 1;
    req.TaxID = 1;
    req.SalesTaxID = 1;
    req.SalesTaxExemptExpireDate = DateTime.Today;
    req.BirthDate = 1;
    req.PayableToName = 1;
    req.DefaultWarehouseID = 1;     //Unique location for orders
    req.Date1 = DateTime.Today;
    req.Date2 = DateTime.Today;
    req.Date3 = DateTime.Today;
    req.Date4 = DateTime.Today;
    req.Date5 = DateTime.Today;
    req.MiddleName = 1;
    req.NameSuffix = 1;
    req.BinaryPlacementPreference = 1;
    req.UseBinaryHoldingTank = true;
    req.MainAddressVerified = true;
    req.MailAddressVerified = true;
    req.OtherAddressVerified = true;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.PayableTy = "Check";
    req.TaxIDTy = "SSN";
    req.EntryDate = DateTime.Today;

    //Send Request to Server and Get Response
    UpdateCustomerResponse res = api.UpdateCustomer(req);

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
    Dim req as new UpdateCustomerRequest()

    req.CustomerID = 1
    req.FirstName = 1
    req.LastName = 1
    req.Company = 1
    req.CustomerType = 1
    req.CustomerStatus = 1
    req.Email = 1
    req.Phone = 1
    req.Phone2 = 1
    req.MobilePhone = 1
    req.Fax = 1
    req.MainAddress1 = 1
    req.MainAddress2 = 1
    req.MainAddress3 = 1
    req.MainCity = 1
    req.MainState = TX
    req.MainZip = 1
    req.MainCountry = US
    req.MainCounty = 1
    req.MailAddress1 = 1
    req.MailAddress2 = 1
    req.MailAddress3 = 1
    req.MailCity = 1
    req.MailZip = 1
    req.MailCounty = 1
    req.OtherAddress1 = 1
    req.OtherAddress2 = 1
    req.OtherAddress3 = 1
    req.OtherCity = 1
    req.OtherZip = 1
    req.OtherCounty = 1
    req.CanLogin = 1
    req.LoginName = 1
    req.LoginPassword = 1
    req.TaxID = 1
    req.SalesTaxID = 1
    req.SalesTaxExemptExpireDate = DateTime.Today
    req.BirthDate = 1
    req.PayableToName = 1
    req.DefaultWarehouseID = 1
    req.Date1 = DateTime.Today
    req.Date2 = DateTime.Today
    req.Date3 = DateTime.Today
    req.Date4 = DateTime.Today
    req.Date5 = DateTime.Today
    req.MiddleName = 1
    req.NameSuffix = 1
    req.BinaryPlacementPreference = 1
    req.UseBinaryHoldingTank = true
    req.MainAddressVerified = true
    req.MailAddressVerified = true
    req.OtherAddressVerified = true
    req.CustomerKey = "1"
    req.PayableTy = "Check"
    req.TaxIDTy = "SSN"
    req.EntryDate = DateTime.Today

    'Send Request to Server and Get Response
    Dim res As UpdateCustomerResponse = api.UpdateCustomer(req)

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
    $req->FirstName = 1;
    $req->LastName = 1;
    $req->Company = 1;
    $req->CustomerType = 1;
    $req->CustomerStatus = 1;
    $req->Email = 1;
    $req->Phone = 1;
    $req->Phone2 = 1;
    $req->MobilePhone = 1;
    $req->Fax = 1;
    $req->MainAddress1 = 1;
    $req->MainAddress2 = 1;
    $req->MainAddress3 = 1;
    $req->MainCity = 1;
    $req->MainState = TX;
    $req->MainZip = 1;
    $req->MainCountry = US;
    $req->MainCounty = 1;
    $req->MailAddress1 = 1;
    $req->MailAddress2 = 1;
    $req->MailAddress3 = 1;
    $req->MailCity = 1;
    $req->MailZip = 1;
    $req->MailCounty = 1;
    $req->OtherAddress1 = 1;
    $req->OtherAddress2 = 1;
    $req->OtherAddress3 = 1;
    $req->OtherCity = 1;
    $req->OtherZip = 1;
    $req->OtherCounty = 1;
    $req->CanLogin = 1;
    $req->LoginName = 1;
    $req->LoginPassword = 1;
    $req->TaxID = 1;
    $req->SalesTaxID = 1;
    $req->SalesTaxExemptExpireDate = 1;
    $req->BirthDate = 1;
    $req->PayableToName = 1;
    $req->DefaultWarehouseID = 1;
    $req->Date1 = 1;
    $req->Date2 = 1;
    $req->Date3 = 1;
    $req->Date4 = 1;
    $req->Date5 = 1;
    $req->MiddleName = 1;
    $req->NameSuffix = 1;
    $req->BinaryPlacementPreference = 1;
    $req->UseBinaryHoldingTank = 1;
    $req->MainAddressVerified = 1;
    $req->MailAddressVerified = 1;
    $req->OtherAddressVerified = 1;
    $req->CustomerKey = "1";
    $req->PayableTy = "Check";
    $req->TaxIDTy = "SSN";
    $req->EntryDate = 1;

    //Send Request to Server and Get Response
    $res = $api.UpdateCustomer($req);

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
    UpdateCustomerRequest req = new UpdateCustomerRequest();

    req.setCustomerID(1);
    req.setFirstName(1);
    req.setLastName(1);
    req.setCompany(1);
    req.setCustomerType(1);
    req.setCustomerStatus(1);
    req.setEmail(1);
    req.setPhone(1);
    req.setPhone2(1);
    req.setMobilePhone(1);
    req.setFax(1);
    req.setMainAddress1(1);
    req.setMainAddress2(1);
    req.setMainAddress3(1);
    req.setMainCity(1);
    req.setMainState(TX);
    req.setMainZip(1);
    req.setMainCountry(US);
    req.setMainCounty(1);
    req.setMailAddress1(1);
    req.setMailAddress2(1);
    req.setMailAddress3(1);
    req.setMailCity(1);
    req.setMailZip(1);
    req.setMailCounty(1);
    req.setOtherAddress1(1);
    req.setOtherAddress2(1);
    req.setOtherAddress3(1);
    req.setOtherCity(1);
    req.setOtherZip(1);
    req.setOtherCounty(1);
    req.setCanLogin(1);
    req.setLoginName(1);
    req.setLoginPassword(1);
    req.setTaxID(1);
    req.setSalesTaxID(1);
    req.setSalesTaxExemptExpireDate(1);
    req.setBirthDate(1);
    req.setPayableToName(1);
    req.setDefaultWarehouseID(1);
    req.setDate1(1);
    req.setDate2(1);
    req.setDate3(1);
    req.setDate4(1);
    req.setDate5(1);
    req.setMiddleName(1);
    req.setNameSuffix(1);
    req.setBinaryPlacementPreference(1);
    req.setUseBinaryHoldingTank(1);
    req.setMainAddressVerified(1);
    req.setMailAddressVerified(1);
    req.setOtherAddressVerified(1);
    req.setCustomerKey("1");
    req.setPayableTy("Check");
    req.setTaxIDTy("SSN");
    req.setEntryDate(1);

    //Send Request to Server and Get Response
    UpdateCustomerResponse res = api.getExigoApiSoap().updateCustomer(req, auth);

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

### AuthenticateCustomer

> Authenticates a customer for login using UserName and Password combination.

| | |
|---|---|
| Category | Customers |
| REST | `POST /3.0/customers/authenticate` |
| SOAP action | `https://api.exigo.com/AuthenticateCustomer` |
| WSDL elements | `AuthenticateCustomerRequest` → `AuthenticateCustomerResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=AuthenticateCustomer |

#### Input

**`AuthenticateCustomerRequest`**

| Property | Type | Notes |
|---|---|---|
| `LoginName` | `String` | The customer's login name. |
| `Password` | `String` | The customer's password. |

#### Output

**`AuthenticateCustomerResponse`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `FirstName` | `String` | Customer first name. |
| `LastName` | `String` | Customer first name. |
| `CustomerKey` | `String` | Unique alpha numeric identifier for customer record. |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/customers/authenticate HTTP/1.1
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
  "customerID": 1,
  "firstName": "",
  "lastName": "",
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
SOAPAction: "https://api.exigo.com/AuthenticateCustomer"

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
    <AuthenticateCustomerRequest xmlns="http://api.exigo.com/">
      <LoginName>string</LoginName>
      <Password>string</Password>
    </AuthenticateCustomerRequest>
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
    <AuthenticateCustomerResult xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <FirstName>string</FirstName>
      <LastName>string</LastName>
      <CustomerKey>string</CustomerKey>
    </AuthenticateCustomerResult>
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
    var req = new AuthenticateCustomerRequest();

    req.LoginName = "1";            //The customer's login name
    req.Password = "1";             //The customer's password

    //Send Request to Server and Get Response
    var res = await api.AuthenticateCustomerAsync(req);

    //Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID);
    Console.WriteLine("FirstName: {0}", res.FirstName);
    Console.WriteLine("LastName: {0}", res.LastName);
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
    AuthenticateCustomerRequest req = new AuthenticateCustomerRequest();

    req.LoginName = "1";            //The customer's login name
    req.Password = "1";             //The customer's password

    //Send Request to Server and Get Response
    AuthenticateCustomerResponse res = api.AuthenticateCustomer(req);

    //Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID);
    Console.WriteLine("FirstName: {0}", res.FirstName);
    Console.WriteLine("LastName: {0}", res.LastName);
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
    Dim req as new AuthenticateCustomerRequest()

    req.LoginName = "1"
    req.Password = "1"

    'Send Request to Server and Get Response
    Dim res As AuthenticateCustomerResponse = api.AuthenticateCustomer(req)

    'Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID)
    Console.WriteLine("FirstName: {0}", res.FirstName)
    Console.WriteLine("LastName: {0}", res.LastName)
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

    $req->LoginName = "1";
    $req->Password = "1";

    //Send Request to Server and Get Response
    $res = $api.AuthenticateCustomer($req);

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
    AuthenticateCustomerRequest req = new AuthenticateCustomerRequest();

    req.setLoginName("1");
    req.setPassword("1");

    //Send Request to Server and Get Response
    AuthenticateCustomerResponse res = api.getExigoApiSoap().authenticateCustomer(req, auth);

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

### SetAccountCreditCardToken

> Setup primary or secondary credit card token on file for an
>  existing customer, or new customer in a transaction.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Customers |
| REST | `PUT /3.0/account/cctoken` |
| SOAP action | `https://api.exigo.com/SetAccountCreditCardToken` |
| WSDL elements | `SetAccountCreditCardTokenRequest` → `SetAccountCreditCardTokenResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=SetAccountCreditCardToken |

#### Input

**`SetAccountCreditCardTokenRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CreditCardAccountType` | `AccountCreditCardType` | Optional. Whether the credit card is the customer's primary or secondary card. Defaults to Primary.<br>**Values:** `Primary`, `Secondary` |
| `CreditCardToken` | `String` | The credit card's token created by the Token Provider. |
| `ExpirationMonth` | `Int32` | The month of the card's expiration date. |
| `ExpirationYear` | `Int32` | The year of the card's expiration date. |
| `CreditCardType` | `Int32` | Optional. Defaults to 1. |
| `BillingName` | `String` | Optional. |
| `UseMainAddress` | `Boolean` | If true, the customer's main address on file will be used. If UseMainAddress is set to true, do not submit a seperate billing address. |
| `BillingAddress` | `String` | Optional. |
| `BillingAddress2` | `String` | Optional. |
| `BillingCity` | `String` | Optional. |
| `BillingState` | `String` | The state of the card's billing address. If UseMainAddress is set to true, do not set this field. |
| `BillingZip` | `String` | Optional. |
| `BillingCountry` | `String` | The country of the card's billing address. If UseMainAddress is set to true, do not set this field. |
| `HideFromWeb` | `Boolean` | Optional. Can be used for AutoOrder but will not show up in shopping cart. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exception will occur if CustomerID & CustomerKey are provided. |
| `MovePrimaryToSecondary` | `Boolean` | Optional. If true, the new card will be added as the primary card and the existing primary card will overwrite the secondary slot. Defaults to False. |
| `TokenType` | `Int32` | Optional. Optionally supply TokenType. |
| `FirstSix` | `String` | Optional. Optionally supply card prefix. |
| `LastFour` | `String` | Optional. Optionally supply card last four. |

#### Output

**`SetAccountResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/account/cctoken HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "creditCardAccountType": null,
  "creditCardToken": "5AE56HJ42OPZ5487",
  "expirationMonth": 1,
  "expirationYear": 2015,
  "creditCardType": 1,
  "useMainAddress": true,
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
SOAPAction: "https://api.exigo.com/SetAccountCreditCardToken"

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
    <SetAccountCreditCardTokenRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CreditCardAccountType>Primary or Secondary</CreditCardAccountType>
      <CreditCardToken>string</CreditCardToken>
      <ExpirationMonth>int</ExpirationMonth>
      <ExpirationYear>int</ExpirationYear>
      <CreditCardType>int</CreditCardType>
      <BillingName>string</BillingName>
      <UseMainAddress>boolean</UseMainAddress>
      <BillingAddress>string</BillingAddress>
      <BillingAddress2>string</BillingAddress2>
      <BillingCity>string</BillingCity>
      <BillingState>string</BillingState>
      <BillingZip>string</BillingZip>
      <BillingCountry>string</BillingCountry>
      <HideFromWeb>boolean</HideFromWeb>
      <CustomerKey>string</CustomerKey>
      <MovePrimaryToSecondary>boolean</MovePrimaryToSecondary>
      <TokenType>int</TokenType>
      <FirstSix>string</FirstSix>
      <LastFour>string</LastFour>
    </SetAccountCreditCardTokenRequest>
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
    <SetAccountCreditCardTokenResult xmlns="http://api.exigo.com/" />
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
    var req = new SetAccountCreditCardTokenRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CreditCardAccountType = AccountCreditCardType.Primary;  //Whether the credit card is the customer's primary or secondary card.
    req.CreditCardToken = "5AE56HJ42OPZ5487";//The credit card's token created by the Token Provider
    req.ExpirationMonth = 1;        //The month of the card's expiration date
    req.ExpirationYear = 2015;      //The year of the card's expiration date
    req.CreditCardType = 1;         //Defaults to 1.
    req.UseMainAddress = true;         //If true, the customer's main address on file will be used. If UseMainAddress is set to true, do not submit a seperate billing address
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exception will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.SetAccountCreditCardTokenAsync(req);

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
    SetAccountCreditCardTokenRequest req = new SetAccountCreditCardTokenRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CreditCardAccountType = AccountCreditCardType.Primary;  //Whether the credit card is the customer's primary or secondary card.
    req.CreditCardToken = "5AE56HJ42OPZ5487";//The credit card's token created by the Token Provider
    req.ExpirationMonth = 1;        //The month of the card's expiration date
    req.ExpirationYear = 2015;      //The year of the card's expiration date
    req.CreditCardType = 1;         //Defaults to 1.
    req.UseMainAddress = true;         //If true, the customer's main address on file will be used. If UseMainAddress is set to true, do not submit a seperate billing address
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exception will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    SetAccountResponse res = api.SetAccountCreditCardToken(req);

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
    Dim req as new SetAccountCreditCardTokenRequest()

    req.CustomerID = 1
    req.CreditCardAccountType = AccountCreditCardType.Primary
    req.CreditCardToken = "5AE56HJ42OPZ5487"
    req.ExpirationMonth = 1
    req.ExpirationYear = 2015
    req.CreditCardType = 1
    req.UseMainAddress = true
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As SetAccountResponse = api.SetAccountCreditCardToken(req)

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
    $req->CreditCardAccountType = 1;
    $req->CreditCardToken = "5AE56HJ42OPZ5487";
    $req->ExpirationMonth = 1;
    $req->ExpirationYear = 2015;
    $req->CreditCardType = 1;
    $req->UseMainAddress = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.SetAccountCreditCardToken($req);

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
    SetAccountCreditCardTokenRequest req = new SetAccountCreditCardTokenRequest();

    req.setCustomerID(1);
    req.setCreditCardAccountType(1);
    req.setCreditCardToken("5AE56HJ42OPZ5487");
    req.setExpirationMonth(1);
    req.setExpirationYear(2015);
    req.setCreditCardType(1);
    req.setUseMainAddress(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    SetAccountResponse res = api.getExigoApiSoap().setAccountCreditCardToken(req, auth);

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

### SetAccountChecking

> Setup bank account on file an existing customer, or new customer
>  in a transaction. You can also empty the account settings by simply leaving everything but CustomerID empty.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Customers |
| REST | `PUT /3.0/account/checking` |
| SOAP action | `https://api.exigo.com/SetAccountChecking` |
| WSDL elements | `SetAccountCheckingRequest` → `SetAccountCheckingResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=SetAccountChecking |

#### Input

**`SetAccountCheckingRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `BankAccountNumber` | `String` | Optional. |
| `BankRoutingNumber` | `String` | Optional. |
| `BankName` | `String` | Optional. |
| `BankAccountType` | `BankAccountType` | Optional. The type of bank account. Defaults to CheckingPersonal.<br>**Values:** `CheckingPersonal`, `CheckingBusiness`, `SavingsPersonal`, `SavingsBusiness` |
| `NameOnAccount` | `String` | Optional. |
| `UseMainAddress` | `Boolean` | If true, the customer's main address on file will be used. If UseMainAddress is set to true, do not submit a seperate billing address. |
| `BillingAddress` | `String` | Optional. |
| `BillingCity` | `String` | Optional. |
| `BillingState` | `String` | Optional. The state of the account's billing address. If UseMainAddress is set to true, do not set this field. |
| `BillingZip` | `String` | Optional. |
| `BillingCountry` | `String` | Optional. The country of the account's billing address. If UseMainAddress is set to true, do not set this field. |
| `DriversLicenseNumber` | `String` | Optional. |
| `Iban` | `String` | Optional. |
| `SwiftCode` | `String` | Optional. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`SetAccountResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/account/checking HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "bankAccountNumber": "",
  "bankRoutingNumber": "",
  "bankName": "",
  "bankAccountType": null,
  "nameOnAccount": "",
  "useMainAddress": true,
  "billingAddress": "",
  "billingCity": "",
  "billingZip": "",
  "driversLicenseNumber": "",
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
SOAPAction: "https://api.exigo.com/SetAccountChecking"

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
    <SetAccountCheckingRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <BankAccountNumber>string</BankAccountNumber>
      <BankRoutingNumber>string</BankRoutingNumber>
      <BankName>string</BankName>
      <BankAccountType>CheckingPersonal or CheckingBusiness or SavingsPersonal or SavingsBusiness</BankAccountType>
      <NameOnAccount>string</NameOnAccount>
      <UseMainAddress>boolean</UseMainAddress>
      <BillingAddress>string</BillingAddress>
      <BillingCity>string</BillingCity>
      <BillingState>string</BillingState>
      <BillingZip>string</BillingZip>
      <BillingCountry>string</BillingCountry>
      <DriversLicenseNumber>string</DriversLicenseNumber>
      <Iban>string</Iban>
      <SwiftCode>string</SwiftCode>
      <CustomerKey>string</CustomerKey>
    </SetAccountCheckingRequest>
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
    <SetAccountCheckingResult xmlns="http://api.exigo.com/" />
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
    var req = new SetAccountCheckingRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.BankAccountNumber = "1";
    req.BankRoutingNumber = "1";
    req.BankName = "1";
    req.BankAccountType = BankAccountType.CheckingPersonal;        //The type of bank account
    req.NameOnAccount = "1";
    req.UseMainAddress = true;         //If true, the customer's main address on file will be used. If UseMainAddress is set to true, do not submit a seperate billing address
    req.BillingAddress = "1";
    req.BillingCity = "1";
    req.BillingZip = "1";
    req.DriversLicenseNumber = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.SetAccountCheckingAsync(req);

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
    SetAccountCheckingRequest req = new SetAccountCheckingRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.BankAccountNumber = "1";
    req.BankRoutingNumber = "1";
    req.BankName = "1";
    req.BankAccountType = BankAccountType.CheckingPersonal;        //The type of bank account
    req.NameOnAccount = "1";
    req.UseMainAddress = true;         //If true, the customer's main address on file will be used. If UseMainAddress is set to true, do not submit a seperate billing address
    req.BillingAddress = "1";
    req.BillingCity = "1";
    req.BillingZip = "1";
    req.DriversLicenseNumber = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    SetAccountResponse res = api.SetAccountChecking(req);

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
    Dim req as new SetAccountCheckingRequest()

    req.CustomerID = 1
    req.BankAccountNumber = "1"
    req.BankRoutingNumber = "1"
    req.BankName = "1"
    req.BankAccountType = BankAccountType.CheckingPersonal
    req.NameOnAccount = "1"
    req.UseMainAddress = true
    req.BillingAddress = "1"
    req.BillingCity = "1"
    req.BillingZip = "1"
    req.DriversLicenseNumber = "1"
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As SetAccountResponse = api.SetAccountChecking(req)

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
    $req->BankAccountNumber = "1";
    $req->BankRoutingNumber = "1";
    $req->BankName = "1";
    $req->BankAccountType = 1;
    $req->NameOnAccount = "1";
    $req->UseMainAddress = 1;
    $req->BillingAddress = "1";
    $req->BillingCity = "1";
    $req->BillingZip = "1";
    $req->DriversLicenseNumber = "1";
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.SetAccountChecking($req);

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
    SetAccountCheckingRequest req = new SetAccountCheckingRequest();

    req.setCustomerID(1);
    req.setBankAccountNumber("1");
    req.setBankRoutingNumber("1");
    req.setBankName("1");
    req.setBankAccountType(1);
    req.setNameOnAccount("1");
    req.setUseMainAddress(1);
    req.setBillingAddress("1");
    req.setBillingCity("1");
    req.setBillingZip("1");
    req.setDriversLicenseNumber("1");
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    SetAccountResponse res = api.getExigoApiSoap().setAccountChecking(req, auth);

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

### SetAccountDirectDeposit

> Setup direct deposit info for an existing customer, or new customer
>  in a transaction. You can also empty the account settings by simply leaving everything but CustomerID empty.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Customers |
| REST | `PUT /3.0/account/directdeposit` |
| SOAP action | `https://api.exigo.com/SetAccountDirectDeposit` |
| WSDL elements | `SetAccountDirectDepositRequest` → `SetAccountDirectDepositResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=SetAccountDirectDeposit |

#### Input

**`SetAccountDirectDepositRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `NameOnAccount` | `String` | Optional. |
| `BankAccountNumber` | `String` | Optional. |
| `BankRoutingNumber` | `String` | Optional. |
| `DepositAccountType` | `DepositAccountType` | Deprecated, use DepositAccountTypeID instead.<br>**Values:** `Checking`, `Saving`, `Business`, `Personal` |
| `BankName` | `String` | Optional. |
| `BankAddress` | `String` | Optional. |
| `BankCity` | `String` | Optional. |
| `BankState` | `String` | Optional. |
| `BankZip` | `String` | Optional. |
| `BankCountry` | `String` | Optional. |
| `Iban` | `String` | Optional. |
| `SwiftCode` | `String` | Optional. |
| `BankAccountType` | `BankAccountType` | Deprecated, use DepositAccountTypeID instead.<br>**Values:** `CheckingPersonal`, `CheckingBusiness`, `SavingsPersonal`, `SavingsBusiness` |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |
| `DepositAccountTypeID` | `Int32` | Optional. Classification of bank account.<br>**Lookup:** company-specific list (see company-lists.md) |

#### Output

**`SetAccountResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/account/directdeposit HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "nameOnAccount": "",
  "bankAccountNumber": "",
  "bankRoutingNumber": "",
  "bankName": "",
  "bankAddress": "",
  "bankCity": "",
  "bankState": "",
  "bankZip": "",
  "bankCountry": "",
  "iban": "",
  "swiftCode": "",
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
SOAPAction: "https://api.exigo.com/SetAccountDirectDeposit"

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
    <SetAccountDirectDepositRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <NameOnAccount>string</NameOnAccount>
      <BankAccountNumber>string</BankAccountNumber>
      <BankRoutingNumber>string</BankRoutingNumber>
      <DepositAccountType>Checking or Saving or Business or Personal</DepositAccountType>
      <BankName>string</BankName>
      <BankAddress>string</BankAddress>
      <BankCity>string</BankCity>
      <BankState>string</BankState>
      <BankZip>string</BankZip>
      <BankCountry>string</BankCountry>
      <Iban>string</Iban>
      <SwiftCode>string</SwiftCode>
      <BankAccountType>CheckingPersonal or CheckingBusiness or SavingsPersonal or SavingsBusiness</BankAccountType>
      <CustomerKey>string</CustomerKey>
      <DepositAccountTypeID>int</DepositAccountTypeID>
    </SetAccountDirectDepositRequest>
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
    <SetAccountDirectDepositResult xmlns="http://api.exigo.com/" />
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
    var req = new SetAccountDirectDepositRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.NameOnAccount = "1";
    req.BankAccountNumber = "1";
    req.BankRoutingNumber = "1";
    req.BankName = "1";
    req.BankAddress = "1";
    req.BankCity = "1";
    req.BankState = "1";
    req.BankZip = "1";
    req.BankCountry = "1";
    req.Iban = "1";
    req.SwiftCode = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.SetAccountDirectDepositAsync(req);

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
    SetAccountDirectDepositRequest req = new SetAccountDirectDepositRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.NameOnAccount = "1";
    req.BankAccountNumber = "1";
    req.BankRoutingNumber = "1";
    req.BankName = "1";
    req.BankAddress = "1";
    req.BankCity = "1";
    req.BankState = "1";
    req.BankZip = "1";
    req.BankCountry = "1";
    req.Iban = "1";
    req.SwiftCode = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    SetAccountResponse res = api.SetAccountDirectDeposit(req);

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
    Dim req as new SetAccountDirectDepositRequest()

    req.CustomerID = 1
    req.NameOnAccount = "1"
    req.BankAccountNumber = "1"
    req.BankRoutingNumber = "1"
    req.BankName = "1"
    req.BankAddress = "1"
    req.BankCity = "1"
    req.BankState = "1"
    req.BankZip = "1"
    req.BankCountry = "1"
    req.Iban = "1"
    req.SwiftCode = "1"
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As SetAccountResponse = api.SetAccountDirectDeposit(req)

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
    $req->NameOnAccount = "1";
    $req->BankAccountNumber = "1";
    $req->BankRoutingNumber = "1";
    $req->BankName = "1";
    $req->BankAddress = "1";
    $req->BankCity = "1";
    $req->BankState = "1";
    $req->BankZip = "1";
    $req->BankCountry = "1";
    $req->Iban = "1";
    $req->SwiftCode = "1";
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.SetAccountDirectDeposit($req);

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
    SetAccountDirectDepositRequest req = new SetAccountDirectDepositRequest();

    req.setCustomerID(1);
    req.setNameOnAccount("1");
    req.setBankAccountNumber("1");
    req.setBankRoutingNumber("1");
    req.setBankName("1");
    req.setBankAddress("1");
    req.setBankCity("1");
    req.setBankState("1");
    req.setBankZip("1");
    req.setBankCountry("1");
    req.setIban("1");
    req.setSwiftCode("1");
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    SetAccountResponse res = api.getExigoApiSoap().setAccountDirectDeposit(req, auth);

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

### SetAccountWallet

> Setup primary or secondary wallet account on file for an existing
>  customer, or new customer in a transaction.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Customers |
| REST | `PUT /3.0/account/wallet` |
| SOAP action | `https://api.exigo.com/SetAccountWallet` |
| WSDL elements | `SetAccountWalletRequest` → `SetAccountWalletResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=SetAccountWallet |

#### Input

**`SetAccountWalletRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `WalletAccountType` | `AccountWalletType` | Optional. The customer's wallet slot. Defaults to 0.<br>**Values:** `Primary`, `Secondary`, `Third`, `Fourth`, `Fifth` |
| `WalletType` | `Int32` | The type of wallet account. |
| `WalletAccount` | `String` | The wallet's account number. Leave empty to delete. |
| `WalletOther1` | `String` | Optional. |
| `WalletOther2` | `String` | Optional. |
| `WalletOther3` | `String` | Optional. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`SetAccountResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/account/wallet HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "walletAccountType": null,
  "walletType": 1,
  "walletAccount": "1",
  "walletOther1": "1",
  "walletOther2": "1",
  "walletOther3": "1",
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
SOAPAction: "https://api.exigo.com/SetAccountWallet"

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
    <SetAccountWalletRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <WalletAccountType>Primary or Secondary or Third or Fourth or Fifth</WalletAccountType>
      <WalletType>int</WalletType>
      <WalletAccount>string</WalletAccount>
      <WalletOther1>string</WalletOther1>
      <WalletOther2>string</WalletOther2>
      <WalletOther3>string</WalletOther3>
      <CustomerKey>string</CustomerKey>
    </SetAccountWalletRequest>
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
    <SetAccountWalletResult xmlns="http://api.exigo.com/" />
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
    var req = new SetAccountWalletRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.WalletAccountType = AccountWalletType.Primary;      //The customer's wallet slot.
    req.WalletType = 1;             //The type of wallet account.
    req.WalletAccount = "1";        //The wallet's account number. Leave empty to delete
    req.WalletOther1 = "1";
    req.WalletOther2 = "1";
    req.WalletOther3 = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.SetAccountWalletAsync(req);

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
    SetAccountWalletRequest req = new SetAccountWalletRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.WalletAccountType = AccountWalletType.Primary;      //The customer's wallet slot.
    req.WalletType = 1;             //The type of wallet account.
    req.WalletAccount = "1";        //The wallet's account number. Leave empty to delete
    req.WalletOther1 = "1";
    req.WalletOther2 = "1";
    req.WalletOther3 = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    SetAccountResponse res = api.SetAccountWallet(req);

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
    Dim req as new SetAccountWalletRequest()

    req.CustomerID = 1
    req.WalletAccountType = AccountWalletType.Primary
    req.WalletType = 1
    req.WalletAccount = "1"
    req.WalletOther1 = "1"
    req.WalletOther2 = "1"
    req.WalletOther3 = "1"
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As SetAccountResponse = api.SetAccountWallet(req)

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
    $req->WalletAccountType = 1;
    $req->WalletType = 1;
    $req->WalletAccount = "1";
    $req->WalletOther1 = "1";
    $req->WalletOther2 = "1";
    $req->WalletOther3 = "1";
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.SetAccountWallet($req);

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
    SetAccountWalletRequest req = new SetAccountWalletRequest();

    req.setCustomerID(1);
    req.setWalletAccountType(1);
    req.setWalletType(1);
    req.setWalletAccount("1");
    req.setWalletOther1("1");
    req.setWalletOther2("1");
    req.setWalletOther3("1");
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    SetAccountResponse res = api.getExigoApiSoap().setAccountWallet(req, auth);

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

### SetCustomerSite

> Setup public web site info for an existing customer, or new customer in a transaction.

| | |
|---|---|
| Category | Customers |
| REST | `PUT /3.0/customers/site` |
| SOAP action | `https://api.exigo.com/SetCustomerSite` |
| WSDL elements | `SetCusotmerSiteRequest` → `SetCustomerSiteResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=SetCustomerSite |

#### Input

**`SetCustomerSiteRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `WebAlias` | `String` | The unique name used in a replicated site to identify the customer. |
| `FirstName` | `String` | Optional. |
| `LastName` | `String` | Optional. |
| `Company` | `String` | Optional. |
| `Address1` | `String` | Optional. |
| `Address2` | `String` | Optional. |
| `City` | `String` | Optional. |
| `State` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Zip` | `String` | Optional. |
| `Country` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Email` | `String` | Optional. |
| `Phone` | `String` | Optional. |
| `Phone2` | `String` | Optional. |
| `Fax` | `String` | Optional. |
| `Notes1` | `String` | Optional. |
| `Notes2` | `String` | Optional. |
| `Notes3` | `String` | Optional. |
| `Notes4` | `String` | Optional. |
| `Url1` | `String` | Optional. |
| `Url2` | `String` | Optional. |
| `Url3` | `String` | Optional. |
| `Url4` | `String` | Optional. |
| `Url5` | `String` | Optional. |
| `Url6` | `String` | Optional. |
| `Url7` | `String` | Optional. |
| `Url8` | `String` | Optional. |
| `Url9` | `String` | Optional. |
| `Url10` | `String` | Optional. |
| `Url1Description` | `String` | Optional. |
| `Url2Description` | `String` | Optional. |
| `Url3Description` | `String` | Optional. |
| `Url4Description` | `String` | Optional. |
| `Url5Description` | `String` | Optional. |
| `Url6Description` | `String` | Optional. |
| `Url7Description` | `String` | Optional. |
| `Url8Description` | `String` | Optional. |
| `Url9Description` | `String` | Optional. |
| `Url10Description` | `String` | Optional. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`SetCustomerSiteResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/customers/site HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "webAlias": "1",
  "firstName": "",
  "lastName": "",
  "company": "",
  "address1": "",
  "address2": "",
  "city": "",
  "zip": "",
  "email": "",
  "phone": "",
  "phone2": "",
  "fax": "",
  "notes1": "",
  "notes2": "",
  "notes3": "",
  "notes4": "",
  "url1": "",
  "url2": "",
  "url3": "",
  "url4": "",
  "url5": "",
  "url6": "",
  "url7": "",
  "url8": "",
  "url9": "",
  "url10": "",
  "url1Description": "",
  "url2Description": "",
  "url3Description": "",
  "url4Description": "",
  "url5Description": "",
  "url6Description": "",
  "url7Description": "",
  "url8Description": "",
  "url9Description": "",
  "url10Description": "",
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
SOAPAction: "https://api.exigo.com/SetCustomerSite"

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
    <SetCusotmerSiteRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <WebAlias>string</WebAlias>
      <FirstName>string</FirstName>
      <LastName>string</LastName>
      <Company>string</Company>
      <Address1>string</Address1>
      <Address2>string</Address2>
      <City>string</City>
      <State>string</State>
      <Zip>string</Zip>
      <Country>string</Country>
      <Email>string</Email>
      <Phone>string</Phone>
      <Phone2>string</Phone2>
      <Fax>string</Fax>
      <Notes1>string</Notes1>
      <Notes2>string</Notes2>
      <Notes3>string</Notes3>
      <Notes4>string</Notes4>
      <Url1>string</Url1>
      <Url2>string</Url2>
      <Url3>string</Url3>
      <Url4>string</Url4>
      <Url5>string</Url5>
      <Url6>string</Url6>
      <Url7>string</Url7>
      <Url8>string</Url8>
      <Url9>string</Url9>
      <Url10>string</Url10>
      <Url1Description>string</Url1Description>
      <Url2Description>string</Url2Description>
      <Url3Description>string</Url3Description>
      <Url4Description>string</Url4Description>
      <Url5Description>string</Url5Description>
      <Url6Description>string</Url6Description>
      <Url7Description>string</Url7Description>
      <Url8Description>string</Url8Description>
      <Url9Description>string</Url9Description>
      <Url10Description>string</Url10Description>
      <CustomerKey>string</CustomerKey>
    </SetCusotmerSiteRequest>
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
    <SetCustomerSiteResult xmlns="http://api.exigo.com/" />
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
    var req = new SetCustomerSiteRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.WebAlias = "1";             //The unique name used in a replicated site to identify the customer.
    req.FirstName = "1";
    req.LastName = "1";
    req.Company = "1";
    req.Address1 = "1";
    req.Address2 = "1";
    req.City = "1";
    req.Zip = "1";
    req.Email = "1";
    req.Phone = "1";
    req.Phone2 = "1";
    req.Fax = "1";
    req.Notes1 = "1";
    req.Notes2 = "1";
    req.Notes3 = "1";
    req.Notes4 = "1";
    req.Url1 = "1";
    req.Url2 = "1";
    req.Url3 = "1";
    req.Url4 = "1";
    req.Url5 = "1";
    req.Url6 = "1";
    req.Url7 = "1";
    req.Url8 = "1";
    req.Url9 = "1";
    req.Url10 = "1";
    req.Url1Description = "1";
    req.Url2Description = "1";
    req.Url3Description = "1";
    req.Url4Description = "1";
    req.Url5Description = "1";
    req.Url6Description = "1";
    req.Url7Description = "1";
    req.Url8Description = "1";
    req.Url9Description = "1";
    req.Url10Description = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.SetCustomerSiteAsync(req);

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
    SetCustomerSiteRequest req = new SetCustomerSiteRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.WebAlias = "1";             //The unique name used in a replicated site to identify the customer.
    req.FirstName = "1";
    req.LastName = "1";
    req.Company = "1";
    req.Address1 = "1";
    req.Address2 = "1";
    req.City = "1";
    req.Zip = "1";
    req.Email = "1";
    req.Phone = "1";
    req.Phone2 = "1";
    req.Fax = "1";
    req.Notes1 = "1";
    req.Notes2 = "1";
    req.Notes3 = "1";
    req.Notes4 = "1";
    req.Url1 = "1";
    req.Url2 = "1";
    req.Url3 = "1";
    req.Url4 = "1";
    req.Url5 = "1";
    req.Url6 = "1";
    req.Url7 = "1";
    req.Url8 = "1";
    req.Url9 = "1";
    req.Url10 = "1";
    req.Url1Description = "1";
    req.Url2Description = "1";
    req.Url3Description = "1";
    req.Url4Description = "1";
    req.Url5Description = "1";
    req.Url6Description = "1";
    req.Url7Description = "1";
    req.Url8Description = "1";
    req.Url9Description = "1";
    req.Url10Description = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    SetCustomerSiteResponse res = api.SetCustomerSite(req);

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
    Dim req as new SetCustomerSiteRequest()

    req.CustomerID = 1
    req.WebAlias = "1"
    req.FirstName = "1"
    req.LastName = "1"
    req.Company = "1"
    req.Address1 = "1"
    req.Address2 = "1"
    req.City = "1"
    req.Zip = "1"
    req.Email = "1"
    req.Phone = "1"
    req.Phone2 = "1"
    req.Fax = "1"
    req.Notes1 = "1"
    req.Notes2 = "1"
    req.Notes3 = "1"
    req.Notes4 = "1"
    req.Url1 = "1"
    req.Url2 = "1"
    req.Url3 = "1"
    req.Url4 = "1"
    req.Url5 = "1"
    req.Url6 = "1"
    req.Url7 = "1"
    req.Url8 = "1"
    req.Url9 = "1"
    req.Url10 = "1"
    req.Url1Description = "1"
    req.Url2Description = "1"
    req.Url3Description = "1"
    req.Url4Description = "1"
    req.Url5Description = "1"
    req.Url6Description = "1"
    req.Url7Description = "1"
    req.Url8Description = "1"
    req.Url9Description = "1"
    req.Url10Description = "1"
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As SetCustomerSiteResponse = api.SetCustomerSite(req)

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
    $req->WebAlias = "1";
    $req->FirstName = "1";
    $req->LastName = "1";
    $req->Company = "1";
    $req->Address1 = "1";
    $req->Address2 = "1";
    $req->City = "1";
    $req->Zip = "1";
    $req->Email = "1";
    $req->Phone = "1";
    $req->Phone2 = "1";
    $req->Fax = "1";
    $req->Notes1 = "1";
    $req->Notes2 = "1";
    $req->Notes3 = "1";
    $req->Notes4 = "1";
    $req->Url1 = "1";
    $req->Url2 = "1";
    $req->Url3 = "1";
    $req->Url4 = "1";
    $req->Url5 = "1";
    $req->Url6 = "1";
    $req->Url7 = "1";
    $req->Url8 = "1";
    $req->Url9 = "1";
    $req->Url10 = "1";
    $req->Url1Description = "1";
    $req->Url2Description = "1";
    $req->Url3Description = "1";
    $req->Url4Description = "1";
    $req->Url5Description = "1";
    $req->Url6Description = "1";
    $req->Url7Description = "1";
    $req->Url8Description = "1";
    $req->Url9Description = "1";
    $req->Url10Description = "1";
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.SetCustomerSite($req);

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
    SetCustomerSiteRequest req = new SetCustomerSiteRequest();

    req.setCustomerID(1);
    req.setWebAlias("1");
    req.setFirstName("1");
    req.setLastName("1");
    req.setCompany("1");
    req.setAddress1("1");
    req.setAddress2("1");
    req.setCity("1");
    req.setZip("1");
    req.setEmail("1");
    req.setPhone("1");
    req.setPhone2("1");
    req.setFax("1");
    req.setNotes1("1");
    req.setNotes2("1");
    req.setNotes3("1");
    req.setNotes4("1");
    req.setUrl1("1");
    req.setUrl2("1");
    req.setUrl3("1");
    req.setUrl4("1");
    req.setUrl5("1");
    req.setUrl6("1");
    req.setUrl7("1");
    req.setUrl8("1");
    req.setUrl9("1");
    req.setUrl10("1");
    req.setUrl1Description("1");
    req.setUrl2Description("1");
    req.setUrl3Description("1");
    req.setUrl4Description("1");
    req.setUrl5Description("1");
    req.setUrl6Description("1");
    req.setUrl7Description("1");
    req.setUrl8Description("1");
    req.setUrl9Description("1");
    req.setUrl10Description("1");
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    SetCustomerSiteResponse res = api.getExigoApiSoap().setCustomerSite(req, auth);

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

### SetCustomerSiteImage

> Setup public web site image for an existing customer.

| | |
|---|---|
| Category | Customers |
| REST | `PUT /3.0/customers/site/image` |
| SOAP action | `https://api.exigo.com/SetCustomerSiteImage` |
| WSDL elements | `SetCusotmerSiteImageRequest` → `SetCustomerSiteImageResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=SetCustomerSiteImage |

#### Input

**`SetCustomerSiteImageRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `ImageName` | `String` | The image's file name. |
| `ImageData` | `Byte[]` | The image's data. |
| `CustomerSiteImageType` | `CustomerSiteImageType` | Optional. The desired image slot. Defaults to 0.<br>**Values:** `Primary`, `Secondary` |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`SetCustomerSiteImageResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/customers/site/image HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "imageName": "1",
  "imageData": null,
  "customerSiteImageType": null,
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
SOAPAction: "https://api.exigo.com/SetCustomerSiteImage"

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
    <SetCusotmerSiteImageRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <ImageName>string</ImageName>
      <ImageData>base64Binary</ImageData>
      <CustomerSiteImageType>Primary or Secondary</CustomerSiteImageType>
      <CustomerKey>string</CustomerKey>
    </SetCusotmerSiteImageRequest>
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
    <SetCustomerSiteImageResult xmlns="http://api.exigo.com/" />
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
    var req = new SetCustomerSiteImageRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.ImageName = "1";            //The image's file name

    //Add ImageData
    var imagedata = new List<Byte>();
    imagedata.Add(1);
    imagedata.Add(2);

    //Now attach the list to the request
    req.ImageData = imagedata.ToArray();
    req.CustomerSiteImageType = CustomerSiteImageType.Primary;  //The desired image slot
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.SetCustomerSiteImageAsync(req);

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
    SetCustomerSiteImageRequest req = new SetCustomerSiteImageRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.ImageName = "1";            //The image's file name

    //Add ImageData
    List<Byte> imagedata = new List<Byte>();
    imagedata.Add(1);
    imagedata.Add(2);

    //Now attach the list to the request
    req.ImageData = imagedata.ToArray();
    req.CustomerSiteImageType = CustomerSiteImageType.Primary;  //The desired image slot
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    SetCustomerSiteImageResponse res = api.SetCustomerSiteImage(req);

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
    Dim req as new SetCustomerSiteImageRequest()

    req.CustomerID = 1
    req.ImageName = "1"

    'Add ImageData
    Dim imagedata As New List(Of Byte)()
    imagedata.Add(1)
    imagedata.Add(2)

    'Now attach the list to the request
    req.ImageData = imagedata.ToArray()
    req.CustomerSiteImageType = CustomerSiteImageType.Primary
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As SetCustomerSiteImageResponse = api.SetCustomerSiteImage(req)

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
    $req->ImageName = "1";

    //Add ImageData

    //Now attach the list to the request
    req.ImageData = array(imageDat1,imageDat2);
    $req->CustomerSiteImageType = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.SetCustomerSiteImage($req);

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
    SetCustomerSiteImageRequest req = new SetCustomerSiteImageRequest();

    req.setCustomerID(1);
    req.setImageName("1");

    //Add ImageData
    ArrayOfSystem.Byte imagedata = new ArrayOfSystem.Byte();

    Byte imageDat1 = new Byte();
    imagedata.Add(imageDat1);

    Byte imageDat2 = new Byte();
    imagedata.Add(imageDat2);

    //Now attach the list to the request
    req.setImageData(imagedata);
    req.setCustomerSiteImageType(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    SetCustomerSiteImageResponse res = api.getExigoApiSoap().setCustomerSiteImage(req, auth);

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

### GetCustomers

> Returns one or more customers that match the filter critera passed in.

| | |
|---|---|
| Category | Customers |
| REST | `GET /3.0/customers?customerID=1` |
| SOAP action | `https://api.exigo.com/GetCustomers` |
| WSDL elements | `GetCustomersRequest` → `GetCustomersResult` |
| CSV output | Yes — `GET https://api.exigo.com/3.0/csv/?method=GetCustomers&ApiLoginName=…&ApiPassword=…&ApiCompany=…` |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetCustomers |

#### Input

**`GetCustomersRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Optional. Unique numeric identifier for customer record. Provide value for single record lookups only. |
| `Company` | `String` | Optional. |
| `FirstName` | `String` | Optional. |
| `LastName` | `String` | Optional. |
| `Email` | `String` | Optional. |
| `Phone` | `String` | Optional. |
| `Phone2` | `String` | Optional. |
| `MobilePhone` | `String` | Optional. |
| `Fax` | `String` | Optional. |
| `MainAddress1` | `String` | Optional. |
| `MainAddress2` | `String` | Optional. |
| `MainAddress3` | `String` | Optional. |
| `MainCity` | `String` | Optional. |
| `MainState` | `String` | Optional. |
| `MainZip` | `String` | Optional. |
| `MainCountry` | `String` | Optional. |
| `TaxID` | `String` | Optional. |
| `CustomerTypes` | `Int32[]` | Optional. |
| `CustomerStatuses` | `Int32[]` | Optional. |
| `EnrollerID` | `Int32` | Optional. Unique alpha numeric identifier for customer enroller record. |
| `SponsorID` | `Int32` | Optional. Unique numeric identifier for customer sponsor record. |
| `Field1` | `String` | Optional. |
| `Field10` | `String` | Optional. |
| `Field11` | `String` | Optional. |
| `Field12` | `String` | Optional. |
| `Field13` | `String` | Optional. |
| `Field14` | `String` | Optional. |
| `Field15` | `String` | Optional. |
| `Field2` | `String` | Optional. |
| `Field3` | `String` | Optional. |
| `Field4` | `String` | Optional. |
| `Field5` | `String` | Optional. |
| `Field6` | `String` | Optional. |
| `Field7` | `String` | Optional. |
| `Field8` | `String` | Optional. |
| `Field9` | `String` | Optional. |
| `GreaterThanCustomerID` | `Int32` | Optional. Paging controller. |
| `GreaterThanModifiedDate` | `DateTime` | Optional. Use when pulling changes only. |
| `BatchSize` | `Int32` | Optional. Defaults to 100 at a time. |
| `LoginName` | `String` | Optional. |
| `CreatedDateEnd` | `DateTime` | Optional. |
| `CreatedDateStart` | `DateTime` | Optional. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exception will occur if CustomerID & CustomerKey are provided. |
| `EnrollerKey` | `String` | Optional. Unique alpha numeric identifier for customer enroller record. Exception will occur if EnrollerID & EnrollerKey are provided. |
| `SponsorKey` | `String` | Optional. Unique alpha numeric identifier for customer sponsor record. Exception will occur if SponsorID & SponsorKey are provided. |
| `SalesTaxID` | `String` | Optional. |

#### Output

**`GetCustomersResponse`**

| Property | Type | Notes |
|---|---|---|
| `Customers` | `CustomerResponse[]` |  |
| `RecordCount` | `Int32` |  |

**`CustomerResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| &nbsp;&nbsp;↳ `FirstName` | `String` |  |
| &nbsp;&nbsp;↳ `LastName` | `String` |  |
| &nbsp;&nbsp;↳ `Company` | `String` |  |
| &nbsp;&nbsp;↳ `CustomerType` | `Int32` | Classification of a customer as defined by the company.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `CustomerStatus` | `Int32` | Current status of a customer as defined by the company.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Email` | `String` |  |
| &nbsp;&nbsp;↳ `Phone` | `String` |  |
| &nbsp;&nbsp;↳ `Phone2` | `String` |  |
| &nbsp;&nbsp;↳ `MobilePhone` | `String` |  |
| &nbsp;&nbsp;↳ `Fax` | `String` |  |
| &nbsp;&nbsp;↳ `MainAddress1` | `String` |  |
| &nbsp;&nbsp;↳ `MainAddress2` | `String` |  |
| &nbsp;&nbsp;↳ `MainCity` | `String` |  |
| &nbsp;&nbsp;↳ `MainState` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `MainZip` | `String` |  |
| &nbsp;&nbsp;↳ `MainCountry` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `MainCounty` | `String` |  |
| &nbsp;&nbsp;↳ `MailAddress1` | `String` |  |
| &nbsp;&nbsp;↳ `MailAddress2` | `String` |  |
| &nbsp;&nbsp;↳ `MailCity` | `String` |  |
| &nbsp;&nbsp;↳ `MailState` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `MailZip` | `String` |  |
| &nbsp;&nbsp;↳ `MailCountry` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `MailCounty` | `String` |  |
| &nbsp;&nbsp;↳ `OtherAddress1` | `String` |  |
| &nbsp;&nbsp;↳ `OtherAddress2` | `String` |  |
| &nbsp;&nbsp;↳ `OtherCity` | `String` |  |
| &nbsp;&nbsp;↳ `OtherState` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `OtherZip` | `String` |  |
| &nbsp;&nbsp;↳ `OtherCountry` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `OtherCounty` | `String` |  |
| &nbsp;&nbsp;↳ `LoginName` | `String` |  |
| &nbsp;&nbsp;↳ `EnrollerID` | `Int32` | Unique numeric identifier for customer enroller record. |
| &nbsp;&nbsp;↳ `SponsorID` | `Int32` | Unique numeric identifier for customer sponsor record. |
| &nbsp;&nbsp;↳ `RankID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `BirthDate` | `DateTime` |  |
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
| &nbsp;&nbsp;↳ `CurrencyCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `PayableToName` | `String` |  |
| &nbsp;&nbsp;↳ `DefaultWarehouseID` | `Int32` | Unique location for orders.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `PayableType` | `PayableType` | Deprecated, use PayableTyID instead.<br>**Values:** `Check`, `WireTransfer`, `PaymentCard`, `DirectDeposit`, `OnHold`, `BankWire`, `DebitCardHold`, `Other100` |
| &nbsp;&nbsp;↳ `CheckThreshold` | `Decimal` |  |
| &nbsp;&nbsp;↳ `PriceType` | `Int32` | Controls which price band to use.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `LanguageID` | `Int32` | Customize the web experience by setting this.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Gender` | `Gender` | Obsolete field. Please consider upgrading to GenderID.<br>**Values:** `Unknown`, `Male`, `Female` |
| &nbsp;&nbsp;↳ `SalesTaxID` | `String` |  |
| &nbsp;&nbsp;↳ `VatRegistration` | `String` |  |
| &nbsp;&nbsp;↳ `IsSalesTaxExempt` | `Boolean` |  |
| &nbsp;&nbsp;↳ `IsSubscribedToBroadcasts` | `Boolean` |  |
| &nbsp;&nbsp;↳ `CreatedDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `ModifiedDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `MiddleName` | `String` |  |
| &nbsp;&nbsp;↳ `NameSuffix` | `String` |  |
| &nbsp;&nbsp;↳ `MainAddress3` | `String` |  |
| &nbsp;&nbsp;↳ `MailAddress3` | `String` |  |
| &nbsp;&nbsp;↳ `OtherAddress3` | `String` |  |
| &nbsp;&nbsp;↳ `BinaryPlacementPreference` | `Int32` |  |
| &nbsp;&nbsp;↳ `UseBinaryHoldingTank` | `Boolean` |  |
| &nbsp;&nbsp;↳ `MainAddressVerified` | `Boolean` |  |
| &nbsp;&nbsp;↳ `MailAddressVerified` | `Boolean` |  |
| &nbsp;&nbsp;↳ `OtherAddressVerified` | `Boolean` |  |
| &nbsp;&nbsp;↳ `CustomerKey` | `String` | Unique alpha numeric identifier for customer record . |
| &nbsp;&nbsp;↳ `EnrollerKey` | `String` | Unique alpha numeric identifier for customer enroller record. |
| &nbsp;&nbsp;↳ `SponsorKey` | `String` | Unique alpha numeric identifier for customer sponsor record. |
| &nbsp;&nbsp;↳ `PayableTyID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `CanLogin` | `Boolean` |  |
| &nbsp;&nbsp;↳ `GenderID` | `String` | The customer's gender.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `GenderDescription` | `String` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/customers?customerID=1
  &enrollerID=1
  &sponsorID=1
  &customerKey=1
  &enrollerKey=1
  &sponsorKey=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "customers": null,
  "recordCount": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetCustomers"

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
    <GetCustomersRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <Company>string</Company>
      <FirstName>string</FirstName>
      <LastName>string</LastName>
      <Email>string</Email>
      <Phone>string</Phone>
      <Phone2>string</Phone2>
      <MobilePhone>string</MobilePhone>
      <Fax>string</Fax>
      <MainAddress1>string</MainAddress1>
      <MainAddress2>string</MainAddress2>
      <MainAddress3>string</MainAddress3>
      <MainCity>string</MainCity>
      <MainState>string</MainState>
      <MainZip>string</MainZip>
      <MainCountry>string</MainCountry>
      <TaxID>string</TaxID>
      <CustomerTypes>
        <int>int</int>
      </CustomerTypes>
      <CustomerStatuses>
        <int>int</int>
      </CustomerStatuses>
      <EnrollerID>int</EnrollerID>
      <SponsorID>int</SponsorID>
      <Field1>string</Field1>
      <Field10>string</Field10>
      <Field11>string</Field11>
      <Field12>string</Field12>
      <Field13>string</Field13>
      <Field14>string</Field14>
      <Field15>string</Field15>
      <Field2>string</Field2>
      <Field3>string</Field3>
      <Field4>string</Field4>
      <Field5>string</Field5>
      <Field6>string</Field6>
      <Field7>string</Field7>
      <Field8>string</Field8>
      <Field9>string</Field9>
      <GreaterThanCustomerID>int</GreaterThanCustomerID>
      <GreaterThanModifiedDate>dateTime</GreaterThanModifiedDate>
      <BatchSize>int</BatchSize>
      <LoginName>string</LoginName>
      <CreatedDateEnd>dateTime</CreatedDateEnd>
      <CreatedDateStart>dateTime</CreatedDateStart>
      <CustomerKey>string</CustomerKey>
      <EnrollerKey>string</EnrollerKey>
      <SponsorKey>string</SponsorKey>
      <SalesTaxID>string</SalesTaxID>
    </GetCustomersRequest>
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
    <GetCustomersResult xmlns="http://api.exigo.com/">
      <Customers>
        <CustomerResponse>
          <CustomerID>int</CustomerID>
          <FirstName>string</FirstName>
          <LastName>string</LastName>
          <Company>string</Company>
          <CustomerType>int</CustomerType>
          <CustomerStatus>int</CustomerStatus>
          <Email>string</Email>
          <Phone>string</Phone>
          <Phone2>string</Phone2>
          <MobilePhone>string</MobilePhone>
          <Fax>string</Fax>
          <MainAddress1>string</MainAddress1>
          <MainAddress2>string</MainAddress2>
          <MainCity>string</MainCity>
          <MainState>string</MainState>
          <MainZip>string</MainZip>
          <MainCountry>string</MainCountry>
          <MainCounty>string</MainCounty>
          <MailAddress1>string</MailAddress1>
          <MailAddress2>string</MailAddress2>
          <MailCity>string</MailCity>
          <MailState>string</MailState>
          <MailZip>string</MailZip>
          <MailCountry>string</MailCountry>
          <MailCounty>string</MailCounty>
          <OtherAddress1>string</OtherAddress1>
          <OtherAddress2>string</OtherAddress2>
          <OtherCity>string</OtherCity>
          <OtherState>string</OtherState>
          <OtherZip>string</OtherZip>
          <OtherCountry>string</OtherCountry>
          <OtherCounty>string</OtherCounty>
          <LoginName>string</LoginName>
          <EnrollerID>int</EnrollerID>
          <SponsorID>int</SponsorID>
          <RankID>int</RankID>
          <BirthDate>dateTime</BirthDate>
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
          <CurrencyCode>string</CurrencyCode>
          <PayableToName>string</PayableToName>
          <DefaultWarehouseID>int</DefaultWarehouseID>
          <PayableType>Check or WireTransfer or PaymentCard or DirectDeposit or OnHold or BankWire or DebitCardHold or Other100</PayableType>
          <CheckThreshold>decimal</CheckThreshold>
          <PriceType>int</PriceType>
          <LanguageID>int</LanguageID>
          <Gender>Unknown or Male or Female</Gender>
          <SalesTaxID>string</SalesTaxID>
          <VatRegistration>string</VatRegistration>
          <IsSalesTaxExempt>boolean</IsSalesTaxExempt>
          <IsSubscribedToBroadcasts>boolean</IsSubscribedToBroadcasts>
          <CreatedDate>dateTime</CreatedDate>
          <ModifiedDate>dateTime</ModifiedDate>
          <MiddleName>string</MiddleName>
          <NameSuffix>string</NameSuffix>
          <MainAddress3>string</MainAddress3>
          <MailAddress3>string</MailAddress3>
          <OtherAddress3>string</OtherAddress3>
          <BinaryPlacementPreference>int</BinaryPlacementPreference>
          <UseBinaryHoldingTank>boolean</UseBinaryHoldingTank>
          <MainAddressVerified>boolean</MainAddressVerified>
          <MailAddressVerified>boolean</MailAddressVerified>
          <OtherAddressVerified>boolean</OtherAddressVerified>
          <CustomerKey>string</CustomerKey>
          <EnrollerKey>string</EnrollerKey>
          <SponsorKey>string</SponsorKey>
          <PayableTyID>int</PayableTyID>
          <CanLogin>boolean</CanLogin>
          <GenderID>string</GenderID>
          <GenderDescription>string</GenderDescription>
        </CustomerResponse>
      </Customers>
      <RecordCount>int</RecordCount>
    </GetCustomersResult>
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
    var req = new GetCustomersRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record. Provide value for single record lookups only.
    req.EnrollerID = 1;             //Unique alpha numeric identifier for customer enroller record.
    req.SponsorID = 1;              //Unique numeric identifier for customer sponsor record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exception will occur if CustomerID & CustomerKey are provided.
    req.EnrollerKey = "1";          //Unique alpha numeric identifier for customer enroller record. Exception will occur if EnrollerID & EnrollerKey are provided.
    req.SponsorKey = "1";           //Unique alpha numeric identifier for customer sponsor record. Exception will occur if SponsorID & SponsorKey are provided.

    //Send Request to Server and Get Response
    var res = await api.GetCustomersAsync(req);

    //Now examine the results:

    foreach (var customer  in res.Customers)
    {
        Console.WriteLine("CustomerID: {0}", customer.CustomerID);
        Console.WriteLine("FirstName: {0}", customer.FirstName);
        Console.WriteLine("LastName: {0}", customer.LastName);
        Console.WriteLine("Company: {0}", customer.Company);
        Console.WriteLine("CustomerType: {0}", customer.CustomerType);
        Console.WriteLine("CustomerStatus: {0}", customer.CustomerStatus);
        Console.WriteLine("Email: {0}", customer.Email);
        Console.WriteLine("Phone: {0}", customer.Phone);
        Console.WriteLine("Phone2: {0}", customer.Phone2);
        Console.WriteLine("MobilePhone: {0}", customer.MobilePhone);
        Console.WriteLine("Fax: {0}", customer.Fax);
        Console.WriteLine("MainAddress1: {0}", customer.MainAddress1);
        Console.WriteLine("MainAddress2: {0}", customer.MainAddress2);
        Console.WriteLine("MainCity: {0}", customer.MainCity);
        Console.WriteLine("MainState: {0}", customer.MainState);
        Console.WriteLine("MainZip: {0}", customer.MainZip);
        Console.WriteLine("MainCountry: {0}", customer.MainCountry);
        Console.WriteLine("MainCounty: {0}", customer.MainCounty);
        Console.WriteLine("MailAddress1: {0}", customer.MailAddress1);
        Console.WriteLine("MailAddress2: {0}", customer.MailAddress2);
        Console.WriteLine("MailCity: {0}", customer.MailCity);
        Console.WriteLine("MailZip: {0}", customer.MailZip);
        Console.WriteLine("MailCounty: {0}", customer.MailCounty);
        Console.WriteLine("OtherAddress1: {0}", customer.OtherAddress1);
        Console.WriteLine("OtherAddress2: {0}", customer.OtherAddress2);
        Console.WriteLine("OtherCity: {0}", customer.OtherCity);
        Console.WriteLine("OtherZip: {0}", customer.OtherZip);
        Console.WriteLine("OtherCounty: {0}", customer.OtherCounty);
        Console.WriteLine("LoginName: {0}", customer.LoginName);
        Console.WriteLine("EnrollerID: {0}", customer.EnrollerID);
        Console.WriteLine("SponsorID: {0}", customer.SponsorID);
        Console.WriteLine("RankID: {0}", customer.RankID);
        Console.WriteLine("BirthDate: {0}", customer.BirthDate);
        Console.WriteLine("Date1: {0}", customer.Date1);
        Console.WriteLine("Date2: {0}", customer.Date2);
        Console.WriteLine("Date3: {0}", customer.Date3);
        Console.WriteLine("Date4: {0}", customer.Date4);
        Console.WriteLine("Date5: {0}", customer.Date5);
        Console.WriteLine("CurrencyCode: {0}", customer.CurrencyCode);
        Console.WriteLine("PayableToName: {0}", customer.PayableToName);
        Console.WriteLine("DefaultWarehouseID: {0}", customer.DefaultWarehouseID);
        Console.WriteLine("CheckThreshold: {0}", customer.CheckThreshold);
        Console.WriteLine("PriceType: {0}", customer.PriceType);
        Console.WriteLine("SalesTaxID: {0}", customer.SalesTaxID);
        Console.WriteLine("VatRegistration: {0}", customer.VatRegistration);
        Console.WriteLine("IsSalesTaxExempt: {0}", customer.IsSalesTaxExempt);
        Console.WriteLine("IsSubscribedToBroadcasts: {0}", customer.IsSubscribedToBroadcasts);
        Console.WriteLine("CreatedDate: {0}", customer.CreatedDate);
        Console.WriteLine("ModifiedDate: {0}", customer.ModifiedDate);
        Console.WriteLine("MiddleName: {0}", customer.MiddleName);
        Console.WriteLine("NameSuffix: {0}", customer.NameSuffix);
        Console.WriteLine("MainAddress3: {0}", customer.MainAddress3);
        Console.WriteLine("MailAddress3: {0}", customer.MailAddress3);
        Console.WriteLine("OtherAddress3: {0}", customer.OtherAddress3);
        Console.WriteLine("BinaryPlacementPreference: {0}", customer.BinaryPlacementPreference);
        Console.WriteLine("UseBinaryHoldingTank: {0}", customer.UseBinaryHoldingTank);
        Console.WriteLine("MainAddressVerified: {0}", customer.MainAddressVerified);
        Console.WriteLine("MailAddressVerified: {0}", customer.MailAddressVerified);
        Console.WriteLine("OtherAddressVerified: {0}", customer.OtherAddressVerified);
        Console.WriteLine("CustomerKey: {0}", customer.CustomerKey);
        Console.WriteLine("EnrollerKey: {0}", customer.EnrollerKey);
        Console.WriteLine("SponsorKey: {0}", customer.SponsorKey);
        Console.WriteLine("PayableTyID: {0}", customer.PayableTyID);
        Console.WriteLine("CanLogin: {0}", customer.CanLogin);
        Console.WriteLine("GenderDescription: {0}", customer.GenderDescription);
    }
    Console.WriteLine("RecordCount: {0}", res.RecordCount);
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
    GetCustomersRequest req = new GetCustomersRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record. Provide value for single record lookups only.
    req.EnrollerID = 1;             //Unique alpha numeric identifier for customer enroller record.
    req.SponsorID = 1;              //Unique numeric identifier for customer sponsor record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exception will occur if CustomerID & CustomerKey are provided.
    req.EnrollerKey = "1";          //Unique alpha numeric identifier for customer enroller record. Exception will occur if EnrollerID & EnrollerKey are provided.
    req.SponsorKey = "1";           //Unique alpha numeric identifier for customer sponsor record. Exception will occur if SponsorID & SponsorKey are provided.

    //Send Request to Server and Get Response
    GetCustomersResponse res = api.GetCustomers(req);

    //Now examine the results:

    foreach (CustomerResponse customer  in res.Customers)
    {
        Console.WriteLine("CustomerID: {0}", customer.CustomerID);
        Console.WriteLine("FirstName: {0}", customer.FirstName);
        Console.WriteLine("LastName: {0}", customer.LastName);
        Console.WriteLine("Company: {0}", customer.Company);
        Console.WriteLine("CustomerType: {0}", customer.CustomerType);
        Console.WriteLine("CustomerStatus: {0}", customer.CustomerStatus);
        Console.WriteLine("Email: {0}", customer.Email);
        Console.WriteLine("Phone: {0}", customer.Phone);
        Console.WriteLine("Phone2: {0}", customer.Phone2);
        Console.WriteLine("MobilePhone: {0}", customer.MobilePhone);
        Console.WriteLine("Fax: {0}", customer.Fax);
        Console.WriteLine("MainAddress1: {0}", customer.MainAddress1);
        Console.WriteLine("MainAddress2: {0}", customer.MainAddress2);
        Console.WriteLine("MainCity: {0}", customer.MainCity);
        Console.WriteLine("MainState: {0}", customer.MainState);
        Console.WriteLine("MainZip: {0}", customer.MainZip);
        Console.WriteLine("MainCountry: {0}", customer.MainCountry);
        Console.WriteLine("MainCounty: {0}", customer.MainCounty);
        Console.WriteLine("MailAddress1: {0}", customer.MailAddress1);
        Console.WriteLine("MailAddress2: {0}", customer.MailAddress2);
        Console.WriteLine("MailCity: {0}", customer.MailCity);
        Console.WriteLine("MailZip: {0}", customer.MailZip);
        Console.WriteLine("MailCounty: {0}", customer.MailCounty);
        Console.WriteLine("OtherAddress1: {0}", customer.OtherAddress1);
        Console.WriteLine("OtherAddress2: {0}", customer.OtherAddress2);
        Console.WriteLine("OtherCity: {0}", customer.OtherCity);
        Console.WriteLine("OtherZip: {0}", customer.OtherZip);
        Console.WriteLine("OtherCounty: {0}", customer.OtherCounty);
        Console.WriteLine("LoginName: {0}", customer.LoginName);
        Console.WriteLine("EnrollerID: {0}", customer.EnrollerID);
        Console.WriteLine("SponsorID: {0}", customer.SponsorID);
        Console.WriteLine("RankID: {0}", customer.RankID);
        Console.WriteLine("BirthDate: {0}", customer.BirthDate);
        Console.WriteLine("Date1: {0}", customer.Date1);
        Console.WriteLine("Date2: {0}", customer.Date2);
        Console.WriteLine("Date3: {0}", customer.Date3);
        Console.WriteLine("Date4: {0}", customer.Date4);
        Console.WriteLine("Date5: {0}", customer.Date5);
        Console.WriteLine("CurrencyCode: {0}", customer.CurrencyCode);
        Console.WriteLine("PayableToName: {0}", customer.PayableToName);
        Console.WriteLine("DefaultWarehouseID: {0}", customer.DefaultWarehouseID);
        Console.WriteLine("CheckThreshold: {0}", customer.CheckThreshold);
        Console.WriteLine("PriceType: {0}", customer.PriceType);
        Console.WriteLine("SalesTaxID: {0}", customer.SalesTaxID);
        Console.WriteLine("VatRegistration: {0}", customer.VatRegistration);
        Console.WriteLine("IsSalesTaxExempt: {0}", customer.IsSalesTaxExempt);
        Console.WriteLine("IsSubscribedToBroadcasts: {0}", customer.IsSubscribedToBroadcasts);
        Console.WriteLine("CreatedDate: {0}", customer.CreatedDate);
        Console.WriteLine("ModifiedDate: {0}", customer.ModifiedDate);
        Console.WriteLine("MiddleName: {0}", customer.MiddleName);
        Console.WriteLine("NameSuffix: {0}", customer.NameSuffix);
        Console.WriteLine("MainAddress3: {0}", customer.MainAddress3);
        Console.WriteLine("MailAddress3: {0}", customer.MailAddress3);
        Console.WriteLine("OtherAddress3: {0}", customer.OtherAddress3);
        Console.WriteLine("BinaryPlacementPreference: {0}", customer.BinaryPlacementPreference);
        Console.WriteLine("UseBinaryHoldingTank: {0}", customer.UseBinaryHoldingTank);
        Console.WriteLine("MainAddressVerified: {0}", customer.MainAddressVerified);
        Console.WriteLine("MailAddressVerified: {0}", customer.MailAddressVerified);
        Console.WriteLine("OtherAddressVerified: {0}", customer.OtherAddressVerified);
        Console.WriteLine("CustomerKey: {0}", customer.CustomerKey);
        Console.WriteLine("EnrollerKey: {0}", customer.EnrollerKey);
        Console.WriteLine("SponsorKey: {0}", customer.SponsorKey);
        Console.WriteLine("PayableTyID: {0}", customer.PayableTyID);
        Console.WriteLine("CanLogin: {0}", customer.CanLogin);
        Console.WriteLine("GenderDescription: {0}", customer.GenderDescription);
    }
    Console.WriteLine("RecordCount: {0}", res.RecordCount);
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
    Dim req as new GetCustomersRequest()

    req.CustomerID = 1
    req.EnrollerID = 1
    req.SponsorID = 1
    req.CustomerKey = "1"
    req.EnrollerKey = "1"
    req.SponsorKey = "1"

    'Send Request to Server and Get Response
    Dim res As GetCustomersResponse = api.GetCustomers(req)

    'Now examine the results:

    For Each customer As CustomerResponse In res.Customers
        Console.WriteLine("CustomerID: {0}", customer.CustomerID)
        Console.WriteLine("FirstName: {0}", customer.FirstName)
        Console.WriteLine("LastName: {0}", customer.LastName)
        Console.WriteLine("Company: {0}", customer.Company)
        Console.WriteLine("CustomerType: {0}", customer.CustomerType)
        Console.WriteLine("CustomerStatus: {0}", customer.CustomerStatus)
        Console.WriteLine("Email: {0}", customer.Email)
        Console.WriteLine("Phone: {0}", customer.Phone)
        Console.WriteLine("Phone2: {0}", customer.Phone2)
        Console.WriteLine("MobilePhone: {0}", customer.MobilePhone)
        Console.WriteLine("Fax: {0}", customer.Fax)
        Console.WriteLine("MainAddress1: {0}", customer.MainAddress1)
        Console.WriteLine("MainAddress2: {0}", customer.MainAddress2)
        Console.WriteLine("MainCity: {0}", customer.MainCity)
        Console.WriteLine("MainState: {0}", customer.MainState)
        Console.WriteLine("MainZip: {0}", customer.MainZip)
        Console.WriteLine("MainCountry: {0}", customer.MainCountry)
        Console.WriteLine("MainCounty: {0}", customer.MainCounty)
        Console.WriteLine("MailAddress1: {0}", customer.MailAddress1)
        Console.WriteLine("MailAddress2: {0}", customer.MailAddress2)
        Console.WriteLine("MailCity: {0}", customer.MailCity)
        Console.WriteLine("MailZip: {0}", customer.MailZip)
        Console.WriteLine("MailCounty: {0}", customer.MailCounty)
        Console.WriteLine("OtherAddress1: {0}", customer.OtherAddress1)
        Console.WriteLine("OtherAddress2: {0}", customer.OtherAddress2)
        Console.WriteLine("OtherCity: {0}", customer.OtherCity)
        Console.WriteLine("OtherZip: {0}", customer.OtherZip)
        Console.WriteLine("OtherCounty: {0}", customer.OtherCounty)
        Console.WriteLine("LoginName: {0}", customer.LoginName)
        Console.WriteLine("EnrollerID: {0}", customer.EnrollerID)
        Console.WriteLine("SponsorID: {0}", customer.SponsorID)
        Console.WriteLine("RankID: {0}", customer.RankID)
        Console.WriteLine("BirthDate: {0}", customer.BirthDate)
        Console.WriteLine("Date1: {0}", customer.Date1)
        Console.WriteLine("Date2: {0}", customer.Date2)
        Console.WriteLine("Date3: {0}", customer.Date3)
        Console.WriteLine("Date4: {0}", customer.Date4)
        Console.WriteLine("Date5: {0}", customer.Date5)
        Console.WriteLine("CurrencyCode: {0}", customer.CurrencyCode)
        Console.WriteLine("PayableToName: {0}", customer.PayableToName)
        Console.WriteLine("DefaultWarehouseID: {0}", customer.DefaultWarehouseID)
        Console.WriteLine("CheckThreshold: {0}", customer.CheckThreshold)
        Console.WriteLine("PriceType: {0}", customer.PriceType)
        Console.WriteLine("SalesTaxID: {0}", customer.SalesTaxID)
        Console.WriteLine("VatRegistration: {0}", customer.VatRegistration)
        Console.WriteLine("IsSalesTaxExempt: {0}", customer.IsSalesTaxExempt)
        Console.WriteLine("IsSubscribedToBroadcasts: {0}", customer.IsSubscribedToBroadcasts)
        Console.WriteLine("CreatedDate: {0}", customer.CreatedDate)
        Console.WriteLine("ModifiedDate: {0}", customer.ModifiedDate)
        Console.WriteLine("MiddleName: {0}", customer.MiddleName)
        Console.WriteLine("NameSuffix: {0}", customer.NameSuffix)
        Console.WriteLine("MainAddress3: {0}", customer.MainAddress3)
        Console.WriteLine("MailAddress3: {0}", customer.MailAddress3)
        Console.WriteLine("OtherAddress3: {0}", customer.OtherAddress3)
        Console.WriteLine("BinaryPlacementPreference: {0}", customer.BinaryPlacementPreference)
        Console.WriteLine("UseBinaryHoldingTank: {0}", customer.UseBinaryHoldingTank)
        Console.WriteLine("MainAddressVerified: {0}", customer.MainAddressVerified)
        Console.WriteLine("MailAddressVerified: {0}", customer.MailAddressVerified)
        Console.WriteLine("OtherAddressVerified: {0}", customer.OtherAddressVerified)
        Console.WriteLine("CustomerKey: {0}", customer.CustomerKey)
        Console.WriteLine("EnrollerKey: {0}", customer.EnrollerKey)
        Console.WriteLine("SponsorKey: {0}", customer.SponsorKey)
        Console.WriteLine("PayableTyID: {0}", customer.PayableTyID)
        Console.WriteLine("CanLogin: {0}", customer.CanLogin)
        Console.WriteLine("GenderDescription: {0}", customer.GenderDescription)
    Next
    Console.WriteLine("RecordCount: {0}", res.RecordCount)
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
    $req->EnrollerID = 1;
    $req->SponsorID = 1;
    $req->CustomerKey = "1";
    $req->EnrollerKey = "1";
    $req->SponsorKey = "1";

    //Send Request to Server and Get Response
    $res = $api.GetCustomers($req);

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
    GetCustomersRequest req = new GetCustomersRequest();

    req.setCustomerID(1);
    req.setEnrollerID(1);
    req.setSponsorID(1);
    req.setCustomerKey("1");
    req.setEnrollerKey("1");
    req.setSponsorKey("1");

    //Send Request to Server and Get Response
    GetCustomersResponse res = api.getExigoApiSoap().getCustomers(req, auth);

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
https://api.exigo.com/3.0/csv/?method=GetCustomers
&ApiLoginName=String
&ApiPassword=String
&ApiCompany=String
&CustomerID=Nullable`1
&Company=String
&FirstName=String
&LastName=String
&Email=String
&Phone=String
&Phone2=String
&MobilePhone=String
&Fax=String
&MainAddress1=String
&MainAddress2=String
&MainAddress3=String
&MainCity=String
&MainState=String
&MainZip=String
&MainCountry=String
&TaxID=String
&CustomerTypes=Int32[]
&CustomerStatuses=Int32[]
&EnrollerID=Nullable`1
&SponsorID=Nullable`1
&Field1=String
&Field10=String
&Field11=String
&Field12=String
&Field13=String
&Field14=String
&Field15=String
&Field2=String
&Field3=String
&Field4=String
&Field5=String
&Field6=String
&Field7=String
&Field8=String
&Field9=String
&GreaterThanCustomerID=Nullable`1
&GreaterThanModifiedDate=Nullable`1
&BatchSize=Nullable`1
&LoginName=String
&CreatedDateEnd=Nullable`1
&CreatedDateStart=Nullable`1
&CustomerKey=String
&EnrollerKey=String
&SponsorKey=String
&SalesTaxID=String
Response FieldsCustomerID,FirstName,LastName,Company,CustomerType,CustomerStatus,Email,Phone,Phone2,MobilePhone,Fax,MainAddress1,MainAddress2,MainCity,MainState,MainZip,MainCountry,MainCounty,MailAddress1,MailAddress2,MailCity,MailState,MailZip,MailCountry,MailCounty,OtherAddress1,OtherAddress2,OtherCity,OtherState,OtherZip,OtherCountry,OtherCounty,LoginName,EnrollerID,SponsorID,RankID,BirthDate,Field1,Field2,Field3,Field4,Field5,Field6,Field7,Field8,Field9,Field10,Field11,Field12,Field13,Field14,Field15,Date1,Date2,Date3,Date4,Date5,CurrencyCode,PayableToName,DefaultWarehouseID,PayableType,CheckThreshold,PriceType,LanguageID,Gender,SalesTaxID,VatRegistration,IsSalesTaxExempt,IsSubscribedToBroadcasts,CreatedDate,ModifiedDate,MiddleName,NameSuffix,MainAddress3,MailAddress3,OtherAddress3,BinaryPlacementPreference,UseBinaryHoldingTank,MainAddressVerified,MailAddressVerified,OtherAddressVerified,CustomerKey,EnrollerKey,SponsorKey,PayableTyID,CanLogin,GenderID,GenderDescription,RecordCount
Int32,String,String,String,Int32,Int32,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,Int32,Int32,Int32,DateTime,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,Nullable`1,Nullable`1,Nullable`1,Nullable`1,Nullable`1,String,String,Int32,PayableType,Decimal,Int32,Int32,Gender,String,String,Boolean,Boolean,DateTime,DateTime,String,String,String,String,String,Int32,Boolean,Boolean,Boolean,Boolean,String,String,String,Int32,Boolean,String,String,Int32

                    © 2026 Exigo.
```

</details>

---

### GetCustomerSite

> Returns the public web site info setup for a customer. Pass in CustomerID or WebAlias. If the customer's type has enabled Create Web Info and a record does not exist a customer site record will be created.

| | |
|---|---|
| Category | Customers |
| REST | `GET /3.0/customers/site?webAlias=1` |
| SOAP action | `https://api.exigo.com/GetCustomerSite` |
| WSDL elements | `GetCustomerSiteRequest` → `GetCustomerSiteResult` |
| CSV output | Yes — `GET https://api.exigo.com/3.0/csv/?method=GetCustomerSite&ApiLoginName=…&ApiPassword=…&ApiCompany=…` |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetCustomerSite |

#### Input

**`GetCustomerSiteRequest`**

| Property | Type | Notes |
|---|---|---|
| `WebAlias` | `String` | Optional. |
| `CustomerID` | `Int32` | Optional. Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`GetCustomerSiteResponse`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `WebAlias` | `String` |  |
| `FirstName` | `String` |  |
| `LastName` | `String` |  |
| `Company` | `String` |  |
| `Address1` | `String` |  |
| `Address2` | `String` |  |
| `City` | `String` |  |
| `State` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| `Zip` | `String` |  |
| `Country` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| `Email` | `String` |  |
| `Phone` | `String` |  |
| `Phone2` | `String` |  |
| `Fax` | `String` |  |
| `Notes1` | `String` |  |
| `Notes2` | `String` |  |
| `Notes3` | `String` |  |
| `Notes4` | `String` |  |
| `Url1` | `String` |  |
| `Url2` | `String` |  |
| `Url3` | `String` |  |
| `Url4` | `String` |  |
| `Url5` | `String` |  |
| `Url6` | `String` |  |
| `Url7` | `String` |  |
| `Url8` | `String` |  |
| `Url9` | `String` |  |
| `Url10` | `String` |  |
| `Url1Description` | `String` |  |
| `Url2Description` | `String` |  |
| `Url3Description` | `String` |  |
| `Url4Description` | `String` |  |
| `Url5Description` | `String` |  |
| `Url6Description` | `String` |  |
| `Url7Description` | `String` |  |
| `Url8Description` | `String` |  |
| `Url9Description` | `String` |  |
| `Url10Description` | `String` |  |
| `Image1` | `String` |  |
| `Image2` | `String` |  |
| `ImageUrl1` | `String` | Deprecated, there is no support for this field. |
| `ImageUrl2` | `String` | Deprecated, there is no support for this field. |
| `CustomerKey` | `String` | Unique alpha numeric identifier for customer record . |
| `DataImage1` | `Byte[]` |  |
| `DataImage2` | `Byte[]` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/customers/site?webAlias=1
  &customerID=1
  &customerKey=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "customerID": 1,
  "webAlias": "",
  "firstName": "",
  "lastName": "",
  "company": "",
  "address1": "",
  "address2": "",
  "city": "",
  "state": "",
  "zip": "",
  "country": "",
  "email": "",
  "phone": "",
  "phone2": "",
  "fax": "",
  "notes1": "",
  "notes2": "",
  "notes3": "",
  "notes4": "",
  "url1": "",
  "url2": "",
  "url3": "",
  "url4": "",
  "url5": "",
  "url6": "",
  "url7": "",
  "url8": "",
  "url9": "",
  "url10": "",
  "url1Description": "",
  "url2Description": "",
  "url3Description": "",
  "url4Description": "",
  "url5Description": "",
  "url6Description": "",
  "url7Description": "",
  "url8Description": "",
  "url9Description": "",
  "url10Description": "",
  "image1": "",
  "image2": "",
  "imageUrl1": "",
  "imageUrl2": "",
  "customerKey": "",
  "dataImage1": null,
  "dataImage2": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetCustomerSite"

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
    <GetCustomerSiteRequest xmlns="http://api.exigo.com/">
      <WebAlias>string</WebAlias>
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
    </GetCustomerSiteRequest>
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
    <GetCustomerSiteResult xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <WebAlias>string</WebAlias>
      <FirstName>string</FirstName>
      <LastName>string</LastName>
      <Company>string</Company>
      <Address1>string</Address1>
      <Address2>string</Address2>
      <City>string</City>
      <State>string</State>
      <Zip>string</Zip>
      <Country>string</Country>
      <Email>string</Email>
      <Phone>string</Phone>
      <Phone2>string</Phone2>
      <Fax>string</Fax>
      <Notes1>string</Notes1>
      <Notes2>string</Notes2>
      <Notes3>string</Notes3>
      <Notes4>string</Notes4>
      <Url1>string</Url1>
      <Url2>string</Url2>
      <Url3>string</Url3>
      <Url4>string</Url4>
      <Url5>string</Url5>
      <Url6>string</Url6>
      <Url7>string</Url7>
      <Url8>string</Url8>
      <Url9>string</Url9>
      <Url10>string</Url10>
      <Url1Description>string</Url1Description>
      <Url2Description>string</Url2Description>
      <Url3Description>string</Url3Description>
      <Url4Description>string</Url4Description>
      <Url5Description>string</Url5Description>
      <Url6Description>string</Url6Description>
      <Url7Description>string</Url7Description>
      <Url8Description>string</Url8Description>
      <Url9Description>string</Url9Description>
      <Url10Description>string</Url10Description>
      <Image1>string</Image1>
      <Image2>string</Image2>
      <ImageUrl1>string</ImageUrl1>
      <ImageUrl2>string</ImageUrl2>
      <CustomerKey>string</CustomerKey>
      <DataImage1>base64Binary</DataImage1>
      <DataImage2>base64Binary</DataImage2>
    </GetCustomerSiteResult>
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
    var req = new GetCustomerSiteRequest();

    req.WebAlias = "1";
    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.GetCustomerSiteAsync(req);

    //Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID);
    Console.WriteLine("WebAlias: {0}", res.WebAlias);
    Console.WriteLine("FirstName: {0}", res.FirstName);
    Console.WriteLine("LastName: {0}", res.LastName);
    Console.WriteLine("Company: {0}", res.Company);
    Console.WriteLine("Address1: {0}", res.Address1);
    Console.WriteLine("Address2: {0}", res.Address2);
    Console.WriteLine("City: {0}", res.City);
    Console.WriteLine("Zip: {0}", res.Zip);
    Console.WriteLine("Email: {0}", res.Email);
    Console.WriteLine("Phone: {0}", res.Phone);
    Console.WriteLine("Phone2: {0}", res.Phone2);
    Console.WriteLine("Fax: {0}", res.Fax);
    Console.WriteLine("Notes1: {0}", res.Notes1);
    Console.WriteLine("Notes2: {0}", res.Notes2);
    Console.WriteLine("Notes3: {0}", res.Notes3);
    Console.WriteLine("Notes4: {0}", res.Notes4);
    Console.WriteLine("Url1: {0}", res.Url1);
    Console.WriteLine("Url2: {0}", res.Url2);
    Console.WriteLine("Url3: {0}", res.Url3);
    Console.WriteLine("Url4: {0}", res.Url4);
    Console.WriteLine("Url5: {0}", res.Url5);
    Console.WriteLine("Url6: {0}", res.Url6);
    Console.WriteLine("Url7: {0}", res.Url7);
    Console.WriteLine("Url8: {0}", res.Url8);
    Console.WriteLine("Url9: {0}", res.Url9);
    Console.WriteLine("Url10: {0}", res.Url10);
    Console.WriteLine("Url1Description: {0}", res.Url1Description);
    Console.WriteLine("Url2Description: {0}", res.Url2Description);
    Console.WriteLine("Url3Description: {0}", res.Url3Description);
    Console.WriteLine("Url4Description: {0}", res.Url4Description);
    Console.WriteLine("Url5Description: {0}", res.Url5Description);
    Console.WriteLine("Url6Description: {0}", res.Url6Description);
    Console.WriteLine("Url7Description: {0}", res.Url7Description);
    Console.WriteLine("Url8Description: {0}", res.Url8Description);
    Console.WriteLine("Url9Description: {0}", res.Url9Description);
    Console.WriteLine("Url10Description: {0}", res.Url10Description);
    Console.WriteLine("Image1: {0}", res.Image1);
    Console.WriteLine("Image2: {0}", res.Image2);
    Console.WriteLine("ImageUrl1: {0}", res.ImageUrl1);
    Console.WriteLine("ImageUrl2: {0}", res.ImageUrl2);
    Console.WriteLine("CustomerKey: {0}", res.CustomerKey);

    foreach (var byte  in res.DataImage1)
    {
    }

    foreach (var byte  in res.DataImage2)
    {
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
    GetCustomerSiteRequest req = new GetCustomerSiteRequest();

    req.WebAlias = "1";
    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    GetCustomerSiteResponse res = api.GetCustomerSite(req);

    //Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID);
    Console.WriteLine("WebAlias: {0}", res.WebAlias);
    Console.WriteLine("FirstName: {0}", res.FirstName);
    Console.WriteLine("LastName: {0}", res.LastName);
    Console.WriteLine("Company: {0}", res.Company);
    Console.WriteLine("Address1: {0}", res.Address1);
    Console.WriteLine("Address2: {0}", res.Address2);
    Console.WriteLine("City: {0}", res.City);
    Console.WriteLine("Zip: {0}", res.Zip);
    Console.WriteLine("Email: {0}", res.Email);
    Console.WriteLine("Phone: {0}", res.Phone);
    Console.WriteLine("Phone2: {0}", res.Phone2);
    Console.WriteLine("Fax: {0}", res.Fax);
    Console.WriteLine("Notes1: {0}", res.Notes1);
    Console.WriteLine("Notes2: {0}", res.Notes2);
    Console.WriteLine("Notes3: {0}", res.Notes3);
    Console.WriteLine("Notes4: {0}", res.Notes4);
    Console.WriteLine("Url1: {0}", res.Url1);
    Console.WriteLine("Url2: {0}", res.Url2);
    Console.WriteLine("Url3: {0}", res.Url3);
    Console.WriteLine("Url4: {0}", res.Url4);
    Console.WriteLine("Url5: {0}", res.Url5);
    Console.WriteLine("Url6: {0}", res.Url6);
    Console.WriteLine("Url7: {0}", res.Url7);
    Console.WriteLine("Url8: {0}", res.Url8);
    Console.WriteLine("Url9: {0}", res.Url9);
    Console.WriteLine("Url10: {0}", res.Url10);
    Console.WriteLine("Url1Description: {0}", res.Url1Description);
    Console.WriteLine("Url2Description: {0}", res.Url2Description);
    Console.WriteLine("Url3Description: {0}", res.Url3Description);
    Console.WriteLine("Url4Description: {0}", res.Url4Description);
    Console.WriteLine("Url5Description: {0}", res.Url5Description);
    Console.WriteLine("Url6Description: {0}", res.Url6Description);
    Console.WriteLine("Url7Description: {0}", res.Url7Description);
    Console.WriteLine("Url8Description: {0}", res.Url8Description);
    Console.WriteLine("Url9Description: {0}", res.Url9Description);
    Console.WriteLine("Url10Description: {0}", res.Url10Description);
    Console.WriteLine("Image1: {0}", res.Image1);
    Console.WriteLine("Image2: {0}", res.Image2);
    Console.WriteLine("ImageUrl1: {0}", res.ImageUrl1);
    Console.WriteLine("ImageUrl2: {0}", res.ImageUrl2);
    Console.WriteLine("CustomerKey: {0}", res.CustomerKey);

    foreach (Byte byte  in res.DataImage1)
    {
    }

    foreach (Byte byte  in res.DataImage2)
    {
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
    Dim req as new GetCustomerSiteRequest()

    req.WebAlias = "1"
    req.CustomerID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As GetCustomerSiteResponse = api.GetCustomerSite(req)

    'Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID)
    Console.WriteLine("WebAlias: {0}", res.WebAlias)
    Console.WriteLine("FirstName: {0}", res.FirstName)
    Console.WriteLine("LastName: {0}", res.LastName)
    Console.WriteLine("Company: {0}", res.Company)
    Console.WriteLine("Address1: {0}", res.Address1)
    Console.WriteLine("Address2: {0}", res.Address2)
    Console.WriteLine("City: {0}", res.City)
    Console.WriteLine("Zip: {0}", res.Zip)
    Console.WriteLine("Email: {0}", res.Email)
    Console.WriteLine("Phone: {0}", res.Phone)
    Console.WriteLine("Phone2: {0}", res.Phone2)
    Console.WriteLine("Fax: {0}", res.Fax)
    Console.WriteLine("Notes1: {0}", res.Notes1)
    Console.WriteLine("Notes2: {0}", res.Notes2)
    Console.WriteLine("Notes3: {0}", res.Notes3)
    Console.WriteLine("Notes4: {0}", res.Notes4)
    Console.WriteLine("Url1: {0}", res.Url1)
    Console.WriteLine("Url2: {0}", res.Url2)
    Console.WriteLine("Url3: {0}", res.Url3)
    Console.WriteLine("Url4: {0}", res.Url4)
    Console.WriteLine("Url5: {0}", res.Url5)
    Console.WriteLine("Url6: {0}", res.Url6)
    Console.WriteLine("Url7: {0}", res.Url7)
    Console.WriteLine("Url8: {0}", res.Url8)
    Console.WriteLine("Url9: {0}", res.Url9)
    Console.WriteLine("Url10: {0}", res.Url10)
    Console.WriteLine("Url1Description: {0}", res.Url1Description)
    Console.WriteLine("Url2Description: {0}", res.Url2Description)
    Console.WriteLine("Url3Description: {0}", res.Url3Description)
    Console.WriteLine("Url4Description: {0}", res.Url4Description)
    Console.WriteLine("Url5Description: {0}", res.Url5Description)
    Console.WriteLine("Url6Description: {0}", res.Url6Description)
    Console.WriteLine("Url7Description: {0}", res.Url7Description)
    Console.WriteLine("Url8Description: {0}", res.Url8Description)
    Console.WriteLine("Url9Description: {0}", res.Url9Description)
    Console.WriteLine("Url10Description: {0}", res.Url10Description)
    Console.WriteLine("Image1: {0}", res.Image1)
    Console.WriteLine("Image2: {0}", res.Image2)
    Console.WriteLine("ImageUrl1: {0}", res.ImageUrl1)
    Console.WriteLine("ImageUrl2: {0}", res.ImageUrl2)
    Console.WriteLine("CustomerKey: {0}", res.CustomerKey)

    For Each byte As Byte In res.DataImage1
    Next

    For Each byte As Byte In res.DataImage2
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

    $req->WebAlias = "1";
    $req->CustomerID = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.GetCustomerSite($req);

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
    GetCustomerSiteRequest req = new GetCustomerSiteRequest();

    req.setWebAlias("1");
    req.setCustomerID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    GetCustomerSiteResponse res = api.getExigoApiSoap().getCustomerSite(req, auth);

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
https://api.exigo.com/3.0/csv/?method=GetCustomerSite
&ApiLoginName=String
&ApiPassword=String
&ApiCompany=String
&WebAlias=String
&CustomerID=Nullable`1
&CustomerKey=String
Response FieldsCustomerID,WebAlias,FirstName,LastName,Company,Address1,Address2,City,State,Zip,Country,Email,Phone,Phone2,Fax,Notes1,Notes2,Notes3,Notes4,Url1,Url2,Url3,Url4,Url5,Url6,Url7,Url8,Url9,Url10,Url1Description,Url2Description,Url3Description,Url4Description,Url5Description,Url6Description,Url7Description,Url8Description,Url9Description,Url10Description,Image1,Image2,ImageUrl1,ImageUrl2,CustomerKey
Int32,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String,String

                    © 2026 Exigo.
```

</details>

---

### GetCustomerBilling

>  Returns billing accounts on file for a customer. Only => s last
>  four digits of a credit card.

| | |
|---|---|
| Category | Customers |
| REST | `GET /3.0/account?customerID=1` |
| SOAP action | `https://api.exigo.com/GetCustomerBilling` |
| WSDL elements | `GetCustomerBillingRequest` → `GetCustomerBillingResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetCustomerBilling |

#### Input

**`GetCustomerBillingRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`GetCustomerBillingResponse`**

| Property | Type | Notes |
|---|---|---|
| `PrimaryCreditCard` | `CreditCardAccountResponse` |  |
| `SecondaryCreditCard` | `CreditCardAccountResponse` |  |
| `BankAccount` | `BankAccountResponse` |  |
| `PrimaryWalletAccount` | `WalletAccountResponse` |  |
| `SecondaryWallletAccount` | `WalletAccountResponse` |  |
| `ThirdWalletAccount` | `WalletAccountResponse` |  |
| `FourthWalletAccount` | `WalletAccountResponse` |  |
| `FifthWalletAccount` | `WalletAccountResponse` |  |

**`CreditCardAccountResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `CreditCardNumberDisplay` | `String` |  |
| &nbsp;&nbsp;↳ `CreditCardToken` | `String` |  |
| &nbsp;&nbsp;↳ `ExpirationMonth` | `Int32` |  |
| &nbsp;&nbsp;↳ `ExpirationYear` | `Int32` |  |
| &nbsp;&nbsp;↳ `CreditCardType` | `Int32` | Optionally pass in Visa, Master Card, etc.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `CreditCardTypeDescription` | `String` |  |
| &nbsp;&nbsp;↳ `BillingName` | `String` |  |
| &nbsp;&nbsp;↳ `BillingAddress` | `String` |  |
| &nbsp;&nbsp;↳ `BillingCity` | `String` |  |
| &nbsp;&nbsp;↳ `BillingState` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `BillingZip` | `String` |  |
| &nbsp;&nbsp;↳ `BillingCountry` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `BillingAddress2` | `String` |  |

**`CreditCardAccountResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `CreditCardNumberDisplay` | `String` |  |
| &nbsp;&nbsp;↳ `CreditCardToken` | `String` |  |
| &nbsp;&nbsp;↳ `ExpirationMonth` | `Int32` |  |
| &nbsp;&nbsp;↳ `ExpirationYear` | `Int32` |  |
| &nbsp;&nbsp;↳ `CreditCardType` | `Int32` | Optionally pass in Visa, Master Card, etc.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `CreditCardTypeDescription` | `String` |  |
| &nbsp;&nbsp;↳ `BillingName` | `String` |  |
| &nbsp;&nbsp;↳ `BillingAddress` | `String` |  |
| &nbsp;&nbsp;↳ `BillingCity` | `String` |  |
| &nbsp;&nbsp;↳ `BillingState` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `BillingZip` | `String` |  |
| &nbsp;&nbsp;↳ `BillingCountry` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `BillingAddress2` | `String` |  |

**`BankAccountResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `BankAccountNumberDisplay` | `String` |  |
| &nbsp;&nbsp;↳ `BankRoutingNumber` | `String` |  |
| &nbsp;&nbsp;↳ `BankName` | `String` |  |
| &nbsp;&nbsp;↳ `BankAccountType` | `BankAccountType` | **Values:** `CheckingPersonal`, `CheckingBusiness`, `SavingsPersonal`, `SavingsBusiness` |
| &nbsp;&nbsp;↳ `NameOnAccount` | `String` |  |
| &nbsp;&nbsp;↳ `BillingAddress` | `String` |  |
| &nbsp;&nbsp;↳ `BillingCity` | `String` |  |
| &nbsp;&nbsp;↳ `BillingState` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `BillingZip` | `String` |  |
| &nbsp;&nbsp;↳ `BillingCountry` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `BillingAddress2` | `String` |  |
| &nbsp;&nbsp;↳ `CheckIban` | `String` |  |
| &nbsp;&nbsp;↳ `CheckSwiftCode` | `String` |  |

**`WalletAccountResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `WalletType` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `WalletAccountDisplay` | `String` |  |
| &nbsp;&nbsp;↳ `WalletOther1` | `String` |  |
| &nbsp;&nbsp;↳ `WalletOther2` | `String` |  |
| &nbsp;&nbsp;↳ `WalletOther3` | `String` |  |

**`WalletAccountResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `WalletType` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `WalletAccountDisplay` | `String` |  |
| &nbsp;&nbsp;↳ `WalletOther1` | `String` |  |
| &nbsp;&nbsp;↳ `WalletOther2` | `String` |  |
| &nbsp;&nbsp;↳ `WalletOther3` | `String` |  |

**`WalletAccountResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `WalletType` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `WalletAccountDisplay` | `String` |  |
| &nbsp;&nbsp;↳ `WalletOther1` | `String` |  |
| &nbsp;&nbsp;↳ `WalletOther2` | `String` |  |
| &nbsp;&nbsp;↳ `WalletOther3` | `String` |  |

**`WalletAccountResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `WalletType` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `WalletAccountDisplay` | `String` |  |
| &nbsp;&nbsp;↳ `WalletOther1` | `String` |  |
| &nbsp;&nbsp;↳ `WalletOther2` | `String` |  |
| &nbsp;&nbsp;↳ `WalletOther3` | `String` |  |

**`WalletAccountResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `WalletType` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `WalletAccountDisplay` | `String` |  |
| &nbsp;&nbsp;↳ `WalletOther1` | `String` |  |
| &nbsp;&nbsp;↳ `WalletOther2` | `String` |  |
| &nbsp;&nbsp;↳ `WalletOther3` | `String` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/account?customerID=1
  &customerKey=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "primaryCreditCard": null,
  "secondaryCreditCard": null,
  "bankAccount": null,
  "primaryWalletAccount": null,
  "secondaryWallletAccount": null,
  "thirdWalletAccount": null,
  "fourthWalletAccount": null,
  "fifthWalletAccount": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetCustomerBilling"

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
    <GetCustomerBillingRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
    </GetCustomerBillingRequest>
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
    <GetCustomerBillingResult xmlns="http://api.exigo.com/">
      <PrimaryCreditCard>
        <CreditCardNumberDisplay>string</CreditCardNumberDisplay>
        <CreditCardToken>string</CreditCardToken>
        <ExpirationMonth>int</ExpirationMonth>
        <ExpirationYear>int</ExpirationYear>
        <CreditCardType>int</CreditCardType>
        <CreditCardTypeDescription>string</CreditCardTypeDescription>
        <BillingName>string</BillingName>
        <BillingAddress>string</BillingAddress>
        <BillingCity>string</BillingCity>
        <BillingState>string</BillingState>
        <BillingZip>string</BillingZip>
        <BillingCountry>string</BillingCountry>
        <BillingAddress2>string</BillingAddress2>
      </PrimaryCreditCard>
      <SecondaryCreditCard>
        <CreditCardNumberDisplay>string</CreditCardNumberDisplay>
        <CreditCardToken>string</CreditCardToken>
        <ExpirationMonth>int</ExpirationMonth>
        <ExpirationYear>int</ExpirationYear>
        <CreditCardType>int</CreditCardType>
        <CreditCardTypeDescription>string</CreditCardTypeDescription>
        <BillingName>string</BillingName>
        <BillingAddress>string</BillingAddress>
        <BillingCity>string</BillingCity>
        <BillingState>string</BillingState>
        <BillingZip>string</BillingZip>
        <BillingCountry>string</BillingCountry>
        <BillingAddress2>string</BillingAddress2>
      </SecondaryCreditCard>
      <BankAccount>
        <BankAccountNumberDisplay>string</BankAccountNumberDisplay>
        <BankRoutingNumber>string</BankRoutingNumber>
        <BankName>string</BankName>
        <BankAccountType>CheckingPersonal or CheckingBusiness or SavingsPersonal or SavingsBusiness</BankAccountType>
        <NameOnAccount>string</NameOnAccount>
        <BillingAddress>string</BillingAddress>
        <BillingCity>string</BillingCity>
        <BillingState>string</BillingState>
        <BillingZip>string</BillingZip>
        <BillingCountry>string</BillingCountry>
        <BillingAddress2>string</BillingAddress2>
        <CheckIban>string</CheckIban>
        <CheckSwiftCode>string</CheckSwiftCode>
      </BankAccount>
      <PrimaryWalletAccount>
        <WalletType>int</WalletType>
        <WalletAccountDisplay>string</WalletAccountDisplay>
        <WalletOther1>string</WalletOther1>
        <WalletOther2>string</WalletOther2>
        <WalletOther3>string</WalletOther3>
      </PrimaryWalletAccount>
      <SecondaryWallletAccount>
        <WalletType>int</WalletType>
        <WalletAccountDisplay>string</WalletAccountDisplay>
        <WalletOther1>string</WalletOther1>
        <WalletOther2>string</WalletOther2>
        <WalletOther3>string</WalletOther3>
      </SecondaryWallletAccount>
      <ThirdWalletAccount>
        <WalletType>int</WalletType>
        <WalletAccountDisplay>string</WalletAccountDisplay>
        <WalletOther1>string</WalletOther1>
        <WalletOther2>string</WalletOther2>
        <WalletOther3>string</WalletOther3>
      </ThirdWalletAccount>
      <FourthWalletAccount>
        <WalletType>int</WalletType>
        <WalletAccountDisplay>string</WalletAccountDisplay>
        <WalletOther1>string</WalletOther1>
        <WalletOther2>string</WalletOther2>
        <WalletOther3>string</WalletOther3>
      </FourthWalletAccount>
      <FifthWalletAccount>
        <WalletType>int</WalletType>
        <WalletAccountDisplay>string</WalletAccountDisplay>
        <WalletOther1>string</WalletOther1>
        <WalletOther2>string</WalletOther2>
        <WalletOther3>string</WalletOther3>
      </FifthWalletAccount>
    </GetCustomerBillingResult>
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
    var req = new GetCustomerBillingRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.GetCustomerBillingAsync(req);

    //Now examine the results:
    Console.WriteLine("PrimaryCreditCard: {0}", res.PrimaryCreditCard);
    Console.WriteLine("SecondaryCreditCard: {0}", res.SecondaryCreditCard);
    Console.WriteLine("BankAccount: {0}", res.BankAccount);
    Console.WriteLine("PrimaryWalletAccount: {0}", res.PrimaryWalletAccount);
    Console.WriteLine("SecondaryWallletAccount: {0}", res.SecondaryWallletAccount);
    Console.WriteLine("ThirdWalletAccount: {0}", res.ThirdWalletAccount);
    Console.WriteLine("FourthWalletAccount: {0}", res.FourthWalletAccount);
    Console.WriteLine("FifthWalletAccount: {0}", res.FifthWalletAccount);
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
    GetCustomerBillingRequest req = new GetCustomerBillingRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    GetCustomerBillingResponse res = api.GetCustomerBilling(req);

    //Now examine the results:
    Console.WriteLine("PrimaryCreditCard: {0}", res.PrimaryCreditCard);
    Console.WriteLine("SecondaryCreditCard: {0}", res.SecondaryCreditCard);
    Console.WriteLine("BankAccount: {0}", res.BankAccount);
    Console.WriteLine("PrimaryWalletAccount: {0}", res.PrimaryWalletAccount);
    Console.WriteLine("SecondaryWallletAccount: {0}", res.SecondaryWallletAccount);
    Console.WriteLine("ThirdWalletAccount: {0}", res.ThirdWalletAccount);
    Console.WriteLine("FourthWalletAccount: {0}", res.FourthWalletAccount);
    Console.WriteLine("FifthWalletAccount: {0}", res.FifthWalletAccount);
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
    Dim req as new GetCustomerBillingRequest()

    req.CustomerID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As GetCustomerBillingResponse = api.GetCustomerBilling(req)

    'Now examine the results:
    Console.WriteLine("PrimaryCreditCard: {0}", res.PrimaryCreditCard)
    Console.WriteLine("SecondaryCreditCard: {0}", res.SecondaryCreditCard)
    Console.WriteLine("BankAccount: {0}", res.BankAccount)
    Console.WriteLine("PrimaryWalletAccount: {0}", res.PrimaryWalletAccount)
    Console.WriteLine("SecondaryWallletAccount: {0}", res.SecondaryWallletAccount)
    Console.WriteLine("ThirdWalletAccount: {0}", res.ThirdWalletAccount)
    Console.WriteLine("FourthWalletAccount: {0}", res.FourthWalletAccount)
    Console.WriteLine("FifthWalletAccount: {0}", res.FifthWalletAccount)
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
    $res = $api.GetCustomerBilling($req);

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
    GetCustomerBillingRequest req = new GetCustomerBillingRequest();

    req.setCustomerID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    GetCustomerBillingResponse res = api.getExigoApiSoap().getCustomerBilling(req, auth);

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

### GetCustomerNotes

> Returns the notes field for one or more customers that match the
>  filter critera passed in.

| | |
|---|---|
| Category | Customers |
| REST | `GET /3.0/customers/notes?customerID=1` |
| SOAP action | `https://api.exigo.com/GetCustomerNotes` |
| WSDL elements | `GetCustomerNotesRequest` → `GetCustomerNotesResult` |
| CSV output | Yes — `GET https://api.exigo.com/3.0/csv/?method=GetCustomerNotes&ApiLoginName=…&ApiPassword=…&ApiCompany=…` |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetCustomerNotes |

#### Input

**`GetCustomerNotesRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`GetCustomerNotesResponse`**

| Property | Type | Notes |
|---|---|---|
| `CustomerNotes` | `CustomerNotesResponse[]` |  |

**`CustomerNotesResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| &nbsp;&nbsp;↳ `Notes` | `String` |  |
| &nbsp;&nbsp;↳ `CustomerKey` | `String` | Unique alpha numeric identifier for customer record . |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/customers/notes?customerID=1
  &customerKey=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "customerNotes": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetCustomerNotes"

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
    <GetCustomerNotesRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
    </GetCustomerNotesRequest>
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
    <GetCustomerNotesResult xmlns="http://api.exigo.com/">
      <CustomerNotes>
        <CustomerNotesResponse>
          <CustomerID>int</CustomerID>
          <Notes>string</Notes>
          <CustomerKey>string</CustomerKey>
        </CustomerNotesResponse>
      </CustomerNotes>
    </GetCustomerNotesResult>
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
    var req = new GetCustomerNotesRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.GetCustomerNotesAsync(req);

    //Now examine the results:

    foreach (var customerNotes  in res.CustomerNotes)
    {
        Console.WriteLine("CustomerID: {0}", customerNotes.CustomerID);
        Console.WriteLine("Notes: {0}", customerNotes.Notes);
        Console.WriteLine("CustomerKey: {0}", customerNotes.CustomerKey);
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
    GetCustomerNotesRequest req = new GetCustomerNotesRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    GetCustomerNotesResponse res = api.GetCustomerNotes(req);

    //Now examine the results:

    foreach (CustomerNotesResponse customerNotes  in res.CustomerNotes)
    {
        Console.WriteLine("CustomerID: {0}", customerNotes.CustomerID);
        Console.WriteLine("Notes: {0}", customerNotes.Notes);
        Console.WriteLine("CustomerKey: {0}", customerNotes.CustomerKey);
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
    Dim req as new GetCustomerNotesRequest()

    req.CustomerID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As GetCustomerNotesResponse = api.GetCustomerNotes(req)

    'Now examine the results:

    For Each customerNotes As CustomerNotesResponse In res.CustomerNotes
        Console.WriteLine("CustomerID: {0}", customerNotes.CustomerID)
        Console.WriteLine("Notes: {0}", customerNotes.Notes)
        Console.WriteLine("CustomerKey: {0}", customerNotes.CustomerKey)
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
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.GetCustomerNotes($req);

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
    GetCustomerNotesRequest req = new GetCustomerNotesRequest();

    req.setCustomerID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    GetCustomerNotesResponse res = api.getExigoApiSoap().getCustomerNotes(req, auth);

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
https://api.exigo.com/3.0/csv/?method=GetCustomerNotes
&ApiLoginName=String
&ApiPassword=String
&ApiCompany=String
&CustomerID=Int32
&CustomerKey=String
Response FieldsCustomerID,Notes,CustomerKey
Int32,String,String

                    © 2026 Exigo.
```

</details>

---

### AppendCustomerNotes

> Appends a specified value to the specified Customer's Notes record
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Customers |
| REST | `PATCH /3.0/customers/notes` |
| SOAP action | `https://api.exigo.com/AppendCustomerNotes` |
| WSDL elements | `AppendCustomerNotesRequest` → `AppendCustomerNotesResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=AppendCustomerNotes |

#### Input

**`AppendCustomerNotesRequest`**

| Property | Type | Notes |
|---|---|---|
| `Notes` | `String` | Optional. Value to be appended to Customer Notes. |
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`AppendCustomerNotesResponse`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Unique alpha numeric identifier for customer record . |

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/customers/notes HTTP/1.1
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
  "customerID": 1,
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
SOAPAction: "https://api.exigo.com/AppendCustomerNotes"

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
    <AppendCustomerNotesRequest xmlns="http://api.exigo.com/">
      <Notes>string</Notes>
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
    </AppendCustomerNotesRequest>
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
    <AppendCustomerNotesResult xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
    </AppendCustomerNotesResult>
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
    var req = new AppendCustomerNotesRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.AppendCustomerNotesAsync(req);

    //Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID);
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
    AppendCustomerNotesRequest req = new AppendCustomerNotesRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    AppendCustomerNotesResponse res = api.AppendCustomerNotes(req);

    //Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID);
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
    Dim req as new AppendCustomerNotesRequest()

    req.CustomerID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As AppendCustomerNotesResponse = api.AppendCustomerNotes(req)

    'Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID)
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
    $res = $api.AppendCustomerNotes($req);

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
    AppendCustomerNotesRequest req = new AppendCustomerNotesRequest();

    req.setCustomerID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    AppendCustomerNotesResponse res = api.getExigoApiSoap().appendCustomerNotes(req, auth);

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

### GetAccountDirectDeposit

> Returns direct deposit info for an existing customer.

| | |
|---|---|
| Category | Customers |
| REST | `GET /3.0/account/directdeposit?customerID=1` |
| SOAP action | `https://api.exigo.com/GetAccountDirectDeposit` |
| WSDL elements | `GetAccountDirectDepositRequest` → `GetAccountDirectDepositResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetAccountDirectDeposit |

#### Input

**`GetAccountDirectDepositRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`GetAccountDirectDepositResponse`**

| Property | Type | Notes |
|---|---|---|
| `NameOnAccount` | `String` |  |
| `BankAccountNumberDisplay` | `String` |  |
| `BankRoutingNumber` | `String` |  |
| `DepositAccountType` | `DepositAccountType` | Deprecated, use DepositAccountType instead.<br>**Values:** `Checking`, `Saving`, `Business`, `Personal` |
| `BankName` | `String` |  |
| `BankAddress` | `String` |  |
| `BankCity` | `String` |  |
| `BankState` | `String` |  |
| `BankZip` | `String` |  |
| `BankCountry` | `String` |  |
| `BankAccountType` | `BankAccountType` | Deprecated, use DepositAccountTypeID instead.<br>**Values:** `CheckingPersonal`, `CheckingBusiness`, `SavingsPersonal`, `SavingsBusiness` |
| `Iban` | `String` |  |
| `SwiftCode` | `String` |  |
| `DepositAccountTypeID` | `Int32` | Classification of bank account.<br>**Lookup:** company-specific list (see company-lists.md) |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/account/directdeposit?customerID=1
  &customerKey=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "nameOnAccount": "",
  "bankAccountNumberDisplay": "",
  "bankRoutingNumber": "",
  "depositAccountType": null,
  "bankName": "",
  "bankAddress": "",
  "bankCity": "",
  "bankState": "",
  "bankZip": "",
  "bankCountry": "",
  "bankAccountType": null,
  "iban": "",
  "swiftCode": "",
  "depositAccountTypeID": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetAccountDirectDeposit"

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
    <GetAccountDirectDepositRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
    </GetAccountDirectDepositRequest>
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
    <GetAccountDirectDepositResult xmlns="http://api.exigo.com/">
      <NameOnAccount>string</NameOnAccount>
      <BankAccountNumberDisplay>string</BankAccountNumberDisplay>
      <BankRoutingNumber>string</BankRoutingNumber>
      <DepositAccountType>Checking or Saving or Business or Personal</DepositAccountType>
      <BankName>string</BankName>
      <BankAddress>string</BankAddress>
      <BankCity>string</BankCity>
      <BankState>string</BankState>
      <BankZip>string</BankZip>
      <BankCountry>string</BankCountry>
      <BankAccountType>CheckingPersonal or CheckingBusiness or SavingsPersonal or SavingsBusiness</BankAccountType>
      <Iban>string</Iban>
      <SwiftCode>string</SwiftCode>
      <DepositAccountTypeID>int</DepositAccountTypeID>
    </GetAccountDirectDepositResult>
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
    var req = new GetAccountDirectDepositRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.GetAccountDirectDepositAsync(req);

    //Now examine the results:
    Console.WriteLine("NameOnAccount: {0}", res.NameOnAccount);
    Console.WriteLine("BankAccountNumberDisplay: {0}", res.BankAccountNumberDisplay);
    Console.WriteLine("BankRoutingNumber: {0}", res.BankRoutingNumber);
    Console.WriteLine("BankName: {0}", res.BankName);
    Console.WriteLine("BankAddress: {0}", res.BankAddress);
    Console.WriteLine("BankCity: {0}", res.BankCity);
    Console.WriteLine("BankState: {0}", res.BankState);
    Console.WriteLine("BankZip: {0}", res.BankZip);
    Console.WriteLine("BankCountry: {0}", res.BankCountry);
    Console.WriteLine("Iban: {0}", res.Iban);
    Console.WriteLine("SwiftCode: {0}", res.SwiftCode);
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
    GetAccountDirectDepositRequest req = new GetAccountDirectDepositRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    GetAccountDirectDepositResponse res = api.GetAccountDirectDeposit(req);

    //Now examine the results:
    Console.WriteLine("NameOnAccount: {0}", res.NameOnAccount);
    Console.WriteLine("BankAccountNumberDisplay: {0}", res.BankAccountNumberDisplay);
    Console.WriteLine("BankRoutingNumber: {0}", res.BankRoutingNumber);
    Console.WriteLine("BankName: {0}", res.BankName);
    Console.WriteLine("BankAddress: {0}", res.BankAddress);
    Console.WriteLine("BankCity: {0}", res.BankCity);
    Console.WriteLine("BankState: {0}", res.BankState);
    Console.WriteLine("BankZip: {0}", res.BankZip);
    Console.WriteLine("BankCountry: {0}", res.BankCountry);
    Console.WriteLine("Iban: {0}", res.Iban);
    Console.WriteLine("SwiftCode: {0}", res.SwiftCode);
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
    Dim req as new GetAccountDirectDepositRequest()

    req.CustomerID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As GetAccountDirectDepositResponse = api.GetAccountDirectDeposit(req)

    'Now examine the results:
    Console.WriteLine("NameOnAccount: {0}", res.NameOnAccount)
    Console.WriteLine("BankAccountNumberDisplay: {0}", res.BankAccountNumberDisplay)
    Console.WriteLine("BankRoutingNumber: {0}", res.BankRoutingNumber)
    Console.WriteLine("BankName: {0}", res.BankName)
    Console.WriteLine("BankAddress: {0}", res.BankAddress)
    Console.WriteLine("BankCity: {0}", res.BankCity)
    Console.WriteLine("BankState: {0}", res.BankState)
    Console.WriteLine("BankZip: {0}", res.BankZip)
    Console.WriteLine("BankCountry: {0}", res.BankCountry)
    Console.WriteLine("Iban: {0}", res.Iban)
    Console.WriteLine("SwiftCode: {0}", res.SwiftCode)
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
    $res = $api.GetAccountDirectDeposit($req);

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
    GetAccountDirectDepositRequest req = new GetAccountDirectDepositRequest();

    req.setCustomerID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    GetAccountDirectDepositResponse res = api.getExigoApiSoap().getAccountDirectDeposit(req, auth);

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

### CreateCustomerExtended

> Creates a new customer extended record.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Customers |
| REST | `POST /3.0/customers/extended` |
| SOAP action | `https://api.exigo.com/CreateCustomerExtended` |
| WSDL elements | `CreateCustomerExtendedRequest` → `CreateCustomerExtendedResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateCustomerExtended |

#### Input

**`CreateCustomerExtendedRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `ExtendedGroupID` | `Int32` | Unique ID of data set.<br>**Lookup:** company-specific list (see company-lists.md) |
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
| `Field16` | `String` | Optional. |
| `Field17` | `String` | Optional. |
| `Field18` | `String` | Optional. |
| `Field19` | `String` | Optional. |
| `Field20` | `String` | Optional. |
| `Field21` | `String` | Optional. |
| `Field22` | `String` | Optional. |
| `Field23` | `String` | Optional. |
| `Field24` | `String` | Optional. |
| `Field25` | `String` | Optional. |
| `Field26` | `String` | Optional. |
| `Field27` | `String` | Optional. |
| `Field28` | `String` | Optional. |
| `Field29` | `String` | Optional. |
| `Field30` | `String` | Optional. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`CreateCustomerExtendedResponse`**

| Property | Type | Notes |
|---|---|---|
| `CustomerExtendedID` | `Int32` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/customers/extended HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "extendedGroupID": 1,
  "customerKey": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "customerExtendedID": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateCustomerExtended"

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
    <CreateCustomerExtendedRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <ExtendedGroupID>int</ExtendedGroupID>
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
      <Field16>string</Field16>
      <Field17>string</Field17>
      <Field18>string</Field18>
      <Field19>string</Field19>
      <Field20>string</Field20>
      <Field21>string</Field21>
      <Field22>string</Field22>
      <Field23>string</Field23>
      <Field24>string</Field24>
      <Field25>string</Field25>
      <Field26>string</Field26>
      <Field27>string</Field27>
      <Field28>string</Field28>
      <Field29>string</Field29>
      <Field30>string</Field30>
      <CustomerKey>string</CustomerKey>
    </CreateCustomerExtendedRequest>
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
    <CreateCustomerExtendedResult xmlns="http://api.exigo.com/">
      <CustomerExtendedID>int</CustomerExtendedID>
    </CreateCustomerExtendedResult>
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
    var req = new CreateCustomerExtendedRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.ExtendedGroupID = 1;        //Unique ID of data set
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.CreateCustomerExtendedAsync(req);

    //Now examine the results:
    Console.WriteLine("CustomerExtendedID: {0}", res.CustomerExtendedID);
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
    CreateCustomerExtendedRequest req = new CreateCustomerExtendedRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.ExtendedGroupID = 1;        //Unique ID of data set
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    CreateCustomerExtendedResponse res = api.CreateCustomerExtended(req);

    //Now examine the results:
    Console.WriteLine("CustomerExtendedID: {0}", res.CustomerExtendedID);
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
    Dim req as new CreateCustomerExtendedRequest()

    req.CustomerID = 1
    req.ExtendedGroupID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As CreateCustomerExtendedResponse = api.CreateCustomerExtended(req)

    'Now examine the results:
    Console.WriteLine("CustomerExtendedID: {0}", res.CustomerExtendedID)
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
    $req->ExtendedGroupID = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.CreateCustomerExtended($req);

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
    CreateCustomerExtendedRequest req = new CreateCustomerExtendedRequest();

    req.setCustomerID(1);
    req.setExtendedGroupID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    CreateCustomerExtendedResponse res = api.getExigoApiSoap().createCustomerExtended(req, auth);

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

### UpdateCustomerExtended

> Updates one customer extended record.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Customers |
| REST | `PATCH /3.0/customers/extended` |
| SOAP action | `https://api.exigo.com/UpdateCustomerExtended` |
| WSDL elements | `UpdateCustomerExtendedRequest` → `UpdateCustomerExtendedResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateCustomerExtended |

#### Input

**`UpdateCustomerExtendedRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `ExtendedGroupID` | `Int32` | The identifer for the ExtendedProperty to update.<br>**Lookup:** company-specific list (see company-lists.md) |
| `CustomerExtendedID` | `Int32` | The identifier for the CustomerExtended entry. |
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
| `Field16` | `String` | Optional. |
| `Field17` | `String` | Optional. |
| `Field18` | `String` | Optional. |
| `Field19` | `String` | Optional. |
| `Field20` | `String` | Optional. |
| `Field21` | `String` | Optional. |
| `Field22` | `String` | Optional. |
| `Field23` | `String` | Optional. |
| `Field24` | `String` | Optional. |
| `Field25` | `String` | Optional. |
| `Field26` | `String` | Optional. |
| `Field27` | `String` | Optional. |
| `Field28` | `String` | Optional. |
| `Field29` | `String` | Optional. |
| `Field30` | `String` | Optional. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`UpdateCustomerExtendedResponse`**

_No properties._

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/customers/extended HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "extendedGroupID": 1,
  "customerExtendedID": 1,
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
SOAPAction: "https://api.exigo.com/UpdateCustomerExtended"

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
    <UpdateCustomerExtendedRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <ExtendedGroupID>int</ExtendedGroupID>
      <CustomerExtendedID>int</CustomerExtendedID>
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
      <Field16>string</Field16>
      <Field17>string</Field17>
      <Field18>string</Field18>
      <Field19>string</Field19>
      <Field20>string</Field20>
      <Field21>string</Field21>
      <Field22>string</Field22>
      <Field23>string</Field23>
      <Field24>string</Field24>
      <Field25>string</Field25>
      <Field26>string</Field26>
      <Field27>string</Field27>
      <Field28>string</Field28>
      <Field29>string</Field29>
      <Field30>string</Field30>
      <CustomerKey>string</CustomerKey>
    </UpdateCustomerExtendedRequest>
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
    <UpdateCustomerExtendedResult xmlns="http://api.exigo.com/" />
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
    var req = new UpdateCustomerExtendedRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.ExtendedGroupID = 1;        //The identifer for the ExtendedProperty to update.
    req.CustomerExtendedID = 1;     //The identifier for the CustomerExtended entry.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.UpdateCustomerExtendedAsync(req);

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
    UpdateCustomerExtendedRequest req = new UpdateCustomerExtendedRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.ExtendedGroupID = 1;        //The identifer for the ExtendedProperty to update.
    req.CustomerExtendedID = 1;     //The identifier for the CustomerExtended entry.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    UpdateCustomerExtendedResponse res = api.UpdateCustomerExtended(req);

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
    Dim req as new UpdateCustomerExtendedRequest()

    req.CustomerID = 1
    req.ExtendedGroupID = 1
    req.CustomerExtendedID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As UpdateCustomerExtendedResponse = api.UpdateCustomerExtended(req)

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
    $req->ExtendedGroupID = 1;
    $req->CustomerExtendedID = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.UpdateCustomerExtended($req);

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
    UpdateCustomerExtendedRequest req = new UpdateCustomerExtendedRequest();

    req.setCustomerID(1);
    req.setExtendedGroupID(1);
    req.setCustomerExtendedID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    UpdateCustomerExtendedResponse res = api.getExigoApiSoap().updateCustomerExtended(req, auth);

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

### GetCustomerExtended

>  Returns extended properties setup for a customer.

| | |
|---|---|
| Category | Customers |
| REST | `GET /3.0/customers/extended?extendedGroupID=1` |
| SOAP action | `https://api.exigo.com/GetCustomerExtended` |
| WSDL elements | `GetCustomerExtendedRequest` → `GetCustomerExtendedResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetCustomerExtended |

#### Input

**`GetCustomerExtendedRequest`**

| Property | Type | Notes |
|---|---|---|
| `ExtendedGroupID` | `Int32` | Unique ID of data set.<br>**Lookup:** company-specific list (see company-lists.md) |
| `CustomerID` | `Int32` | Optional. Optionally supply if getting data for just one customer. |
| `CustomerExtendedID` | `Int32` | Optional. Optionally supply if getting a single record. |
| `Field1` | `String` | Optional. Optionally search Field1. |
| `Field2` | `String` | Optional. Optionally search Field2. |
| `Field3` | `String` | Optional. Optionally search Field3. |
| `Field4` | `String` | Optional. Optionally search Field4. |
| `Field5` | `String` | Optional. Optionally search Field5. |
| `Field6` | `String` | Optional. Optionally search Field6. |
| `Field7` | `String` | Optional. Optionally search Field7. |
| `Field8` | `String` | Optional. Optionally search Field8. |
| `Field9` | `String` | Optional. Optionally search Field9. |
| `Field10` | `String` | Optional. Optionally search Field10. |
| `Field11` | `String` | Optional. Optionally search Field11. |
| `Field12` | `String` | Optional. Optionally search Field12. |
| `Field13` | `String` | Optional. Optionally search Field13. |
| `Field14` | `String` | Optional. Optionally search Field14. |
| `Field15` | `String` | Optional. Optionally search Field15. |
| `Field16` | `String` | Optional. Optionally search Field16. |
| `Field17` | `String` | Optional. Optionally search Field17. |
| `Field18` | `String` | Optional. Optionally search Field18. |
| `Field19` | `String` | Optional. Optionally search Field19. |
| `Field20` | `String` | Optional. Optionally search Field20. |
| `Field21` | `String` | Optional. Optionally search Field21. |
| `Field22` | `String` | Optional. Optionally search Field22. |
| `Field23` | `String` | Optional. Optionally search Field23. |
| `Field24` | `String` | Optional. Optionally search Field24. |
| `Field25` | `String` | Optional. Optionally search Field25. |
| `Field26` | `String` | Optional. Optionally search Field26. |
| `Field27` | `String` | Optional. Optionally search Field27. |
| `Field28` | `String` | Optional. Optionally search Field28. |
| `Field29` | `String` | Optional. Optionally search Field29. |
| `Field30` | `String` | Optional. Optionally search Field30. |
| `GreaterThanCustomerExtendedID` | `Int32` | Optional. Use when pulling data in chunks. |
| `GreaterThanModifiedDate` | `DateTime` | Optional. Use when pulling data in chunks. |
| `BatchSize` | `Int32` | Optional. Defaults to 100 at a time. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`GetCustomerExtendedResponse`**

| Property | Type | Notes |
|---|---|---|
| `Items` | `CustomerExtendedResponse[]` |  |

**`CustomerExtendedResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| &nbsp;&nbsp;↳ `ExtendedGroupID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `CustomerExtendedID` | `Int32` |  |
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
| &nbsp;&nbsp;↳ `Field16` | `String` |  |
| &nbsp;&nbsp;↳ `Field17` | `String` |  |
| &nbsp;&nbsp;↳ `Field18` | `String` |  |
| &nbsp;&nbsp;↳ `Field19` | `String` |  |
| &nbsp;&nbsp;↳ `Field20` | `String` |  |
| &nbsp;&nbsp;↳ `Field21` | `String` |  |
| &nbsp;&nbsp;↳ `Field22` | `String` |  |
| &nbsp;&nbsp;↳ `Field23` | `String` |  |
| &nbsp;&nbsp;↳ `Field24` | `String` |  |
| &nbsp;&nbsp;↳ `Field25` | `String` |  |
| &nbsp;&nbsp;↳ `Field26` | `String` |  |
| &nbsp;&nbsp;↳ `Field27` | `String` |  |
| &nbsp;&nbsp;↳ `Field28` | `String` |  |
| &nbsp;&nbsp;↳ `Field29` | `String` |  |
| &nbsp;&nbsp;↳ `Field30` | `String` |  |
| &nbsp;&nbsp;↳ `ModifiedDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `CustomerKey` | `String` | Unique alpha numeric identifier for customer record . |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/customers/extended?extendedGroupID=1
  &customerID=1
  &customerKey=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
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
SOAPAction: "https://api.exigo.com/GetCustomerExtended"

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
    <GetCustomerExtendedRequest xmlns="http://api.exigo.com/">
      <ExtendedGroupID>int</ExtendedGroupID>
      <CustomerID>int</CustomerID>
      <CustomerExtendedID>int</CustomerExtendedID>
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
      <Field16>string</Field16>
      <Field17>string</Field17>
      <Field18>string</Field18>
      <Field19>string</Field19>
      <Field20>string</Field20>
      <Field21>string</Field21>
      <Field22>string</Field22>
      <Field23>string</Field23>
      <Field24>string</Field24>
      <Field25>string</Field25>
      <Field26>string</Field26>
      <Field27>string</Field27>
      <Field28>string</Field28>
      <Field29>string</Field29>
      <Field30>string</Field30>
      <GreaterThanCustomerExtendedID>int</GreaterThanCustomerExtendedID>
      <GreaterThanModifiedDate>dateTime</GreaterThanModifiedDate>
      <BatchSize>int</BatchSize>
      <CustomerKey>string</CustomerKey>
    </GetCustomerExtendedRequest>
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
    <GetCustomerExtendedResult xmlns="http://api.exigo.com/">
      <Items>
        <CustomerExtendedResponse>
          <CustomerID>int</CustomerID>
          <ExtendedGroupID>int</ExtendedGroupID>
          <CustomerExtendedID>int</CustomerExtendedID>
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
          <Field16>string</Field16>
          <Field17>string</Field17>
          <Field18>string</Field18>
          <Field19>string</Field19>
          <Field20>string</Field20>
          <Field21>string</Field21>
          <Field22>string</Field22>
          <Field23>string</Field23>
          <Field24>string</Field24>
          <Field25>string</Field25>
          <Field26>string</Field26>
          <Field27>string</Field27>
          <Field28>string</Field28>
          <Field29>string</Field29>
          <Field30>string</Field30>
          <ModifiedDate>dateTime</ModifiedDate>
          <CustomerKey>string</CustomerKey>
        </CustomerExtendedResponse>
      </Items>
    </GetCustomerExtendedResult>
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
    var req = new GetCustomerExtendedRequest();

    req.ExtendedGroupID = 1;        //Unique ID of data set
    req.CustomerID = 1;             //Optionally supply if getting data for just one customer
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.GetCustomerExtendedAsync(req);

    //Now examine the results:

    foreach (var customerExtended  in res.Items)
    {
        Console.WriteLine("CustomerID: {0}", customerExtended.CustomerID);
        Console.WriteLine("ExtendedGroupID: {0}", customerExtended.ExtendedGroupID);
        Console.WriteLine("CustomerExtendedID: {0}", customerExtended.CustomerExtendedID);
        Console.WriteLine("Field16: {0}", customerExtended.Field16);
        Console.WriteLine("Field17: {0}", customerExtended.Field17);
        Console.WriteLine("Field18: {0}", customerExtended.Field18);
        Console.WriteLine("Field19: {0}", customerExtended.Field19);
        Console.WriteLine("Field20: {0}", customerExtended.Field20);
        Console.WriteLine("Field21: {0}", customerExtended.Field21);
        Console.WriteLine("Field22: {0}", customerExtended.Field22);
        Console.WriteLine("Field23: {0}", customerExtended.Field23);
        Console.WriteLine("Field24: {0}", customerExtended.Field24);
        Console.WriteLine("Field25: {0}", customerExtended.Field25);
        Console.WriteLine("Field26: {0}", customerExtended.Field26);
        Console.WriteLine("Field27: {0}", customerExtended.Field27);
        Console.WriteLine("Field28: {0}", customerExtended.Field28);
        Console.WriteLine("Field29: {0}", customerExtended.Field29);
        Console.WriteLine("Field30: {0}", customerExtended.Field30);
        Console.WriteLine("ModifiedDate: {0}", customerExtended.ModifiedDate);
        Console.WriteLine("CustomerKey: {0}", customerExtended.CustomerKey);
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
    GetCustomerExtendedRequest req = new GetCustomerExtendedRequest();

    req.ExtendedGroupID = 1;        //Unique ID of data set
    req.CustomerID = 1;             //Optionally supply if getting data for just one customer
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    GetCustomerExtendedResponse res = api.GetCustomerExtended(req);

    //Now examine the results:

    foreach (CustomerExtendedResponse customerExtended  in res.Items)
    {
        Console.WriteLine("CustomerID: {0}", customerExtended.CustomerID);
        Console.WriteLine("ExtendedGroupID: {0}", customerExtended.ExtendedGroupID);
        Console.WriteLine("CustomerExtendedID: {0}", customerExtended.CustomerExtendedID);
        Console.WriteLine("Field16: {0}", customerExtended.Field16);
        Console.WriteLine("Field17: {0}", customerExtended.Field17);
        Console.WriteLine("Field18: {0}", customerExtended.Field18);
        Console.WriteLine("Field19: {0}", customerExtended.Field19);
        Console.WriteLine("Field20: {0}", customerExtended.Field20);
        Console.WriteLine("Field21: {0}", customerExtended.Field21);
        Console.WriteLine("Field22: {0}", customerExtended.Field22);
        Console.WriteLine("Field23: {0}", customerExtended.Field23);
        Console.WriteLine("Field24: {0}", customerExtended.Field24);
        Console.WriteLine("Field25: {0}", customerExtended.Field25);
        Console.WriteLine("Field26: {0}", customerExtended.Field26);
        Console.WriteLine("Field27: {0}", customerExtended.Field27);
        Console.WriteLine("Field28: {0}", customerExtended.Field28);
        Console.WriteLine("Field29: {0}", customerExtended.Field29);
        Console.WriteLine("Field30: {0}", customerExtended.Field30);
        Console.WriteLine("ModifiedDate: {0}", customerExtended.ModifiedDate);
        Console.WriteLine("CustomerKey: {0}", customerExtended.CustomerKey);
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
    Dim req as new GetCustomerExtendedRequest()

    req.ExtendedGroupID = 1
    req.CustomerID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As GetCustomerExtendedResponse = api.GetCustomerExtended(req)

    'Now examine the results:

    For Each customerExtended As CustomerExtendedResponse In res.Items
        Console.WriteLine("CustomerID: {0}", customerExtended.CustomerID)
        Console.WriteLine("ExtendedGroupID: {0}", customerExtended.ExtendedGroupID)
        Console.WriteLine("CustomerExtendedID: {0}", customerExtended.CustomerExtendedID)
        Console.WriteLine("Field16: {0}", customerExtended.Field16)
        Console.WriteLine("Field17: {0}", customerExtended.Field17)
        Console.WriteLine("Field18: {0}", customerExtended.Field18)
        Console.WriteLine("Field19: {0}", customerExtended.Field19)
        Console.WriteLine("Field20: {0}", customerExtended.Field20)
        Console.WriteLine("Field21: {0}", customerExtended.Field21)
        Console.WriteLine("Field22: {0}", customerExtended.Field22)
        Console.WriteLine("Field23: {0}", customerExtended.Field23)
        Console.WriteLine("Field24: {0}", customerExtended.Field24)
        Console.WriteLine("Field25: {0}", customerExtended.Field25)
        Console.WriteLine("Field26: {0}", customerExtended.Field26)
        Console.WriteLine("Field27: {0}", customerExtended.Field27)
        Console.WriteLine("Field28: {0}", customerExtended.Field28)
        Console.WriteLine("Field29: {0}", customerExtended.Field29)
        Console.WriteLine("Field30: {0}", customerExtended.Field30)
        Console.WriteLine("ModifiedDate: {0}", customerExtended.ModifiedDate)
        Console.WriteLine("CustomerKey: {0}", customerExtended.CustomerKey)
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

    $req->ExtendedGroupID = 1;
    $req->CustomerID = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.GetCustomerExtended($req);

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
    GetCustomerExtendedRequest req = new GetCustomerExtendedRequest();

    req.setExtendedGroupID(1);
    req.setCustomerID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    GetCustomerExtendedResponse res = api.getExigoApiSoap().getCustomerExtended(req, auth);

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

### DeleteCustomerExtended

> Removes one customer extended record.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Customers |
| REST | `DELETE /3.0/customers/extended` |
| SOAP action | `https://api.exigo.com/DeleteCustomerExtended` |
| WSDL elements | `DeleteCustomerExtendedRequest` → `DeleteCustomerExtendedResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DeleteCustomerExtended |

#### Input

**`DeleteCustomerExtendedRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `ExtendedGroupID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| `CustomerExtendedID` | `Int32` |  |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`DeleteCustomerExtendedResponse`**

| Property | Type | Notes |
|---|---|---|
| `CustomerExtendedID` | `Int32` |  |

#### REST example

```http
DELETE https://yourcompany-api.exigo.com/3.0/customers/extended HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "extendedGroupID": 1,
  "customerExtendedID": 1,
  "customerKey": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "customerExtendedID": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/DeleteCustomerExtended"

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
    <DeleteCustomerExtendedRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <ExtendedGroupID>int</ExtendedGroupID>
      <CustomerExtendedID>int</CustomerExtendedID>
      <CustomerKey>string</CustomerKey>
    </DeleteCustomerExtendedRequest>
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
    <DeleteCustomerExtendedResult xmlns="http://api.exigo.com/">
      <CustomerExtendedID>int</CustomerExtendedID>
    </DeleteCustomerExtendedResult>
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
    var req = new DeleteCustomerExtendedRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.ExtendedGroupID = 1;
    req.CustomerExtendedID = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.DeleteCustomerExtendedAsync(req);

    //Now examine the results:
    Console.WriteLine("CustomerExtendedID: {0}", res.CustomerExtendedID);
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
    DeleteCustomerExtendedRequest req = new DeleteCustomerExtendedRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.ExtendedGroupID = 1;
    req.CustomerExtendedID = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    DeleteCustomerExtendedResponse res = api.DeleteCustomerExtended(req);

    //Now examine the results:
    Console.WriteLine("CustomerExtendedID: {0}", res.CustomerExtendedID);
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
    Dim req as new DeleteCustomerExtendedRequest()

    req.CustomerID = 1
    req.ExtendedGroupID = 1
    req.CustomerExtendedID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As DeleteCustomerExtendedResponse = api.DeleteCustomerExtended(req)

    'Now examine the results:
    Console.WriteLine("CustomerExtendedID: {0}", res.CustomerExtendedID)
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
    $req->ExtendedGroupID = 1;
    $req->CustomerExtendedID = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.DeleteCustomerExtended($req);

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
    DeleteCustomerExtendedRequest req = new DeleteCustomerExtendedRequest();

    req.setCustomerID(1);
    req.setExtendedGroupID(1);
    req.setCustomerExtendedID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    DeleteCustomerExtendedResponse res = api.getExigoApiSoap().deleteCustomerExtended(req, auth);

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

### SetCustomerSocialNetworks

> Deletes all existing social network(s) for the customer, then inserts
>  the provided list of social network(s) for the customer.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Customers |
| REST | `PUT /3.0/customers/socialnetworks` |
| SOAP action | `https://api.exigo.com/SetCustomerSocialNetworks` |
| WSDL elements | `SetCustomerSocialNetworksRequest` → `SetCustomerSocialNetworksResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=SetCustomerSocialNetworks |

#### Input

**`SetCustomerSocialNetworksRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerSocialNetworks` | `CustomerSocialNetworkRequest[]` |  |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

**`CustomerSocialNetworkRequest`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `SocialNetworkID` | `Int32` |  |
| &nbsp;&nbsp;↳ `Url` | `String` |  |

#### Output

**`SetCustomerSocialNetworksResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/customers/socialnetworks HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "customerSocialNetworks": null,
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
SOAPAction: "https://api.exigo.com/SetCustomerSocialNetworks"

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
    <SetCustomerSocialNetworksRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerSocialNetworks>
        <CustomerSocialNetworkRequest>
          <SocialNetworkID>int</SocialNetworkID>
          <Url>string</Url>
        </CustomerSocialNetworkRequest>
      </CustomerSocialNetworks>
      <CustomerKey>string</CustomerKey>
    </SetCustomerSocialNetworksRequest>
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
    <SetCustomerSocialNetworksResult xmlns="http://api.exigo.com/" />
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
    var req = new SetCustomerSocialNetworksRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.

    //Add CustomerSocialNetworks
    var customersocialnetworks = new List<CustomerSocialNetworkRequest>();

    var customerSocialNetwork1 = new CustomerSocialNetworkRequest();
    customerSocialNetwork1.SocialNetworkID = 1;
    customerSocialNetwork1.Url = "1";
    customersocialnetworks.Add(customerSocialNetwork1);

    var customerSocialNetwork2 = new CustomerSocialNetworkRequest();
    customerSocialNetwork2.SocialNetworkID = 2;
    customerSocialNetwork2.Url = "2";
    customersocialnetworks.Add(customerSocialNetwork2);

    //Now attach the list to the request
    req.CustomerSocialNetworks = customersocialnetworks.ToArray();
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.SetCustomerSocialNetworksAsync(req);

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
    SetCustomerSocialNetworksRequest req = new SetCustomerSocialNetworksRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.

    //Add CustomerSocialNetworks
    List<CustomerSocialNetworkRequest> customersocialnetworks = new List<CustomerSocialNetworkRequest>();

    CustomerSocialNetworkRequest customerSocialNetwork1 = new CustomerSocialNetworkRequest();
    customerSocialNetwork1.SocialNetworkID = 1;
    customerSocialNetwork1.Url = "1";
    customersocialnetworks.Add(customerSocialNetwork1);

    CustomerSocialNetworkRequest customerSocialNetwork2 = new CustomerSocialNetworkRequest();
    customerSocialNetwork2.SocialNetworkID = 2;
    customerSocialNetwork2.Url = "2";
    customersocialnetworks.Add(customerSocialNetwork2);

    //Now attach the list to the request
    req.CustomerSocialNetworks = customersocialnetworks.ToArray();
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    SetCustomerSocialNetworksResponse res = api.SetCustomerSocialNetworks(req);

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
    Dim req as new SetCustomerSocialNetworksRequest()

    req.CustomerID = 1

    'Add CustomerSocialNetworks
    Dim customersocialnetworks As New List(Of CustomerSocialNetworkRequest)()

    Dim customerSocialNetwork1 as new CustomerSocialNetworkRequest()
    customerSocialNetwork1.SocialNetworkID = 1
    customerSocialNetwork1.Url = "1"
    customersocialnetworks.Add(customerSocialNetwork1)

    Dim customerSocialNetwork2 as new CustomerSocialNetworkRequest()
    customerSocialNetwork2.SocialNetworkID = 2
    customerSocialNetwork2.Url = "2"
    customersocialnetworks.Add(customerSocialNetwork2)

    'Now attach the list to the request
    req.CustomerSocialNetworks = customersocialnetworks.ToArray()
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As SetCustomerSocialNetworksResponse = api.SetCustomerSocialNetworks(req)

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

    //Add CustomerSocialNetworks

    $customerSocialNetwork1->SocialNetworkID = 1;
    $customerSocialNetwork1->Url = "1";

    $customerSocialNetwork2->SocialNetworkID = 2;
    $customerSocialNetwork2->Url = "2";

    //Now attach the list to the request
    req.CustomerSocialNetworks = array(customerSocialNetwork1,customerSocialNetwork2);
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.SetCustomerSocialNetworks($req);

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
    SetCustomerSocialNetworksRequest req = new SetCustomerSocialNetworksRequest();

    req.setCustomerID(1);

    //Add CustomerSocialNetworks
    ArrayOfCustomerSocialNetworkRequest customersocialnetworks = new ArrayOfCustomerSocialNetworkRequest();

    CustomerSocialNetworkRequest customerSocialNetwork1 = new CustomerSocialNetworkRequest();
    customerSocialNetwork1.setSocialNetworkID(1);
    customerSocialNetwork1.setUrl("1");
    customersocialnetworks.Add(customerSocialNetwork1);

    CustomerSocialNetworkRequest customerSocialNetwork2 = new CustomerSocialNetworkRequest();
    customerSocialNetwork2.setSocialNetworkID(2);
    customerSocialNetwork2.setUrl("2");
    customersocialnetworks.Add(customerSocialNetwork2);

    //Now attach the list to the request
    req.setCustomerSocialNetworks(customersocialnetworks);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    SetCustomerSocialNetworksResponse res = api.getExigoApiSoap().setCustomerSocialNetworks(req, auth);

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

### GetCustomerSocialNetworks

> Returns a list of social network(s) for the customer.

| | |
|---|---|
| Category | Customers |
| REST | `GET /3.0/customers/socialnetworks?customerID=1` |
| SOAP action | `https://api.exigo.com/GetCustomerSocialNetworks` |
| WSDL elements | `GetCustomerSocialNetworksRequest` → `GetCustomerSocialNetworksResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetCustomerSocialNetworks |

#### Input

**`GetCustomerSocialNetworksRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`GetCustomerSocialNetworksResponse`**

| Property | Type | Notes |
|---|---|---|
| `CustomerSocialNetwork` | `CustomerSocialNetworksResponse[]` |  |

**`CustomerSocialNetworksResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `SocialNetworkID` | `Int32` | Unique Social Network ID.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `SocialNetworkDescription` | `String` |  |
| &nbsp;&nbsp;↳ `Url` | `String` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/customers/socialnetworks?customerID=1
  &customerKey=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "customerSocialNetwork": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetCustomerSocialNetworks"

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
    <GetCustomerSocialNetworksRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
    </GetCustomerSocialNetworksRequest>
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
    <GetCustomerSocialNetworksResult xmlns="http://api.exigo.com/">
      <CustomerSocialNetwork>
        <CustomerSocialNetworksResponse>
          <SocialNetworkID>int</SocialNetworkID>
          <SocialNetworkDescription>string</SocialNetworkDescription>
          <Url>string</Url>
        </CustomerSocialNetworksResponse>
      </CustomerSocialNetwork>
    </GetCustomerSocialNetworksResult>
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
    var req = new GetCustomerSocialNetworksRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.GetCustomerSocialNetworksAsync(req);

    //Now examine the results:

    foreach (var customerSocialNetworks  in res.CustomerSocialNetwork)
    {
        Console.WriteLine("SocialNetworkDescription: {0}", customerSocialNetworks.SocialNetworkDescription);
        Console.WriteLine("Url: {0}", customerSocialNetworks.Url);
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
    GetCustomerSocialNetworksRequest req = new GetCustomerSocialNetworksRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    GetCustomerSocialNetworksResponse res = api.GetCustomerSocialNetworks(req);

    //Now examine the results:

    foreach (CustomerSocialNetworksResponse customerSocialNetworks  in res.CustomerSocialNetwork)
    {
        Console.WriteLine("SocialNetworkDescription: {0}", customerSocialNetworks.SocialNetworkDescription);
        Console.WriteLine("Url: {0}", customerSocialNetworks.Url);
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
    Dim req as new GetCustomerSocialNetworksRequest()

    req.CustomerID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As GetCustomerSocialNetworksResponse = api.GetCustomerSocialNetworks(req)

    'Now examine the results:

    For Each customerSocialNetworks As CustomerSocialNetworksResponse In res.CustomerSocialNetwork
        Console.WriteLine("SocialNetworkDescription: {0}", customerSocialNetworks.SocialNetworkDescription)
        Console.WriteLine("Url: {0}", customerSocialNetworks.Url)
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
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.GetCustomerSocialNetworks($req);

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
    GetCustomerSocialNetworksRequest req = new GetCustomerSocialNetworksRequest();

    req.setCustomerID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    GetCustomerSocialNetworksResponse res = api.getExigoApiSoap().getCustomerSocialNetworks(req, auth);

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

### GetCustomerWall

> Get wall item(s) from CustomerWall table.

| | |
|---|---|
| Category | Customers |
| REST | `GET /3.0/customers/wall?customerID=1` |
| SOAP action | `https://api.exigo.com/GetCustomerWall` |
| WSDL elements | `GetCustomerWallRequest` → `GetCustomerWallResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetCustomerWall |

#### Input

**`GetCustomerWallRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `WallItemID` | `Int32` | Optional. Identifier for a single wall item. |
| `OlderThanEntryDate` | `DateTime` | Optional. Filter for wall item(s) older than the provided date. |
| `BatchSize` | `Int32` | Optional. Defaults to 100 at a time. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`GetCustomerWallResponse`**

| Property | Type | Notes |
|---|---|---|
| `CustomerWallItems` | `CustomerWallItemResponse[]` |  |

**`CustomerWallItemResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| &nbsp;&nbsp;↳ `WallItemID` | `Int32` | Unique identifier for a customer wall item. |
| &nbsp;&nbsp;↳ `Text` | `String` | Text for wall item. |
| &nbsp;&nbsp;↳ `EntryDate` | `DateTime` | Entry date for wall item. |
| &nbsp;&nbsp;↳ `Field1` | `String` |  |
| &nbsp;&nbsp;↳ `Field2` | `String` |  |
| &nbsp;&nbsp;↳ `Field3` | `String` |  |
| &nbsp;&nbsp;↳ `CustomerKey` | `String` | Unique alpha numeric identifier for customer record . |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/customers/wall?customerID=1
  &wallItemID=1
  &customerKey=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "customerWallItems": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetCustomerWall"

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
    <GetCustomerWallRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <WallItemID>int</WallItemID>
      <OlderThanEntryDate>dateTime</OlderThanEntryDate>
      <BatchSize>int</BatchSize>
      <CustomerKey>string</CustomerKey>
    </GetCustomerWallRequest>
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
    <GetCustomerWallResult xmlns="http://api.exigo.com/">
      <CustomerWallItems>
        <CustomerWallItemResponse>
          <CustomerID>int</CustomerID>
          <WallItemID>int</WallItemID>
          <Text>string</Text>
          <EntryDate>dateTime</EntryDate>
          <Field1>string</Field1>
          <Field2>string</Field2>
          <Field3>string</Field3>
          <CustomerKey>string</CustomerKey>
        </CustomerWallItemResponse>
      </CustomerWallItems>
    </GetCustomerWallResult>
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
    var req = new GetCustomerWallRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.WallItemID = 1;             //Identifier for a single wall item
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.GetCustomerWallAsync(req);

    //Now examine the results:

    foreach (var customerWallItem  in res.CustomerWallItems)
    {
        Console.WriteLine("CustomerID: {0}", customerWallItem.CustomerID);
        Console.WriteLine("WallItemID: {0}", customerWallItem.WallItemID);
        Console.WriteLine("Text: {0}", customerWallItem.Text);
        Console.WriteLine("EntryDate: {0}", customerWallItem.EntryDate);
        Console.WriteLine("Field1: {0}", customerWallItem.Field1);
        Console.WriteLine("Field2: {0}", customerWallItem.Field2);
        Console.WriteLine("Field3: {0}", customerWallItem.Field3);
        Console.WriteLine("CustomerKey: {0}", customerWallItem.CustomerKey);
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
    GetCustomerWallRequest req = new GetCustomerWallRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.WallItemID = 1;             //Identifier for a single wall item
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    GetCustomerWallResponse res = api.GetCustomerWall(req);

    //Now examine the results:

    foreach (CustomerWallItemResponse customerWallItem  in res.CustomerWallItems)
    {
        Console.WriteLine("CustomerID: {0}", customerWallItem.CustomerID);
        Console.WriteLine("WallItemID: {0}", customerWallItem.WallItemID);
        Console.WriteLine("Text: {0}", customerWallItem.Text);
        Console.WriteLine("EntryDate: {0}", customerWallItem.EntryDate);
        Console.WriteLine("Field1: {0}", customerWallItem.Field1);
        Console.WriteLine("Field2: {0}", customerWallItem.Field2);
        Console.WriteLine("Field3: {0}", customerWallItem.Field3);
        Console.WriteLine("CustomerKey: {0}", customerWallItem.CustomerKey);
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
    Dim req as new GetCustomerWallRequest()

    req.CustomerID = 1
    req.WallItemID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As GetCustomerWallResponse = api.GetCustomerWall(req)

    'Now examine the results:

    For Each customerWallItem As CustomerWallItemResponse In res.CustomerWallItems
        Console.WriteLine("CustomerID: {0}", customerWallItem.CustomerID)
        Console.WriteLine("WallItemID: {0}", customerWallItem.WallItemID)
        Console.WriteLine("Text: {0}", customerWallItem.Text)
        Console.WriteLine("EntryDate: {0}", customerWallItem.EntryDate)
        Console.WriteLine("Field1: {0}", customerWallItem.Field1)
        Console.WriteLine("Field2: {0}", customerWallItem.Field2)
        Console.WriteLine("Field3: {0}", customerWallItem.Field3)
        Console.WriteLine("CustomerKey: {0}", customerWallItem.CustomerKey)
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
    $req->WallItemID = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.GetCustomerWall($req);

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
    GetCustomerWallRequest req = new GetCustomerWallRequest();

    req.setCustomerID(1);
    req.setWallItemID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    GetCustomerWallResponse res = api.getExigoApiSoap().getCustomerWall(req, auth);

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

### CreateCustomerWallItem

>  Create new wall item in CustomerWall table.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Customers |
| REST | `POST /3.0/customers/wall` |
| SOAP action | `https://api.exigo.com/CreateCustomerWallItem` |
| WSDL elements | `CreateCustomerWallItemRequest` → `CreateCustomerWallItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateCustomerWallItem |

#### Input

**`CreateCustomerWallItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `Text` | `String` | Text for new wall item. |
| `Field1` | `String` | Optional. |
| `Field2` | `String` | Optional. |
| `Field3` | `String` | Optional. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`CreateCustomerWallItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `WallItemID` | `Int32` | Unique identifier for new wall item. |
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Unique alpha numeric identifier for customer record . |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/customers/wall HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "text": "1",
  "field1": "1",
  "field2": "1",
  "field3": "1",
  "customerKey": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "wallItemID": 1,
  "customerID": 1,
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
SOAPAction: "https://api.exigo.com/CreateCustomerWallItem"

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
    <CreateCustomerWallItemRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <Text>string</Text>
      <Field1>string</Field1>
      <Field2>string</Field2>
      <Field3>string</Field3>
      <CustomerKey>string</CustomerKey>
    </CreateCustomerWallItemRequest>
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
    <CreateCustomerWallItemResult xmlns="http://api.exigo.com/">
      <WallItemID>int</WallItemID>
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
    </CreateCustomerWallItemResult>
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
    var req = new CreateCustomerWallItemRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.Text = "1";                 //Text for new wall item
    req.Field1 = "1";
    req.Field2 = "1";
    req.Field3 = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.CreateCustomerWallItemAsync(req);

    //Now examine the results:
    Console.WriteLine("WallItemID: {0}", res.WallItemID);
    Console.WriteLine("CustomerID: {0}", res.CustomerID);
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
    CreateCustomerWallItemRequest req = new CreateCustomerWallItemRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.Text = "1";                 //Text for new wall item
    req.Field1 = "1";
    req.Field2 = "1";
    req.Field3 = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    CreateCustomerWallItemResponse res = api.CreateCustomerWallItem(req);

    //Now examine the results:
    Console.WriteLine("WallItemID: {0}", res.WallItemID);
    Console.WriteLine("CustomerID: {0}", res.CustomerID);
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
    Dim req as new CreateCustomerWallItemRequest()

    req.CustomerID = 1
    req.Text = "1"
    req.Field1 = "1"
    req.Field2 = "1"
    req.Field3 = "1"
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As CreateCustomerWallItemResponse = api.CreateCustomerWallItem(req)

    'Now examine the results:
    Console.WriteLine("WallItemID: {0}", res.WallItemID)
    Console.WriteLine("CustomerID: {0}", res.CustomerID)
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
    $req->Text = "1";
    $req->Field1 = "1";
    $req->Field2 = "1";
    $req->Field3 = "1";
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.CreateCustomerWallItem($req);

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
    CreateCustomerWallItemRequest req = new CreateCustomerWallItemRequest();

    req.setCustomerID(1);
    req.setText("1");
    req.setField1("1");
    req.setField2("1");
    req.setField3("1");
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    CreateCustomerWallItemResponse res = api.getExigoApiSoap().createCustomerWallItem(req, auth);

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

### DeleteCustomerWallItem

> Delete wall item(s) from CustomerWall table.

| | |
|---|---|
| Category | Customers |
| REST | `DELETE /3.0/customers/wall` |
| SOAP action | `https://api.exigo.com/DeleteCustomerWallItem` |
| WSDL elements | `DeleteCustomerWallItemRequest` → `DeleteCustomerWallItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DeleteCustomerWallItem |

#### Input

**`DeleteCustomerWallItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `WallItemID` | `Int32` | Optional. Identifier for a single wall item. |
| `OlderThanEntryDate` | `DateTime` | Optional. Filter for wall item(s) older than date. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`DeleteCustomerWallItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `CountOfDeletedRows` | `Int32` | How many wall items were deleted. |

#### REST example

```http
DELETE https://yourcompany-api.exigo.com/3.0/customers/wall HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "wallItemID": 1,
  "olderThanEntryDate": "2026-11-10T00:00:00-06:00",
  "customerKey": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "countOfDeletedRows": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/DeleteCustomerWallItem"

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
    <DeleteCustomerWallItemRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <WallItemID>int</WallItemID>
      <OlderThanEntryDate>dateTime</OlderThanEntryDate>
      <CustomerKey>string</CustomerKey>
    </DeleteCustomerWallItemRequest>
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
    <DeleteCustomerWallItemResult xmlns="http://api.exigo.com/">
      <CountOfDeletedRows>int</CountOfDeletedRows>
    </DeleteCustomerWallItemResult>
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
    var req = new DeleteCustomerWallItemRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.WallItemID = 1;             //Identifier for a single wall item
    req.OlderThanEntryDate = DateTime.Today;     //Filter for wall item(s) older than date
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.DeleteCustomerWallItemAsync(req);

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
    DeleteCustomerWallItemRequest req = new DeleteCustomerWallItemRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.WallItemID = 1;             //Identifier for a single wall item
    req.OlderThanEntryDate = DateTime.Today;     //Filter for wall item(s) older than date
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    DeleteCustomerWallItemResponse res = api.DeleteCustomerWallItem(req);

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
    Dim req as new DeleteCustomerWallItemRequest()

    req.CustomerID = 1
    req.WallItemID = 1
    req.OlderThanEntryDate = DateTime.Today
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As DeleteCustomerWallItemResponse = api.DeleteCustomerWallItem(req)

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
    $req->WallItemID = 1;
    $req->OlderThanEntryDate = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.DeleteCustomerWallItem($req);

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
    DeleteCustomerWallItemRequest req = new DeleteCustomerWallItemRequest();

    req.setCustomerID(1);
    req.setWallItemID(1);
    req.setOlderThanEntryDate(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    DeleteCustomerWallItemResponse res = api.getExigoApiSoap().deleteCustomerWallItem(req, auth);

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

### CreateCustomerInquiry

> Creates a customer history record.

| | |
|---|---|
| Category | Customers |
| REST | `POST /3.0/customers/inquiry` |
| SOAP action | `https://api.exigo.com/CreateCustomerInquiry` |
| WSDL elements | `CreateCustomerInquiryRequest` → `CreateCustomerInquiryResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateCustomerInquiry |

#### Input

**`CreateCustomerInquiryRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `Detail` | `String` | Optional. |
| `Description` | `String` | Optional. |
| `AssignToUser` | `String` | The Exigo admin's login name that should be assigned this inquiry. |
| `CustomerInquiryStatusID` | `Int32` | Customer history/inquiry status type.<br>**Lookup:** company-specific list (see company-lists.md) |
| `CustomerInquiryCategoryID` | `Int32` | Customer history/inquiry category type.<br>**Lookup:** company-specific list (see company-lists.md) |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |
| `ParentID` | `Int32` | Optional. |

#### Output

**`CreateCustomerInquiryResponse`**

| Property | Type | Notes |
|---|---|---|
| `NewCustomerHistoryID` | `Int32` | Unique identifier for newly create customer history/inquiry record. |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/customers/inquiry HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "detail": "",
  "description": "",
  "assignToUser": "1",
  "customerInquiryStatusID": 1,
  "customerInquiryCategoryID": 1,
  "customerKey": "1",
  "parentID": 1
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "newCustomerHistoryID": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateCustomerInquiry"

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
    <CreateCustomerInquiryRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <Detail>string</Detail>
      <Description>string</Description>
      <AssignToUser>string</AssignToUser>
      <CustomerInquiryStatusID>int</CustomerInquiryStatusID>
      <CustomerInquiryCategoryID>int</CustomerInquiryCategoryID>
      <CustomerKey>string</CustomerKey>
      <ParentID>int</ParentID>
    </CreateCustomerInquiryRequest>
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
    <CreateCustomerInquiryResult xmlns="http://api.exigo.com/">
      <NewCustomerHistoryID>int</NewCustomerHistoryID>
    </CreateCustomerInquiryResult>
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
    var req = new CreateCustomerInquiryRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.Detail = "1";
    req.Description = "1";
    req.AssignToUser = "1";         //The Exigo admin's login name that should be assigned this inquiry
    req.CustomerInquiryStatusID = 1;//Customer history/inquiry status type
    req.CustomerInquiryCategoryID = 1;//Customer history/inquiry category type
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.ParentID = 1;

    //Send Request to Server and Get Response
    var res = await api.CreateCustomerInquiryAsync(req);

    //Now examine the results:
    Console.WriteLine("NewCustomerHistoryID: {0}", res.NewCustomerHistoryID);
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
    CreateCustomerInquiryRequest req = new CreateCustomerInquiryRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.Detail = "1";
    req.Description = "1";
    req.AssignToUser = "1";         //The Exigo admin's login name that should be assigned this inquiry
    req.CustomerInquiryStatusID = 1;//Customer history/inquiry status type
    req.CustomerInquiryCategoryID = 1;//Customer history/inquiry category type
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.ParentID = 1;

    //Send Request to Server and Get Response
    CreateCustomerInquiryResponse res = api.CreateCustomerInquiry(req);

    //Now examine the results:
    Console.WriteLine("NewCustomerHistoryID: {0}", res.NewCustomerHistoryID);
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
    Dim req as new CreateCustomerInquiryRequest()

    req.CustomerID = 1
    req.Detail = "1"
    req.Description = "1"
    req.AssignToUser = "1"
    req.CustomerInquiryStatusID = 1
    req.CustomerInquiryCategoryID = 1
    req.CustomerKey = "1"
    req.ParentID = 1

    'Send Request to Server and Get Response
    Dim res As CreateCustomerInquiryResponse = api.CreateCustomerInquiry(req)

    'Now examine the results:
    Console.WriteLine("NewCustomerHistoryID: {0}", res.NewCustomerHistoryID)
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
    $req->Detail = "1";
    $req->Description = "1";
    $req->AssignToUser = "1";
    $req->CustomerInquiryStatusID = 1;
    $req->CustomerInquiryCategoryID = 1;
    $req->CustomerKey = "1";
    $req->ParentID = 1;

    //Send Request to Server and Get Response
    $res = $api.CreateCustomerInquiry($req);

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
    CreateCustomerInquiryRequest req = new CreateCustomerInquiryRequest();

    req.setCustomerID(1);
    req.setDetail("1");
    req.setDescription("1");
    req.setAssignToUser("1");
    req.setCustomerInquiryStatusID(1);
    req.setCustomerInquiryCategoryID(1);
    req.setCustomerKey("1");
    req.setParentID(1);

    //Send Request to Server and Get Response
    CreateCustomerInquiryResponse res = api.getExigoApiSoap().createCustomerInquiry(req, auth);

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

### DequeueCustomerEvents

> This will 'pop' the oldest 100 customer events off the event queue.

| | |
|---|---|
| Category | Customers |
| REST | `POST /3.0/customers/events` |
| SOAP action | `https://api.exigo.com/DequeueCustomerEvents` |
| WSDL elements | `DequeuCustomerEventsRequest` → `DequeueCustomerEventsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DequeueCustomerEvents |

#### Input

**`DequeueCustomerEventsRequest`**

_No properties._

#### Output

**`DequeueCustomerEventsResponse`**

| Property | Type | Notes |
|---|---|---|
| `CustomerEvents` | `CustomerEventResponse[]` |  |

**`CustomerEventResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `EventID` | `Int32` |  |
| &nbsp;&nbsp;↳ `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| &nbsp;&nbsp;↳ `EventDescription` | `String` |  |
| &nbsp;&nbsp;↳ `Fields` | `CustomerEventField[]` |  |
| &nbsp;&nbsp;↳ `EventDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `CustomerKey` | `String` | Unique alpha numeric identifier for customer record . |

**`CustomerEventField`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Name` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Value` | `Int32` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/customers/events HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "customerEvents": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/DequeueCustomerEvents"

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
    <DequeuCustomerEventsRequest xmlns="http://api.exigo.com/" />
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
    <DequeueCustomerEventsResult xmlns="http://api.exigo.com/">
      <CustomerEvents>
        <CustomerEventResponse>
          <EventID>int</EventID>
          <CustomerID>int</CustomerID>
          <EventDescription>string</EventDescription>
          <Fields>
            <CustomerEventField>
              <Name>string</Name>
              <Value>int</Value>
            </CustomerEventField>
          </Fields>
          <EventDate>dateTime</EventDate>
          <CustomerKey>string</CustomerKey>
        </CustomerEventResponse>
      </CustomerEvents>
    </DequeueCustomerEventsResult>
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
    var req = new DequeueCustomerEventsRequest();

    //Send Request to Server and Get Response
    var res = await api.DequeueCustomerEventsAsync(req);

    //Now examine the results:

    foreach (var customerEvent  in res.CustomerEvents)
    {
        Console.WriteLine("EventID: {0}", customerEvent.EventID);
        Console.WriteLine("CustomerID: {0}", customerEvent.CustomerID);
        Console.WriteLine("EventDescription: {0}", customerEvent.EventDescription);

        foreach (var customerEventField  in customerEvent.Fields)
        {
            Console.WriteLine("Name: {0}", customerEventField.Name);
            Console.WriteLine("Value: {0}", customerEventField.Value);
        }
        Console.WriteLine("EventDate: {0}", customerEvent.EventDate);
        Console.WriteLine("CustomerKey: {0}", customerEvent.CustomerKey);
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
    DequeueCustomerEventsRequest req = new DequeueCustomerEventsRequest();

    //Send Request to Server and Get Response
    DequeueCustomerEventsResponse res = api.DequeueCustomerEvents(req);

    //Now examine the results:

    foreach (CustomerEventResponse customerEvent  in res.CustomerEvents)
    {
        Console.WriteLine("EventID: {0}", customerEvent.EventID);
        Console.WriteLine("CustomerID: {0}", customerEvent.CustomerID);
        Console.WriteLine("EventDescription: {0}", customerEvent.EventDescription);

        foreach (CustomerEventField customerEventField  in customerEvent.Fields)
        {
            Console.WriteLine("Name: {0}", customerEventField.Name);
            Console.WriteLine("Value: {0}", customerEventField.Value);
        }
        Console.WriteLine("EventDate: {0}", customerEvent.EventDate);
        Console.WriteLine("CustomerKey: {0}", customerEvent.CustomerKey);
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
    Dim req as new DequeueCustomerEventsRequest()

    'Send Request to Server and Get Response
    Dim res As DequeueCustomerEventsResponse = api.DequeueCustomerEvents(req)

    'Now examine the results:

    For Each customerEvent As CustomerEventResponse In res.CustomerEvents
        Console.WriteLine("EventID: {0}", customerEvent.EventID)
        Console.WriteLine("CustomerID: {0}", customerEvent.CustomerID)
        Console.WriteLine("EventDescription: {0}", customerEvent.EventDescription)

        For Each customerEventField As CustomerEventField In customerEvent.Fields
            Console.WriteLine("Name: {0}", customerEventField.Name)
            Console.WriteLine("Value: {0}", customerEventField.Value)
        Next
        Console.WriteLine("EventDate: {0}", customerEvent.EventDate)
        Console.WriteLine("CustomerKey: {0}", customerEvent.CustomerKey)
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
    $res = $api.DequeueCustomerEvents($req);

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
    DequeueCustomerEventsRequest req = new DequeueCustomerEventsRequest();

    //Send Request to Server and Get Response
    DequeueCustomerEventsResponse res = api.getExigoApiSoap().dequeueCustomerEvents(req, auth);

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

### CreateSilentLoginCipher

> Creates backoffice silent login authentication cipher

| | |
|---|---|
| Category | Customers |
| REST | `GET /3.0/customers/createsilentlogincipher?silentLoginKey=1` |
| SOAP action | `https://api.exigo.com/CreateSilentLoginCipher` |
| WSDL elements | `silentLoginCipherRequest` → `CreateSilentLoginCipherResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateSilentLoginCipher |

#### Input

**`CreateSilentLoginCipherRequest`**

| Property | Type | Notes |
|---|---|---|
| `SilentLoginKey` | `String` | Silent login key. |
| `CustomerID` | `Int32` | Optional. Unique numeric identifier for customer record. Defaults to 0. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exception will occur if CustomerID & CustomerKey are provided. |
| `UserID` | `String` | Unique alpha numeric identifier which represents the external calling user identifier. |
| `Route` | `String` | Optional. Optional route to redirect to once authenticated. |

#### Output

**`CreateSilentLoginCipherResponse`**

| Property | Type | Notes |
|---|---|---|
| `SilentLoginCipher` | `String` | Silent Login Cipher. |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/customers/createsilentlogincipher?silentLoginKey=1
  &customerID=1
  &customerKey=1
  &userID=1
  &route=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "silentLoginCipher": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateSilentLoginCipher"

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
    <silentLoginCipherRequest xmlns="http://api.exigo.com/">
      <SilentLoginKey>string</SilentLoginKey>
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
      <UserID>string</UserID>
      <Route>string</Route>
    </silentLoginCipherRequest>
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
    <CreateSilentLoginCipherResult xmlns="http://api.exigo.com/">
      <SilentLoginCipher>string</SilentLoginCipher>
    </CreateSilentLoginCipherResult>
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
    var req = new CreateSilentLoginCipherRequest();

    req.SilentLoginKey = "1";       //Silent login key.
    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exception will occur if CustomerID & CustomerKey are provided.
    req.UserID = "1";               //Unique alpha numeric identifier which represents the external calling user identifier.
    req.Route = "1";                //Optional route to redirect to once authenticated.

    //Send Request to Server and Get Response
    var res = await api.CreateSilentLoginCipherAsync(req);

    //Now examine the results:
    Console.WriteLine("SilentLoginCipher: {0}", res.SilentLoginCipher);
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
    CreateSilentLoginCipherRequest req = new CreateSilentLoginCipherRequest();

    req.SilentLoginKey = "1";       //Silent login key.
    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exception will occur if CustomerID & CustomerKey are provided.
    req.UserID = "1";               //Unique alpha numeric identifier which represents the external calling user identifier.
    req.Route = "1";                //Optional route to redirect to once authenticated.

    //Send Request to Server and Get Response
    CreateSilentLoginCipherResponse res = api.CreateSilentLoginCipher(req);

    //Now examine the results:
    Console.WriteLine("SilentLoginCipher: {0}", res.SilentLoginCipher);
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
    Dim req as new CreateSilentLoginCipherRequest()

    req.SilentLoginKey = "1"
    req.CustomerID = 1
    req.CustomerKey = "1"
    req.UserID = "1"
    req.Route = "1"

    'Send Request to Server and Get Response
    Dim res As CreateSilentLoginCipherResponse = api.CreateSilentLoginCipher(req)

    'Now examine the results:
    Console.WriteLine("SilentLoginCipher: {0}", res.SilentLoginCipher)
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

    $req->SilentLoginKey = "1";
    $req->CustomerID = 1;
    $req->CustomerKey = "1";
    $req->UserID = "1";
    $req->Route = "1";

    //Send Request to Server and Get Response
    $res = $api.CreateSilentLoginCipher($req);

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
    CreateSilentLoginCipherRequest req = new CreateSilentLoginCipherRequest();

    req.setSilentLoginKey("1");
    req.setCustomerID(1);
    req.setCustomerKey("1");
    req.setUserID("1");
    req.setRoute("1");

    //Send Request to Server and Get Response
    CreateSilentLoginCipherResponse res = api.getExigoApiSoap().createSilentLoginCipher(req, auth);

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

### TerminateCustomer

> Terminates a Customer

| | |
|---|---|
| Category | Customers |
| REST | `POST /3.0/customers/terminate` |
| SOAP action | `https://api.exigo.com/TerminateCustomer` |
| WSDL elements | `TerminateCustomerRequest` → `TerminateCustomerResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=TerminateCustomer |

#### Input

**`TerminateCustomerRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |
| `AgreedToTerminate` | `Boolean` | Flag to begin termination. |
| `TerminationSettingID` | `Int32` | Optional. Unique numeric identifier for the termination setting profile to use, if not set default profile will be used.<br>**Lookup:** company-specific list (see company-lists.md) |

#### Output

**`TerminateCustomerResponse`**

_No properties._

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/customers/terminate HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerKey": "1",
  "agreedToTerminate": true
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
SOAPAction: "https://api.exigo.com/TerminateCustomer"

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
    <TerminateCustomerRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
      <AgreedToTerminate>boolean</AgreedToTerminate>
      <TerminationSettingID>int</TerminationSettingID>
    </TerminateCustomerRequest>
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
    <TerminateCustomerResult xmlns="http://api.exigo.com/" />
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
    var req = new TerminateCustomerRequest();

    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.AgreedToTerminate = true;      //Flag to begin termination

    //Send Request to Server and Get Response
    var res = await api.TerminateCustomerAsync(req);

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
    TerminateCustomerRequest req = new TerminateCustomerRequest();

    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.AgreedToTerminate = true;      //Flag to begin termination

    //Send Request to Server and Get Response
    TerminateCustomerResponse res = api.TerminateCustomer(req);

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
    Dim req as new TerminateCustomerRequest()

    req.CustomerKey = "1"
    req.AgreedToTerminate = true

    'Send Request to Server and Get Response
    Dim res As TerminateCustomerResponse = api.TerminateCustomer(req)

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

    $req->CustomerKey = "1";
    $req->AgreedToTerminate = 1;

    //Send Request to Server and Get Response
    $res = $api.TerminateCustomer($req);

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
    TerminateCustomerRequest req = new TerminateCustomerRequest();

    req.setCustomerKey("1");
    req.setAgreedToTerminate(1);

    //Send Request to Server and Get Response
    TerminateCustomerResponse res = api.getExigoApiSoap().terminateCustomer(req, auth);

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
