# Exigo API — Points/Subscriptions

API version v2025.11.7.6. Crawled 2026-11-11 from https://api.exigo.com/3.0/. Back to [index](../README.md).

| Operation | REST | Summary |
|---|---|---|
| [CreatePointTransaction](#createpointtransaction) | `POST /3.0/point` | Create a transaction that adjusts or redeems points from a customer's point account. |
| [GetPointAccount](#getpointaccount) | `GET /3.0/point/account?pointAccountID=1` | Get the balance of a point account for a customer. |
| [GetSubscription](#getsubscription) | `GET /3.0/subscription?subscriptionID=1` | Get the subscription account for a customer. |
| [GetSubscriptions](#getsubscriptions) | `GET /3.0/subscriptions?customerID=1` | Get all subscriptions for a customer. |

---
### CreatePointTransaction

> Create a transaction that adjusts or redeems points from a customer's point account.

| | |
|---|---|
| Category | Points/Subscriptions |
| REST | `POST /3.0/point` |
| SOAP action | `https://api.exigo.com/CreatePointTransaction` |
| WSDL elements | `CreatePointTransactionRequest` → `CreatePointTransactionResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreatePointTransaction |

#### Input

**`CreatePointTransactionRequest`**

| Property | Type | Notes |
|---|---|---|
| `PointAccountID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `Amount` | `Decimal` | The amount to apply to the point account. A positive amount will add points while a negative amount will subtract points from the account. |
| `Reference` | `String` | Optional. |
| `TransactionType` | `PointTransactionType` | Obsolete field. Please consider upgrading to PointTransactionTy.<br>**Values:** `Redemption`, `Adjustment` |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |
| `PointTransactionTy` | `String` | Optional. The type of point transaction. This property is for logging purposes only and has no bearing on how the points are applied to the point account.<br>**Lookup:** company-specific list (see company-lists.md) |

#### Output

**`CreatePointTransactionResponse`**

| Property | Type | Notes |
|---|---|---|
| `TransactionID` | `Int32` | Newly created unique identifier for a point transaction record. |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/point HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "pointAccountID": 1,
  "customerID": 1,
  "amount": null,
  "reference": "",
  "customerKey": "1",
  "pointTransactionTy": "PointRedemptionPayment"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "transactionID": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreatePointTransaction"

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
    <CreatePointTransactionRequest xmlns="http://api.exigo.com/">
      <PointAccountID>int</PointAccountID>
      <CustomerID>int</CustomerID>
      <Amount>decimal</Amount>
      <Reference>string</Reference>
      <TransactionType>Redemption or Adjustment</TransactionType>
      <CustomerKey>string</CustomerKey>
      <PointTransactionTy>string</PointTransactionTy>
    </CreatePointTransactionRequest>
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
    <CreatePointTransactionResult xmlns="http://api.exigo.com/">
      <TransactionID>int</TransactionID>
    </CreatePointTransactionResult>
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
    var req = new CreatePointTransactionRequest();

    req.PointAccountID = 1;
    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.Amount = 1;                 //The amount to apply to the point account. A positive amount will add points while a negative amount will subtract points from the account.
    req.Reference = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.PointTransactionTy = "PointRedemptionPayment";//The type of point transaction. This property is for logging purposes only and has no bearing on how the points are applied to the point account.

    //Send Request to Server and Get Response
    var res = await api.CreatePointTransactionAsync(req);

    //Now examine the results:
    Console.WriteLine("TransactionID: {0}", res.TransactionID);
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
    CreatePointTransactionRequest req = new CreatePointTransactionRequest();

    req.PointAccountID = 1;
    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.Amount = 1;                 //The amount to apply to the point account. A positive amount will add points while a negative amount will subtract points from the account.
    req.Reference = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.PointTransactionTy = "PointRedemptionPayment";//The type of point transaction. This property is for logging purposes only and has no bearing on how the points are applied to the point account.

    //Send Request to Server and Get Response
    CreatePointTransactionResponse res = api.CreatePointTransaction(req);

    //Now examine the results:
    Console.WriteLine("TransactionID: {0}", res.TransactionID);
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
    Dim req as new CreatePointTransactionRequest()

    req.PointAccountID = 1
    req.CustomerID = 1
    req.Amount = 1
    req.Reference = "1"
    req.CustomerKey = "1"
    req.PointTransactionTy = "PointRedemptionPayment"

    'Send Request to Server and Get Response
    Dim res As CreatePointTransactionResponse = api.CreatePointTransaction(req)

    'Now examine the results:
    Console.WriteLine("TransactionID: {0}", res.TransactionID)
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

    $req->PointAccountID = 1;
    $req->CustomerID = 1;
    $req->Amount = 1;
    $req->Reference = "1";
    $req->CustomerKey = "1";
    $req->PointTransactionTy = "PointRedemptionPayment";

    //Send Request to Server and Get Response
    $res = $api.CreatePointTransaction($req);

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
    CreatePointTransactionRequest req = new CreatePointTransactionRequest();

    req.setPointAccountID(1);
    req.setCustomerID(1);
    req.setAmount(1);
    req.setReference("1");
    req.setCustomerKey("1");
    req.setPointTransactionTy("PointRedemptionPayment");

    //Send Request to Server and Get Response
    CreatePointTransactionResponse res = api.getExigoApiSoap().createPointTransaction(req, auth);

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

### GetPointAccount

> Get the balance of a point account for a customer.

| | |
|---|---|
| Category | Points/Subscriptions |
| REST | `GET /3.0/point/account?pointAccountID=1` |
| SOAP action | `https://api.exigo.com/GetPointAccount` |
| WSDL elements | `GetPointAccountRequest` → `GetPointAccountResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetPointAccount |

#### Input

**`GetPointAccountRequest`**

| Property | Type | Notes |
|---|---|---|
| `PointAccountID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`GetPointAccountResponse`**

| Property | Type | Notes |
|---|---|---|
| `Balance` | `Decimal` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/point/account?pointAccountID=1
  &customerID=1
  &customerKey=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "balance": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetPointAccount"

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
    <GetPointAccountRequest xmlns="http://api.exigo.com/">
      <PointAccountID>int</PointAccountID>
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
    </GetPointAccountRequest>
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
    <GetPointAccountResult xmlns="http://api.exigo.com/">
      <Balance>decimal</Balance>
    </GetPointAccountResult>
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
    var req = new GetPointAccountRequest();

    req.PointAccountID = 1;
    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.GetPointAccountAsync(req);

    //Now examine the results:
    Console.WriteLine("Balance: {0}", res.Balance);
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
    GetPointAccountRequest req = new GetPointAccountRequest();

    req.PointAccountID = 1;
    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    GetPointAccountResponse res = api.GetPointAccount(req);

    //Now examine the results:
    Console.WriteLine("Balance: {0}", res.Balance);
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
    Dim req as new GetPointAccountRequest()

    req.PointAccountID = 1
    req.CustomerID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As GetPointAccountResponse = api.GetPointAccount(req)

    'Now examine the results:
    Console.WriteLine("Balance: {0}", res.Balance)
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

    $req->PointAccountID = 1;
    $req->CustomerID = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.GetPointAccount($req);

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
    GetPointAccountRequest req = new GetPointAccountRequest();

    req.setPointAccountID(1);
    req.setCustomerID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    GetPointAccountResponse res = api.getExigoApiSoap().getPointAccount(req, auth);

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

### GetSubscription

> Get the subscription account for a customer.

| | |
|---|---|
| Category | Points/Subscriptions |
| REST | `GET /3.0/subscription?subscriptionID=1` |
| SOAP action | `https://api.exigo.com/GetSubscription` |
| WSDL elements | `GetSubscriptionRequest` → `GetSubscriptionResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetSubscription |

#### Input

**`GetSubscriptionRequest`**

| Property | Type | Notes |
|---|---|---|
| `SubscriptionID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`GetSubscriptionResponse`**

| Property | Type | Notes |
|---|---|---|
| `Status` | `SubscriptionStatus` | **Values:** `NotFound`, `Active`, `Expired`, `Cancelled` |
| `StartDate` | `DateTime` |  |
| `ExpireDate` | `DateTime` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/subscription?subscriptionID=1
  &customerID=1
  &customerKey=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "status": null,
  "startDate": "2026-11-10T00:00:00-06:00",
  "expireDate": "2026-11-10T00:00:00-06:00",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetSubscription"

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
    <GetSubscriptionRequest xmlns="http://api.exigo.com/">
      <SubscriptionID>int</SubscriptionID>
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
    </GetSubscriptionRequest>
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
    <GetSubscriptionResult xmlns="http://api.exigo.com/">
      <Status>NotFound or Active or Expired or Cancelled</Status>
      <StartDate>dateTime</StartDate>
      <ExpireDate>dateTime</ExpireDate>
    </GetSubscriptionResult>
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
    var req = new GetSubscriptionRequest();

    req.SubscriptionID = 1;
    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.GetSubscriptionAsync(req);

    //Now examine the results:
    Console.WriteLine("Status: {0}", res.Status);
    Console.WriteLine("StartDate: {0}", res.StartDate);
    Console.WriteLine("ExpireDate: {0}", res.ExpireDate);
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
    GetSubscriptionRequest req = new GetSubscriptionRequest();

    req.SubscriptionID = 1;
    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    GetSubscriptionResponse res = api.GetSubscription(req);

    //Now examine the results:
    Console.WriteLine("Status: {0}", res.Status);
    Console.WriteLine("StartDate: {0}", res.StartDate);
    Console.WriteLine("ExpireDate: {0}", res.ExpireDate);
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
    Dim req as new GetSubscriptionRequest()

    req.SubscriptionID = 1
    req.CustomerID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As GetSubscriptionResponse = api.GetSubscription(req)

    'Now examine the results:
    Console.WriteLine("Status: {0}", res.Status)
    Console.WriteLine("StartDate: {0}", res.StartDate)
    Console.WriteLine("ExpireDate: {0}", res.ExpireDate)
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

    $req->SubscriptionID = 1;
    $req->CustomerID = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.GetSubscription($req);

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
    GetSubscriptionRequest req = new GetSubscriptionRequest();

    req.setSubscriptionID(1);
    req.setCustomerID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    GetSubscriptionResponse res = api.getExigoApiSoap().getSubscription(req, auth);

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

### GetSubscriptions

> Get all subscriptions for a customer.

| | |
|---|---|
| Category | Points/Subscriptions |
| REST | `GET /3.0/subscriptions?customerID=1` |
| SOAP action | `https://api.exigo.com/GetSubscriptions` |
| WSDL elements | `GetSubscriptionsRequest` → `GetSubscriptionsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetSubscriptions |

#### Input

**`GetSubscriptionsRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |
| `IncludeInactive` | `Boolean` | Optional. Determines whether canceled subscriptions are fetched. Defaults to False. |

#### Output

**`GetSubscriptionsResponse`**

| Property | Type | Notes |
|---|---|---|
| `Subscriptions` | `SubscriptionResponse[]` |  |

**`SubscriptionResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `SubscriptionID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Status` | `SubscriptionStatus` | **Values:** `NotFound`, `Active`, `Expired`, `Cancelled` |
| &nbsp;&nbsp;↳ `StartDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `ExpireDate` | `DateTime` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/subscriptions?customerID=1
  &customerKey=1
  &includeInactive=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "subscriptions": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetSubscriptions"

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
    <GetSubscriptionsRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
      <IncludeInactive>boolean</IncludeInactive>
    </GetSubscriptionsRequest>
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
    <GetSubscriptionsResult xmlns="http://api.exigo.com/">
      <Subscriptions>
        <SubscriptionResponse>
          <SubscriptionID>int</SubscriptionID>
          <Status>NotFound or Active or Expired or Cancelled</Status>
          <StartDate>dateTime</StartDate>
          <ExpireDate>dateTime</ExpireDate>
        </SubscriptionResponse>
      </Subscriptions>
    </GetSubscriptionsResult>
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
    var req = new GetSubscriptionsRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.IncludeInactive = true;        //Determines whether canceled subscriptions are fetched.

    //Send Request to Server and Get Response
    var res = await api.GetSubscriptionsAsync(req);

    //Now examine the results:

    foreach (var subscription  in res.Subscriptions)
    {
        Console.WriteLine("SubscriptionID: {0}", subscription.SubscriptionID);
        Console.WriteLine("Status: {0}", subscription.Status);
        Console.WriteLine("StartDate: {0}", subscription.StartDate);
        Console.WriteLine("ExpireDate: {0}", subscription.ExpireDate);
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
    GetSubscriptionsRequest req = new GetSubscriptionsRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.IncludeInactive = true;        //Determines whether canceled subscriptions are fetched.

    //Send Request to Server and Get Response
    GetSubscriptionsResponse res = api.GetSubscriptions(req);

    //Now examine the results:

    foreach (SubscriptionResponse subscription  in res.Subscriptions)
    {
        Console.WriteLine("SubscriptionID: {0}", subscription.SubscriptionID);
        Console.WriteLine("Status: {0}", subscription.Status);
        Console.WriteLine("StartDate: {0}", subscription.StartDate);
        Console.WriteLine("ExpireDate: {0}", subscription.ExpireDate);
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
    Dim req as new GetSubscriptionsRequest()

    req.CustomerID = 1
    req.CustomerKey = "1"
    req.IncludeInactive = true

    'Send Request to Server and Get Response
    Dim res As GetSubscriptionsResponse = api.GetSubscriptions(req)

    'Now examine the results:

    For Each subscription As SubscriptionResponse In res.Subscriptions
        Console.WriteLine("SubscriptionID: {0}", subscription.SubscriptionID)
        Console.WriteLine("Status: {0}", subscription.Status)
        Console.WriteLine("StartDate: {0}", subscription.StartDate)
        Console.WriteLine("ExpireDate: {0}", subscription.ExpireDate)
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
    $req->IncludeInactive = 1;

    //Send Request to Server and Get Response
    $res = $api.GetSubscriptions($req);

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
    GetSubscriptionsRequest req = new GetSubscriptionsRequest();

    req.setCustomerID(1);
    req.setCustomerKey("1");
    req.setIncludeInactive(1);

    //Send Request to Server and Get Response
    GetSubscriptionsResponse res = api.getExigoApiSoap().getSubscriptions(req, auth);

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
