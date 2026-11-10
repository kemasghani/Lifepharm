# Exigo API — Recurring Orders

API version v2025.11.7.6. Crawled 2026-11-11 from https://api.exigo.com/3.0/. Back to [index](../README.md).

| Operation | REST | Summary |
|---|---|---|
| [CreateAutoOrder](#createautoorder) | `POST /3.0/autoorder` | Create a new Recurring Order template for an existing customer or a new customer as part of a transaction. Client provides schedule, item codes, quantity, and shipping info.… |
| [UpdateAutoOrder](#updateautoorder) | `PUT /3.0/autoorder` | Update a Recurring Order template in or out of a transaction. Client provides schedule, item codes, quantity, and shipping info. Server calculates and commits data, then pricing,… |
| [UpdateAutoOrderDetail](#updateautoorderdetail) | `PUT /3.0/autoorder/detail` | Update a Recurring Order template detail in or out of a transaction. Client provides quantity, pricing , volume and extended detail info. Note: This request can participate in a… |
| [ChangeAutoOrderStatus](#changeautoorderstatus) | `POST /3.0/autoorder/status` | Changes the status of an AutoOrder. This is typically used to delete or suspend an auto order. |
| [GetAutoOrders](#getautoorders) | `GET /3.0/autoorder?customerID=1` | Returns any AutoOrders setup and active for a given customer. |
| [AutoOrderSkipNextShipment](#autoorderskipnextshipment) | `POST /3.0/autoorder/skip` | Disables the auotorder next scheduled date |

---
### CreateAutoOrder

>  Create a new Recurring Order template for an existing customer or a new customer as part of a transaction.
>  Client provides schedule, item codes, quantity, and shipping info. Server calculates and commits data,
>  then pricing, tax, shipping and volume info. You can also update/overwrite an existing autoorder
>  by using the OverwriteExistingAutoOrder and ExistingAutoOrderID properties.

| | |
|---|---|
| Category | Recurring Orders |
| REST | `POST /3.0/autoorder` |
| SOAP action | `https://api.exigo.com/CreateAutoOrder` |
| WSDL elements | `CreateAutoOrderRequest` → `CreateAutoOrderResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateAutoOrder |

#### Input

**`CreateAutoOrderRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `Frequency` | `FrequencyType` | **Values:** `Weekly`, `BiWeekly`, `Monthly`, `Quarterly`, `SemiYearly`, `Yearly`, `BiMonthly`, `EveryFourWeeks`, `EverySixWeeks`, `EveryEightWeeks`, `EveryTwelveWeeks`, `SpecificDays`, `Custom` |
| `StartDate` | `DateTime` |  |
| `StopDate` | `DateTime` | Optional. Leave null if there is no stop date. |
| `SpecificDayInterval` | `Int32` | Optional. To be used with Frequency Type SpecificDays. |
| `CurrencyCode` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `WarehouseID` | `Int32` | Unique location for orders.<br>**Lookup:** company-specific list (see company-lists.md) |
| `ShipMethodID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| `PriceType` | `Int32` | Controls which price band to use.<br>**Lookup:** company-specific list (see company-lists.md) |
| `PaymentType` | `AutoOrderPaymentType` | Payment type.<br>**Values:** `PrimaryCreditCard`, `SecondaryCreditCard`, `CheckingAccount`, `WillSendPayment`, `BankDraft`, `PrimaryWalletAccount`, `SecondaryWalletAccount`, `ThirdWalletAccount`, `FourthWalletAccount`, `FifthWalletAccount` |
| `ProcessType` | `AutoOrderProcessType` | Optional.<br>**Values:** `AlwaysProcess`, `Conditional` |
| `FirstName` | `String` | Optional. |
| `MiddleName` | `String` | Optional. |
| `LastName` | `String` | Optional. |
| `NameSuffix` | `String` | Optional. |
| `Company` | `String` | Optional. |
| `Address1` | `String` | Optional. |
| `Address2` | `String` | Optional. |
| `Address3` | `String` | Optional. |
| `City` | `String` | Optional. |
| `State` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Zip` | `String` | Optional. |
| `Country` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `County` | `String` | Optional. |
| `Email` | `String` | Optional. |
| `Phone` | `String` | Optional. |
| `Notes` | `String` | Optional. |
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
| `Description` | `String` | Optional. Description for this auto order. |
| `OverwriteExistingAutoOrder` | `Boolean` |  |
| `ExistingAutoOrderID` | `Int32` |  |
| `Details` | `OrderDetailRequest[]` |  |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |
| `CustomFrequencyTy` | `Int32` | Optional. To be used with Frequency Type Custom. |

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

**`CreateAutoOrderResponse`**

| Property | Type | Notes |
|---|---|---|
| `AutoOrderID` | `Int32` |  |
| `Description` | `String` |  |
| `Total` | `Decimal` |  |
| `SubTotal` | `Decimal` |  |
| `TaxTotal` | `Decimal` |  |
| `ShippingTotal` | `Decimal` |  |
| `DiscountTotal` | `Decimal` |  |
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
| `ShippingTax` | `Decimal` |  |
| `OrderTax` | `Decimal` |  |
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

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/autoorder HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "frequency": null,
  "startDate": "2026-11-10T00:00:00-06:00",
  "stopDate": "2026-11-10T00:00:00-06:00",
  "specificDayInterval": 1,
  "currencyCode": "usd",
  "warehouseID": 1,
  "shipMethodID": 1,
  "priceType": 1,
  "paymentType": null,
  "processType": null,
  "firstName": "",
  "lastName": "",
  "company": "",
  "address1": "",
  "address2": "",
  "address3": "",
  "city": "",
  "zip": "",
  "county": "",
  "email": "",
  "phone": "",
  "notes": "",
  "overwriteExistingAutoOrder": true,
  "existingAutoOrderID": 1,
  "details": null,
  "customerKey": "1",
  "customFrequencyTy": 1
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "autoOrderID": 1,
  "description": "",
  "total": null,
  "subTotal": null,
  "taxTotal": null,
  "shippingTotal": null,
  "discountTotal": null,
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
  "shippingTax": null,
  "orderTax": null,
  "details": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateAutoOrder"

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
    <CreateAutoOrderRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <Frequency>Weekly or BiWeekly or Monthly or BiMonthly or Quarterly or SemiYearly or Yearly or EveryFourWeeks or EverySixWeeks or EveryEightWeeks or EveryTwelveWeeks or SpecificDays or Custom</Frequency>
      <StartDate>dateTime</StartDate>
      <StopDate>dateTime</StopDate>
      <SpecificDayInterval>int</SpecificDayInterval>
      <CurrencyCode>string</CurrencyCode>
      <WarehouseID>int</WarehouseID>
      <ShipMethodID>int</ShipMethodID>
      <PriceType>int</PriceType>
      <PaymentType>PrimaryCreditCard or SecondaryCreditCard or CheckingAccount or WillSendPayment or BankDraft or PrimaryWalletAccount or SecondaryWalletAccount or ThirdWalletAccount or FourthWalletAccount or FifthWalletAccount</PaymentType>
      <ProcessType>AlwaysProcess or Conditional</ProcessType>
      <FirstName>string</FirstName>
      <MiddleName>string</MiddleName>
      <LastName>string</LastName>
      <NameSuffix>string</NameSuffix>
      <Company>string</Company>
      <Address1>string</Address1>
      <Address2>string</Address2>
      <Address3>string</Address3>
      <City>string</City>
      <State>string</State>
      <Zip>string</Zip>
      <Country>string</Country>
      <County>string</County>
      <Email>string</Email>
      <Phone>string</Phone>
      <Notes>string</Notes>
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
      <Description>string</Description>
      <OverwriteExistingAutoOrder>boolean</OverwriteExistingAutoOrder>
      <ExistingAutoOrderID>int</ExistingAutoOrderID>
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
      <CustomerKey>string</CustomerKey>
      <CustomFrequencyTy>int</CustomFrequencyTy>
    </CreateAutoOrderRequest>
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
    <CreateAutoOrderResult xmlns="http://api.exigo.com/">
      <AutoOrderID>int</AutoOrderID>
      <Description>string</Description>
      <Total>decimal</Total>
      <SubTotal>decimal</SubTotal>
      <TaxTotal>decimal</TaxTotal>
      <ShippingTotal>decimal</ShippingTotal>
      <DiscountTotal>decimal</DiscountTotal>
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
      <ShippingTax>decimal</ShippingTax>
      <OrderTax>decimal</OrderTax>
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
    </CreateAutoOrderResult>
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
    var req = new CreateAutoOrderRequest();

    req.Frequency = FrequencyType.Weekly;
    req.StartDate = DateTime.Today;
    req.StopDate = DateTime.Today;               //Leave null if there is no stop date.
    req.SpecificDayInterval = 1;    //To be used with Frequency Type  SpecificDays
    req.CurrencyCode = "usd";
    req.WarehouseID = 1;            //Unique location for orders
    req.ShipMethodID = 1;
    req.PriceType = 1;              //Controls which price band to use
    req.PaymentType = AutoOrderPaymentType.PrimaryCreditCard;            //Payment type.
    req.ProcessType = AutoOrderProcessType.AlwaysProcess;
    req.FirstName = "1";
    req.LastName = "1";
    req.Company = "1";
    req.Address1 = "1";
    req.Address2 = "1";
    req.Address3 = "1";
    req.City = "1";
    req.Zip = "1";
    req.County = "1";
    req.Email = "1";
    req.Phone = "1";
    req.Notes = "1";
    req.OverwriteExistingAutoOrder = true;
    req.ExistingAutoOrderID = 1;

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
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.CustomFrequencyTy = 1;      //To be used with Frequency Type  Custom

    //Send Request to Server and Get Response
    var res = await api.CreateAutoOrderAsync(req);

    //Now examine the results:
    Console.WriteLine("AutoOrderID: {0}", res.AutoOrderID);
    Console.WriteLine("Description: {0}", res.Description);
    Console.WriteLine("Total: {0}", res.Total);
    Console.WriteLine("SubTotal: {0}", res.SubTotal);
    Console.WriteLine("TaxTotal: {0}", res.TaxTotal);
    Console.WriteLine("ShippingTotal: {0}", res.ShippingTotal);
    Console.WriteLine("DiscountTotal: {0}", res.DiscountTotal);
    Console.WriteLine("WeightTotal: {0}", res.WeightTotal);
    Console.WriteLine("BusinessVolumeTotal: {0}", res.BusinessVolumeTotal);
    Console.WriteLine("CommissionableVolumeTotal: {0}", res.CommissionableVolumeTotal);
    Console.WriteLine("ShippingTax: {0}", res.ShippingTax);
    Console.WriteLine("OrderTax: {0}", res.OrderTax);

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
    CreateAutoOrderRequest req = new CreateAutoOrderRequest();

    req.Frequency = FrequencyType.Weekly;
    req.StartDate = DateTime.Today;
    req.StopDate = DateTime.Today;               //Leave null if there is no stop date.
    req.SpecificDayInterval = 1;    //To be used with Frequency Type  SpecificDays
    req.CurrencyCode = "usd";
    req.WarehouseID = 1;            //Unique location for orders
    req.ShipMethodID = 1;
    req.PriceType = 1;              //Controls which price band to use
    req.PaymentType = AutoOrderPaymentType.PrimaryCreditCard;            //Payment type.
    req.ProcessType = AutoOrderProcessType.AlwaysProcess;
    req.FirstName = "1";
    req.LastName = "1";
    req.Company = "1";
    req.Address1 = "1";
    req.Address2 = "1";
    req.Address3 = "1";
    req.City = "1";
    req.Zip = "1";
    req.County = "1";
    req.Email = "1";
    req.Phone = "1";
    req.Notes = "1";
    req.OverwriteExistingAutoOrder = true;
    req.ExistingAutoOrderID = 1;

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
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.CustomFrequencyTy = 1;      //To be used with Frequency Type  Custom

    //Send Request to Server and Get Response
    CreateAutoOrderResponse res = api.CreateAutoOrder(req);

    //Now examine the results:
    Console.WriteLine("AutoOrderID: {0}", res.AutoOrderID);
    Console.WriteLine("Description: {0}", res.Description);
    Console.WriteLine("Total: {0}", res.Total);
    Console.WriteLine("SubTotal: {0}", res.SubTotal);
    Console.WriteLine("TaxTotal: {0}", res.TaxTotal);
    Console.WriteLine("ShippingTotal: {0}", res.ShippingTotal);
    Console.WriteLine("DiscountTotal: {0}", res.DiscountTotal);
    Console.WriteLine("WeightTotal: {0}", res.WeightTotal);
    Console.WriteLine("BusinessVolumeTotal: {0}", res.BusinessVolumeTotal);
    Console.WriteLine("CommissionableVolumeTotal: {0}", res.CommissionableVolumeTotal);
    Console.WriteLine("ShippingTax: {0}", res.ShippingTax);
    Console.WriteLine("OrderTax: {0}", res.OrderTax);

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
    Dim req as new CreateAutoOrderRequest()

    req.Frequency = FrequencyType.Weekly
    req.StartDate = DateTime.Today
    req.StopDate = DateTime.Today
    req.SpecificDayInterval = 1
    req.CurrencyCode = "usd"
    req.WarehouseID = 1
    req.ShipMethodID = 1
    req.PriceType = 1
    req.PaymentType = AutoOrderPaymentType.PrimaryCreditCard
    req.ProcessType = AutoOrderProcessType.AlwaysProcess
    req.FirstName = "1"
    req.LastName = "1"
    req.Company = "1"
    req.Address1 = "1"
    req.Address2 = "1"
    req.Address3 = "1"
    req.City = "1"
    req.Zip = "1"
    req.County = "1"
    req.Email = "1"
    req.Phone = "1"
    req.Notes = "1"
    req.OverwriteExistingAutoOrder = true
    req.ExistingAutoOrderID = 1

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
    req.CustomerKey = "1"
    req.CustomFrequencyTy = 1

    'Send Request to Server and Get Response
    Dim res As CreateAutoOrderResponse = api.CreateAutoOrder(req)

    'Now examine the results:
    Console.WriteLine("AutoOrderID: {0}", res.AutoOrderID)
    Console.WriteLine("Description: {0}", res.Description)
    Console.WriteLine("Total: {0}", res.Total)
    Console.WriteLine("SubTotal: {0}", res.SubTotal)
    Console.WriteLine("TaxTotal: {0}", res.TaxTotal)
    Console.WriteLine("ShippingTotal: {0}", res.ShippingTotal)
    Console.WriteLine("DiscountTotal: {0}", res.DiscountTotal)
    Console.WriteLine("WeightTotal: {0}", res.WeightTotal)
    Console.WriteLine("BusinessVolumeTotal: {0}", res.BusinessVolumeTotal)
    Console.WriteLine("CommissionableVolumeTotal: {0}", res.CommissionableVolumeTotal)
    Console.WriteLine("ShippingTax: {0}", res.ShippingTax)
    Console.WriteLine("OrderTax: {0}", res.OrderTax)

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

    $req->Frequency = 1;
    $req->StartDate = 1;
    $req->StopDate = 1;
    $req->SpecificDayInterval = 1;
    $req->CurrencyCode = "usd";
    $req->WarehouseID = 1;
    $req->ShipMethodID = 1;
    $req->PriceType = 1;
    $req->PaymentType = 1;
    $req->ProcessType = 1;
    $req->FirstName = "1";
    $req->LastName = "1";
    $req->Company = "1";
    $req->Address1 = "1";
    $req->Address2 = "1";
    $req->Address3 = "1";
    $req->City = "1";
    $req->Zip = "1";
    $req->County = "1";
    $req->Email = "1";
    $req->Phone = "1";
    $req->Notes = "1";
    $req->OverwriteExistingAutoOrder = 1;
    $req->ExistingAutoOrderID = 1;

    //Add Details

    $detail1->ItemCode = "1";
    $detail1->Quantity = 1;

    $detail2->ItemCode = "2";
    $detail2->Quantity = 2;

    //Now attach the list to the request
    req.Details = array(detail1,detail2);
    $req->CustomerKey = "1";
    $req->CustomFrequencyTy = 1;

    //Send Request to Server and Get Response
    $res = $api.CreateAutoOrder($req);

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
    CreateAutoOrderRequest req = new CreateAutoOrderRequest();

    req.setFrequency(1);
    req.setStartDate(1);
    req.setStopDate(1);
    req.setSpecificDayInterval(1);
    req.setCurrencyCode("usd");
    req.setWarehouseID(1);
    req.setShipMethodID(1);
    req.setPriceType(1);
    req.setPaymentType(1);
    req.setProcessType(1);
    req.setFirstName("1");
    req.setLastName("1");
    req.setCompany("1");
    req.setAddress1("1");
    req.setAddress2("1");
    req.setAddress3("1");
    req.setCity("1");
    req.setZip("1");
    req.setCounty("1");
    req.setEmail("1");
    req.setPhone("1");
    req.setNotes("1");
    req.setOverwriteExistingAutoOrder(1);
    req.setExistingAutoOrderID(1);

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
    req.setCustomerKey("1");
    req.setCustomFrequencyTy(1);

    //Send Request to Server and Get Response
    CreateAutoOrderResponse res = api.getExigoApiSoap().createAutoOrder(req, auth);

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

### UpdateAutoOrder

>  Update a Recurring Order template in or out of a transaction.
>  Client provides schedule, item codes, quantity, and shipping info. Server calculates and commits data,
>  then pricing, tax, shipping and volume info.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Recurring Orders |
| REST | `PUT /3.0/autoorder` |
| SOAP action | `https://api.exigo.com/UpdateAutoOrder` |
| WSDL elements | `UpdateAutoOrderRequest` → `UpdateAutoOrderResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateAutoOrder |

#### Input

**`UpdateAutoOrderRequest`**

| Property | Type | Notes |
|---|---|---|
| `AutoOrderID` | `Int32` |  |
| `Frequency` | `FrequencyType` | Optional. Leave null to ignore. If set to SpecificDays, SpecificDayInterval must be filled.<br>**Values:** `Weekly`, `BiWeekly`, `Monthly`, `Quarterly`, `SemiYearly`, `Yearly`, `BiMonthly`, `EveryFourWeeks`, `EverySixWeeks`, `EveryEightWeeks`, `EveryTwelveWeeks`, `SpecificDays`, `Custom` |
| `StartDate` | `DateTime` | Optional. Leave null to ignore. |
| `StopDate` | `DateTime` | Optional. Leave null to ignore. Pass in DateTime minimum to set field empty. |
| `SpecificDayInterval` | `Int32` | Optional. Leave null to ignore. To fill, Frequency must be filled with SpecificDays, even if previously set to SpecificDays. |
| `CurrencyCode` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `WarehouseID` | `Int32` | Optional. Leave null to ignore. |
| `ShipMethodID` | `Int32` | Optional. Leave null to ignore. |
| `PaymentType` | `AutoOrderPaymentType` | Optional. Leave null to ignore.<br>**Values:** `PrimaryCreditCard`, `SecondaryCreditCard`, `CheckingAccount`, `WillSendPayment`, `BankDraft`, `PrimaryWalletAccount`, `SecondaryWalletAccount`, `ThirdWalletAccount`, `FourthWalletAccount`, `FifthWalletAccount` |
| `ProcessType` | `AutoOrderProcessType` | Optional. Leave null to ignore.<br>**Values:** `AlwaysProcess`, `Conditional` |
| `FirstName` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `MiddleName` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `LastName` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `NameSuffix` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `Company` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `Address1` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `Address2` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `Address3` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `City` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `State` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `Zip` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `Country` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `County` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `Email` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `Phone` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `Notes` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `Other11` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `Other12` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `Other13` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `Other14` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `Other15` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `Other16` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `Other17` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `Other18` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `Other19` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `Other20` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `Description` | `String` | Optional. Leave null to ignore, fill with empty string to set field empty. |
| `CustomFrequencyTy` | `Int32` | Optional. To be used with Frequency Type Custom. |

#### Output

**`UpdateAutoOrderResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/autoorder HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customFrequencyTy": 1
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
SOAPAction: "https://api.exigo.com/UpdateAutoOrder"

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
    <UpdateAutoOrderRequest xmlns="http://api.exigo.com/">
      <AutoOrderID>int</AutoOrderID>
      <Frequency>Weekly or BiWeekly or Monthly or BiMonthly or Quarterly or SemiYearly or Yearly or EveryFourWeeks or EverySixWeeks or EveryEightWeeks or EveryTwelveWeeks or SpecificDays or Custom</Frequency>
      <StartDate>dateTime</StartDate>
      <StopDate>dateTime</StopDate>
      <SpecificDayInterval>int</SpecificDayInterval>
      <CurrencyCode>string</CurrencyCode>
      <WarehouseID>int</WarehouseID>
      <ShipMethodID>int</ShipMethodID>
      <PaymentType>PrimaryCreditCard or SecondaryCreditCard or CheckingAccount or WillSendPayment or BankDraft or PrimaryWalletAccount or SecondaryWalletAccount or ThirdWalletAccount or FourthWalletAccount or FifthWalletAccount</PaymentType>
      <ProcessType>AlwaysProcess or Conditional</ProcessType>
      <FirstName>string</FirstName>
      <MiddleName>string</MiddleName>
      <LastName>string</LastName>
      <NameSuffix>string</NameSuffix>
      <Company>string</Company>
      <Address1>string</Address1>
      <Address2>string</Address2>
      <Address3>string</Address3>
      <City>string</City>
      <State>string</State>
      <Zip>string</Zip>
      <Country>string</Country>
      <County>string</County>
      <Email>string</Email>
      <Phone>string</Phone>
      <Notes>string</Notes>
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
      <Description>string</Description>
      <CustomFrequencyTy>int</CustomFrequencyTy>
    </UpdateAutoOrderRequest>
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
    <UpdateAutoOrderResult xmlns="http://api.exigo.com/" />
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
    var req = new UpdateAutoOrderRequest();

    req.CustomFrequencyTy = 1;      //To be used with Frequency Type  Custom

    //Send Request to Server and Get Response
    var res = await api.UpdateAutoOrderAsync(req);

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
    UpdateAutoOrderRequest req = new UpdateAutoOrderRequest();

    req.CustomFrequencyTy = 1;      //To be used with Frequency Type  Custom

    //Send Request to Server and Get Response
    UpdateAutoOrderResponse res = api.UpdateAutoOrder(req);

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
    Dim req as new UpdateAutoOrderRequest()

    req.CustomFrequencyTy = 1

    'Send Request to Server and Get Response
    Dim res As UpdateAutoOrderResponse = api.UpdateAutoOrder(req)

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

    $req->CustomFrequencyTy = 1;

    //Send Request to Server and Get Response
    $res = $api.UpdateAutoOrder($req);

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
    UpdateAutoOrderRequest req = new UpdateAutoOrderRequest();

    req.setCustomFrequencyTy(1);

    //Send Request to Server and Get Response
    UpdateAutoOrderResponse res = api.getExigoApiSoap().updateAutoOrder(req, auth);

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

### UpdateAutoOrderDetail

>  Update a Recurring Order template detail in or out of a transaction.
>  Client provides quantity, pricing , volume and extended detail info.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Recurring Orders |
| REST | `PUT /3.0/autoorder/detail` |
| SOAP action | `https://api.exigo.com/UpdateAutoOrderDetail` |
| WSDL elements | `UpdateAutoOrderDetailRequest` → `UpdateAutoOrderDetailResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateAutoOrderDetail |

#### Input

**`UpdateAutoOrderDetailRequest`**

| Property | Type | Notes |
|---|---|---|
| `AutoOrderID` | `Int32` |  |
| `OrderLine` | `Int32` |  |
| `ItemID` | `Int32` | Unique identifier for a item record. |
| `Qty` | `Decimal` |  |
| `ManualPriceEach` | `Decimal` | Optional. |
| `ManualTaxablePriceEach` | `Decimal` | Optional. |
| `ManualShippingPriceEach` | `Decimal` | Optional. |
| `ManualBVEach` | `Decimal` | Optional. |
| `ManualCVEach` | `Decimal` | Optional. |
| `Description` | `String` | Optional. |
| `PeriodDescriptionTy` | `Int32` | Optional. |
| `PriceEach` | `Decimal` | Optional. |
| `PriceExt` | `Decimal` | Optional. |
| `BVEach` | `Decimal` | Optional. |
| `BusinessVolume` | `Decimal` | Optional. Price amount. |
| `CVEach` | `Decimal` | Optional. |
| `CommissionableVolume` | `Decimal` | Optional. Price amount. |
| `DynamicKitItemID` | `Int32` | Optional. |
| `Reference1` | `String` | Optional. |

#### Output

**`UpdateAutoOrderDetailResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/autoorder/detail HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "autoOrderID": 1,
  "orderLine": 1,
  "itemID": 1,
  "qty": null,
  "manualPriceEach": null,
  "manualTaxablePriceEach": null,
  "manualShippingPriceEach": null,
  "manualBVEach": null,
  "manualCVEach": null,
  "description": "",
  "periodDescriptionTy": 1,
  "priceEach": null,
  "priceExt": null,
  "bVEach": null,
  "businessVolume": null,
  "cVEach": null,
  "commissionableVolume": null,
  "dynamicKitItemID": 1,
  "reference1": ""
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
SOAPAction: "https://api.exigo.com/UpdateAutoOrderDetail"

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
    <UpdateAutoOrderDetailRequest xmlns="http://api.exigo.com/">
      <AutoOrderID>int</AutoOrderID>
      <OrderLine>int</OrderLine>
      <ItemID>int</ItemID>
      <Qty>decimal</Qty>
      <ManualPriceEach>decimal</ManualPriceEach>
      <ManualTaxablePriceEach>decimal</ManualTaxablePriceEach>
      <ManualShippingPriceEach>decimal</ManualShippingPriceEach>
      <ManualBVEach>decimal</ManualBVEach>
      <ManualCVEach>decimal</ManualCVEach>
      <Description>string</Description>
      <PeriodDescriptionTy>int</PeriodDescriptionTy>
      <PriceEach>decimal</PriceEach>
      <PriceExt>decimal</PriceExt>
      <BVEach>decimal</BVEach>
      <BusinessVolume>decimal</BusinessVolume>
      <CVEach>decimal</CVEach>
      <CommissionableVolume>decimal</CommissionableVolume>
      <DynamicKitItemID>int</DynamicKitItemID>
      <Reference1>string</Reference1>
    </UpdateAutoOrderDetailRequest>
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
    <UpdateAutoOrderDetailResult xmlns="http://api.exigo.com/" />
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
    var req = new UpdateAutoOrderDetailRequest();

    req.AutoOrderID = 1;
    req.OrderLine = 1;
    req.ItemID = 1;                 //Unique identifier for a item record.
    req.Qty = 1;
    req.ManualPriceEach = 1;
    req.ManualTaxablePriceEach = 1;
    req.ManualShippingPriceEach = 1;
    req.ManualBVEach = 1;
    req.ManualCVEach = 1;
    req.Description = "1";
    req.PeriodDescriptionTy = 1;
    req.PriceEach = 1;
    req.PriceExt = 1;
    req.BVEach = 1;
    req.BusinessVolume = 1;         //Price amount
    req.CVEach = 1;
    req.CommissionableVolume = 1;   //Price amount
    req.DynamicKitItemID = 1;
    req.Reference1 = "1";

    //Send Request to Server and Get Response
    var res = await api.UpdateAutoOrderDetailAsync(req);

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
    UpdateAutoOrderDetailRequest req = new UpdateAutoOrderDetailRequest();

    req.AutoOrderID = 1;
    req.OrderLine = 1;
    req.ItemID = 1;                 //Unique identifier for a item record.
    req.Qty = 1;
    req.ManualPriceEach = 1;
    req.ManualTaxablePriceEach = 1;
    req.ManualShippingPriceEach = 1;
    req.ManualBVEach = 1;
    req.ManualCVEach = 1;
    req.Description = "1";
    req.PeriodDescriptionTy = 1;
    req.PriceEach = 1;
    req.PriceExt = 1;
    req.BVEach = 1;
    req.BusinessVolume = 1;         //Price amount
    req.CVEach = 1;
    req.CommissionableVolume = 1;   //Price amount
    req.DynamicKitItemID = 1;
    req.Reference1 = "1";

    //Send Request to Server and Get Response
    UpdateAutoOrderDetailResponse res = api.UpdateAutoOrderDetail(req);

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
    Dim req as new UpdateAutoOrderDetailRequest()

    req.AutoOrderID = 1
    req.OrderLine = 1
    req.ItemID = 1
    req.Qty = 1
    req.ManualPriceEach = 1
    req.ManualTaxablePriceEach = 1
    req.ManualShippingPriceEach = 1
    req.ManualBVEach = 1
    req.ManualCVEach = 1
    req.Description = "1"
    req.PeriodDescriptionTy = 1
    req.PriceEach = 1
    req.PriceExt = 1
    req.BVEach = 1
    req.BusinessVolume = 1
    req.CVEach = 1
    req.CommissionableVolume = 1
    req.DynamicKitItemID = 1
    req.Reference1 = "1"

    'Send Request to Server and Get Response
    Dim res As UpdateAutoOrderDetailResponse = api.UpdateAutoOrderDetail(req)

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

    $req->AutoOrderID = 1;
    $req->OrderLine = 1;
    $req->ItemID = 1;
    $req->Qty = 1;
    $req->ManualPriceEach = 1;
    $req->ManualTaxablePriceEach = 1;
    $req->ManualShippingPriceEach = 1;
    $req->ManualBVEach = 1;
    $req->ManualCVEach = 1;
    $req->Description = "1";
    $req->PeriodDescriptionTy = 1;
    $req->PriceEach = 1;
    $req->PriceExt = 1;
    $req->BVEach = 1;
    $req->BusinessVolume = 1;
    $req->CVEach = 1;
    $req->CommissionableVolume = 1;
    $req->DynamicKitItemID = 1;
    $req->Reference1 = "1";

    //Send Request to Server and Get Response
    $res = $api.UpdateAutoOrderDetail($req);

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
    UpdateAutoOrderDetailRequest req = new UpdateAutoOrderDetailRequest();

    req.setAutoOrderID(1);
    req.setOrderLine(1);
    req.setItemID(1);
    req.setQty(1);
    req.setManualPriceEach(1);
    req.setManualTaxablePriceEach(1);
    req.setManualShippingPriceEach(1);
    req.setManualBVEach(1);
    req.setManualCVEach(1);
    req.setDescription("1");
    req.setPeriodDescriptionTy(1);
    req.setPriceEach(1);
    req.setPriceExt(1);
    req.setBVEach(1);
    req.setBusinessVolume(1);
    req.setCVEach(1);
    req.setCommissionableVolume(1);
    req.setDynamicKitItemID(1);
    req.setReference1("1");

    //Send Request to Server and Get Response
    UpdateAutoOrderDetailResponse res = api.getExigoApiSoap().updateAutoOrderDetail(req, auth);

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

### ChangeAutoOrderStatus

>  Changes the status of an AutoOrder. This is typically used to delete or suspend an auto order.

| | |
|---|---|
| Category | Recurring Orders |
| REST | `POST /3.0/autoorder/status` |
| SOAP action | `https://api.exigo.com/ChangeAutoOrderStatus` |
| WSDL elements | `ChangeAutoOrderStatusRequest` → `ChangeAutoOrderStatusResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=ChangeAutoOrderStatus |

#### Input

**`ChangeAutoOrderStatusRequest`**

| Property | Type | Notes |
|---|---|---|
| `AutoOrderID` | `Int32` |  |
| `AutoOrderStatus` | `AutoOrderStatusType` | **Values:** `Active`, `Inactive`, `Deleted` |

#### Output

**`ChangeAutoOrderStatusResponse`**

_No properties._

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/autoorder/status HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "autoOrderID": 1,
  "autoOrderStatus": null
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
SOAPAction: "https://api.exigo.com/ChangeAutoOrderStatus"

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
    <ChangeAutoOrderStatusRequest xmlns="http://api.exigo.com/">
      <AutoOrderID>int</AutoOrderID>
      <AutoOrderStatus>Active or Inactive or Deleted</AutoOrderStatus>
    </ChangeAutoOrderStatusRequest>
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
    <ChangeAutoOrderStatusResult xmlns="http://api.exigo.com/" />
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
    var req = new ChangeAutoOrderStatusRequest();

    req.AutoOrderID = 1;
    req.AutoOrderStatus = AutoOrderStatusType.Active;

    //Send Request to Server and Get Response
    var res = await api.ChangeAutoOrderStatusAsync(req);

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
    ChangeAutoOrderStatusRequest req = new ChangeAutoOrderStatusRequest();

    req.AutoOrderID = 1;
    req.AutoOrderStatus = AutoOrderStatusType.Active;

    //Send Request to Server and Get Response
    ChangeAutoOrderStatusResponse res = api.ChangeAutoOrderStatus(req);

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
    Dim req as new ChangeAutoOrderStatusRequest()

    req.AutoOrderID = 1
    req.AutoOrderStatus = AutoOrderStatusType.Active

    'Send Request to Server and Get Response
    Dim res As ChangeAutoOrderStatusResponse = api.ChangeAutoOrderStatus(req)

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

    $req->AutoOrderID = 1;
    $req->AutoOrderStatus = 1;

    //Send Request to Server and Get Response
    $res = $api.ChangeAutoOrderStatus($req);

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
    ChangeAutoOrderStatusRequest req = new ChangeAutoOrderStatusRequest();

    req.setAutoOrderID(1);
    req.setAutoOrderStatus(1);

    //Send Request to Server and Get Response
    ChangeAutoOrderStatusResponse res = api.getExigoApiSoap().changeAutoOrderStatus(req, auth);

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

### GetAutoOrders

>  Returns any AutoOrders setup and active for a given customer.

| | |
|---|---|
| Category | Recurring Orders |
| REST | `GET /3.0/autoorder?customerID=1` |
| SOAP action | `https://api.exigo.com/GetAutoOrders` |
| WSDL elements | `GetAutoOrdersRequest` → `GetAutoOrdersResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetAutoOrders |

#### Input

**`GetAutoOrdersRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `AutoOrderID` | `Int32` | Optional. Use to pull just one AutoOrder. |
| `AutoOrderStatus` | `AutoOrderStatusType` | Optional. Will assume Active if not supplied.<br>**Values:** `Active`, `Inactive`, `Deleted` |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`GetAutoOrdersResponse`**

| Property | Type | Notes |
|---|---|---|
| `AutoOrders` | `AutoOrderResponse[]` |  |

**`AutoOrderResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| &nbsp;&nbsp;↳ `AutoOrderID` | `Int32` |  |
| &nbsp;&nbsp;↳ `AutoOrderStatus` | `AutoOrderStatusType` | **Values:** `Active`, `Inactive`, `Deleted` |
| &nbsp;&nbsp;↳ `Frequency` | `FrequencyType` | **Values:** `Weekly`, `BiWeekly`, `Monthly`, `Quarterly`, `SemiYearly`, `Yearly`, `BiMonthly`, `EveryFourWeeks`, `EverySixWeeks`, `EveryEightWeeks`, `EveryTwelveWeeks`, `SpecificDays`, `Custom` |
| &nbsp;&nbsp;↳ `StartDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `StopDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `LastRunDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `NextRunDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `CurrencyCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `WarehouseID` | `Int32` | Unique location for orders.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `ShipMethodID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `PaymentType` | `AutoOrderPaymentType` | Payment type.<br>**Values:** `PrimaryCreditCard`, `SecondaryCreditCard`, `CheckingAccount`, `WillSendPayment`, `BankDraft`, `PrimaryWalletAccount`, `SecondaryWalletAccount`, `ThirdWalletAccount`, `FourthWalletAccount`, `FifthWalletAccount` |
| &nbsp;&nbsp;↳ `ProcessType` | `AutoOrderProcessType` | **Values:** `AlwaysProcess`, `Conditional` |
| &nbsp;&nbsp;↳ `FirstName` | `String` |  |
| &nbsp;&nbsp;↳ `LastName` | `String` |  |
| &nbsp;&nbsp;↳ `Company` | `String` |  |
| &nbsp;&nbsp;↳ `Address1` | `String` |  |
| &nbsp;&nbsp;↳ `Address2` | `String` |  |
| &nbsp;&nbsp;↳ `Address3` | `String` |  |
| &nbsp;&nbsp;↳ `City` | `String` |  |
| &nbsp;&nbsp;↳ `State` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Zip` | `String` |  |
| &nbsp;&nbsp;↳ `Country` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `County` | `String` |  |
| &nbsp;&nbsp;↳ `Email` | `String` |  |
| &nbsp;&nbsp;↳ `Phone` | `String` |  |
| &nbsp;&nbsp;↳ `Notes` | `String` |  |
| &nbsp;&nbsp;↳ `Total` | `Decimal` |  |
| &nbsp;&nbsp;↳ `SubTotal` | `Decimal` |  |
| &nbsp;&nbsp;↳ `TaxTotal` | `Decimal` |  |
| &nbsp;&nbsp;↳ `ShippingTotal` | `Decimal` |  |
| &nbsp;&nbsp;↳ `DiscountTotal` | `Decimal` |  |
| &nbsp;&nbsp;↳ `BusinessVolumeTotal` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CommissionableVolumeTotal` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Description` | `String` |  |
| &nbsp;&nbsp;↳ `Other11` | `String` |  |
| &nbsp;&nbsp;↳ `Other12` | `String` |  |
| &nbsp;&nbsp;↳ `Other13` | `String` |  |
| &nbsp;&nbsp;↳ `Other14` | `String` |  |
| &nbsp;&nbsp;↳ `Other15` | `String` |  |
| &nbsp;&nbsp;↳ `Other16` | `String` |  |
| &nbsp;&nbsp;↳ `Other17` | `String` |  |
| &nbsp;&nbsp;↳ `Other18` | `String` |  |
| &nbsp;&nbsp;↳ `Other19` | `String` |  |
| &nbsp;&nbsp;↳ `Other20` | `String` |  |
| &nbsp;&nbsp;↳ `Details` | `AutoOrderDetailResponse[]` |  |
| &nbsp;&nbsp;↳ `ModifiedDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `ModifiedBy` | `String` |  |
| &nbsp;&nbsp;↳ `MiddleName` | `String` |  |
| &nbsp;&nbsp;↳ `NameSuffix` | `String` |  |
| &nbsp;&nbsp;↳ `SpecificDayInterval` | `Int32` |  |
| &nbsp;&nbsp;↳ `CreatedDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `CreatedBy` | `String` |  |
| &nbsp;&nbsp;↳ `CustomerKey` | `String` | Unique alpha numeric identifier for customer record . |
| &nbsp;&nbsp;↳ `CustomFrequencyTy` | `Int32` | To be used with Frequency Type Custom. |

**`AutoOrderDetailResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `ItemCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Description` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Quantity` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `PriceEach` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `PriceTotal` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `BusinessVolumeEach` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `CommissionableVolumeEach` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `CommissionableVolume` | `Decimal` | Price amount. |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `ParentItemCode` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `PriceEachOverride` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `TaxableEachOverride` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `ShippingPriceEachOverride` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `BusinessVolumeEachOverride` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `CommissionableVolumeEachOverride` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Reference1` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `ProcessWhileDate` | `DateTime` | Obsolete. Use DetailEndDate instead. |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `SkipUntilDate` | `DateTime` | Obsolete. Use DetailStartDate instead. |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `DetailStartDate` | `DateTime` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `DetailEndDate` | `DateTime` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `DetailInterval` | `Int32` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `OrderLine` | `Int32` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `BusinessVolume` | `Decimal` | Price amount. |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `AutoOrderDetailID` | `Guid` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `ParentAutoOrderDetailID` | `Guid` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/autoorder?customerID=1
  &customerKey=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "autoOrders": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetAutoOrders"

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
    <GetAutoOrdersRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <AutoOrderID>int</AutoOrderID>
      <AutoOrderStatus>Active or Inactive or Deleted</AutoOrderStatus>
      <CustomerKey>string</CustomerKey>
    </GetAutoOrdersRequest>
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
    <GetAutoOrdersResult xmlns="http://api.exigo.com/">
      <AutoOrders>
        <AutoOrderResponse>
          <CustomerID>int</CustomerID>
          <AutoOrderID>int</AutoOrderID>
          <AutoOrderStatus>Active or Inactive or Deleted</AutoOrderStatus>
          <Frequency>Weekly or BiWeekly or Monthly or BiMonthly or Quarterly or SemiYearly or Yearly or EveryFourWeeks or EverySixWeeks or EveryEightWeeks or EveryTwelveWeeks or SpecificDays or Custom</Frequency>
          <StartDate>dateTime</StartDate>
          <StopDate>dateTime</StopDate>
          <LastRunDate>dateTime</LastRunDate>
          <NextRunDate>dateTime</NextRunDate>
          <CurrencyCode>string</CurrencyCode>
          <WarehouseID>int</WarehouseID>
          <ShipMethodID>int</ShipMethodID>
          <PaymentType>PrimaryCreditCard or SecondaryCreditCard or CheckingAccount or WillSendPayment or BankDraft or PrimaryWalletAccount or SecondaryWalletAccount or ThirdWalletAccount or FourthWalletAccount or FifthWalletAccount</PaymentType>
          <ProcessType>AlwaysProcess or Conditional</ProcessType>
          <FirstName>string</FirstName>
          <LastName>string</LastName>
          <Company>string</Company>
          <Address1>string</Address1>
          <Address2>string</Address2>
          <Address3>string</Address3>
          <City>string</City>
          <State>string</State>
          <Zip>string</Zip>
          <Country>string</Country>
          <County>string</County>
          <Email>string</Email>
          <Phone>string</Phone>
          <Notes>string</Notes>
          <Total>decimal</Total>
          <SubTotal>decimal</SubTotal>
          <TaxTotal>decimal</TaxTotal>
          <ShippingTotal>decimal</ShippingTotal>
          <DiscountTotal>decimal</DiscountTotal>
          <BusinessVolumeTotal>decimal</BusinessVolumeTotal>
          <CommissionableVolumeTotal>decimal</CommissionableVolumeTotal>
          <Description>string</Description>
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
            <AutoOrderDetailResponse>
              <ItemCode>string</ItemCode>
              <Description>string</Description>
              <Quantity>decimal</Quantity>
              <PriceEach>decimal</PriceEach>
              <PriceTotal>decimal</PriceTotal>
              <BusinessVolumeEach>decimal</BusinessVolumeEach>
              <BusinesVolume>decimal</BusinesVolume>
              <CommissionableVolumeEach>decimal</CommissionableVolumeEach>
              <CommissionableVolume>decimal</CommissionableVolume>
              <ParentItemCode>string</ParentItemCode>
              <PriceEachOverride>decimal</PriceEachOverride>
              <TaxableEachOverride>decimal</TaxableEachOverride>
              <ShippingPriceEachOverride>decimal</ShippingPriceEachOverride>
              <BusinessVolumeEachOverride>decimal</BusinessVolumeEachOverride>
              <CommissionableVolumeEachOverride>decimal</CommissionableVolumeEachOverride>
              <Reference1>string</Reference1>
              <ProcessWhileDate>dateTime</ProcessWhileDate>
              <SkipUntilDate>dateTime</SkipUntilDate>
              <DetailStartDate>dateTime</DetailStartDate>
              <DetailEndDate>dateTime</DetailEndDate>
              <DetailInterval>int</DetailInterval>
              <OrderLine>int</OrderLine>
              <BusinessVolume>decimal</BusinessVolume>
              <AutoOrderDetailID>guid</AutoOrderDetailID>
              <ParentAutoOrderDetailID>guid</ParentAutoOrderDetailID>
            </AutoOrderDetailResponse>
          </Details>
          <ModifiedDate>dateTime</ModifiedDate>
          <ModifiedBy>string</ModifiedBy>
          <MiddleName>string</MiddleName>
          <NameSuffix>string</NameSuffix>
          <SpecificDayInterval>int</SpecificDayInterval>
          <CreatedDate>dateTime</CreatedDate>
          <CreatedBy>string</CreatedBy>
          <CustomerKey>string</CustomerKey>
          <CustomFrequencyTy>int</CustomFrequencyTy>
        </AutoOrderResponse>
      </AutoOrders>
    </GetAutoOrdersResult>
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
    var req = new GetAutoOrdersRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.GetAutoOrdersAsync(req);

    //Now examine the results:

    foreach (var autoOrder  in res.AutoOrders)
    {
        Console.WriteLine("CustomerID: {0}", autoOrder.CustomerID);
        Console.WriteLine("AutoOrderID: {0}", autoOrder.AutoOrderID);
        Console.WriteLine("AutoOrderStatus: {0}", autoOrder.AutoOrderStatus);
        Console.WriteLine("Frequency: {0}", autoOrder.Frequency);
        Console.WriteLine("StartDate: {0}", autoOrder.StartDate);
        Console.WriteLine("StopDate: {0}", autoOrder.StopDate);
        Console.WriteLine("LastRunDate: {0}", autoOrder.LastRunDate);
        Console.WriteLine("NextRunDate: {0}", autoOrder.NextRunDate);
        Console.WriteLine("CurrencyCode: {0}", autoOrder.CurrencyCode);
        Console.WriteLine("WarehouseID: {0}", autoOrder.WarehouseID);
        Console.WriteLine("ShipMethodID: {0}", autoOrder.ShipMethodID);
        Console.WriteLine("PaymentType: {0}", autoOrder.PaymentType);
        Console.WriteLine("ProcessType: {0}", autoOrder.ProcessType);
        Console.WriteLine("FirstName: {0}", autoOrder.FirstName);
        Console.WriteLine("LastName: {0}", autoOrder.LastName);
        Console.WriteLine("Company: {0}", autoOrder.Company);
        Console.WriteLine("Address1: {0}", autoOrder.Address1);
        Console.WriteLine("Address2: {0}", autoOrder.Address2);
        Console.WriteLine("Address3: {0}", autoOrder.Address3);
        Console.WriteLine("City: {0}", autoOrder.City);
        Console.WriteLine("Zip: {0}", autoOrder.Zip);
        Console.WriteLine("County: {0}", autoOrder.County);
        Console.WriteLine("Email: {0}", autoOrder.Email);
        Console.WriteLine("Phone: {0}", autoOrder.Phone);
        Console.WriteLine("Notes: {0}", autoOrder.Notes);
        Console.WriteLine("Total: {0}", autoOrder.Total);
        Console.WriteLine("SubTotal: {0}", autoOrder.SubTotal);
        Console.WriteLine("TaxTotal: {0}", autoOrder.TaxTotal);
        Console.WriteLine("ShippingTotal: {0}", autoOrder.ShippingTotal);
        Console.WriteLine("DiscountTotal: {0}", autoOrder.DiscountTotal);
        Console.WriteLine("BusinessVolumeTotal: {0}", autoOrder.BusinessVolumeTotal);
        Console.WriteLine("CommissionableVolumeTotal: {0}", autoOrder.CommissionableVolumeTotal);
        Console.WriteLine("Description: {0}", autoOrder.Description);
        Console.WriteLine("Other11: {0}", autoOrder.Other11);
        Console.WriteLine("Other12: {0}", autoOrder.Other12);
        Console.WriteLine("Other13: {0}", autoOrder.Other13);
        Console.WriteLine("Other14: {0}", autoOrder.Other14);
        Console.WriteLine("Other15: {0}", autoOrder.Other15);
        Console.WriteLine("Other16: {0}", autoOrder.Other16);
        Console.WriteLine("Other17: {0}", autoOrder.Other17);
        Console.WriteLine("Other18: {0}", autoOrder.Other18);
        Console.WriteLine("Other19: {0}", autoOrder.Other19);
        Console.WriteLine("Other20: {0}", autoOrder.Other20);

        foreach (var autoOrderDetail  in autoOrder.Details)
        {
            Console.WriteLine("ItemCode: {0}", autoOrderDetail.ItemCode);
            Console.WriteLine("Description: {0}", autoOrderDetail.Description);
            Console.WriteLine("Quantity: {0}", autoOrderDetail.Quantity);
            Console.WriteLine("PriceEach: {0}", autoOrderDetail.PriceEach);
            Console.WriteLine("PriceTotal: {0}", autoOrderDetail.PriceTotal);
            Console.WriteLine("BusinessVolumeEach: {0}", autoOrderDetail.BusinessVolumeEach);
            Console.WriteLine("BusinesVolume: {0}", autoOrderDetail.BusinesVolume);
            Console.WriteLine("CommissionableVolumeEach: {0}", autoOrderDetail.CommissionableVolumeEach);
            Console.WriteLine("CommissionableVolume: {0}", autoOrderDetail.CommissionableVolume);
            Console.WriteLine("OrderLine: {0}", autoOrderDetail.OrderLine);
            Console.WriteLine("BusinessVolume: {0}", autoOrderDetail.BusinessVolume);
            Console.WriteLine("AutoOrderDetailID: {0}", autoOrderDetail.AutoOrderDetailID);
            Console.WriteLine("ParentAutoOrderDetailID: {0}", autoOrderDetail.ParentAutoOrderDetailID);
        }
        Console.WriteLine("ModifiedDate: {0}", autoOrder.ModifiedDate);
        Console.WriteLine("ModifiedBy: {0}", autoOrder.ModifiedBy);
        Console.WriteLine("MiddleName: {0}", autoOrder.MiddleName);
        Console.WriteLine("NameSuffix: {0}", autoOrder.NameSuffix);
        Console.WriteLine("SpecificDayInterval: {0}", autoOrder.SpecificDayInterval);
        Console.WriteLine("CreatedDate: {0}", autoOrder.CreatedDate);
        Console.WriteLine("CreatedBy: {0}", autoOrder.CreatedBy);
        Console.WriteLine("CustomerKey: {0}", autoOrder.CustomerKey);
        Console.WriteLine("CustomFrequencyTy: {0}", autoOrder.CustomFrequencyTy);
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
    GetAutoOrdersRequest req = new GetAutoOrdersRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    GetAutoOrdersResponse res = api.GetAutoOrders(req);

    //Now examine the results:

    foreach (AutoOrderResponse autoOrder  in res.AutoOrders)
    {
        Console.WriteLine("CustomerID: {0}", autoOrder.CustomerID);
        Console.WriteLine("AutoOrderID: {0}", autoOrder.AutoOrderID);
        Console.WriteLine("AutoOrderStatus: {0}", autoOrder.AutoOrderStatus);
        Console.WriteLine("Frequency: {0}", autoOrder.Frequency);
        Console.WriteLine("StartDate: {0}", autoOrder.StartDate);
        Console.WriteLine("StopDate: {0}", autoOrder.StopDate);
        Console.WriteLine("LastRunDate: {0}", autoOrder.LastRunDate);
        Console.WriteLine("NextRunDate: {0}", autoOrder.NextRunDate);
        Console.WriteLine("CurrencyCode: {0}", autoOrder.CurrencyCode);
        Console.WriteLine("WarehouseID: {0}", autoOrder.WarehouseID);
        Console.WriteLine("ShipMethodID: {0}", autoOrder.ShipMethodID);
        Console.WriteLine("PaymentType: {0}", autoOrder.PaymentType);
        Console.WriteLine("ProcessType: {0}", autoOrder.ProcessType);
        Console.WriteLine("FirstName: {0}", autoOrder.FirstName);
        Console.WriteLine("LastName: {0}", autoOrder.LastName);
        Console.WriteLine("Company: {0}", autoOrder.Company);
        Console.WriteLine("Address1: {0}", autoOrder.Address1);
        Console.WriteLine("Address2: {0}", autoOrder.Address2);
        Console.WriteLine("Address3: {0}", autoOrder.Address3);
        Console.WriteLine("City: {0}", autoOrder.City);
        Console.WriteLine("Zip: {0}", autoOrder.Zip);
        Console.WriteLine("County: {0}", autoOrder.County);
        Console.WriteLine("Email: {0}", autoOrder.Email);
        Console.WriteLine("Phone: {0}", autoOrder.Phone);
        Console.WriteLine("Notes: {0}", autoOrder.Notes);
        Console.WriteLine("Total: {0}", autoOrder.Total);
        Console.WriteLine("SubTotal: {0}", autoOrder.SubTotal);
        Console.WriteLine("TaxTotal: {0}", autoOrder.TaxTotal);
        Console.WriteLine("ShippingTotal: {0}", autoOrder.ShippingTotal);
        Console.WriteLine("DiscountTotal: {0}", autoOrder.DiscountTotal);
        Console.WriteLine("BusinessVolumeTotal: {0}", autoOrder.BusinessVolumeTotal);
        Console.WriteLine("CommissionableVolumeTotal: {0}", autoOrder.CommissionableVolumeTotal);
        Console.WriteLine("Description: {0}", autoOrder.Description);
        Console.WriteLine("Other11: {0}", autoOrder.Other11);
        Console.WriteLine("Other12: {0}", autoOrder.Other12);
        Console.WriteLine("Other13: {0}", autoOrder.Other13);
        Console.WriteLine("Other14: {0}", autoOrder.Other14);
        Console.WriteLine("Other15: {0}", autoOrder.Other15);
        Console.WriteLine("Other16: {0}", autoOrder.Other16);
        Console.WriteLine("Other17: {0}", autoOrder.Other17);
        Console.WriteLine("Other18: {0}", autoOrder.Other18);
        Console.WriteLine("Other19: {0}", autoOrder.Other19);
        Console.WriteLine("Other20: {0}", autoOrder.Other20);

        foreach (AutoOrderDetailResponse autoOrderDetail  in autoOrder.Details)
        {
            Console.WriteLine("ItemCode: {0}", autoOrderDetail.ItemCode);
            Console.WriteLine("Description: {0}", autoOrderDetail.Description);
            Console.WriteLine("Quantity: {0}", autoOrderDetail.Quantity);
            Console.WriteLine("PriceEach: {0}", autoOrderDetail.PriceEach);
            Console.WriteLine("PriceTotal: {0}", autoOrderDetail.PriceTotal);
            Console.WriteLine("BusinessVolumeEach: {0}", autoOrderDetail.BusinessVolumeEach);
            Console.WriteLine("BusinesVolume: {0}", autoOrderDetail.BusinesVolume);
            Console.WriteLine("CommissionableVolumeEach: {0}", autoOrderDetail.CommissionableVolumeEach);
            Console.WriteLine("CommissionableVolume: {0}", autoOrderDetail.CommissionableVolume);
            Console.WriteLine("OrderLine: {0}", autoOrderDetail.OrderLine);
            Console.WriteLine("BusinessVolume: {0}", autoOrderDetail.BusinessVolume);
            Console.WriteLine("AutoOrderDetailID: {0}", autoOrderDetail.AutoOrderDetailID);
            Console.WriteLine("ParentAutoOrderDetailID: {0}", autoOrderDetail.ParentAutoOrderDetailID);
        }
        Console.WriteLine("ModifiedDate: {0}", autoOrder.ModifiedDate);
        Console.WriteLine("ModifiedBy: {0}", autoOrder.ModifiedBy);
        Console.WriteLine("MiddleName: {0}", autoOrder.MiddleName);
        Console.WriteLine("NameSuffix: {0}", autoOrder.NameSuffix);
        Console.WriteLine("SpecificDayInterval: {0}", autoOrder.SpecificDayInterval);
        Console.WriteLine("CreatedDate: {0}", autoOrder.CreatedDate);
        Console.WriteLine("CreatedBy: {0}", autoOrder.CreatedBy);
        Console.WriteLine("CustomerKey: {0}", autoOrder.CustomerKey);
        Console.WriteLine("CustomFrequencyTy: {0}", autoOrder.CustomFrequencyTy);
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
    Dim req as new GetAutoOrdersRequest()

    req.CustomerID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As GetAutoOrdersResponse = api.GetAutoOrders(req)

    'Now examine the results:

    For Each autoOrder As AutoOrderResponse In res.AutoOrders
        Console.WriteLine("CustomerID: {0}", autoOrder.CustomerID)
        Console.WriteLine("AutoOrderID: {0}", autoOrder.AutoOrderID)
        Console.WriteLine("AutoOrderStatus: {0}", autoOrder.AutoOrderStatus)
        Console.WriteLine("Frequency: {0}", autoOrder.Frequency)
        Console.WriteLine("StartDate: {0}", autoOrder.StartDate)
        Console.WriteLine("StopDate: {0}", autoOrder.StopDate)
        Console.WriteLine("LastRunDate: {0}", autoOrder.LastRunDate)
        Console.WriteLine("NextRunDate: {0}", autoOrder.NextRunDate)
        Console.WriteLine("CurrencyCode: {0}", autoOrder.CurrencyCode)
        Console.WriteLine("WarehouseID: {0}", autoOrder.WarehouseID)
        Console.WriteLine("ShipMethodID: {0}", autoOrder.ShipMethodID)
        Console.WriteLine("PaymentType: {0}", autoOrder.PaymentType)
        Console.WriteLine("ProcessType: {0}", autoOrder.ProcessType)
        Console.WriteLine("FirstName: {0}", autoOrder.FirstName)
        Console.WriteLine("LastName: {0}", autoOrder.LastName)
        Console.WriteLine("Company: {0}", autoOrder.Company)
        Console.WriteLine("Address1: {0}", autoOrder.Address1)
        Console.WriteLine("Address2: {0}", autoOrder.Address2)
        Console.WriteLine("Address3: {0}", autoOrder.Address3)
        Console.WriteLine("City: {0}", autoOrder.City)
        Console.WriteLine("Zip: {0}", autoOrder.Zip)
        Console.WriteLine("County: {0}", autoOrder.County)
        Console.WriteLine("Email: {0}", autoOrder.Email)
        Console.WriteLine("Phone: {0}", autoOrder.Phone)
        Console.WriteLine("Notes: {0}", autoOrder.Notes)
        Console.WriteLine("Total: {0}", autoOrder.Total)
        Console.WriteLine("SubTotal: {0}", autoOrder.SubTotal)
        Console.WriteLine("TaxTotal: {0}", autoOrder.TaxTotal)
        Console.WriteLine("ShippingTotal: {0}", autoOrder.ShippingTotal)
        Console.WriteLine("DiscountTotal: {0}", autoOrder.DiscountTotal)
        Console.WriteLine("BusinessVolumeTotal: {0}", autoOrder.BusinessVolumeTotal)
        Console.WriteLine("CommissionableVolumeTotal: {0}", autoOrder.CommissionableVolumeTotal)
        Console.WriteLine("Description: {0}", autoOrder.Description)
        Console.WriteLine("Other11: {0}", autoOrder.Other11)
        Console.WriteLine("Other12: {0}", autoOrder.Other12)
        Console.WriteLine("Other13: {0}", autoOrder.Other13)
        Console.WriteLine("Other14: {0}", autoOrder.Other14)
        Console.WriteLine("Other15: {0}", autoOrder.Other15)
        Console.WriteLine("Other16: {0}", autoOrder.Other16)
        Console.WriteLine("Other17: {0}", autoOrder.Other17)
        Console.WriteLine("Other18: {0}", autoOrder.Other18)
        Console.WriteLine("Other19: {0}", autoOrder.Other19)
        Console.WriteLine("Other20: {0}", autoOrder.Other20)

        For Each autoOrderDetail As AutoOrderDetailResponse In autoOrder.Details
            Console.WriteLine("ItemCode: {0}", autoOrderDetail.ItemCode)
            Console.WriteLine("Description: {0}", autoOrderDetail.Description)
            Console.WriteLine("Quantity: {0}", autoOrderDetail.Quantity)
            Console.WriteLine("PriceEach: {0}", autoOrderDetail.PriceEach)
            Console.WriteLine("PriceTotal: {0}", autoOrderDetail.PriceTotal)
            Console.WriteLine("BusinessVolumeEach: {0}", autoOrderDetail.BusinessVolumeEach)
            Console.WriteLine("BusinesVolume: {0}", autoOrderDetail.BusinesVolume)
            Console.WriteLine("CommissionableVolumeEach: {0}", autoOrderDetail.CommissionableVolumeEach)
            Console.WriteLine("CommissionableVolume: {0}", autoOrderDetail.CommissionableVolume)
            Console.WriteLine("OrderLine: {0}", autoOrderDetail.OrderLine)
            Console.WriteLine("BusinessVolume: {0}", autoOrderDetail.BusinessVolume)
            Console.WriteLine("AutoOrderDetailID: {0}", autoOrderDetail.AutoOrderDetailID)
            Console.WriteLine("ParentAutoOrderDetailID: {0}", autoOrderDetail.ParentAutoOrderDetailID)
        Next
        Console.WriteLine("ModifiedDate: {0}", autoOrder.ModifiedDate)
        Console.WriteLine("ModifiedBy: {0}", autoOrder.ModifiedBy)
        Console.WriteLine("MiddleName: {0}", autoOrder.MiddleName)
        Console.WriteLine("NameSuffix: {0}", autoOrder.NameSuffix)
        Console.WriteLine("SpecificDayInterval: {0}", autoOrder.SpecificDayInterval)
        Console.WriteLine("CreatedDate: {0}", autoOrder.CreatedDate)
        Console.WriteLine("CreatedBy: {0}", autoOrder.CreatedBy)
        Console.WriteLine("CustomerKey: {0}", autoOrder.CustomerKey)
        Console.WriteLine("CustomFrequencyTy: {0}", autoOrder.CustomFrequencyTy)
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
    $res = $api.GetAutoOrders($req);

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
    GetAutoOrdersRequest req = new GetAutoOrdersRequest();

    req.setCustomerID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    GetAutoOrdersResponse res = api.getExigoApiSoap().getAutoOrders(req, auth);

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

### AutoOrderSkipNextShipment

> Disables the auotorder next scheduled date

| | |
|---|---|
| Category | Recurring Orders |
| REST | `POST /3.0/autoorder/skip` |
| SOAP action | `https://api.exigo.com/AutoOrderSkipNextShipment` |
| WSDL elements | `AutoOrderSkipNextShipmentRequest` → `AutoOrderSkipNextShipmentResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=AutoOrderSkipNextShipment |

#### Input

**`AutoOrderSkipNextShipmentRequest`**

| Property | Type | Notes |
|---|---|---|
| `AutoOrderId` | `Int32` | Unique numeric identifier for the AutoOrder. |

#### Output

**`AutoOrderSkipNextShipmentResponse`**

| Property | Type | Notes |
|---|---|---|
| `NextRunDate` | `DateTime` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/autoorder/skip HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "autoOrderId": 1
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "nextRunDate": "2026-11-10T00:00:00-06:00",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/AutoOrderSkipNextShipment"

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
    <AutoOrderSkipNextShipmentRequest xmlns="http://api.exigo.com/">
      <AutoOrderId>int</AutoOrderId>
    </AutoOrderSkipNextShipmentRequest>
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
    <AutoOrderSkipNextShipmentResult xmlns="http://api.exigo.com/">
      <NextRunDate>dateTime</NextRunDate>
    </AutoOrderSkipNextShipmentResult>
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
    var req = new AutoOrderSkipNextShipmentRequest();

    req.AutoOrderId = 1;            //Unique numeric identifier for the AutoOrder.

    //Send Request to Server and Get Response
    var res = await api.AutoOrderSkipNextShipmentAsync(req);

    //Now examine the results:
    Console.WriteLine("NextRunDate: {0}", res.NextRunDate);
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
    AutoOrderSkipNextShipmentRequest req = new AutoOrderSkipNextShipmentRequest();

    req.AutoOrderId = 1;            //Unique numeric identifier for the AutoOrder.

    //Send Request to Server and Get Response
    AutoOrderSkipNextShipmentResponse res = api.AutoOrderSkipNextShipment(req);

    //Now examine the results:
    Console.WriteLine("NextRunDate: {0}", res.NextRunDate);
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
    Dim req as new AutoOrderSkipNextShipmentRequest()

    req.AutoOrderId = 1

    'Send Request to Server and Get Response
    Dim res As AutoOrderSkipNextShipmentResponse = api.AutoOrderSkipNextShipment(req)

    'Now examine the results:
    Console.WriteLine("NextRunDate: {0}", res.NextRunDate)
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

    $req->AutoOrderId = 1;

    //Send Request to Server and Get Response
    $res = $api.AutoOrderSkipNextShipment($req);

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
    AutoOrderSkipNextShipmentRequest req = new AutoOrderSkipNextShipmentRequest();

    req.setAutoOrderId(1);

    //Send Request to Server and Get Response
    AutoOrderSkipNextShipmentResponse res = api.getExigoApiSoap().autoOrderSkipNextShipment(req, auth);

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
