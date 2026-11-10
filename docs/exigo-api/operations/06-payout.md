# Exigo API — Payout

API version v2025.11.7.6. Crawled 2026-11-11 from https://api.exigo.com/3.0/. Back to [index](../README.md).

| Operation | REST | Summary |
|---|---|---|
| [CreateBill](#createbill) | `POST /3.0/bill` | Creates a new bill |
| [UpdateBill](#updatebill) | `PATCH /3.0/bill` | Updates one or more fields on an existing customer bill. |
| [GetBills](#getbills) | `GET /3.0/payout/bills?customers=1` | Gets existing customer bills |
| [GetBillAmountsDue](#getbillamountsdue) | `GET /3.0/payout/amountsdue?startDate=1` | Gets customer bill amounts due grouped by customer. |
| [QueueBillPayout](#queuebillpayout) | `POST /3.0/payout/queuepayout` | Queues a new customer bill payout to be process by a third party. |
| [CreateBillPayout](#createbillpayout) | `POST /3.0/payout/createpayout` | Creates payment transaction records for customer bills. This method does not process third party transactions |
| [GetBillPayments](#getbillpayments) | `GET /3.0/payout/payments?paymentIDs=1` | Gets customer bill payments and associated bill records . |
| [GetBillPayoutQueue](#getbillpayoutqueue) | `GET /3.0/payout/payoutqueue?payoutQueueRequestID=1` | Gets customer bill payout queue status and details |
| [VoidPayments](#voidpayments) | `POST /3.0/payment/void` | Voids payments |
| [CreateBills](#createbills) | `POST /3.0/bills` | Creates max 100 new bills |

---
### CreateBill

> Creates a new bill

| | |
|---|---|
| Category | Payout |
| REST | `POST /3.0/bill` |
| SOAP action | `https://api.exigo.com/CreateBill` |
| WSDL elements | `CreateBillRequest` → `CreateBillResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateBill |

#### Input

**`CreateBillRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CurrencyCode` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `IsOtherIncome` | `Boolean` |  |
| `DueDate` | `DateTime` |  |
| `Amount` | `Decimal` |  |
| `Reference` | `String` | Optional. |
| `Notes` | `String` | Optional. |
| `BillStatusTypeID` | `Int32` | Optional. Bill Status (default is Unpaid). |
| `PayableTypeIDOverride` | `Int32` | Optional. Optionally override the payable type of the bill. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |
| `TaxablePeriodTy` | `Int32` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `TaxablePeriodID` | `Int32` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `WarehouseID` | `Int32` | Optional. Unique location for orders.<br>**Lookup:** company-specific list (see company-lists.md) |

#### Output

**`CreateBillResponse`**

| Property | Type | Notes |
|---|---|---|
| `BillID` | `Int32` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/bill HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "currencyCode": "usd",
  "isOtherIncome": true,
  "dueDate": "2026-11-10T00:00:00-06:00",
  "amount": null,
  "reference": "",
  "notes": "",
  "billStatusTypeID": 1,
  "payableTypeIDOverride": 1,
  "customerKey": "1",
  "taxablePeriodTy": 1,
  "taxablePeriodID": 1,
  "warehouseID": 1
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "billID": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateBill"

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
    <CreateBillRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CurrencyCode>string</CurrencyCode>
      <IsOtherIncome>boolean</IsOtherIncome>
      <DueDate>dateTime</DueDate>
      <Amount>decimal</Amount>
      <Reference>string</Reference>
      <Notes>string</Notes>
      <BillStatusTypeID>int</BillStatusTypeID>
      <PayableTypeIDOverride>int</PayableTypeIDOverride>
      <CustomerKey>string</CustomerKey>
      <TaxablePeriodTy>int</TaxablePeriodTy>
      <TaxablePeriodID>int</TaxablePeriodID>
      <WarehouseID>int</WarehouseID>
    </CreateBillRequest>
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
    <CreateBillResult xmlns="http://api.exigo.com/">
      <BillID>int</BillID>
    </CreateBillResult>
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
    var req = new CreateBillRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CurrencyCode = "usd";
    req.IsOtherIncome = true;
    req.DueDate = DateTime.Today;
    req.Amount = 1;
    req.Reference = "1";
    req.Notes = "1";
    req.BillStatusTypeID = 1;       //Bill Status (default is Unpaid)
    req.PayableTypeIDOverride = 1;  //Optionally override the payable type of the bill
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.TaxablePeriodTy = 1;
    req.TaxablePeriodID = 1;
    req.WarehouseID = 1;            //Unique location for orders

    //Send Request to Server and Get Response
    var res = await api.CreateBillAsync(req);

    //Now examine the results:
    Console.WriteLine("BillID: {0}", res.BillID);
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
    CreateBillRequest req = new CreateBillRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CurrencyCode = "usd";
    req.IsOtherIncome = true;
    req.DueDate = DateTime.Today;
    req.Amount = 1;
    req.Reference = "1";
    req.Notes = "1";
    req.BillStatusTypeID = 1;       //Bill Status (default is Unpaid)
    req.PayableTypeIDOverride = 1;  //Optionally override the payable type of the bill
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.TaxablePeriodTy = 1;
    req.TaxablePeriodID = 1;
    req.WarehouseID = 1;            //Unique location for orders

    //Send Request to Server and Get Response
    CreateBillResponse res = api.CreateBill(req);

    //Now examine the results:
    Console.WriteLine("BillID: {0}", res.BillID);
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
    Dim req as new CreateBillRequest()

    req.CustomerID = 1
    req.CurrencyCode = "usd"
    req.IsOtherIncome = true
    req.DueDate = DateTime.Today
    req.Amount = 1
    req.Reference = "1"
    req.Notes = "1"
    req.BillStatusTypeID = 1
    req.PayableTypeIDOverride = 1
    req.CustomerKey = "1"
    req.TaxablePeriodTy = 1
    req.TaxablePeriodID = 1
    req.WarehouseID = 1

    'Send Request to Server and Get Response
    Dim res As CreateBillResponse = api.CreateBill(req)

    'Now examine the results:
    Console.WriteLine("BillID: {0}", res.BillID)
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
    $req->IsOtherIncome = 1;
    $req->DueDate = 1;
    $req->Amount = 1;
    $req->Reference = "1";
    $req->Notes = "1";
    $req->BillStatusTypeID = 1;
    $req->PayableTypeIDOverride = 1;
    $req->CustomerKey = "1";
    $req->TaxablePeriodTy = 1;
    $req->TaxablePeriodID = 1;
    $req->WarehouseID = 1;

    //Send Request to Server and Get Response
    $res = $api.CreateBill($req);

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
    CreateBillRequest req = new CreateBillRequest();

    req.setCustomerID(1);
    req.setCurrencyCode("usd");
    req.setIsOtherIncome(1);
    req.setDueDate(1);
    req.setAmount(1);
    req.setReference("1");
    req.setNotes("1");
    req.setBillStatusTypeID(1);
    req.setPayableTypeIDOverride(1);
    req.setCustomerKey("1");
    req.setTaxablePeriodTy(1);
    req.setTaxablePeriodID(1);
    req.setWarehouseID(1);

    //Send Request to Server and Get Response
    CreateBillResponse res = api.getExigoApiSoap().createBill(req, auth);

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

### UpdateBill

> Updates one or more fields on an existing customer bill.

| | |
|---|---|
| Category | Payout |
| REST | `PATCH /3.0/bill` |
| SOAP action | `https://api.exigo.com/UpdateBill` |
| WSDL elements | `UpdateBillRequest` → `UpdateBillResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateBill |

#### Input

**`UpdateBillRequest`**

| Property | Type | Notes |
|---|---|---|
| `VendorBillID` | `Int32` | Unique numeric identifier for bill record. |
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |
| `WarehouseID` | `Int32` | Optional. Unique location for orders.<br>**Lookup:** company-specific list (see company-lists.md) |
| `CurrencyCode` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `DatePaymentDue` | `DateTime` | Optional. |
| `Reference` | `String` | Optional. |
| `DateReceived` | `DateTime` | Optional. |
| `Amount` | `Decimal` | Optional. |
| `IsOtherIncome` | `Boolean` | Optional. |
| `Notes` | `String` | Optional. |
| `StatusType` | `Int32` | Optional. Optional status of the bill (default is unpaid).<br>**Lookup:** company-specific list (see company-lists.md) |
| `PayableType` | `Int32` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `TaxablePeriodTy` | `Int32` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `TaxablePeriodID` | `Int32` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `VendorBillTy` | `Int32` | Optional. VendorBillTy.<br>**Lookup:** company-specific list (see company-lists.md) |

#### Output

**`UpdateBillResponse`**

_No properties._

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/bill HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "vendorBillID": 1,
  "customerID": 1,
  "customerKey": "1",
  "warehouseID": 1,
  "currencyCode": "usd",
  "datePaymentDue": "2026-11-10T00:00:00-06:00",
  "reference": "",
  "dateReceived": "2026-11-10T00:00:00-06:00",
  "amount": null,
  "isOtherIncome": true,
  "notes": "",
  "payableType": 1,
  "taxablePeriodTy": 1,
  "taxablePeriodID": 1
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
SOAPAction: "https://api.exigo.com/UpdateBill"

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
    <UpdateBillRequest xmlns="http://api.exigo.com/">
      <VendorBillID>int</VendorBillID>
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
      <WarehouseID>int</WarehouseID>
      <CurrencyCode>string</CurrencyCode>
      <DatePaymentDue>dateTime</DatePaymentDue>
      <Reference>string</Reference>
      <DateReceived>dateTime</DateReceived>
      <Amount>decimal</Amount>
      <IsOtherIncome>boolean</IsOtherIncome>
      <Notes>string</Notes>
      <StatusType>int</StatusType>
      <PayableType>int</PayableType>
      <TaxablePeriodTy>int</TaxablePeriodTy>
      <TaxablePeriodID>int</TaxablePeriodID>
      <VendorBillTy>int</VendorBillTy>
    </UpdateBillRequest>
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
    <UpdateBillResult xmlns="http://api.exigo.com/" />
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
    var req = new UpdateBillRequest();

    req.VendorBillID = 1;           //Unique numeric identifier for bill record.
    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided
    req.WarehouseID = 1;            //Unique location for orders
    req.CurrencyCode = "usd";
    req.DatePaymentDue = DateTime.Today;
    req.Reference = "1";
    req.DateReceived = DateTime.Today;
    req.Amount = 1;
    req.IsOtherIncome = true;
    req.Notes = "1";
    req.PayableType = 1;
    req.TaxablePeriodTy = 1;
    req.TaxablePeriodID = 1;

    //Send Request to Server and Get Response
    var res = await api.UpdateBillAsync(req);

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
    UpdateBillRequest req = new UpdateBillRequest();

    req.VendorBillID = 1;           //Unique numeric identifier for bill record.
    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided
    req.WarehouseID = 1;            //Unique location for orders
    req.CurrencyCode = "usd";
    req.DatePaymentDue = DateTime.Today;
    req.Reference = "1";
    req.DateReceived = DateTime.Today;
    req.Amount = 1;
    req.IsOtherIncome = true;
    req.Notes = "1";
    req.PayableType = 1;
    req.TaxablePeriodTy = 1;
    req.TaxablePeriodID = 1;

    //Send Request to Server and Get Response
    UpdateBillResponse res = api.UpdateBill(req);

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
    Dim req as new UpdateBillRequest()

    req.VendorBillID = 1
    req.CustomerID = 1
    req.CustomerKey = "1"
    req.WarehouseID = 1
    req.CurrencyCode = "usd"
    req.DatePaymentDue = DateTime.Today
    req.Reference = "1"
    req.DateReceived = DateTime.Today
    req.Amount = 1
    req.IsOtherIncome = true
    req.Notes = "1"
    req.PayableType = 1
    req.TaxablePeriodTy = 1
    req.TaxablePeriodID = 1

    'Send Request to Server and Get Response
    Dim res As UpdateBillResponse = api.UpdateBill(req)

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

    $req->VendorBillID = 1;
    $req->CustomerID = 1;
    $req->CustomerKey = "1";
    $req->WarehouseID = 1;
    $req->CurrencyCode = "usd";
    $req->DatePaymentDue = 1;
    $req->Reference = "1";
    $req->DateReceived = 1;
    $req->Amount = 1;
    $req->IsOtherIncome = 1;
    $req->Notes = "1";
    $req->PayableType = 1;
    $req->TaxablePeriodTy = 1;
    $req->TaxablePeriodID = 1;

    //Send Request to Server and Get Response
    $res = $api.UpdateBill($req);

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
    UpdateBillRequest req = new UpdateBillRequest();

    req.setVendorBillID(1);
    req.setCustomerID(1);
    req.setCustomerKey("1");
    req.setWarehouseID(1);
    req.setCurrencyCode("usd");
    req.setDatePaymentDue(1);
    req.setReference("1");
    req.setDateReceived(1);
    req.setAmount(1);
    req.setIsOtherIncome(1);
    req.setNotes("1");
    req.setPayableType(1);
    req.setTaxablePeriodTy(1);
    req.setTaxablePeriodID(1);

    //Send Request to Server and Get Response
    UpdateBillResponse res = api.getExigoApiSoap().updateBill(req, auth);

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

### GetBills

> Gets existing customer bills

| | |
|---|---|
| Category | Payout |
| REST | `GET /3.0/payout/bills?customers=1` |
| SOAP action | `https://api.exigo.com/GetBills` |
| WSDL elements | `GetBillsRequest` → `GetBillsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetBills |

#### Input

**`GetBillsRequest`**

| Property | Type | Notes |
|---|---|---|
| `Customers` | `Int32[]` | Optional. . Defaults to System.Int32[]. |
| `Bills` | `Int32[]` | Optional. . Defaults to System.Int32[]. |
| `StartBillID` | `Int32` | Optional. |
| `EndBillID` | `Int32` | Optional. |
| `WarehouseID` | `Int32` | Optional. Unique location for orders.<br>**Lookup:** company-specific list (see company-lists.md) |
| `StatusType` | `Int32` | Optional. Optional status of the bill (default is unpaid).<br>**Lookup:** company-specific list (see company-lists.md) |
| `DatePaymentDueStart` | `DateTime` | Optional. |
| `DatePaymentDueEnd` | `DateTime` | Optional. |
| `CurrencyCode` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `PayableType` | `Int32` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `TaxablePeriodType` | `Int32` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `TaxablePeriodID` | `Int32` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |

#### Output

**`GetBillsResponse`**

| Property | Type | Notes |
|---|---|---|
| `BillItems` | `BillItem[]` |  |

**`BillItem`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `BillID` | `Int32` |  |
| &nbsp;&nbsp;↳ `BillType` | `Int32` | The type of bill record.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `CustomerID` | `Int32` | Unique numeric identifier for a customer record. |
| &nbsp;&nbsp;↳ `WarehouseID` | `Int32` | Unique location for orders.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `PeriodID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `RunID` | `Int32` |  |
| &nbsp;&nbsp;↳ `StatusType` | `Int32` | Optional status of the bill (default is unpaid).<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Reference` | `String` |  |
| &nbsp;&nbsp;↳ `Notes` | `String` |  |
| &nbsp;&nbsp;↳ `SubTotal` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Shipping` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Tax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Amount` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CurrencyCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `DateReceived` | `DateTime` |  |
| &nbsp;&nbsp;↳ `DatePaymentDue` | `DateTime` |  |
| &nbsp;&nbsp;↳ `DateEntered` | `DateTime` |  |
| &nbsp;&nbsp;↳ `CreatedBy` | `String` |  |
| &nbsp;&nbsp;↳ `ModifiedBy` | `String` |  |
| &nbsp;&nbsp;↳ `ModifiedDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `BillImage` | `String` |  |
| &nbsp;&nbsp;↳ `IsOtherIncome` | `Boolean` |  |
| &nbsp;&nbsp;↳ `SourceType` | `Int32` | Bill origination source.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `PayableType` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `TaxablePeriodType` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `TaxablePeriodID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/payout/bills?customers=1
  &bills=1
  &startBillID=1
  &endBillID=1
  &warehouseID=1
  &datePaymentDueStart=1
  &datePaymentDueEnd=1
  &currencyCode=usd
  &payableType=1
  &taxablePeriodType=1
  &taxablePeriodID=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "billItems": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetBills"

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
    <GetBillsRequest xmlns="http://api.exigo.com/">
      <Customers>
        <int>int</int>
      </Customers>
      <Bills>
        <int>int</int>
      </Bills>
      <StartBillID>int</StartBillID>
      <EndBillID>int</EndBillID>
      <WarehouseID>int</WarehouseID>
      <StatusType>int</StatusType>
      <DatePaymentDueStart>dateTime</DatePaymentDueStart>
      <DatePaymentDueEnd>dateTime</DatePaymentDueEnd>
      <CurrencyCode>string</CurrencyCode>
      <PayableType>int</PayableType>
      <TaxablePeriodType>int</TaxablePeriodType>
      <TaxablePeriodID>int</TaxablePeriodID>
    </GetBillsRequest>
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
    <GetBillsResult xmlns="http://api.exigo.com/">
      <BillItems>
        <BillItem>
          <BillID>int</BillID>
          <BillType>int</BillType>
          <CustomerID>int</CustomerID>
          <WarehouseID>int</WarehouseID>
          <PeriodID>int</PeriodID>
          <RunID>int</RunID>
          <StatusType>int</StatusType>
          <Reference>string</Reference>
          <Notes>string</Notes>
          <SubTotal>decimal</SubTotal>
          <Shipping>decimal</Shipping>
          <Tax>decimal</Tax>
          <Amount>decimal</Amount>
          <CurrencyCode>string</CurrencyCode>
          <DateReceived>dateTime</DateReceived>
          <DatePaymentDue>dateTime</DatePaymentDue>
          <DateEntered>dateTime</DateEntered>
          <CreatedBy>string</CreatedBy>
          <ModifiedBy>string</ModifiedBy>
          <ModifiedDate>dateTime</ModifiedDate>
          <BillImage>string</BillImage>
          <IsOtherIncome>boolean</IsOtherIncome>
          <SourceType>int</SourceType>
          <PayableType>int</PayableType>
          <TaxablePeriodType>int</TaxablePeriodType>
          <TaxablePeriodID>int</TaxablePeriodID>
        </BillItem>
      </BillItems>
    </GetBillsResult>
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
    var req = new GetBillsRequest();

    //Add Customers
    var customers = new List<Int32>();
    customers.Add(1);
    customers.Add(2);

    //Now attach the list to the request
    req.Customers = customers.ToArray();

    //Add Bills
    var bills = new List<Int32>();
    bills.Add(1);
    bills.Add(2);

    //Now attach the list to the request
    req.Bills = bills.ToArray();
    req.StartBillID = 1;
    req.EndBillID = 1;
    req.WarehouseID = 1;            //Unique location for orders
    req.DatePaymentDueStart = DateTime.Today;
    req.DatePaymentDueEnd = DateTime.Today;
    req.CurrencyCode = "usd";
    req.PayableType = 1;
    req.TaxablePeriodType = 1;
    req.TaxablePeriodID = 1;

    //Send Request to Server and Get Response
    var res = await api.GetBillsAsync(req);

    //Now examine the results:

    foreach (var billItem  in res.BillItems)
    {
        Console.WriteLine("BillID: {0}", billItem.BillID);
        Console.WriteLine("CustomerID: {0}", billItem.CustomerID);
        Console.WriteLine("WarehouseID: {0}", billItem.WarehouseID);
        Console.WriteLine("PeriodID: {0}", billItem.PeriodID);
        Console.WriteLine("RunID: {0}", billItem.RunID);
        Console.WriteLine("Reference: {0}", billItem.Reference);
        Console.WriteLine("Notes: {0}", billItem.Notes);
        Console.WriteLine("SubTotal: {0}", billItem.SubTotal);
        Console.WriteLine("Shipping: {0}", billItem.Shipping);
        Console.WriteLine("Tax: {0}", billItem.Tax);
        Console.WriteLine("Amount: {0}", billItem.Amount);
        Console.WriteLine("CurrencyCode: {0}", billItem.CurrencyCode);
        Console.WriteLine("DateReceived: {0}", billItem.DateReceived);
        Console.WriteLine("DatePaymentDue: {0}", billItem.DatePaymentDue);
        Console.WriteLine("DateEntered: {0}", billItem.DateEntered);
        Console.WriteLine("CreatedBy: {0}", billItem.CreatedBy);
        Console.WriteLine("ModifiedBy: {0}", billItem.ModifiedBy);
        Console.WriteLine("ModifiedDate: {0}", billItem.ModifiedDate);
        Console.WriteLine("BillImage: {0}", billItem.BillImage);
        Console.WriteLine("IsOtherIncome: {0}", billItem.IsOtherIncome);
        Console.WriteLine("PayableType: {0}", billItem.PayableType);
        Console.WriteLine("TaxablePeriodType: {0}", billItem.TaxablePeriodType);
        Console.WriteLine("TaxablePeriodID: {0}", billItem.TaxablePeriodID);
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
    GetBillsRequest req = new GetBillsRequest();

    //Add Customers
    List<Int32> customers = new List<Int32>();
    customers.Add(1);
    customers.Add(2);

    //Now attach the list to the request
    req.Customers = customers.ToArray();

    //Add Bills
    List<Int32> bills = new List<Int32>();
    bills.Add(1);
    bills.Add(2);

    //Now attach the list to the request
    req.Bills = bills.ToArray();
    req.StartBillID = 1;
    req.EndBillID = 1;
    req.WarehouseID = 1;            //Unique location for orders
    req.DatePaymentDueStart = DateTime.Today;
    req.DatePaymentDueEnd = DateTime.Today;
    req.CurrencyCode = "usd";
    req.PayableType = 1;
    req.TaxablePeriodType = 1;
    req.TaxablePeriodID = 1;

    //Send Request to Server and Get Response
    GetBillsResponse res = api.GetBills(req);

    //Now examine the results:

    foreach (BillItem billItem  in res.BillItems)
    {
        Console.WriteLine("BillID: {0}", billItem.BillID);
        Console.WriteLine("CustomerID: {0}", billItem.CustomerID);
        Console.WriteLine("WarehouseID: {0}", billItem.WarehouseID);
        Console.WriteLine("PeriodID: {0}", billItem.PeriodID);
        Console.WriteLine("RunID: {0}", billItem.RunID);
        Console.WriteLine("Reference: {0}", billItem.Reference);
        Console.WriteLine("Notes: {0}", billItem.Notes);
        Console.WriteLine("SubTotal: {0}", billItem.SubTotal);
        Console.WriteLine("Shipping: {0}", billItem.Shipping);
        Console.WriteLine("Tax: {0}", billItem.Tax);
        Console.WriteLine("Amount: {0}", billItem.Amount);
        Console.WriteLine("CurrencyCode: {0}", billItem.CurrencyCode);
        Console.WriteLine("DateReceived: {0}", billItem.DateReceived);
        Console.WriteLine("DatePaymentDue: {0}", billItem.DatePaymentDue);
        Console.WriteLine("DateEntered: {0}", billItem.DateEntered);
        Console.WriteLine("CreatedBy: {0}", billItem.CreatedBy);
        Console.WriteLine("ModifiedBy: {0}", billItem.ModifiedBy);
        Console.WriteLine("ModifiedDate: {0}", billItem.ModifiedDate);
        Console.WriteLine("BillImage: {0}", billItem.BillImage);
        Console.WriteLine("IsOtherIncome: {0}", billItem.IsOtherIncome);
        Console.WriteLine("PayableType: {0}", billItem.PayableType);
        Console.WriteLine("TaxablePeriodType: {0}", billItem.TaxablePeriodType);
        Console.WriteLine("TaxablePeriodID: {0}", billItem.TaxablePeriodID);
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
    Dim req as new GetBillsRequest()

    'Add Customers
    Dim customers As New List(Of Int32)()
    customers.Add(1)
    customers.Add(2)

    'Now attach the list to the request
    req.Customers = customers.ToArray()

    'Add Bills
    Dim bills As New List(Of Int32)()
    bills.Add(1)
    bills.Add(2)

    'Now attach the list to the request
    req.Bills = bills.ToArray()
    req.StartBillID = 1
    req.EndBillID = 1
    req.WarehouseID = 1
    req.DatePaymentDueStart = DateTime.Today
    req.DatePaymentDueEnd = DateTime.Today
    req.CurrencyCode = "usd"
    req.PayableType = 1
    req.TaxablePeriodType = 1
    req.TaxablePeriodID = 1

    'Send Request to Server and Get Response
    Dim res As GetBillsResponse = api.GetBills(req)

    'Now examine the results:

    For Each billItem As BillItem In res.BillItems
        Console.WriteLine("BillID: {0}", billItem.BillID)
        Console.WriteLine("CustomerID: {0}", billItem.CustomerID)
        Console.WriteLine("WarehouseID: {0}", billItem.WarehouseID)
        Console.WriteLine("PeriodID: {0}", billItem.PeriodID)
        Console.WriteLine("RunID: {0}", billItem.RunID)
        Console.WriteLine("Reference: {0}", billItem.Reference)
        Console.WriteLine("Notes: {0}", billItem.Notes)
        Console.WriteLine("SubTotal: {0}", billItem.SubTotal)
        Console.WriteLine("Shipping: {0}", billItem.Shipping)
        Console.WriteLine("Tax: {0}", billItem.Tax)
        Console.WriteLine("Amount: {0}", billItem.Amount)
        Console.WriteLine("CurrencyCode: {0}", billItem.CurrencyCode)
        Console.WriteLine("DateReceived: {0}", billItem.DateReceived)
        Console.WriteLine("DatePaymentDue: {0}", billItem.DatePaymentDue)
        Console.WriteLine("DateEntered: {0}", billItem.DateEntered)
        Console.WriteLine("CreatedBy: {0}", billItem.CreatedBy)
        Console.WriteLine("ModifiedBy: {0}", billItem.ModifiedBy)
        Console.WriteLine("ModifiedDate: {0}", billItem.ModifiedDate)
        Console.WriteLine("BillImage: {0}", billItem.BillImage)
        Console.WriteLine("IsOtherIncome: {0}", billItem.IsOtherIncome)
        Console.WriteLine("PayableType: {0}", billItem.PayableType)
        Console.WriteLine("TaxablePeriodType: {0}", billItem.TaxablePeriodType)
        Console.WriteLine("TaxablePeriodID: {0}", billItem.TaxablePeriodID)
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

    //Add Customers

    //Now attach the list to the request
    req.Customers = array(customer1,customer2);

    //Add Bills

    //Now attach the list to the request
    req.Bills = array(bill1,bill2);
    $req->StartBillID = 1;
    $req->EndBillID = 1;
    $req->WarehouseID = 1;
    $req->DatePaymentDueStart = 1;
    $req->DatePaymentDueEnd = 1;
    $req->CurrencyCode = "usd";
    $req->PayableType = 1;
    $req->TaxablePeriodType = 1;
    $req->TaxablePeriodID = 1;

    //Send Request to Server and Get Response
    $res = $api.GetBills($req);

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
    GetBillsRequest req = new GetBillsRequest();

    //Add Customers
    ArrayOfSystem.Int32 customers = new ArrayOfSystem.Int32();

    Int32 customer1 = new Int32();
    customers.Add(customer1);

    Int32 customer2 = new Int32();
    customers.Add(customer2);

    //Now attach the list to the request
    req.setCustomers(customers);

    //Add Bills
    ArrayOfSystem.Int32 bills = new ArrayOfSystem.Int32();

    Int32 bill1 = new Int32();
    bills.Add(bill1);

    Int32 bill2 = new Int32();
    bills.Add(bill2);

    //Now attach the list to the request
    req.setBills(bills);
    req.setStartBillID(1);
    req.setEndBillID(1);
    req.setWarehouseID(1);
    req.setDatePaymentDueStart(1);
    req.setDatePaymentDueEnd(1);
    req.setCurrencyCode("usd");
    req.setPayableType(1);
    req.setTaxablePeriodType(1);
    req.setTaxablePeriodID(1);

    //Send Request to Server and Get Response
    GetBillsResponse res = api.getExigoApiSoap().getBills(req, auth);

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

### GetBillAmountsDue

> Gets customer bill amounts due grouped by customer.

| | |
|---|---|
| Category | Payout |
| REST | `GET /3.0/payout/amountsdue?startDate=1` |
| SOAP action | `https://api.exigo.com/GetBillAmountsDue` |
| WSDL elements | `GetBillAmountsDueRequest` → `GetBillAmountsDueResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetBillAmountsDue |

#### Input

**`GetBillAmountsDueRequest`**

| Property | Type | Notes |
|---|---|---|
| `StartDate` | `DateTime` |  |
| `EndDate` | `DateTime` |  |
| `CurrencyCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| `CountryCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| `PayableType` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| `PaymentCardType` | `Int32` | Optional. The type of paycard.<br>**Lookup:** company-specific list (see company-lists.md) |
| `MinimumAmount` | `Decimal` |  |
| `MaximumAmount` | `Decimal` | Optional. |
| `Customers` | `Int32[]` | Optional. Use this to filter list by one or more customer ids. Defaults to System.Int32[]. |

#### Output

**`GetBillAmountsDueResponse`**

| Property | Type | Notes |
|---|---|---|
| `AmountsDue` | `BillAmount[]` |  |

**`BillAmount`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `CustomerID` | `Int32` | Unique numeric identifier for a customer record. |
| &nbsp;&nbsp;↳ `Name` | `String` |  |
| &nbsp;&nbsp;↳ `BillDetails` | `BillDetail[]` |  |
| &nbsp;&nbsp;↳ `AmountDue` | `Decimal` |  |
| &nbsp;&nbsp;↳ `TotalBills` | `Int32` |  |

**`BillDetail`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `BillID` | `Int32` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `AmountDue` | `Decimal` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/payout/amountsdue?startDate=1
  &endDate=1
  &currencyCode=1
  &countryCode=1
  &payableType=1
  &paymentCardType=1
  &minimumAmount=1
  &maximumAmount=1
  &customers=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "amountsDue": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetBillAmountsDue"

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
    <GetBillAmountsDueRequest xmlns="http://api.exigo.com/">
      <StartDate>dateTime</StartDate>
      <EndDate>dateTime</EndDate>
      <CurrencyCode>string</CurrencyCode>
      <CountryCode>string</CountryCode>
      <PayableType>int</PayableType>
      <PaymentCardType>int</PaymentCardType>
      <MinimumAmount>decimal</MinimumAmount>
      <MaximumAmount>decimal</MaximumAmount>
      <Customers>
        <int>int</int>
      </Customers>
    </GetBillAmountsDueRequest>
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
    <GetBillAmountsDueResult xmlns="http://api.exigo.com/">
      <AmountsDue>
        <BillAmount>
          <CustomerID>int</CustomerID>
          <Name>string</Name>
          <BillDetails>
            <BillDetail>
              <BillID>int</BillID>
              <AmountDue>decimal</AmountDue>
            </BillDetail>
          </BillDetails>
          <AmountDue>decimal</AmountDue>
          <TotalBills>int</TotalBills>
        </BillAmount>
      </AmountsDue>
    </GetBillAmountsDueResult>
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
    var req = new GetBillAmountsDueRequest();

    req.StartDate = DateTime.Today;
    req.EndDate = DateTime.Today;
    req.CurrencyCode = "1";
    req.CountryCode = "1";
    req.PayableType = 1;
    req.PaymentCardType = 1;        //The type of paycard
    req.MinimumAmount = 1;
    req.MaximumAmount = 1;

    //Add Customers
    var customers = new List<Int32>();
    customers.Add(1);
    customers.Add(2);

    //Now attach the list to the request
    req.Customers = customers.ToArray();

    //Send Request to Server and Get Response
    var res = await api.GetBillAmountsDueAsync(req);

    //Now examine the results:

    foreach (var billAmount  in res.AmountsDue)
    {
        Console.WriteLine("CustomerID: {0}", billAmount.CustomerID);
        Console.WriteLine("Name: {0}", billAmount.Name);

        foreach (var billDetail  in billAmount.BillDetails)
        {
            Console.WriteLine("BillID: {0}", billDetail.BillID);
            Console.WriteLine("AmountDue: {0}", billDetail.AmountDue);
        }
        Console.WriteLine("AmountDue: {0}", billAmount.AmountDue);
        Console.WriteLine("TotalBills: {0}", billAmount.TotalBills);
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
    GetBillAmountsDueRequest req = new GetBillAmountsDueRequest();

    req.StartDate = DateTime.Today;
    req.EndDate = DateTime.Today;
    req.CurrencyCode = "1";
    req.CountryCode = "1";
    req.PayableType = 1;
    req.PaymentCardType = 1;        //The type of paycard
    req.MinimumAmount = 1;
    req.MaximumAmount = 1;

    //Add Customers
    List<Int32> customers = new List<Int32>();
    customers.Add(1);
    customers.Add(2);

    //Now attach the list to the request
    req.Customers = customers.ToArray();

    //Send Request to Server and Get Response
    GetBillAmountsDueResponse res = api.GetBillAmountsDue(req);

    //Now examine the results:

    foreach (BillAmount billAmount  in res.AmountsDue)
    {
        Console.WriteLine("CustomerID: {0}", billAmount.CustomerID);
        Console.WriteLine("Name: {0}", billAmount.Name);

        foreach (BillDetail billDetail  in billAmount.BillDetails)
        {
            Console.WriteLine("BillID: {0}", billDetail.BillID);
            Console.WriteLine("AmountDue: {0}", billDetail.AmountDue);
        }
        Console.WriteLine("AmountDue: {0}", billAmount.AmountDue);
        Console.WriteLine("TotalBills: {0}", billAmount.TotalBills);
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
    Dim req as new GetBillAmountsDueRequest()

    req.StartDate = DateTime.Today
    req.EndDate = DateTime.Today
    req.CurrencyCode = "1"
    req.CountryCode = "1"
    req.PayableType = 1
    req.PaymentCardType = 1
    req.MinimumAmount = 1
    req.MaximumAmount = 1

    'Add Customers
    Dim customers As New List(Of Int32)()
    customers.Add(1)
    customers.Add(2)

    'Now attach the list to the request
    req.Customers = customers.ToArray()

    'Send Request to Server and Get Response
    Dim res As GetBillAmountsDueResponse = api.GetBillAmountsDue(req)

    'Now examine the results:

    For Each billAmount As BillAmount In res.AmountsDue
        Console.WriteLine("CustomerID: {0}", billAmount.CustomerID)
        Console.WriteLine("Name: {0}", billAmount.Name)

        For Each billDetail As BillDetail In billAmount.BillDetails
            Console.WriteLine("BillID: {0}", billDetail.BillID)
            Console.WriteLine("AmountDue: {0}", billDetail.AmountDue)
        Next
        Console.WriteLine("AmountDue: {0}", billAmount.AmountDue)
        Console.WriteLine("TotalBills: {0}", billAmount.TotalBills)
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
    $req->CurrencyCode = "1";
    $req->CountryCode = "1";
    $req->PayableType = 1;
    $req->PaymentCardType = 1;
    $req->MinimumAmount = 1;
    $req->MaximumAmount = 1;

    //Add Customers

    //Now attach the list to the request
    req.Customers = array(customer1,customer2);

    //Send Request to Server and Get Response
    $res = $api.GetBillAmountsDue($req);

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
    GetBillAmountsDueRequest req = new GetBillAmountsDueRequest();

    req.setStartDate(1);
    req.setEndDate(1);
    req.setCurrencyCode("1");
    req.setCountryCode("1");
    req.setPayableType(1);
    req.setPaymentCardType(1);
    req.setMinimumAmount(1);
    req.setMaximumAmount(1);

    //Add Customers
    ArrayOfSystem.Int32 customers = new ArrayOfSystem.Int32();

    Int32 customer1 = new Int32();
    customers.Add(customer1);

    Int32 customer2 = new Int32();
    customers.Add(customer2);

    //Now attach the list to the request
    req.setCustomers(customers);

    //Send Request to Server and Get Response
    GetBillAmountsDueResponse res = api.getExigoApiSoap().getBillAmountsDue(req, auth);

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

### QueueBillPayout

> Queues a new customer bill payout to be process by a third party.

| | |
|---|---|
| Category | Payout |
| REST | `POST /3.0/payout/queuepayout` |
| SOAP action | `https://api.exigo.com/QueueBillPayout` |
| WSDL elements | `QueueBillPayoutRequest` → `QueueBillPayoutResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=QueueBillPayout |

#### Input

**`QueueBillPayoutRequest`**

| Property | Type | Notes |
|---|---|---|
| `StartDate` | `DateTime` |  |
| `EndDate` | `DateTime` |  |
| `CurrencyCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| `CountryCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| `PayableType` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| `PaymentCardType` | `Int32` | Optional. The type of paycard.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Reference` | `String` |  |
| `BatchDescription` | `String` |  |
| `UseBatchPayout` | `Boolean` | Optional. . Defaults to False. |
| `BankAccountID` | `Int32` |  |
| `Fee` | `Decimal` | Optional. |
| `FeeDescription` | `String` | Optional. |
| `StartCheckNumber` | `Int32` | Optional. |
| `CustomerID` | `Int32[]` | Optional. . Defaults to System.Int32[]. |
| `CustomerKey` | `String[]` | Optional. |
| `PaymentDate` | `DateTime` |  |
| `MinimumAmount` | `Decimal` | Optional. . Defaults to 0. |
| `MaximumAmount` | `Decimal` | Optional. |
| `GroupPaymentByVendor` | `Boolean` | Optional. . Defaults to True. |

#### Output

**`QueueBillPayoutResponse`**

| Property | Type | Notes |
|---|---|---|
| `PaymentQueueRequestId` | `Guid` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/payout/queuepayout HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "startDate": "2026-11-10T00:00:00-06:00",
  "endDate": "2026-11-10T00:00:00-06:00",
  "currencyCode": "1",
  "countryCode": "1",
  "payableType": 1,
  "paymentCardType": 1,
  "reference": "1",
  "batchDescription": "1",
  "useBatchPayout": true,
  "bankAccountID": 1,
  "fee": null,
  "feeDescription": "1",
  "startCheckNumber": 1,
  "customerID": null,
  "customerKey": null,
  "paymentDate": "2026-11-10T00:00:00-06:00",
  "minimumAmount": null,
  "maximumAmount": null,
  "groupPaymentByVendor": true
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "paymentQueueRequestId": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/QueueBillPayout"

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
    <QueueBillPayoutRequest xmlns="http://api.exigo.com/" />
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
    <QueueBillPayoutResult xmlns="http://api.exigo.com/">
      <PaymentQueueRequestId>guid</PaymentQueueRequestId>
    </QueueBillPayoutResult>
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
    var req = new QueueBillPayoutRequest();

    req.StartDate = DateTime.Today;
    req.EndDate = DateTime.Today;
    req.CurrencyCode = "1";
    req.CountryCode = "1";
    req.PayableType = 1;
    req.PaymentCardType = 1;        //The type of paycard
    req.Reference = "1";
    req.BatchDescription = "1";
    req.UseBatchPayout = true;
    req.BankAccountID = 1;
    req.Fee = 1;
    req.FeeDescription = "1";
    req.StartCheckNumber = 1;

    //Add CustomerID
    var customerid = new List<Int32>();
    customerid.Add(1);
    customerid.Add(2);

    //Now attach the list to the request
    req.CustomerID = customerid.ToArray();

    //Add CustomerKey
    var customerkey = new List<String>();
    customerkey.Add("1");
    customerkey.Add("2");

    //Now attach the list to the request
    req.CustomerKey = customerkey.ToArray();
    req.PaymentDate = DateTime.Today;
    req.MinimumAmount = 1;
    req.MaximumAmount = 1;
    req.GroupPaymentByVendor = true;

    //Send Request to Server and Get Response
    var res = await api.QueueBillPayoutAsync(req);

    //Now examine the results:
    Console.WriteLine("PaymentQueueRequestId: {0}", res.PaymentQueueRequestId);
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
    QueueBillPayoutRequest req = new QueueBillPayoutRequest();

    req.StartDate = DateTime.Today;
    req.EndDate = DateTime.Today;
    req.CurrencyCode = "1";
    req.CountryCode = "1";
    req.PayableType = 1;
    req.PaymentCardType = 1;        //The type of paycard
    req.Reference = "1";
    req.BatchDescription = "1";
    req.UseBatchPayout = true;
    req.BankAccountID = 1;
    req.Fee = 1;
    req.FeeDescription = "1";
    req.StartCheckNumber = 1;

    //Add CustomerID
    List<Int32> customerid = new List<Int32>();
    customerid.Add(1);
    customerid.Add(2);

    //Now attach the list to the request
    req.CustomerID = customerid.ToArray();

    //Add CustomerKey
    List<String> customerkey = new List<String>();
    customerkey.Add("1");
    customerkey.Add("2");

    //Now attach the list to the request
    req.CustomerKey = customerkey.ToArray();
    req.PaymentDate = DateTime.Today;
    req.MinimumAmount = 1;
    req.MaximumAmount = 1;
    req.GroupPaymentByVendor = true;

    //Send Request to Server and Get Response
    QueueBillPayoutResponse res = api.QueueBillPayout(req);

    //Now examine the results:
    Console.WriteLine("PaymentQueueRequestId: {0}", res.PaymentQueueRequestId);
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
    Dim req as new QueueBillPayoutRequest()

    req.StartDate = DateTime.Today
    req.EndDate = DateTime.Today
    req.CurrencyCode = "1"
    req.CountryCode = "1"
    req.PayableType = 1
    req.PaymentCardType = 1
    req.Reference = "1"
    req.BatchDescription = "1"
    req.UseBatchPayout = true
    req.BankAccountID = 1
    req.Fee = 1
    req.FeeDescription = "1"
    req.StartCheckNumber = 1

    'Add CustomerID
    Dim customerid As New List(Of Int32)()
    customerid.Add(1)
    customerid.Add(2)

    'Now attach the list to the request
    req.CustomerID = customerid.ToArray()

    'Add CustomerKey
    Dim customerkey As New List(Of String)()
    customerkey.Add("1")
    customerkey.Add("2")

    'Now attach the list to the request
    req.CustomerKey = customerkey.ToArray()
    req.PaymentDate = DateTime.Today
    req.MinimumAmount = 1
    req.MaximumAmount = 1
    req.GroupPaymentByVendor = true

    'Send Request to Server and Get Response
    Dim res As QueueBillPayoutResponse = api.QueueBillPayout(req)

    'Now examine the results:
    Console.WriteLine("PaymentQueueRequestId: {0}", res.PaymentQueueRequestId)
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
    $req->CurrencyCode = "1";
    $req->CountryCode = "1";
    $req->PayableType = 1;
    $req->PaymentCardType = 1;
    $req->Reference = "1";
    $req->BatchDescription = "1";
    $req->UseBatchPayout = 1;
    $req->BankAccountID = 1;
    $req->Fee = 1;
    $req->FeeDescription = "1";
    $req->StartCheckNumber = 1;

    //Add CustomerID

    //Now attach the list to the request
    req.CustomerID = array(customerI1,customerI2);

    //Add CustomerKey

    $customerKe1->Chars = 1;
    $customerKe1->Length = 1;

    $customerKe2->Length = 2;
    $customerKe2->Chars = 2;

    //Now attach the list to the request
    req.CustomerKey = array(customerKe1,customerKe2);
    $req->PaymentDate = 1;
    $req->MinimumAmount = 1;
    $req->MaximumAmount = 1;
    $req->GroupPaymentByVendor = 1;

    //Send Request to Server and Get Response
    $res = $api.QueueBillPayout($req);

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
    QueueBillPayoutRequest req = new QueueBillPayoutRequest();

    req.setStartDate(1);
    req.setEndDate(1);
    req.setCurrencyCode("1");
    req.setCountryCode("1");
    req.setPayableType(1);
    req.setPaymentCardType(1);
    req.setReference("1");
    req.setBatchDescription("1");
    req.setUseBatchPayout(1);
    req.setBankAccountID(1);
    req.setFee(1);
    req.setFeeDescription("1");
    req.setStartCheckNumber(1);

    //Add CustomerID
    ArrayOfSystem.Int32 customerid = new ArrayOfSystem.Int32();

    Int32 customerI1 = new Int32();
    customerid.Add(customerI1);

    Int32 customerI2 = new Int32();
    customerid.Add(customerI2);

    //Now attach the list to the request
    req.setCustomerID(customerid);

    //Add CustomerKey
    ArrayOfSystem.String customerkey = new ArrayOfSystem.String();

    String customerKe1 = new String();
    customerKe1.setLength(1);
    customerKe1.setChars(1);
    customerkey.Add(customerKe1);

    String customerKe2 = new String();
    customerKe2.setLength(2);
    customerKe2.setChars(2);
    customerkey.Add(customerKe2);

    //Now attach the list to the request
    req.setCustomerKey(customerkey);
    req.setPaymentDate(1);
    req.setMinimumAmount(1);
    req.setMaximumAmount(1);
    req.setGroupPaymentByVendor(1);

    //Send Request to Server and Get Response
    QueueBillPayoutResponse res = api.getExigoApiSoap().queueBillPayout(req, auth);

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

### CreateBillPayout

> Creates payment transaction records for customer bills. This method does not process third party transactions

| | |
|---|---|
| Category | Payout |
| REST | `POST /3.0/payout/createpayout` |
| SOAP action | `https://api.exigo.com/CreateBillPayout` |
| WSDL elements | `CreateBillPayoutRequest` → `CreateBillPayoutResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateBillPayout |

#### Input

**`CreateBillPayoutRequest`**

| Property | Type | Notes |
|---|---|---|
| `StartDate` | `DateTime` |  |
| `EndDate` | `DateTime` |  |
| `CurrencyCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| `CountryCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| `PayableType` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| `PaymentCardType` | `Int32` | Optional. The type of paycard.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Reference` | `String` |  |
| `BatchDescription` | `String` |  |
| `UseBatchPayout` | `Boolean` | Optional. . Defaults to False. |
| `BankAccountID` | `Int32` |  |
| `Fee` | `Decimal` | Optional. |
| `FeeDescription` | `String` | Optional. |
| `StartCheckNumber` | `Int32` | Optional. |
| `CustomerID` | `Int32[]` | Optional. . Defaults to System.Int32[]. |
| `CustomerKey` | `String[]` | Optional. |
| `PaymentDate` | `DateTime` |  |
| `MinimumAmount` | `Decimal` | Optional. . Defaults to 0. |
| `MaximumAmount` | `Decimal` | Optional. |
| `GroupPaymentByVendor` | `Boolean` | Optional. . Defaults to True. |

#### Output

**`CreateBillPayoutResponse`**

| Property | Type | Notes |
|---|---|---|
| `StartCheckNumber` | `Int32` |  |
| `EndCheckNumber` | `Int32` |  |
| `StartPaymentID` | `Int32` |  |
| `EndPaymentID` | `Int32` |  |
| `PayoutTotal` | `Decimal` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/payout/createpayout HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "startDate": "2026-11-10T00:00:00-06:00",
  "endDate": "2026-11-10T00:00:00-06:00",
  "currencyCode": "1",
  "countryCode": "1",
  "payableType": 1,
  "paymentCardType": 1,
  "reference": "1",
  "batchDescription": "1",
  "useBatchPayout": true,
  "bankAccountID": 1,
  "fee": null,
  "feeDescription": "1",
  "startCheckNumber": 1,
  "customerID": null,
  "customerKey": null,
  "paymentDate": "2026-11-10T00:00:00-06:00",
  "minimumAmount": null,
  "maximumAmount": null,
  "groupPaymentByVendor": true
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "startCheckNumber": 1,
  "endCheckNumber": 1,
  "startPaymentID": 1,
  "endPaymentID": 1,
  "payoutTotal": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateBillPayout"

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
    <CreateBillPayoutRequest xmlns="http://api.exigo.com/" />
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
    <CreateBillPayoutResult xmlns="http://api.exigo.com/">
      <StartCheckNumber>int</StartCheckNumber>
      <EndCheckNumber>int</EndCheckNumber>
      <StartPaymentID>int</StartPaymentID>
      <EndPaymentID>int</EndPaymentID>
      <PayoutTotal>decimal</PayoutTotal>
    </CreateBillPayoutResult>
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
    var req = new CreateBillPayoutRequest();

    req.StartDate = DateTime.Today;
    req.EndDate = DateTime.Today;
    req.CurrencyCode = "1";
    req.CountryCode = "1";
    req.PayableType = 1;
    req.PaymentCardType = 1;        //The type of paycard
    req.Reference = "1";
    req.BatchDescription = "1";
    req.UseBatchPayout = true;
    req.BankAccountID = 1;
    req.Fee = 1;
    req.FeeDescription = "1";
    req.StartCheckNumber = 1;

    //Add CustomerID
    var customerid = new List<Int32>();
    customerid.Add(1);
    customerid.Add(2);

    //Now attach the list to the request
    req.CustomerID = customerid.ToArray();

    //Add CustomerKey
    var customerkey = new List<String>();
    customerkey.Add("1");
    customerkey.Add("2");

    //Now attach the list to the request
    req.CustomerKey = customerkey.ToArray();
    req.PaymentDate = DateTime.Today;
    req.MinimumAmount = 1;
    req.MaximumAmount = 1;
    req.GroupPaymentByVendor = true;

    //Send Request to Server and Get Response
    var res = await api.CreateBillPayoutAsync(req);

    //Now examine the results:
    Console.WriteLine("StartCheckNumber: {0}", res.StartCheckNumber);
    Console.WriteLine("EndCheckNumber: {0}", res.EndCheckNumber);
    Console.WriteLine("StartPaymentID: {0}", res.StartPaymentID);
    Console.WriteLine("EndPaymentID: {0}", res.EndPaymentID);
    Console.WriteLine("PayoutTotal: {0}", res.PayoutTotal);
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
    CreateBillPayoutRequest req = new CreateBillPayoutRequest();

    req.StartDate = DateTime.Today;
    req.EndDate = DateTime.Today;
    req.CurrencyCode = "1";
    req.CountryCode = "1";
    req.PayableType = 1;
    req.PaymentCardType = 1;        //The type of paycard
    req.Reference = "1";
    req.BatchDescription = "1";
    req.UseBatchPayout = true;
    req.BankAccountID = 1;
    req.Fee = 1;
    req.FeeDescription = "1";
    req.StartCheckNumber = 1;

    //Add CustomerID
    List<Int32> customerid = new List<Int32>();
    customerid.Add(1);
    customerid.Add(2);

    //Now attach the list to the request
    req.CustomerID = customerid.ToArray();

    //Add CustomerKey
    List<String> customerkey = new List<String>();
    customerkey.Add("1");
    customerkey.Add("2");

    //Now attach the list to the request
    req.CustomerKey = customerkey.ToArray();
    req.PaymentDate = DateTime.Today;
    req.MinimumAmount = 1;
    req.MaximumAmount = 1;
    req.GroupPaymentByVendor = true;

    //Send Request to Server and Get Response
    CreateBillPayoutResponse res = api.CreateBillPayout(req);

    //Now examine the results:
    Console.WriteLine("StartCheckNumber: {0}", res.StartCheckNumber);
    Console.WriteLine("EndCheckNumber: {0}", res.EndCheckNumber);
    Console.WriteLine("StartPaymentID: {0}", res.StartPaymentID);
    Console.WriteLine("EndPaymentID: {0}", res.EndPaymentID);
    Console.WriteLine("PayoutTotal: {0}", res.PayoutTotal);
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
    Dim req as new CreateBillPayoutRequest()

    req.StartDate = DateTime.Today
    req.EndDate = DateTime.Today
    req.CurrencyCode = "1"
    req.CountryCode = "1"
    req.PayableType = 1
    req.PaymentCardType = 1
    req.Reference = "1"
    req.BatchDescription = "1"
    req.UseBatchPayout = true
    req.BankAccountID = 1
    req.Fee = 1
    req.FeeDescription = "1"
    req.StartCheckNumber = 1

    'Add CustomerID
    Dim customerid As New List(Of Int32)()
    customerid.Add(1)
    customerid.Add(2)

    'Now attach the list to the request
    req.CustomerID = customerid.ToArray()

    'Add CustomerKey
    Dim customerkey As New List(Of String)()
    customerkey.Add("1")
    customerkey.Add("2")

    'Now attach the list to the request
    req.CustomerKey = customerkey.ToArray()
    req.PaymentDate = DateTime.Today
    req.MinimumAmount = 1
    req.MaximumAmount = 1
    req.GroupPaymentByVendor = true

    'Send Request to Server and Get Response
    Dim res As CreateBillPayoutResponse = api.CreateBillPayout(req)

    'Now examine the results:
    Console.WriteLine("StartCheckNumber: {0}", res.StartCheckNumber)
    Console.WriteLine("EndCheckNumber: {0}", res.EndCheckNumber)
    Console.WriteLine("StartPaymentID: {0}", res.StartPaymentID)
    Console.WriteLine("EndPaymentID: {0}", res.EndPaymentID)
    Console.WriteLine("PayoutTotal: {0}", res.PayoutTotal)
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
    $req->CurrencyCode = "1";
    $req->CountryCode = "1";
    $req->PayableType = 1;
    $req->PaymentCardType = 1;
    $req->Reference = "1";
    $req->BatchDescription = "1";
    $req->UseBatchPayout = 1;
    $req->BankAccountID = 1;
    $req->Fee = 1;
    $req->FeeDescription = "1";
    $req->StartCheckNumber = 1;

    //Add CustomerID

    //Now attach the list to the request
    req.CustomerID = array(customerI1,customerI2);

    //Add CustomerKey

    $customerKe1->Length = 1;
    $customerKe1->Chars = 1;

    $customerKe2->Length = 2;
    $customerKe2->Chars = 2;

    //Now attach the list to the request
    req.CustomerKey = array(customerKe1,customerKe2);
    $req->PaymentDate = 1;
    $req->MinimumAmount = 1;
    $req->MaximumAmount = 1;
    $req->GroupPaymentByVendor = 1;

    //Send Request to Server and Get Response
    $res = $api.CreateBillPayout($req);

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
    CreateBillPayoutRequest req = new CreateBillPayoutRequest();

    req.setStartDate(1);
    req.setEndDate(1);
    req.setCurrencyCode("1");
    req.setCountryCode("1");
    req.setPayableType(1);
    req.setPaymentCardType(1);
    req.setReference("1");
    req.setBatchDescription("1");
    req.setUseBatchPayout(1);
    req.setBankAccountID(1);
    req.setFee(1);
    req.setFeeDescription("1");
    req.setStartCheckNumber(1);

    //Add CustomerID
    ArrayOfSystem.Int32 customerid = new ArrayOfSystem.Int32();

    Int32 customerI1 = new Int32();
    customerid.Add(customerI1);

    Int32 customerI2 = new Int32();
    customerid.Add(customerI2);

    //Now attach the list to the request
    req.setCustomerID(customerid);

    //Add CustomerKey
    ArrayOfSystem.String customerkey = new ArrayOfSystem.String();

    String customerKe1 = new String();
    customerKe1.setLength(1);
    customerKe1.setChars(1);
    customerkey.Add(customerKe1);

    String customerKe2 = new String();
    customerKe2.setLength(2);
    customerKe2.setChars(2);
    customerkey.Add(customerKe2);

    //Now attach the list to the request
    req.setCustomerKey(customerkey);
    req.setPaymentDate(1);
    req.setMinimumAmount(1);
    req.setMaximumAmount(1);
    req.setGroupPaymentByVendor(1);

    //Send Request to Server and Get Response
    CreateBillPayoutResponse res = api.getExigoApiSoap().createBillPayout(req, auth);

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

### GetBillPayments

> Gets customer bill payments and associated bill records .

| | |
|---|---|
| Category | Payout |
| REST | `GET /3.0/payout/payments?paymentIDs=1` |
| SOAP action | `https://api.exigo.com/GetBillPayments` |
| WSDL elements | `GetBillPaymentsRequest` → `GetBillPaymentsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetBillPayments |

#### Input

**`GetBillPaymentsRequest`**

| Property | Type | Notes |
|---|---|---|
| `PaymentIDs` | `Int32[]` | Optional. . Defaults to System.Int32[]. |
| `StartPaymentID` | `Int32` | Optional. |
| `EndPaymentID` | `Int32` | Optional. |

#### Output

**`GetBillPaymentsResponse`**

| Property | Type | Notes |
|---|---|---|
| `BillPayments` | `BillPayment[]` |  |

**`BillPayment`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `PaymentID` | `Int32` |  |
| &nbsp;&nbsp;↳ `CustomerID` | `Int32` | Unique numeric identifier for a customer record. |
| &nbsp;&nbsp;↳ `PaymentType` | `Int32` | Payment type.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `PaymentDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `Amount` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CurrencyCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `BankAccountID` | `Int32` | Bank account identifier.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `PayeeName` | `String` |  |
| &nbsp;&nbsp;↳ `PayeeAddress1` | `String` |  |
| &nbsp;&nbsp;↳ `PayeeAddress2` | `String` |  |
| &nbsp;&nbsp;↳ `PayeeCity` | `String` |  |
| &nbsp;&nbsp;↳ `PayeeState` | `String` |  |
| &nbsp;&nbsp;↳ `PayeeZip` | `String` |  |
| &nbsp;&nbsp;↳ `PayeeCountry` | `String` |  |
| &nbsp;&nbsp;↳ `CheckNumber` | `String` | Check number will be auto generated if pay by check. |
| &nbsp;&nbsp;↳ `CheckDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `ClearedDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `VoidedDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `DeductionType` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `DeductionNotes` | `String` |  |
| &nbsp;&nbsp;↳ `IsTaxable` | `Boolean` |  |
| &nbsp;&nbsp;↳ `PeriodID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Reference` | `String` |  |
| &nbsp;&nbsp;↳ `TransactionDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `ModifiedDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `CreatedBy` | `String` |  |
| &nbsp;&nbsp;↳ `ModifiedBy` | `String` |  |
| &nbsp;&nbsp;↳ `PayeeCompany` | `String` |  |
| &nbsp;&nbsp;↳ `DepositNumber` | `String` | Will be auto generated if pay by direct deposit. |
| &nbsp;&nbsp;↳ `Other1` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Other2` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Other3` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Other4` | `String` | **Lookup:** company-specific list (see company-lists.md) |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/payout/payments?paymentIDs=1
  &startPaymentID=1
  &endPaymentID=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "billPayments": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetBillPayments"

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
    <GetBillPaymentsRequest xmlns="http://api.exigo.com/">
      <PaymentIDs>
        <int>int</int>
      </PaymentIDs>
      <StartPaymentID>int</StartPaymentID>
      <EndPaymentID>int</EndPaymentID>
    </GetBillPaymentsRequest>
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
    <GetBillPaymentsResult xmlns="http://api.exigo.com/">
      <BillPayments>
        <BillPayment>
          <BillItems>
            <BillItem>
              <BillID>int</BillID>
              <BillType>int</BillType>
              <CustomerID>int</CustomerID>
              <WarehouseID>int</WarehouseID>
              <PeriodID>int</PeriodID>
              <RunID>int</RunID>
              <StatusType>int</StatusType>
              <Reference>string</Reference>
              <Notes>string</Notes>
              <SubTotal>decimal</SubTotal>
              <Shipping>decimal</Shipping>
              <Tax>decimal</Tax>
              <Amount>decimal</Amount>
              <CurrencyCode>string</CurrencyCode>
              <DateReceived>dateTime</DateReceived>
              <DatePaymentDue>dateTime</DatePaymentDue>
              <DateEntered>dateTime</DateEntered>
              <CreatedBy>string</CreatedBy>
              <ModifiedBy>string</ModifiedBy>
              <ModifiedDate>dateTime</ModifiedDate>
              <BillImage>string</BillImage>
              <IsOtherIncome>boolean</IsOtherIncome>
              <SourceType>int</SourceType>
              <PayableType>int</PayableType>
              <TaxablePeriodType>int</TaxablePeriodType>
              <TaxablePeriodID>int</TaxablePeriodID>
            </BillItem>
          </BillItems>
          <PaymentID>int</PaymentID>
          <CustomerID>int</CustomerID>
          <PaymentType>int</PaymentType>
          <PaymentDate>dateTime</PaymentDate>
          <Amount>decimal</Amount>
          <CurrencyCode>string</CurrencyCode>
          <BankAccountID>int</BankAccountID>
          <PayeeName>string</PayeeName>
          <PayeeAddress1>string</PayeeAddress1>
          <PayeeAddress2>string</PayeeAddress2>
          <PayeeCity>string</PayeeCity>
          <PayeeState>string</PayeeState>
          <PayeeZip>string</PayeeZip>
          <PayeeCountry>string</PayeeCountry>
          <CheckNumber>string</CheckNumber>
          <CheckDate>dateTime</CheckDate>
          <ClearedDate>dateTime</ClearedDate>
          <VoidedDate>dateTime</VoidedDate>
          <DeductionType>int</DeductionType>
          <DeductionNotes>string</DeductionNotes>
          <IsTaxable>boolean</IsTaxable>
          <PeriodID>int</PeriodID>
          <Reference>string</Reference>
          <TransactionDate>dateTime</TransactionDate>
          <ModifiedDate>dateTime</ModifiedDate>
          <CreatedBy>string</CreatedBy>
          <ModifiedBy>string</ModifiedBy>
          <PayeeCompany>string</PayeeCompany>
          <DepositNumber>string</DepositNumber>
          <Other1>string</Other1>
          <Other2>string</Other2>
          <Other3>string</Other3>
          <Other4>string</Other4>
        </BillPayment>
      </BillPayments>
    </GetBillPaymentsResult>
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
    var req = new GetBillPaymentsRequest();

    //Add PaymentIDs
    var paymentids = new List<Int32>();
    paymentids.Add(1);
    paymentids.Add(2);

    //Now attach the list to the request
    req.PaymentIDs = paymentids.ToArray();
    req.StartPaymentID = 1;
    req.EndPaymentID = 1;

    //Send Request to Server and Get Response
    var res = await api.GetBillPaymentsAsync(req);

    //Now examine the results:

    foreach (var billPayment  in res.BillPayments)
    {
        Console.WriteLine("PaymentID: {0}", billPayment.PaymentID);
        Console.WriteLine("CustomerID: {0}", billPayment.CustomerID);
        Console.WriteLine("PaymentType: {0}", billPayment.PaymentType);
        Console.WriteLine("PaymentDate: {0}", billPayment.PaymentDate);
        Console.WriteLine("Amount: {0}", billPayment.Amount);
        Console.WriteLine("CurrencyCode: {0}", billPayment.CurrencyCode);
        Console.WriteLine("PayeeName: {0}", billPayment.PayeeName);
        Console.WriteLine("PayeeAddress1: {0}", billPayment.PayeeAddress1);
        Console.WriteLine("PayeeAddress2: {0}", billPayment.PayeeAddress2);
        Console.WriteLine("PayeeCity: {0}", billPayment.PayeeCity);
        Console.WriteLine("PayeeState: {0}", billPayment.PayeeState);
        Console.WriteLine("PayeeZip: {0}", billPayment.PayeeZip);
        Console.WriteLine("PayeeCountry: {0}", billPayment.PayeeCountry);
        Console.WriteLine("CheckNumber: {0}", billPayment.CheckNumber);
        Console.WriteLine("CheckDate: {0}", billPayment.CheckDate);
        Console.WriteLine("ClearedDate: {0}", billPayment.ClearedDate);
        Console.WriteLine("VoidedDate: {0}", billPayment.VoidedDate);
        Console.WriteLine("DeductionNotes: {0}", billPayment.DeductionNotes);
        Console.WriteLine("IsTaxable: {0}", billPayment.IsTaxable);
        Console.WriteLine("PeriodID: {0}", billPayment.PeriodID);
        Console.WriteLine("Reference: {0}", billPayment.Reference);
        Console.WriteLine("TransactionDate: {0}", billPayment.TransactionDate);
        Console.WriteLine("ModifiedDate: {0}", billPayment.ModifiedDate);
        Console.WriteLine("CreatedBy: {0}", billPayment.CreatedBy);
        Console.WriteLine("ModifiedBy: {0}", billPayment.ModifiedBy);
        Console.WriteLine("PayeeCompany: {0}", billPayment.PayeeCompany);
        Console.WriteLine("DepositNumber: {0}", billPayment.DepositNumber);
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
    GetBillPaymentsRequest req = new GetBillPaymentsRequest();

    //Add PaymentIDs
    List<Int32> paymentids = new List<Int32>();
    paymentids.Add(1);
    paymentids.Add(2);

    //Now attach the list to the request
    req.PaymentIDs = paymentids.ToArray();
    req.StartPaymentID = 1;
    req.EndPaymentID = 1;

    //Send Request to Server and Get Response
    GetBillPaymentsResponse res = api.GetBillPayments(req);

    //Now examine the results:

    foreach (BillPayment billPayment  in res.BillPayments)
    {
        Console.WriteLine("PaymentID: {0}", billPayment.PaymentID);
        Console.WriteLine("CustomerID: {0}", billPayment.CustomerID);
        Console.WriteLine("PaymentType: {0}", billPayment.PaymentType);
        Console.WriteLine("PaymentDate: {0}", billPayment.PaymentDate);
        Console.WriteLine("Amount: {0}", billPayment.Amount);
        Console.WriteLine("CurrencyCode: {0}", billPayment.CurrencyCode);
        Console.WriteLine("PayeeName: {0}", billPayment.PayeeName);
        Console.WriteLine("PayeeAddress1: {0}", billPayment.PayeeAddress1);
        Console.WriteLine("PayeeAddress2: {0}", billPayment.PayeeAddress2);
        Console.WriteLine("PayeeCity: {0}", billPayment.PayeeCity);
        Console.WriteLine("PayeeState: {0}", billPayment.PayeeState);
        Console.WriteLine("PayeeZip: {0}", billPayment.PayeeZip);
        Console.WriteLine("PayeeCountry: {0}", billPayment.PayeeCountry);
        Console.WriteLine("CheckNumber: {0}", billPayment.CheckNumber);
        Console.WriteLine("CheckDate: {0}", billPayment.CheckDate);
        Console.WriteLine("ClearedDate: {0}", billPayment.ClearedDate);
        Console.WriteLine("VoidedDate: {0}", billPayment.VoidedDate);
        Console.WriteLine("DeductionNotes: {0}", billPayment.DeductionNotes);
        Console.WriteLine("IsTaxable: {0}", billPayment.IsTaxable);
        Console.WriteLine("PeriodID: {0}", billPayment.PeriodID);
        Console.WriteLine("Reference: {0}", billPayment.Reference);
        Console.WriteLine("TransactionDate: {0}", billPayment.TransactionDate);
        Console.WriteLine("ModifiedDate: {0}", billPayment.ModifiedDate);
        Console.WriteLine("CreatedBy: {0}", billPayment.CreatedBy);
        Console.WriteLine("ModifiedBy: {0}", billPayment.ModifiedBy);
        Console.WriteLine("PayeeCompany: {0}", billPayment.PayeeCompany);
        Console.WriteLine("DepositNumber: {0}", billPayment.DepositNumber);
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
    Dim req as new GetBillPaymentsRequest()

    'Add PaymentIDs
    Dim paymentids As New List(Of Int32)()
    paymentids.Add(1)
    paymentids.Add(2)

    'Now attach the list to the request
    req.PaymentIDs = paymentids.ToArray()
    req.StartPaymentID = 1
    req.EndPaymentID = 1

    'Send Request to Server and Get Response
    Dim res As GetBillPaymentsResponse = api.GetBillPayments(req)

    'Now examine the results:

    For Each billPayment As BillPayment In res.BillPayments
        Console.WriteLine("PaymentID: {0}", billPayment.PaymentID)
        Console.WriteLine("CustomerID: {0}", billPayment.CustomerID)
        Console.WriteLine("PaymentType: {0}", billPayment.PaymentType)
        Console.WriteLine("PaymentDate: {0}", billPayment.PaymentDate)
        Console.WriteLine("Amount: {0}", billPayment.Amount)
        Console.WriteLine("CurrencyCode: {0}", billPayment.CurrencyCode)
        Console.WriteLine("PayeeName: {0}", billPayment.PayeeName)
        Console.WriteLine("PayeeAddress1: {0}", billPayment.PayeeAddress1)
        Console.WriteLine("PayeeAddress2: {0}", billPayment.PayeeAddress2)
        Console.WriteLine("PayeeCity: {0}", billPayment.PayeeCity)
        Console.WriteLine("PayeeState: {0}", billPayment.PayeeState)
        Console.WriteLine("PayeeZip: {0}", billPayment.PayeeZip)
        Console.WriteLine("PayeeCountry: {0}", billPayment.PayeeCountry)
        Console.WriteLine("CheckNumber: {0}", billPayment.CheckNumber)
        Console.WriteLine("CheckDate: {0}", billPayment.CheckDate)
        Console.WriteLine("ClearedDate: {0}", billPayment.ClearedDate)
        Console.WriteLine("VoidedDate: {0}", billPayment.VoidedDate)
        Console.WriteLine("DeductionNotes: {0}", billPayment.DeductionNotes)
        Console.WriteLine("IsTaxable: {0}", billPayment.IsTaxable)
        Console.WriteLine("PeriodID: {0}", billPayment.PeriodID)
        Console.WriteLine("Reference: {0}", billPayment.Reference)
        Console.WriteLine("TransactionDate: {0}", billPayment.TransactionDate)
        Console.WriteLine("ModifiedDate: {0}", billPayment.ModifiedDate)
        Console.WriteLine("CreatedBy: {0}", billPayment.CreatedBy)
        Console.WriteLine("ModifiedBy: {0}", billPayment.ModifiedBy)
        Console.WriteLine("PayeeCompany: {0}", billPayment.PayeeCompany)
        Console.WriteLine("DepositNumber: {0}", billPayment.DepositNumber)
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

    //Add PaymentIDs

    //Now attach the list to the request
    req.PaymentIDs = array(paymentID1,paymentID2);
    $req->StartPaymentID = 1;
    $req->EndPaymentID = 1;

    //Send Request to Server and Get Response
    $res = $api.GetBillPayments($req);

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
    GetBillPaymentsRequest req = new GetBillPaymentsRequest();

    //Add PaymentIDs
    ArrayOfSystem.Int32 paymentids = new ArrayOfSystem.Int32();

    Int32 paymentID1 = new Int32();
    paymentids.Add(paymentID1);

    Int32 paymentID2 = new Int32();
    paymentids.Add(paymentID2);

    //Now attach the list to the request
    req.setPaymentIDs(paymentids);
    req.setStartPaymentID(1);
    req.setEndPaymentID(1);

    //Send Request to Server and Get Response
    GetBillPaymentsResponse res = api.getExigoApiSoap().getBillPayments(req, auth);

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

### GetBillPayoutQueue

> Gets customer bill payout queue status and details

| | |
|---|---|
| Category | Payout |
| REST | `GET /3.0/payout/payoutqueue?payoutQueueRequestID=1` |
| SOAP action | `https://api.exigo.com/GetBillPayoutQueue` |
| WSDL elements | `GetBillPayoutQueueRequest` → `GetBillPayoutQueueResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetBillPayoutQueue |

#### Input

**`GetBillPayoutQueueRequest`**

| Property | Type | Notes |
|---|---|---|
| `PayoutQueueRequestID` | `Guid` | Optional. Unique numeric identifier for payout queue item. |
| `CurrencyCode` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `CountryCode` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `PayableType` | `Int32` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `PaymentCardType` | `Int32` | Optional. Use only if PaymentType = Payment Card.<br>**Lookup:** company-specific list (see company-lists.md) |
| `StartDate` | `DateTime` | Optional. |
| `EndDate` | `DateTime` | Optional. |

#### Output

**`GetBillPayoutQueueResponse`**

| Property | Type | Notes |
|---|---|---|
| `BillPayoutQueueItems` | `BillPayoutQueueItem[]` |  |

**`BillPayoutQueueItem`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `PayoutQueueRequestID` | `Guid` |  |
| &nbsp;&nbsp;↳ `Count` | `Int32` |  |
| &nbsp;&nbsp;↳ `Amount` | `Decimal` |  |
| &nbsp;&nbsp;↳ `MinimumAmount` | `Decimal` |  |
| &nbsp;&nbsp;↳ `MaximumAmount` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CountryCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Fee` | `Decimal` |  |
| &nbsp;&nbsp;↳ `FeeDescription` | `String` |  |
| &nbsp;&nbsp;↳ `PayableType` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `PaymentCardType` | `Int32` | The type of paycard.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `StartCheckNumber` | `Int32` |  |
| &nbsp;&nbsp;↳ `EndCheckNumber` | `Int32` |  |
| &nbsp;&nbsp;↳ `StartDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `EndDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `StartPaymentID` | `Int32` |  |
| &nbsp;&nbsp;↳ `EndPaymentID` | `Int32` |  |
| &nbsp;&nbsp;↳ `PaymentDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `CurrencyCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `BankAccountID` | `Int32` | Bank account identifier.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Reference` | `String` |  |
| &nbsp;&nbsp;↳ `RequestByUserID` | `Int32` |  |
| &nbsp;&nbsp;↳ `RequestDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `RequestCompleteDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `BatchDescription` | `String` |  |
| &nbsp;&nbsp;↳ `UseBatchPayout` | `Boolean` |  |
| &nbsp;&nbsp;↳ `StatusType` | `PayoutQueueStatusType` | Optional status of the bill (default is unpaid).<br>**Values:** `Processing`, `Complete`, `CompleteWithErrors` |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/payout/payoutqueue?payoutQueueRequestID=1
  &currencyCode=usd
  &payableType=1
  &paymentCardType=1
  &startDate=1
  &endDate=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "billPayoutQueueItems": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetBillPayoutQueue"

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
    <GetBillPayoutQueueRequest xmlns="http://api.exigo.com/">
      <PayoutQueueRequestID>guid</PayoutQueueRequestID>
      <CurrencyCode>string</CurrencyCode>
      <CountryCode>string</CountryCode>
      <PayableType>int</PayableType>
      <PaymentCardType>int</PaymentCardType>
      <StartDate>dateTime</StartDate>
      <EndDate>dateTime</EndDate>
    </GetBillPayoutQueueRequest>
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
    <GetBillPayoutQueueResult xmlns="http://api.exigo.com/">
      <BillPayoutQueueItems>
        <BillPayoutQueueItem>
          <PayoutQueueRequestID>guid</PayoutQueueRequestID>
          <Count>int</Count>
          <Amount>decimal</Amount>
          <MinimumAmount>decimal</MinimumAmount>
          <MaximumAmount>decimal</MaximumAmount>
          <CountryCode>string</CountryCode>
          <Fee>decimal</Fee>
          <FeeDescription>string</FeeDescription>
          <PayableType>int</PayableType>
          <PaymentCardType>int</PaymentCardType>
          <StartCheckNumber>int</StartCheckNumber>
          <EndCheckNumber>int</EndCheckNumber>
          <StartDate>dateTime</StartDate>
          <EndDate>dateTime</EndDate>
          <StartPaymentID>int</StartPaymentID>
          <EndPaymentID>int</EndPaymentID>
          <PaymentDate>dateTime</PaymentDate>
          <CurrencyCode>string</CurrencyCode>
          <BankAccountID>int</BankAccountID>
          <Reference>string</Reference>
          <RequestByUserID>int</RequestByUserID>
          <RequestDate>dateTime</RequestDate>
          <RequestCompleteDate>dateTime</RequestCompleteDate>
          <BatchDescription>string</BatchDescription>
          <UseBatchPayout>boolean</UseBatchPayout>
          <StatusType>Processing or Complete or CompleteWithErrors</StatusType>
        </BillPayoutQueueItem>
      </BillPayoutQueueItems>
    </GetBillPayoutQueueResult>
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
    var req = new GetBillPayoutQueueRequest();

    req.PayoutQueueRequestID = 1;   //Unique numeric identifier for payout queue item.
    req.CurrencyCode = "usd";
    req.PayableType = 1;
    req.PaymentCardType = 1;        //Use only if PaymentType = Payment Card
    req.StartDate = DateTime.Today;
    req.EndDate = DateTime.Today;

    //Send Request to Server and Get Response
    var res = await api.GetBillPayoutQueueAsync(req);

    //Now examine the results:

    foreach (var billPayoutQueueItem  in res.BillPayoutQueueItems)
    {
        Console.WriteLine("PayoutQueueRequestID: {0}", billPayoutQueueItem.PayoutQueueRequestID);
        Console.WriteLine("Count: {0}", billPayoutQueueItem.Count);
        Console.WriteLine("Amount: {0}", billPayoutQueueItem.Amount);
        Console.WriteLine("MinimumAmount: {0}", billPayoutQueueItem.MinimumAmount);
        Console.WriteLine("MaximumAmount: {0}", billPayoutQueueItem.MaximumAmount);
        Console.WriteLine("Fee: {0}", billPayoutQueueItem.Fee);
        Console.WriteLine("FeeDescription: {0}", billPayoutQueueItem.FeeDescription);
        Console.WriteLine("PayableType: {0}", billPayoutQueueItem.PayableType);
        Console.WriteLine("PaymentCardType: {0}", billPayoutQueueItem.PaymentCardType);
        Console.WriteLine("StartCheckNumber: {0}", billPayoutQueueItem.StartCheckNumber);
        Console.WriteLine("EndCheckNumber: {0}", billPayoutQueueItem.EndCheckNumber);
        Console.WriteLine("StartDate: {0}", billPayoutQueueItem.StartDate);
        Console.WriteLine("EndDate: {0}", billPayoutQueueItem.EndDate);
        Console.WriteLine("StartPaymentID: {0}", billPayoutQueueItem.StartPaymentID);
        Console.WriteLine("EndPaymentID: {0}", billPayoutQueueItem.EndPaymentID);
        Console.WriteLine("PaymentDate: {0}", billPayoutQueueItem.PaymentDate);
        Console.WriteLine("CurrencyCode: {0}", billPayoutQueueItem.CurrencyCode);
        Console.WriteLine("Reference: {0}", billPayoutQueueItem.Reference);
        Console.WriteLine("RequestByUserID: {0}", billPayoutQueueItem.RequestByUserID);
        Console.WriteLine("RequestDate: {0}", billPayoutQueueItem.RequestDate);
        Console.WriteLine("RequestCompleteDate: {0}", billPayoutQueueItem.RequestCompleteDate);
        Console.WriteLine("BatchDescription: {0}", billPayoutQueueItem.BatchDescription);
        Console.WriteLine("UseBatchPayout: {0}", billPayoutQueueItem.UseBatchPayout);
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
    GetBillPayoutQueueRequest req = new GetBillPayoutQueueRequest();

    req.PayoutQueueRequestID = 1;   //Unique numeric identifier for payout queue item.
    req.CurrencyCode = "usd";
    req.PayableType = 1;
    req.PaymentCardType = 1;        //Use only if PaymentType = Payment Card
    req.StartDate = DateTime.Today;
    req.EndDate = DateTime.Today;

    //Send Request to Server and Get Response
    GetBillPayoutQueueResponse res = api.GetBillPayoutQueue(req);

    //Now examine the results:

    foreach (BillPayoutQueueItem billPayoutQueueItem  in res.BillPayoutQueueItems)
    {
        Console.WriteLine("PayoutQueueRequestID: {0}", billPayoutQueueItem.PayoutQueueRequestID);
        Console.WriteLine("Count: {0}", billPayoutQueueItem.Count);
        Console.WriteLine("Amount: {0}", billPayoutQueueItem.Amount);
        Console.WriteLine("MinimumAmount: {0}", billPayoutQueueItem.MinimumAmount);
        Console.WriteLine("MaximumAmount: {0}", billPayoutQueueItem.MaximumAmount);
        Console.WriteLine("Fee: {0}", billPayoutQueueItem.Fee);
        Console.WriteLine("FeeDescription: {0}", billPayoutQueueItem.FeeDescription);
        Console.WriteLine("PayableType: {0}", billPayoutQueueItem.PayableType);
        Console.WriteLine("PaymentCardType: {0}", billPayoutQueueItem.PaymentCardType);
        Console.WriteLine("StartCheckNumber: {0}", billPayoutQueueItem.StartCheckNumber);
        Console.WriteLine("EndCheckNumber: {0}", billPayoutQueueItem.EndCheckNumber);
        Console.WriteLine("StartDate: {0}", billPayoutQueueItem.StartDate);
        Console.WriteLine("EndDate: {0}", billPayoutQueueItem.EndDate);
        Console.WriteLine("StartPaymentID: {0}", billPayoutQueueItem.StartPaymentID);
        Console.WriteLine("EndPaymentID: {0}", billPayoutQueueItem.EndPaymentID);
        Console.WriteLine("PaymentDate: {0}", billPayoutQueueItem.PaymentDate);
        Console.WriteLine("CurrencyCode: {0}", billPayoutQueueItem.CurrencyCode);
        Console.WriteLine("Reference: {0}", billPayoutQueueItem.Reference);
        Console.WriteLine("RequestByUserID: {0}", billPayoutQueueItem.RequestByUserID);
        Console.WriteLine("RequestDate: {0}", billPayoutQueueItem.RequestDate);
        Console.WriteLine("RequestCompleteDate: {0}", billPayoutQueueItem.RequestCompleteDate);
        Console.WriteLine("BatchDescription: {0}", billPayoutQueueItem.BatchDescription);
        Console.WriteLine("UseBatchPayout: {0}", billPayoutQueueItem.UseBatchPayout);
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
    Dim req as new GetBillPayoutQueueRequest()

    req.PayoutQueueRequestID = 1
    req.CurrencyCode = "usd"
    req.PayableType = 1
    req.PaymentCardType = 1
    req.StartDate = DateTime.Today
    req.EndDate = DateTime.Today

    'Send Request to Server and Get Response
    Dim res As GetBillPayoutQueueResponse = api.GetBillPayoutQueue(req)

    'Now examine the results:

    For Each billPayoutQueueItem As BillPayoutQueueItem In res.BillPayoutQueueItems
        Console.WriteLine("PayoutQueueRequestID: {0}", billPayoutQueueItem.PayoutQueueRequestID)
        Console.WriteLine("Count: {0}", billPayoutQueueItem.Count)
        Console.WriteLine("Amount: {0}", billPayoutQueueItem.Amount)
        Console.WriteLine("MinimumAmount: {0}", billPayoutQueueItem.MinimumAmount)
        Console.WriteLine("MaximumAmount: {0}", billPayoutQueueItem.MaximumAmount)
        Console.WriteLine("Fee: {0}", billPayoutQueueItem.Fee)
        Console.WriteLine("FeeDescription: {0}", billPayoutQueueItem.FeeDescription)
        Console.WriteLine("PayableType: {0}", billPayoutQueueItem.PayableType)
        Console.WriteLine("PaymentCardType: {0}", billPayoutQueueItem.PaymentCardType)
        Console.WriteLine("StartCheckNumber: {0}", billPayoutQueueItem.StartCheckNumber)
        Console.WriteLine("EndCheckNumber: {0}", billPayoutQueueItem.EndCheckNumber)
        Console.WriteLine("StartDate: {0}", billPayoutQueueItem.StartDate)
        Console.WriteLine("EndDate: {0}", billPayoutQueueItem.EndDate)
        Console.WriteLine("StartPaymentID: {0}", billPayoutQueueItem.StartPaymentID)
        Console.WriteLine("EndPaymentID: {0}", billPayoutQueueItem.EndPaymentID)
        Console.WriteLine("PaymentDate: {0}", billPayoutQueueItem.PaymentDate)
        Console.WriteLine("CurrencyCode: {0}", billPayoutQueueItem.CurrencyCode)
        Console.WriteLine("Reference: {0}", billPayoutQueueItem.Reference)
        Console.WriteLine("RequestByUserID: {0}", billPayoutQueueItem.RequestByUserID)
        Console.WriteLine("RequestDate: {0}", billPayoutQueueItem.RequestDate)
        Console.WriteLine("RequestCompleteDate: {0}", billPayoutQueueItem.RequestCompleteDate)
        Console.WriteLine("BatchDescription: {0}", billPayoutQueueItem.BatchDescription)
        Console.WriteLine("UseBatchPayout: {0}", billPayoutQueueItem.UseBatchPayout)
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

    $req->PayoutQueueRequestID = 1;
    $req->CurrencyCode = "usd";
    $req->PayableType = 1;
    $req->PaymentCardType = 1;
    $req->StartDate = 1;
    $req->EndDate = 1;

    //Send Request to Server and Get Response
    $res = $api.GetBillPayoutQueue($req);

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
    GetBillPayoutQueueRequest req = new GetBillPayoutQueueRequest();

    req.setPayoutQueueRequestID(1);
    req.setCurrencyCode("usd");
    req.setPayableType(1);
    req.setPaymentCardType(1);
    req.setStartDate(1);
    req.setEndDate(1);

    //Send Request to Server and Get Response
    GetBillPayoutQueueResponse res = api.getExigoApiSoap().getBillPayoutQueue(req, auth);

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

### VoidPayments

> Voids payments

| | |
|---|---|
| Category | Payout |
| REST | `POST /3.0/payment/void` |
| SOAP action | `https://api.exigo.com/VoidPayments` |
| WSDL elements | `voidPaymentsRequest` → `VoidPaymentsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=VoidPayments |

#### Input

**`VoidPaymentsRequest`**

| Property | Type | Notes |
|---|---|---|
| `PaymentIdStart` | `Int32` | Optional. If voiding payments by range, PaymentIdEnd must also be set. Defaults to 0. |
| `PaymentIdEnd` | `Int32` | Optional. If voiding payments by range, PaymentIdStart must also be set. Defaults to 0. |
| `PaymentIds` | `Int32[]` | Optional. If voiding payments by list, neither PaymentIdStart nor PaymentIdEnd must be set. |
| `Memo` | `String` | Optional. |

#### Output

**`VoidPaymentsResponse`**

_No properties._

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/payment/void HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "paymentIdStart": 1,
  "paymentIdEnd": 1,
  "memo": ""
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
SOAPAction: "https://api.exigo.com/VoidPayments"

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
    <voidPaymentsRequest xmlns="http://api.exigo.com/">
      <PaymentIdStart>int</PaymentIdStart>
      <PaymentIdEnd>int</PaymentIdEnd>
      <PaymentIds>
        <int>int</int>
      </PaymentIds>
      <Memo>string</Memo>
    </voidPaymentsRequest>
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
    <VoidPaymentsResult xmlns="http://api.exigo.com/" />
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
    var req = new VoidPaymentsRequest();

    req.PaymentIdStart = 1;         //If voiding payments by range, PaymentIdEnd must also be set.
    req.PaymentIdEnd = 1;           //If voiding payments by range, PaymentIdStart must also be set.
    req.Memo = "1";

    //Send Request to Server and Get Response
    var res = await api.VoidPaymentsAsync(req);

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
    VoidPaymentsRequest req = new VoidPaymentsRequest();

    req.PaymentIdStart = 1;         //If voiding payments by range, PaymentIdEnd must also be set.
    req.PaymentIdEnd = 1;           //If voiding payments by range, PaymentIdStart must also be set.
    req.Memo = "1";

    //Send Request to Server and Get Response
    VoidPaymentsResponse res = api.VoidPayments(req);

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
    Dim req as new VoidPaymentsRequest()

    req.PaymentIdStart = 1
    req.PaymentIdEnd = 1
    req.Memo = "1"

    'Send Request to Server and Get Response
    Dim res As VoidPaymentsResponse = api.VoidPayments(req)

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

    $req->PaymentIdStart = 1;
    $req->PaymentIdEnd = 1;
    $req->Memo = "1";

    //Send Request to Server and Get Response
    $res = $api.VoidPayments($req);

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
    VoidPaymentsRequest req = new VoidPaymentsRequest();

    req.setPaymentIdStart(1);
    req.setPaymentIdEnd(1);
    req.setMemo("1");

    //Send Request to Server and Get Response
    VoidPaymentsResponse res = api.getExigoApiSoap().voidPayments(req, auth);

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

### CreateBills

> Creates max 100 new bills

| | |
|---|---|
| Category | Payout |
| REST | `POST /3.0/bills` |
| SOAP action | `https://api.exigo.com/CreateBills` |
| WSDL elements | `CreateBillsRequest` → `CreateBillsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateBills |

#### Input

**`CreateBillsRequest`**

| Property | Type | Notes |
|---|---|---|
| `Bills` | `Bill[]` |  |

**`Bill`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| &nbsp;&nbsp;↳ `CurrencyCode` | `String` | The Bill's currency. |
| &nbsp;&nbsp;↳ `IsOtherIncome` | `Boolean` |  |
| &nbsp;&nbsp;↳ `DueDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `Amount` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Reference` | `String` | Optional. |
| &nbsp;&nbsp;↳ `Notes` | `String` | Optional. |
| &nbsp;&nbsp;↳ `BillStatusTypeID` | `Int32` | Optional. Bill Status (default is Unpaid). |
| &nbsp;&nbsp;↳ `PayableTypeIDOverride` | `Int32` | Optional. Optionally override the payable type of the bill. |
| &nbsp;&nbsp;↳ `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |
| &nbsp;&nbsp;↳ `TaxablePeriodTy` | `Int32` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `TaxablePeriodID` | `Int32` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `WarehouseID` | `Int32` | Optional. Unique location for orders.<br>**Lookup:** company-specific list (see company-lists.md) |

#### Output

**`CreateBillsResponse`**

| Property | Type | Notes |
|---|---|---|
| `Bills` | `BillResponse[]` |  |

**`BillResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `BillID` | `Int32` |  |
| &nbsp;&nbsp;↳ `Errors` | `String` |  |
| &nbsp;&nbsp;↳ `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| &nbsp;&nbsp;↳ `CurrencyCode` | `String` | The Bill's currency. |
| &nbsp;&nbsp;↳ `IsOtherIncome` | `Boolean` |  |
| &nbsp;&nbsp;↳ `DueDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `Amount` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Reference` | `String` |  |
| &nbsp;&nbsp;↳ `Notes` | `String` |  |
| &nbsp;&nbsp;↳ `BillStatusTypeID` | `Int32` | Bill Status (default is Unpaid). |
| &nbsp;&nbsp;↳ `PayableTypeIDOverride` | `Int32` | Optionally override the payable type of the bill. |
| &nbsp;&nbsp;↳ `CustomerKey` | `String` | Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |
| &nbsp;&nbsp;↳ `TaxablePeriodTy` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `TaxablePeriodID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `WarehouseID` | `Int32` | Unique location for orders.<br>**Lookup:** company-specific list (see company-lists.md) |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/bills HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "bills": null
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "bills": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateBills"

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
    <CreateBillsRequest xmlns="http://api.exigo.com/">
      <Bills>
        <Bill>
          <CustomerID>int</CustomerID>
          <CurrencyCode>string</CurrencyCode>
          <IsOtherIncome>boolean</IsOtherIncome>
          <DueDate>dateTime</DueDate>
          <Amount>decimal</Amount>
          <Reference>string</Reference>
          <Notes>string</Notes>
          <BillStatusTypeID>int</BillStatusTypeID>
          <PayableTypeIDOverride>int</PayableTypeIDOverride>
          <CustomerKey>string</CustomerKey>
          <TaxablePeriodTy>int</TaxablePeriodTy>
          <TaxablePeriodID>int</TaxablePeriodID>
          <WarehouseID>int</WarehouseID>
        </Bill>
      </Bills>
    </CreateBillsRequest>
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
    <CreateBillsResult xmlns="http://api.exigo.com/">
      <Bills>
        <BillResponse>
          <BillID>int</BillID>
          <Errors>
            <string>string</string>
          </Errors>
        </BillResponse>
      </Bills>
    </CreateBillsResult>
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
    var req = new CreateBillsRequest();

    //Add Bills
    var bills = new List<Bill>();

    var bill1 = new Bill();
    bill1.CustomerID = 1;
    bill1.CurrencyCode = "1";
    bill1.IsOtherIncome = true;
    bill1.DueDate = DateTime.Today;
    bill1.Amount = 1;
    bill1.Reference = "1";
    bill1.Notes = "1";
    bill1.BillStatusTypeID = 1;
    bill1.PayableTypeIDOverride = 1;
    bill1.CustomerKey = "1";
    bill1.TaxablePeriodTy = 1;
    bill1.TaxablePeriodID = 1;
    bill1.WarehouseID = 1;
    bills.Add(bill1);

    var bill2 = new Bill();
    bill2.CustomerID = 2;
    bill2.CurrencyCode = "2";
    bill2.IsOtherIncome = true;
    bill2.DueDate = DateTime.Today;
    bill2.Amount = 2;
    bill2.Reference = "2";
    bill2.Notes = "2";
    bill2.BillStatusTypeID = 2;
    bill2.PayableTypeIDOverride = 2;
    bill2.CustomerKey = "2";
    bill2.TaxablePeriodTy = 2;
    bill2.TaxablePeriodID = 2;
    bill2.WarehouseID = 2;
    bills.Add(bill2);

    //Now attach the list to the request
    req.Bills = bills.ToArray();

    //Send Request to Server and Get Response
    var res = await api.CreateBillsAsync(req);

    //Now examine the results:

    foreach (var bill  in res.Bills)
    {
        Console.WriteLine("BillID: {0}", bill.BillID);
        Console.WriteLine("Errors: {0}", bill.Errors);
        Console.WriteLine("CustomerID: {0}", bill.CustomerID);
        Console.WriteLine("CurrencyCode: {0}", bill.CurrencyCode);
        Console.WriteLine("IsOtherIncome: {0}", bill.IsOtherIncome);
        Console.WriteLine("DueDate: {0}", bill.DueDate);
        Console.WriteLine("Amount: {0}", bill.Amount);
        Console.WriteLine("Reference: {0}", bill.Reference);
        Console.WriteLine("Notes: {0}", bill.Notes);
        Console.WriteLine("BillStatusTypeID: {0}", bill.BillStatusTypeID);
        Console.WriteLine("PayableTypeIDOverride: {0}", bill.PayableTypeIDOverride);
        Console.WriteLine("CustomerKey: {0}", bill.CustomerKey);
        Console.WriteLine("TaxablePeriodTy: {0}", bill.TaxablePeriodTy);
        Console.WriteLine("TaxablePeriodID: {0}", bill.TaxablePeriodID);
        Console.WriteLine("WarehouseID: {0}", bill.WarehouseID);
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
    CreateBillsRequest req = new CreateBillsRequest();

    //Add Bills
    List<Bill> bills = new List<Bill>();

    Bill bill1 = new Bill();
    bill1.CustomerID = 1;
    bill1.CurrencyCode = "1";
    bill1.IsOtherIncome = true;
    bill1.DueDate = DateTime.Today;
    bill1.Amount = 1;
    bill1.Reference = "1";
    bill1.Notes = "1";
    bill1.BillStatusTypeID = 1;
    bill1.PayableTypeIDOverride = 1;
    bill1.CustomerKey = "1";
    bill1.TaxablePeriodTy = 1;
    bill1.TaxablePeriodID = 1;
    bill1.WarehouseID = 1;
    bills.Add(bill1);

    Bill bill2 = new Bill();
    bill2.CustomerID = 2;
    bill2.CurrencyCode = "2";
    bill2.IsOtherIncome = true;
    bill2.DueDate = DateTime.Today;
    bill2.Amount = 2;
    bill2.Reference = "2";
    bill2.Notes = "2";
    bill2.BillStatusTypeID = 2;
    bill2.PayableTypeIDOverride = 2;
    bill2.CustomerKey = "2";
    bill2.TaxablePeriodTy = 2;
    bill2.TaxablePeriodID = 2;
    bill2.WarehouseID = 2;
    bills.Add(bill2);

    //Now attach the list to the request
    req.Bills = bills.ToArray();

    //Send Request to Server and Get Response
    CreateBillsResponse res = api.CreateBills(req);

    //Now examine the results:

    foreach (BillResponse bill  in res.Bills)
    {
        Console.WriteLine("BillID: {0}", bill.BillID);
        Console.WriteLine("Errors: {0}", bill.Errors);
        Console.WriteLine("CustomerID: {0}", bill.CustomerID);
        Console.WriteLine("CurrencyCode: {0}", bill.CurrencyCode);
        Console.WriteLine("IsOtherIncome: {0}", bill.IsOtherIncome);
        Console.WriteLine("DueDate: {0}", bill.DueDate);
        Console.WriteLine("Amount: {0}", bill.Amount);
        Console.WriteLine("Reference: {0}", bill.Reference);
        Console.WriteLine("Notes: {0}", bill.Notes);
        Console.WriteLine("BillStatusTypeID: {0}", bill.BillStatusTypeID);
        Console.WriteLine("PayableTypeIDOverride: {0}", bill.PayableTypeIDOverride);
        Console.WriteLine("CustomerKey: {0}", bill.CustomerKey);
        Console.WriteLine("TaxablePeriodTy: {0}", bill.TaxablePeriodTy);
        Console.WriteLine("TaxablePeriodID: {0}", bill.TaxablePeriodID);
        Console.WriteLine("WarehouseID: {0}", bill.WarehouseID);
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
    Dim req as new CreateBillsRequest()

    'Add Bills
    Dim bills As New List(Of Bill)()

    Dim bill1 as new Bill()
    bill1.CustomerID = 1
    bill1.CurrencyCode = "1"
    bill1.IsOtherIncome = true
    bill1.DueDate = DateTime.Today
    bill1.Amount = 1
    bill1.Reference = "1"
    bill1.Notes = "1"
    bill1.BillStatusTypeID = 1
    bill1.PayableTypeIDOverride = 1
    bill1.CustomerKey = "1"
    bill1.TaxablePeriodTy = 1
    bill1.TaxablePeriodID = 1
    bill1.WarehouseID = 1
    bills.Add(bill1)

    Dim bill2 as new Bill()
    bill2.CustomerID = 2
    bill2.CurrencyCode = "2"
    bill2.IsOtherIncome = true
    bill2.DueDate = DateTime.Today
    bill2.Amount = 2
    bill2.Reference = "2"
    bill2.Notes = "2"
    bill2.BillStatusTypeID = 2
    bill2.PayableTypeIDOverride = 2
    bill2.CustomerKey = "2"
    bill2.TaxablePeriodTy = 2
    bill2.TaxablePeriodID = 2
    bill2.WarehouseID = 2
    bills.Add(bill2)

    'Now attach the list to the request
    req.Bills = bills.ToArray()

    'Send Request to Server and Get Response
    Dim res As CreateBillsResponse = api.CreateBills(req)

    'Now examine the results:

    For Each bill As BillResponse In res.Bills
        Console.WriteLine("BillID: {0}", bill.BillID)
        Console.WriteLine("Errors: {0}", bill.Errors)
        Console.WriteLine("CustomerID: {0}", bill.CustomerID)
        Console.WriteLine("CurrencyCode: {0}", bill.CurrencyCode)
        Console.WriteLine("IsOtherIncome: {0}", bill.IsOtherIncome)
        Console.WriteLine("DueDate: {0}", bill.DueDate)
        Console.WriteLine("Amount: {0}", bill.Amount)
        Console.WriteLine("Reference: {0}", bill.Reference)
        Console.WriteLine("Notes: {0}", bill.Notes)
        Console.WriteLine("BillStatusTypeID: {0}", bill.BillStatusTypeID)
        Console.WriteLine("PayableTypeIDOverride: {0}", bill.PayableTypeIDOverride)
        Console.WriteLine("CustomerKey: {0}", bill.CustomerKey)
        Console.WriteLine("TaxablePeriodTy: {0}", bill.TaxablePeriodTy)
        Console.WriteLine("TaxablePeriodID: {0}", bill.TaxablePeriodID)
        Console.WriteLine("WarehouseID: {0}", bill.WarehouseID)
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

    //Add Bills

    $bill1->CustomerID = 1;
    $bill1->CurrencyCode = "1";
    $bill1->IsOtherIncome = 1;
    $bill1->DueDate = 1;
    $bill1->Amount = 1;
    $bill1->Reference = "1";
    $bill1->Notes = "1";
    $bill1->BillStatusTypeID = 1;
    $bill1->PayableTypeIDOverride = 1;
    $bill1->CustomerKey = "1";
    $bill1->TaxablePeriodTy = 1;
    $bill1->TaxablePeriodID = 1;
    $bill1->WarehouseID = 1;

    $bill2->CustomerID = 2;
    $bill2->CurrencyCode = "2";
    $bill2->IsOtherIncome = 2;
    $bill2->DueDate = 2;
    $bill2->Amount = 2;
    $bill2->Reference = "2";
    $bill2->Notes = "2";
    $bill2->BillStatusTypeID = 2;
    $bill2->PayableTypeIDOverride = 2;
    $bill2->CustomerKey = "2";
    $bill2->TaxablePeriodTy = 2;
    $bill2->TaxablePeriodID = 2;
    $bill2->WarehouseID = 2;

    //Now attach the list to the request
    req.Bills = array(bill1,bill2);

    //Send Request to Server and Get Response
    $res = $api.CreateBills($req);

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
    CreateBillsRequest req = new CreateBillsRequest();

    //Add Bills
    ArrayOfBill bills = new ArrayOfBill();

    Bill bill1 = new Bill();
    bill1.setCustomerID(1);
    bill1.setCurrencyCode("1");
    bill1.setIsOtherIncome(1);
    bill1.setDueDate(1);
    bill1.setAmount(1);
    bill1.setReference("1");
    bill1.setNotes("1");
    bill1.setBillStatusTypeID(1);
    bill1.setPayableTypeIDOverride(1);
    bill1.setCustomerKey("1");
    bill1.setTaxablePeriodTy(1);
    bill1.setTaxablePeriodID(1);
    bill1.setWarehouseID(1);
    bills.Add(bill1);

    Bill bill2 = new Bill();
    bill2.setCustomerID(2);
    bill2.setCurrencyCode("2");
    bill2.setIsOtherIncome(2);
    bill2.setDueDate(2);
    bill2.setAmount(2);
    bill2.setReference("2");
    bill2.setNotes("2");
    bill2.setBillStatusTypeID(2);
    bill2.setPayableTypeIDOverride(2);
    bill2.setCustomerKey("2");
    bill2.setTaxablePeriodTy(2);
    bill2.setTaxablePeriodID(2);
    bill2.setWarehouseID(2);
    bills.Add(bill2);

    //Now attach the list to the request
    req.setBills(bills);

    //Send Request to Server and Get Response
    CreateBillsResponse res = api.getExigoApiSoap().createBills(req, auth);

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
