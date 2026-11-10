# Exigo API — Unlisted (WSDL only)

API version v2025.11.7.6. Crawled 2026-11-11 from https://api.exigo.com/3.0/. Back to [index](../README.md).

These operations exist in the WSDL and have full method pages, but are **not linked from the docs menu**. They may be internal, legacy or limited to specific companies. Confirm with Exigo before relying on them.

| Operation | REST | Summary |
|---|---|---|
| [ChargeCreditCard](#chargecreditcard) | SOAP only | Deprecated. Use ChargeCreditCardToken instead. |
| [ChargeCreditCardOnFile](#chargecreditcardonfile) | SOAP only | Deprecated. Use ChargeCreditCardTokenOnFile instead. |
| [CreateCustomerContact](#createcustomercontact) | SOAP only | Creates a new customer contact. Note: This request can participate in a transaction. Learn more about transactions. |
| [CreateEmail](#createemail) | SOAP only | Creates an email. Note: This request can participate in a transaction. Learn more about transactions. |
| [CreateEmailTemplate](#createemailtemplate) | SOAP only | Creates an email template. Note: This request can participate in a transaction. Learn more about transactions. |
| [CreateMailFolder](#createmailfolder) | SOAP only | Creates a mail folder. Note: This request can participate in a transaction. Learn more about transactions. |
| [CreateOrderDetail](#createorderdetail) | SOAP only | Create a new Order Detail for an existing order without recalculating. Can participate in a transaction. Note: This request can participate in a transaction. Learn more about… |
| [CreatePayout](#createpayout) | `POST /3.0/payout` | Creates a new payout for one or more bills and updates status |
| [CreateVendorBill](#createvendorbill) | SOAP only | Creates a new VendorBill for a customer on file. |
| [DeleteCustomerContact](#deletecustomercontact) | SOAP only | Deletes a customer contact. Note: This request can participate in a transaction. Learn more about transactions. |
| [DeleteEmail](#deleteemail) | SOAP only | Deletes an email forever. Note: This request can participate in a transaction. Learn more about transactions. |
| [DeleteEmailTemplate](#deleteemailtemplate) | SOAP only | Deletes an email template. Note: This request can participate in a transaction. Learn more about transactions. |
| [DeleteMailFolder](#deletemailfolder) | SOAP only | Deletes a mail folder. Note: This request can participate in a transaction. Learn more about transactions. |
| [DeleteOrderDetail](#deleteorderdetail) | SOAP only | Delete an existing Order Detail for an existing order without recalculating. Can participate in a transaction. Note: This request can participate in a transaction. Learn more… |
| [EmptyMailFolder](#emptymailfolder) | SOAP only | Deletes all emails from a folder. Note: This request can participate in a transaction. Learn more about transactions. |
| [EnsureMailFolders](#ensuremailfolders) | SOAP only | Ensures all the basic mail folders exist. Note: This request can participate in a transaction. Learn more about transactions. |
| [FundPaymentCard](#fundpaymentcard) | `POST /3.0/payout/fund` | Creates a new payout and funds a payment card for one or more bills and updates status |
| [GetCompanyLanguages](#getcompanylanguages) | SOAP only | Gets languages list available to the company. |
| [GetEmailAttachment](#getemailattachment) | SOAP only | Gets an email attachment. Note: This request can participate in a transaction. Learn more about transactions. |
| [GetItemCountryRegion](#getitemcountryregion) | SOAP only | Returns item, country and region properties along with taxings for an item. |
| [GetLoginSession](#getloginsession) | SOAP only | Deprecated. Use AuthenticateCustomer instead. |
| [GetOrderTotals](#getordertotals) | SOAP only | Returns the totals of accepted orders within a date range |
| [GetPayments](#getpayments) | `GET /3.0/payment?customerID=1` | Gets payment record(s) for a customer or order. |
| [GetReport](#getreport) | SOAP only | Returns a custom report in dataset format. |
| [GetResourceSetSubscriptionUpdates](#getresourcesetsubscriptionupdates) | `GET /3.0/resourceset/subscriptions/updatesAuthorization:` | Gets all resource item updates for a list of resource subscriptions |
| [GetSandbox](#getsandbox) | SOAP only | Get List of Sandboxes |
| [GetShipMethods](#getshipmethods) | SOAP only | This has been deprecated. Use CalculateOrder with ReturnShipMethods=true instead. |
| [GetShoppingCart](#getshoppingcart) | SOAP only | Gets a existing Shopping Cart Session. |
| [LoginCustomer](#logincustomer) | SOAP only | Deprecated. Use AuthenticateCustomer instead. |
| [MergeCustomer](#mergecustomer) | SOAP only | Merges Order, Payments and AutoOrder data from two Customers |
| [MoveEmail](#moveemail) | SOAP only | Moves an email to a different folder. Note: This request can participate in a transaction. Learn more about transactions. |
| [Ping](#ping) | `POST /3.0/orders/calculate` | Ping to create a speed baseline |
| [PlaceStackNode](#placestacknode) | SOAP only | Inserts/Moves a customer within the Stack Tree. |
| [RefreshSandbox](#refreshsandbox) | SOAP only | Refresh a Sandbox |
| [SetAccountCreditCard](#setaccountcreditcard) | SOAP only | Setup primary or secondary credit card on file for an existing customer, or new customer in a transaction. Note: This request can participate in a transaction. Learn more about… |
| [SetImageFile](#setimagefile) | SOAP only | Set Images |
| [StartSandbox](#startsandbox) | SOAP only | Start a Sandbox |
| [StopSandbox](#stopsandbox) | SOAP only | Stop a Sandbox |
| [UpdateCustomerContact](#updatecustomercontact) | SOAP only | Updates customer contact information. Note: This request can participate in a transaction. Learn more about transactions. |
| [UpdateEmailStatus](#updateemailstatus) | SOAP only | Updates email's status. Note: This request can participate in a transaction. Learn more about transactions. |
| [UpdateEmailTemplate](#updateemailtemplate) | SOAP only | Updates an email template. Note: This request can participate in a transaction. Learn more about transactions. |
| [UpdateMailFolder](#updatemailfolder) | SOAP only | Updates a mail folder. Note: This request can participate in a transaction. Learn more about transactions. |

---
### ChargeCreditCard

> Deprecated. Use ChargeCreditCardToken instead.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/ChargeCreditCard` |
| WSDL elements | `ChargeCreditCardRequest` → `ChargeCreditCardResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=ChargeCreditCard |

#### Input

**`ChargeCreditCardRequest`**

| Property | Type | Notes |
|---|---|---|
| `CreditCardNumber` | `String` | Optional. |
| `ExpirationMonth` | `Int32` |  |
| `ExpirationYear` | `Int32` |  |
| `BillingName` | `String` | Optional. |
| `BillingAddress` | `String` | Optional. |
| `BillingAddress2` | `String` | Optional. |
| `BillingCity` | `String` | Optional. |
| `BillingState` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `BillingZip` | `String` | Optional. |
| `BillingCountry` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `CvcCode` | `String` | Optional. |
| `IssueNumber` | `String` | Optional. |
| `CreditCardType` | `Int32` | Optional. Optionally pass in Visa, Master Card, etc.<br>**Lookup:** company-specific list (see company-lists.md) |
| `OrderID` | `Int32` | Unique numeric identifier for order record. |
| `MaxAmount` | `Decimal` | Optional. Only use if you are applying multiple payments. |
| `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided. |

#### Output

**`ChargeCreditCardResponse`**

| Property | Type | Notes |
|---|---|---|
| `Amount` | `Decimal` |  |
| `AuthorizationCode` | `String` |  |
| `PaymentID` | `Int32` |  |
| `Message` | `String` |  |
| `DisplayMessage` | `String` |  |
| `MerchantTransactionKey` | `String` |  |

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/ChargeCreditCard"

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
  <soap:Body />
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
  <soap:Body />
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
    var req = new ChargeCreditCardRequest();

    req.CreditCardNumber = "1";
    req.ExpirationMonth = 1;
    req.ExpirationYear = 1;
    req.BillingName = "1";
    req.BillingAddress = "1";
    req.BillingAddress2 = "1";
    req.BillingCity = "1";
    req.BillingZip = "1";
    req.CvcCode = "1";
    req.IssueNumber = "1";
    req.OrderID = 1;                //Unique numeric identifier for order record.
    req.OrderKey = "DDks8235txcid"; //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    var res = await api.ChargeCreditCardAsync(req);

    //Now examine the results:
    Console.WriteLine("Amount: {0}", res.Amount);
    Console.WriteLine("AuthorizationCode: {0}", res.AuthorizationCode);
    Console.WriteLine("PaymentID: {0}", res.PaymentID);
    Console.WriteLine("Message: {0}", res.Message);
    Console.WriteLine("DisplayMessage: {0}", res.DisplayMessage);
    Console.WriteLine("MerchantTransactionKey: {0}", res.MerchantTransactionKey);
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
    ChargeCreditCardRequest req = new ChargeCreditCardRequest();

    req.CreditCardNumber = "1";
    req.ExpirationMonth = 1;
    req.ExpirationYear = 1;
    req.BillingName = "1";
    req.BillingAddress = "1";
    req.BillingAddress2 = "1";
    req.BillingCity = "1";
    req.BillingZip = "1";
    req.CvcCode = "1";
    req.IssueNumber = "1";
    req.OrderID = 1;                //Unique numeric identifier for order record.
    req.OrderKey = "DDks8235txcid"; //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    ChargeCreditCardResponse res = api.ChargeCreditCard(req);

    //Now examine the results:
    Console.WriteLine("Amount: {0}", res.Amount);
    Console.WriteLine("AuthorizationCode: {0}", res.AuthorizationCode);
    Console.WriteLine("PaymentID: {0}", res.PaymentID);
    Console.WriteLine("Message: {0}", res.Message);
    Console.WriteLine("DisplayMessage: {0}", res.DisplayMessage);
    Console.WriteLine("MerchantTransactionKey: {0}", res.MerchantTransactionKey);
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
    Dim req as new ChargeCreditCardRequest()

    req.CreditCardNumber = "1"
    req.ExpirationMonth = 1
    req.ExpirationYear = 1
    req.BillingName = "1"
    req.BillingAddress = "1"
    req.BillingAddress2 = "1"
    req.BillingCity = "1"
    req.BillingZip = "1"
    req.CvcCode = "1"
    req.IssueNumber = "1"
    req.OrderID = 1
    req.OrderKey = "DDks8235txcid"

    'Send Request to Server and Get Response
    Dim res As ChargeCreditCardResponse = api.ChargeCreditCard(req)

    'Now examine the results:
    Console.WriteLine("Amount: {0}", res.Amount)
    Console.WriteLine("AuthorizationCode: {0}", res.AuthorizationCode)
    Console.WriteLine("PaymentID: {0}", res.PaymentID)
    Console.WriteLine("Message: {0}", res.Message)
    Console.WriteLine("DisplayMessage: {0}", res.DisplayMessage)
    Console.WriteLine("MerchantTransactionKey: {0}", res.MerchantTransactionKey)
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

    $req->CreditCardNumber = "1";
    $req->ExpirationMonth = 1;
    $req->ExpirationYear = 1;
    $req->BillingName = "1";
    $req->BillingAddress = "1";
    $req->BillingAddress2 = "1";
    $req->BillingCity = "1";
    $req->BillingZip = "1";
    $req->CvcCode = "1";
    $req->IssueNumber = "1";
    $req->OrderID = 1;
    $req->OrderKey = "DDks8235txcid";

    //Send Request to Server and Get Response
    $res = $api.ChargeCreditCard($req);

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
    ChargeCreditCardRequest req = new ChargeCreditCardRequest();

    req.setCreditCardNumber("1");
    req.setExpirationMonth(1);
    req.setExpirationYear(1);
    req.setBillingName("1");
    req.setBillingAddress("1");
    req.setBillingAddress2("1");
    req.setBillingCity("1");
    req.setBillingZip("1");
    req.setCvcCode("1");
    req.setIssueNumber("1");
    req.setOrderID(1);
    req.setOrderKey("DDks8235txcid");

    //Send Request to Server and Get Response
    ChargeCreditCardResponse res = api.getExigoApiSoap().chargeCreditCard(req, auth);

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

### ChargeCreditCardOnFile

>  Deprecated. Use ChargeCreditCardTokenOnFile instead.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/ChargeCreditCardOnFile` |
| WSDL elements | `ChargeCreditCardOnFileRequest` → `ChargeCreditCardOnFileResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=ChargeCreditCardOnFile |

#### Input

**`ChargeCreditCardOnFileRequest`**

| Property | Type | Notes |
|---|---|---|
| `CreditCardAccountType` | `AccountCreditCardType` | **Values:** `Primary`, `Secondary` |
| `OrderID` | `Int32` | Unique numeric identifier for order record. |
| `MaxAmount` | `Decimal` | Optional. Only use if you are applying multiple payments. |
| `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided. |

#### Output

**`ChargeCreditCardResponse`**

| Property | Type | Notes |
|---|---|---|
| `Amount` | `Decimal` |  |
| `AuthorizationCode` | `String` |  |
| `PaymentID` | `Int32` |  |
| `Message` | `String` |  |
| `DisplayMessage` | `String` |  |
| `MerchantTransactionKey` | `String` |  |

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/ChargeCreditCardOnFile"

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
    <ChargeCreditCardOnFileRequest xmlns="http://api.exigo.com/">
      <CreditCardAccountType>Primary or Secondary</CreditCardAccountType>
      <OrderID>int</OrderID>
      <MaxAmount>decimal</MaxAmount>
      <OrderKey>string</OrderKey>
    </ChargeCreditCardOnFileRequest>
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
    <ChargeCreditCardOnFileResult xmlns="http://api.exigo.com/">
      <Amount>decimal</Amount>
      <AuthorizationCode>string</AuthorizationCode>
    </ChargeCreditCardOnFileResult>
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
    var req = new ChargeCreditCardOnFileRequest();

    req.CreditCardAccountType = AccountCreditCardType.Primary;
    req.OrderID = 1;                //Unique numeric identifier for order record.
    req.OrderKey = "DDks8235txcid"; //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    var res = await api.ChargeCreditCardOnFileAsync(req);

    //Now examine the results:
    Console.WriteLine("Amount: {0}", res.Amount);
    Console.WriteLine("AuthorizationCode: {0}", res.AuthorizationCode);
    Console.WriteLine("PaymentID: {0}", res.PaymentID);
    Console.WriteLine("Message: {0}", res.Message);
    Console.WriteLine("DisplayMessage: {0}", res.DisplayMessage);
    Console.WriteLine("MerchantTransactionKey: {0}", res.MerchantTransactionKey);
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
    ChargeCreditCardOnFileRequest req = new ChargeCreditCardOnFileRequest();

    req.CreditCardAccountType = AccountCreditCardType.Primary;
    req.OrderID = 1;                //Unique numeric identifier for order record.
    req.OrderKey = "DDks8235txcid"; //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    ChargeCreditCardResponse res = api.ChargeCreditCardOnFile(req);

    //Now examine the results:
    Console.WriteLine("Amount: {0}", res.Amount);
    Console.WriteLine("AuthorizationCode: {0}", res.AuthorizationCode);
    Console.WriteLine("PaymentID: {0}", res.PaymentID);
    Console.WriteLine("Message: {0}", res.Message);
    Console.WriteLine("DisplayMessage: {0}", res.DisplayMessage);
    Console.WriteLine("MerchantTransactionKey: {0}", res.MerchantTransactionKey);
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
    Dim req as new ChargeCreditCardOnFileRequest()

    req.CreditCardAccountType = AccountCreditCardType.Primary
    req.OrderID = 1
    req.OrderKey = "DDks8235txcid"

    'Send Request to Server and Get Response
    Dim res As ChargeCreditCardResponse = api.ChargeCreditCardOnFile(req)

    'Now examine the results:
    Console.WriteLine("Amount: {0}", res.Amount)
    Console.WriteLine("AuthorizationCode: {0}", res.AuthorizationCode)
    Console.WriteLine("PaymentID: {0}", res.PaymentID)
    Console.WriteLine("Message: {0}", res.Message)
    Console.WriteLine("DisplayMessage: {0}", res.DisplayMessage)
    Console.WriteLine("MerchantTransactionKey: {0}", res.MerchantTransactionKey)
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

    $req->CreditCardAccountType = 1;
    $req->OrderID = 1;
    $req->OrderKey = "DDks8235txcid";

    //Send Request to Server and Get Response
    $res = $api.ChargeCreditCardOnFile($req);

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
    ChargeCreditCardOnFileRequest req = new ChargeCreditCardOnFileRequest();

    req.setCreditCardAccountType(1);
    req.setOrderID(1);
    req.setOrderKey("DDks8235txcid");

    //Send Request to Server and Get Response
    ChargeCreditCardResponse res = api.getExigoApiSoap().chargeCreditCardOnFile(req, auth);

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

### CreateCustomerContact

> Creates a new customer contact.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/CreateCustomerContact` |
| WSDL elements | `CreateCustomerContactRequest` → `CreateCustomerContactResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateCustomerContact |

#### Input

**`CreateCustomerContactRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `FirstName` | `String` | Optional. |
| `LastName` | `String` | Optional. |
| `MiddleName` | `String` | Optional. |
| `Company` | `String` | Optional. |
| `BusinessPhone` | `String` | Optional. |
| `HomePhone` | `String` | Optional. |
| `Mobile` | `String` | Optional. |
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
| `LinkedIn` | `String` | Optional. |
| `Facebook` | `String` | Optional. |
| `Blog` | `String` | Optional. |
| `MySpace` | `String` | Optional. |
| `GooglePlus` | `String` | Optional. |
| `Twitter` | `String` | Optional. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`CreateCustomerContactResponse`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerContactID` | `Int32` |  |
| `CustomerKey` | `String` | Unique alpha numeric identifier for customer record . |

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateCustomerContact"

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
    <CreateCustomerContactRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <FirstName>string</FirstName>
      <LastName>string</LastName>
      <MiddleName>string</MiddleName>
      <Company>string</Company>
      <BusinessPhone>string</BusinessPhone>
      <HomePhone>string</HomePhone>
      <Mobile>string</Mobile>
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
      <LinkedIn>string</LinkedIn>
      <Facebook>string</Facebook>
      <Blog>string</Blog>
      <MySpace>string</MySpace>
      <GooglePlus>string</GooglePlus>
      <Twitter>string</Twitter>
      <CustomerKey>string</CustomerKey>
    </CreateCustomerContactRequest>
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
    <CreateCustomerContactResult xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerContactID>int</CustomerContactID>
      <CustomerKey>string</CustomerKey>
    </CreateCustomerContactResult>
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
    var req = new CreateCustomerContactRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.FirstName = "1";
    req.LastName = "1";
    req.MiddleName = "1";
    req.Company = "1";
    req.BusinessPhone = "1";
    req.HomePhone = "1";
    req.Mobile = "1";
    req.Fax = "1";
    req.Email = "1";
    req.Address1 = "1";
    req.Address2 = "1";
    req.City = "1";
    req.Zip = "1";
    req.BirthDate = DateTime.Today;
    req.Notes = "1";
    req.LinkedIn = "1";
    req.Facebook = "1";
    req.Blog = "1";
    req.MySpace = "1";
    req.GooglePlus = "1";
    req.Twitter = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.CreateCustomerContactAsync(req);

    //Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID);
    Console.WriteLine("CustomerContactID: {0}", res.CustomerContactID);
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
    CreateCustomerContactRequest req = new CreateCustomerContactRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.FirstName = "1";
    req.LastName = "1";
    req.MiddleName = "1";
    req.Company = "1";
    req.BusinessPhone = "1";
    req.HomePhone = "1";
    req.Mobile = "1";
    req.Fax = "1";
    req.Email = "1";
    req.Address1 = "1";
    req.Address2 = "1";
    req.City = "1";
    req.Zip = "1";
    req.BirthDate = DateTime.Today;
    req.Notes = "1";
    req.LinkedIn = "1";
    req.Facebook = "1";
    req.Blog = "1";
    req.MySpace = "1";
    req.GooglePlus = "1";
    req.Twitter = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    CreateCustomerContactResponse res = api.CreateCustomerContact(req);

    //Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID);
    Console.WriteLine("CustomerContactID: {0}", res.CustomerContactID);
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
    Dim req as new CreateCustomerContactRequest()

    req.CustomerID = 1
    req.FirstName = "1"
    req.LastName = "1"
    req.MiddleName = "1"
    req.Company = "1"
    req.BusinessPhone = "1"
    req.HomePhone = "1"
    req.Mobile = "1"
    req.Fax = "1"
    req.Email = "1"
    req.Address1 = "1"
    req.Address2 = "1"
    req.City = "1"
    req.Zip = "1"
    req.BirthDate = DateTime.Today
    req.Notes = "1"
    req.LinkedIn = "1"
    req.Facebook = "1"
    req.Blog = "1"
    req.MySpace = "1"
    req.GooglePlus = "1"
    req.Twitter = "1"
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As CreateCustomerContactResponse = api.CreateCustomerContact(req)

    'Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID)
    Console.WriteLine("CustomerContactID: {0}", res.CustomerContactID)
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
    $req->FirstName = "1";
    $req->LastName = "1";
    $req->MiddleName = "1";
    $req->Company = "1";
    $req->BusinessPhone = "1";
    $req->HomePhone = "1";
    $req->Mobile = "1";
    $req->Fax = "1";
    $req->Email = "1";
    $req->Address1 = "1";
    $req->Address2 = "1";
    $req->City = "1";
    $req->Zip = "1";
    $req->BirthDate = 1;
    $req->Notes = "1";
    $req->LinkedIn = "1";
    $req->Facebook = "1";
    $req->Blog = "1";
    $req->MySpace = "1";
    $req->GooglePlus = "1";
    $req->Twitter = "1";
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.CreateCustomerContact($req);

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
    CreateCustomerContactRequest req = new CreateCustomerContactRequest();

    req.setCustomerID(1);
    req.setFirstName("1");
    req.setLastName("1");
    req.setMiddleName("1");
    req.setCompany("1");
    req.setBusinessPhone("1");
    req.setHomePhone("1");
    req.setMobile("1");
    req.setFax("1");
    req.setEmail("1");
    req.setAddress1("1");
    req.setAddress2("1");
    req.setCity("1");
    req.setZip("1");
    req.setBirthDate(1);
    req.setNotes("1");
    req.setLinkedIn("1");
    req.setFacebook("1");
    req.setBlog("1");
    req.setMySpace("1");
    req.setGooglePlus("1");
    req.setTwitter("1");
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    CreateCustomerContactResponse res = api.getExigoApiSoap().createCustomerContact(req, auth);

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

### CreateEmail

> Creates an email.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/CreateEmail` |
| WSDL elements | `CreateEmailRequest` → `CreateEmailResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateEmail |

#### Input

**`CreateEmailRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `MailFolderType` | `MailForderType` | **Values:** `SubFolder`, `Inbox`, `SentItems`, `Drafts`, `DeletedItems`, `JunkMail`, `FaxInbox`, `SentFaxes`, `PersonalFolders` |
| `Priority` | `MailPriority` | **Values:** `Low`, `Normal`, `High` |
| `MailStatusType` | `MailStatusType` | **Values:** `New`, `Read`, `Forwarded`, `Replied` |
| `Subject` | `String` | Optional. |
| `MailFrom` | `String` | Optional. |
| `MailTo` | `String` | Optional. |
| `ReplyTo` | `String` | Optional. |
| `MailCC` | `String` | Optional. |
| `MailBCC` | `String` | Optional. |
| `Content` | `String` | Optional. |
| `SmtpServer` | `String` | Optional. |
| `Attachments` | `EmailAttachment` | Optional. |
| `ForwardedAttachments` | `ForwardedAttachment` | Optional. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`CreateEmailResponse`**

_No properties._

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateEmail"

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
    <CreateEmailRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <MailFolderType>SubFolder or Inbox or SentItems or Drafts or DeletedItems or JunkMail or FaxInbox or SentFaxes or PersonalFolders</MailFolderType>
      <Priority>High or Low or Normal</Priority>
      <MailStatusType>New or Read or Forwarded or Replied</MailStatusType>
      <Subject>string</Subject>
      <MailFrom>string</MailFrom>
      <MailTo>string</MailTo>
      <ReplyTo>string</ReplyTo>
      <MailCC>string</MailCC>
      <MailBCC>string</MailBCC>
      <Content>string</Content>
      <SmtpServer>string</SmtpServer>
      <Attachments>
        <EmailAttachment>
          <BinaryData>base64Binary</BinaryData>
          <FileName>string</FileName>
          <ContentLength>int</ContentLength>
        </EmailAttachment>
      </Attachments>
      <ForwardedAttachments>
        <ForwardedAttachment>
          <MailID>int</MailID>
          <AttachmentID>int</AttachmentID>
        </ForwardedAttachment>
      </ForwardedAttachments>
      <CustomerKey>string</CustomerKey>
    </CreateEmailRequest>
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
    <CreateEmailResult xmlns="http://api.exigo.com/" />
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
    var req = new CreateEmailRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.MailFolderType = MailForderType.SubFolder;
    req.Priority = MailPriority.Low;
    req.MailStatusType = MailStatusType.New;
    req.Subject = "1";
    req.MailFrom = "1";
    req.MailTo = "1";
    req.ReplyTo = "1";
    req.MailCC = "1";
    req.MailBCC = "1";
    req.Content = "1";
    req.SmtpServer = "1";
    req.Attachments = 1;
    req.ForwardedAttachments = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.CreateEmailAsync(req);

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
    CreateEmailRequest req = new CreateEmailRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.MailFolderType = MailForderType.SubFolder;
    req.Priority = MailPriority.Low;
    req.MailStatusType = MailStatusType.New;
    req.Subject = "1";
    req.MailFrom = "1";
    req.MailTo = "1";
    req.ReplyTo = "1";
    req.MailCC = "1";
    req.MailBCC = "1";
    req.Content = "1";
    req.SmtpServer = "1";
    req.Attachments = 1;
    req.ForwardedAttachments = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    CreateEmailResponse res = api.CreateEmail(req);

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
    Dim req as new CreateEmailRequest()

    req.CustomerID = 1
    req.MailFolderType = MailForderType.SubFolder
    req.Priority = MailPriority.Low
    req.MailStatusType = MailStatusType.New
    req.Subject = "1"
    req.MailFrom = "1"
    req.MailTo = "1"
    req.ReplyTo = "1"
    req.MailCC = "1"
    req.MailBCC = "1"
    req.Content = "1"
    req.SmtpServer = "1"
    req.Attachments = 1
    req.ForwardedAttachments = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As CreateEmailResponse = api.CreateEmail(req)

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
    $req->MailFolderType = 1;
    $req->Priority = 1;
    $req->MailStatusType = 1;
    $req->Subject = "1";
    $req->MailFrom = "1";
    $req->MailTo = "1";
    $req->ReplyTo = "1";
    $req->MailCC = "1";
    $req->MailBCC = "1";
    $req->Content = "1";
    $req->SmtpServer = "1";
    $req->Attachments = 1;
    $req->ForwardedAttachments = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.CreateEmail($req);

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
    CreateEmailRequest req = new CreateEmailRequest();

    req.setCustomerID(1);
    req.setMailFolderType(1);
    req.setPriority(1);
    req.setMailStatusType(1);
    req.setSubject("1");
    req.setMailFrom("1");
    req.setMailTo("1");
    req.setReplyTo("1");
    req.setMailCC("1");
    req.setMailBCC("1");
    req.setContent("1");
    req.setSmtpServer("1");
    req.setAttachments(1);
    req.setForwardedAttachments(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    CreateEmailResponse res = api.getExigoApiSoap().createEmail(req, auth);

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

### CreateEmailTemplate

>  Creates an email template.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/CreateEmailTemplate` |
| WSDL elements | `CreateEmailTemplateRequest` → `CreateEmailTemplateResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateEmailTemplate |

#### Input

**`CreateEmailTemplateRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `Description` | `String` | Optional. |
| `Content` | `String` | Optional. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`CreateEmailTemplateResponse`**

| Property | Type | Notes |
|---|---|---|
| `TemplateID` | `Int32` |  |

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateEmailTemplate"

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
    <CreateEmailTemplateRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <Description>string</Description>
      <Content>string</Content>
      <CustomerKey>string</CustomerKey>
    </CreateEmailTemplateRequest>
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
    <CreateEmailTemplateResult xmlns="http://api.exigo.com/">
      <TemplateID>int</TemplateID>
    </CreateEmailTemplateResult>
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
    var req = new CreateEmailTemplateRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.Description = "1";
    req.Content = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.CreateEmailTemplateAsync(req);

    //Now examine the results:
    Console.WriteLine("TemplateID: {0}", res.TemplateID);
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
    CreateEmailTemplateRequest req = new CreateEmailTemplateRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.Description = "1";
    req.Content = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    CreateEmailTemplateResponse res = api.CreateEmailTemplate(req);

    //Now examine the results:
    Console.WriteLine("TemplateID: {0}", res.TemplateID);
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
    Dim req as new CreateEmailTemplateRequest()

    req.CustomerID = 1
    req.Description = "1"
    req.Content = "1"
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As CreateEmailTemplateResponse = api.CreateEmailTemplate(req)

    'Now examine the results:
    Console.WriteLine("TemplateID: {0}", res.TemplateID)
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
    $req->Description = "1";
    $req->Content = "1";
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.CreateEmailTemplate($req);

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
    CreateEmailTemplateRequest req = new CreateEmailTemplateRequest();

    req.setCustomerID(1);
    req.setDescription("1");
    req.setContent("1");
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    CreateEmailTemplateResponse res = api.getExigoApiSoap().createEmailTemplate(req, auth);

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

### CreateMailFolder

> Creates a mail folder.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/CreateMailFolder` |
| WSDL elements | `CreateMailFolderRequest` → `CreateMailFolderResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateMailFolder |

#### Input

**`CreateMailFolderRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `MailFolderName` | `String` | Optional. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`CreateMailFolderResponse`**

_No properties._

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateMailFolder"

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
    <CreateMailFolderRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <MailFolderName>string</MailFolderName>
      <CustomerKey>string</CustomerKey>
    </CreateMailFolderRequest>
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
    <CreateMailFolderResult xmlns="http://api.exigo.com/" />
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
    var req = new CreateMailFolderRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.MailFolderName = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.CreateMailFolderAsync(req);

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
    CreateMailFolderRequest req = new CreateMailFolderRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.MailFolderName = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    CreateMailFolderResponse res = api.CreateMailFolder(req);

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
    Dim req as new CreateMailFolderRequest()

    req.CustomerID = 1
    req.MailFolderName = "1"
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As CreateMailFolderResponse = api.CreateMailFolder(req)

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
    $req->MailFolderName = "1";
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.CreateMailFolder($req);

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
    CreateMailFolderRequest req = new CreateMailFolderRequest();

    req.setCustomerID(1);
    req.setMailFolderName("1");
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    CreateMailFolderResponse res = api.getExigoApiSoap().createMailFolder(req, auth);

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

### CreateOrderDetail

>  Create a new Order Detail for an existing order without recalculating. Can participate in a transaction.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/CreateOrderDetail` |
| WSDL elements | `CreateOrderDetailRequest` → `CreateOrderDetailResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateOrderDetail |

#### Input

**`CreateOrderDetailRequest`**

| Property | Type | Notes |
|---|---|---|
| `OrderID` | `Int32` | Unique numeric identifier for new order record. |
| `OrderLine` | `Int32` |  |
| `ItemCode` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Description` | `String` | Optional. |
| `Qty` | `Decimal` |  |
| `PriceEach` | `Decimal` | Optional. |
| `PriceExt` | `Decimal` | Optional. |
| `BVEach` | `Decimal` | Optional. |
| `BusinessVolume` | `Decimal` | Optional. Price amount. |
| `CVEach` | `Decimal` | Optional. |
| `CommissionableVolume` | `Decimal` | Optional. Price amount. |
| `ShippingPriceEach` | `Decimal` | Optional. |
| `ChargeShippingOn` | `Decimal` | Optional. |
| `IsTaxedInRegion` | `Boolean` | Optional. |
| `IsTaxedInRegionFed` | `Boolean` | Optional. |
| `IsTaxedInRegionState` | `Boolean` | Optional. |
| `TaxablePriceEach` | `Decimal` | Optional. |
| `Taxable` | `Decimal` | Optional. |
| `CombinedTax` | `Decimal` | Optional. |
| `FedTax` | `Decimal` | Optional. |
| `StateTax` | `Decimal` | Optional. |
| `CityTax` | `Decimal` | Optional. |
| `CityLocalTax` | `Decimal` | Optional. |
| `CountyTax` | `Decimal` | Optional. |
| `CountyLocalTax` | `Decimal` | Optional. |
| `ManualTax` | `Decimal` | Optional. |
| `IsBackOrder` | `Boolean` | Optional. |
| `WeightEach` | `Decimal` | Optional. |
| `Other1Each` | `Decimal` | Optional. |
| `Other1` | `Decimal` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other2Each` | `Decimal` | Optional. |
| `Other2` | `Decimal` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other3Each` | `Decimal` | Optional. |
| `Other3` | `Decimal` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other4Each` | `Decimal` | Optional. |
| `Other4` | `Decimal` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other5Each` | `Decimal` | Optional. |
| `Other5` | `Decimal` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other6Each` | `Decimal` | Optional. |
| `Other6` | `Decimal` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other7Each` | `Decimal` | Optional. |
| `Other7` | `Decimal` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other8Each` | `Decimal` | Optional. |
| `Other8` | `Decimal` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other9Each` | `Decimal` | Optional. |
| `Other9` | `Decimal` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other10Each` | `Decimal` | Optional. |
| `Other10` | `Decimal` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `DiscountExt` | `Decimal` | Optional. |
| `OriginalTaxableEach` | `Decimal` | Optional. |
| `OriginalBVEach` | `Decimal` | Optional. |
| `OriginalCVEach` | `Decimal` | Optional. |
| `StateTaxable` | `Decimal` | Optional. |
| `IsStateTaxOverride` | `Boolean` | Optional. |
| `DynamicKitItemID` | `Int32` | Optional. |
| `HandlingFee` | `Decimal` | Optional. |
| `Reference1` | `String` | Optional. |
| `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided. |

#### Output

**`CreateOrderDetailResponse`**

| Property | Type | Notes |
|---|---|---|
| `OrderID` | `Int32` | Unique numeric identifier for order record. |
| `OrderLine` | `Int32` |  |
| `OrderKey` | `String` | Unique alpha numeric identifier for order record. |

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateOrderDetail"

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
    <CreateOrderDetailRequest xmlns="http://api.exigo.com/">
      <OrderID>int</OrderID>
      <OrderLine>int</OrderLine>
      <ItemCode>string</ItemCode>
      <Description>string</Description>
      <Qty>decimal</Qty>
      <PriceEach>decimal</PriceEach>
      <PriceExt>decimal</PriceExt>
      <BVEach>decimal</BVEach>
      <BusinessVolume>decimal</BusinessVolume>
      <CVEach>decimal</CVEach>
      <CommissionableVolume>decimal</CommissionableVolume>
      <ShippingPriceEach>decimal</ShippingPriceEach>
      <ChargeShippingOn>decimal</ChargeShippingOn>
      <IsTaxedInRegion>boolean</IsTaxedInRegion>
      <IsTaxedInRegionFed>boolean</IsTaxedInRegionFed>
      <IsTaxedInRegionState>boolean</IsTaxedInRegionState>
      <TaxablePriceEach>decimal</TaxablePriceEach>
      <Taxable>decimal</Taxable>
      <CombinedTax>decimal</CombinedTax>
      <FedTax>decimal</FedTax>
      <StateTax>decimal</StateTax>
      <CityTax>decimal</CityTax>
      <CityLocalTax>decimal</CityLocalTax>
      <CountyTax>decimal</CountyTax>
      <CountyLocalTax>decimal</CountyLocalTax>
      <ManualTax>decimal</ManualTax>
      <IsBackOrder>boolean</IsBackOrder>
      <WeightEach>decimal</WeightEach>
      <Other1Each>decimal</Other1Each>
      <Other1>decimal</Other1>
      <Other2Each>decimal</Other2Each>
      <Other2>decimal</Other2>
      <Other3Each>decimal</Other3Each>
      <Other3>decimal</Other3>
      <Other4Each>decimal</Other4Each>
      <Other4>decimal</Other4>
      <Other5Each>decimal</Other5Each>
      <Other5>decimal</Other5>
      <Other6Each>decimal</Other6Each>
      <Other6>decimal</Other6>
      <Other7Each>decimal</Other7Each>
      <Other7>decimal</Other7>
      <Other8Each>decimal</Other8Each>
      <Other8>decimal</Other8>
      <Other9Each>decimal</Other9Each>
      <Other9>decimal</Other9>
      <Other10Each>decimal</Other10Each>
      <Other10>decimal</Other10>
      <DiscountExt>decimal</DiscountExt>
      <OriginalTaxableEach>decimal</OriginalTaxableEach>
      <OriginalBVEach>decimal</OriginalBVEach>
      <OriginalCVEach>decimal</OriginalCVEach>
      <StateTaxable>decimal</StateTaxable>
      <IsStateTaxOverride>boolean</IsStateTaxOverride>
      <DynamicKitItemID>int</DynamicKitItemID>
      <HandlingFee>decimal</HandlingFee>
      <Reference1>string</Reference1>
      <OrderKey>string</OrderKey>
    </CreateOrderDetailRequest>
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
    <CreateOrderDetailResult xmlns="http://api.exigo.com/">
      <OrderID>int</OrderID>
      <OrderLine>int</OrderLine>
      <OrderKey>string</OrderKey>
    </CreateOrderDetailResult>
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
    var req = new CreateOrderDetailRequest();

    req.OrderLine = 1;
    req.ItemCode = "1";
    req.Description = "1";
    req.Qty = 1;
    req.PriceEach = 1;
    req.PriceExt = 1;
    req.BVEach = 1;
    req.BusinessVolume = 1;         //Price amount
    req.CVEach = 1;
    req.CommissionableVolume = 1;   //Price amount
    req.ShippingPriceEach = 1;
    req.ChargeShippingOn = 1;
    req.IsTaxedInRegion = true;
    req.IsTaxedInRegionFed = true;
    req.IsTaxedInRegionState = true;
    req.TaxablePriceEach = 1;
    req.Taxable = 1;
    req.CombinedTax = 1;
    req.FedTax = 1;
    req.StateTax = 1;
    req.CityTax = 1;
    req.CityLocalTax = 1;
    req.CountyTax = 1;
    req.CountyLocalTax = 1;
    req.ManualTax = 1;
    req.IsBackOrder = true;
    req.WeightEach = 1;
    req.Other1Each = 1;
    req.Other2Each = 1;
    req.Other3Each = 1;
    req.Other4Each = 1;
    req.Other5Each = 1;
    req.Other6Each = 1;
    req.Other7Each = 1;
    req.Other8Each = 1;
    req.Other9Each = 1;
    req.Other10Each = 1;
    req.DiscountExt = 1;
    req.OriginalTaxableEach = 1;
    req.OriginalBVEach = 1;
    req.OriginalCVEach = 1;
    req.StateTaxable = 1;
    req.IsStateTaxOverride = true;
    req.DynamicKitItemID = 1;
    req.HandlingFee = 1;
    req.Reference1 = "1";
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    var res = await api.CreateOrderDetailAsync(req);

    //Now examine the results:
    Console.WriteLine("OrderID: {0}", res.OrderID);
    Console.WriteLine("OrderLine: {0}", res.OrderLine);
    Console.WriteLine("OrderKey: {0}", res.OrderKey);
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
    CreateOrderDetailRequest req = new CreateOrderDetailRequest();

    req.OrderLine = 1;
    req.ItemCode = "1";
    req.Description = "1";
    req.Qty = 1;
    req.PriceEach = 1;
    req.PriceExt = 1;
    req.BVEach = 1;
    req.BusinessVolume = 1;         //Price amount
    req.CVEach = 1;
    req.CommissionableVolume = 1;   //Price amount
    req.ShippingPriceEach = 1;
    req.ChargeShippingOn = 1;
    req.IsTaxedInRegion = true;
    req.IsTaxedInRegionFed = true;
    req.IsTaxedInRegionState = true;
    req.TaxablePriceEach = 1;
    req.Taxable = 1;
    req.CombinedTax = 1;
    req.FedTax = 1;
    req.StateTax = 1;
    req.CityTax = 1;
    req.CityLocalTax = 1;
    req.CountyTax = 1;
    req.CountyLocalTax = 1;
    req.ManualTax = 1;
    req.IsBackOrder = true;
    req.WeightEach = 1;
    req.Other1Each = 1;
    req.Other2Each = 1;
    req.Other3Each = 1;
    req.Other4Each = 1;
    req.Other5Each = 1;
    req.Other6Each = 1;
    req.Other7Each = 1;
    req.Other8Each = 1;
    req.Other9Each = 1;
    req.Other10Each = 1;
    req.DiscountExt = 1;
    req.OriginalTaxableEach = 1;
    req.OriginalBVEach = 1;
    req.OriginalCVEach = 1;
    req.StateTaxable = 1;
    req.IsStateTaxOverride = true;
    req.DynamicKitItemID = 1;
    req.HandlingFee = 1;
    req.Reference1 = "1";
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    CreateOrderDetailResponse res = api.CreateOrderDetail(req);

    //Now examine the results:
    Console.WriteLine("OrderID: {0}", res.OrderID);
    Console.WriteLine("OrderLine: {0}", res.OrderLine);
    Console.WriteLine("OrderKey: {0}", res.OrderKey);
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
    Dim req as new CreateOrderDetailRequest()

    req.OrderLine = 1
    req.ItemCode = "1"
    req.Description = "1"
    req.Qty = 1
    req.PriceEach = 1
    req.PriceExt = 1
    req.BVEach = 1
    req.BusinessVolume = 1
    req.CVEach = 1
    req.CommissionableVolume = 1
    req.ShippingPriceEach = 1
    req.ChargeShippingOn = 1
    req.IsTaxedInRegion = true
    req.IsTaxedInRegionFed = true
    req.IsTaxedInRegionState = true
    req.TaxablePriceEach = 1
    req.Taxable = 1
    req.CombinedTax = 1
    req.FedTax = 1
    req.StateTax = 1
    req.CityTax = 1
    req.CityLocalTax = 1
    req.CountyTax = 1
    req.CountyLocalTax = 1
    req.ManualTax = 1
    req.IsBackOrder = true
    req.WeightEach = 1
    req.Other1Each = 1
    req.Other2Each = 1
    req.Other3Each = 1
    req.Other4Each = 1
    req.Other5Each = 1
    req.Other6Each = 1
    req.Other7Each = 1
    req.Other8Each = 1
    req.Other9Each = 1
    req.Other10Each = 1
    req.DiscountExt = 1
    req.OriginalTaxableEach = 1
    req.OriginalBVEach = 1
    req.OriginalCVEach = 1
    req.StateTaxable = 1
    req.IsStateTaxOverride = true
    req.DynamicKitItemID = 1
    req.HandlingFee = 1
    req.Reference1 = "1"
    req.OrderKey = "1"

    'Send Request to Server and Get Response
    Dim res As CreateOrderDetailResponse = api.CreateOrderDetail(req)

    'Now examine the results:
    Console.WriteLine("OrderID: {0}", res.OrderID)
    Console.WriteLine("OrderLine: {0}", res.OrderLine)
    Console.WriteLine("OrderKey: {0}", res.OrderKey)
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

    $req->OrderLine = 1;
    $req->ItemCode = "1";
    $req->Description = "1";
    $req->Qty = 1;
    $req->PriceEach = 1;
    $req->PriceExt = 1;
    $req->BVEach = 1;
    $req->BusinessVolume = 1;
    $req->CVEach = 1;
    $req->CommissionableVolume = 1;
    $req->ShippingPriceEach = 1;
    $req->ChargeShippingOn = 1;
    $req->IsTaxedInRegion = 1;
    $req->IsTaxedInRegionFed = 1;
    $req->IsTaxedInRegionState = 1;
    $req->TaxablePriceEach = 1;
    $req->Taxable = 1;
    $req->CombinedTax = 1;
    $req->FedTax = 1;
    $req->StateTax = 1;
    $req->CityTax = 1;
    $req->CityLocalTax = 1;
    $req->CountyTax = 1;
    $req->CountyLocalTax = 1;
    $req->ManualTax = 1;
    $req->IsBackOrder = 1;
    $req->WeightEach = 1;
    $req->Other1Each = 1;
    $req->Other2Each = 1;
    $req->Other3Each = 1;
    $req->Other4Each = 1;
    $req->Other5Each = 1;
    $req->Other6Each = 1;
    $req->Other7Each = 1;
    $req->Other8Each = 1;
    $req->Other9Each = 1;
    $req->Other10Each = 1;
    $req->DiscountExt = 1;
    $req->OriginalTaxableEach = 1;
    $req->OriginalBVEach = 1;
    $req->OriginalCVEach = 1;
    $req->StateTaxable = 1;
    $req->IsStateTaxOverride = 1;
    $req->DynamicKitItemID = 1;
    $req->HandlingFee = 1;
    $req->Reference1 = "1";
    $req->OrderKey = "1";

    //Send Request to Server and Get Response
    $res = $api.CreateOrderDetail($req);

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
    CreateOrderDetailRequest req = new CreateOrderDetailRequest();

    req.setOrderLine(1);
    req.setItemCode("1");
    req.setDescription("1");
    req.setQty(1);
    req.setPriceEach(1);
    req.setPriceExt(1);
    req.setBVEach(1);
    req.setBusinessVolume(1);
    req.setCVEach(1);
    req.setCommissionableVolume(1);
    req.setShippingPriceEach(1);
    req.setChargeShippingOn(1);
    req.setIsTaxedInRegion(1);
    req.setIsTaxedInRegionFed(1);
    req.setIsTaxedInRegionState(1);
    req.setTaxablePriceEach(1);
    req.setTaxable(1);
    req.setCombinedTax(1);
    req.setFedTax(1);
    req.setStateTax(1);
    req.setCityTax(1);
    req.setCityLocalTax(1);
    req.setCountyTax(1);
    req.setCountyLocalTax(1);
    req.setManualTax(1);
    req.setIsBackOrder(1);
    req.setWeightEach(1);
    req.setOther1Each(1);
    req.setOther2Each(1);
    req.setOther3Each(1);
    req.setOther4Each(1);
    req.setOther5Each(1);
    req.setOther6Each(1);
    req.setOther7Each(1);
    req.setOther8Each(1);
    req.setOther9Each(1);
    req.setOther10Each(1);
    req.setDiscountExt(1);
    req.setOriginalTaxableEach(1);
    req.setOriginalBVEach(1);
    req.setOriginalCVEach(1);
    req.setStateTaxable(1);
    req.setIsStateTaxOverride(1);
    req.setDynamicKitItemID(1);
    req.setHandlingFee(1);
    req.setReference1("1");
    req.setOrderKey("1");

    //Send Request to Server and Get Response
    CreateOrderDetailResponse res = api.getExigoApiSoap().createOrderDetail(req, auth);

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

### CreatePayout

> Creates a new payout for one or more bills and updates status

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | `POST /3.0/payout` |
| SOAP action | `https://api.exigo.com/CreatePayout` |
| WSDL elements | `CreatePayoutRequest` → `CreatePayoutResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreatePayout |

#### Input

**`CreatePayoutRequest`**

| Property | Type | Notes |
|---|---|---|
| `BillIDs_ToPay` | `Int32[]` |  |
| `VendorPaymentTypeID` | `Int32` | Payment type.<br>**Lookup:** company-specific list (see company-lists.md) |
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `BankAccountID` | `Int32` | Bank account identifier.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Reference` | `String` | Optional. |
| `TransactionNote` | `String` | Optional. |
| `PaymentDate` | `DateTime` |  |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`CreatePayoutResponse`**

| Property | Type | Notes |
|---|---|---|
| `PayoutID` | `Int32` |  |
| `TotalDollarAmount` | `Decimal` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/payout HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "billIDs_ToPay": null,
  "vendorPaymentTypeID": 1,
  "customerID": 1,
  "reference": "",
  "transactionNote": "",
  "paymentDate": "2026-11-10T00:00:00-06:00",
  "customerKey": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "payoutID": 1,
  "totalDollarAmount": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreatePayout"

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
    <CreatePayoutRequest xmlns="http://api.exigo.com/">
      <BillIDs_ToPay>
        <int>int</int>
      </BillIDs_ToPay>
      <VendorPaymentTypeID>int</VendorPaymentTypeID>
    </CreatePayoutRequest>
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
    <CreatePayoutResult xmlns="http://api.exigo.com/">
      <PayoutID>int</PayoutID>
      <TotalDollarAmount>decimal</TotalDollarAmount>
    </CreatePayoutResult>
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
    var req = new CreatePayoutRequest();

    //Add BillIDs_ToPay
    var billids_topay = new List<Int32>();
    billids_topay.Add(1);
    billids_topay.Add(2);

    //Now attach the list to the request
    req.BillIDs_ToPay = billids_topay.ToArray();
    req.VendorPaymentTypeID = 1;    //Payment type.
    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.Reference = "1";
    req.TransactionNote = "1";
    req.PaymentDate = DateTime.Today;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.CreatePayoutAsync(req);

    //Now examine the results:
    Console.WriteLine("PayoutID: {0}", res.PayoutID);
    Console.WriteLine("TotalDollarAmount: {0}", res.TotalDollarAmount);
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
    CreatePayoutRequest req = new CreatePayoutRequest();

    //Add BillIDs_ToPay
    List<Int32> billids_topay = new List<Int32>();
    billids_topay.Add(1);
    billids_topay.Add(2);

    //Now attach the list to the request
    req.BillIDs_ToPay = billids_topay.ToArray();
    req.VendorPaymentTypeID = 1;    //Payment type.
    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.Reference = "1";
    req.TransactionNote = "1";
    req.PaymentDate = DateTime.Today;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    CreatePayoutResponse res = api.CreatePayout(req);

    //Now examine the results:
    Console.WriteLine("PayoutID: {0}", res.PayoutID);
    Console.WriteLine("TotalDollarAmount: {0}", res.TotalDollarAmount);
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
    Dim req as new CreatePayoutRequest()

    'Add BillIDs_ToPay
    Dim billids_topay As New List(Of Int32)()
    billids_topay.Add(1)
    billids_topay.Add(2)

    'Now attach the list to the request
    req.BillIDs_ToPay = billids_topay.ToArray()
    req.VendorPaymentTypeID = 1
    req.CustomerID = 1
    req.Reference = "1"
    req.TransactionNote = "1"
    req.PaymentDate = DateTime.Today
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As CreatePayoutResponse = api.CreatePayout(req)

    'Now examine the results:
    Console.WriteLine("PayoutID: {0}", res.PayoutID)
    Console.WriteLine("TotalDollarAmount: {0}", res.TotalDollarAmount)
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

    //Add BillIDs_ToPay

    //Now attach the list to the request
    req.BillIDs_ToPay = array(billIDs_ToPa1,billIDs_ToPa2);
    $req->VendorPaymentTypeID = 1;
    $req->CustomerID = 1;
    $req->Reference = "1";
    $req->TransactionNote = "1";
    $req->PaymentDate = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.CreatePayout($req);

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
    CreatePayoutRequest req = new CreatePayoutRequest();

    //Add BillIDs_ToPay
    ArrayOfSystem.Int32 billids_topay = new ArrayOfSystem.Int32();

    Int32 billIDs_ToPa1 = new Int32();
    billids_topay.Add(billIDs_ToPa1);

    Int32 billIDs_ToPa2 = new Int32();
    billids_topay.Add(billIDs_ToPa2);

    //Now attach the list to the request
    req.setBillIDs_ToPay(billids_topay);
    req.setVendorPaymentTypeID(1);
    req.setCustomerID(1);
    req.setReference("1");
    req.setTransactionNote("1");
    req.setPaymentDate(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    CreatePayoutResponse res = api.getExigoApiSoap().createPayout(req, auth);

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

### CreateVendorBill

> Creates a new VendorBill for a customer on file.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/CreateVendorBill` |
| WSDL elements | `CreateVendorBillRequest` → `CreateVendorBillResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateVendorBill |

#### Input

**`CreateVendorBillRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CurrencyCode` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `DueDate` | `DateTime` |  |
| `Amount` | `Decimal` |  |
| `Reference` | `String` | Optional. |
| `Notes` | `String` | Optional. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |
| `TaxablePeriodTy` | `Int32` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `TaxablePeriodID` | `Int32` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |

#### Output

**`CreateVendorBillResponse`**

| Property | Type | Notes |
|---|---|---|
| `VendorBillID` | `Int32` |  |

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateVendorBill"

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
    <CreateVendorBillRequest xmlns="http://api.exigo.com/">
      <VendorBillStatusTypeID>int</VendorBillStatusTypeID>
      <CustomerID>int</CustomerID>
      <CurrencyCode>string</CurrencyCode>
      <DueDate>dateTime</DueDate>
      <Amount>decimal</Amount>
      <Reference>string</Reference>
      <Notes>string</Notes>
      <CustomerKey>string</CustomerKey>
      <TaxablePeriodTy>int</TaxablePeriodTy>
      <TaxablePeriodID>int</TaxablePeriodID>
    </CreateVendorBillRequest>
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
    <CreateVendorBillResult xmlns="http://api.exigo.com/">
      <VendorBillID>int</VendorBillID>
    </CreateVendorBillResult>
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
    var req = new CreateVendorBillRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CurrencyCode = "usd";
    req.DueDate = DateTime.Today;
    req.Amount = 1;
    req.Reference = "1";
    req.Notes = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.TaxablePeriodTy = 1;
    req.TaxablePeriodID = 1;

    //Send Request to Server and Get Response
    var res = await api.CreateVendorBillAsync(req);

    //Now examine the results:
    Console.WriteLine("VendorBillID: {0}", res.VendorBillID);
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
    CreateVendorBillRequest req = new CreateVendorBillRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CurrencyCode = "usd";
    req.DueDate = DateTime.Today;
    req.Amount = 1;
    req.Reference = "1";
    req.Notes = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.TaxablePeriodTy = 1;
    req.TaxablePeriodID = 1;

    //Send Request to Server and Get Response
    CreateVendorBillResponse res = api.CreateVendorBill(req);

    //Now examine the results:
    Console.WriteLine("VendorBillID: {0}", res.VendorBillID);
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
    Dim req as new CreateVendorBillRequest()

    req.CustomerID = 1
    req.CurrencyCode = "usd"
    req.DueDate = DateTime.Today
    req.Amount = 1
    req.Reference = "1"
    req.Notes = "1"
    req.CustomerKey = "1"
    req.TaxablePeriodTy = 1
    req.TaxablePeriodID = 1

    'Send Request to Server and Get Response
    Dim res As CreateVendorBillResponse = api.CreateVendorBill(req)

    'Now examine the results:
    Console.WriteLine("VendorBillID: {0}", res.VendorBillID)
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
    $req->CurrencyCode = "usd";
    $req->DueDate = 1;
    $req->Amount = 1;
    $req->Reference = "1";
    $req->Notes = "1";
    $req->CustomerKey = "1";
    $req->TaxablePeriodTy = 1;
    $req->TaxablePeriodID = 1;

    //Send Request to Server and Get Response
    $res = $api.CreateVendorBill($req);

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
    CreateVendorBillRequest req = new CreateVendorBillRequest();

    req.setCustomerID(1);
    req.setCurrencyCode("usd");
    req.setDueDate(1);
    req.setAmount(1);
    req.setReference("1");
    req.setNotes("1");
    req.setCustomerKey("1");
    req.setTaxablePeriodTy(1);
    req.setTaxablePeriodID(1);

    //Send Request to Server and Get Response
    CreateVendorBillResponse res = api.getExigoApiSoap().createVendorBill(req, auth);

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

### DeleteCustomerContact

> Deletes a customer contact.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/DeleteCustomerContact` |
| WSDL elements | `DeleteCustomerContactRequest` → `DeleteCustomerContactResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DeleteCustomerContact |

#### Input

**`DeleteCustomerContactRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerContactID` | `Int32` |  |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`DeleteCustomerContactResponse`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerContactID` | `Int32` |  |
| `CustomerKey` | `String` | Unique alpha numeric identifier for customer record . |

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/DeleteCustomerContact"

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
    <DeleteCustomerContactRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerContactID>int</CustomerContactID>
      <CustomerKey>string</CustomerKey>
    </DeleteCustomerContactRequest>
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
    <DeleteCustomerContactResult xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerContactID>int</CustomerContactID>
      <CustomerKey>string</CustomerKey>
    </DeleteCustomerContactResult>
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
    var req = new DeleteCustomerContactRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerContactID = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.DeleteCustomerContactAsync(req);

    //Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID);
    Console.WriteLine("CustomerContactID: {0}", res.CustomerContactID);
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
    DeleteCustomerContactRequest req = new DeleteCustomerContactRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerContactID = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    DeleteCustomerContactResponse res = api.DeleteCustomerContact(req);

    //Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID);
    Console.WriteLine("CustomerContactID: {0}", res.CustomerContactID);
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
    Dim req as new DeleteCustomerContactRequest()

    req.CustomerID = 1
    req.CustomerContactID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As DeleteCustomerContactResponse = api.DeleteCustomerContact(req)

    'Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID)
    Console.WriteLine("CustomerContactID: {0}", res.CustomerContactID)
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
    $req->CustomerContactID = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.DeleteCustomerContact($req);

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
    DeleteCustomerContactRequest req = new DeleteCustomerContactRequest();

    req.setCustomerID(1);
    req.setCustomerContactID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    DeleteCustomerContactResponse res = api.getExigoApiSoap().deleteCustomerContact(req, auth);

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

### DeleteEmail

> Deletes an email forever.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/DeleteEmail` |
| WSDL elements | `DeleteEmailRequest` → `DeleteEmailResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DeleteEmail |

#### Input

**`DeleteEmailRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `MailID` | `Int32` |  |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`DeleteEmailResponse`**

_No properties._

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/DeleteEmail"

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
    <DeleteEmailRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <MailID>int</MailID>
      <CustomerKey>string</CustomerKey>
    </DeleteEmailRequest>
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
    <DeleteEmailResult xmlns="http://api.exigo.com/" />
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
    var req = new DeleteEmailRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.MailID = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.DeleteEmailAsync(req);

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
    DeleteEmailRequest req = new DeleteEmailRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.MailID = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    DeleteEmailResponse res = api.DeleteEmail(req);

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
    Dim req as new DeleteEmailRequest()

    req.CustomerID = 1
    req.MailID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As DeleteEmailResponse = api.DeleteEmail(req)

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
    $req->MailID = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.DeleteEmail($req);

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
    DeleteEmailRequest req = new DeleteEmailRequest();

    req.setCustomerID(1);
    req.setMailID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    DeleteEmailResponse res = api.getExigoApiSoap().deleteEmail(req, auth);

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

### DeleteEmailTemplate

> Deletes an email template.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/DeleteEmailTemplate` |
| WSDL elements | `DeleteEmailTemplateRequest` → `DeleteEmailTemplateResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DeleteEmailTemplate |

#### Input

**`DeleteEmailTemplateRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `TemplateID` | `Int32` |  |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`DeleteEmailTemplateResponse`**

_No properties._

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/DeleteEmailTemplate"

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
    <DeleteEmailTemplateRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <TemplateID>int</TemplateID>
      <CustomerKey>string</CustomerKey>
    </DeleteEmailTemplateRequest>
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
    <DeleteEmailTemplateResult xmlns="http://api.exigo.com/" />
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
    var req = new DeleteEmailTemplateRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.TemplateID = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.DeleteEmailTemplateAsync(req);

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
    DeleteEmailTemplateRequest req = new DeleteEmailTemplateRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.TemplateID = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    DeleteEmailTemplateResponse res = api.DeleteEmailTemplate(req);

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
    Dim req as new DeleteEmailTemplateRequest()

    req.CustomerID = 1
    req.TemplateID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As DeleteEmailTemplateResponse = api.DeleteEmailTemplate(req)

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
    $req->TemplateID = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.DeleteEmailTemplate($req);

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
    DeleteEmailTemplateRequest req = new DeleteEmailTemplateRequest();

    req.setCustomerID(1);
    req.setTemplateID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    DeleteEmailTemplateResponse res = api.getExigoApiSoap().deleteEmailTemplate(req, auth);

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

### DeleteMailFolder

> Deletes a mail folder.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/DeleteMailFolder` |
| WSDL elements | `DeleteMailFolderRequest` → `DeleteMailFolderResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DeleteMailFolder |

#### Input

**`DeleteMailFolderRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `MailFolderID` | `Int32` |  |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`DeleteMailFolderResponse`**

_No properties._

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/DeleteMailFolder"

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
    <DeleteMailFolderRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <MailFolderID>int</MailFolderID>
      <CustomerKey>string</CustomerKey>
    </DeleteMailFolderRequest>
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
    <DeleteMailFolderResult xmlns="http://api.exigo.com/" />
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
    var req = new DeleteMailFolderRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.MailFolderID = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.DeleteMailFolderAsync(req);

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
    DeleteMailFolderRequest req = new DeleteMailFolderRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.MailFolderID = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    DeleteMailFolderResponse res = api.DeleteMailFolder(req);

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
    Dim req as new DeleteMailFolderRequest()

    req.CustomerID = 1
    req.MailFolderID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As DeleteMailFolderResponse = api.DeleteMailFolder(req)

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
    $req->MailFolderID = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.DeleteMailFolder($req);

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
    DeleteMailFolderRequest req = new DeleteMailFolderRequest();

    req.setCustomerID(1);
    req.setMailFolderID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    DeleteMailFolderResponse res = api.getExigoApiSoap().deleteMailFolder(req, auth);

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

### DeleteOrderDetail

>  Delete an existing Order Detail for an existing order without recalculating. Can participate in a transaction.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/DeleteOrderDetail` |
| WSDL elements | `DeleteOrderDetailRequest` → `DeleteOrderDetailResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DeleteOrderDetail |

#### Input

**`DeleteOrderDetailRequest`**

| Property | Type | Notes |
|---|---|---|
| `OrderID` | `Int32` | Unique numeric identifier for new order record. |
| `OrderLine` | `Int32` |  |
| `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided. |

#### Output

**`DeleteOrderDetailResponse`**

_No properties._

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/DeleteOrderDetail"

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
    <DeleteOrderDetailRequest xmlns="http://api.exigo.com/">
      <OrderID>int</OrderID>
      <OrderLine>int</OrderLine>
      <OrderKey>string</OrderKey>
    </DeleteOrderDetailRequest>
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
    <DeleteOrderDetailResult xmlns="http://api.exigo.com/" />
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
    var req = new DeleteOrderDetailRequest();

    req.OrderLine = 1;
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    var res = await api.DeleteOrderDetailAsync(req);

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
    DeleteOrderDetailRequest req = new DeleteOrderDetailRequest();

    req.OrderLine = 1;
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    DeleteOrderDetailResponse res = api.DeleteOrderDetail(req);

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
    Dim req as new DeleteOrderDetailRequest()

    req.OrderLine = 1
    req.OrderKey = "1"

    'Send Request to Server and Get Response
    Dim res As DeleteOrderDetailResponse = api.DeleteOrderDetail(req)

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

    $req->OrderLine = 1;
    $req->OrderKey = "1";

    //Send Request to Server and Get Response
    $res = $api.DeleteOrderDetail($req);

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
    DeleteOrderDetailRequest req = new DeleteOrderDetailRequest();

    req.setOrderLine(1);
    req.setOrderKey("1");

    //Send Request to Server and Get Response
    DeleteOrderDetailResponse res = api.getExigoApiSoap().deleteOrderDetail(req, auth);

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

### EmptyMailFolder

> Deletes all emails from a folder.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/EmptyMailFolder` |
| WSDL elements | `EmptyMailFolderRequest` → `EmptyMailFolderResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=EmptyMailFolder |

#### Input

**`EmptyMailFolderRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `MailFolderID` | `Int32` |  |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`EmptyMailFolderResponse`**

_No properties._

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/EmptyMailFolder"

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
    <EmptyMailFolderRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <MailFolderID>int</MailFolderID>
      <CustomerKey>string</CustomerKey>
    </EmptyMailFolderRequest>
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
    <EmptyMailFolderResult xmlns="http://api.exigo.com/" />
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
    var req = new EmptyMailFolderRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.MailFolderID = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.EmptyMailFolderAsync(req);

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
    EmptyMailFolderRequest req = new EmptyMailFolderRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.MailFolderID = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    EmptyMailFolderResponse res = api.EmptyMailFolder(req);

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
    Dim req as new EmptyMailFolderRequest()

    req.CustomerID = 1
    req.MailFolderID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As EmptyMailFolderResponse = api.EmptyMailFolder(req)

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
    $req->MailFolderID = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.EmptyMailFolder($req);

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
    EmptyMailFolderRequest req = new EmptyMailFolderRequest();

    req.setCustomerID(1);
    req.setMailFolderID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    EmptyMailFolderResponse res = api.getExigoApiSoap().emptyMailFolder(req, auth);

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

### EnsureMailFolders

> Ensures all the basic mail folders exist.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/EnsureMailFolders` |
| WSDL elements | `EnsureMailFoldersRequest` → `EnsureMailFoldersResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=EnsureMailFolders |

#### Input

**`EnsureMailFoldersRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`EnsureMailFoldersResponse`**

_No properties._

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/EnsureMailFolders"

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
    <EnsureMailFoldersRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
    </EnsureMailFoldersRequest>
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
    <EnsureMailFoldersResult xmlns="http://api.exigo.com/" />
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
    var req = new EnsureMailFoldersRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.EnsureMailFoldersAsync(req);

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
    EnsureMailFoldersRequest req = new EnsureMailFoldersRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    EnsureMailFoldersResponse res = api.EnsureMailFolders(req);

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
    Dim req as new EnsureMailFoldersRequest()

    req.CustomerID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As EnsureMailFoldersResponse = api.EnsureMailFolders(req)

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
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.EnsureMailFolders($req);

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
    EnsureMailFoldersRequest req = new EnsureMailFoldersRequest();

    req.setCustomerID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    EnsureMailFoldersResponse res = api.getExigoApiSoap().ensureMailFolders(req, auth);

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

### FundPaymentCard

> Creates a new payout and funds a payment card for one or more bills and updates status

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | `POST /3.0/payout/fund` |
| SOAP action | `https://api.exigo.com/FundPaymentCard` |
| WSDL elements | `FundPaymentCardRequest` → `FundPaymentCardResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=FundPaymentCard |

#### Input

**`FundPaymentCardRequest`**

| Property | Type | Notes |
|---|---|---|
| `PaymentCardTypeID` | `Int32` |  |
| `BillIDList` | `Int32[]` |  |
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `BankAccountID` | `Int32` | Bank account identifier.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Reference` | `String` | Optional. |
| `TransactionNote` | `String` | Optional. |
| `PaymentDate` | `DateTime` |  |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`FundPaymentCardResponse`**

| Property | Type | Notes |
|---|---|---|
| `PayoutID` | `Int32` |  |
| `TotalDollarAmount` | `Decimal` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/payout/fund HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "paymentCardTypeID": 1,
  "billIDList": null,
  "customerID": 1,
  "reference": "",
  "transactionNote": "",
  "paymentDate": "2026-11-10T00:00:00-06:00",
  "customerKey": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "payoutID": 1,
  "totalDollarAmount": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/FundPaymentCard"

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
    <FundPaymentCardRequest xmlns="http://api.exigo.com/">
      <PaymentCardTypeID>int</PaymentCardTypeID>
      <BillIDList>
        <int>int</int>
      </BillIDList>
    </FundPaymentCardRequest>
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
    <FundPaymentCardResult xmlns="http://api.exigo.com/" />
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
    var req = new FundPaymentCardRequest();

    req.PaymentCardTypeID = 1;

    //Add BillIDList
    var billidlist = new List<Int32>();
    billidlist.Add(1);
    billidlist.Add(2);

    //Now attach the list to the request
    req.BillIDList = billidlist.ToArray();
    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.Reference = "1";
    req.TransactionNote = "1";
    req.PaymentDate = DateTime.Today;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.FundPaymentCardAsync(req);

    //Now examine the results:
    Console.WriteLine("PayoutID: {0}", res.PayoutID);
    Console.WriteLine("TotalDollarAmount: {0}", res.TotalDollarAmount);
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
    FundPaymentCardRequest req = new FundPaymentCardRequest();

    req.PaymentCardTypeID = 1;

    //Add BillIDList
    List<Int32> billidlist = new List<Int32>();
    billidlist.Add(1);
    billidlist.Add(2);

    //Now attach the list to the request
    req.BillIDList = billidlist.ToArray();
    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.Reference = "1";
    req.TransactionNote = "1";
    req.PaymentDate = DateTime.Today;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    FundPaymentCardResponse res = api.FundPaymentCard(req);

    //Now examine the results:
    Console.WriteLine("PayoutID: {0}", res.PayoutID);
    Console.WriteLine("TotalDollarAmount: {0}", res.TotalDollarAmount);
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
    Dim req as new FundPaymentCardRequest()

    req.PaymentCardTypeID = 1

    'Add BillIDList
    Dim billidlist As New List(Of Int32)()
    billidlist.Add(1)
    billidlist.Add(2)

    'Now attach the list to the request
    req.BillIDList = billidlist.ToArray()
    req.CustomerID = 1
    req.Reference = "1"
    req.TransactionNote = "1"
    req.PaymentDate = DateTime.Today
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As FundPaymentCardResponse = api.FundPaymentCard(req)

    'Now examine the results:
    Console.WriteLine("PayoutID: {0}", res.PayoutID)
    Console.WriteLine("TotalDollarAmount: {0}", res.TotalDollarAmount)
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

    $req->PaymentCardTypeID = 1;

    //Add BillIDList

    //Now attach the list to the request
    req.BillIDList = array(billIDLis1,billIDLis2);
    $req->CustomerID = 1;
    $req->Reference = "1";
    $req->TransactionNote = "1";
    $req->PaymentDate = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.FundPaymentCard($req);

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
    FundPaymentCardRequest req = new FundPaymentCardRequest();

    req.setPaymentCardTypeID(1);

    //Add BillIDList
    ArrayOfSystem.Int32 billidlist = new ArrayOfSystem.Int32();

    Int32 billIDLis1 = new Int32();
    billidlist.Add(billIDLis1);

    Int32 billIDLis2 = new Int32();
    billidlist.Add(billIDLis2);

    //Now attach the list to the request
    req.setBillIDList(billidlist);
    req.setCustomerID(1);
    req.setReference("1");
    req.setTransactionNote("1");
    req.setPaymentDate(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    FundPaymentCardResponse res = api.getExigoApiSoap().fundPaymentCard(req, auth);

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

### GetCompanyLanguages

>  Gets languages list available to the company.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/GetCompanyLanguages` |
| WSDL elements | `GetLanguagesRequest` → `GetCompanyLanguagesResult` |
| CSV output | Yes — `GET https://api.exigo.com/3.0/csv/?method=GetCompanyLanguages&ApiLoginName=…&ApiPassword=…&ApiCompany=…` |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetCompanyLanguages |

#### Input

**`GetLanguagesRequest`**

_No properties._

#### Output

**`GetLanguagesResponse`**

| Property | Type | Notes |
|---|---|---|
| `CompanyLanguages` | `LanguageResponse[]` |  |

**`LanguageResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `LanguageID` | `Int32` | Customize the web experience by setting this.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Description` | `String` |  |
| &nbsp;&nbsp;↳ `CultureCode` | `String` |  |

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetCompanyLanguages"

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
    <GetLanguagesRequest xmlns="http://api.exigo.com/" />
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
    <GetCompanyLanguagesResult xmlns="http://api.exigo.com/">
      <CompanyLanguages>
        <LanguageResponse>
          <LanguageID>int</LanguageID>
          <Description>string</Description>
          <CultureCode>string</CultureCode>
        </LanguageResponse>
      </CompanyLanguages>
    </GetCompanyLanguagesResult>
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
    var req = new GetLanguagesRequest();

    //Send Request to Server and Get Response
    var res = await api.GetCompanyLanguagesAsync(req);

    //Now examine the results:

    foreach (var language  in res.CompanyLanguages)
    {
        Console.WriteLine("Description: {0}", language.Description);
        Console.WriteLine("CultureCode: {0}", language.CultureCode);
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
    GetLanguagesRequest req = new GetLanguagesRequest();

    //Send Request to Server and Get Response
    GetLanguagesResponse res = api.GetCompanyLanguages(req);

    //Now examine the results:

    foreach (LanguageResponse language  in res.CompanyLanguages)
    {
        Console.WriteLine("Description: {0}", language.Description);
        Console.WriteLine("CultureCode: {0}", language.CultureCode);
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
    Dim req as new GetLanguagesRequest()

    'Send Request to Server and Get Response
    Dim res As GetLanguagesResponse = api.GetCompanyLanguages(req)

    'Now examine the results:

    For Each language As LanguageResponse In res.CompanyLanguages
        Console.WriteLine("Description: {0}", language.Description)
        Console.WriteLine("CultureCode: {0}", language.CultureCode)
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
    $res = $api.GetCompanyLanguages($req);

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
    GetLanguagesRequest req = new GetLanguagesRequest();

    //Send Request to Server and Get Response
    GetLanguagesResponse res = api.getExigoApiSoap().getCompanyLanguages(req, auth);

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
https://api.exigo.com/3.0/csv/?method=GetCompanyLanguages
&ApiLoginName=String
&ApiPassword=String
&ApiCompany=String
Response FieldsLanguageID,Description,CultureCode
Int32,String,String

                    © 2026 Exigo.
```

</details>

---

### GetEmailAttachment

> Gets an email attachment.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/GetEmailAttachment` |
| WSDL elements | `GetEmailAttachmentRequest` → `GetEmailAttachmentResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetEmailAttachment |

#### Input

**`GetEmailAttachmentRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `MailID` | `Int32` |  |
| `AttachmentID` | `Int32` |  |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`GetEmailAttachmentResponse`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Unique alpha numeric identifier for customer record . |
| `MailID` | `Int32` |  |
| `Attachment` | `EmailAttachment` |  |

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetEmailAttachment"

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
    <GetEmailAttachmentRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <MailID>int</MailID>
      <AttachmentID>int</AttachmentID>
      <CustomerKey>string</CustomerKey>
    </GetEmailAttachmentRequest>
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
    <GetEmailAttachmentResult xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
      <MailID>int</MailID>
      <Attachment>
        <BinaryData>base64Binary</BinaryData>
        <FileName>string</FileName>
        <ContentLength>int</ContentLength>
      </Attachment>
    </GetEmailAttachmentResult>
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
    var req = new GetEmailAttachmentRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.MailID = 1;
    req.AttachmentID = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.GetEmailAttachmentAsync(req);

    //Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID);
    Console.WriteLine("CustomerKey: {0}", res.CustomerKey);
    Console.WriteLine("MailID: {0}", res.MailID);
    Console.WriteLine("Attachment: {0}", res.Attachment);
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
    GetEmailAttachmentRequest req = new GetEmailAttachmentRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.MailID = 1;
    req.AttachmentID = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    GetEmailAttachmentResponse res = api.GetEmailAttachment(req);

    //Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID);
    Console.WriteLine("CustomerKey: {0}", res.CustomerKey);
    Console.WriteLine("MailID: {0}", res.MailID);
    Console.WriteLine("Attachment: {0}", res.Attachment);
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
    Dim req as new GetEmailAttachmentRequest()

    req.CustomerID = 1
    req.MailID = 1
    req.AttachmentID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As GetEmailAttachmentResponse = api.GetEmailAttachment(req)

    'Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID)
    Console.WriteLine("CustomerKey: {0}", res.CustomerKey)
    Console.WriteLine("MailID: {0}", res.MailID)
    Console.WriteLine("Attachment: {0}", res.Attachment)
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
    $req->MailID = 1;
    $req->AttachmentID = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.GetEmailAttachment($req);

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
    GetEmailAttachmentRequest req = new GetEmailAttachmentRequest();

    req.setCustomerID(1);
    req.setMailID(1);
    req.setAttachmentID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    GetEmailAttachmentResponse res = api.getExigoApiSoap().getEmailAttachment(req, auth);

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

### GetItemCountryRegion

> Returns item, country and region properties along with taxings for an item.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/GetItemCountryRegion` |
| WSDL elements | `GetItemCountryRegionRequest` → `GetItemCountryRegionResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetItemCountryRegion |

#### Input

**`GetItemCountryRegionRequest`**

| Property | Type | Notes |
|---|---|---|
| `ItemCode` | `String` | Optional. |

#### Output

**`GetItemCountryRegionResponse`**

| Property | Type | Notes |
|---|---|---|
| `ItemCountryRegions` | `ItemCountryRegionResponse[]` |  |

**`ItemCountryRegionResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `ItemCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `CountryCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `RegionCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Taxed` | `Boolean` |  |
| &nbsp;&nbsp;↳ `TaxedFed` | `Boolean` |  |
| &nbsp;&nbsp;↳ `TaxedState` | `Boolean` |  |
| &nbsp;&nbsp;↳ `UseTaxOverride` | `Boolean` |  |
| &nbsp;&nbsp;↳ `TaxOverridePct` | `Decimal` |  |

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetItemCountryRegion"

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
    <GetItemCountryRegionRequest xmlns="http://api.exigo.com/">
      <ItemCode>string</ItemCode>
    </GetItemCountryRegionRequest>
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
    <GetItemCountryRegionResult xmlns="http://api.exigo.com/">
      <ItemCountryRegions>
        <ItemCountryRegionResponse>
          <ItemCode>string</ItemCode>
          <CountryCode>string</CountryCode>
          <RegionCode>string</RegionCode>
          <Taxed>boolean</Taxed>
          <TaxedFed>boolean</TaxedFed>
          <TaxedState>boolean</TaxedState>
          <UseTaxOverride>boolean</UseTaxOverride>
          <TaxOverridePct>decimal</TaxOverridePct>
        </ItemCountryRegionResponse>
      </ItemCountryRegions>
    </GetItemCountryRegionResult>
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
    var req = new GetItemCountryRegionRequest();

    req.ItemCode = "1";

    //Send Request to Server and Get Response
    var res = await api.GetItemCountryRegionAsync(req);

    //Now examine the results:

    foreach (var itemCountryRegion  in res.ItemCountryRegions)
    {
        Console.WriteLine("ItemCode: {0}", itemCountryRegion.ItemCode);
        Console.WriteLine("Taxed: {0}", itemCountryRegion.Taxed);
        Console.WriteLine("TaxedFed: {0}", itemCountryRegion.TaxedFed);
        Console.WriteLine("TaxedState: {0}", itemCountryRegion.TaxedState);
        Console.WriteLine("UseTaxOverride: {0}", itemCountryRegion.UseTaxOverride);
        Console.WriteLine("TaxOverridePct: {0}", itemCountryRegion.TaxOverridePct);
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
    GetItemCountryRegionRequest req = new GetItemCountryRegionRequest();

    req.ItemCode = "1";

    //Send Request to Server and Get Response
    GetItemCountryRegionResponse res = api.GetItemCountryRegion(req);

    //Now examine the results:

    foreach (ItemCountryRegionResponse itemCountryRegion  in res.ItemCountryRegions)
    {
        Console.WriteLine("ItemCode: {0}", itemCountryRegion.ItemCode);
        Console.WriteLine("Taxed: {0}", itemCountryRegion.Taxed);
        Console.WriteLine("TaxedFed: {0}", itemCountryRegion.TaxedFed);
        Console.WriteLine("TaxedState: {0}", itemCountryRegion.TaxedState);
        Console.WriteLine("UseTaxOverride: {0}", itemCountryRegion.UseTaxOverride);
        Console.WriteLine("TaxOverridePct: {0}", itemCountryRegion.TaxOverridePct);
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
    Dim req as new GetItemCountryRegionRequest()

    req.ItemCode = "1"

    'Send Request to Server and Get Response
    Dim res As GetItemCountryRegionResponse = api.GetItemCountryRegion(req)

    'Now examine the results:

    For Each itemCountryRegion As ItemCountryRegionResponse In res.ItemCountryRegions
        Console.WriteLine("ItemCode: {0}", itemCountryRegion.ItemCode)
        Console.WriteLine("Taxed: {0}", itemCountryRegion.Taxed)
        Console.WriteLine("TaxedFed: {0}", itemCountryRegion.TaxedFed)
        Console.WriteLine("TaxedState: {0}", itemCountryRegion.TaxedState)
        Console.WriteLine("UseTaxOverride: {0}", itemCountryRegion.UseTaxOverride)
        Console.WriteLine("TaxOverridePct: {0}", itemCountryRegion.TaxOverridePct)
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

    $req->ItemCode = "1";

    //Send Request to Server and Get Response
    $res = $api.GetItemCountryRegion($req);

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
    GetItemCountryRegionRequest req = new GetItemCountryRegionRequest();

    req.setItemCode("1");

    //Send Request to Server and Get Response
    GetItemCountryRegionResponse res = api.getExigoApiSoap().getItemCountryRegion(req, auth);

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

### GetLoginSession

> Deprecated. Use AuthenticateCustomer instead.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/GetLoginSession` |
| WSDL elements | `GetLoginSessionRequest` → `GetLoginSessionResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetLoginSession |

#### Input

**`GetLoginSessionRequest`**

| Property | Type | Notes |
|---|---|---|
| `SessionID` | `String` | Optional. |

#### Output

**`GetLoginSessionResponse`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `FirstName` | `String` |  |
| `LastName` | `String` |  |
| `CustomerKey` | `String` | Unique alpha numeric identifier for customer record . |

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetLoginSession"

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
    <GetLoginSessionRequest xmlns="http://api.exigo.com/">
      <SessionID>string</SessionID>
    </GetLoginSessionRequest>
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
    <GetLoginSessionResult xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <FirstName>string</FirstName>
      <LastName>string</LastName>
      <CustomerKey>string</CustomerKey>
    </GetLoginSessionResult>
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
    var req = new GetLoginSessionRequest();

    req.SessionID = "1";

    //Send Request to Server and Get Response
    var res = await api.GetLoginSessionAsync(req);

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
    GetLoginSessionRequest req = new GetLoginSessionRequest();

    req.SessionID = "1";

    //Send Request to Server and Get Response
    GetLoginSessionResponse res = api.GetLoginSession(req);

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
    Dim req as new GetLoginSessionRequest()

    req.SessionID = "1"

    'Send Request to Server and Get Response
    Dim res As GetLoginSessionResponse = api.GetLoginSession(req)

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

    $req->SessionID = "1";

    //Send Request to Server and Get Response
    $res = $api.GetLoginSession($req);

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
    GetLoginSessionRequest req = new GetLoginSessionRequest();

    req.setSessionID("1");

    //Send Request to Server and Get Response
    GetLoginSessionResponse res = api.getExigoApiSoap().getLoginSession(req, auth);

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

### GetOrderTotals

> Returns the totals of accepted orders within a date range

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/GetOrderTotals` |
| WSDL elements | `GetOrderTotalsRequest` → `GetOrderTotalsResult` |
| CSV output | Yes — `GET https://api.exigo.com/3.0/csv/?method=GetOrderTotals&ApiLoginName=…&ApiPassword=…&ApiCompany=…` |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetOrderTotals |

#### Input

**`GetOrderTotalsRequest`**

| Property | Type | Notes |
|---|---|---|
| `StartDate` | `DateTime` |  |
| `EndDate` | `DateTime` |  |

#### Output

**`GetOrderTotalsResponse`**

| Property | Type | Notes |
|---|---|---|
| `StartDate` | `DateTime` |  |
| `EndDate` | `DateTime` |  |
| `AcceptedByCurrency` | `OrderTotalByCurrency[]` |  |

**`OrderTotalByCurrency`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `CurrencyCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Amount` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Count` | `Int32` |  |

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetOrderTotals"

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
    <GetOrderTotalsRequest xmlns="http://api.exigo.com/">
      <StartDate>dateTime</StartDate>
      <EndDate>dateTime</EndDate>
    </GetOrderTotalsRequest>
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
    <GetOrderTotalsResult xmlns="http://api.exigo.com/">
      <StartDate>dateTime</StartDate>
      <EndDate>dateTime</EndDate>
      <AcceptedByCurrency>
        <OrderTotalByCurrency>
          <CurrencyCode>string</CurrencyCode>
          <Amount>decimal</Amount>
          <Count>int</Count>
        </OrderTotalByCurrency>
      </AcceptedByCurrency>
    </GetOrderTotalsResult>
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
    var req = new GetOrderTotalsRequest();

    req.StartDate = DateTime.Today;
    req.EndDate = DateTime.Today;

    //Send Request to Server and Get Response
    var res = await api.GetOrderTotalsAsync(req);

    //Now examine the results:
    Console.WriteLine("StartDate: {0}", res.StartDate);
    Console.WriteLine("EndDate: {0}", res.EndDate);

    foreach (var orderTotalByCurrency  in res.AcceptedByCurrency)
    {
        Console.WriteLine("CurrencyCode: {0}", orderTotalByCurrency.CurrencyCode);
        Console.WriteLine("Amount: {0}", orderTotalByCurrency.Amount);
        Console.WriteLine("Count: {0}", orderTotalByCurrency.Count);
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
    GetOrderTotalsRequest req = new GetOrderTotalsRequest();

    req.StartDate = DateTime.Today;
    req.EndDate = DateTime.Today;

    //Send Request to Server and Get Response
    GetOrderTotalsResponse res = api.GetOrderTotals(req);

    //Now examine the results:
    Console.WriteLine("StartDate: {0}", res.StartDate);
    Console.WriteLine("EndDate: {0}", res.EndDate);

    foreach (OrderTotalByCurrency orderTotalByCurrency  in res.AcceptedByCurrency)
    {
        Console.WriteLine("CurrencyCode: {0}", orderTotalByCurrency.CurrencyCode);
        Console.WriteLine("Amount: {0}", orderTotalByCurrency.Amount);
        Console.WriteLine("Count: {0}", orderTotalByCurrency.Count);
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
    Dim req as new GetOrderTotalsRequest()

    req.StartDate = DateTime.Today
    req.EndDate = DateTime.Today

    'Send Request to Server and Get Response
    Dim res As GetOrderTotalsResponse = api.GetOrderTotals(req)

    'Now examine the results:
    Console.WriteLine("StartDate: {0}", res.StartDate)
    Console.WriteLine("EndDate: {0}", res.EndDate)

    For Each orderTotalByCurrency As OrderTotalByCurrency In res.AcceptedByCurrency
        Console.WriteLine("CurrencyCode: {0}", orderTotalByCurrency.CurrencyCode)
        Console.WriteLine("Amount: {0}", orderTotalByCurrency.Amount)
        Console.WriteLine("Count: {0}", orderTotalByCurrency.Count)
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

    $req->StartDate = 1;
    $req->EndDate = 1;

    //Send Request to Server and Get Response
    $res = $api.GetOrderTotals($req);

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
    GetOrderTotalsRequest req = new GetOrderTotalsRequest();

    req.setStartDate(1);
    req.setEndDate(1);

    //Send Request to Server and Get Response
    GetOrderTotalsResponse res = api.getExigoApiSoap().getOrderTotals(req, auth);

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
https://api.exigo.com/3.0/csv/?method=GetOrderTotals
&ApiLoginName=String
&ApiPassword=String
&ApiCompany=String
&StartDate=DateTime
&EndDate=DateTime
Response FieldsStartDate,EndDate,CurrencyCode,Amount,Count
DateTime,DateTime,String,Decimal,Int32

                    © 2026 Exigo.
```

</details>

---

### GetPayments

> Gets payment record(s) for a customer or order.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | `GET /3.0/payment?customerID=1` |
| SOAP action | `https://api.exigo.com/GetPayments` |
| WSDL elements | `GetPaymentsRequest` → `GetPaymentsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetPayments |

#### Input

**`GetPaymentsRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Optional. Unique numeric identifier for a customer record. |
| `OrderID` | `Int32` | Optional. Unique numeric identifier for order record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |
| `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided. |

#### Output

**`GetPaymentsResponse`**

| Property | Type | Notes |
|---|---|---|
| `Payments` | `PaymentResponse[]` |  |

**`PaymentResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `PaymentID` | `Int32` |  |
| &nbsp;&nbsp;↳ `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| &nbsp;&nbsp;↳ `PaymentType` | `PaymentType` | Obsolete field. Please consider upgrading to PaymentTypeId.<br>**Values:** `Cash`, `CreditCard`, `Check`, `CreditVoucher`, `Net30`, `Net60`, `UseCredit`, `ACHDebit`, `BankDraft`, `BankWire`, `PointRedemtion`, `COD`, `MoneyOrder`, `BankDeposit`, `Other1`, `Other2`, `Other3`, `Wallet`, `Other4`, `Other5`, `Other6`, `Other7`, `Other8`, `Other9`, `Other10`, `Other11`, `Other12`, `Other13`, `Other14`, `Other15` |
| &nbsp;&nbsp;↳ `PaymentDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `Amount` | `Decimal` |  |
| &nbsp;&nbsp;↳ `OrderID` | `Int32` | Unique numeric identifier for order record. |
| &nbsp;&nbsp;↳ `CurrencyCode` | `String` |  |
| &nbsp;&nbsp;↳ `BillingName` | `String` |  |
| &nbsp;&nbsp;↳ `BillingAddress1` | `String` |  |
| &nbsp;&nbsp;↳ `BillingAddress2` | `String` |  |
| &nbsp;&nbsp;↳ `BillingCity` | `String` |  |
| &nbsp;&nbsp;↳ `BillingState` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `BillingZip` | `String` |  |
| &nbsp;&nbsp;↳ `BillingCountry` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `BankName` | `String` |  |
| &nbsp;&nbsp;↳ `Memo` | `String` |  |
| &nbsp;&nbsp;↳ `CreditCardNumberDisplay` | `String` |  |
| &nbsp;&nbsp;↳ `AuthorizationCode` | `String` |  |
| &nbsp;&nbsp;↳ `CreditCardType` | `Int32` | Optionally pass in Visa, Master Card, etc.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `CreditCardTypeDescription` | `String` |  |
| &nbsp;&nbsp;↳ `OrderKey` | `String` | Unique alpha numeric identifier for order record. |
| &nbsp;&nbsp;↳ `CustomerKey` | `String` | Unique alpha numeric identifier for customer record . |
| &nbsp;&nbsp;↳ `WalletTy` | `Int32` |  |
| &nbsp;&nbsp;↳ `PaymentTypeId` | `Int32` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/payment?customerID=1
  &orderID=1
  &customerKey=1
  &orderKey=DDks8235txcid
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "payments": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetPayments"

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
    <GetPaymentsRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <OrderID>int</OrderID>
      <CustomerKey>string</CustomerKey>
      <OrderKey>string</OrderKey>
    </GetPaymentsRequest>
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
    <GetPaymentsResult xmlns="http://api.exigo.com/">
      <Payments>
        <PaymentResponse>
          <PaymentID>int</PaymentID>
          <CustomerID>int</CustomerID>
          <PaymentType>Cash or CreditCard or Check or CreditVoucher or Net30 or Net60 or ACHDebit or UseCredit or BankDraft or BankWire or PointRedemtion or COD or MoneyOrder or BankDeposit or Other1 or Other2 or Other3 or Wallet or Other4 or Other5 or Other6 or Other7 or Other8 or Other9 or Other10 or Other11 or Other12 or Other13 or Other14 or Other15</PaymentType>
          <PaymentDate>dateTime</PaymentDate>
          <Amount>decimal</Amount>
          <OrderID>int</OrderID>
          <CurrencyCode>string</CurrencyCode>
          <BillingName>string</BillingName>
          <BillingAddress1>string</BillingAddress1>
          <BillingAddress2>string</BillingAddress2>
          <BillingCity>string</BillingCity>
          <BillingState>string</BillingState>
          <BillingZip>string</BillingZip>
          <BillingCountry>string</BillingCountry>
          <BankName>string</BankName>
          <Memo>string</Memo>
          <CreditCardNumberDisplay>string</CreditCardNumberDisplay>
          <AuthorizationCode>string</AuthorizationCode>
          <CreditCardType>int</CreditCardType>
          <CreditCardTypeDescription>string</CreditCardTypeDescription>
          <OrderKey>string</OrderKey>
          <CustomerKey>string</CustomerKey>
          <WalletTy>int</WalletTy>
          <PaymentTypeId>int</PaymentTypeId>
        </PaymentResponse>
      </Payments>
    </GetPaymentsResult>
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
    var req = new GetPaymentsRequest();

    req.CustomerID = 1;             //Unique numeric identifier for a customer record.
    req.OrderID = 1;                //Unique numeric identifier for order record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.OrderKey = "DDks8235txcid"; //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    var res = await api.GetPaymentsAsync(req);

    //Now examine the results:

    foreach (var payment  in res.Payments)
    {
        Console.WriteLine("CustomerID: {0}", payment.CustomerID);
        Console.WriteLine("Amount: {0}", payment.Amount);
        Console.WriteLine("OrderID: {0}", payment.OrderID);
        Console.WriteLine("BillingName: {0}", payment.BillingName);
        Console.WriteLine("BillingAddress1: {0}", payment.BillingAddress1);
        Console.WriteLine("BillingAddress2: {0}", payment.BillingAddress2);
        Console.WriteLine("BillingCity: {0}", payment.BillingCity);
        Console.WriteLine("BillingZip: {0}", payment.BillingZip);
        Console.WriteLine("BankName: {0}", payment.BankName);
        Console.WriteLine("Memo: {0}", payment.Memo);
        Console.WriteLine("CreditCardNumberDisplay: {0}", payment.CreditCardNumberDisplay);
        Console.WriteLine("AuthorizationCode: {0}", payment.AuthorizationCode);
        Console.WriteLine("CreditCardTypeDescription: {0}", payment.CreditCardTypeDescription);
        Console.WriteLine("OrderKey: {0}", payment.OrderKey);
        Console.WriteLine("CustomerKey: {0}", payment.CustomerKey);
        Console.WriteLine("WalletTy: {0}", payment.WalletTy);
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
    GetPaymentsRequest req = new GetPaymentsRequest();

    req.CustomerID = 1;             //Unique numeric identifier for a customer record.
    req.OrderID = 1;                //Unique numeric identifier for order record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.OrderKey = "DDks8235txcid"; //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    GetPaymentsResponse res = api.GetPayments(req);

    //Now examine the results:

    foreach (PaymentResponse payment  in res.Payments)
    {
        Console.WriteLine("CustomerID: {0}", payment.CustomerID);
        Console.WriteLine("Amount: {0}", payment.Amount);
        Console.WriteLine("OrderID: {0}", payment.OrderID);
        Console.WriteLine("BillingName: {0}", payment.BillingName);
        Console.WriteLine("BillingAddress1: {0}", payment.BillingAddress1);
        Console.WriteLine("BillingAddress2: {0}", payment.BillingAddress2);
        Console.WriteLine("BillingCity: {0}", payment.BillingCity);
        Console.WriteLine("BillingZip: {0}", payment.BillingZip);
        Console.WriteLine("BankName: {0}", payment.BankName);
        Console.WriteLine("Memo: {0}", payment.Memo);
        Console.WriteLine("CreditCardNumberDisplay: {0}", payment.CreditCardNumberDisplay);
        Console.WriteLine("AuthorizationCode: {0}", payment.AuthorizationCode);
        Console.WriteLine("CreditCardTypeDescription: {0}", payment.CreditCardTypeDescription);
        Console.WriteLine("OrderKey: {0}", payment.OrderKey);
        Console.WriteLine("CustomerKey: {0}", payment.CustomerKey);
        Console.WriteLine("WalletTy: {0}", payment.WalletTy);
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
    Dim req as new GetPaymentsRequest()

    req.CustomerID = 1
    req.OrderID = 1
    req.CustomerKey = "1"
    req.OrderKey = "DDks8235txcid"

    'Send Request to Server and Get Response
    Dim res As GetPaymentsResponse = api.GetPayments(req)

    'Now examine the results:

    For Each payment As PaymentResponse In res.Payments
        Console.WriteLine("CustomerID: {0}", payment.CustomerID)
        Console.WriteLine("Amount: {0}", payment.Amount)
        Console.WriteLine("OrderID: {0}", payment.OrderID)
        Console.WriteLine("BillingName: {0}", payment.BillingName)
        Console.WriteLine("BillingAddress1: {0}", payment.BillingAddress1)
        Console.WriteLine("BillingAddress2: {0}", payment.BillingAddress2)
        Console.WriteLine("BillingCity: {0}", payment.BillingCity)
        Console.WriteLine("BillingZip: {0}", payment.BillingZip)
        Console.WriteLine("BankName: {0}", payment.BankName)
        Console.WriteLine("Memo: {0}", payment.Memo)
        Console.WriteLine("CreditCardNumberDisplay: {0}", payment.CreditCardNumberDisplay)
        Console.WriteLine("AuthorizationCode: {0}", payment.AuthorizationCode)
        Console.WriteLine("CreditCardTypeDescription: {0}", payment.CreditCardTypeDescription)
        Console.WriteLine("OrderKey: {0}", payment.OrderKey)
        Console.WriteLine("CustomerKey: {0}", payment.CustomerKey)
        Console.WriteLine("WalletTy: {0}", payment.WalletTy)
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
    $req->OrderID = 1;
    $req->CustomerKey = "1";
    $req->OrderKey = "DDks8235txcid";

    //Send Request to Server and Get Response
    $res = $api.GetPayments($req);

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
    GetPaymentsRequest req = new GetPaymentsRequest();

    req.setCustomerID(1);
    req.setOrderID(1);
    req.setCustomerKey("1");
    req.setOrderKey("DDks8235txcid");

    //Send Request to Server and Get Response
    GetPaymentsResponse res = api.getExigoApiSoap().getPayments(req, auth);

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

### GetReport

> Returns a custom report in dataset format.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/GetReport` |
| WSDL elements | `GetReportRequest` → `GetReportResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetReport |

#### Input

**`GetReportRequest`**

| Property | Type | Notes |
|---|---|---|
| `ReportID` | `Int32` | Unique Report ID.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Parameters` | `ReportParameterRequest[]` | **Lookup:** company-specific list (see company-lists.md) |

**`ReportParameterRequest`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `ParameterName` | `String` | Optional. |
| &nbsp;&nbsp;↳ `Value` | `String` | Optional. |

#### Output

**`GetReportResponse`**

| Property | Type | Notes |
|---|---|---|
| `ReportData` | `DataSet` |  |

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetReport"

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
    <GetReportRequest xmlns="http://api.exigo.com/">
      <ReportID>int</ReportID>
      <Parameters>
        <ReportParameterRequest>
          <ParameterName>string</ParameterName>
          <Value>string</Value>
        </ReportParameterRequest>
      </Parameters>
    </GetReportRequest>
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
    <GetReportResult xmlns="http://api.exigo.com/">
      <ReportData>
        <xsd:schema>schema</xsd:schema>xml</ReportData>
    </GetReportResult>
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
    var req = new GetReportRequest();

    req.ReportID = 1;               //Unique Report ID

    //Add Parameters
    var parameters = new List<ReportParameterRequest>();

    var parameter1 = new ReportParameterRequest();
    parameter1.ParameterName = "1";
    parameter1.Value = "1";
    parameters.Add(parameter1);

    var parameter2 = new ReportParameterRequest();
    parameter2.ParameterName = "2";
    parameter2.Value = "2";
    parameters.Add(parameter2);

    //Now attach the list to the request
    req.Parameters = parameters.ToArray();

    //Send Request to Server and Get Response
    var res = await api.GetReportAsync(req);

    //Now examine the results:
    Console.WriteLine("ReportData: {0}", res.ReportData);
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
    GetReportRequest req = new GetReportRequest();

    req.ReportID = 1;               //Unique Report ID

    //Add Parameters
    List<ReportParameterRequest> parameters = new List<ReportParameterRequest>();

    ReportParameterRequest parameter1 = new ReportParameterRequest();
    parameter1.ParameterName = "1";
    parameter1.Value = "1";
    parameters.Add(parameter1);

    ReportParameterRequest parameter2 = new ReportParameterRequest();
    parameter2.ParameterName = "2";
    parameter2.Value = "2";
    parameters.Add(parameter2);

    //Now attach the list to the request
    req.Parameters = parameters.ToArray();

    //Send Request to Server and Get Response
    GetReportResponse res = api.GetReport(req);

    //Now examine the results:
    Console.WriteLine("ReportData: {0}", res.ReportData);
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
    Dim req as new GetReportRequest()

    req.ReportID = 1

    'Add Parameters
    Dim parameters As New List(Of ReportParameterRequest)()

    Dim parameter1 as new ReportParameterRequest()
    parameter1.ParameterName = "1"
    parameter1.Value = "1"
    parameters.Add(parameter1)

    Dim parameter2 as new ReportParameterRequest()
    parameter2.ParameterName = "2"
    parameter2.Value = "2"
    parameters.Add(parameter2)

    'Now attach the list to the request
    req.Parameters = parameters.ToArray()

    'Send Request to Server and Get Response
    Dim res As GetReportResponse = api.GetReport(req)

    'Now examine the results:
    Console.WriteLine("ReportData: {0}", res.ReportData)
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

    $req->ReportID = 1;

    //Add Parameters

    $parameter1->ParameterName = "1";
    $parameter1->Value = "1";

    $parameter2->ParameterName = "2";
    $parameter2->Value = "2";

    //Now attach the list to the request
    req.Parameters = array(parameter1,parameter2);

    //Send Request to Server and Get Response
    $res = $api.GetReport($req);

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
    GetReportRequest req = new GetReportRequest();

    req.setReportID(1);

    //Add Parameters
    ArrayOfReportParameterRequest parameters = new ArrayOfReportParameterRequest();

    ReportParameterRequest parameter1 = new ReportParameterRequest();
    parameter1.setParameterName("1");
    parameter1.setValue("1");
    parameters.Add(parameter1);

    ReportParameterRequest parameter2 = new ReportParameterRequest();
    parameter2.setParameterName("2");
    parameter2.setValue("2");
    parameters.Add(parameter2);

    //Now attach the list to the request
    req.setParameters(parameters);

    //Send Request to Server and Get Response
    GetReportResponse res = api.getExigoApiSoap().getReport(req, auth);

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

### GetResourceSetSubscriptionUpdates

> Gets all resource item updates for a list of resource subscriptions

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | `GET /3.0/resourceset/subscriptions/updatesAuthorization:` |
| SOAP action | `https://api.exigo.com/GetResourceSetSubscriptionUpdates` |
| WSDL elements | `GetResourceSetSubscriptionUpdatesRequest` → `GetResourceSetSubscriptionUpdatesResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetResourceSetSubscriptionUpdates |

#### Input

**`GetResourceSetSubscriptionUpdatesRequest`**

| Property | Type | Notes |
|---|---|---|
| `ResourceSubscriptions` | `ResourceSetSubscriptionCheckIn[]` | Array of ResourceSetSubscriptionCheckIn items. |
| `Full` | `Boolean` | Setting this to true will ignore the InstalledReleaseDate. |

**`ResourceSetSubscriptionCheckIn`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `SubscriptionKey` | `String` |  |
| &nbsp;&nbsp;↳ `EnvironmentCode` | `String` |  |
| &nbsp;&nbsp;↳ `InstalledVersion` | `String` | Optional. |
| &nbsp;&nbsp;↳ `InstalledReleaseDate` | `DateTime` | Optional. |
| &nbsp;&nbsp;↳ `MachineName` | `String` | Optional. |
| &nbsp;&nbsp;↳ `HostAssemblyName` | `String` | Optional. |
| &nbsp;&nbsp;↳ `ComponentVersion` | `String` | Optional. |

#### Output

**`GetResourceSetSubscriptionUpdatesResponse`**

| Property | Type | Notes |
|---|---|---|
| `Updates` | `ResourceSubscriptionUpdate[]` | Array of ResourceSubscriptionUpdate items. |

**`ResourceSubscriptionUpdate`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `Subscription` | `ResourceSubscription` |  |
| &nbsp;&nbsp;↳ `CultureCodeItems` | `CultureCodeItem` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/resourceset/subscriptions/updatesAuthorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "updates": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetResourceSetSubscriptionUpdates"

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
    <GetResourceSetSubscriptionUpdatesRequest xmlns="http://api.exigo.com/">
      <ResourceSubscriptions>
        <ResourceSetSubscriptionCheckIn>
          <SubscriptionKey>string</SubscriptionKey>
          <EnvironmentCode>string</EnvironmentCode>
          <InstalledVersion>string</InstalledVersion>
          <InstalledReleaseDate>dateTime</InstalledReleaseDate>
          <MachineName>string</MachineName>
          <HostAssemblyName>string</HostAssemblyName>
          <ComponentVersion>string</ComponentVersion>
        </ResourceSetSubscriptionCheckIn>
      </ResourceSubscriptions>
      <Full>boolean</Full>
    </GetResourceSetSubscriptionUpdatesRequest>
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
    <GetResourceSetSubscriptionUpdatesResult xmlns="http://api.exigo.com/">
      <Updates>
        <ResourceSubscriptionUpdate>
          <Subscription>
            <SubscriptionKey>string</SubscriptionKey>
            <EnvironmentCode>string</EnvironmentCode>
            <Version>string</Version>
            <ReleaseDate>dateTime</ReleaseDate>
            <ClassName>string</ClassName>
            <Namespace>string</Namespace>
          </Subscription>
          <CultureCodeItems>
            <CultureCodeItem>
              <CultureCode>string</CultureCode>
              <ResourceItems
                xsi:nil="true" />
            </CultureCodeItem>
          </CultureCodeItems>
        </ResourceSubscriptionUpdate>
      </Updates>
    </GetResourceSetSubscriptionUpdatesResult>
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
    var req = new GetResourceSetSubscriptionUpdatesRequest();

    //Send Request to Server and Get Response
    var res = await api.GetResourceSetSubscriptionUpdatesAsync(req);

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
    GetResourceSetSubscriptionUpdatesRequest req = new GetResourceSetSubscriptionUpdatesRequest();

    //Send Request to Server and Get Response
    GetResourceSetSubscriptionUpdatesResponse res = api.GetResourceSetSubscriptionUpdates(req);

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
    Dim req as new GetResourceSetSubscriptionUpdatesRequest()

    'Send Request to Server and Get Response
    Dim res As GetResourceSetSubscriptionUpdatesResponse = api.GetResourceSetSubscriptionUpdates(req)

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
    $res = $api.GetResourceSetSubscriptionUpdates($req);

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
    GetResourceSetSubscriptionUpdatesRequest req = new GetResourceSetSubscriptionUpdatesRequest();

    //Send Request to Server and Get Response
    GetResourceSetSubscriptionUpdatesResponse res = api.getExigoApiSoap().getResourceSetSubscriptionUpdates(req, auth);

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

### GetSandbox

> Get List of Sandboxes

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/GetSandbox` |
| WSDL elements | `GetSandboxRequest` → `GetSandboxResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetSandbox |

#### Input

**`GetSandboxRequest`**

| Property | Type | Notes |
|---|---|---|
| `SandboxID` | `Int32` | Optional. Return sandbox instance specified. |

#### Output

**`GetSandboxResponse`**

| Property | Type | Notes |
|---|---|---|
| `Sandbox` | `Sandbox` |  |
| `Sandboxes` | `Sandbox` |  |

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetSandbox"

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
    <GetSandboxRequest xmlns="http://api.exigo.com/">
      <SandboxID>int</SandboxID>
    </GetSandboxRequest>
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
    <GetSandboxResult xmlns="http://api.exigo.com/">
      <Sandbox>
        <CompanyID>int</CompanyID>
        <SandboxID>int</SandboxID>
        <Description>string</Description>
        <Type>Sandbox or Commission or Premium</Type>
        <Status>string</Status>
        <StartDate>dateTime</StartDate>
        <PercentComplete>decimal</PercentComplete>
        <Hours>decimal</Hours>
        <AllowVolumePush>boolean</AllowVolumePush>
        <AllowBiSync>boolean</AllowBiSync>
        <SyncFilterDays>int</SyncFilterDays>
        <UseRealTimeBackup>boolean</UseRealTimeBackup>
      </Sandbox>
      <Sandboxes />
    </GetSandboxResult>
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
    var req = new GetSandboxRequest();

    req.SandboxID = 1;              //Return sandbox instance specified

    //Send Request to Server and Get Response
    var res = await api.GetSandboxAsync(req);

    //Now examine the results:
    Console.WriteLine("Sandbox: {0}", res.Sandbox);
    Console.WriteLine("Sandboxes: {0}", res.Sandboxes);
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
    GetSandboxRequest req = new GetSandboxRequest();

    req.SandboxID = 1;              //Return sandbox instance specified

    //Send Request to Server and Get Response
    GetSandboxResponse res = api.GetSandbox(req);

    //Now examine the results:
    Console.WriteLine("Sandbox: {0}", res.Sandbox);
    Console.WriteLine("Sandboxes: {0}", res.Sandboxes);
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
    Dim req as new GetSandboxRequest()

    req.SandboxID = 1

    'Send Request to Server and Get Response
    Dim res As GetSandboxResponse = api.GetSandbox(req)

    'Now examine the results:
    Console.WriteLine("Sandbox: {0}", res.Sandbox)
    Console.WriteLine("Sandboxes: {0}", res.Sandboxes)
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

    $req->SandboxID = 1;

    //Send Request to Server and Get Response
    $res = $api.GetSandbox($req);

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
    GetSandboxRequest req = new GetSandboxRequest();

    req.setSandboxID(1);

    //Send Request to Server and Get Response
    GetSandboxResponse res = api.getExigoApiSoap().getSandbox(req, auth);

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

### GetShipMethods

> This has been deprecated. Use CalculateOrder with ReturnShipMethods=true instead.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/GetShipMethods` |
| WSDL elements | `GetShipMethodsRequest` → `GetShipMethodsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetShipMethods |

#### Input

**`GetShipMethodsRequest`**

| Property | Type | Notes |
|---|---|---|
| `WarehouseID` | `Int32` | Unique location for orders.<br>**Lookup:** company-specific list (see company-lists.md) |
| `CurrencyCode` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `OrderSubTotal` | `Decimal` |  |
| `OrderWieght` | `Decimal` |  |

#### Output

**`GetShipMethodsResponse`**

| Property | Type | Notes |
|---|---|---|
| `ShipMethods` | `ShipMethodResponse[]` |  |

**`ShipMethodResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `ShipMethodID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Description` | `String` |  |
| &nbsp;&nbsp;↳ `ShippingAmount` | `Decimal` |  |

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetShipMethods"

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
    <GetShipMethodsRequest xmlns="http://api.exigo.com/">
      <WarehouseID>int</WarehouseID>
      <CurrencyCode>string</CurrencyCode>
      <OrderSubTotal>decimal</OrderSubTotal>
      <OrderWieght>decimal</OrderWieght>
    </GetShipMethodsRequest>
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
    <GetShipMethodsResult xmlns="http://api.exigo.com/">
      <ShipMethods>
        <ShipMethodResponse>
          <ShipMethodID>int</ShipMethodID>
          <Description>string</Description>
          <ShippingAmount>decimal</ShippingAmount>
        </ShipMethodResponse>
      </ShipMethods>
    </GetShipMethodsResult>
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
    var req = new GetShipMethodsRequest();

    req.WarehouseID = 1;            //Unique location for orders
    req.CurrencyCode = "usd";
    req.OrderSubTotal = 1;
    req.OrderWieght = 1;

    //Send Request to Server and Get Response
    var res = await api.GetShipMethodsAsync(req);

    //Now examine the results:

    foreach (var shipMethod  in res.ShipMethods)
    {
        Console.WriteLine("ShipMethodID: {0}", shipMethod.ShipMethodID);
        Console.WriteLine("Description: {0}", shipMethod.Description);
        Console.WriteLine("ShippingAmount: {0}", shipMethod.ShippingAmount);
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
    GetShipMethodsRequest req = new GetShipMethodsRequest();

    req.WarehouseID = 1;            //Unique location for orders
    req.CurrencyCode = "usd";
    req.OrderSubTotal = 1;
    req.OrderWieght = 1;

    //Send Request to Server and Get Response
    GetShipMethodsResponse res = api.GetShipMethods(req);

    //Now examine the results:

    foreach (ShipMethodResponse shipMethod  in res.ShipMethods)
    {
        Console.WriteLine("ShipMethodID: {0}", shipMethod.ShipMethodID);
        Console.WriteLine("Description: {0}", shipMethod.Description);
        Console.WriteLine("ShippingAmount: {0}", shipMethod.ShippingAmount);
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
    Dim req as new GetShipMethodsRequest()

    req.WarehouseID = 1
    req.CurrencyCode = "usd"
    req.OrderSubTotal = 1
    req.OrderWieght = 1

    'Send Request to Server and Get Response
    Dim res As GetShipMethodsResponse = api.GetShipMethods(req)

    'Now examine the results:

    For Each shipMethod As ShipMethodResponse In res.ShipMethods
        Console.WriteLine("ShipMethodID: {0}", shipMethod.ShipMethodID)
        Console.WriteLine("Description: {0}", shipMethod.Description)
        Console.WriteLine("ShippingAmount: {0}", shipMethod.ShippingAmount)
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

    $req->WarehouseID = 1;
    $req->CurrencyCode = "usd";
    $req->OrderSubTotal = 1;
    $req->OrderWieght = 1;

    //Send Request to Server and Get Response
    $res = $api.GetShipMethods($req);

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
    GetShipMethodsRequest req = new GetShipMethodsRequest();

    req.setWarehouseID(1);
    req.setCurrencyCode("usd");
    req.setOrderSubTotal(1);
    req.setOrderWieght(1);

    //Send Request to Server and Get Response
    GetShipMethodsResponse res = api.getExigoApiSoap().getShipMethods(req, auth);

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

### GetShoppingCart

> Gets a existing Shopping Cart Session.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/GetShoppingCart` |
| WSDL elements | `GetShoppingCartRequest` → `GetShoppingCartResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetShoppingCart |

#### Input

**`GetShoppingCartRequest`**

| Property | Type | Notes |
|---|---|---|
| `ShoppingID` | `String` | Optional. |

#### Output

**`GetShoppingCartResponse`**

| Property | Type | Notes |
|---|---|---|
| `ExistingOrderID` | `Int32` | Unique numeric identifier for order record. |
| `ExistingAutoOrderID` | `Int32` |  |
| `Details` | `OrderDetailResponse[]` |  |

**`OrderDetailResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `OrderDetailID` | `Guid` |  |
| &nbsp;&nbsp;↳ `ParentOrderDetailID` | `Guid` |  |
| &nbsp;&nbsp;↳ `ItemCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Description` | `String` |  |
| &nbsp;&nbsp;↳ `Quantity` | `Decimal` |  |
| &nbsp;&nbsp;↳ `PriceEach` | `Decimal` |  |
| &nbsp;&nbsp;↳ `PriceTotal` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Tax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `WeightEach` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Weight` | `Decimal` |  |
| &nbsp;&nbsp;↳ `BusinessVolumeEach` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CommissionableVolumeEach` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CommissionableVolume` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other1Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other1` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Other2Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other2` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Other3Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other3` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Other4Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other4` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Other5Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other5` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Other6Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other6` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Other7Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other7` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Other8Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other8` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Other9Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other9` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Other10Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other10` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `ParentItemCode` | `String` |  |
| &nbsp;&nbsp;↳ `Taxable` | `Decimal` |  |
| &nbsp;&nbsp;↳ `FedTax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `StateTax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CityTax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CityLocalTax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CountyTax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CountyLocalTax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `ManualTax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `IsStateTaxOverride` | `Boolean` |  |
| &nbsp;&nbsp;↳ `OrderLine` | `Int32` |  |
| &nbsp;&nbsp;↳ `Reference1` | `String` |  |
| &nbsp;&nbsp;↳ `ShippingPriceEach` | `Decimal` |  |
| &nbsp;&nbsp;↳ `HandlingFee` | `Decimal` |  |
| &nbsp;&nbsp;↳ `BusinessVolume` | `Decimal` |  |

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetShoppingCart"

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
    <GetShoppingCartRequest xmlns="http://api.exigo.com/">
      <ShoppingID>string</ShoppingID>
    </GetShoppingCartRequest>
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
    <GetShoppingCartResult xmlns="http://api.exigo.com/">
      <ExistingOrderID>int</ExistingOrderID>
      <ExistingAutoOrderID>int</ExistingAutoOrderID>
      <Details>
        <OrderDetailResponse>
          <OrderDetailID>guid</OrderDetailID>
          <ParentOrderDetailID>guid</ParentOrderDetailID>
          <ItemCode>string</ItemCode>
          <Description>string</Description>
          <Quantity>decimal</Quantity>
          <PriceEach>decimal</PriceEach>
          <PriceTotal>decimal</PriceTotal>
          <Tax>decimal</Tax>
          <WeightEach>decimal</WeightEach>
          <Weight>decimal</Weight>
          <BusinessVolumeEach>decimal</BusinessVolumeEach>
          <BusinesVolume>decimal</BusinesVolume>
          <CommissionableVolumeEach>decimal</CommissionableVolumeEach>
          <CommissionableVolume>decimal</CommissionableVolume>
          <Other1Each>decimal</Other1Each>
          <Other1>decimal</Other1>
          <Other2Each>decimal</Other2Each>
          <Other2>decimal</Other2>
          <Other3Each>decimal</Other3Each>
          <Other3>decimal</Other3>
          <Other4Each>decimal</Other4Each>
          <Other4>decimal</Other4>
          <Other5Each>decimal</Other5Each>
          <Other5>decimal</Other5>
          <Other6Each>decimal</Other6Each>
          <Other6>decimal</Other6>
          <Other7Each>decimal</Other7Each>
          <Other7>decimal</Other7>
          <Other8Each>decimal</Other8Each>
          <Other8>decimal</Other8>
          <Other9Each>decimal</Other9Each>
          <Other9>decimal</Other9>
          <Other10Each>decimal</Other10Each>
          <Other10>decimal</Other10>
          <ParentItemCode>string</ParentItemCode>
          <Taxable>decimal</Taxable>
          <FedTax>decimal</FedTax>
          <StateTax>decimal</StateTax>
          <CityTax>decimal</CityTax>
          <CityLocalTax>decimal</CityLocalTax>
          <CountyTax>decimal</CountyTax>
          <CountyLocalTax>decimal</CountyLocalTax>
          <ManualTax>decimal</ManualTax>
          <IsStateTaxOverride>boolean</IsStateTaxOverride>
          <OrderLine>int</OrderLine>
          <Reference1>string</Reference1>
          <ShippingPriceEach>decimal</ShippingPriceEach>
          <HandlingFee>decimal</HandlingFee>
          <BusinessVolume>decimal</BusinessVolume>
        </OrderDetailResponse>
      </Details>
    </GetShoppingCartResult>
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
    var req = new GetShoppingCartRequest();

    req.ShoppingID = "1";

    //Send Request to Server and Get Response
    var res = await api.GetShoppingCartAsync(req);

    //Now examine the results:
    Console.WriteLine("ExistingOrderID: {0}", res.ExistingOrderID);
    Console.WriteLine("ExistingAutoOrderID: {0}", res.ExistingAutoOrderID);

    foreach (var orderDetail  in res.Details)
    {
        Console.WriteLine("OrderDetailID: {0}", orderDetail.OrderDetailID);
        Console.WriteLine("ParentOrderDetailID: {0}", orderDetail.ParentOrderDetailID);
        Console.WriteLine("ItemCode: {0}", orderDetail.ItemCode);
        Console.WriteLine("Description: {0}", orderDetail.Description);
        Console.WriteLine("Quantity: {0}", orderDetail.Quantity);
        Console.WriteLine("BusinesVolume: {0}", orderDetail.BusinesVolume);
        Console.WriteLine("OrderLine: {0}", orderDetail.OrderLine);
        Console.WriteLine("Reference1: {0}", orderDetail.Reference1);
        Console.WriteLine("ShippingPriceEach: {0}", orderDetail.ShippingPriceEach);
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
    GetShoppingCartRequest req = new GetShoppingCartRequest();

    req.ShoppingID = "1";

    //Send Request to Server and Get Response
    GetShoppingCartResponse res = api.GetShoppingCart(req);

    //Now examine the results:
    Console.WriteLine("ExistingOrderID: {0}", res.ExistingOrderID);
    Console.WriteLine("ExistingAutoOrderID: {0}", res.ExistingAutoOrderID);

    foreach (OrderDetailResponse orderDetail  in res.Details)
    {
        Console.WriteLine("OrderDetailID: {0}", orderDetail.OrderDetailID);
        Console.WriteLine("ParentOrderDetailID: {0}", orderDetail.ParentOrderDetailID);
        Console.WriteLine("ItemCode: {0}", orderDetail.ItemCode);
        Console.WriteLine("Description: {0}", orderDetail.Description);
        Console.WriteLine("Quantity: {0}", orderDetail.Quantity);
        Console.WriteLine("BusinesVolume: {0}", orderDetail.BusinesVolume);
        Console.WriteLine("OrderLine: {0}", orderDetail.OrderLine);
        Console.WriteLine("Reference1: {0}", orderDetail.Reference1);
        Console.WriteLine("ShippingPriceEach: {0}", orderDetail.ShippingPriceEach);
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
    Dim req as new GetShoppingCartRequest()

    req.ShoppingID = "1"

    'Send Request to Server and Get Response
    Dim res As GetShoppingCartResponse = api.GetShoppingCart(req)

    'Now examine the results:
    Console.WriteLine("ExistingOrderID: {0}", res.ExistingOrderID)
    Console.WriteLine("ExistingAutoOrderID: {0}", res.ExistingAutoOrderID)

    For Each orderDetail As OrderDetailResponse In res.Details
        Console.WriteLine("OrderDetailID: {0}", orderDetail.OrderDetailID)
        Console.WriteLine("ParentOrderDetailID: {0}", orderDetail.ParentOrderDetailID)
        Console.WriteLine("ItemCode: {0}", orderDetail.ItemCode)
        Console.WriteLine("Description: {0}", orderDetail.Description)
        Console.WriteLine("Quantity: {0}", orderDetail.Quantity)
        Console.WriteLine("BusinesVolume: {0}", orderDetail.BusinesVolume)
        Console.WriteLine("OrderLine: {0}", orderDetail.OrderLine)
        Console.WriteLine("Reference1: {0}", orderDetail.Reference1)
        Console.WriteLine("ShippingPriceEach: {0}", orderDetail.ShippingPriceEach)
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

    $req->ShoppingID = "1";

    //Send Request to Server and Get Response
    $res = $api.GetShoppingCart($req);

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
    GetShoppingCartRequest req = new GetShoppingCartRequest();

    req.setShoppingID("1");

    //Send Request to Server and Get Response
    GetShoppingCartResponse res = api.getExigoApiSoap().getShoppingCart(req, auth);

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

### LoginCustomer

> Deprecated. Use AuthenticateCustomer instead.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/LoginCustomer` |
| WSDL elements | `LoginCustomerRequest` → `LoginCustomerResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=LoginCustomer |

#### Input

**`LoginCustomerRequest`**

| Property | Type | Notes |
|---|---|---|
| `LoginName` | `String` | Optional. |
| `Password` | `String` | Optional. |
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`LoginCustomerResponse`**

| Property | Type | Notes |
|---|---|---|
| `SessionID` | `String` |  |

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/LoginCustomer"

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
    <LoginCustomerRequest xmlns="http://api.exigo.com/">
      <LoginName>string</LoginName>
      <Password>string</Password>
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
    </LoginCustomerRequest>
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
    <LoginCustomerResult xmlns="http://api.exigo.com/">
      <SessionID>string</SessionID>
    </LoginCustomerResult>
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
    var req = new LoginCustomerRequest();

    req.LoginName = "1";
    req.Password = "1";
    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.LoginCustomerAsync(req);

    //Now examine the results:
    Console.WriteLine("SessionID: {0}", res.SessionID);
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
    LoginCustomerRequest req = new LoginCustomerRequest();

    req.LoginName = "1";
    req.Password = "1";
    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    LoginCustomerResponse res = api.LoginCustomer(req);

    //Now examine the results:
    Console.WriteLine("SessionID: {0}", res.SessionID);
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
    Dim req as new LoginCustomerRequest()

    req.LoginName = "1"
    req.Password = "1"
    req.CustomerID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As LoginCustomerResponse = api.LoginCustomer(req)

    'Now examine the results:
    Console.WriteLine("SessionID: {0}", res.SessionID)
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
    $req->CustomerID = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.LoginCustomer($req);

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
    LoginCustomerRequest req = new LoginCustomerRequest();

    req.setLoginName("1");
    req.setPassword("1");
    req.setCustomerID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    LoginCustomerResponse res = api.getExigoApiSoap().loginCustomer(req, auth);

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

### MergeCustomer

> Merges Order, Payments and AutoOrder data from two Customers

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/MergeCustomer` |
| WSDL elements | `MergeCustomerRequest` → `MergeCustomerResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=MergeCustomer |

#### Input

**`MergeCustomerRequest`**

| Property | Type | Notes |
|---|---|---|
| `ToCustomerID` | `Int32` |  |
| `FromCustomerID` | `Int32` |  |
| `ToCustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |
| `FromCustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`MergeCustomerResponse`**

_No properties._

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/MergeCustomer"

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
    <MergeCustomerRequest xmlns="http://api.exigo.com/">
      <ToCustomerID>int</ToCustomerID>
      <FromCustomerID>int</FromCustomerID>
      <ToCustomerKey>string</ToCustomerKey>
      <FromCustomerKey>string</FromCustomerKey>
    </MergeCustomerRequest>
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
    <MergeCustomerResult xmlns="http://api.exigo.com/" />
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
    var req = new MergeCustomerRequest();

    req.ToCustomerID = 1;
    req.FromCustomerID = 1;
    req.ToCustomerKey = "DDks8235txcid";//Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.FromCustomerKey = "DDks8235txcid";//Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.MergeCustomerAsync(req);

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
    MergeCustomerRequest req = new MergeCustomerRequest();

    req.ToCustomerID = 1;
    req.FromCustomerID = 1;
    req.ToCustomerKey = "DDks8235txcid";//Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.FromCustomerKey = "DDks8235txcid";//Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    MergeCustomerResponse res = api.MergeCustomer(req);

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
    Dim req as new MergeCustomerRequest()

    req.ToCustomerID = 1
    req.FromCustomerID = 1
    req.ToCustomerKey = "DDks8235txcid"
    req.FromCustomerKey = "DDks8235txcid"

    'Send Request to Server and Get Response
    Dim res As MergeCustomerResponse = api.MergeCustomer(req)

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

    $req->ToCustomerID = 1;
    $req->FromCustomerID = 1;
    $req->ToCustomerKey = "DDks8235txcid";
    $req->FromCustomerKey = "DDks8235txcid";

    //Send Request to Server and Get Response
    $res = $api.MergeCustomer($req);

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
    MergeCustomerRequest req = new MergeCustomerRequest();

    req.setToCustomerID(1);
    req.setFromCustomerID(1);
    req.setToCustomerKey("DDks8235txcid");
    req.setFromCustomerKey("DDks8235txcid");

    //Send Request to Server and Get Response
    MergeCustomerResponse res = api.getExigoApiSoap().mergeCustomer(req, auth);

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

### MoveEmail

>  Moves an email to a different folder.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/MoveEmail` |
| WSDL elements | `MoveEmailRequest` → `MoveEmailResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=MoveEmail |

#### Input

**`MoveEmailRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `MailID` | `Int32` |  |
| `ToMailFolderID` | `Int32` |  |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`MoveEmailResponse`**

_No properties._

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/MoveEmail"

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
    <MoveEmailRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <MailID>int</MailID>
      <ToMailFolderID>int</ToMailFolderID>
      <CustomerKey>string</CustomerKey>
    </MoveEmailRequest>
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
    <MoveEmailResult xmlns="http://api.exigo.com/" />
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
    var req = new MoveEmailRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.MailID = 1;
    req.ToMailFolderID = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.MoveEmailAsync(req);

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
    MoveEmailRequest req = new MoveEmailRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.MailID = 1;
    req.ToMailFolderID = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    MoveEmailResponse res = api.MoveEmail(req);

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
    Dim req as new MoveEmailRequest()

    req.CustomerID = 1
    req.MailID = 1
    req.ToMailFolderID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As MoveEmailResponse = api.MoveEmail(req)

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
    $req->MailID = 1;
    $req->ToMailFolderID = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.MoveEmail($req);

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
    MoveEmailRequest req = new MoveEmailRequest();

    req.setCustomerID(1);
    req.setMailID(1);
    req.setToMailFolderID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    MoveEmailResponse res = api.getExigoApiSoap().moveEmail(req, auth);

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

### Ping

>  Ping to create a speed baseline

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | `POST /3.0/orders/calculate` |
| SOAP action | `https://api.exigo.com/Ping` |
| WSDL elements | `input` → `PingResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=Ping |

#### Input

**`CalculateOrderRequest`**

| Property | Type | Notes |
|---|---|---|
| `CurrencyCode` | `String` |  |
| `WarehouseID` | `Int32` | Unique location for orders.<br>**Lookup:** company-specific list (see company-lists.md) |
| `ShipMethodID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| `PriceType` | `Int32` | Controls which price band to use.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Address1` | `String` | Optional. |
| `Address2` | `String` | Optional. |
| `Address3` | `String` | Optional. |
| `City` | `String` | Optional. |
| `State` | `String` |  |
| `Zip` | `String` | Optional. |
| `Country` | `String` |  |
| `County` | `String` | Optional. |
| `CustomerID` | `Int32` | Unique numeric identifier for a customer record. |
| `TaxRateOverride` | `Decimal` | Optional. |
| `ShippingAmountOverride` | `Decimal` | Optional. |
| `ReturnOrderID` | `Int32` | Optional. |
| `Other11` | `String` | Optional. |
| `Other12` | `String` | Optional. |
| `Other13` | `String` | Optional. |
| `Other14` | `String` | Optional. |
| `Other15` | `String` | Optional. |
| `Other16` | `String` | Optional. |
| `Other17` | `String` | Optional. |
| `Other18` | `String` | Optional. |
| `Other19` | `String` | Optional. |
| `Other20` | `String` | Optional. |
| `Details` | `OrderDetailRequest[]` | At least 1 item is required. |
| `ReturnShipMethods` | `Boolean` |  |
| `PartyID` | `Int32` | Optional. |
| `ReturnTrace` | `Boolean` | Optional. . Defaults to False. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |
| `ReturnOrderKey` | `String` | Optional. |
| `OrderID` | `Int32` | Optional. . Defaults to 0. |
| `OrderType` | `OrderType` | **Values:** `Default`, `CustomerService`, `ShoppingCart`, `WebWizard`, `AutoOrder`, `Import`, `BackOrder`, `ReplacementOrder`, `ReturnOrder`, `WebAutoOrder`, `TicketSystem`, `APIOrder`, `BackOrderParent`, `ChildOrder`, `Other1`, `Other2`, `Other3`, `Other4`, `Other5`, `Other6`, `Other7`, `Other8`, `Other9`, `Other10` |
| `OrderSubStatusTy` | `Int32` | Optional. |
| `AutoOrderId` | `Int32` | Optional. |
| `ReplacementOrderId` | `Int32` | Optional. |
| `DeclineCount` | `Int32` | Optional. . Defaults to 0. |
| `IsRMA` | `Boolean` | Optional. . Defaults to False. |
| `BackOrderFromId` | `Int32` | Optional. |
| `IsCommissionable` | `Boolean` | Optional. . Defaults to False. |
| `Flag1` | `Boolean` | Optional. . Defaults to False. |
| `Flag2` | `Boolean` | Optional. . Defaults to False. |
| `Flag3` | `Boolean` | Optional. . Defaults to False. |
| `ReturnCategoryId` | `Int32` | Optional. |
| `ReplacementCategoryId` | `Int32` | Optional. |

**`OrderDetailRequest`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `ItemCode` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `OrderDetailID` | `Guid` | Optional. Recommended to be filled for all dynamic kit items with proper parent-child relationships. |
| &nbsp;&nbsp;↳ `ParentOrderDetailID` | `Guid` | Optional. Recommended to be filled for all dynamic kit items with proper parent-child relationships. |
| &nbsp;&nbsp;↳ `Quantity` | `Decimal` |  |
| &nbsp;&nbsp;↳ `ParentItemCode` | `String` | Optional. Use only when building kits. |
| &nbsp;&nbsp;↳ `PriceEachOverride` | `Decimal` | Optional. Overrides item setup. |
| &nbsp;&nbsp;↳ `TaxableEachOverride` | `Decimal` | Optional. Overrides item setup. |
| &nbsp;&nbsp;↳ `ShippingPriceEachOverride` | `Decimal` | Optional. Overrides item setup. |
| &nbsp;&nbsp;↳ `BusinessVolumeEachOverride` | `Decimal` | Optional. Overrides item setup. |
| &nbsp;&nbsp;↳ `CommissionableVolumeEachOverride` | `Decimal` | Optional. Overrides item setup. |
| &nbsp;&nbsp;↳ `Other1EachOverride` | `Decimal` | Optional. Overrides item setup. |
| &nbsp;&nbsp;↳ `Other2EachOverride` | `Decimal` | Optional. Overrides item setup. |
| &nbsp;&nbsp;↳ `Other3EachOverride` | `Decimal` | Optional. Overrides item setup. |
| &nbsp;&nbsp;↳ `Other4EachOverride` | `Decimal` | Optional. Overrides item setup. |
| &nbsp;&nbsp;↳ `Other5EachOverride` | `Decimal` | Optional. Overrides item setup. |
| &nbsp;&nbsp;↳ `Other6EachOverride` | `Decimal` | Optional. Overrides item setup. |
| &nbsp;&nbsp;↳ `Other7EachOverride` | `Decimal` | Optional. Overrides item setup. |
| &nbsp;&nbsp;↳ `Other8EachOverride` | `Decimal` | Optional. Overrides item setup. |
| &nbsp;&nbsp;↳ `Other9EachOverride` | `Decimal` | Optional. Overrides item setup. |
| &nbsp;&nbsp;↳ `Other10EachOverride` | `Decimal` | Optional. Overrides item setup. |
| &nbsp;&nbsp;↳ `DescriptionOverride` | `String` | Optional. Overrides item setup. |
| &nbsp;&nbsp;↳ `Reference1` | `String` | Optional. Reference field. |
| &nbsp;&nbsp;↳ `AdvancedAutoOptions` | `AdvancedAutoOptionsRequest` | Optional. Advanced auto order options. |
| &nbsp;&nbsp;↳ `OrderLine` | `Int32` | Optional. Sets OrderLine if sent. |

#### Output

**`CalculateOrderResponse`**

| Property | Type | Notes |
|---|---|---|
| `Total` | `Decimal` |  |
| `SubTotal` | `Decimal` |  |
| `TaxTotal` | `Decimal` |  |
| `ShippingTotal` | `Decimal` |  |
| `DiscountTotal` | `Decimal` |  |
| `DiscountPercent` | `Decimal` |  |
| `WeightTotal` | `Decimal` |  |
| `BusinessVolumeTotal` | `Decimal` |  |
| `CommissionableVolumeTotal` | `Decimal` |  |
| `Other1Total` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| `Other2Total` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| `Other3Total` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| `Other4Total` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| `Other5Total` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| `Other6Total` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| `Other7Total` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| `Other8Total` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| `Other9Total` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| `Other10Total` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| `Other11` | `String` |  |
| `Other12` | `String` |  |
| `Other13` | `String` |  |
| `Other14` | `String` |  |
| `Other15` | `String` |  |
| `Other16` | `String` |  |
| `Other17` | `String` |  |
| `Other18` | `String` |  |
| `Other19` | `String` |  |
| `Other20` | `String` |  |
| `ShippingTax` | `Decimal` |  |
| `OrderTax` | `Decimal` |  |
| `FedTaxTotal` | `Decimal` |  |
| `StateTaxTotal` | `Decimal` |  |
| `Details` | `OrderDetailResponse[]` |  |
| `ShipMethods` | `ShipMethodResponse[]` |  |
| `Warnings` | `String` |  |
| `Trace` | `String` |  |
| `HandlingFeeTotal` | `Decimal` |  |
| `AutoOrderId` | `Int32` |  |
| `ReplacementOrderId` | `Int32` |  |
| `DeclineCount` | `Int32` |  |
| `IsRMA` | `Boolean` |  |
| `BackOrderFromId` | `Int32` |  |
| `IsCommissionable` | `Boolean` |  |
| `Flag1` | `Boolean` |  |
| `Flag2` | `Boolean` |  |
| `Flag3` | `Boolean` |  |
| `ReturnCategoryId` | `Int32` |  |
| `ReplacementCategoryId` | `Int32` |  |

**`OrderDetailResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `OrderDetailID` | `Guid` |  |
| &nbsp;&nbsp;↳ `ParentOrderDetailID` | `Guid` |  |
| &nbsp;&nbsp;↳ `ItemCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Description` | `String` |  |
| &nbsp;&nbsp;↳ `Quantity` | `Decimal` |  |
| &nbsp;&nbsp;↳ `PriceEach` | `Decimal` |  |
| &nbsp;&nbsp;↳ `PriceTotal` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Tax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `WeightEach` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Weight` | `Decimal` |  |
| &nbsp;&nbsp;↳ `BusinessVolumeEach` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CommissionableVolumeEach` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CommissionableVolume` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other1Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other1` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Other2Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other2` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Other3Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other3` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Other4Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other4` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Other5Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other5` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Other6Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other6` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Other7Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other7` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Other8Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other8` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Other9Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other9` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Other10Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other10` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `ParentItemCode` | `String` |  |
| &nbsp;&nbsp;↳ `Taxable` | `Decimal` |  |
| &nbsp;&nbsp;↳ `FedTax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `StateTax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CityTax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CityLocalTax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CountyTax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CountyLocalTax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `ManualTax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `IsStateTaxOverride` | `Boolean` |  |
| &nbsp;&nbsp;↳ `OrderLine` | `Int32` |  |
| &nbsp;&nbsp;↳ `Reference1` | `String` |  |
| &nbsp;&nbsp;↳ `ShippingPriceEach` | `Decimal` |  |
| &nbsp;&nbsp;↳ `HandlingFee` | `Decimal` |  |
| &nbsp;&nbsp;↳ `BusinessVolume` | `Decimal` |  |

**`ShipMethodResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `ShipMethodID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Description` | `String` |  |
| &nbsp;&nbsp;↳ `ShippingAmount` | `Decimal` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/orders/calculate HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "currencyCode": "1",
  "warehouseID": 1,
  "shipMethodID": 1,
  "priceType": 1,
  "address1": "",
  "address2": "",
  "address3": "",
  "city": "",
  "state": "1",
  "zip": "",
  "country": "1",
  "county": "",
  "customerID": 1,
  "details": null,
  "returnShipMethods": true,
  "partyID": 1,
  "customerKey": "DDks8235txcid",
  "orderType": null
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "total": null,
  "subTotal": null,
  "taxTotal": null,
  "shippingTotal": null,
  "discountTotal": null,
  "discountPercent": null,
  "weightTotal": null,
  "businessVolumeTotal": null,
  "commissionableVolumeTotal": null,
  "other1Total": null,
  "other2Total": null,
  "other3Total": null,
  "other4Total": null,
  "other5Total": null,
  "other6Total": null,
  "other7Total": null,
  "other8Total": null,
  "other9Total": null,
  "other10Total": null,
  "other11": "",
  "other12": "",
  "other13": "",
  "other14": "",
  "other15": "",
  "other16": "",
  "other17": "",
  "other18": "",
  "other19": "",
  "other20": "",
  "shippingTax": null,
  "orderTax": null,
  "fedTaxTotal": null,
  "stateTaxTotal": null,
  "details": null,
  "shipMethods": null,
  "warnings": "",
  "trace": "",
  "handlingFeeTotal": null,
  "autoOrderId": 1,
  "replacementOrderId": 1,
  "declineCount": 1,
  "isRMA": true,
  "backOrderFromId": 1,
  "isCommissionable": true,
  "flag1": true,
  "flag2": true,
  "flag3": true,
  "returnCategoryId": 1,
  "replacementCategoryId": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/Ping"

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
    <input xmlns="http://api.exigo.com/">
      <CurrencyCode>string</CurrencyCode>
      <WarehouseID>int</WarehouseID>
      <ShipMethodID>int</ShipMethodID>
      <PriceType>int</PriceType>
      <Address1>string</Address1>
      <Address2>string</Address2>
      <Address3>string</Address3>
      <City>string</City>
      <State>string</State>
      <Zip>string</Zip>
      <Country>string</Country>
      <County>string</County>
      <CustomerID>int</CustomerID>
      <TaxRateOverride>decimal</TaxRateOverride>
      <ShippingAmountOverride>decimal</ShippingAmountOverride>
      <ReturnOrderID>int</ReturnOrderID>
      <Other11>string</Other11>
      <Other12>string</Other12>
      <Other13>string</Other13>
      <Other14>string</Other14>
      <Other15>string</Other15>
      <Other16>string</Other16>
      <Other17>string</Other17>
      <Other18>string</Other18>
      <Other19>string</Other19>
      <Other20>string</Other20>
      <Details>
        <OrderDetailRequest>
          <ItemCode>string</ItemCode>
          <OrderDetailID>guid</OrderDetailID>
          <ParentOrderDetailID>guid</ParentOrderDetailID>
          <Quantity>decimal</Quantity>
          <ParentItemCode>string</ParentItemCode>
          <PriceEachOverride>decimal</PriceEachOverride>
          <TaxableEachOverride>decimal</TaxableEachOverride>
          <ShippingPriceEachOverride>decimal</ShippingPriceEachOverride>
          <BusinessVolumeEachOverride>decimal</BusinessVolumeEachOverride>
          <CommissionableVolumeEachOverride>decimal</CommissionableVolumeEachOverride>
          <Other1EachOverride>decimal</Other1EachOverride>
          <Other2EachOverride>decimal</Other2EachOverride>
          <Other3EachOverride>decimal</Other3EachOverride>
          <Other4EachOverride>decimal</Other4EachOverride>
          <Other5EachOverride>decimal</Other5EachOverride>
          <Other6EachOverride>decimal</Other6EachOverride>
          <Other7EachOverride>decimal</Other7EachOverride>
          <Other8EachOverride>decimal</Other8EachOverride>
          <Other9EachOverride>decimal</Other9EachOverride>
          <Other10EachOverride>decimal</Other10EachOverride>
          <DescriptionOverride>string</DescriptionOverride>
          <Reference1>string</Reference1>
          <AdvancedAutoOptions>
            <ProcessWhileDate>dateTime</ProcessWhileDate>
            <SkipUntilDate>dateTime</SkipUntilDate>
            <DetailStartDate>dateTime</DetailStartDate>
            <DetailEndDate>dateTime</DetailEndDate>
            <DetailInterval>int</DetailInterval>
          </AdvancedAutoOptions>
          <OrderLine>int</OrderLine>
        </OrderDetailRequest>
      </Details>
      <ReturnShipMethods>boolean</ReturnShipMethods>
      <PartyID>int</PartyID>
      <ReturnTrace>boolean</ReturnTrace>
      <CustomerKey>string</CustomerKey>
      <ReturnOrderKey>string</ReturnOrderKey>
      <OrderID>int</OrderID>
      <OrderType>Default or CustomerService or ShoppingCart or WebWizard or AutoOrder or Import or BackOrder or ReplacementOrder or ReturnOrder or WebAutoOrder or TicketSystem or APIOrder or BackOrderParent or ChildOrder or Other1 or Other2 or Other3 or Other4 or Other5 or Other6 or Other7 or Other8 or Other9 or Other10</OrderType>
      <OrderSubStatusTy>int</OrderSubStatusTy>
      <AutoOrderId>int</AutoOrderId>
      <ReplacementOrderId>int</ReplacementOrderId>
      <DeclineCount>int</DeclineCount>
      <IsRMA>boolean</IsRMA>
      <BackOrderFromId>int</BackOrderFromId>
      <IsCommissionable>boolean</IsCommissionable>
      <Flag1>boolean</Flag1>
      <Flag2>boolean</Flag2>
      <Flag3>boolean</Flag3>
      <ReturnCategoryId>int</ReturnCategoryId>
      <ReplacementCategoryId>int</ReplacementCategoryId>
    </input>
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
    <PingResult xmlns="http://api.exigo.com/">
      <Total>decimal</Total>
      <SubTotal>decimal</SubTotal>
      <TaxTotal>decimal</TaxTotal>
      <ShippingTotal>decimal</ShippingTotal>
      <DiscountTotal>decimal</DiscountTotal>
      <DiscountPercent>decimal</DiscountPercent>
      <WeightTotal>decimal</WeightTotal>
      <BusinessVolumeTotal>decimal</BusinessVolumeTotal>
      <CommissionableVolumeTotal>decimal</CommissionableVolumeTotal>
      <Other1Total>decimal</Other1Total>
      <Other2Total>decimal</Other2Total>
      <Other3Total>decimal</Other3Total>
      <Other4Total>decimal</Other4Total>
      <Other5Total>decimal</Other5Total>
      <Other6Total>decimal</Other6Total>
      <Other7Total>decimal</Other7Total>
      <Other8Total>decimal</Other8Total>
      <Other9Total>decimal</Other9Total>
      <Other10Total>decimal</Other10Total>
      <Other11>string</Other11>
      <Other12>string</Other12>
      <Other13>string</Other13>
      <Other14>string</Other14>
      <Other15>string</Other15>
      <Other16>string</Other16>
      <Other17>string</Other17>
      <Other18>string</Other18>
      <Other19>string</Other19>
      <Other20>string</Other20>
      <ShippingTax>decimal</ShippingTax>
      <OrderTax>decimal</OrderTax>
      <FedTaxTotal>decimal</FedTaxTotal>
      <StateTaxTotal>decimal</StateTaxTotal>
      <Details>
        <OrderDetailResponse>
          <OrderDetailID>guid</OrderDetailID>
          <ParentOrderDetailID>guid</ParentOrderDetailID>
          <ItemCode>string</ItemCode>
          <Description>string</Description>
          <Quantity>decimal</Quantity>
          <PriceEach>decimal</PriceEach>
          <PriceTotal>decimal</PriceTotal>
          <Tax>decimal</Tax>
          <WeightEach>decimal</WeightEach>
          <Weight>decimal</Weight>
          <BusinessVolumeEach>decimal</BusinessVolumeEach>
          <BusinesVolume>decimal</BusinesVolume>
          <CommissionableVolumeEach>decimal</CommissionableVolumeEach>
          <CommissionableVolume>decimal</CommissionableVolume>
          <Other1Each>decimal</Other1Each>
          <Other1>decimal</Other1>
          <Other2Each>decimal</Other2Each>
          <Other2>decimal</Other2>
          <Other3Each>decimal</Other3Each>
          <Other3>decimal</Other3>
          <Other4Each>decimal</Other4Each>
          <Other4>decimal</Other4>
          <Other5Each>decimal</Other5Each>
          <Other5>decimal</Other5>
          <Other6Each>decimal</Other6Each>
          <Other6>decimal</Other6>
          <Other7Each>decimal</Other7Each>
          <Other7>decimal</Other7>
          <Other8Each>decimal</Other8Each>
          <Other8>decimal</Other8>
          <Other9Each>decimal</Other9Each>
          <Other9>decimal</Other9>
          <Other10Each>decimal</Other10Each>
          <Other10>decimal</Other10>
          <ParentItemCode>string</ParentItemCode>
          <Taxable>decimal</Taxable>
          <FedTax>decimal</FedTax>
          <StateTax>decimal</StateTax>
          <CityTax>decimal</CityTax>
          <CityLocalTax>decimal</CityLocalTax>
          <CountyTax>decimal</CountyTax>
          <CountyLocalTax>decimal</CountyLocalTax>
          <ManualTax>decimal</ManualTax>
          <IsStateTaxOverride>boolean</IsStateTaxOverride>
          <OrderLine>int</OrderLine>
          <Reference1>string</Reference1>
          <ShippingPriceEach>decimal</ShippingPriceEach>
          <HandlingFee>decimal</HandlingFee>
          <BusinessVolume>decimal</BusinessVolume>
        </OrderDetailResponse>
      </Details>
      <ShipMethods>
        <ShipMethodResponse>
          <ShipMethodID>int</ShipMethodID>
          <Description>string</Description>
          <ShippingAmount>decimal</ShippingAmount>
        </ShipMethodResponse>
      </ShipMethods>
      <Warnings>
        <string>string</string>
      </Warnings>
      <Trace>string</Trace>
      <HandlingFeeTotal>decimal</HandlingFeeTotal>
      <AutoOrderId>int</AutoOrderId>
      <ReplacementOrderId>int</ReplacementOrderId>
      <DeclineCount>int</DeclineCount>
      <IsRMA>boolean</IsRMA>
      <BackOrderFromId>int</BackOrderFromId>
      <IsCommissionable>boolean</IsCommissionable>
      <Flag1>boolean</Flag1>
      <Flag2>boolean</Flag2>
      <Flag3>boolean</Flag3>
      <ReturnCategoryId>int</ReturnCategoryId>
      <ReplacementCategoryId>int</ReplacementCategoryId>
    </PingResult>
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
    var req = new CalculateOrderRequest();

    req.CurrencyCode = "1";
    req.WarehouseID = 1;            //Unique location for orders
    req.ShipMethodID = 1;
    req.PriceType = 1;              //Controls which price band to use
    req.Address1 = "1";
    req.Address2 = "1";
    req.Address3 = "1";
    req.City = "1";
    req.State = "1";
    req.Zip = "1";
    req.Country = "1";
    req.County = "1";
    req.CustomerID = 1;             //Unique numeric identifier for a customer record.

    //Add Details
    var details = new List<OrderDetailRequest>();

    var detail1 = new OrderDetailRequest();
    detail1.ItemCode = "1";
    detail1.Quantity = 1;
    details.Add(detail1);

    var detail2 = new OrderDetailRequest();
    detail2.ItemCode = "2";
    detail2.Quantity = 2;
    details.Add(detail2);

    //Now attach the list to the request
    req.Details = details.ToArray();
    req.ReturnShipMethods = true;
    req.PartyID = 1;
    req.CustomerKey = "DDks8235txcid";//Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.OrderType = OrderType.Default;

    //Send Request to Server and Get Response
    var res = await api.PingAsync(req);

    //Now examine the results:
    Console.WriteLine("Total: {0}", res.Total);
    Console.WriteLine("SubTotal: {0}", res.SubTotal);
    Console.WriteLine("TaxTotal: {0}", res.TaxTotal);
    Console.WriteLine("ShippingTotal: {0}", res.ShippingTotal);
    Console.WriteLine("DiscountTotal: {0}", res.DiscountTotal);
    Console.WriteLine("DiscountPercent: {0}", res.DiscountPercent);
    Console.WriteLine("WeightTotal: {0}", res.WeightTotal);
    Console.WriteLine("BusinessVolumeTotal: {0}", res.BusinessVolumeTotal);
    Console.WriteLine("CommissionableVolumeTotal: {0}", res.CommissionableVolumeTotal);
    Console.WriteLine("Other11: {0}", res.Other11);
    Console.WriteLine("Other12: {0}", res.Other12);
    Console.WriteLine("Other13: {0}", res.Other13);
    Console.WriteLine("Other14: {0}", res.Other14);
    Console.WriteLine("Other15: {0}", res.Other15);
    Console.WriteLine("Other16: {0}", res.Other16);
    Console.WriteLine("Other17: {0}", res.Other17);
    Console.WriteLine("Other18: {0}", res.Other18);
    Console.WriteLine("Other19: {0}", res.Other19);
    Console.WriteLine("Other20: {0}", res.Other20);
    Console.WriteLine("ShippingTax: {0}", res.ShippingTax);
    Console.WriteLine("OrderTax: {0}", res.OrderTax);
    Console.WriteLine("FedTaxTotal: {0}", res.FedTaxTotal);
    Console.WriteLine("StateTaxTotal: {0}", res.StateTaxTotal);

    foreach (var orderDetail  in res.Details)
    {
        Console.WriteLine("OrderDetailID: {0}", orderDetail.OrderDetailID);
        Console.WriteLine("ParentOrderDetailID: {0}", orderDetail.ParentOrderDetailID);
        Console.WriteLine("ItemCode: {0}", orderDetail.ItemCode);
        Console.WriteLine("Description: {0}", orderDetail.Description);
        Console.WriteLine("Quantity: {0}", orderDetail.Quantity);
        Console.WriteLine("BusinesVolume: {0}", orderDetail.BusinesVolume);
        Console.WriteLine("OrderLine: {0}", orderDetail.OrderLine);
        Console.WriteLine("Reference1: {0}", orderDetail.Reference1);
        Console.WriteLine("ShippingPriceEach: {0}", orderDetail.ShippingPriceEach);
    }

    foreach (var shipMethod  in res.ShipMethods)
    {
        Console.WriteLine("ShipMethodID: {0}", shipMethod.ShipMethodID);
        Console.WriteLine("Description: {0}", shipMethod.Description);
        Console.WriteLine("ShippingAmount: {0}", shipMethod.ShippingAmount);
    }
    Console.WriteLine("Warnings: {0}", res.Warnings);
    Console.WriteLine("Trace: {0}", res.Trace);
    Console.WriteLine("HandlingFeeTotal: {0}", res.HandlingFeeTotal);
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
    CalculateOrderRequest req = new CalculateOrderRequest();

    req.CurrencyCode = "1";
    req.WarehouseID = 1;            //Unique location for orders
    req.ShipMethodID = 1;
    req.PriceType = 1;              //Controls which price band to use
    req.Address1 = "1";
    req.Address2 = "1";
    req.Address3 = "1";
    req.City = "1";
    req.State = "1";
    req.Zip = "1";
    req.Country = "1";
    req.County = "1";
    req.CustomerID = 1;             //Unique numeric identifier for a customer record.

    //Add Details
    List<OrderDetailRequest> details = new List<OrderDetailRequest>();

    OrderDetailRequest detail1 = new OrderDetailRequest();
    detail1.ItemCode = "1";
    detail1.Quantity = 1;
    details.Add(detail1);

    OrderDetailRequest detail2 = new OrderDetailRequest();
    detail2.ItemCode = "2";
    detail2.Quantity = 2;
    details.Add(detail2);

    //Now attach the list to the request
    req.Details = details.ToArray();
    req.ReturnShipMethods = true;
    req.PartyID = 1;
    req.CustomerKey = "DDks8235txcid";//Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.OrderType = OrderType.Default;

    //Send Request to Server and Get Response
    CalculateOrderResponse res = api.Ping(req);

    //Now examine the results:
    Console.WriteLine("Total: {0}", res.Total);
    Console.WriteLine("SubTotal: {0}", res.SubTotal);
    Console.WriteLine("TaxTotal: {0}", res.TaxTotal);
    Console.WriteLine("ShippingTotal: {0}", res.ShippingTotal);
    Console.WriteLine("DiscountTotal: {0}", res.DiscountTotal);
    Console.WriteLine("DiscountPercent: {0}", res.DiscountPercent);
    Console.WriteLine("WeightTotal: {0}", res.WeightTotal);
    Console.WriteLine("BusinessVolumeTotal: {0}", res.BusinessVolumeTotal);
    Console.WriteLine("CommissionableVolumeTotal: {0}", res.CommissionableVolumeTotal);
    Console.WriteLine("Other11: {0}", res.Other11);
    Console.WriteLine("Other12: {0}", res.Other12);
    Console.WriteLine("Other13: {0}", res.Other13);
    Console.WriteLine("Other14: {0}", res.Other14);
    Console.WriteLine("Other15: {0}", res.Other15);
    Console.WriteLine("Other16: {0}", res.Other16);
    Console.WriteLine("Other17: {0}", res.Other17);
    Console.WriteLine("Other18: {0}", res.Other18);
    Console.WriteLine("Other19: {0}", res.Other19);
    Console.WriteLine("Other20: {0}", res.Other20);
    Console.WriteLine("ShippingTax: {0}", res.ShippingTax);
    Console.WriteLine("OrderTax: {0}", res.OrderTax);
    Console.WriteLine("FedTaxTotal: {0}", res.FedTaxTotal);
    Console.WriteLine("StateTaxTotal: {0}", res.StateTaxTotal);

    foreach (OrderDetailResponse orderDetail  in res.Details)
    {
        Console.WriteLine("OrderDetailID: {0}", orderDetail.OrderDetailID);
        Console.WriteLine("ParentOrderDetailID: {0}", orderDetail.ParentOrderDetailID);
        Console.WriteLine("ItemCode: {0}", orderDetail.ItemCode);
        Console.WriteLine("Description: {0}", orderDetail.Description);
        Console.WriteLine("Quantity: {0}", orderDetail.Quantity);
        Console.WriteLine("BusinesVolume: {0}", orderDetail.BusinesVolume);
        Console.WriteLine("OrderLine: {0}", orderDetail.OrderLine);
        Console.WriteLine("Reference1: {0}", orderDetail.Reference1);
        Console.WriteLine("ShippingPriceEach: {0}", orderDetail.ShippingPriceEach);
    }

    foreach (ShipMethodResponse shipMethod  in res.ShipMethods)
    {
        Console.WriteLine("ShipMethodID: {0}", shipMethod.ShipMethodID);
        Console.WriteLine("Description: {0}", shipMethod.Description);
        Console.WriteLine("ShippingAmount: {0}", shipMethod.ShippingAmount);
    }
    Console.WriteLine("Warnings: {0}", res.Warnings);
    Console.WriteLine("Trace: {0}", res.Trace);
    Console.WriteLine("HandlingFeeTotal: {0}", res.HandlingFeeTotal);
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
    Dim req as new CalculateOrderRequest()

    req.CurrencyCode = "1"
    req.WarehouseID = 1
    req.ShipMethodID = 1
    req.PriceType = 1
    req.Address1 = "1"
    req.Address2 = "1"
    req.Address3 = "1"
    req.City = "1"
    req.State = "1"
    req.Zip = "1"
    req.Country = "1"
    req.County = "1"
    req.CustomerID = 1

    'Add Details
    Dim details As New List(Of OrderDetailRequest)()

    Dim detail1 as new OrderDetailRequest()
    detail1.ItemCode = "1"
    detail1.Quantity = 1
    details.Add(detail1)

    Dim detail2 as new OrderDetailRequest()
    detail2.ItemCode = "2"
    detail2.Quantity = 2
    details.Add(detail2)

    'Now attach the list to the request
    req.Details = details.ToArray()
    req.ReturnShipMethods = true
    req.PartyID = 1
    req.CustomerKey = "DDks8235txcid"
    req.OrderType = OrderType.Default

    'Send Request to Server and Get Response
    Dim res As CalculateOrderResponse = api.Ping(req)

    'Now examine the results:
    Console.WriteLine("Total: {0}", res.Total)
    Console.WriteLine("SubTotal: {0}", res.SubTotal)
    Console.WriteLine("TaxTotal: {0}", res.TaxTotal)
    Console.WriteLine("ShippingTotal: {0}", res.ShippingTotal)
    Console.WriteLine("DiscountTotal: {0}", res.DiscountTotal)
    Console.WriteLine("DiscountPercent: {0}", res.DiscountPercent)
    Console.WriteLine("WeightTotal: {0}", res.WeightTotal)
    Console.WriteLine("BusinessVolumeTotal: {0}", res.BusinessVolumeTotal)
    Console.WriteLine("CommissionableVolumeTotal: {0}", res.CommissionableVolumeTotal)
    Console.WriteLine("Other11: {0}", res.Other11)
    Console.WriteLine("Other12: {0}", res.Other12)
    Console.WriteLine("Other13: {0}", res.Other13)
    Console.WriteLine("Other14: {0}", res.Other14)
    Console.WriteLine("Other15: {0}", res.Other15)
    Console.WriteLine("Other16: {0}", res.Other16)
    Console.WriteLine("Other17: {0}", res.Other17)
    Console.WriteLine("Other18: {0}", res.Other18)
    Console.WriteLine("Other19: {0}", res.Other19)
    Console.WriteLine("Other20: {0}", res.Other20)
    Console.WriteLine("ShippingTax: {0}", res.ShippingTax)
    Console.WriteLine("OrderTax: {0}", res.OrderTax)
    Console.WriteLine("FedTaxTotal: {0}", res.FedTaxTotal)
    Console.WriteLine("StateTaxTotal: {0}", res.StateTaxTotal)

    For Each orderDetail As OrderDetailResponse In res.Details
        Console.WriteLine("OrderDetailID: {0}", orderDetail.OrderDetailID)
        Console.WriteLine("ParentOrderDetailID: {0}", orderDetail.ParentOrderDetailID)
        Console.WriteLine("ItemCode: {0}", orderDetail.ItemCode)
        Console.WriteLine("Description: {0}", orderDetail.Description)
        Console.WriteLine("Quantity: {0}", orderDetail.Quantity)
        Console.WriteLine("BusinesVolume: {0}", orderDetail.BusinesVolume)
        Console.WriteLine("OrderLine: {0}", orderDetail.OrderLine)
        Console.WriteLine("Reference1: {0}", orderDetail.Reference1)
        Console.WriteLine("ShippingPriceEach: {0}", orderDetail.ShippingPriceEach)
    Next

    For Each shipMethod As ShipMethodResponse In res.ShipMethods
        Console.WriteLine("ShipMethodID: {0}", shipMethod.ShipMethodID)
        Console.WriteLine("Description: {0}", shipMethod.Description)
        Console.WriteLine("ShippingAmount: {0}", shipMethod.ShippingAmount)
    Next
    Console.WriteLine("Warnings: {0}", res.Warnings)
    Console.WriteLine("Trace: {0}", res.Trace)
    Console.WriteLine("HandlingFeeTotal: {0}", res.HandlingFeeTotal)
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

    $req->CurrencyCode = "1";
    $req->WarehouseID = 1;
    $req->ShipMethodID = 1;
    $req->PriceType = 1;
    $req->Address1 = "1";
    $req->Address2 = "1";
    $req->Address3 = "1";
    $req->City = "1";
    $req->State = "1";
    $req->Zip = "1";
    $req->Country = "1";
    $req->County = "1";
    $req->CustomerID = 1;

    //Add Details

    $detail1->ItemCode = "1";
    $detail1->Quantity = 1;

    $detail2->ItemCode = "2";
    $detail2->Quantity = 2;

    //Now attach the list to the request
    req.Details = array(detail1,detail2);
    $req->ReturnShipMethods = 1;
    $req->PartyID = 1;
    $req->CustomerKey = "DDks8235txcid";
    $req->OrderType = 1;

    //Send Request to Server and Get Response
    $res = $api.Ping($req);

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
    CalculateOrderRequest req = new CalculateOrderRequest();

    req.setCurrencyCode("1");
    req.setWarehouseID(1);
    req.setShipMethodID(1);
    req.setPriceType(1);
    req.setAddress1("1");
    req.setAddress2("1");
    req.setAddress3("1");
    req.setCity("1");
    req.setState("1");
    req.setZip("1");
    req.setCountry("1");
    req.setCounty("1");
    req.setCustomerID(1);

    //Add Details
    ArrayOfOrderDetailRequest details = new ArrayOfOrderDetailRequest();

    OrderDetailRequest detail1 = new OrderDetailRequest();
    detail1.setItemCode("1");
    detail1.setQuantity(1);
    details.Add(detail1);

    OrderDetailRequest detail2 = new OrderDetailRequest();
    detail2.setItemCode("2");
    detail2.setQuantity(2);
    details.Add(detail2);

    //Now attach the list to the request
    req.setDetails(details);
    req.setReturnShipMethods(1);
    req.setPartyID(1);
    req.setCustomerKey("DDks8235txcid");
    req.setOrderType(1);

    //Send Request to Server and Get Response
    CalculateOrderResponse res = api.getExigoApiSoap().ping(req, auth);

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

### PlaceStackNode

> Inserts/Moves a customer within the Stack Tree.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/PlaceStackNode` |
| WSDL elements | `PlaceStackNodeRequest` → `PlaceStackNodeResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=PlaceStackNode |

#### Input

**`PlaceStackNodeRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |
| `ToParentID` | `Int32` | Unique numeric identifier for customer record. |
| `ToParentKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if ToParentID & ToParentKey are provided. |
| `Reason` | `String` | Optional. |

#### Output

**`PlaceStackNodeResponse`**

_No properties._

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/PlaceStackNode"

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
  <soap:Body />
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
  <soap:Body />
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
    var req = new PlaceStackNodeRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.ToParentID = 1;             //Unique numeric identifier for customer record.
    req.ToParentKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if ToParentID & ToParentKey are provided.
    req.Reason = "1";

    //Send Request to Server and Get Response
    var res = await api.PlaceStackNodeAsync(req);

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
    PlaceStackNodeRequest req = new PlaceStackNodeRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.ToParentID = 1;             //Unique numeric identifier for customer record.
    req.ToParentKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if ToParentID & ToParentKey are provided.
    req.Reason = "1";

    //Send Request to Server and Get Response
    PlaceStackNodeResponse res = api.PlaceStackNode(req);

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
    Dim req as new PlaceStackNodeRequest()

    req.CustomerID = 1
    req.CustomerKey = "1"
    req.ToParentID = 1
    req.ToParentKey = "1"
    req.Reason = "1"

    'Send Request to Server and Get Response
    Dim res As PlaceStackNodeResponse = api.PlaceStackNode(req)

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
    $req->CustomerKey = "1";
    $req->ToParentID = 1;
    $req->ToParentKey = "1";
    $req->Reason = "1";

    //Send Request to Server and Get Response
    $res = $api.PlaceStackNode($req);

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
    PlaceStackNodeRequest req = new PlaceStackNodeRequest();

    req.setCustomerID(1);
    req.setCustomerKey("1");
    req.setToParentID(1);
    req.setToParentKey("1");
    req.setReason("1");

    //Send Request to Server and Get Response
    PlaceStackNodeResponse res = api.getExigoApiSoap().placeStackNode(req, auth);

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

### RefreshSandbox

> Refresh a Sandbox

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/RefreshSandbox` |
| WSDL elements | `RefreshSandboxRequest` → `RefreshSandboxResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=RefreshSandbox |

#### Input

**`RefreshSandboxRequest`**

| Property | Type | Notes |
|---|---|---|
| `SandboxID` | `Int32` | Start sandbox instance specified. |

#### Output

**`RefreshSandboxResponse`**

| Property | Type | Notes |
|---|---|---|
| `Sandbox` | `Sandbox` |  |

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/RefreshSandbox"

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
    <RefreshSandboxRequest xmlns="http://api.exigo.com/">
      <SandboxID>int</SandboxID>
    </RefreshSandboxRequest>
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
    <RefreshSandboxResult xmlns="http://api.exigo.com/">
      <Sandbox>
        <CompanyID>int</CompanyID>
        <SandboxID>int</SandboxID>
        <Description>string</Description>
        <Type>Sandbox or Commission or Premium</Type>
        <Status>string</Status>
        <StartDate>dateTime</StartDate>
        <PercentComplete>decimal</PercentComplete>
        <Hours>decimal</Hours>
        <AllowVolumePush>boolean</AllowVolumePush>
        <AllowBiSync>boolean</AllowBiSync>
        <SyncFilterDays>int</SyncFilterDays>
        <UseRealTimeBackup>boolean</UseRealTimeBackup>
      </Sandbox>
    </RefreshSandboxResult>
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
    var req = new RefreshSandboxRequest();

    req.SandboxID = 1;              //Start sandbox instance specified

    //Send Request to Server and Get Response
    var res = await api.RefreshSandboxAsync(req);

    //Now examine the results:
    Console.WriteLine("Sandbox: {0}", res.Sandbox);
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
    RefreshSandboxRequest req = new RefreshSandboxRequest();

    req.SandboxID = 1;              //Start sandbox instance specified

    //Send Request to Server and Get Response
    RefreshSandboxResponse res = api.RefreshSandbox(req);

    //Now examine the results:
    Console.WriteLine("Sandbox: {0}", res.Sandbox);
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
    Dim req as new RefreshSandboxRequest()

    req.SandboxID = 1

    'Send Request to Server and Get Response
    Dim res As RefreshSandboxResponse = api.RefreshSandbox(req)

    'Now examine the results:
    Console.WriteLine("Sandbox: {0}", res.Sandbox)
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

    $req->SandboxID = 1;

    //Send Request to Server and Get Response
    $res = $api.RefreshSandbox($req);

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
    RefreshSandboxRequest req = new RefreshSandboxRequest();

    req.setSandboxID(1);

    //Send Request to Server and Get Response
    RefreshSandboxResponse res = api.getExigoApiSoap().refreshSandbox(req, auth);

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

### SetAccountCreditCard

> Setup primary or secondary credit card on file for an existing
>  customer, or new customer in a transaction.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/SetAccountCreditCard` |
| WSDL elements | `SetAccountCreditCardRequest` → `SetAccountCreditCardResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=SetAccountCreditCard |

#### Input

**`SetAccountCreditCardRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CreditCardAccountType` | `AccountCreditCardType` | **Values:** `Primary`, `Secondary` |
| `CreditCardNumber` | `String` | Optional. |
| `ExpirationMonth` | `Int32` |  |
| `ExpirationYear` | `Int32` |  |
| `CvcCode` | `String` | Optional. |
| `IssueCode` | `String` | Optional. |
| `CreditCardType` | `Int32` | Optional. Optionally pass in Visa, Master Card, etc.<br>**Lookup:** company-specific list (see company-lists.md) |
| `BillingName` | `String` | Optional. |
| `UseMainAddress` | `Boolean` |  |
| `BillingAddress` | `String` | Optional. |
| `BillingCity` | `String` | Optional. |
| `BillingState` | `String` | Optional. |
| `BillingZip` | `String` | Optional. |
| `BillingCountry` | `String` | Optional. |
| `HideFromWeb` | `Boolean` | Optional. Can be used for AutoOrder but will not show up in shopping cart. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`SetAccountResponse`**

_No properties._

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/SetAccountCreditCard"

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
    <SetAccountCreditCardRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CreditCardAccountType>Primary or Secondary</CreditCardAccountType>
      <CreditCardNumber>string</CreditCardNumber>
      <ExpirationMonth>int</ExpirationMonth>
      <ExpirationYear>int</ExpirationYear>
      <CvcCode>string</CvcCode>
      <IssueCode>string</IssueCode>
      <CreditCardType>int</CreditCardType>
      <BillingName>string</BillingName>
      <UseMainAddress>boolean</UseMainAddress>
      <BillingAddress>string</BillingAddress>
      <BillingCity>string</BillingCity>
      <BillingState>string</BillingState>
      <BillingZip>string</BillingZip>
      <BillingCountry>string</BillingCountry>
      <HideFromWeb>boolean</HideFromWeb>
      <CustomerKey>string</CustomerKey>
    </SetAccountCreditCardRequest>
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
    <SetAccountCreditCardResult xmlns="http://api.exigo.com/" />
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
    var req = new SetAccountCreditCardRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CreditCardAccountType = AccountCreditCardType.Primary;
    req.CreditCardNumber = "2432342342342323";
    req.ExpirationMonth = 1;
    req.ExpirationYear = 2013;
    req.CvcCode = "254";
    req.UseMainAddress = true;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.SetAccountCreditCardAsync(req);

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
    SetAccountCreditCardRequest req = new SetAccountCreditCardRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CreditCardAccountType = AccountCreditCardType.Primary;
    req.CreditCardNumber = "2432342342342323";
    req.ExpirationMonth = 1;
    req.ExpirationYear = 2013;
    req.CvcCode = "254";
    req.UseMainAddress = true;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    SetAccountResponse res = api.SetAccountCreditCard(req);

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
    Dim req as new SetAccountCreditCardRequest()

    req.CustomerID = 1
    req.CreditCardAccountType = AccountCreditCardType.Primary
    req.CreditCardNumber = "2432342342342323"
    req.ExpirationMonth = 1
    req.ExpirationYear = 2013
    req.CvcCode = "254"
    req.UseMainAddress = true
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As SetAccountResponse = api.SetAccountCreditCard(req)

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
    $req->CreditCardNumber = "2432342342342323";
    $req->ExpirationMonth = 1;
    $req->ExpirationYear = 2013;
    $req->CvcCode = "254";
    $req->UseMainAddress = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.SetAccountCreditCard($req);

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
    SetAccountCreditCardRequest req = new SetAccountCreditCardRequest();

    req.setCustomerID(1);
    req.setCreditCardAccountType(1);
    req.setCreditCardNumber("2432342342342323");
    req.setExpirationMonth(1);
    req.setExpirationYear(2013);
    req.setCvcCode("254");
    req.setUseMainAddress(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    SetAccountResponse res = api.getExigoApiSoap().setAccountCreditCard(req, auth);

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

### SetImageFile

> Set Images

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/SetImageFile` |
| WSDL elements | `SetImageFileRequest` → `SetImageFileResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=SetImageFile |

#### Input

**`SetImageFileRequest`**

| Property | Type | Notes |
|---|---|---|
| `Path` | `String` | Optional. |
| `Name` | `String` | Optional. |
| `ImageData` | `Byte[]` |  |

#### Output

**`SetImageFileResponse`**

_No properties._

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/SetImageFile"

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
  <soap:Body />
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
  <soap:Body />
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
    var req = new SetImageFileRequest();

    req.Path = "1";
    req.Name = "1";

    //Add ImageData
    var imagedata = new List<Byte>();
    imagedata.Add(1);
    imagedata.Add(2);

    //Now attach the list to the request
    req.ImageData = imagedata.ToArray();

    //Send Request to Server and Get Response
    var res = await api.SetImageFileAsync(req);

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
    SetImageFileRequest req = new SetImageFileRequest();

    req.Path = "1";
    req.Name = "1";

    //Add ImageData
    List<Byte> imagedata = new List<Byte>();
    imagedata.Add(1);
    imagedata.Add(2);

    //Now attach the list to the request
    req.ImageData = imagedata.ToArray();

    //Send Request to Server and Get Response
    SetImageFileResponse res = api.SetImageFile(req);

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
    Dim req as new SetImageFileRequest()

    req.Path = "1"
    req.Name = "1"

    'Add ImageData
    Dim imagedata As New List(Of Byte)()
    imagedata.Add(1)
    imagedata.Add(2)

    'Now attach the list to the request
    req.ImageData = imagedata.ToArray()

    'Send Request to Server and Get Response
    Dim res As SetImageFileResponse = api.SetImageFile(req)

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

    $req->Path = "1";
    $req->Name = "1";

    //Add ImageData

    //Now attach the list to the request
    req.ImageData = array(imageDat1,imageDat2);

    //Send Request to Server and Get Response
    $res = $api.SetImageFile($req);

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
    SetImageFileRequest req = new SetImageFileRequest();

    req.setPath("1");
    req.setName("1");

    //Add ImageData
    ArrayOfSystem.Byte imagedata = new ArrayOfSystem.Byte();

    Byte imageDat1 = new Byte();
    imagedata.Add(imageDat1);

    Byte imageDat2 = new Byte();
    imagedata.Add(imageDat2);

    //Now attach the list to the request
    req.setImageData(imagedata);

    //Send Request to Server and Get Response
    SetImageFileResponse res = api.getExigoApiSoap().setImageFile(req, auth);

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

### StartSandbox

> Start a Sandbox

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/StartSandbox` |
| WSDL elements | `StartSandboxRequest` → `StartSandboxResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=StartSandbox |

#### Input

**`StartSandboxRequest`**

| Property | Type | Notes |
|---|---|---|
| `SandboxID` | `Int32` | Start sandbox instance specified. |
| `EnableRevolvingCommissionRun` | `Boolean` | Optional. Enable revolving commission run. Defaults to False. |
| `EnableBiSync` | `Boolean` | Optional. Enable Exigo BI Sync Server. Defaults to False. |
| `UseRealTimeBackup` | `Boolean` | Optional. Type of sandbox to start. Defaults to False. |
| `SyncFilterDays` | `Int32` | Optional. Type of sandbox to start. Defaults to 0. |
| `SyncSettingsEnable` | `String` | Optional. Comma delmited list of sync setting names to enable on sandbox start. |

#### Output

**`StartSandboxResponse`**

| Property | Type | Notes |
|---|---|---|
| `Sandbox` | `Sandbox` |  |

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/StartSandbox"

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
    <StartSandboxRequest xmlns="http://api.exigo.com/">
      <SandboxID>int</SandboxID>
      <EnableRevolvingCommissionRun>boolean</EnableRevolvingCommissionRun>
      <EnableBiSync>boolean</EnableBiSync>
      <UseRealTimeBackup>boolean</UseRealTimeBackup>
      <SyncFilterDays>int</SyncFilterDays>
      <SyncSettingsEnable>string</SyncSettingsEnable>
    </StartSandboxRequest>
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
    <StartSandboxResult xmlns="http://api.exigo.com/">
      <Sandbox>
        <CompanyID>int</CompanyID>
        <SandboxID>int</SandboxID>
        <Description>string</Description>
        <Type>Sandbox or Commission or Premium</Type>
        <Status>string</Status>
        <StartDate>dateTime</StartDate>
        <PercentComplete>decimal</PercentComplete>
        <Hours>decimal</Hours>
        <AllowVolumePush>boolean</AllowVolumePush>
        <AllowBiSync>boolean</AllowBiSync>
        <SyncFilterDays>int</SyncFilterDays>
        <UseRealTimeBackup>boolean</UseRealTimeBackup>
      </Sandbox>
    </StartSandboxResult>
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
    var req = new StartSandboxRequest();

    req.SandboxID = 1;              //Start sandbox instance specified
    req.EnableRevolvingCommissionRun = true;//Enable revolving commission run
    req.EnableBiSync = true;           //Enable Exigo BI Sync Server
    req.UseRealTimeBackup = true;      //Type of sandbox to start
    req.SyncFilterDays = 1;         //Type of sandbox to start
    req.SyncSettingsEnable = "1";   //Comma delmited list of sync setting names to enable on sandbox start

    //Send Request to Server and Get Response
    var res = await api.StartSandboxAsync(req);

    //Now examine the results:
    Console.WriteLine("Sandbox: {0}", res.Sandbox);
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
    StartSandboxRequest req = new StartSandboxRequest();

    req.SandboxID = 1;              //Start sandbox instance specified
    req.EnableRevolvingCommissionRun = true;//Enable revolving commission run
    req.EnableBiSync = true;           //Enable Exigo BI Sync Server
    req.UseRealTimeBackup = true;      //Type of sandbox to start
    req.SyncFilterDays = 1;         //Type of sandbox to start
    req.SyncSettingsEnable = "1";   //Comma delmited list of sync setting names to enable on sandbox start

    //Send Request to Server and Get Response
    StartSandboxResponse res = api.StartSandbox(req);

    //Now examine the results:
    Console.WriteLine("Sandbox: {0}", res.Sandbox);
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
    Dim req as new StartSandboxRequest()

    req.SandboxID = 1
    req.EnableRevolvingCommissionRun = true
    req.EnableBiSync = true
    req.UseRealTimeBackup = true
    req.SyncFilterDays = 1
    req.SyncSettingsEnable = "1"

    'Send Request to Server and Get Response
    Dim res As StartSandboxResponse = api.StartSandbox(req)

    'Now examine the results:
    Console.WriteLine("Sandbox: {0}", res.Sandbox)
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

    $req->SandboxID = 1;
    $req->EnableRevolvingCommissionRun = 1;
    $req->EnableBiSync = 1;
    $req->UseRealTimeBackup = 1;
    $req->SyncFilterDays = 1;
    $req->SyncSettingsEnable = "1";

    //Send Request to Server and Get Response
    $res = $api.StartSandbox($req);

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
    StartSandboxRequest req = new StartSandboxRequest();

    req.setSandboxID(1);
    req.setEnableRevolvingCommissionRun(1);
    req.setEnableBiSync(1);
    req.setUseRealTimeBackup(1);
    req.setSyncFilterDays(1);
    req.setSyncSettingsEnable("1");

    //Send Request to Server and Get Response
    StartSandboxResponse res = api.getExigoApiSoap().startSandbox(req, auth);

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

### StopSandbox

> Stop a Sandbox

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/StopSandbox` |
| WSDL elements | `StopSandboxRequest` → `StopSandboxResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=StopSandbox |

#### Input

**`StopSandboxRequest`**

| Property | Type | Notes |
|---|---|---|
| `SandboxID` | `Int32` | Stop sandbox instance specified. |

#### Output

**`StopSandboxResponse`**

| Property | Type | Notes |
|---|---|---|
| `SandboxID` | `Int32` |  |

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/StopSandbox"

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
    <StopSandboxRequest xmlns="http://api.exigo.com/">
      <SandboxID>int</SandboxID>
    </StopSandboxRequest>
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
    <StopSandboxResult xmlns="http://api.exigo.com/">
      <SandboxID>int</SandboxID>
    </StopSandboxResult>
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
    var req = new StopSandboxRequest();

    req.SandboxID = 1;              //Stop sandbox instance specified

    //Send Request to Server and Get Response
    var res = await api.StopSandboxAsync(req);

    //Now examine the results:
    Console.WriteLine("SandboxID: {0}", res.SandboxID);
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
    StopSandboxRequest req = new StopSandboxRequest();

    req.SandboxID = 1;              //Stop sandbox instance specified

    //Send Request to Server and Get Response
    StopSandboxResponse res = api.StopSandbox(req);

    //Now examine the results:
    Console.WriteLine("SandboxID: {0}", res.SandboxID);
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
    Dim req as new StopSandboxRequest()

    req.SandboxID = 1

    'Send Request to Server and Get Response
    Dim res As StopSandboxResponse = api.StopSandbox(req)

    'Now examine the results:
    Console.WriteLine("SandboxID: {0}", res.SandboxID)
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

    $req->SandboxID = 1;

    //Send Request to Server and Get Response
    $res = $api.StopSandbox($req);

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
    StopSandboxRequest req = new StopSandboxRequest();

    req.setSandboxID(1);

    //Send Request to Server and Get Response
    StopSandboxResponse res = api.getExigoApiSoap().stopSandbox(req, auth);

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

### UpdateCustomerContact

> Updates customer contact information.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/UpdateCustomerContact` |
| WSDL elements | `UpdateCustomerContactRequest` → `UpdateCustomerContactResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateCustomerContact |

#### Input

**`UpdateCustomerContactRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerContactID` | `Int32` |  |
| `FirstName` | `String` | Optional. |
| `LastName` | `String` | Optional. |
| `MiddleName` | `String` | Optional. |
| `Company` | `String` | Optional. |
| `BusinessPhone` | `String` | Optional. |
| `HomePhone` | `String` | Optional. |
| `Mobile` | `String` | Optional. |
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
| `LinkedIn` | `String` | Optional. |
| `Facebook` | `String` | Optional. |
| `Blog` | `String` | Optional. |
| `MySpace` | `String` | Optional. |
| `GooglePlus` | `String` | Optional. |
| `Twitter` | `String` | Optional. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`UpdateCustomerContactResponse`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerContactID` | `Int32` |  |
| `CustomerKey` | `String` | Unique alpha numeric identifier for customer record . |

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/UpdateCustomerContact"

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
    <UpdateCustomerContactRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerContactID>int</CustomerContactID>
      <FirstName>string</FirstName>
      <LastName>string</LastName>
      <MiddleName>string</MiddleName>
      <Company>string</Company>
      <BusinessPhone>string</BusinessPhone>
      <HomePhone>string</HomePhone>
      <Mobile>string</Mobile>
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
      <LinkedIn>string</LinkedIn>
      <Facebook>string</Facebook>
      <Blog>string</Blog>
      <MySpace>string</MySpace>
      <GooglePlus>string</GooglePlus>
      <Twitter>string</Twitter>
      <CustomerKey>string</CustomerKey>
    </UpdateCustomerContactRequest>
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
    <UpdateCustomerContactResult xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerContactID>int</CustomerContactID>
      <CustomerKey>string</CustomerKey>
    </UpdateCustomerContactResult>
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
    var req = new UpdateCustomerContactRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerContactID = 1;
    req.FirstName = "1";
    req.LastName = "1";
    req.MiddleName = "1";
    req.Company = "1";
    req.BusinessPhone = "1";
    req.HomePhone = "1";
    req.Mobile = "1";
    req.Fax = "1";
    req.Email = "1";
    req.Address1 = "1";
    req.Address2 = "1";
    req.City = "1";
    req.Zip = "1";
    req.BirthDate = DateTime.Today;
    req.Notes = "1";
    req.LinkedIn = "1";
    req.Facebook = "1";
    req.Blog = "1";
    req.MySpace = "1";
    req.GooglePlus = "1";
    req.Twitter = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.UpdateCustomerContactAsync(req);

    //Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID);
    Console.WriteLine("CustomerContactID: {0}", res.CustomerContactID);
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
    UpdateCustomerContactRequest req = new UpdateCustomerContactRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerContactID = 1;
    req.FirstName = "1";
    req.LastName = "1";
    req.MiddleName = "1";
    req.Company = "1";
    req.BusinessPhone = "1";
    req.HomePhone = "1";
    req.Mobile = "1";
    req.Fax = "1";
    req.Email = "1";
    req.Address1 = "1";
    req.Address2 = "1";
    req.City = "1";
    req.Zip = "1";
    req.BirthDate = DateTime.Today;
    req.Notes = "1";
    req.LinkedIn = "1";
    req.Facebook = "1";
    req.Blog = "1";
    req.MySpace = "1";
    req.GooglePlus = "1";
    req.Twitter = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    UpdateCustomerContactResponse res = api.UpdateCustomerContact(req);

    //Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID);
    Console.WriteLine("CustomerContactID: {0}", res.CustomerContactID);
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
    Dim req as new UpdateCustomerContactRequest()

    req.CustomerID = 1
    req.CustomerContactID = 1
    req.FirstName = "1"
    req.LastName = "1"
    req.MiddleName = "1"
    req.Company = "1"
    req.BusinessPhone = "1"
    req.HomePhone = "1"
    req.Mobile = "1"
    req.Fax = "1"
    req.Email = "1"
    req.Address1 = "1"
    req.Address2 = "1"
    req.City = "1"
    req.Zip = "1"
    req.BirthDate = DateTime.Today
    req.Notes = "1"
    req.LinkedIn = "1"
    req.Facebook = "1"
    req.Blog = "1"
    req.MySpace = "1"
    req.GooglePlus = "1"
    req.Twitter = "1"
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As UpdateCustomerContactResponse = api.UpdateCustomerContact(req)

    'Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID)
    Console.WriteLine("CustomerContactID: {0}", res.CustomerContactID)
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
    $req->CustomerContactID = 1;
    $req->FirstName = "1";
    $req->LastName = "1";
    $req->MiddleName = "1";
    $req->Company = "1";
    $req->BusinessPhone = "1";
    $req->HomePhone = "1";
    $req->Mobile = "1";
    $req->Fax = "1";
    $req->Email = "1";
    $req->Address1 = "1";
    $req->Address2 = "1";
    $req->City = "1";
    $req->Zip = "1";
    $req->BirthDate = 1;
    $req->Notes = "1";
    $req->LinkedIn = "1";
    $req->Facebook = "1";
    $req->Blog = "1";
    $req->MySpace = "1";
    $req->GooglePlus = "1";
    $req->Twitter = "1";
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.UpdateCustomerContact($req);

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
    UpdateCustomerContactRequest req = new UpdateCustomerContactRequest();

    req.setCustomerID(1);
    req.setCustomerContactID(1);
    req.setFirstName("1");
    req.setLastName("1");
    req.setMiddleName("1");
    req.setCompany("1");
    req.setBusinessPhone("1");
    req.setHomePhone("1");
    req.setMobile("1");
    req.setFax("1");
    req.setEmail("1");
    req.setAddress1("1");
    req.setAddress2("1");
    req.setCity("1");
    req.setZip("1");
    req.setBirthDate(1);
    req.setNotes("1");
    req.setLinkedIn("1");
    req.setFacebook("1");
    req.setBlog("1");
    req.setMySpace("1");
    req.setGooglePlus("1");
    req.setTwitter("1");
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    UpdateCustomerContactResponse res = api.getExigoApiSoap().updateCustomerContact(req, auth);

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

### UpdateEmailStatus

> Updates email's status.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/UpdateEmailStatus` |
| WSDL elements | `UpdateEmailStatusRequest` → `UpdateEmailStatusResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateEmailStatus |

#### Input

**`UpdateEmailStatusRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `MailID` | `Int32` |  |
| `MailStatusType` | `MailStatusType` | **Values:** `New`, `Read`, `Forwarded`, `Replied` |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`UpdateEmailStatusResponse`**

_No properties._

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/UpdateEmailStatus"

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
    <UpdateEmailStatusRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <MailID>int</MailID>
      <MailStatusType>New or Read or Forwarded or Replied</MailStatusType>
      <CustomerKey>string</CustomerKey>
    </UpdateEmailStatusRequest>
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
    <UpdateEmailStatusResult xmlns="http://api.exigo.com/" />
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
    var req = new UpdateEmailStatusRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.MailID = 1;
    req.MailStatusType = MailStatusType.New;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.UpdateEmailStatusAsync(req);

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
    UpdateEmailStatusRequest req = new UpdateEmailStatusRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.MailID = 1;
    req.MailStatusType = MailStatusType.New;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    UpdateEmailStatusResponse res = api.UpdateEmailStatus(req);

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
    Dim req as new UpdateEmailStatusRequest()

    req.CustomerID = 1
    req.MailID = 1
    req.MailStatusType = MailStatusType.New
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As UpdateEmailStatusResponse = api.UpdateEmailStatus(req)

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
    $req->MailID = 1;
    $req->MailStatusType = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.UpdateEmailStatus($req);

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
    UpdateEmailStatusRequest req = new UpdateEmailStatusRequest();

    req.setCustomerID(1);
    req.setMailID(1);
    req.setMailStatusType(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    UpdateEmailStatusResponse res = api.getExigoApiSoap().updateEmailStatus(req, auth);

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

### UpdateEmailTemplate

> Updates an email template.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/UpdateEmailTemplate` |
| WSDL elements | `UpdateEmailTemplateRequest` → `UpdateEmailTemplateResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateEmailTemplate |

#### Input

**`UpdateEmailTemplateRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `TemplateID` | `Int32` |  |
| `Description` | `String` | Optional. |
| `Content` | `String` | Optional. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`UpdateEmailTemplateResponse`**

_No properties._

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/UpdateEmailTemplate"

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
    <UpdateEmailTemplateRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <TemplateID>int</TemplateID>
      <Description>string</Description>
      <Content>string</Content>
      <CustomerKey>string</CustomerKey>
    </UpdateEmailTemplateRequest>
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
    <UpdateEmailTemplateResult xmlns="http://api.exigo.com/" />
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
    var req = new UpdateEmailTemplateRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.TemplateID = 1;
    req.Description = "1";
    req.Content = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.UpdateEmailTemplateAsync(req);

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
    UpdateEmailTemplateRequest req = new UpdateEmailTemplateRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.TemplateID = 1;
    req.Description = "1";
    req.Content = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    UpdateEmailTemplateResponse res = api.UpdateEmailTemplate(req);

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
    Dim req as new UpdateEmailTemplateRequest()

    req.CustomerID = 1
    req.TemplateID = 1
    req.Description = "1"
    req.Content = "1"
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As UpdateEmailTemplateResponse = api.UpdateEmailTemplate(req)

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
    $req->TemplateID = 1;
    $req->Description = "1";
    $req->Content = "1";
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.UpdateEmailTemplate($req);

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
    UpdateEmailTemplateRequest req = new UpdateEmailTemplateRequest();

    req.setCustomerID(1);
    req.setTemplateID(1);
    req.setDescription("1");
    req.setContent("1");
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    UpdateEmailTemplateResponse res = api.getExigoApiSoap().updateEmailTemplate(req, auth);

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

### UpdateMailFolder

> Updates a mail folder.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Unlisted (WSDL only) (not listed in the docs menu, documented in WSDL + method page) |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/UpdateMailFolder` |
| WSDL elements | `UpdateMailFolderRequest` → `UpdateMailFolderResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateMailFolder |

#### Input

**`UpdateMailFolderRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `MailFolderID` | `Int32` |  |
| `MailFolderName` | `String` | Optional. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`UpdateMailFolderResponse`**

_No properties._

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/UpdateMailFolder"

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
    <UpdateMailFolderRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <MailFolderID>int</MailFolderID>
      <MailFolderName>string</MailFolderName>
      <CustomerKey>string</CustomerKey>
    </UpdateMailFolderRequest>
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
    <UpdateMailFolderResult xmlns="http://api.exigo.com/" />
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
    var req = new UpdateMailFolderRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.MailFolderID = 1;
    req.MailFolderName = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.UpdateMailFolderAsync(req);

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
    UpdateMailFolderRequest req = new UpdateMailFolderRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.MailFolderID = 1;
    req.MailFolderName = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    UpdateMailFolderResponse res = api.UpdateMailFolder(req);

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
    Dim req as new UpdateMailFolderRequest()

    req.CustomerID = 1
    req.MailFolderID = 1
    req.MailFolderName = "1"
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As UpdateMailFolderResponse = api.UpdateMailFolder(req)

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
    $req->MailFolderID = 1;
    $req->MailFolderName = "1";
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.UpdateMailFolder($req);

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
    UpdateMailFolderRequest req = new UpdateMailFolderRequest();

    req.setCustomerID(1);
    req.setMailFolderID(1);
    req.setMailFolderName("1");
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    UpdateMailFolderResponse res = api.getExigoApiSoap().updateMailFolder(req, auth);

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
