# Exigo API — Orders/Payments

API version v2025.11.7.6. Crawled 2026-11-11 from https://api.exigo.com/3.0/. Back to [index](../README.md).

A robust API for handling all transaction functions, including batch orders, invoicing, payment methods, and more. Full authentication is provided to support credit, debit and ACH transactions.

| Operation | REST | Summary |
|---|---|---|
| [ProcessTransaction](#processtransaction) | SOAP only | Commits multiple requests in one step. All business rules are checked before commit and it is a commit-all or fail-all. In your application, you may come across several instances… |
| [CalculateOrder](#calculateorder) | `POST /3.0/orders/calculate` | Calculates pricing, tax, shipping and volume info for a potential order. This is for calculation only and does not store a permanent record. Client provides address, itemcodes,… |
| [CreateOrder](#createorder) | `POST /3.0/orders` | Creates a new Order for an existing customer. Can create an order for a new customer if part of a transaction. Server will calculate all pricing, tax, shipping and volume info… |
| [CreateOrderImport](#createorderimport) | `POST /3.0/orders/import` | Imports a new Order for an existing customer. Use this for import routines or other instances where you wish to supply all calculation data. It is advised to use CreateOrder… |
| [UpdateOrder](#updateorder) | `PATCH /3.0/orders` | Updates one or more fields on an existing order. Can participate in a transaction. Note: This request can participate in a transaction. Learn more about transactions. |
| [UpdateOrderDetail](#updateorderdetail) | `PUT /3.0/orders/detail` | Update an existing Order Detail for an existing order without recalculating. Can participate in a transaction. Note: This request can participate in a transaction. Learn more… |
| [ChangeOrderStatus](#changeorderstatus) | `POST /3.0/orders/status` | Changes an existing order from one status to another. |
| [ChangeOrderStatusBatch](#changeorderstatusbatch) | `POST /3.0/orders/statusbatch` | Changes existing orders from one status to another in a batch. Can optionally update tracking numbers as well. |
| [ValidateCreditCardToken](#validatecreditcardtoken) | `POST /3.0/payment/validate/token` | Validates a credit card token. |
| [CreatePayment](#createpayment) | `POST /3.0/payment` | Creates a new payment type using cash, money order etc. |
| [CreatePaymentCreditCard](#createpaymentcreditcard) | `POST /3.0/payment/creditcard` | Creates a specific credit card payment for an existing order, or a new order in a transaction. Note: This does not charge a card, and you must have an authorization code to submit… |
| [CreatePaymentWallet](#createpaymentwallet) | `POST /3.0/payment/wallet` | Creates a new payment for wallet account. |
| [CreatePaymentPointAccount](#createpaymentpointaccount) | `POST /3.0/payment/pointaccount` | Creates a new payment for point account. |
| [CreatePaymentCheck](#createpaymentcheck) | `POST /3.0/payment/check` | Creates a new payment using check information. |
| [ChargeCreditCardToken](#chargecreditcardtoken) | `POST /3.0/payment/charge/token` | Attempts to charge a card token with the amount found on an exiting order, or a new order in a transaction.If the charge is successful, the order is changed to accepted. |
| [ChargeCreditCardTokenOnFile](#chargecreditcardtokenonfile) | `POST /3.0/payment/charge/tokenonfile` | Attempts to charge a card token on file with the amount found on an exiting order, or a new order in a transaction. If the charge is successful, the order is changed to accepted. |
| [ChargeGroupOrderCreditCardToken](#chargegroupordercreditcardtoken) | `POST /3.0/payment/charge/tokengroup` | Attempts to charge a card token with the amount found on the specified orders. |
| [RefundPriorCreditCardCharge](#refundpriorcreditcardcharge) | `POST /3.0/payment/refund/cc` | Refunds a prior charge. To be used with an order. |
| [ChargeWalletAccount](#chargewalletaccount) | `POST /3.0/payment/charge/wallet` | Attempts to debit a wallet account with the amount found on an exiting order, or a new order in a transaction. If the debit request is successful, the order is changed to accepted. |
| [ChargeWalletAccountOnFile](#chargewalletaccountonfile) | `POST /3.0/payment/charge/walletonfile` | Attempts to debit a wallet account with the amount found on an exiting order, or a new order in a transaction. If the debit request is successful, the order is changed to accepted. |
| [DebitBankAccount](#debitbankaccount) | `POST /3.0/payment/charge/bank` | Attempts to debit a bank account with the amount found on an exiting order, or a new order in a transaction. If the debit request is successful, the order is changed to accepted. |
| [DebitBankAccountOnFile](#debitbankaccountonfile) | `POST /3.0/payment/charge/bankonfile` | Attempts to debit a bank account on file with the amount found on an exiting order, or a new order in a transaction. If the debit request is successful, the order is changed to… |
| [CreateExpectedPayment](#createexpectedpayment) | `POST /3.0/payment/expectedpayment` | Creates a new expected payment type using cash, money order etc. Note: This request can participate in a transaction. Learn more about transactions. |
| [CreateExpectedBankWire](#createexpectedbankwire) | `POST /3.0/payment/wire` | Creates a new expected payment of type Bank Bire. Note: This request can participate in a transaction. Learn more about transactions. |
| [GetOrders](#getorders) | `GET /3.0/orders?customerID=1` | Returns one or more orders. You can submit several optional filter fields to control the results. |
| [GetCountryRegions](#getcountryregions) | `GET /3.0/country/regionsAuthorization:` | Returns countries setup for company as well as the regions for a single country requested. |
| [GetCustomerBalances](#getcustomerbalances) | `GET /3.0/customers/balances?customerID=1` | Returns the sum of orders, payments, and adjustments per currency. |
| [CreateCustomerBalanceAdjustment](#createcustomerbalanceadjustment) | `POST /3.0/customers/balances/adjustment` | Create an adjustment for a customer's account in a currency. |
| [RefundPriorWalletCharge](#refundpriorwalletcharge) | `POST /3.0/payment/refund/wallet` | Refunds a prior wallet charge. To be used with an order. |
| [GetOrderInvoice](#getorderinvoice) | `GET /3.0/orders/invoice?orderID=1` | Returns an Rendered Order Invoice |
| [GetOrderInvoiceBatch](#getorderinvoicebatch) | `GET /3.0/orders/invoicebatch?reportlayoutID=1` | Returns an rendered invoice of an orders batch |
| [ChargePriorAuthorization](#chargepriorauthorization) | SOAP only | Attempts to charge a prior authorization with the amount found on an existing order, or a new order in a transaction. If the charge is successful, the order is changed to accepted. |
| [AuthorizeOnlyCreditCardToken](#authorizeonlycreditcardtoken) | SOAP only | Attempts to authorize only a credit card token. A follow up ChargePriorAuthorization will need to be issued to actually capture and settle the authorization. |
| [AuthorizeOnlyCreditCardTokenOnFile](#authorizeonlycreditcardtokenonfile) | SOAP only | Attempts to authorize only a credit card token on file. A follow up ChargePriorAuthorization will need to be issued to actually capture and settle the authorization. |
| [RefundPriorDebitCharge](#refundpriordebitcharge) | `POST /3.0/payment/refund/debit` | Refunds a prior charge. To be used with an order. |
| [ValidateWalletAccount](#validatewalletaccount) | `POST /3.0/payment/validate/wallet` | Validates a Wallet Account. |

---
### ProcessTransaction

> Commits multiple requests in one step. All business rules are
>  checked before commit and it is a commit-all or fail-all.
>
> In your application, you may come across several instances where multiple method calls are needed to complete a single data entry.
>
> An example of this may be you are creating a new customer, generating a new order, applying a new payment and setting up a new auto order. In this scenario, it would be undesirable to have saved the customer, saved the order, but when you went to apply the payment, you received an error. You would now have a half-committed transaction. If you corrected the issue with the payment then resubmitted from the start, you would now have duplicate customers and orders. Hence the need for transactional support.
>
> This works by allowing you to create and post all your requests into a transactional "envelope". The server will then check all business rules before attempting to commit to the database. If all business rules pass, it then commits all data at once using a single database transaction. This guarantees that even if there is a sql exception, all will get rolled back cleanly. If an exception is encountered, you can safely correct the input that caused it and safely re-commit the request.

| | |
|---|---|
| Category | Orders/Payments |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/ProcessTransaction` |
| WSDL elements | `TransactionalRequest` → `ProcessTransactionResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=ProcessTransaction |

#### Input

**`TransactionalRequest`**

| Property | Type | Notes |
|---|---|---|
| `TransactionRequests` | `ApiRequest[]` |  |

**`ApiRequest`**

_No properties._

#### Output

**`TransactionalResponse`**

| Property | Type | Notes |
|---|---|---|
| `TransactionResponses` | `ApiResponse[]` |  |

**`ApiResponse`**

_No properties._

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/ProcessTransaction"

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
    <TransactionalRequest xmlns="http://api.exigo.com/">
      <TransactionRequests>
        <ApiRequest />
      </TransactionRequests>
    </TransactionalRequest>
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
    <ProcessTransactionResult xmlns="http://api.exigo.com/">
      <TransactionResponses>
        <ApiResponse>
          <Result>
            <Status>Success or Failure</Status>
            <Errors>
              <string>string</string>
            </Errors>
            <TransactionKey>string</TransactionKey>
          </Result>
        </ApiResponse>
      </TransactionResponses>
    </ProcessTransactionResult>
  </soap:Body>
</soap:Envelope>
```

</details>

<details><summary>C# REST client</summary>

_Install Nuget package Exigo.Api.Client_

```csharp

```

</details>

<details><summary>C# SOAP client</summary>

```csharp

```

</details>

<details><summary>VB.Net</summary>

```vbnet

```

</details>

<details><summary>PHP</summary>

_Note: PHP is not officially supported._

```php

```

</details>

<details><summary>Java</summary>

_Note: Java is not officially supported._

```java

```

</details>

<details><summary>CSV</summary>

_This method does not support csv output._

```text
© 2026 Exigo.
```

</details>

---

### CalculateOrder

>  Calculates pricing, tax, shipping and volume info for a potential order. This is for calculation only and does not
>  store a permanent record. Client provides address, itemcodes, and quantity. Server calculates and => s pricing, tax,
>  shipping and volume info.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `POST /3.0/orders/calculate` |
| SOAP action | `https://api.exigo.com/CalculateOrder` |
| WSDL elements | `CalculateOrderRequest` → `CalculateOrderResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CalculateOrder |

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
SOAPAction: "https://api.exigo.com/CalculateOrder"

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
    <CalculateOrderRequest xmlns="http://api.exigo.com/">
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
    </CalculateOrderRequest>
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
    <CalculateOrderResult xmlns="http://api.exigo.com/">
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
    </CalculateOrderResult>
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
    var res = await api.CalculateOrderAsync(req);

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
    CalculateOrderResponse res = api.CalculateOrder(req);

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
    Dim res As CalculateOrderResponse = api.CalculateOrder(req)

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
    $res = $api.CalculateOrder($req);

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
    CalculateOrderResponse res = api.getExigoApiSoap().calculateOrder(req, auth);

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

### CreateOrder

>  Creates a new Order for an existing customer. Can create an order for a new customer if part of a transaction.
>  Server will calculate all pricing, tax, shipping and volume info unless overridden in the request.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `POST /3.0/orders` |
| SOAP action | `https://api.exigo.com/CreateOrder` |
| WSDL elements | `CreateOrderRequest` → `CreateOrderResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateOrder |

#### Input

**`CreateOrderRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for a customer record. |
| `OrderStatus` | `OrderStatusType` | **Values:** `Incomplete`, `Pending`, `CCDeclined`, `ACHDeclined`, `Canceled`, `CCPending`, `ACHPending`, `Accepted`, `Printed`, `Shipped`, `PendingInventory` |
| `OrderDate` | `DateTime` |  |
| `CurrencyCode` | `String` |  |
| `WarehouseID` | `Int32` | Unique location for orders.<br>**Lookup:** company-specific list (see company-lists.md) |
| `ShipMethodID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| `PriceType` | `Int32` | Controls which price band to use.<br>**Lookup:** company-specific list (see company-lists.md) |
| `FirstName` | `String` | Optional. |
| `MiddleName` | `String` | Optional. |
| `LastName` | `String` | Optional. |
| `NameSuffix` | `String` | Optional. |
| `Company` | `String` | Optional. |
| `Address1` | `String` | Optional. |
| `Address2` | `String` | Optional. |
| `Address3` | `String` | Optional. |
| `City` | `String` | Optional. |
| `State` | `String` |  |
| `Zip` | `String` | Optional. |
| `Country` | `String` |  |
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
| `OrderType` | `OrderType` | **Values:** `Default`, `CustomerService`, `ShoppingCart`, `WebWizard`, `AutoOrder`, `Import`, `BackOrder`, `ReplacementOrder`, `ReturnOrder`, `WebAutoOrder`, `TicketSystem`, `APIOrder`, `BackOrderParent`, `ChildOrder`, `Other1`, `Other2`, `Other3`, `Other4`, `Other5`, `Other6`, `Other7`, `Other8`, `Other9`, `Other10` |
| `TaxRateOverride` | `Decimal` | Optional. |
| `ShippingAmountOverride` | `Decimal` | Optional. |
| `UseManualOrderID` | `Boolean` | Optional. If true, the new order's ID will be set to the ID provided in the ManualOrderID or ManualOrderKey. |
| `ManualOrderID` | `Int32` | Optional. Unique numeric identifier for new order record. If set, UseManualOrderID must also be set to true. |
| `TransferVolumeToID` | `Int32` | Optional. Only pass in if you want volume to goto another CustomerID. |
| `ReturnOrderID` | `Int32` | Optional. Unique numeric identifier for return order record. |
| `OverwriteExistingOrder` | `Boolean` |  |
| `ExistingOrderID` | `Int32` | Optional. Unique numeric identifier for existing order record. Defaults to 0. |
| `PartyID` | `Int32` | Optional. |
| `Details` | `OrderDetailRequest[]` | At least 1 item is required. |
| `SuppressPackSlipPrice` | `Boolean` |  |
| `TransferVolumeToKey` | `String` | Optional. Only pass in if you want volume to goto another Customer Key. |
| `ReturnOrderKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if ReturnOrderID & ReturnOrderKey are provided. |
| `ManualOrderKey` | `String` | Optional. Unique alpha numeric identifier for new order record. If set, UseManualOrderID must also be set to true. Exception will occur if ManualOrderID & ManualOrderKey are provided. |
| `ExistingOrderKey` | `String` | Optional. Unique alpha numeric identifier for existing order record. Exeption will occur if ExistingOrderID & ExistingOrderKey are provided. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if OrderID & OrderKey are provided. |
| `OrderSubStatusTy` | `Int32` | Optional. |
| `ReferralID` | `Int32` | Optional. Numeric identifier for the customer who owns the site from the order was created on, if apply. |

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

**`CreateOrderResponse`**

| Property | Type | Notes |
|---|---|---|
| `OrderID` | `Int32` | Unique numeric identifier for order record. |
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
| `HandlingFeeTotal` | `Decimal` |  |
| `Details` | `OrderDetailResponse[]` |  |
| `Warnings` | `String` |  |
| `OrderKey` | `String` | Unique alpha numeric identifier for order record. |
| `ReferralID` | `Int32` | Numeric identifier for the customer who owns the site from the order was created on, if apply. |

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
POST https://yourcompany-api.exigo.com/3.0/orders HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "orderStatus": null,
  "orderDate": "2026-11-10T00:00:00-06:00",
  "currencyCode": "1",
  "warehouseID": 1,
  "shipMethodID": 1,
  "priceType": 1,
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
  "orderType": null,
  "transferVolumeToID": 1,
  "returnOrderID": 1,
  "overwriteExistingOrder": true,
  "existingOrderID": 1,
  "partyID": 1,
  "details": null,
  "suppressPackSlipPrice": true,
  "transferVolumeToKey": "1",
  "returnOrderKey": "1",
  "existingOrderKey": "1",
  "customerKey": "1",
  "referralID": 1
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "orderID": 1,
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
  "handlingFeeTotal": null,
  "details": null,
  "warnings": "",
  "orderKey": "",
  "referralID": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateOrder"

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
    <CreateOrderRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <OrderStatus>Incomplete or Pending or CCDeclined or ACHDeclined or Canceled or CCPending or ACHPending or Accepted or Printed or Shipped or PendingInventory</OrderStatus>
      <OrderDate>dateTime</OrderDate>
      <CurrencyCode>string</CurrencyCode>
      <WarehouseID>int</WarehouseID>
      <ShipMethodID>int</ShipMethodID>
      <PriceType>int</PriceType>
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
      <OrderType>Default or CustomerService or ShoppingCart or WebWizard or AutoOrder or Import or BackOrder or ReplacementOrder or ReturnOrder or WebAutoOrder or TicketSystem or APIOrder or BackOrderParent or ChildOrder or Other1 or Other2 or Other3 or Other4 or Other5 or Other6 or Other7 or Other8 or Other9 or Other10</OrderType>
      <TaxRateOverride>decimal</TaxRateOverride>
      <ShippingAmountOverride>decimal</ShippingAmountOverride>
      <UseManualOrderID>boolean</UseManualOrderID>
      <ManualOrderID>int</ManualOrderID>
      <TransferVolumeToID>int</TransferVolumeToID>
      <ReturnOrderID>int</ReturnOrderID>
      <OverwriteExistingOrder>boolean</OverwriteExistingOrder>
      <ExistingOrderID>int</ExistingOrderID>
      <PartyID>int</PartyID>
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
      <SuppressPackSlipPrice>boolean</SuppressPackSlipPrice>
      <TransferVolumeToKey>string</TransferVolumeToKey>
      <ReturnOrderKey>string</ReturnOrderKey>
      <ManualOrderKey>string</ManualOrderKey>
      <ExistingOrderKey>string</ExistingOrderKey>
      <CustomerKey>string</CustomerKey>
      <OrderSubStatusTy>int</OrderSubStatusTy>
      <ReferralID>int</ReferralID>
    </CreateOrderRequest>
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
    <CreateOrderResult xmlns="http://api.exigo.com/">
      <OrderID>int</OrderID>
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
      <HandlingFeeTotal>decimal</HandlingFeeTotal>
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
      <Warnings>
        <string>string</string>
      </Warnings>
      <OrderKey>string</OrderKey>
      <ReferralID>int</ReferralID>
    </CreateOrderResult>
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
    var req = new CreateOrderRequest();

    req.CustomerID = 1;             //Unique numeric identifier for a customer record.
    req.OrderStatus = OrderStatusType.Incomplete;
    req.OrderDate = DateTime.Today;
    req.CurrencyCode = "1";
    req.WarehouseID = 1;            //Unique location for orders
    req.ShipMethodID = 1;
    req.PriceType = 1;              //Controls which price band to use
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
    req.Other11 = "1";
    req.Other12 = "1";
    req.Other13 = "1";
    req.Other14 = "1";
    req.Other15 = "1";
    req.Other16 = "1";
    req.Other17 = "1";
    req.Other18 = "1";
    req.Other19 = "1";
    req.Other20 = "1";
    req.OrderType = OrderType.Default;
    req.TransferVolumeToID = 1;     //Only pass in if you want volume to goto another CustomerID
    req.ReturnOrderID = 1;          //Unique numeric identifier for return order record.
    req.OverwriteExistingOrder = true;
    req.ExistingOrderID = 1;        //Unique numeric identifier for existing order record.
    req.PartyID = 1;

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
    req.SuppressPackSlipPrice = true;
    req.TransferVolumeToKey = "1";  //Only pass in if you want volume to goto another Customer Key
    req.ReturnOrderKey = "1";       //Unique alpha numeric identifier for customer record. Exeption will occur if ReturnOrderID & ReturnOrderKey are provided.
    req.ExistingOrderKey = "1";     //Unique alpha numeric identifier for existing order record. Exeption will occur if ExistingOrderID & ExistingOrderKey are provided.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if OrderID & OrderKey are provided.
    req.ReferralID = 1;             //Numeric identifier for the customer who owns the site from the order was created on, if apply.

    //Send Request to Server and Get Response
    var res = await api.CreateOrderAsync(req);

    //Now examine the results:
    Console.WriteLine("OrderID: {0}", res.OrderID);
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
    Console.WriteLine("HandlingFeeTotal: {0}", res.HandlingFeeTotal);

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
    Console.WriteLine("Warnings: {0}", res.Warnings);
    Console.WriteLine("OrderKey: {0}", res.OrderKey);
    Console.WriteLine("ReferralID: {0}", res.ReferralID);
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
    CreateOrderRequest req = new CreateOrderRequest();

    req.CustomerID = 1;             //Unique numeric identifier for a customer record.
    req.OrderStatus = OrderStatusType.Incomplete;
    req.OrderDate = DateTime.Today;
    req.CurrencyCode = "1";
    req.WarehouseID = 1;            //Unique location for orders
    req.ShipMethodID = 1;
    req.PriceType = 1;              //Controls which price band to use
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
    req.Other11 = "1";
    req.Other12 = "1";
    req.Other13 = "1";
    req.Other14 = "1";
    req.Other15 = "1";
    req.Other16 = "1";
    req.Other17 = "1";
    req.Other18 = "1";
    req.Other19 = "1";
    req.Other20 = "1";
    req.OrderType = OrderType.Default;
    req.TransferVolumeToID = 1;     //Only pass in if you want volume to goto another CustomerID
    req.ReturnOrderID = 1;          //Unique numeric identifier for return order record.
    req.OverwriteExistingOrder = true;
    req.ExistingOrderID = 1;        //Unique numeric identifier for existing order record.
    req.PartyID = 1;

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
    req.SuppressPackSlipPrice = true;
    req.TransferVolumeToKey = "1";  //Only pass in if you want volume to goto another Customer Key
    req.ReturnOrderKey = "1";       //Unique alpha numeric identifier for customer record. Exeption will occur if ReturnOrderID & ReturnOrderKey are provided.
    req.ExistingOrderKey = "1";     //Unique alpha numeric identifier for existing order record. Exeption will occur if ExistingOrderID & ExistingOrderKey are provided.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if OrderID & OrderKey are provided.
    req.ReferralID = 1;             //Numeric identifier for the customer who owns the site from the order was created on, if apply.

    //Send Request to Server and Get Response
    CreateOrderResponse res = api.CreateOrder(req);

    //Now examine the results:
    Console.WriteLine("OrderID: {0}", res.OrderID);
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
    Console.WriteLine("HandlingFeeTotal: {0}", res.HandlingFeeTotal);

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
    Console.WriteLine("Warnings: {0}", res.Warnings);
    Console.WriteLine("OrderKey: {0}", res.OrderKey);
    Console.WriteLine("ReferralID: {0}", res.ReferralID);
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
    Dim req as new CreateOrderRequest()

    req.CustomerID = 1
    req.OrderStatus = OrderStatusType.Incomplete
    req.OrderDate = DateTime.Today
    req.CurrencyCode = "1"
    req.WarehouseID = 1
    req.ShipMethodID = 1
    req.PriceType = 1
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
    req.Other11 = "1"
    req.Other12 = "1"
    req.Other13 = "1"
    req.Other14 = "1"
    req.Other15 = "1"
    req.Other16 = "1"
    req.Other17 = "1"
    req.Other18 = "1"
    req.Other19 = "1"
    req.Other20 = "1"
    req.OrderType = OrderType.Default
    req.TransferVolumeToID = 1
    req.ReturnOrderID = 1
    req.OverwriteExistingOrder = true
    req.ExistingOrderID = 1
    req.PartyID = 1

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
    req.SuppressPackSlipPrice = true
    req.TransferVolumeToKey = "1"
    req.ReturnOrderKey = "1"
    req.ExistingOrderKey = "1"
    req.CustomerKey = "1"
    req.ReferralID = 1

    'Send Request to Server and Get Response
    Dim res As CreateOrderResponse = api.CreateOrder(req)

    'Now examine the results:
    Console.WriteLine("OrderID: {0}", res.OrderID)
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
    Console.WriteLine("HandlingFeeTotal: {0}", res.HandlingFeeTotal)

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
    Console.WriteLine("Warnings: {0}", res.Warnings)
    Console.WriteLine("OrderKey: {0}", res.OrderKey)
    Console.WriteLine("ReferralID: {0}", res.ReferralID)
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
    $req->OrderStatus = 1;
    $req->OrderDate = 1;
    $req->CurrencyCode = "1";
    $req->WarehouseID = 1;
    $req->ShipMethodID = 1;
    $req->PriceType = 1;
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
    $req->Other11 = "1";
    $req->Other12 = "1";
    $req->Other13 = "1";
    $req->Other14 = "1";
    $req->Other15 = "1";
    $req->Other16 = "1";
    $req->Other17 = "1";
    $req->Other18 = "1";
    $req->Other19 = "1";
    $req->Other20 = "1";
    $req->OrderType = 1;
    $req->TransferVolumeToID = 1;
    $req->ReturnOrderID = 1;
    $req->OverwriteExistingOrder = 1;
    $req->ExistingOrderID = 1;
    $req->PartyID = 1;

    //Add Details

    $detail1->ItemCode = "1";
    $detail1->Quantity = 1;

    $detail2->ItemCode = "2";
    $detail2->Quantity = 2;

    //Now attach the list to the request
    req.Details = array(detail1,detail2);
    $req->SuppressPackSlipPrice = 1;
    $req->TransferVolumeToKey = "1";
    $req->ReturnOrderKey = "1";
    $req->ExistingOrderKey = "1";
    $req->CustomerKey = "1";
    $req->ReferralID = 1;

    //Send Request to Server and Get Response
    $res = $api.CreateOrder($req);

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
    CreateOrderRequest req = new CreateOrderRequest();

    req.setCustomerID(1);
    req.setOrderStatus(1);
    req.setOrderDate(1);
    req.setCurrencyCode("1");
    req.setWarehouseID(1);
    req.setShipMethodID(1);
    req.setPriceType(1);
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
    req.setOther11("1");
    req.setOther12("1");
    req.setOther13("1");
    req.setOther14("1");
    req.setOther15("1");
    req.setOther16("1");
    req.setOther17("1");
    req.setOther18("1");
    req.setOther19("1");
    req.setOther20("1");
    req.setOrderType(1);
    req.setTransferVolumeToID(1);
    req.setReturnOrderID(1);
    req.setOverwriteExistingOrder(1);
    req.setExistingOrderID(1);
    req.setPartyID(1);

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
    req.setSuppressPackSlipPrice(1);
    req.setTransferVolumeToKey("1");
    req.setReturnOrderKey("1");
    req.setExistingOrderKey("1");
    req.setCustomerKey("1");
    req.setReferralID(1);

    //Send Request to Server and Get Response
    CreateOrderResponse res = api.getExigoApiSoap().createOrder(req, auth);

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

### CreateOrderImport

>  Imports a new Order for an existing customer.
>  Use this for import routines or other instances where you wish to supply all calculation data.
>  It is advised to use CreateOrder unless you know the exact breakdown of all pricing, tax, shipping and volume info.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `POST /3.0/orders/import` |
| SOAP action | `https://api.exigo.com/CreateOrderImport` |
| WSDL elements | `CreateOrderImportRequest` → `CreateOrderImportResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateOrderImport |

#### Input

**`CreateOrderImportRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `FirstName` | `String` | Optional. |
| `LastName` | `String` | Optional. |
| `Company` | `String` | Optional. |
| `Phone` | `String` | Optional. |
| `Email` | `String` | Optional. |
| `ShipMethodID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| `Address1` | `String` | Optional. |
| `Address2` | `String` | Optional. |
| `Address3` | `String` | Optional. |
| `City` | `String` | Optional. |
| `State` | `String` | Optional. |
| `Zip` | `String` | Optional. |
| `Country` | `String` | Optional. |
| `County` | `String` | Optional. |
| `Notes` | `String` | Optional. |
| `WarehouseID` | `Int32` | Unique location for orders.<br>**Lookup:** company-specific list (see company-lists.md) |
| `CurrencyCode` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `ShippingStateTax` | `Decimal` |  |
| `ShippingFedTax` | `Decimal` |  |
| `ShippingCountyLocalTax` | `Decimal` |  |
| `ShippingCountyTax` | `Decimal` |  |
| `ShippingCityLocalTax` | `Decimal` |  |
| `ShippingCityTax` | `Decimal` |  |
| `Shipping` | `Decimal` |  |
| `PriceType` | `Int32` | Controls which price band to use.<br>**Lookup:** company-specific list (see company-lists.md) |
| `OrderStatus` | `OrderStatusType` | **Values:** `Incomplete`, `Pending`, `CCDeclined`, `ACHDeclined`, `Canceled`, `CCPending`, `ACHPending`, `Accepted`, `Printed`, `Shipped`, `PendingInventory` |
| `OrderDate` | `DateTime` |  |
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
| `OrderType` | `OrderType` | **Values:** `Default`, `CustomerService`, `ShoppingCart`, `WebWizard`, `AutoOrder`, `Import`, `BackOrder`, `ReplacementOrder`, `ReturnOrder`, `WebAutoOrder`, `TicketSystem`, `APIOrder`, `BackOrderParent`, `ChildOrder`, `Other1`, `Other2`, `Other3`, `Other4`, `Other5`, `Other6`, `Other7`, `Other8`, `Other9`, `Other10` |
| `UseManualOrderID` | `Boolean` | Optional. |
| `ManualOrderID` | `Int32` | Optional. Unique numeric identifier for new order record. |
| `ReturnOrderID` | `Int32` | Optional. Unique numeric identifier for return order record. |
| `OrderDetails` | `OrderImportDetail[]` |  |
| `PartyID` | `Int32` | Optional. |
| `ManualOrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided. |
| `ReturnOrderKey` | `String` | Optional. Unique alpha numeric identifier for return order record. Exeption will occur if ReturnOrderID & ReturnOrderKey are provided. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |
| `OverwriteExistingOrder` | `Boolean` |  |
| `ExistingOrderID` | `Int32` | Optional. Unique numeric identifier for existing order record. |
| `ExistingOrderKey` | `String` | Optional. Unique alpha numeric identifier for existing order record. Exeption will occur if ExistingOrderID & ExistingOrderKey are provided. |
| `IsCommissionable` | `Boolean` | Optional. . Defaults to True. |
| `HandlingFee` | `Decimal` | Optional. |
| `PreserveOrderCreateDate` | `Boolean` | Optional. Only if OverwriteExistingOrder == true, not update the CreateDate of the order. Defaults to False. |
| `ParentOrderID` | `Int32` | Optional. Unique numeric identifier for the Parent Order. Defaults to 0. |

**`OrderImportDetail`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `ParentItemCode` | `String` | Optional. |
| &nbsp;&nbsp;↳ `ItemCode` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Description` | `String` | Optional. |
| &nbsp;&nbsp;↳ `Qty` | `Decimal` |  |
| &nbsp;&nbsp;↳ `WeightEach` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CountyLocalTax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CountyTax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CityTax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `StateTax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `FedTax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `TaxablePriceEach` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CVEach` | `Decimal` |  |
| &nbsp;&nbsp;↳ `BVEach` | `Decimal` |  |
| &nbsp;&nbsp;↳ `PriceEach` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other10Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other9Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other8Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other7Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other6Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other5Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other4Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other3Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other2Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other1Each` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Reference1` | `String` | Optional. |
| &nbsp;&nbsp;↳ `CityLocalTax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `OrderLine` | `Int32` | Optional. |
| &nbsp;&nbsp;↳ `OrderDetailID` | `Guid` | Optional. |
| &nbsp;&nbsp;↳ `ParentOrderDetailID` | `Guid` | Optional. |

#### Output

**`CreateOrderImportResponse`**

| Property | Type | Notes |
|---|---|---|
| `OrderID` | `Int32` | Unique numeric identifier for order record. |
| `OrderKey` | `String` | Unique alpha numeric identifier for order record. |
| `DetailIDs` | `OrderDetailIDs[]` |  |

**`OrderDetailIDs`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `OrderDetailID` | `Guid` |  |
| &nbsp;&nbsp;↳ `ParentOrderDetailID` | `Guid` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/orders/import HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "firstName": "",
  "lastName": "",
  "company": "",
  "phone": "",
  "email": "",
  "shipMethodID": 1,
  "address1": "1",
  "address2": "1",
  "address3": "1",
  "city": "1",
  "state": "1",
  "zip": "1",
  "country": "1",
  "county": "1",
  "notes": "",
  "warehouseID": 1,
  "currencyCode": "usd",
  "shippingStateTax": null,
  "shippingFedTax": null,
  "shippingCountyLocalTax": null,
  "shippingCountyTax": null,
  "shippingCityLocalTax": null,
  "shippingCityTax": null,
  "shipping": null,
  "priceType": 1,
  "orderStatus": null,
  "orderDate": "2026-11-10T00:00:00-06:00",
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
  "orderType": null,
  "orderDetails": null,
  "partyID": 1,
  "manualOrderKey": "1",
  "returnOrderKey": "1",
  "customerKey": "1",
  "overwriteExistingOrder": true,
  "existingOrderID": 1,
  "existingOrderKey": "1",
  "isCommissionable": true,
  "handlingFee": null,
  "preserveOrderCreateDate": true,
  "parentOrderID": 1
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "orderID": 1,
  "orderKey": "",
  "detailIDs": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateOrderImport"

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
    <CreateOrderImportRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <FirstName>string</FirstName>
      <LastName>string</LastName>
      <Company>string</Company>
      <Phone>string</Phone>
      <Email>string</Email>
      <ShipMethodID>int</ShipMethodID>
      <Address1>string</Address1>
      <Address2>string</Address2>
      <Address3>string</Address3>
      <City>string</City>
      <State>string</State>
      <Zip>string</Zip>
      <Country>string</Country>
      <County>string</County>
      <Notes>string</Notes>
      <WarehouseID>int</WarehouseID>
      <CurrencyCode>string</CurrencyCode>
      <ShippingStateTax>decimal</ShippingStateTax>
      <ShippingFedTax>decimal</ShippingFedTax>
      <ShippingCountyLocalTax>decimal</ShippingCountyLocalTax>
      <ShippingCountyTax>decimal</ShippingCountyTax>
      <ShippingCityLocalTax>decimal</ShippingCityLocalTax>
      <ShippingCityTax>decimal</ShippingCityTax>
      <Shipping>decimal</Shipping>
      <PriceType>int</PriceType>
      <OrderStatus>Incomplete or Pending or CCDeclined or ACHDeclined or Canceled or CCPending or ACHPending or Accepted or Printed or Shipped or PendingInventory</OrderStatus>
      <OrderDate>dateTime</OrderDate>
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
      <OrderType>Default or CustomerService or ShoppingCart or WebWizard or AutoOrder or Import or BackOrder or ReplacementOrder or ReturnOrder or WebAutoOrder or TicketSystem or APIOrder or BackOrderParent or ChildOrder or Other1 or Other2 or Other3 or Other4 or Other5 or Other6 or Other7 or Other8 or Other9 or Other10</OrderType>
      <UseManualOrderID>boolean</UseManualOrderID>
      <ManualOrderID>int</ManualOrderID>
      <ReturnOrderID>int</ReturnOrderID>
      <OrderDetails>
        <OrderImportDetail>
          <ParentItemCode>string</ParentItemCode>
          <ItemCode>string</ItemCode>
          <Description>string</Description>
          <Qty>decimal</Qty>
          <WeightEach>decimal</WeightEach>
          <CountyLocalTax>decimal</CountyLocalTax>
          <CountyTax>decimal</CountyTax>
          <CityTax>decimal</CityTax>
          <StateTax>decimal</StateTax>
          <FedTax>decimal</FedTax>
          <TaxablePriceEach>decimal</TaxablePriceEach>
          <CVEach>decimal</CVEach>
          <BVEach>decimal</BVEach>
          <PriceEach>decimal</PriceEach>
          <Other10Each>decimal</Other10Each>
          <Other9Each>decimal</Other9Each>
          <Other8Each>decimal</Other8Each>
          <Other7Each>decimal</Other7Each>
          <Other6Each>decimal</Other6Each>
          <Other5Each>decimal</Other5Each>
          <Other4Each>decimal</Other4Each>
          <Other3Each>decimal</Other3Each>
          <Other2Each>decimal</Other2Each>
          <Other1Each>decimal</Other1Each>
          <Reference1>string</Reference1>
          <CityLocalTax>decimal</CityLocalTax>
          <OrderLine>int</OrderLine>
          <OrderDetailID>guid</OrderDetailID>
          <ParentOrderDetailID>guid</ParentOrderDetailID>
        </OrderImportDetail>
      </OrderDetails>
      <PartyID>int</PartyID>
      <ManualOrderKey>string</ManualOrderKey>
      <ReturnOrderKey>string</ReturnOrderKey>
      <CustomerKey>string</CustomerKey>
      <OverwriteExistingOrder>boolean</OverwriteExistingOrder>
      <ExistingOrderID>int</ExistingOrderID>
      <ExistingOrderKey>string</ExistingOrderKey>
      <IsCommissionable>boolean</IsCommissionable>
      <HandlingFee>decimal</HandlingFee>
      <PreserveOrderCreateDate>boolean</PreserveOrderCreateDate>
      <ParentOrderID>int</ParentOrderID>
    </CreateOrderImportRequest>
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
    <CreateOrderImportResult xmlns="http://api.exigo.com/">
      <OrderID>int</OrderID>
      <OrderKey>string</OrderKey>
      <DetailIDs>
        <OrderDetailIDs>
          <OrderDetailID>guid</OrderDetailID>
          <ParentOrderDetailID>guid</ParentOrderDetailID>
        </OrderDetailIDs>
      </DetailIDs>
    </CreateOrderImportResult>
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
    var req = new CreateOrderImportRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.FirstName = "1";
    req.LastName = "1";
    req.Company = "1";
    req.Phone = "1";
    req.Email = "1";
    req.ShipMethodID = 1;
    req.Address1 = "1";
    req.Address2 = "1";
    req.Address3 = "1";
    req.City = "1";
    req.State = "1";
    req.Zip = "1";
    req.Country = "1";
    req.County = "1";
    req.Notes = "1";
    req.WarehouseID = 1;            //Unique location for orders
    req.CurrencyCode = "usd";
    req.ShippingStateTax = 1;
    req.ShippingFedTax = 1;
    req.ShippingCountyLocalTax = 1;
    req.ShippingCountyTax = 1;
    req.ShippingCityLocalTax = 1;
    req.ShippingCityTax = 1;
    req.Shipping = 1;
    req.PriceType = 1;              //Controls which price band to use
    req.OrderStatus = OrderStatusType.Incomplete;
    req.OrderDate = DateTime.Today;
    req.Other11 = "1";
    req.Other12 = "1";
    req.Other13 = "1";
    req.Other14 = "1";
    req.Other15 = "1";
    req.Other16 = "1";
    req.Other17 = "1";
    req.Other18 = "1";
    req.Other19 = "1";
    req.Other20 = "1";
    req.OrderType = OrderType.Default;

    //Add OrderDetails
    var orderdetails = new List<OrderImportDetail>();

    var orderDetail1 = new OrderImportDetail();
    orderDetail1.ParentItemCode = "1";
    orderDetail1.ItemCode = "1";
    orderDetail1.Description = "1";
    orderDetail1.Qty = 1;
    orderDetail1.WeightEach = 1;
    orderDetail1.CountyLocalTax = 1;
    orderDetail1.CountyTax = 1;
    orderDetail1.CityTax = 1;
    orderDetail1.StateTax = 1;
    orderDetail1.FedTax = 1;
    orderDetail1.TaxablePriceEach = 1;
    orderDetail1.CVEach = 1;
    orderDetail1.BVEach = 1;
    orderDetail1.PriceEach = 1;
    orderDetail1.Other10Each = 1;
    orderDetail1.Other9Each = 1;
    orderDetail1.Other8Each = 1;
    orderDetail1.Other7Each = 1;
    orderDetail1.Other6Each = 1;
    orderDetail1.Other5Each = 1;
    orderDetail1.Other4Each = 1;
    orderDetail1.Other3Each = 1;
    orderDetail1.Other2Each = 1;
    orderDetail1.Other1Each = 1;
    orderDetail1.Reference1 = "1";
    orderDetail1.CityLocalTax = 1;
    orderDetail1.OrderLine = 1;
    orderDetail1.OrderDetailID = 1;
    orderDetail1.ParentOrderDetailID = 1;
    orderdetails.Add(orderDetail1);

    var orderDetail2 = new OrderImportDetail();
    orderDetail2.ParentItemCode = "2";
    orderDetail2.ItemCode = "2";
    orderDetail2.Description = "2";
    orderDetail2.Qty = 2;
    orderDetail2.WeightEach = 2;
    orderDetail2.CountyLocalTax = 2;
    orderDetail2.CountyTax = 2;
    orderDetail2.CityTax = 2;
    orderDetail2.StateTax = 2;
    orderDetail2.FedTax = 2;
    orderDetail2.TaxablePriceEach = 2;
    orderDetail2.CVEach = 2;
    orderDetail2.BVEach = 2;
    orderDetail2.PriceEach = 2;
    orderDetail2.Other10Each = 2;
    orderDetail2.Other9Each = 2;
    orderDetail2.Other8Each = 2;
    orderDetail2.Other7Each = 2;
    orderDetail2.Other6Each = 2;
    orderDetail2.Other5Each = 2;
    orderDetail2.Other4Each = 2;
    orderDetail2.Other3Each = 2;
    orderDetail2.Other2Each = 2;
    orderDetail2.Other1Each = 2;
    orderDetail2.Reference1 = "2";
    orderDetail2.CityLocalTax = 2;
    orderDetail2.OrderLine = 2;
    orderDetail2.OrderDetailID = 2;
    orderDetail2.ParentOrderDetailID = 2;
    orderdetails.Add(orderDetail2);

    //Now attach the list to the request
    req.OrderDetails = orderdetails.ToArray();
    req.PartyID = 1;
    req.ManualOrderKey = "1";       //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.
    req.ReturnOrderKey = "1";       //Unique alpha numeric identifier for return order record. Exeption will occur if ReturnOrderID & ReturnOrderKey are provided.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.OverwriteExistingOrder = true;
    req.ExistingOrderID = 1;        //Unique numeric identifier for existing order record.
    req.ExistingOrderKey = "1";     //Unique alpha numeric identifier for existing order record. Exeption will occur if ExistingOrderID & ExistingOrderKey are provided.
    req.IsCommissionable = true;
    req.HandlingFee = 1;
    req.PreserveOrderCreateDate = true;//Only if OverwriteExistingOrder == true, not update the CreateDate of the order
    req.ParentOrderID = 1;          //Unique numeric identifier for the Parent Order.

    //Send Request to Server and Get Response
    var res = await api.CreateOrderImportAsync(req);

    //Now examine the results:
    Console.WriteLine("OrderID: {0}", res.OrderID);
    Console.WriteLine("OrderKey: {0}", res.OrderKey);

    foreach (var orderDetailIDs  in res.DetailIDs)
    {
        Console.WriteLine("OrderDetailID: {0}", orderDetailIDs.OrderDetailID);
        Console.WriteLine("ParentOrderDetailID: {0}", orderDetailIDs.ParentOrderDetailID);
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
    CreateOrderImportRequest req = new CreateOrderImportRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.FirstName = "1";
    req.LastName = "1";
    req.Company = "1";
    req.Phone = "1";
    req.Email = "1";
    req.ShipMethodID = 1;
    req.Address1 = "1";
    req.Address2 = "1";
    req.Address3 = "1";
    req.City = "1";
    req.State = "1";
    req.Zip = "1";
    req.Country = "1";
    req.County = "1";
    req.Notes = "1";
    req.WarehouseID = 1;            //Unique location for orders
    req.CurrencyCode = "usd";
    req.ShippingStateTax = 1;
    req.ShippingFedTax = 1;
    req.ShippingCountyLocalTax = 1;
    req.ShippingCountyTax = 1;
    req.ShippingCityLocalTax = 1;
    req.ShippingCityTax = 1;
    req.Shipping = 1;
    req.PriceType = 1;              //Controls which price band to use
    req.OrderStatus = OrderStatusType.Incomplete;
    req.OrderDate = DateTime.Today;
    req.Other11 = "1";
    req.Other12 = "1";
    req.Other13 = "1";
    req.Other14 = "1";
    req.Other15 = "1";
    req.Other16 = "1";
    req.Other17 = "1";
    req.Other18 = "1";
    req.Other19 = "1";
    req.Other20 = "1";
    req.OrderType = OrderType.Default;

    //Add OrderDetails
    List<OrderImportDetail> orderdetails = new List<OrderImportDetail>();

    OrderImportDetail orderDetail1 = new OrderImportDetail();
    orderDetail1.ParentItemCode = "1";
    orderDetail1.ItemCode = "1";
    orderDetail1.Description = "1";
    orderDetail1.Qty = 1;
    orderDetail1.WeightEach = 1;
    orderDetail1.CountyLocalTax = 1;
    orderDetail1.CountyTax = 1;
    orderDetail1.CityTax = 1;
    orderDetail1.StateTax = 1;
    orderDetail1.FedTax = 1;
    orderDetail1.TaxablePriceEach = 1;
    orderDetail1.CVEach = 1;
    orderDetail1.BVEach = 1;
    orderDetail1.PriceEach = 1;
    orderDetail1.Other10Each = 1;
    orderDetail1.Other9Each = 1;
    orderDetail1.Other8Each = 1;
    orderDetail1.Other7Each = 1;
    orderDetail1.Other6Each = 1;
    orderDetail1.Other5Each = 1;
    orderDetail1.Other4Each = 1;
    orderDetail1.Other3Each = 1;
    orderDetail1.Other2Each = 1;
    orderDetail1.Other1Each = 1;
    orderDetail1.Reference1 = "1";
    orderDetail1.CityLocalTax = 1;
    orderDetail1.OrderLine = 1;
    orderDetail1.OrderDetailID = 1;
    orderDetail1.ParentOrderDetailID = 1;
    orderdetails.Add(orderDetail1);

    OrderImportDetail orderDetail2 = new OrderImportDetail();
    orderDetail2.ParentItemCode = "2";
    orderDetail2.ItemCode = "2";
    orderDetail2.Description = "2";
    orderDetail2.Qty = 2;
    orderDetail2.WeightEach = 2;
    orderDetail2.CountyLocalTax = 2;
    orderDetail2.CountyTax = 2;
    orderDetail2.CityTax = 2;
    orderDetail2.StateTax = 2;
    orderDetail2.FedTax = 2;
    orderDetail2.TaxablePriceEach = 2;
    orderDetail2.CVEach = 2;
    orderDetail2.BVEach = 2;
    orderDetail2.PriceEach = 2;
    orderDetail2.Other10Each = 2;
    orderDetail2.Other9Each = 2;
    orderDetail2.Other8Each = 2;
    orderDetail2.Other7Each = 2;
    orderDetail2.Other6Each = 2;
    orderDetail2.Other5Each = 2;
    orderDetail2.Other4Each = 2;
    orderDetail2.Other3Each = 2;
    orderDetail2.Other2Each = 2;
    orderDetail2.Other1Each = 2;
    orderDetail2.Reference1 = "2";
    orderDetail2.CityLocalTax = 2;
    orderDetail2.OrderLine = 2;
    orderDetail2.OrderDetailID = 2;
    orderDetail2.ParentOrderDetailID = 2;
    orderdetails.Add(orderDetail2);

    //Now attach the list to the request
    req.OrderDetails = orderdetails.ToArray();
    req.PartyID = 1;
    req.ManualOrderKey = "1";       //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.
    req.ReturnOrderKey = "1";       //Unique alpha numeric identifier for return order record. Exeption will occur if ReturnOrderID & ReturnOrderKey are provided.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.OverwriteExistingOrder = true;
    req.ExistingOrderID = 1;        //Unique numeric identifier for existing order record.
    req.ExistingOrderKey = "1";     //Unique alpha numeric identifier for existing order record. Exeption will occur if ExistingOrderID & ExistingOrderKey are provided.
    req.IsCommissionable = true;
    req.HandlingFee = 1;
    req.PreserveOrderCreateDate = true;//Only if OverwriteExistingOrder == true, not update the CreateDate of the order
    req.ParentOrderID = 1;          //Unique numeric identifier for the Parent Order.

    //Send Request to Server and Get Response
    CreateOrderImportResponse res = api.CreateOrderImport(req);

    //Now examine the results:
    Console.WriteLine("OrderID: {0}", res.OrderID);
    Console.WriteLine("OrderKey: {0}", res.OrderKey);

    foreach (OrderDetailIDs orderDetailIDs  in res.DetailIDs)
    {
        Console.WriteLine("OrderDetailID: {0}", orderDetailIDs.OrderDetailID);
        Console.WriteLine("ParentOrderDetailID: {0}", orderDetailIDs.ParentOrderDetailID);
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
    Dim req as new CreateOrderImportRequest()

    req.CustomerID = 1
    req.FirstName = "1"
    req.LastName = "1"
    req.Company = "1"
    req.Phone = "1"
    req.Email = "1"
    req.ShipMethodID = 1
    req.Address1 = "1"
    req.Address2 = "1"
    req.Address3 = "1"
    req.City = "1"
    req.State = "1"
    req.Zip = "1"
    req.Country = "1"
    req.County = "1"
    req.Notes = "1"
    req.WarehouseID = 1
    req.CurrencyCode = "usd"
    req.ShippingStateTax = 1
    req.ShippingFedTax = 1
    req.ShippingCountyLocalTax = 1
    req.ShippingCountyTax = 1
    req.ShippingCityLocalTax = 1
    req.ShippingCityTax = 1
    req.Shipping = 1
    req.PriceType = 1
    req.OrderStatus = OrderStatusType.Incomplete
    req.OrderDate = DateTime.Today
    req.Other11 = "1"
    req.Other12 = "1"
    req.Other13 = "1"
    req.Other14 = "1"
    req.Other15 = "1"
    req.Other16 = "1"
    req.Other17 = "1"
    req.Other18 = "1"
    req.Other19 = "1"
    req.Other20 = "1"
    req.OrderType = OrderType.Default

    'Add OrderDetails
    Dim orderdetails As New List(Of OrderImportDetail)()

    Dim orderDetail1 as new OrderImportDetail()
    orderDetail1.ParentItemCode = "1"
    orderDetail1.ItemCode = "1"
    orderDetail1.Description = "1"
    orderDetail1.Qty = 1
    orderDetail1.WeightEach = 1
    orderDetail1.CountyLocalTax = 1
    orderDetail1.CountyTax = 1
    orderDetail1.CityTax = 1
    orderDetail1.StateTax = 1
    orderDetail1.FedTax = 1
    orderDetail1.TaxablePriceEach = 1
    orderDetail1.CVEach = 1
    orderDetail1.BVEach = 1
    orderDetail1.PriceEach = 1
    orderDetail1.Other10Each = 1
    orderDetail1.Other9Each = 1
    orderDetail1.Other8Each = 1
    orderDetail1.Other7Each = 1
    orderDetail1.Other6Each = 1
    orderDetail1.Other5Each = 1
    orderDetail1.Other4Each = 1
    orderDetail1.Other3Each = 1
    orderDetail1.Other2Each = 1
    orderDetail1.Other1Each = 1
    orderDetail1.Reference1 = "1"
    orderDetail1.CityLocalTax = 1
    orderDetail1.OrderLine = 1
    orderDetail1.OrderDetailID = 1
    orderDetail1.ParentOrderDetailID = 1
    orderdetails.Add(orderDetail1)

    Dim orderDetail2 as new OrderImportDetail()
    orderDetail2.ParentItemCode = "2"
    orderDetail2.ItemCode = "2"
    orderDetail2.Description = "2"
    orderDetail2.Qty = 2
    orderDetail2.WeightEach = 2
    orderDetail2.CountyLocalTax = 2
    orderDetail2.CountyTax = 2
    orderDetail2.CityTax = 2
    orderDetail2.StateTax = 2
    orderDetail2.FedTax = 2
    orderDetail2.TaxablePriceEach = 2
    orderDetail2.CVEach = 2
    orderDetail2.BVEach = 2
    orderDetail2.PriceEach = 2
    orderDetail2.Other10Each = 2
    orderDetail2.Other9Each = 2
    orderDetail2.Other8Each = 2
    orderDetail2.Other7Each = 2
    orderDetail2.Other6Each = 2
    orderDetail2.Other5Each = 2
    orderDetail2.Other4Each = 2
    orderDetail2.Other3Each = 2
    orderDetail2.Other2Each = 2
    orderDetail2.Other1Each = 2
    orderDetail2.Reference1 = "2"
    orderDetail2.CityLocalTax = 2
    orderDetail2.OrderLine = 2
    orderDetail2.OrderDetailID = 2
    orderDetail2.ParentOrderDetailID = 2
    orderdetails.Add(orderDetail2)

    'Now attach the list to the request
    req.OrderDetails = orderdetails.ToArray()
    req.PartyID = 1
    req.ManualOrderKey = "1"
    req.ReturnOrderKey = "1"
    req.CustomerKey = "1"
    req.OverwriteExistingOrder = true
    req.ExistingOrderID = 1
    req.ExistingOrderKey = "1"
    req.IsCommissionable = true
    req.HandlingFee = 1
    req.PreserveOrderCreateDate = true
    req.ParentOrderID = 1

    'Send Request to Server and Get Response
    Dim res As CreateOrderImportResponse = api.CreateOrderImport(req)

    'Now examine the results:
    Console.WriteLine("OrderID: {0}", res.OrderID)
    Console.WriteLine("OrderKey: {0}", res.OrderKey)

    For Each orderDetailIDs As OrderDetailIDs In res.DetailIDs
        Console.WriteLine("OrderDetailID: {0}", orderDetailIDs.OrderDetailID)
        Console.WriteLine("ParentOrderDetailID: {0}", orderDetailIDs.ParentOrderDetailID)
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
    $req->FirstName = "1";
    $req->LastName = "1";
    $req->Company = "1";
    $req->Phone = "1";
    $req->Email = "1";
    $req->ShipMethodID = 1;
    $req->Address1 = "1";
    $req->Address2 = "1";
    $req->Address3 = "1";
    $req->City = "1";
    $req->State = "1";
    $req->Zip = "1";
    $req->Country = "1";
    $req->County = "1";
    $req->Notes = "1";
    $req->WarehouseID = 1;
    $req->CurrencyCode = "usd";
    $req->ShippingStateTax = 1;
    $req->ShippingFedTax = 1;
    $req->ShippingCountyLocalTax = 1;
    $req->ShippingCountyTax = 1;
    $req->ShippingCityLocalTax = 1;
    $req->ShippingCityTax = 1;
    $req->Shipping = 1;
    $req->PriceType = 1;
    $req->OrderStatus = 1;
    $req->OrderDate = 1;
    $req->Other11 = "1";
    $req->Other12 = "1";
    $req->Other13 = "1";
    $req->Other14 = "1";
    $req->Other15 = "1";
    $req->Other16 = "1";
    $req->Other17 = "1";
    $req->Other18 = "1";
    $req->Other19 = "1";
    $req->Other20 = "1";
    $req->OrderType = 1;

    //Add OrderDetails

    $orderDetail1->ParentItemCode = "1";
    $orderDetail1->ItemCode = "1";
    $orderDetail1->Description = "1";
    $orderDetail1->Qty = 1;
    $orderDetail1->WeightEach = 1;
    $orderDetail1->CountyLocalTax = 1;
    $orderDetail1->CountyTax = 1;
    $orderDetail1->CityTax = 1;
    $orderDetail1->StateTax = 1;
    $orderDetail1->FedTax = 1;
    $orderDetail1->TaxablePriceEach = 1;
    $orderDetail1->CVEach = 1;
    $orderDetail1->BVEach = 1;
    $orderDetail1->PriceEach = 1;
    $orderDetail1->Other10Each = 1;
    $orderDetail1->Other9Each = 1;
    $orderDetail1->Other8Each = 1;
    $orderDetail1->Other7Each = 1;
    $orderDetail1->Other6Each = 1;
    $orderDetail1->Other5Each = 1;
    $orderDetail1->Other4Each = 1;
    $orderDetail1->Other3Each = 1;
    $orderDetail1->Other2Each = 1;
    $orderDetail1->Other1Each = 1;
    $orderDetail1->Reference1 = "1";
    $orderDetail1->CityLocalTax = 1;
    $orderDetail1->OrderLine = 1;
    $orderDetail1->OrderDetailID = 1;
    $orderDetail1->ParentOrderDetailID = 1;

    $orderDetail2->ParentItemCode = "2";
    $orderDetail2->ItemCode = "2";
    $orderDetail2->Description = "2";
    $orderDetail2->Qty = 2;
    $orderDetail2->WeightEach = 2;
    $orderDetail2->CountyLocalTax = 2;
    $orderDetail2->CountyTax = 2;
    $orderDetail2->CityTax = 2;
    $orderDetail2->StateTax = 2;
    $orderDetail2->FedTax = 2;
    $orderDetail2->TaxablePriceEach = 2;
    $orderDetail2->CVEach = 2;
    $orderDetail2->BVEach = 2;
    $orderDetail2->PriceEach = 2;
    $orderDetail2->Other10Each = 2;
    $orderDetail2->Other9Each = 2;
    $orderDetail2->Other8Each = 2;
    $orderDetail2->Other7Each = 2;
    $orderDetail2->Other6Each = 2;
    $orderDetail2->Other5Each = 2;
    $orderDetail2->Other4Each = 2;
    $orderDetail2->Other3Each = 2;
    $orderDetail2->Other2Each = 2;
    $orderDetail2->Other1Each = 2;
    $orderDetail2->Reference1 = "2";
    $orderDetail2->CityLocalTax = 2;
    $orderDetail2->OrderLine = 2;
    $orderDetail2->OrderDetailID = 2;
    $orderDetail2->ParentOrderDetailID = 2;

    //Now attach the list to the request
    req.OrderDetails = array(orderDetail1,orderDetail2);
    $req->PartyID = 1;
    $req->ManualOrderKey = "1";
    $req->ReturnOrderKey = "1";
    $req->CustomerKey = "1";
    $req->OverwriteExistingOrder = 1;
    $req->ExistingOrderID = 1;
    $req->ExistingOrderKey = "1";
    $req->IsCommissionable = 1;
    $req->HandlingFee = 1;
    $req->PreserveOrderCreateDate = 1;
    $req->ParentOrderID = 1;

    //Send Request to Server and Get Response
    $res = $api.CreateOrderImport($req);

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
    CreateOrderImportRequest req = new CreateOrderImportRequest();

    req.setCustomerID(1);
    req.setFirstName("1");
    req.setLastName("1");
    req.setCompany("1");
    req.setPhone("1");
    req.setEmail("1");
    req.setShipMethodID(1);
    req.setAddress1("1");
    req.setAddress2("1");
    req.setAddress3("1");
    req.setCity("1");
    req.setState("1");
    req.setZip("1");
    req.setCountry("1");
    req.setCounty("1");
    req.setNotes("1");
    req.setWarehouseID(1);
    req.setCurrencyCode("usd");
    req.setShippingStateTax(1);
    req.setShippingFedTax(1);
    req.setShippingCountyLocalTax(1);
    req.setShippingCountyTax(1);
    req.setShippingCityLocalTax(1);
    req.setShippingCityTax(1);
    req.setShipping(1);
    req.setPriceType(1);
    req.setOrderStatus(1);
    req.setOrderDate(1);
    req.setOther11("1");
    req.setOther12("1");
    req.setOther13("1");
    req.setOther14("1");
    req.setOther15("1");
    req.setOther16("1");
    req.setOther17("1");
    req.setOther18("1");
    req.setOther19("1");
    req.setOther20("1");
    req.setOrderType(1);

    //Add OrderDetails
    ArrayOfOrderImportDetail orderdetails = new ArrayOfOrderImportDetail();

    OrderImportDetail orderDetail1 = new OrderImportDetail();
    orderDetail1.setParentItemCode("1");
    orderDetail1.setItemCode("1");
    orderDetail1.setDescription("1");
    orderDetail1.setQty(1);
    orderDetail1.setWeightEach(1);
    orderDetail1.setCountyLocalTax(1);
    orderDetail1.setCountyTax(1);
    orderDetail1.setCityTax(1);
    orderDetail1.setStateTax(1);
    orderDetail1.setFedTax(1);
    orderDetail1.setTaxablePriceEach(1);
    orderDetail1.setCVEach(1);
    orderDetail1.setBVEach(1);
    orderDetail1.setPriceEach(1);
    orderDetail1.setOther10Each(1);
    orderDetail1.setOther9Each(1);
    orderDetail1.setOther8Each(1);
    orderDetail1.setOther7Each(1);
    orderDetail1.setOther6Each(1);
    orderDetail1.setOther5Each(1);
    orderDetail1.setOther4Each(1);
    orderDetail1.setOther3Each(1);
    orderDetail1.setOther2Each(1);
    orderDetail1.setOther1Each(1);
    orderDetail1.setReference1("1");
    orderDetail1.setCityLocalTax(1);
    orderDetail1.setOrderLine(1);
    orderDetail1.setOrderDetailID(1);
    orderDetail1.setParentOrderDetailID(1);
    orderdetails.Add(orderDetail1);

    OrderImportDetail orderDetail2 = new OrderImportDetail();
    orderDetail2.setParentItemCode("2");
    orderDetail2.setItemCode("2");
    orderDetail2.setDescription("2");
    orderDetail2.setQty(2);
    orderDetail2.setWeightEach(2);
    orderDetail2.setCountyLocalTax(2);
    orderDetail2.setCountyTax(2);
    orderDetail2.setCityTax(2);
    orderDetail2.setStateTax(2);
    orderDetail2.setFedTax(2);
    orderDetail2.setTaxablePriceEach(2);
    orderDetail2.setCVEach(2);
    orderDetail2.setBVEach(2);
    orderDetail2.setPriceEach(2);
    orderDetail2.setOther10Each(2);
    orderDetail2.setOther9Each(2);
    orderDetail2.setOther8Each(2);
    orderDetail2.setOther7Each(2);
    orderDetail2.setOther6Each(2);
    orderDetail2.setOther5Each(2);
    orderDetail2.setOther4Each(2);
    orderDetail2.setOther3Each(2);
    orderDetail2.setOther2Each(2);
    orderDetail2.setOther1Each(2);
    orderDetail2.setReference1("2");
    orderDetail2.setCityLocalTax(2);
    orderDetail2.setOrderLine(2);
    orderDetail2.setOrderDetailID(2);
    orderDetail2.setParentOrderDetailID(2);
    orderdetails.Add(orderDetail2);

    //Now attach the list to the request
    req.setOrderDetails(orderdetails);
    req.setPartyID(1);
    req.setManualOrderKey("1");
    req.setReturnOrderKey("1");
    req.setCustomerKey("1");
    req.setOverwriteExistingOrder(1);
    req.setExistingOrderID(1);
    req.setExistingOrderKey("1");
    req.setIsCommissionable(1);
    req.setHandlingFee(1);
    req.setPreserveOrderCreateDate(1);
    req.setParentOrderID(1);

    //Send Request to Server and Get Response
    CreateOrderImportResponse res = api.getExigoApiSoap().createOrderImport(req, auth);

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

### UpdateOrder

> Updates one or more fields on an existing order. Can participate in a transaction.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `PATCH /3.0/orders` |
| SOAP action | `https://api.exigo.com/UpdateOrder` |
| WSDL elements | `UpdateOrderRequest` → `UpdateOrderResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateOrder |

#### Input

**`UpdateOrderRequest`**

| Property | Type | Notes |
|---|---|---|
| `OrderID` | `Int32` | Unique numeric identifier for order record. |
| `OrderDate` | `DateTime` | Optional. |
| `DeclineCount` | `Int32` | Optional. |
| `OrderTy` | `Int32` | Optional. |
| `OrderStatus` | `Int32` | Optional. |
| `PriceTy` | `Int32` | Optional. Controls which price band to use.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Total` | `Decimal` | Optional. |
| `SubTotal` | `Decimal` | Optional. |
| `Shipping` | `Decimal` | Optional. |
| `OrderTax` | `Decimal` | Optional. |
| `ShippingTax` | `Decimal` | Optional. |
| `FedShippingTax` | `Decimal` | Optional. |
| `StateShippingTax` | `Decimal` | Optional. |
| `CityShippingTax` | `Decimal` | Optional. |
| `CityLocalShippingTax` | `Decimal` | Optional. |
| `CountyShippingTax` | `Decimal` | Optional. |
| `CountyLocalShippingTax` | `Decimal` | Optional. |
| `ManualTaxRate` | `Decimal` | Optional. |
| `TotalTax` | `Decimal` | Optional. |
| `CurrencyCode` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `PaymentMethod` | `Int32` | Optional. |
| `WarehouseID` | `Int32` | Optional. Unique location for orders.<br>**Lookup:** company-specific list (see company-lists.md) |
| `BatchID` | `Int32` | Optional. |
| `PreviousBalance` | `Decimal` | Optional. |
| `OverrideShipping` | `Boolean` | Optional. |
| `OverrideTax` | `Boolean` | Optional. |
| `BusinessVolume` | `Decimal` | Optional. Price amount. |
| `CommissionableVolume` | `Decimal` | Optional. Price amount. |
| `Other1` | `Decimal` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other2` | `Decimal` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other3` | `Decimal` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other4` | `Decimal` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other5` | `Decimal` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Discount` | `Decimal` | Optional. |
| `DiscountPercent` | `Decimal` | Optional. |
| `Weight` | `Decimal` | Optional. |
| `Sourcety` | `Int32` | Optional. |
| `Notes` | `String` | Optional. |
| `Usr` | `String` | Optional. |
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
| `SuppressPackSlipPrice` | `Boolean` | Optional. |
| `ShipMethodID` | `Int32` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `AutoOrderID` | `Int32` | Optional. |
| `CreatedBy` | `String` | Optional. |
| `ReturnOrderID` | `Int32` | Optional. Unique numeric identifier for transfer to order record. |
| `OrderRankID` | `Int32` | Optional. |
| `OrderPayRankID` | `Int32` | Optional. |
| `AddressIsVerified` | `Boolean` | Optional. |
| `County` | `String` | Optional. |
| `IsRMA` | `Boolean` | Optional. |
| `BackOrderFromID` | `Int32` | Optional. Unique numeric identifier for transfer to order record. |
| `CreditsEarned` | `Decimal` | Optional. |
| `TotalFedTax` | `Decimal` | Optional. |
| `TotalStateTax` | `Decimal` | Optional. |
| `ManualShippingTax` | `Decimal` | Optional. |
| `ReplacementOrderID` | `Int32` | Optional. Unique numeric identifier for transfer to order record. |
| `LockedDate` | `DateTime` | Optional. |
| `CommissionedDate` | `DateTime` | Optional. |
| `Flag1` | `Boolean` | Optional. |
| `Flag2` | `Boolean` | Optional. |
| `Flag3` | `Boolean` | Optional. |
| `Other6` | `Decimal` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other7` | `Decimal` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other8` | `Decimal` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other9` | `Decimal` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other10` | `Decimal` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `OriginalWarehouseID` | `Int32` | Optional. |
| `PickupName` | `String` | Optional. |
| `TransferToID` | `Int32` | Optional. Unique numeric identifier for transfer to order record. |
| `IsCommissionable` | `Boolean` | Optional. |
| `FulfilledBy` | `String` | Optional. |
| `CreditApplied` | `Decimal` | Optional. |
| `ShippedDate` | `DateTime` | Optional. |
| `TaxLockDate` | `DateTime` | Optional. |
| `TotalTaxable` | `Decimal` | Optional. |
| `ReturnCategoryID` | `Int32` | Optional. |
| `ReplacementCategoryID` | `Int32` | Optional. |
| `CalculatedShipping` | `Decimal` | Optional. |
| `HandlingFee` | `Decimal` | Optional. |
| `OrderProcessTy` | `Int32` | Optional. |
| `ActualCarrier` | `Int32` | Optional. |
| `ParentOrderID` | `Int32` | Optional. Unique numeric identifier for transfer to order record. |
| `CustomerTy` | `Int32` | Optional. Classification of a customer as defined by the company.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Reference` | `String` | Optional. |
| `MiddleName` | `String` | Optional. |
| `NameSuffix` | `String` | Optional. |
| `Address3` | `String` | Optional. |
| `PartyID` | `Int32` | Optional. |
| `TrackingNumber1` | `String` | Optional. |
| `TrackingNumber2` | `String` | Optional. |
| `TrackingNumber3` | `String` | Optional. |
| `TrackingNumber4` | `String` | Optional. |
| `TrackingNumber5` | `String` | Optional. |
| `WebCarrierID` | `OrderShipCarrier` | Optional.<br>**Values:** `FedEx`, `UPS`, `Purolator`, `CanadaPostRegular`, `CanadaPostExpress`, `DHL`, `USPS`, `Estafeta`, `RoyalMail`, `GLSHungary`, `PostenNorway`, `LandMarkGlobal`, `GDEX` |
| `WebCarrierID2` | `OrderShipCarrier` | Optional.<br>**Values:** `FedEx`, `UPS`, `Purolator`, `CanadaPostRegular`, `CanadaPostExpress`, `DHL`, `USPS`, `Estafeta`, `RoyalMail`, `GLSHungary`, `PostenNorway`, `LandMarkGlobal`, `GDEX` |
| `WebCarrierID3` | `OrderShipCarrier` | Optional.<br>**Values:** `FedEx`, `UPS`, `Purolator`, `CanadaPostRegular`, `CanadaPostExpress`, `DHL`, `USPS`, `Estafeta`, `RoyalMail`, `GLSHungary`, `PostenNorway`, `LandMarkGlobal`, `GDEX` |
| `WebCarrierID4` | `OrderShipCarrier` | Optional.<br>**Values:** `FedEx`, `UPS`, `Purolator`, `CanadaPostRegular`, `CanadaPostExpress`, `DHL`, `USPS`, `Estafeta`, `RoyalMail`, `GLSHungary`, `PostenNorway`, `LandMarkGlobal`, `GDEX` |
| `WebCarrierID5` | `OrderShipCarrier` | Optional.<br>**Values:** `FedEx`, `UPS`, `Purolator`, `CanadaPostRegular`, `CanadaPostExpress`, `DHL`, `USPS`, `Estafeta`, `RoyalMail`, `GLSHungary`, `PostenNorway`, `LandMarkGlobal`, `GDEX` |
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
| `TransferToKey` | `String` | Optional. Unique alpha numeric identifier for transfer to order record. Exeption will occur if TransferToID & TransferToKey are provided. |
| `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided. |
| `ReturnOrderKey` | `String` | Optional. Unique alpha numeric identifier for transfer to order record. Exeption will occur if ReturnOrderID & ReturnOrderKey are provided. |
| `ReplacementOrderKey` | `String` | Optional. Unique alpha numeric identifier for transfer to order record. Exeption will occur if ReplacementOrderID & ReplacementOrderKey are provided. |
| `ParentOrderKey` | `String` | Optional. Unique alpha numeric identifier for transfer to order record. Exeption will occur if ParentOrderID & ParentOrderKey are provided. |
| `BackOrderFromKey` | `String` | Optional. Unique alpha numeric identifier for transfer to order record. Exeption will occur if BackOrderFromID & BackOrderFromKey are provided. |
| `OrderSubStatusTy` | `Int32` | Optional. Optional Order Sub-Status Type (Set 0 to remove it from the Order.<br>**Lookup:** company-specific list (see company-lists.md) |

#### Output

**`UpdateOrderResponse`**

_No properties._

#### REST example

```http
PATCH https://yourcompany-api.exigo.com/3.0/orders HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "orderID": 1,
  "orderDate": "2026-11-10T00:00:00-06:00",
  "declineCount": 1,
  "orderTy": 1,
  "orderStatus": 1,
  "priceTy": 1,
  "total": null,
  "subTotal": null,
  "shipping": null,
  "orderTax": null,
  "shippingTax": null,
  "fedShippingTax": null,
  "stateShippingTax": null,
  "cityShippingTax": null,
  "cityLocalShippingTax": null,
  "countyShippingTax": null,
  "countyLocalShippingTax": null,
  "manualTaxRate": null,
  "totalTax": null,
  "currencyCode": null,
  "paymentMethod": 1,
  "warehouseID": 1,
  "batchID": 1,
  "previousBalance": null,
  "overrideShipping": true,
  "overrideTax": true,
  "businessVolume": null,
  "commissionableVolume": null,
  "discount": null,
  "discountPercent": null,
  "weight": null,
  "sourcety": 1,
  "notes": null,
  "usr": null,
  "firstName": null,
  "lastName": null,
  "company": null,
  "address1": null,
  "address2": null,
  "city": null,
  "zip": null,
  "email": null,
  "phone": null,
  "suppressPackSlipPrice": true,
  "shipMethodID": 1,
  "autoOrderID": 1,
  "createdBy": null,
  "returnOrderID": 1,
  "orderRankID": 1,
  "orderPayRankID": 1,
  "addressIsVerified": true,
  "county": null,
  "isRMA": true,
  "backOrderFromID": 1,
  "creditsEarned": null,
  "totalFedTax": null,
  "totalStateTax": null,
  "manualShippingTax": null,
  "replacementOrderID": 1,
  "lockedDate": "2026-11-10T00:00:00-06:00",
  "commissionedDate": "2026-11-10T00:00:00-06:00",
  "flag1": true,
  "flag2": true,
  "flag3": true,
  "originalWarehouseID": 1,
  "pickupName": null,
  "transferToID": 1,
  "isCommissionable": true,
  "fulfilledBy": null,
  "creditApplied": null,
  "shippedDate": "2026-11-10T00:00:00-06:00",
  "taxLockDate": "2026-11-10T00:00:00-06:00",
  "totalTaxable": null,
  "returnCategoryID": 1,
  "replacementCategoryID": 1,
  "calculatedShipping": null,
  "handlingFee": null,
  "orderProcessTy": 1,
  "actualCarrier": 1,
  "parentOrderID": 1,
  "customerTy": 1,
  "reference": null,
  "middleName": null,
  "nameSuffix": null,
  "address3": null,
  "partyID": 1,
  "trackingNumber1": null,
  "trackingNumber2": null,
  "trackingNumber3": null,
  "trackingNumber4": null,
  "trackingNumber5": null,
  "webCarrierID": null,
  "webCarrierID2": null,
  "webCarrierID3": null,
  "webCarrierID4": null,
  "webCarrierID5": null,
  "other11": null,
  "other12": null,
  "other13": null,
  "other14": null,
  "other15": null,
  "other16": null,
  "other17": null,
  "other18": null,
  "other19": null,
  "other20": null,
  "transferToKey": "1",
  "orderKey": "DDks8235txcid",
  "returnOrderKey": "1",
  "replacementOrderKey": "1",
  "parentOrderKey": "1",
  "backOrderFromKey": "1"
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
SOAPAction: "https://api.exigo.com/UpdateOrder"

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
    <UpdateOrderRequest xmlns="http://api.exigo.com/">
      <OrderID>int</OrderID>
      <OrderDate>dateTime</OrderDate>
      <DeclineCount>int</DeclineCount>
      <OrderTy>int</OrderTy>
      <OrderStatus>int</OrderStatus>
      <PriceTy>int</PriceTy>
      <Total>decimal</Total>
      <SubTotal>decimal</SubTotal>
      <Shipping>decimal</Shipping>
      <OrderTax>decimal</OrderTax>
      <ShippingTax>decimal</ShippingTax>
      <FedShippingTax>decimal</FedShippingTax>
      <StateShippingTax>decimal</StateShippingTax>
      <CityShippingTax>decimal</CityShippingTax>
      <CityLocalShippingTax>decimal</CityLocalShippingTax>
      <CountyShippingTax>decimal</CountyShippingTax>
      <CountyLocalShippingTax>decimal</CountyLocalShippingTax>
      <ManualTaxRate>decimal</ManualTaxRate>
      <TotalTax>decimal</TotalTax>
      <CurrencyCode>string</CurrencyCode>
      <PaymentMethod>int</PaymentMethod>
      <WarehouseID>int</WarehouseID>
      <BatchID>int</BatchID>
      <PreviousBalance>decimal</PreviousBalance>
      <OverrideShipping>boolean</OverrideShipping>
      <OverrideTax>boolean</OverrideTax>
      <BusinessVolume>decimal</BusinessVolume>
      <CommissionableVolume>decimal</CommissionableVolume>
      <Other1>decimal</Other1>
      <Other2>decimal</Other2>
      <Other3>decimal</Other3>
      <Other4>decimal</Other4>
      <Other5>decimal</Other5>
      <Discount>decimal</Discount>
      <DiscountPercent>decimal</DiscountPercent>
      <Weight>decimal</Weight>
      <Sourcety>int</Sourcety>
      <Notes>string</Notes>
      <Usr>string</Usr>
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
      <SuppressPackSlipPrice>boolean</SuppressPackSlipPrice>
      <ShipMethodID>int</ShipMethodID>
      <AutoOrderID>int</AutoOrderID>
      <CreatedBy>string</CreatedBy>
      <ReturnOrderID>int</ReturnOrderID>
      <OrderRankID>int</OrderRankID>
      <OrderPayRankID>int</OrderPayRankID>
      <AddressIsVerified>boolean</AddressIsVerified>
      <County>string</County>
      <IsRMA>boolean</IsRMA>
      <BackOrderFromID>int</BackOrderFromID>
      <CreditsEarned>decimal</CreditsEarned>
      <TotalFedTax>decimal</TotalFedTax>
      <TotalStateTax>decimal</TotalStateTax>
      <ManualShippingTax>decimal</ManualShippingTax>
      <ReplacementOrderID>int</ReplacementOrderID>
      <LockedDate>dateTime</LockedDate>
      <CommissionedDate>dateTime</CommissionedDate>
      <Flag1>boolean</Flag1>
      <Flag2>boolean</Flag2>
      <Flag3>boolean</Flag3>
      <Other6>decimal</Other6>
      <Other7>decimal</Other7>
      <Other8>decimal</Other8>
      <Other9>decimal</Other9>
      <Other10>decimal</Other10>
      <OriginalWarehouseID>int</OriginalWarehouseID>
      <PickupName>string</PickupName>
      <TransferToID>int</TransferToID>
      <IsCommissionable>boolean</IsCommissionable>
      <FulfilledBy>string</FulfilledBy>
      <CreditApplied>decimal</CreditApplied>
      <ShippedDate>dateTime</ShippedDate>
      <TaxLockDate>dateTime</TaxLockDate>
      <TotalTaxable>decimal</TotalTaxable>
      <ReturnCategoryID>int</ReturnCategoryID>
      <ReplacementCategoryID>int</ReplacementCategoryID>
      <CalculatedShipping>decimal</CalculatedShipping>
      <HandlingFee>decimal</HandlingFee>
      <OrderProcessTy>int</OrderProcessTy>
      <ActualCarrier>int</ActualCarrier>
      <ParentOrderID>int</ParentOrderID>
      <CustomerTy>int</CustomerTy>
      <Reference>string</Reference>
      <MiddleName>string</MiddleName>
      <NameSuffix>string</NameSuffix>
      <Address3>string</Address3>
      <PartyID>int</PartyID>
      <TrackingNumber1>string</TrackingNumber1>
      <TrackingNumber2>string</TrackingNumber2>
      <TrackingNumber3>string</TrackingNumber3>
      <TrackingNumber4>string</TrackingNumber4>
      <TrackingNumber5>string</TrackingNumber5>
      <WebCarrierID>FedEx or UPS or Purolator or CanadaPostRegular or CanadaPostExpress or DHL or USPS or Estafeta or RoyalMail or GLSHungary or PostenNorway or LandMarkGlobal or GDEX</WebCarrierID>
      <WebCarrierID2>FedEx or UPS or Purolator or CanadaPostRegular or CanadaPostExpress or DHL or USPS or Estafeta or RoyalMail or GLSHungary or PostenNorway or LandMarkGlobal or GDEX</WebCarrierID2>
      <WebCarrierID3>FedEx or UPS or Purolator or CanadaPostRegular or CanadaPostExpress or DHL or USPS or Estafeta or RoyalMail or GLSHungary or PostenNorway or LandMarkGlobal or GDEX</WebCarrierID3>
      <WebCarrierID4>FedEx or UPS or Purolator or CanadaPostRegular or CanadaPostExpress or DHL or USPS or Estafeta or RoyalMail or GLSHungary or PostenNorway or LandMarkGlobal or GDEX</WebCarrierID4>
      <WebCarrierID5>FedEx or UPS or Purolator or CanadaPostRegular or CanadaPostExpress or DHL or USPS or Estafeta or RoyalMail or GLSHungary or PostenNorway or LandMarkGlobal or GDEX</WebCarrierID5>
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
      <TransferToKey>string</TransferToKey>
      <OrderKey>string</OrderKey>
      <ReturnOrderKey>string</ReturnOrderKey>
      <ReplacementOrderKey>string</ReplacementOrderKey>
      <ParentOrderKey>string</ParentOrderKey>
      <BackOrderFromKey>string</BackOrderFromKey>
      <OrderSubStatusTy>int</OrderSubStatusTy>
    </UpdateOrderRequest>
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
    <UpdateOrderResult xmlns="http://api.exigo.com/" />
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
    var req = new UpdateOrderRequest();

    req.OrderID = 1;                //Unique numeric identifier for order record.
    req.OrderDate = DateTime.Today;
    req.DeclineCount = 1;
    req.OrderTy = 1;
    req.OrderStatus = 1;
    req.PriceTy = 1;                //Controls which price band to use
    req.Total = 1;
    req.SubTotal = 1;
    req.Shipping = 1;
    req.OrderTax = 1;
    req.ShippingTax = 1;
    req.FedShippingTax = 1;
    req.StateShippingTax = 1;
    req.CityShippingTax = 1;
    req.CityLocalShippingTax = 1;
    req.CountyShippingTax = 1;
    req.CountyLocalShippingTax = 1;
    req.ManualTaxRate = 1;
    req.TotalTax = 1;
    req.CurrencyCode = usd;
    req.PaymentMethod = 1;
    req.WarehouseID = 1;            //Unique location for orders
    req.BatchID = 1;
    req.PreviousBalance = 1;
    req.OverrideShipping = true;
    req.OverrideTax = true;
    req.BusinessVolume = 1;         //Price amount
    req.CommissionableVolume = 1;   //Price amount
    req.Discount = 1;
    req.DiscountPercent = 1;
    req.Weight = 1;
    req.Sourcety = 1;
    req.Notes = 1;
    req.Usr = 1;
    req.FirstName = 1;
    req.LastName = 1;
    req.Company = 1;
    req.Address1 = 1;
    req.Address2 = 1;
    req.City = 1;
    req.Zip = 1;
    req.Email = 1;
    req.Phone = 1;
    req.SuppressPackSlipPrice = true;
    req.ShipMethodID = 1;
    req.AutoOrderID = 1;
    req.CreatedBy = 1;
    req.ReturnOrderID = 1;          //Unique numeric identifier for transfer to order record.
    req.OrderRankID = 1;
    req.OrderPayRankID = 1;
    req.AddressIsVerified = true;
    req.County = 1;
    req.IsRMA = true;
    req.BackOrderFromID = 1;        //Unique numeric identifier for transfer to order record.
    req.CreditsEarned = 1;
    req.TotalFedTax = 1;
    req.TotalStateTax = 1;
    req.ManualShippingTax = 1;
    req.ReplacementOrderID = 1;     //Unique numeric identifier for transfer to order record.
    req.LockedDate = DateTime.Today;
    req.CommissionedDate = DateTime.Today;
    req.Flag1 = true;
    req.Flag2 = true;
    req.Flag3 = true;
    req.OriginalWarehouseID = 1;
    req.PickupName = 1;
    req.TransferToID = 1;           //Unique numeric identifier for transfer to order record.
    req.IsCommissionable = true;
    req.FulfilledBy = 1;
    req.CreditApplied = 1;
    req.ShippedDate = DateTime.Today;
    req.TaxLockDate = DateTime.Today;
    req.TotalTaxable = 1;
    req.ReturnCategoryID = 1;
    req.ReplacementCategoryID = 1;
    req.CalculatedShipping = 1;
    req.HandlingFee = 1;
    req.OrderProcessTy = 1;
    req.ActualCarrier = 1;
    req.ParentOrderID = 1;          //Unique numeric identifier for transfer to order record.
    req.CustomerTy = 1;             //Classification of a customer as defined by the company
    req.Reference = 1;
    req.MiddleName = 1;
    req.NameSuffix = 1;
    req.Address3 = 1;
    req.PartyID = 1;
    req.TrackingNumber1 = 1;
    req.TrackingNumber2 = 1;
    req.TrackingNumber3 = 1;
    req.TrackingNumber4 = 1;
    req.TrackingNumber5 = 1;
    req.WebCarrierID = OrderShipCarrier.FedEx;
    req.WebCarrierID2 = OrderShipCarrier.FedEx;
    req.WebCarrierID3 = OrderShipCarrier.FedEx;
    req.WebCarrierID4 = OrderShipCarrier.FedEx;
    req.WebCarrierID5 = OrderShipCarrier.FedEx;
    req.Other11 = 1;
    req.Other12 = 1;
    req.Other13 = 1;
    req.Other14 = 1;
    req.Other15 = 1;
    req.Other16 = 1;
    req.Other17 = 1;
    req.Other18 = 1;
    req.Other19 = 1;
    req.Other20 = 1;
    req.TransferToKey = "1";        //Unique alpha numeric identifier for transfer to order record. Exeption will occur if TransferToID & TransferToKey are provided.
    req.OrderKey = "DDks8235txcid"; //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.
    req.ReturnOrderKey = "1";       //Unique alpha numeric identifier for transfer to order record. Exeption will occur if ReturnOrderID & ReturnOrderKey are provided.
    req.ReplacementOrderKey = "1";  //Unique alpha numeric identifier for transfer to order record. Exeption will occur if ReplacementOrderID & ReplacementOrderKey are provided.
    req.ParentOrderKey = "1";       //Unique alpha numeric identifier for transfer to order record. Exeption will occur if ParentOrderID & ParentOrderKey are provided.
    req.BackOrderFromKey = "1";     //Unique alpha numeric identifier for transfer to order record. Exeption will occur if BackOrderFromID & BackOrderFromKey are provided.

    //Send Request to Server and Get Response
    var res = await api.UpdateOrderAsync(req);

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
    UpdateOrderRequest req = new UpdateOrderRequest();

    req.OrderID = 1;                //Unique numeric identifier for order record.
    req.OrderDate = DateTime.Today;
    req.DeclineCount = 1;
    req.OrderTy = 1;
    req.OrderStatus = 1;
    req.PriceTy = 1;                //Controls which price band to use
    req.Total = 1;
    req.SubTotal = 1;
    req.Shipping = 1;
    req.OrderTax = 1;
    req.ShippingTax = 1;
    req.FedShippingTax = 1;
    req.StateShippingTax = 1;
    req.CityShippingTax = 1;
    req.CityLocalShippingTax = 1;
    req.CountyShippingTax = 1;
    req.CountyLocalShippingTax = 1;
    req.ManualTaxRate = 1;
    req.TotalTax = 1;
    req.CurrencyCode = usd;
    req.PaymentMethod = 1;
    req.WarehouseID = 1;            //Unique location for orders
    req.BatchID = 1;
    req.PreviousBalance = 1;
    req.OverrideShipping = true;
    req.OverrideTax = true;
    req.BusinessVolume = 1;         //Price amount
    req.CommissionableVolume = 1;   //Price amount
    req.Discount = 1;
    req.DiscountPercent = 1;
    req.Weight = 1;
    req.Sourcety = 1;
    req.Notes = 1;
    req.Usr = 1;
    req.FirstName = 1;
    req.LastName = 1;
    req.Company = 1;
    req.Address1 = 1;
    req.Address2 = 1;
    req.City = 1;
    req.Zip = 1;
    req.Email = 1;
    req.Phone = 1;
    req.SuppressPackSlipPrice = true;
    req.ShipMethodID = 1;
    req.AutoOrderID = 1;
    req.CreatedBy = 1;
    req.ReturnOrderID = 1;          //Unique numeric identifier for transfer to order record.
    req.OrderRankID = 1;
    req.OrderPayRankID = 1;
    req.AddressIsVerified = true;
    req.County = 1;
    req.IsRMA = true;
    req.BackOrderFromID = 1;        //Unique numeric identifier for transfer to order record.
    req.CreditsEarned = 1;
    req.TotalFedTax = 1;
    req.TotalStateTax = 1;
    req.ManualShippingTax = 1;
    req.ReplacementOrderID = 1;     //Unique numeric identifier for transfer to order record.
    req.LockedDate = DateTime.Today;
    req.CommissionedDate = DateTime.Today;
    req.Flag1 = true;
    req.Flag2 = true;
    req.Flag3 = true;
    req.OriginalWarehouseID = 1;
    req.PickupName = 1;
    req.TransferToID = 1;           //Unique numeric identifier for transfer to order record.
    req.IsCommissionable = true;
    req.FulfilledBy = 1;
    req.CreditApplied = 1;
    req.ShippedDate = DateTime.Today;
    req.TaxLockDate = DateTime.Today;
    req.TotalTaxable = 1;
    req.ReturnCategoryID = 1;
    req.ReplacementCategoryID = 1;
    req.CalculatedShipping = 1;
    req.HandlingFee = 1;
    req.OrderProcessTy = 1;
    req.ActualCarrier = 1;
    req.ParentOrderID = 1;          //Unique numeric identifier for transfer to order record.
    req.CustomerTy = 1;             //Classification of a customer as defined by the company
    req.Reference = 1;
    req.MiddleName = 1;
    req.NameSuffix = 1;
    req.Address3 = 1;
    req.PartyID = 1;
    req.TrackingNumber1 = 1;
    req.TrackingNumber2 = 1;
    req.TrackingNumber3 = 1;
    req.TrackingNumber4 = 1;
    req.TrackingNumber5 = 1;
    req.WebCarrierID = OrderShipCarrier.FedEx;
    req.WebCarrierID2 = OrderShipCarrier.FedEx;
    req.WebCarrierID3 = OrderShipCarrier.FedEx;
    req.WebCarrierID4 = OrderShipCarrier.FedEx;
    req.WebCarrierID5 = OrderShipCarrier.FedEx;
    req.Other11 = 1;
    req.Other12 = 1;
    req.Other13 = 1;
    req.Other14 = 1;
    req.Other15 = 1;
    req.Other16 = 1;
    req.Other17 = 1;
    req.Other18 = 1;
    req.Other19 = 1;
    req.Other20 = 1;
    req.TransferToKey = "1";        //Unique alpha numeric identifier for transfer to order record. Exeption will occur if TransferToID & TransferToKey are provided.
    req.OrderKey = "DDks8235txcid"; //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.
    req.ReturnOrderKey = "1";       //Unique alpha numeric identifier for transfer to order record. Exeption will occur if ReturnOrderID & ReturnOrderKey are provided.
    req.ReplacementOrderKey = "1";  //Unique alpha numeric identifier for transfer to order record. Exeption will occur if ReplacementOrderID & ReplacementOrderKey are provided.
    req.ParentOrderKey = "1";       //Unique alpha numeric identifier for transfer to order record. Exeption will occur if ParentOrderID & ParentOrderKey are provided.
    req.BackOrderFromKey = "1";     //Unique alpha numeric identifier for transfer to order record. Exeption will occur if BackOrderFromID & BackOrderFromKey are provided.

    //Send Request to Server and Get Response
    UpdateOrderResponse res = api.UpdateOrder(req);

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
    Dim req as new UpdateOrderRequest()

    req.OrderID = 1
    req.OrderDate = DateTime.Today
    req.DeclineCount = 1
    req.OrderTy = 1
    req.OrderStatus = 1
    req.PriceTy = 1
    req.Total = 1
    req.SubTotal = 1
    req.Shipping = 1
    req.OrderTax = 1
    req.ShippingTax = 1
    req.FedShippingTax = 1
    req.StateShippingTax = 1
    req.CityShippingTax = 1
    req.CityLocalShippingTax = 1
    req.CountyShippingTax = 1
    req.CountyLocalShippingTax = 1
    req.ManualTaxRate = 1
    req.TotalTax = 1
    req.CurrencyCode = usd
    req.PaymentMethod = 1
    req.WarehouseID = 1
    req.BatchID = 1
    req.PreviousBalance = 1
    req.OverrideShipping = true
    req.OverrideTax = true
    req.BusinessVolume = 1
    req.CommissionableVolume = 1
    req.Discount = 1
    req.DiscountPercent = 1
    req.Weight = 1
    req.Sourcety = 1
    req.Notes = 1
    req.Usr = 1
    req.FirstName = 1
    req.LastName = 1
    req.Company = 1
    req.Address1 = 1
    req.Address2 = 1
    req.City = 1
    req.Zip = 1
    req.Email = 1
    req.Phone = 1
    req.SuppressPackSlipPrice = true
    req.ShipMethodID = 1
    req.AutoOrderID = 1
    req.CreatedBy = 1
    req.ReturnOrderID = 1
    req.OrderRankID = 1
    req.OrderPayRankID = 1
    req.AddressIsVerified = true
    req.County = 1
    req.IsRMA = true
    req.BackOrderFromID = 1
    req.CreditsEarned = 1
    req.TotalFedTax = 1
    req.TotalStateTax = 1
    req.ManualShippingTax = 1
    req.ReplacementOrderID = 1
    req.LockedDate = DateTime.Today
    req.CommissionedDate = DateTime.Today
    req.Flag1 = true
    req.Flag2 = true
    req.Flag3 = true
    req.OriginalWarehouseID = 1
    req.PickupName = 1
    req.TransferToID = 1
    req.IsCommissionable = true
    req.FulfilledBy = 1
    req.CreditApplied = 1
    req.ShippedDate = DateTime.Today
    req.TaxLockDate = DateTime.Today
    req.TotalTaxable = 1
    req.ReturnCategoryID = 1
    req.ReplacementCategoryID = 1
    req.CalculatedShipping = 1
    req.HandlingFee = 1
    req.OrderProcessTy = 1
    req.ActualCarrier = 1
    req.ParentOrderID = 1
    req.CustomerTy = 1
    req.Reference = 1
    req.MiddleName = 1
    req.NameSuffix = 1
    req.Address3 = 1
    req.PartyID = 1
    req.TrackingNumber1 = 1
    req.TrackingNumber2 = 1
    req.TrackingNumber3 = 1
    req.TrackingNumber4 = 1
    req.TrackingNumber5 = 1
    req.WebCarrierID = OrderShipCarrier.FedEx
    req.WebCarrierID2 = OrderShipCarrier.FedEx
    req.WebCarrierID3 = OrderShipCarrier.FedEx
    req.WebCarrierID4 = OrderShipCarrier.FedEx
    req.WebCarrierID5 = OrderShipCarrier.FedEx
    req.Other11 = 1
    req.Other12 = 1
    req.Other13 = 1
    req.Other14 = 1
    req.Other15 = 1
    req.Other16 = 1
    req.Other17 = 1
    req.Other18 = 1
    req.Other19 = 1
    req.Other20 = 1
    req.TransferToKey = "1"
    req.OrderKey = "DDks8235txcid"
    req.ReturnOrderKey = "1"
    req.ReplacementOrderKey = "1"
    req.ParentOrderKey = "1"
    req.BackOrderFromKey = "1"

    'Send Request to Server and Get Response
    Dim res As UpdateOrderResponse = api.UpdateOrder(req)

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

    $req->OrderID = 1;
    $req->OrderDate = 1;
    $req->DeclineCount = 1;
    $req->OrderTy = 1;
    $req->OrderStatus = 1;
    $req->PriceTy = 1;
    $req->Total = 1;
    $req->SubTotal = 1;
    $req->Shipping = 1;
    $req->OrderTax = 1;
    $req->ShippingTax = 1;
    $req->FedShippingTax = 1;
    $req->StateShippingTax = 1;
    $req->CityShippingTax = 1;
    $req->CityLocalShippingTax = 1;
    $req->CountyShippingTax = 1;
    $req->CountyLocalShippingTax = 1;
    $req->ManualTaxRate = 1;
    $req->TotalTax = 1;
    $req->CurrencyCode = usd;
    $req->PaymentMethod = 1;
    $req->WarehouseID = 1;
    $req->BatchID = 1;
    $req->PreviousBalance = 1;
    $req->OverrideShipping = 1;
    $req->OverrideTax = 1;
    $req->BusinessVolume = 1;
    $req->CommissionableVolume = 1;
    $req->Discount = 1;
    $req->DiscountPercent = 1;
    $req->Weight = 1;
    $req->Sourcety = 1;
    $req->Notes = 1;
    $req->Usr = 1;
    $req->FirstName = 1;
    $req->LastName = 1;
    $req->Company = 1;
    $req->Address1 = 1;
    $req->Address2 = 1;
    $req->City = 1;
    $req->Zip = 1;
    $req->Email = 1;
    $req->Phone = 1;
    $req->SuppressPackSlipPrice = 1;
    $req->ShipMethodID = 1;
    $req->AutoOrderID = 1;
    $req->CreatedBy = 1;
    $req->ReturnOrderID = 1;
    $req->OrderRankID = 1;
    $req->OrderPayRankID = 1;
    $req->AddressIsVerified = 1;
    $req->County = 1;
    $req->IsRMA = 1;
    $req->BackOrderFromID = 1;
    $req->CreditsEarned = 1;
    $req->TotalFedTax = 1;
    $req->TotalStateTax = 1;
    $req->ManualShippingTax = 1;
    $req->ReplacementOrderID = 1;
    $req->LockedDate = 1;
    $req->CommissionedDate = 1;
    $req->Flag1 = 1;
    $req->Flag2 = 1;
    $req->Flag3 = 1;
    $req->OriginalWarehouseID = 1;
    $req->PickupName = 1;
    $req->TransferToID = 1;
    $req->IsCommissionable = 1;
    $req->FulfilledBy = 1;
    $req->CreditApplied = 1;
    $req->ShippedDate = 1;
    $req->TaxLockDate = 1;
    $req->TotalTaxable = 1;
    $req->ReturnCategoryID = 1;
    $req->ReplacementCategoryID = 1;
    $req->CalculatedShipping = 1;
    $req->HandlingFee = 1;
    $req->OrderProcessTy = 1;
    $req->ActualCarrier = 1;
    $req->ParentOrderID = 1;
    $req->CustomerTy = 1;
    $req->Reference = 1;
    $req->MiddleName = 1;
    $req->NameSuffix = 1;
    $req->Address3 = 1;
    $req->PartyID = 1;
    $req->TrackingNumber1 = 1;
    $req->TrackingNumber2 = 1;
    $req->TrackingNumber3 = 1;
    $req->TrackingNumber4 = 1;
    $req->TrackingNumber5 = 1;
    $req->WebCarrierID = 1;
    $req->WebCarrierID2 = 1;
    $req->WebCarrierID3 = 1;
    $req->WebCarrierID4 = 1;
    $req->WebCarrierID5 = 1;
    $req->Other11 = 1;
    $req->Other12 = 1;
    $req->Other13 = 1;
    $req->Other14 = 1;
    $req->Other15 = 1;
    $req->Other16 = 1;
    $req->Other17 = 1;
    $req->Other18 = 1;
    $req->Other19 = 1;
    $req->Other20 = 1;
    $req->TransferToKey = "1";
    $req->OrderKey = "DDks8235txcid";
    $req->ReturnOrderKey = "1";
    $req->ReplacementOrderKey = "1";
    $req->ParentOrderKey = "1";
    $req->BackOrderFromKey = "1";

    //Send Request to Server and Get Response
    $res = $api.UpdateOrder($req);

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
    UpdateOrderRequest req = new UpdateOrderRequest();

    req.setOrderID(1);
    req.setOrderDate(1);
    req.setDeclineCount(1);
    req.setOrderTy(1);
    req.setOrderStatus(1);
    req.setPriceTy(1);
    req.setTotal(1);
    req.setSubTotal(1);
    req.setShipping(1);
    req.setOrderTax(1);
    req.setShippingTax(1);
    req.setFedShippingTax(1);
    req.setStateShippingTax(1);
    req.setCityShippingTax(1);
    req.setCityLocalShippingTax(1);
    req.setCountyShippingTax(1);
    req.setCountyLocalShippingTax(1);
    req.setManualTaxRate(1);
    req.setTotalTax(1);
    req.setCurrencyCode(usd);
    req.setPaymentMethod(1);
    req.setWarehouseID(1);
    req.setBatchID(1);
    req.setPreviousBalance(1);
    req.setOverrideShipping(1);
    req.setOverrideTax(1);
    req.setBusinessVolume(1);
    req.setCommissionableVolume(1);
    req.setDiscount(1);
    req.setDiscountPercent(1);
    req.setWeight(1);
    req.setSourcety(1);
    req.setNotes(1);
    req.setUsr(1);
    req.setFirstName(1);
    req.setLastName(1);
    req.setCompany(1);
    req.setAddress1(1);
    req.setAddress2(1);
    req.setCity(1);
    req.setZip(1);
    req.setEmail(1);
    req.setPhone(1);
    req.setSuppressPackSlipPrice(1);
    req.setShipMethodID(1);
    req.setAutoOrderID(1);
    req.setCreatedBy(1);
    req.setReturnOrderID(1);
    req.setOrderRankID(1);
    req.setOrderPayRankID(1);
    req.setAddressIsVerified(1);
    req.setCounty(1);
    req.setIsRMA(1);
    req.setBackOrderFromID(1);
    req.setCreditsEarned(1);
    req.setTotalFedTax(1);
    req.setTotalStateTax(1);
    req.setManualShippingTax(1);
    req.setReplacementOrderID(1);
    req.setLockedDate(1);
    req.setCommissionedDate(1);
    req.setFlag1(1);
    req.setFlag2(1);
    req.setFlag3(1);
    req.setOriginalWarehouseID(1);
    req.setPickupName(1);
    req.setTransferToID(1);
    req.setIsCommissionable(1);
    req.setFulfilledBy(1);
    req.setCreditApplied(1);
    req.setShippedDate(1);
    req.setTaxLockDate(1);
    req.setTotalTaxable(1);
    req.setReturnCategoryID(1);
    req.setReplacementCategoryID(1);
    req.setCalculatedShipping(1);
    req.setHandlingFee(1);
    req.setOrderProcessTy(1);
    req.setActualCarrier(1);
    req.setParentOrderID(1);
    req.setCustomerTy(1);
    req.setReference(1);
    req.setMiddleName(1);
    req.setNameSuffix(1);
    req.setAddress3(1);
    req.setPartyID(1);
    req.setTrackingNumber1(1);
    req.setTrackingNumber2(1);
    req.setTrackingNumber3(1);
    req.setTrackingNumber4(1);
    req.setTrackingNumber5(1);
    req.setWebCarrierID(1);
    req.setWebCarrierID2(1);
    req.setWebCarrierID3(1);
    req.setWebCarrierID4(1);
    req.setWebCarrierID5(1);
    req.setOther11(1);
    req.setOther12(1);
    req.setOther13(1);
    req.setOther14(1);
    req.setOther15(1);
    req.setOther16(1);
    req.setOther17(1);
    req.setOther18(1);
    req.setOther19(1);
    req.setOther20(1);
    req.setTransferToKey("1");
    req.setOrderKey("DDks8235txcid");
    req.setReturnOrderKey("1");
    req.setReplacementOrderKey("1");
    req.setParentOrderKey("1");
    req.setBackOrderFromKey("1");

    //Send Request to Server and Get Response
    UpdateOrderResponse res = api.getExigoApiSoap().updateOrder(req, auth);

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

### UpdateOrderDetail

> Update an existing Order Detail for an existing order
>  without recalculating. Can participate in a transaction.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `PUT /3.0/orders/detail` |
| SOAP action | `https://api.exigo.com/UpdateOrderDetail` |
| WSDL elements | `UpdateOrderDetailRequest` → `UpdateOrderDetailResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateOrderDetail |

#### Input

**`UpdateOrderDetailRequest`**

| Property | Type | Notes |
|---|---|---|
| `OrderID` | `Int32` | Unique numeric identifier for new order record. |
| `ItemID` | `Int32` | Optional. Unique identifier for a item record. |
| `ItemCode` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `OrderLine` | `Int32` |  |
| `Description` | `String` | Optional. |
| `Qty` | `Decimal` | Optional. |
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

**`UpdateOrderDetailResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/orders/detail HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "itemID": 1,
  "itemCode": "1",
  "orderLine": 1,
  "description": "",
  "qty": null,
  "priceEach": null,
  "priceExt": null,
  "bVEach": null,
  "businessVolume": null,
  "cVEach": null,
  "commissionableVolume": null,
  "shippingPriceEach": null,
  "chargeShippingOn": null,
  "isTaxedInRegion": true,
  "isTaxedInRegionFed": true,
  "isTaxedInRegionState": true,
  "taxablePriceEach": null,
  "taxable": null,
  "combinedTax": null,
  "fedTax": null,
  "stateTax": null,
  "cityTax": null,
  "cityLocalTax": null,
  "countyTax": null,
  "countyLocalTax": null,
  "manualTax": null,
  "isBackOrder": true,
  "weightEach": null,
  "other1Each": null,
  "other2Each": null,
  "other3Each": null,
  "other4Each": null,
  "other5Each": null,
  "other6Each": null,
  "other7Each": null,
  "other8Each": null,
  "other9Each": null,
  "other10Each": null,
  "discountExt": null,
  "originalTaxableEach": null,
  "originalBVEach": null,
  "originalCVEach": null,
  "stateTaxable": null,
  "isStateTaxOverride": true,
  "dynamicKitItemID": 1,
  "handlingFee": null,
  "reference1": "",
  "orderKey": "1"
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
SOAPAction: "https://api.exigo.com/UpdateOrderDetail"

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
    <UpdateOrderDetailRequest xmlns="http://api.exigo.com/">
      <OrderID>int</OrderID>
      <ItemID>int</ItemID>
      <ItemCode>string</ItemCode>
      <OrderLine>int</OrderLine>
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
    </UpdateOrderDetailRequest>
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
    <UpdateOrderDetailResult xmlns="http://api.exigo.com/" />
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
    var req = new UpdateOrderDetailRequest();

    req.ItemID = 1;                 //Unique identifier for a item record.
    req.ItemCode = "1";
    req.OrderLine = 1;
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
    var res = await api.UpdateOrderDetailAsync(req);

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
    UpdateOrderDetailRequest req = new UpdateOrderDetailRequest();

    req.ItemID = 1;                 //Unique identifier for a item record.
    req.ItemCode = "1";
    req.OrderLine = 1;
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
    UpdateOrderDetailResponse res = api.UpdateOrderDetail(req);

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
    Dim req as new UpdateOrderDetailRequest()

    req.ItemID = 1
    req.ItemCode = "1"
    req.OrderLine = 1
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
    Dim res As UpdateOrderDetailResponse = api.UpdateOrderDetail(req)

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

    $req->ItemID = 1;
    $req->ItemCode = "1";
    $req->OrderLine = 1;
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
    $res = $api.UpdateOrderDetail($req);

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
    UpdateOrderDetailRequest req = new UpdateOrderDetailRequest();

    req.setItemID(1);
    req.setItemCode("1");
    req.setOrderLine(1);
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
    UpdateOrderDetailResponse res = api.getExigoApiSoap().updateOrderDetail(req, auth);

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

### ChangeOrderStatus

>  Changes an existing order from one status to another.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `POST /3.0/orders/status` |
| SOAP action | `https://api.exigo.com/ChangeOrderStatus` |
| WSDL elements | `ChangeOrderStatusRequest` → `ChangeOrderStatusResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=ChangeOrderStatus |

#### Input

**`ChangeOrderStatusRequest`**

| Property | Type | Notes |
|---|---|---|
| `OrderID` | `Int32` | Unique numeric identifier for new order record. |
| `OrderStatus` | `OrderStatusType` | **Values:** `Incomplete`, `Pending`, `CCDeclined`, `ACHDeclined`, `Canceled`, `CCPending`, `ACHPending`, `Accepted`, `Printed`, `Shipped`, `PendingInventory` |
| `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided. |
| `OrderSubStatusTy` | `Int32` | Optional. |

#### Output

**`ChangeOrderStatusResponse`**

_No properties._

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/orders/status HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "orderStatus": null,
  "orderKey": "1"
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
SOAPAction: "https://api.exigo.com/ChangeOrderStatus"

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
    <ChangeOrderStatusRequest xmlns="http://api.exigo.com/">
      <OrderID>int</OrderID>
      <OrderStatus>Incomplete or Pending or CCDeclined or ACHDeclined or Canceled or CCPending or ACHPending or Accepted or Printed or Shipped or PendingInventory</OrderStatus>
      <OrderKey>string</OrderKey>
      <OrderSubStatusTy>int</OrderSubStatusTy>
    </ChangeOrderStatusRequest>
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
    <ChangeOrderStatusResult xmlns="http://api.exigo.com/" />
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
    var req = new ChangeOrderStatusRequest();

    req.OrderStatus = OrderStatusType.Incomplete;
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    var res = await api.ChangeOrderStatusAsync(req);

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
    ChangeOrderStatusRequest req = new ChangeOrderStatusRequest();

    req.OrderStatus = OrderStatusType.Incomplete;
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    ChangeOrderStatusResponse res = api.ChangeOrderStatus(req);

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
    Dim req as new ChangeOrderStatusRequest()

    req.OrderStatus = OrderStatusType.Incomplete
    req.OrderKey = "1"

    'Send Request to Server and Get Response
    Dim res As ChangeOrderStatusResponse = api.ChangeOrderStatus(req)

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

    $req->OrderStatus = 1;
    $req->OrderKey = "1";

    //Send Request to Server and Get Response
    $res = $api.ChangeOrderStatus($req);

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
    ChangeOrderStatusRequest req = new ChangeOrderStatusRequest();

    req.setOrderStatus(1);
    req.setOrderKey("1");

    //Send Request to Server and Get Response
    ChangeOrderStatusResponse res = api.getExigoApiSoap().changeOrderStatus(req, auth);

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

### ChangeOrderStatusBatch

>  Changes existing orders from one status to another in a batch. Can optionally
>  update tracking numbers as well.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `POST /3.0/orders/statusbatch` |
| SOAP action | `https://api.exigo.com/ChangeOrderStatusBatch` |
| WSDL elements | `ChangeOrderStatusBatchRequest` → `ChangeOrderStatusBatchResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=ChangeOrderStatusBatch |

#### Input

**`ChangeOrderStatusBatchRequest`**

| Property | Type | Notes |
|---|---|---|
| `OrderStatus` | `OrderStatusType` | Obsolete field. Please consider upgrading to OrderStatusTy.<br>**Values:** `Incomplete`, `Pending`, `CCDeclined`, `ACHDeclined`, `Canceled`, `CCPending`, `ACHPending`, `Accepted`, `Printed`, `Shipped`, `PendingInventory` |
| `Details` | `OrderBatchDetailRequest[]` |  |
| `OrderStatusTy` | `String` | Optional. The status to apply to all detail.<br>**Lookup:** company-specific list (see company-lists.md) |

**`OrderBatchDetailRequest`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `OrderID` | `Int32` | Unique numeric identifier for new order record. |
| &nbsp;&nbsp;↳ `TrackingNumber1` | `String` | Optional. Optionally update tracking number. |
| &nbsp;&nbsp;↳ `TrackingNumber2` | `String` | Optional. Optionally update tracking number. |
| &nbsp;&nbsp;↳ `TrackingNumber3` | `String` | Optional. Optionally update tracking number. |
| &nbsp;&nbsp;↳ `TrackingNumber4` | `String` | Optional. Optionally update tracking number. |
| &nbsp;&nbsp;↳ `TrackingNumber5` | `String` | Optional. Optionally update tracking number. |
| &nbsp;&nbsp;↳ `ShippedDate` | `DateTime` | Optional. Optionally manually set ShippedDate. |
| &nbsp;&nbsp;↳ `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided. |

#### Output

**`ChangeOrderStatusBatchResponse`**

_No properties._

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/orders/statusbatch HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "details": null,
  "orderStatusTy": "Incomplete"
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
SOAPAction: "https://api.exigo.com/ChangeOrderStatusBatch"

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
    <ChangeOrderStatusBatchRequest xmlns="http://api.exigo.com/">
      <OrderStatus>Incomplete or Pending or CCDeclined or ACHDeclined or Canceled or CCPending or ACHPending or Accepted or Printed or Shipped or PendingInventory</OrderStatus>
      <Details>
        <OrderBatchDetailRequest>
          <OrderID>int</OrderID>
          <TrackingNumber1>string</TrackingNumber1>
          <TrackingNumber2>string</TrackingNumber2>
          <TrackingNumber3>string</TrackingNumber3>
          <TrackingNumber4>string</TrackingNumber4>
          <TrackingNumber5>string</TrackingNumber5>
          <ShippedDate>dateTime</ShippedDate>
          <OrderKey>string</OrderKey>
        </OrderBatchDetailRequest>
      </Details>
      <OrderStatusTy>string</OrderStatusTy>
    </ChangeOrderStatusBatchRequest>
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
    <ChangeOrderStatusBatchResult xmlns="http://api.exigo.com/" />
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
    var req = new ChangeOrderStatusBatchRequest();

    //Add Details
    var details = new List<OrderBatchDetailRequest>();

    var detail1 = new OrderBatchDetailRequest();
    detail1.TrackingNumber1 = "1";
    detail1.OrderKey = "1";
    details.Add(detail1);

    var detail2 = new OrderBatchDetailRequest();
    detail2.TrackingNumber1 = "2";
    detail2.OrderKey = "2";
    details.Add(detail2);

    //Now attach the list to the request
    req.Details = details.ToArray();
    req.OrderStatusTy = "Incomplete";//The status to apply to all detail

    //Send Request to Server and Get Response
    var res = await api.ChangeOrderStatusBatchAsync(req);

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
    ChangeOrderStatusBatchRequest req = new ChangeOrderStatusBatchRequest();

    //Add Details
    List<OrderBatchDetailRequest> details = new List<OrderBatchDetailRequest>();

    OrderBatchDetailRequest detail1 = new OrderBatchDetailRequest();
    detail1.TrackingNumber1 = "1";
    detail1.OrderKey = "1";
    details.Add(detail1);

    OrderBatchDetailRequest detail2 = new OrderBatchDetailRequest();
    detail2.TrackingNumber1 = "2";
    detail2.OrderKey = "2";
    details.Add(detail2);

    //Now attach the list to the request
    req.Details = details.ToArray();
    req.OrderStatusTy = "Incomplete";//The status to apply to all detail

    //Send Request to Server and Get Response
    ChangeOrderStatusBatchResponse res = api.ChangeOrderStatusBatch(req);

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
    Dim req as new ChangeOrderStatusBatchRequest()

    'Add Details
    Dim details As New List(Of OrderBatchDetailRequest)()

    Dim detail1 as new OrderBatchDetailRequest()
    detail1.TrackingNumber1 = "1"
    detail1.OrderKey = "1"
    details.Add(detail1)

    Dim detail2 as new OrderBatchDetailRequest()
    detail2.TrackingNumber1 = "2"
    detail2.OrderKey = "2"
    details.Add(detail2)

    'Now attach the list to the request
    req.Details = details.ToArray()
    req.OrderStatusTy = "Incomplete"

    'Send Request to Server and Get Response
    Dim res As ChangeOrderStatusBatchResponse = api.ChangeOrderStatusBatch(req)

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

    //Add Details

    $detail1->TrackingNumber1 = "1";
    $detail1->OrderKey = "1";

    $detail2->TrackingNumber1 = "2";
    $detail2->OrderKey = "2";

    //Now attach the list to the request
    req.Details = array(detail1,detail2);
    $req->OrderStatusTy = "Incomplete";

    //Send Request to Server and Get Response
    $res = $api.ChangeOrderStatusBatch($req);

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
    ChangeOrderStatusBatchRequest req = new ChangeOrderStatusBatchRequest();

    //Add Details
    ArrayOfOrderBatchDetailRequest details = new ArrayOfOrderBatchDetailRequest();

    OrderBatchDetailRequest detail1 = new OrderBatchDetailRequest();
    detail1.setTrackingNumber1("1");
    detail1.setOrderKey("1");
    details.Add(detail1);

    OrderBatchDetailRequest detail2 = new OrderBatchDetailRequest();
    detail2.setTrackingNumber1("2");
    detail2.setOrderKey("2");
    details.Add(detail2);

    //Now attach the list to the request
    req.setDetails(details);
    req.setOrderStatusTy("Incomplete");

    //Send Request to Server and Get Response
    ChangeOrderStatusBatchResponse res = api.getExigoApiSoap().changeOrderStatusBatch(req, auth);

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

### ValidateCreditCardToken

> Validates a credit card token.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `POST /3.0/payment/validate/token` |
| SOAP action | `https://api.exigo.com/ValidateCreditCardToken` |
| WSDL elements | `ValidateCreditCardTokenRequest` → `ValidateCreditCardTokenResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=ValidateCreditCardToken |

#### Input

**`ValidateCreditCardTokenRequest`**

| Property | Type | Notes |
|---|---|---|
| `CreditCardIdentifier` | `String` | Optional. |
| `ExpirationYear` | `Int32` | Optional. |
| `ExpirationMonth` | `Int32` | Optional. |
| `CvcCode` | `String` | Optional. |
| `BillingName` | `String` | Optional. |
| `BillingAddress1` | `String` | Optional. |
| `BillingAddress2` | `String` | Optional. |
| `BillingCity` | `String` | Optional. |
| `BillingState` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `BillingZip` | `String` | Optional. |
| `BillingCountry` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `CustomerID` | `Int32` | Optional. Unique numeric identifier for a customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |
| `OrderID` | `Int32` | Optional. Unique numeric identifier for order record. |
| `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided. |
| `Other1` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other2` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other3` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other4` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other5` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other6` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other7` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other8` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other9` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other10` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `ValidateTokenOnFile` | `Boolean` | Optional. Use this option to validate information already on file. |
| `AccountOnFile` | `TokenAccount` | Optional. To be used when ValidateTokenOnFile = true.<br>**Values:** `Primary`, `Secondary` |
| `WarehouseID` | `Int32` | Optional. |
| `CurrencyCode` | `String` | Optional. Optional. |
| `Email` | `String` | Optional. Optional. |
| `Phone` | `String` | Optional. Optional. |
| `ClientIpAddress` | `String` | Optional. Optional. |

#### Output

**`ValidateCreditCardTokenResponse`**

| Property | Type | Notes |
|---|---|---|
| `AuthorizationCode` | `String` |  |
| `Message` | `String` |  |
| `Success` | `Boolean` |  |
| `DisplayMessage` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/payment/validate/token HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "creditCardIdentifier": "",
  "expirationYear": 1,
  "expirationMonth": 1,
  "cvcCode": "",
  "billingName": "",
  "billingAddress1": "",
  "billingAddress2": "",
  "billingCity": "",
  "billingZip": "",
  "customerID": 1,
  "customerKey": "DDks8235txcid",
  "orderID": 1,
  "orderKey": "DDks8235txcid",
  "validateTokenOnFile": true,
  "accountOnFile": null,
  "warehouseID": 1,
  "currencyCode": "1",
  "email": "1",
  "phone": "1",
  "clientIpAddress": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "authorizationCode": "",
  "message": "",
  "success": true,
  "displayMessage": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/ValidateCreditCardToken"

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
    <ValidateCreditCardTokenRequest xmlns="http://api.exigo.com/">
      <CreditCardIdentifier>string</CreditCardIdentifier>
      <ExpirationYear>int</ExpirationYear>
      <ExpirationMonth>int</ExpirationMonth>
      <CvcCode>string</CvcCode>
      <BillingName>string</BillingName>
      <BillingAddress1>string</BillingAddress1>
      <BillingAddress2>string</BillingAddress2>
      <BillingCity>string</BillingCity>
      <BillingState>string</BillingState>
      <BillingZip>string</BillingZip>
      <BillingCountry>string</BillingCountry>
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
      <OrderID>int</OrderID>
      <OrderKey>string</OrderKey>
      <Other1>string</Other1>
      <Other2>string</Other2>
      <Other3>string</Other3>
      <Other4>string</Other4>
      <Other5>string</Other5>
      <Other6>string</Other6>
      <Other7>string</Other7>
      <Other8>string</Other8>
      <Other9>string</Other9>
      <Other10>string</Other10>
      <ValidateTokenOnFile>boolean</ValidateTokenOnFile>
      <AccountOnFile>Primary or Secondary</AccountOnFile>
      <WarehouseID>int</WarehouseID>
      <CurrencyCode>string</CurrencyCode>
      <Email>string</Email>
      <Phone>string</Phone>
      <ClientIpAddress>string</ClientIpAddress>
    </ValidateCreditCardTokenRequest>
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
    <ValidateCreditCardTokenResult xmlns="http://api.exigo.com/">
      <AuthorizationCode>string</AuthorizationCode>
      <Message>string</Message>
      <Success>boolean</Success>
      <DisplayMessage>string</DisplayMessage>
    </ValidateCreditCardTokenResult>
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
    var req = new ValidateCreditCardTokenRequest();

    req.CreditCardIdentifier = "1";
    req.ExpirationYear = 1;
    req.ExpirationMonth = 1;
    req.CvcCode = "1";
    req.BillingName = "1";
    req.BillingAddress1 = "1";
    req.BillingAddress2 = "1";
    req.BillingCity = "1";
    req.BillingZip = "1";
    req.CustomerID = 1;             //Unique numeric identifier for a customer record.
    req.CustomerKey = "DDks8235txcid";//Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.OrderID = 1;                //Unique numeric identifier for order record.
    req.OrderKey = "DDks8235txcid"; //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.
    req.ValidateTokenOnFile = true;    //Optional. Use this option to validate information already on file
    req.AccountOnFile = TokenAccount.Primary;          //Optional. To be used when ValidateTokenOnFile = true
    req.WarehouseID = 1;            //Optional
    req.CurrencyCode = "1";         //Optional
    req.Email = "1";                //Optional
    req.Phone = "1";                //Optional
    req.ClientIpAddress = "1";      //Optional

    //Send Request to Server and Get Response
    var res = await api.ValidateCreditCardTokenAsync(req);

    //Now examine the results:
    Console.WriteLine("AuthorizationCode: {0}", res.AuthorizationCode);
    Console.WriteLine("Message: {0}", res.Message);
    Console.WriteLine("Success: {0}", res.Success);
    Console.WriteLine("DisplayMessage: {0}", res.DisplayMessage);
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
    ValidateCreditCardTokenRequest req = new ValidateCreditCardTokenRequest();

    req.CreditCardIdentifier = "1";
    req.ExpirationYear = 1;
    req.ExpirationMonth = 1;
    req.CvcCode = "1";
    req.BillingName = "1";
    req.BillingAddress1 = "1";
    req.BillingAddress2 = "1";
    req.BillingCity = "1";
    req.BillingZip = "1";
    req.CustomerID = 1;             //Unique numeric identifier for a customer record.
    req.CustomerKey = "DDks8235txcid";//Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.OrderID = 1;                //Unique numeric identifier for order record.
    req.OrderKey = "DDks8235txcid"; //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.
    req.ValidateTokenOnFile = true;    //Optional. Use this option to validate information already on file
    req.AccountOnFile = TokenAccount.Primary;          //Optional. To be used when ValidateTokenOnFile = true
    req.WarehouseID = 1;            //Optional
    req.CurrencyCode = "1";         //Optional
    req.Email = "1";                //Optional
    req.Phone = "1";                //Optional
    req.ClientIpAddress = "1";      //Optional

    //Send Request to Server and Get Response
    ValidateCreditCardTokenResponse res = api.ValidateCreditCardToken(req);

    //Now examine the results:
    Console.WriteLine("AuthorizationCode: {0}", res.AuthorizationCode);
    Console.WriteLine("Message: {0}", res.Message);
    Console.WriteLine("Success: {0}", res.Success);
    Console.WriteLine("DisplayMessage: {0}", res.DisplayMessage);
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
    Dim req as new ValidateCreditCardTokenRequest()

    req.CreditCardIdentifier = "1"
    req.ExpirationYear = 1
    req.ExpirationMonth = 1
    req.CvcCode = "1"
    req.BillingName = "1"
    req.BillingAddress1 = "1"
    req.BillingAddress2 = "1"
    req.BillingCity = "1"
    req.BillingZip = "1"
    req.CustomerID = 1
    req.CustomerKey = "DDks8235txcid"
    req.OrderID = 1
    req.OrderKey = "DDks8235txcid"
    req.ValidateTokenOnFile = true
    req.AccountOnFile = TokenAccount.Primary
    req.WarehouseID = 1
    req.CurrencyCode = "1"
    req.Email = "1"
    req.Phone = "1"
    req.ClientIpAddress = "1"

    'Send Request to Server and Get Response
    Dim res As ValidateCreditCardTokenResponse = api.ValidateCreditCardToken(req)

    'Now examine the results:
    Console.WriteLine("AuthorizationCode: {0}", res.AuthorizationCode)
    Console.WriteLine("Message: {0}", res.Message)
    Console.WriteLine("Success: {0}", res.Success)
    Console.WriteLine("DisplayMessage: {0}", res.DisplayMessage)
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

    $req->CreditCardIdentifier = "1";
    $req->ExpirationYear = 1;
    $req->ExpirationMonth = 1;
    $req->CvcCode = "1";
    $req->BillingName = "1";
    $req->BillingAddress1 = "1";
    $req->BillingAddress2 = "1";
    $req->BillingCity = "1";
    $req->BillingZip = "1";
    $req->CustomerID = 1;
    $req->CustomerKey = "DDks8235txcid";
    $req->OrderID = 1;
    $req->OrderKey = "DDks8235txcid";
    $req->ValidateTokenOnFile = 1;
    $req->AccountOnFile = 1;
    $req->WarehouseID = 1;
    $req->CurrencyCode = "1";
    $req->Email = "1";
    $req->Phone = "1";
    $req->ClientIpAddress = "1";

    //Send Request to Server and Get Response
    $res = $api.ValidateCreditCardToken($req);

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
    ValidateCreditCardTokenRequest req = new ValidateCreditCardTokenRequest();

    req.setCreditCardIdentifier("1");
    req.setExpirationYear(1);
    req.setExpirationMonth(1);
    req.setCvcCode("1");
    req.setBillingName("1");
    req.setBillingAddress1("1");
    req.setBillingAddress2("1");
    req.setBillingCity("1");
    req.setBillingZip("1");
    req.setCustomerID(1);
    req.setCustomerKey("DDks8235txcid");
    req.setOrderID(1);
    req.setOrderKey("DDks8235txcid");
    req.setValidateTokenOnFile(1);
    req.setAccountOnFile(1);
    req.setWarehouseID(1);
    req.setCurrencyCode("1");
    req.setEmail("1");
    req.setPhone("1");
    req.setClientIpAddress("1");

    //Send Request to Server and Get Response
    ValidateCreditCardTokenResponse res = api.getExigoApiSoap().validateCreditCardToken(req, auth);

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

### CreatePayment

> Creates a new payment type using cash, money order etc.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `POST /3.0/payment` |
| SOAP action | `https://api.exigo.com/CreatePayment` |
| WSDL elements | `CreatePaymentRequest` → `CreatePaymentResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreatePayment |

#### Input

**`CreatePaymentRequest`**

| Property | Type | Notes |
|---|---|---|
| `OrderID` | `Int32` | Unique numeric identifier for order record. |
| `PaymentDate` | `DateTime` |  |
| `Amount` | `Decimal` |  |
| `PaymentType` | `PaymentType` | Obsolete field. Please consider upgrading to PaymentTy.<br>**Values:** `Cash`, `CreditCard`, `Check`, `CreditVoucher`, `Net30`, `Net60`, `UseCredit`, `ACHDebit`, `BankDraft`, `BankWire`, `PointRedemtion`, `COD`, `MoneyOrder`, `BankDeposit`, `Other1`, `Other2`, `Other3`, `Wallet`, `Other4`, `Other5`, `Other6`, `Other7`, `Other8`, `Other9`, `Other10`, `Other11`, `Other12`, `Other13`, `Other14`, `Other15` |
| `AuthorizationCode` | `String` | Optional. |
| `Memo` | `String` | Optional. |
| `BillingName` | `String` | Optional. |
| `BillingAddress` | `String` | Optional. |
| `BillingAddress2` | `String` | Optional. |
| `BillingCity` | `String` | Optional. |
| `BillingState` | `String` | Optional. |
| `BillingZip` | `String` | Optional. |
| `BillingCountry` | `String` | Optional. |
| `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided. |
| `PaymentTy` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `MerchantTy` | `Int32` | Optional. . Defaults to 0. |
| `MerchantAccount` | `String` | Optional. |
| `MerchantTransactionKey` | `String` | Optional. |

#### Output

**`CreatePaymentResponse`**

| Property | Type | Notes |
|---|---|---|
| `PaymentID` | `Int32` |  |
| `Message` | `String` |  |
| `DisplayMessage` | `String` |  |
| `MerchantTransactionKey` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/payment HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "paymentDate": "2026-11-10T00:00:00-06:00",
  "amount": null,
  "orderKey": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "paymentID": 1,
  "message": "",
  "displayMessage": "",
  "merchantTransactionKey": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreatePayment"

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
    <CreatePaymentRequest xmlns="http://api.exigo.com/">
      <OrderID>int</OrderID>
      <PaymentDate>dateTime</PaymentDate>
      <Amount>decimal</Amount>
      <PaymentType>Cash or CreditCard or Check or CreditVoucher or Net30 or Net60 or ACHDebit or UseCredit or BankDraft or BankWire or PointRedemtion or COD or MoneyOrder or BankDeposit or Other1 or Other2 or Other3 or Wallet or Other4 or Other5 or Other6 or Other7 or Other8 or Other9 or Other10 or Other11 or Other12 or Other13 or Other14 or Other15</PaymentType>
      <AuthorizationCode>string</AuthorizationCode>
      <Memo>string</Memo>
      <BillingName>string</BillingName>
      <BillingAddress>string</BillingAddress>
      <BillingAddress2>string</BillingAddress2>
      <BillingCity>string</BillingCity>
      <BillingState>string</BillingState>
      <BillingZip>string</BillingZip>
      <BillingCountry>string</BillingCountry>
      <OrderKey>string</OrderKey>
      <PaymentTy>string</PaymentTy>
      <MerchantTy>int</MerchantTy>
      <MerchantAccount>string</MerchantAccount>
      <MerchantTransactionKey>string</MerchantTransactionKey>
    </CreatePaymentRequest>
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
    <CreatePaymentResult xmlns="http://api.exigo.com/">
      <PaymentID>int</PaymentID>
      <Message>string</Message>
      <DisplayMessage>string</DisplayMessage>
      <MerchantTransactionKey>string</MerchantTransactionKey>
    </CreatePaymentResult>
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
    var req = new CreatePaymentRequest();

    req.PaymentDate = DateTime.Today;
    req.Amount = 1;
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    var res = await api.CreatePaymentAsync(req);

    //Now examine the results:
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
    CreatePaymentRequest req = new CreatePaymentRequest();

    req.PaymentDate = DateTime.Today;
    req.Amount = 1;
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    CreatePaymentResponse res = api.CreatePayment(req);

    //Now examine the results:
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
    Dim req as new CreatePaymentRequest()

    req.PaymentDate = DateTime.Today
    req.Amount = 1
    req.OrderKey = "1"

    'Send Request to Server and Get Response
    Dim res As CreatePaymentResponse = api.CreatePayment(req)

    'Now examine the results:
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

    $req->PaymentDate = 1;
    $req->Amount = 1;
    $req->OrderKey = "1";

    //Send Request to Server and Get Response
    $res = $api.CreatePayment($req);

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
    CreatePaymentRequest req = new CreatePaymentRequest();

    req.setPaymentDate(1);
    req.setAmount(1);
    req.setOrderKey("1");

    //Send Request to Server and Get Response
    CreatePaymentResponse res = api.getExigoApiSoap().createPayment(req, auth);

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

### CreatePaymentCreditCard

>  Creates a specific credit card payment for an existing order, or a new order in a transaction.
>  Note: This does not charge a card, and you must have an authorization code to submit this.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `POST /3.0/payment/creditcard` |
| SOAP action | `https://api.exigo.com/CreatePaymentCreditCard` |
| WSDL elements | `CreatePaymentCreditCardRequest` → `CreatePaymentCreditCardResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreatePaymentCreditCard |

#### Input

**`CreatePaymentCreditCardRequest`**

| Property | Type | Notes |
|---|---|---|
| `OrderID` | `Int32` | Unique numeric identifier for order record. |
| `PaymentDate` | `DateTime` |  |
| `Amount` | `Decimal` |  |
| `CreditCardNumber` | `String` |  |
| `ExpirationMonth` | `Int32` |  |
| `ExpirationYear` | `Int32` |  |
| `BillingName` | `String` | Optional. |
| `BillingAddress` | `String` | Optional. |
| `BillingAddress2` | `String` | Optional. |
| `BillingCity` | `String` | Optional. |
| `BillingState` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `BillingZip` | `String` | Optional. |
| `BillingCountry` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `CreditCardType` | `Int32` | Optional. Optionally pass in Visa, Master Card, etc.<br>**Lookup:** company-specific list (see company-lists.md) |
| `AuthorizationCode` | `String` |  |
| `Memo` | `String` | Optional. |
| `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided. |
| `MerchantTransactionKey` | `String` | Optional. |
| `MerchantTy` | `Int32` | Optional. . Defaults to 0. |
| `MerchantAccount` | `String` | Optional. |

#### Output

**`CreatePaymentCreditCardResponse`**

| Property | Type | Notes |
|---|---|---|
| `PaymentID` | `Int32` |  |
| `Message` | `String` |  |
| `DisplayMessage` | `String` |  |
| `MerchantTransactionKey` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/payment/creditcard HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "orderID": 1,
  "paymentDate": "2026-11-10T00:00:00-06:00",
  "amount": null,
  "creditCardNumber": "1",
  "expirationMonth": 1,
  "expirationYear": 1,
  "billingName": "",
  "billingAddress": "",
  "billingAddress2": "",
  "billingCity": "",
  "billingZip": "",
  "authorizationCode": "1",
  "memo": "",
  "orderKey": "1",
  "merchantTransactionKey": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "paymentID": 1,
  "message": "",
  "displayMessage": "",
  "merchantTransactionKey": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreatePaymentCreditCard"

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
    <CreatePaymentCreditCardRequest xmlns="http://api.exigo.com/">
      <OrderID>int</OrderID>
      <PaymentDate>dateTime</PaymentDate>
      <Amount>decimal</Amount>
      <CreditCardNumber>string</CreditCardNumber>
      <ExpirationMonth>int</ExpirationMonth>
      <ExpirationYear>int</ExpirationYear>
      <BillingName>string</BillingName>
      <BillingAddress>string</BillingAddress>
      <BillingAddress2>string</BillingAddress2>
      <BillingCity>string</BillingCity>
      <BillingState>string</BillingState>
      <BillingZip>string</BillingZip>
      <BillingCountry>string</BillingCountry>
      <CreditCardType>int</CreditCardType>
      <AuthorizationCode>string</AuthorizationCode>
      <Memo>string</Memo>
      <OrderKey>string</OrderKey>
      <MerchantTransactionKey>string</MerchantTransactionKey>
      <MerchantTy>int</MerchantTy>
      <MerchantAccount>string</MerchantAccount>
    </CreatePaymentCreditCardRequest>
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
    <CreatePaymentCreditCardResult xmlns="http://api.exigo.com/" />
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
    var req = new CreatePaymentCreditCardRequest();

    req.OrderID = 1;                //Unique numeric identifier for order record.
    req.PaymentDate = DateTime.Today;
    req.Amount = 1;
    req.CreditCardNumber = "1";
    req.ExpirationMonth = 1;
    req.ExpirationYear = 1;
    req.BillingName = "1";
    req.BillingAddress = "1";
    req.BillingAddress2 = "1";
    req.BillingCity = "1";
    req.BillingZip = "1";
    req.AuthorizationCode = "1";
    req.Memo = "1";
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.
    req.MerchantTransactionKey = "1";

    //Send Request to Server and Get Response
    var res = await api.CreatePaymentCreditCardAsync(req);

    //Now examine the results:
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
    CreatePaymentCreditCardRequest req = new CreatePaymentCreditCardRequest();

    req.OrderID = 1;                //Unique numeric identifier for order record.
    req.PaymentDate = DateTime.Today;
    req.Amount = 1;
    req.CreditCardNumber = "1";
    req.ExpirationMonth = 1;
    req.ExpirationYear = 1;
    req.BillingName = "1";
    req.BillingAddress = "1";
    req.BillingAddress2 = "1";
    req.BillingCity = "1";
    req.BillingZip = "1";
    req.AuthorizationCode = "1";
    req.Memo = "1";
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.
    req.MerchantTransactionKey = "1";

    //Send Request to Server and Get Response
    CreatePaymentCreditCardResponse res = api.CreatePaymentCreditCard(req);

    //Now examine the results:
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
    Dim req as new CreatePaymentCreditCardRequest()

    req.OrderID = 1
    req.PaymentDate = DateTime.Today
    req.Amount = 1
    req.CreditCardNumber = "1"
    req.ExpirationMonth = 1
    req.ExpirationYear = 1
    req.BillingName = "1"
    req.BillingAddress = "1"
    req.BillingAddress2 = "1"
    req.BillingCity = "1"
    req.BillingZip = "1"
    req.AuthorizationCode = "1"
    req.Memo = "1"
    req.OrderKey = "1"
    req.MerchantTransactionKey = "1"

    'Send Request to Server and Get Response
    Dim res As CreatePaymentCreditCardResponse = api.CreatePaymentCreditCard(req)

    'Now examine the results:
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

    $req->OrderID = 1;
    $req->PaymentDate = 1;
    $req->Amount = 1;
    $req->CreditCardNumber = "1";
    $req->ExpirationMonth = 1;
    $req->ExpirationYear = 1;
    $req->BillingName = "1";
    $req->BillingAddress = "1";
    $req->BillingAddress2 = "1";
    $req->BillingCity = "1";
    $req->BillingZip = "1";
    $req->AuthorizationCode = "1";
    $req->Memo = "1";
    $req->OrderKey = "1";
    $req->MerchantTransactionKey = "1";

    //Send Request to Server and Get Response
    $res = $api.CreatePaymentCreditCard($req);

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
    CreatePaymentCreditCardRequest req = new CreatePaymentCreditCardRequest();

    req.setOrderID(1);
    req.setPaymentDate(1);
    req.setAmount(1);
    req.setCreditCardNumber("1");
    req.setExpirationMonth(1);
    req.setExpirationYear(1);
    req.setBillingName("1");
    req.setBillingAddress("1");
    req.setBillingAddress2("1");
    req.setBillingCity("1");
    req.setBillingZip("1");
    req.setAuthorizationCode("1");
    req.setMemo("1");
    req.setOrderKey("1");
    req.setMerchantTransactionKey("1");

    //Send Request to Server and Get Response
    CreatePaymentCreditCardResponse res = api.getExigoApiSoap().createPaymentCreditCard(req, auth);

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

### CreatePaymentWallet

> Creates a new payment for wallet account.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `POST /3.0/payment/wallet` |
| SOAP action | `https://api.exigo.com/CreatePaymentWallet` |
| WSDL elements | `CreatePaymentWalletRequest` → `CreatePaymentWalletResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreatePaymentWallet |

#### Input

**`CreatePaymentWalletRequest`**

| Property | Type | Notes |
|---|---|---|
| `OrderID` | `Int32` | Unique numeric identifier for order record. |
| `PaymentDate` | `DateTime` |  |
| `Amount` | `Decimal` |  |
| `WalletType` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| `WalletAccount` | `String` | Optional. |
| `AuthorizationCode` | `String` | Optional. |
| `Memo` | `String` | Optional. |
| `BillingName` | `String` | Optional. |
| `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided. |
| `MerchantTy` | `Int32` | Optional. . Defaults to 0. |
| `MerchantAccount` | `String` | Optional. |
| `MerchantTransactionKey` | `String` | Optional. |

#### Output

**`CreatePaymentResponse`**

| Property | Type | Notes |
|---|---|---|
| `PaymentID` | `Int32` |  |
| `Message` | `String` |  |
| `DisplayMessage` | `String` |  |
| `MerchantTransactionKey` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/payment/wallet HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "paymentDate": "2026-11-10T00:00:00-06:00",
  "amount": null,
  "walletAccount": "",
  "authorizationCode": "",
  "memo": "",
  "billingName": "",
  "orderKey": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "paymentID": 1,
  "message": "",
  "displayMessage": "",
  "merchantTransactionKey": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreatePaymentWallet"

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
    <CreatePaymentWalletRequest xmlns="http://api.exigo.com/">
      <OrderID>int</OrderID>
      <PaymentDate>dateTime</PaymentDate>
      <Amount>decimal</Amount>
      <WalletType>int</WalletType>
      <WalletAccount>string</WalletAccount>
      <AuthorizationCode>string</AuthorizationCode>
      <Memo>string</Memo>
      <BillingName>string</BillingName>
      <OrderKey>string</OrderKey>
      <MerchantTy>int</MerchantTy>
      <MerchantAccount>string</MerchantAccount>
      <MerchantTransactionKey>string</MerchantTransactionKey>
    </CreatePaymentWalletRequest>
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
    <CreatePaymentWalletResult xmlns="http://api.exigo.com/">
      <PaymentID>int</PaymentID>
      <Message>string</Message>
      <DisplayMessage>string</DisplayMessage>
      <MerchantTransactionKey>string</MerchantTransactionKey>
    </CreatePaymentWalletResult>
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
    var req = new CreatePaymentWalletRequest();

    req.PaymentDate = DateTime.Today;
    req.Amount = 1;
    req.WalletAccount = "1";
    req.AuthorizationCode = "1";
    req.Memo = "1";
    req.BillingName = "1";
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    var res = await api.CreatePaymentWalletAsync(req);

    //Now examine the results:
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
    CreatePaymentWalletRequest req = new CreatePaymentWalletRequest();

    req.PaymentDate = DateTime.Today;
    req.Amount = 1;
    req.WalletAccount = "1";
    req.AuthorizationCode = "1";
    req.Memo = "1";
    req.BillingName = "1";
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    CreatePaymentResponse res = api.CreatePaymentWallet(req);

    //Now examine the results:
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
    Dim req as new CreatePaymentWalletRequest()

    req.PaymentDate = DateTime.Today
    req.Amount = 1
    req.WalletAccount = "1"
    req.AuthorizationCode = "1"
    req.Memo = "1"
    req.BillingName = "1"
    req.OrderKey = "1"

    'Send Request to Server and Get Response
    Dim res As CreatePaymentResponse = api.CreatePaymentWallet(req)

    'Now examine the results:
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

    $req->PaymentDate = 1;
    $req->Amount = 1;
    $req->WalletAccount = "1";
    $req->AuthorizationCode = "1";
    $req->Memo = "1";
    $req->BillingName = "1";
    $req->OrderKey = "1";

    //Send Request to Server and Get Response
    $res = $api.CreatePaymentWallet($req);

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
    CreatePaymentWalletRequest req = new CreatePaymentWalletRequest();

    req.setPaymentDate(1);
    req.setAmount(1);
    req.setWalletAccount("1");
    req.setAuthorizationCode("1");
    req.setMemo("1");
    req.setBillingName("1");
    req.setOrderKey("1");

    //Send Request to Server and Get Response
    CreatePaymentResponse res = api.getExigoApiSoap().createPaymentWallet(req, auth);

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

### CreatePaymentPointAccount

> Creates a new payment for point account.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `POST /3.0/payment/pointaccount` |
| SOAP action | `https://api.exigo.com/CreatePaymentPointAccount` |
| WSDL elements | `CreatePaymentPointAccountRequest` → `CreatePaymentPointAccountResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreatePaymentPointAccount |

#### Input

**`CreatePaymentPointAccountRequest`**

| Property | Type | Notes |
|---|---|---|
| `OrderID` | `Int32` | Unique numeric identifier for order record. |
| `PointAccountID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| `PaymentDate` | `DateTime` |  |
| `Amount` | `Decimal` |  |
| `Memo` | `String` | Optional. |
| `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided. |

#### Output

**`CreatePaymentPointAccountResponse`**

| Property | Type | Notes |
|---|---|---|
| `PaymentID` | `Int32` |  |
| `Message` | `String` |  |
| `DisplayMessage` | `String` |  |
| `MerchantTransactionKey` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/payment/pointaccount HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "pointAccountID": 1,
  "paymentDate": "2026-11-10T00:00:00-06:00",
  "amount": null,
  "orderKey": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "paymentID": 1,
  "message": "",
  "displayMessage": "",
  "merchantTransactionKey": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreatePaymentPointAccount"

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
    <CreatePaymentPointAccountRequest xmlns="http://api.exigo.com/">
      <OrderID>int</OrderID>
      <PointAccountID>int</PointAccountID>
      <PaymentDate>dateTime</PaymentDate>
      <Amount>decimal</Amount>
      <Memo>string</Memo>
      <OrderKey>string</OrderKey>
    </CreatePaymentPointAccountRequest>
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
    <CreatePaymentPointAccountResult xmlns="http://api.exigo.com/" />
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
    var req = new CreatePaymentPointAccountRequest();

    req.PointAccountID = 1;
    req.PaymentDate = DateTime.Today;
    req.Amount = 1;
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    var res = await api.CreatePaymentPointAccountAsync(req);

    //Now examine the results:
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
    CreatePaymentPointAccountRequest req = new CreatePaymentPointAccountRequest();

    req.PointAccountID = 1;
    req.PaymentDate = DateTime.Today;
    req.Amount = 1;
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    CreatePaymentPointAccountResponse res = api.CreatePaymentPointAccount(req);

    //Now examine the results:
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
    Dim req as new CreatePaymentPointAccountRequest()

    req.PointAccountID = 1
    req.PaymentDate = DateTime.Today
    req.Amount = 1
    req.OrderKey = "1"

    'Send Request to Server and Get Response
    Dim res As CreatePaymentPointAccountResponse = api.CreatePaymentPointAccount(req)

    'Now examine the results:
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

    $req->PointAccountID = 1;
    $req->PaymentDate = 1;
    $req->Amount = 1;
    $req->OrderKey = "1";

    //Send Request to Server and Get Response
    $res = $api.CreatePaymentPointAccount($req);

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
    CreatePaymentPointAccountRequest req = new CreatePaymentPointAccountRequest();

    req.setPointAccountID(1);
    req.setPaymentDate(1);
    req.setAmount(1);
    req.setOrderKey("1");

    //Send Request to Server and Get Response
    CreatePaymentPointAccountResponse res = api.getExigoApiSoap().createPaymentPointAccount(req, auth);

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

### CreatePaymentCheck

> Creates a new payment using check information.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `POST /3.0/payment/check` |
| SOAP action | `https://api.exigo.com/CreatePaymentCheck` |
| WSDL elements | `CreatePaymentCheckRequest` → `CreatePaymentCheckResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreatePaymentCheck |

#### Input

**`CreatePaymentCheckRequest`**

| Property | Type | Notes |
|---|---|---|
| `OrderID` | `Int32` | Unique numeric identifier for order record. |
| `PaymentDate` | `DateTime` |  |
| `Amount` | `Decimal` |  |
| `Memo` | `String` | Optional. |
| `CheckNumber` | `String` | Optional. |
| `CheckAccountNumber` | `String` | Optional. |
| `CheckRoutingNumber` | `String` | Optional. |
| `CheckDate` | `DateTime` | Optional. |
| `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided. |
| `MerchantTy` | `Int32` | Optional. . Defaults to 0. |
| `MerchantAccount` | `String` | Optional. |
| `MerchantTransactionKey` | `String` | Optional. |
| `PayeeName` | `String` | Optional. |

#### Output

**`CreatePaymentCheckResponse`**

| Property | Type | Notes |
|---|---|---|
| `PaymentID` | `Int32` |  |
| `Message` | `String` |  |
| `DisplayMessage` | `String` |  |
| `MerchantTransactionKey` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/payment/check HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "paymentDate": "2026-11-10T00:00:00-06:00",
  "amount": null,
  "orderKey": "1",
  "payeeName": ""
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "paymentID": 1,
  "message": "",
  "displayMessage": "",
  "merchantTransactionKey": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreatePaymentCheck"

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
    <CreatePaymentCheckRequest xmlns="http://api.exigo.com/">
      <OrderID>int</OrderID>
      <PaymentDate>dateTime</PaymentDate>
      <Amount>decimal</Amount>
      <Memo>string</Memo>
      <CheckNumber>string</CheckNumber>
      <CheckAccountNumber>string</CheckAccountNumber>
      <CheckRoutingNumber>string</CheckRoutingNumber>
      <CheckDate>dateTime</CheckDate>
      <OrderKey>string</OrderKey>
      <MerchantTy>int</MerchantTy>
      <MerchantAccount>string</MerchantAccount>
      <MerchantTransactionKey>string</MerchantTransactionKey>
      <PayeeName>string</PayeeName>
    </CreatePaymentCheckRequest>
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
    <CreatePaymentCheckResult xmlns="http://api.exigo.com/" />
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
    var req = new CreatePaymentCheckRequest();

    req.PaymentDate = DateTime.Today;
    req.Amount = 1;
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.
    req.PayeeName = "1";

    //Send Request to Server and Get Response
    var res = await api.CreatePaymentCheckAsync(req);

    //Now examine the results:
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
    CreatePaymentCheckRequest req = new CreatePaymentCheckRequest();

    req.PaymentDate = DateTime.Today;
    req.Amount = 1;
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.
    req.PayeeName = "1";

    //Send Request to Server and Get Response
    CreatePaymentCheckResponse res = api.CreatePaymentCheck(req);

    //Now examine the results:
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
    Dim req as new CreatePaymentCheckRequest()

    req.PaymentDate = DateTime.Today
    req.Amount = 1
    req.OrderKey = "1"
    req.PayeeName = "1"

    'Send Request to Server and Get Response
    Dim res As CreatePaymentCheckResponse = api.CreatePaymentCheck(req)

    'Now examine the results:
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

    $req->PaymentDate = 1;
    $req->Amount = 1;
    $req->OrderKey = "1";
    $req->PayeeName = "1";

    //Send Request to Server and Get Response
    $res = $api.CreatePaymentCheck($req);

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
    CreatePaymentCheckRequest req = new CreatePaymentCheckRequest();

    req.setPaymentDate(1);
    req.setAmount(1);
    req.setOrderKey("1");
    req.setPayeeName("1");

    //Send Request to Server and Get Response
    CreatePaymentCheckResponse res = api.getExigoApiSoap().createPaymentCheck(req, auth);

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

### ChargeCreditCardToken

>  Attempts to charge a card token with the amount found on an exiting order,
>  or a new order in a transaction.If the charge is successful, the order is changed to accepted.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `POST /3.0/payment/charge/token` |
| SOAP action | `https://api.exigo.com/ChargeCreditCardToken` |
| WSDL elements | `ChargeCreditCardTokenRequest` → `ChargeCreditCardTokenResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=ChargeCreditCardToken |

#### Input

**`ChargeCreditCardTokenRequest`**

| Property | Type | Notes |
|---|---|---|
| `CreditCardToken` | `String` | Optional. |
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
| `ExpirationMonth` | `Int32` | Optional. |
| `ExpirationYear` | `Int32` | Optional. |
| `OrderID` | `Int32` | Unique numeric identifier for order record. |
| `MaxAmount` | `Decimal` | Optional. Only use if you are applying multiple payments. |
| `MerchantWarehouseIDOverride` | `Int32` | Optional. Use to override the warehouse used for merchant selection. |
| `ClientIPAddress` | `String` | Optional. |
| `OtherData1` | `String` | Optional. Use for some merchants to pass additional data. |
| `OtherData2` | `String` | Optional. Use for some merchants to pass additional data. |
| `OtherData3` | `String` | Optional. Use for some merchants to pass additional data. |
| `OtherData4` | `String` | Optional. Use for some merchants to pass additional data. |
| `OtherData5` | `String` | Optional. Use for some merchants to pass additional data. |
| `OtherData6` | `String` | Optional. Use for some merchants to pass additional data. |
| `OtherData7` | `String` | Optional. Use for some merchants to pass additional data. |
| `OtherData8` | `String` | Optional. Use for some merchants to pass additional data. |
| `OtherData9` | `String` | Optional. Use for some merchants to pass additional data. |
| `OtherData10` | `String` | Optional. Use for some merchants to pass additional data. |
| `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided. |
| `Phone` | `String` | Optional. |
| `Email` | `String` | Optional. |

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

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/payment/charge/token HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "creditCardToken": "",
  "billingName": "",
  "billingAddress": "",
  "billingAddress2": "",
  "billingCity": "",
  "billingZip": "",
  "expirationMonth": 1,
  "expirationYear": 1,
  "orderKey": "1",
  "phone": "",
  "email": ""
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "amount": null,
  "authorizationCode": "",
  "paymentID": 1,
  "message": "",
  "displayMessage": "",
  "merchantTransactionKey": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/ChargeCreditCardToken"

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
    <ChargeCreditCardTokenRequest xmlns="http://api.exigo.com/">
      <CreditCardToken>string</CreditCardToken>
      <BillingName>string</BillingName>
      <BillingAddress>string</BillingAddress>
      <BillingAddress2>string</BillingAddress2>
      <BillingCity>string</BillingCity>
      <BillingState>string</BillingState>
      <BillingZip>string</BillingZip>
      <BillingCountry>string</BillingCountry>
      <CvcCode>string</CvcCode>
      <IssueNumber>string</IssueNumber>
      <CreditCardType>int</CreditCardType>
      <ExpirationMonth>int</ExpirationMonth>
      <ExpirationYear>int</ExpirationYear>
      <OrderID>int</OrderID>
      <MaxAmount>decimal</MaxAmount>
      <MerchantWarehouseIDOverride>int</MerchantWarehouseIDOverride>
      <ClientIPAddress>string</ClientIPAddress>
      <OtherData1>string</OtherData1>
      <OtherData2>string</OtherData2>
      <OtherData3>string</OtherData3>
      <OtherData4>string</OtherData4>
      <OtherData5>string</OtherData5>
      <OtherData6>string</OtherData6>
      <OtherData7>string</OtherData7>
      <OtherData8>string</OtherData8>
      <OtherData9>string</OtherData9>
      <OtherData10>string</OtherData10>
      <OrderKey>string</OrderKey>
      <Phone>string</Phone>
      <Email>string</Email>
    </ChargeCreditCardTokenRequest>
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
    <ChargeCreditCardTokenResult xmlns="http://api.exigo.com/">
      <Amount>decimal</Amount>
      <AuthorizationCode>string</AuthorizationCode>
    </ChargeCreditCardTokenResult>
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
    var req = new ChargeCreditCardTokenRequest();

    req.CreditCardToken = "1";
    req.BillingName = "1";
    req.BillingAddress = "1";
    req.BillingAddress2 = "1";
    req.BillingCity = "1";
    req.BillingZip = "1";
    req.ExpirationMonth = 1;
    req.ExpirationYear = 1;
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.
    req.Phone = "1";
    req.Email = "1";

    //Send Request to Server and Get Response
    var res = await api.ChargeCreditCardTokenAsync(req);

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
    ChargeCreditCardTokenRequest req = new ChargeCreditCardTokenRequest();

    req.CreditCardToken = "1";
    req.BillingName = "1";
    req.BillingAddress = "1";
    req.BillingAddress2 = "1";
    req.BillingCity = "1";
    req.BillingZip = "1";
    req.ExpirationMonth = 1;
    req.ExpirationYear = 1;
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.
    req.Phone = "1";
    req.Email = "1";

    //Send Request to Server and Get Response
    ChargeCreditCardResponse res = api.ChargeCreditCardToken(req);

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
    Dim req as new ChargeCreditCardTokenRequest()

    req.CreditCardToken = "1"
    req.BillingName = "1"
    req.BillingAddress = "1"
    req.BillingAddress2 = "1"
    req.BillingCity = "1"
    req.BillingZip = "1"
    req.ExpirationMonth = 1
    req.ExpirationYear = 1
    req.OrderKey = "1"
    req.Phone = "1"
    req.Email = "1"

    'Send Request to Server and Get Response
    Dim res As ChargeCreditCardResponse = api.ChargeCreditCardToken(req)

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

    $req->CreditCardToken = "1";
    $req->BillingName = "1";
    $req->BillingAddress = "1";
    $req->BillingAddress2 = "1";
    $req->BillingCity = "1";
    $req->BillingZip = "1";
    $req->ExpirationMonth = 1;
    $req->ExpirationYear = 1;
    $req->OrderKey = "1";
    $req->Phone = "1";
    $req->Email = "1";

    //Send Request to Server and Get Response
    $res = $api.ChargeCreditCardToken($req);

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
    ChargeCreditCardTokenRequest req = new ChargeCreditCardTokenRequest();

    req.setCreditCardToken("1");
    req.setBillingName("1");
    req.setBillingAddress("1");
    req.setBillingAddress2("1");
    req.setBillingCity("1");
    req.setBillingZip("1");
    req.setExpirationMonth(1);
    req.setExpirationYear(1);
    req.setOrderKey("1");
    req.setPhone("1");
    req.setEmail("1");

    //Send Request to Server and Get Response
    ChargeCreditCardResponse res = api.getExigoApiSoap().chargeCreditCardToken(req, auth);

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

### ChargeCreditCardTokenOnFile

>  Attempts to charge a card token on file with the amount found on an
>  exiting order, or a new order in a transaction. If the charge is successful, the order is changed to accepted.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `POST /3.0/payment/charge/tokenonfile` |
| SOAP action | `https://api.exigo.com/ChargeCreditCardTokenOnFile` |
| WSDL elements | `ChargeCreditCardTokenOnFileRequest` → `ChargeCreditCardTokenOnFileResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=ChargeCreditCardTokenOnFile |

#### Input

**`ChargeCreditCardTokenOnFileRequest`**

| Property | Type | Notes |
|---|---|---|
| `CreditCardAccountType` | `AccountCreditCardType` | **Values:** `Primary`, `Secondary` |
| `OrderID` | `Int32` | Unique numeric identifier for order record. |
| `CvcCode` | `String` | Optional. |
| `MaxAmount` | `Decimal` | Optional. Only use if you are applying multiple payments. |
| `MerchantWarehouseIDOverride` | `Int32` | Optional. Use to override the warehouse used for merchant selection. |
| `ClientIPAddress` | `String` | Optional. |
| `OtherData1` | `String` | Optional. Use for some merchants to pass additional data. |
| `OtherData2` | `String` | Optional. Use for some merchants to pass additional data. |
| `OtherData3` | `String` | Optional. Use for some merchants to pass additional data. |
| `OtherData4` | `String` | Optional. Use for some merchants to pass additional data. |
| `OtherData5` | `String` | Optional. Use for some merchants to pass additional data. |
| `OtherData6` | `String` | Optional. Use for some merchants to pass additional data. |
| `OtherData7` | `String` | Optional. Use for some merchants to pass additional data. |
| `OtherData8` | `String` | Optional. Use for some merchants to pass additional data. |
| `OtherData9` | `String` | Optional. Use for some merchants to pass additional data. |
| `OtherData10` | `String` | Optional. Use for some merchants to pass additional data. |
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

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/payment/charge/tokenonfile HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "creditCardAccountType": null,
  "orderKey": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "amount": null,
  "authorizationCode": "",
  "paymentID": 1,
  "message": "",
  "displayMessage": "",
  "merchantTransactionKey": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/ChargeCreditCardTokenOnFile"

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
    <ChargeCreditCardTokenOnFileRequest xmlns="http://api.exigo.com/">
      <CreditCardAccountType>Primary or Secondary</CreditCardAccountType>
      <OrderID>int</OrderID>
      <CvcCode>string</CvcCode>
      <MaxAmount>decimal</MaxAmount>
      <MerchantWarehouseIDOverride>int</MerchantWarehouseIDOverride>
      <ClientIPAddress>string</ClientIPAddress>
      <OtherData1>string</OtherData1>
      <OtherData2>string</OtherData2>
      <OtherData3>string</OtherData3>
      <OtherData4>string</OtherData4>
      <OtherData5>string</OtherData5>
      <OtherData6>string</OtherData6>
      <OtherData7>string</OtherData7>
      <OtherData8>string</OtherData8>
      <OtherData9>string</OtherData9>
      <OtherData10>string</OtherData10>
      <OrderKey>string</OrderKey>
    </ChargeCreditCardTokenOnFileRequest>
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
    <ChargeCreditCardTokenOnFileResult xmlns="http://api.exigo.com/">
      <Amount>decimal</Amount>
      <AuthorizationCode>string</AuthorizationCode>
    </ChargeCreditCardTokenOnFileResult>
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
    var req = new ChargeCreditCardTokenOnFileRequest();

    req.CreditCardAccountType = AccountCreditCardType.Primary;
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    var res = await api.ChargeCreditCardTokenOnFileAsync(req);

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
    ChargeCreditCardTokenOnFileRequest req = new ChargeCreditCardTokenOnFileRequest();

    req.CreditCardAccountType = AccountCreditCardType.Primary;
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    ChargeCreditCardResponse res = api.ChargeCreditCardTokenOnFile(req);

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
    Dim req as new ChargeCreditCardTokenOnFileRequest()

    req.CreditCardAccountType = AccountCreditCardType.Primary
    req.OrderKey = "1"

    'Send Request to Server and Get Response
    Dim res As ChargeCreditCardResponse = api.ChargeCreditCardTokenOnFile(req)

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
    $req->OrderKey = "1";

    //Send Request to Server and Get Response
    $res = $api.ChargeCreditCardTokenOnFile($req);

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
    ChargeCreditCardTokenOnFileRequest req = new ChargeCreditCardTokenOnFileRequest();

    req.setCreditCardAccountType(1);
    req.setOrderKey("1");

    //Send Request to Server and Get Response
    ChargeCreditCardResponse res = api.getExigoApiSoap().chargeCreditCardTokenOnFile(req, auth);

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

### ChargeGroupOrderCreditCardToken

>  Attempts to charge a card token with the amount found on the specified orders.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `POST /3.0/payment/charge/tokengroup` |
| SOAP action | `https://api.exigo.com/ChargeGroupOrderCreditCardToken` |
| WSDL elements | `ChargeGroupOrderCreditCardTokenRequest` → `ChargeGroupOrderCreditCardTokenResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=ChargeGroupOrderCreditCardToken |

#### Input

**`ChargeGroupOrderCreditCardTokenRequest`**

| Property | Type | Notes |
|---|---|---|
| `CreditCardToken` | `String` | Optional. |
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
| `MasterOrderID` | `Int32` | Unique numeric identifier for master order record. |
| `Orders` | `GroupOrder[]` |  |
| `MerchantWarehouseIDOverride` | `Int32` | Optional. Use to override the warehouse used for merchant selection. |
| `ClientIPAddress` | `String` | Optional. |
| `OtherData1` | `String` | Optional. Use for some merchants to pass additional data. |
| `OtherData2` | `String` | Optional. Use for some merchants to pass additional data. |
| `OtherData3` | `String` | Optional. Use for some merchants to pass additional data. |
| `OtherData4` | `String` | Optional. Use for some merchants to pass additional data. |
| `OtherData5` | `String` | Optional. Use for some merchants to pass additional data. |
| `OtherData6` | `String` | Optional. Use for some merchants to pass additional data. |
| `OtherData7` | `String` | Optional. Use for some merchants to pass additional data. |
| `OtherData8` | `String` | Optional. Use for some merchants to pass additional data. |
| `OtherData9` | `String` | Optional. Use for some merchants to pass additional data. |
| `OtherData10` | `String` | Optional. Use for some merchants to pass additional data. |
| `PaymentMemo` | `String` | Optional. Used to specify the memo on the generated payment records for successful transactions. |
| `MasterOrderKey` | `String` | Optional. Unique alpha numeric identifier for master order record. Exeption will occur if MasterOrderID & MasterOrderKey are provided. |

**`GroupOrder`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `OrderID` | `Int32` | Unique numeric identifier for order record. |
| &nbsp;&nbsp;↳ `MaxAmount` | `Decimal` | Optional. |
| &nbsp;&nbsp;↳ `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided. |

#### Output

**`ChargeGroupOrderCreditCardTokenResponse`**

| Property | Type | Notes |
|---|---|---|
| `Amount` | `Decimal` |  |
| `AuthorizationCode` | `String` |  |
| `Payments` | `PaymentsResponse` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/payment/charge/tokengroup HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "creditCardToken": "",
  "billingName": "",
  "billingAddress": "",
  "billingAddress2": "",
  "billingCity": "",
  "billingZip": "",
  "cvcCode": "",
  "issueNumber": "",
  "orders": null,
  "clientIPAddress": "",
  "masterOrderKey": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "amount": null,
  "authorizationCode": "",
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
SOAPAction: "https://api.exigo.com/ChargeGroupOrderCreditCardToken"

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
    <ChargeGroupOrderCreditCardTokenRequest xmlns="http://api.exigo.com/">
      <_orders>
        <GroupOrder>
          <OrderID>int</OrderID>
          <MaxAmount>decimal</MaxAmount>
          <OrderKey>string</OrderKey>
        </GroupOrder>
      </_orders>
      <CreditCardToken>string</CreditCardToken>
      <BillingName>string</BillingName>
      <BillingAddress>string</BillingAddress>
      <BillingAddress2>string</BillingAddress2>
      <BillingCity>string</BillingCity>
      <BillingState>string</BillingState>
      <BillingZip>string</BillingZip>
      <BillingCountry>string</BillingCountry>
      <CvcCode>string</CvcCode>
      <IssueNumber>string</IssueNumber>
      <CreditCardType>int</CreditCardType>
      <MasterOrderID>int</MasterOrderID>
      <Orders>
        <GroupOrder>
          <OrderID>int</OrderID>
          <MaxAmount>decimal</MaxAmount>
          <OrderKey>string</OrderKey>
        </GroupOrder>
      </Orders>
      <MerchantWarehouseIDOverride>int</MerchantWarehouseIDOverride>
      <ClientIPAddress>string</ClientIPAddress>
      <OtherData1>string</OtherData1>
      <OtherData2>string</OtherData2>
      <OtherData3>string</OtherData3>
      <OtherData4>string</OtherData4>
      <OtherData5>string</OtherData5>
      <OtherData6>string</OtherData6>
      <OtherData7>string</OtherData7>
      <OtherData8>string</OtherData8>
      <OtherData9>string</OtherData9>
      <OtherData10>string</OtherData10>
      <PaymentMemo>string</PaymentMemo>
      <MasterOrderKey>string</MasterOrderKey>
    </ChargeGroupOrderCreditCardTokenRequest>
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
    <ChargeGroupOrderCreditCardTokenResult xmlns="http://api.exigo.com/">
      <_paymentIDs>
        <PaymentsResponse>
          <_PaymentID>int</_PaymentID>
          <_OrderID>int</_OrderID>
        </PaymentsResponse>
      </_paymentIDs>
      <Amount>decimal</Amount>
      <AuthorizationCode>string</AuthorizationCode>
      <Payments>
        <PaymentsResponse>
          <_PaymentID>int</_PaymentID>
          <_OrderID>int</_OrderID>
        </PaymentsResponse>
      </Payments>
    </ChargeGroupOrderCreditCardTokenResult>
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
    var req = new ChargeGroupOrderCreditCardTokenRequest();

    req.CreditCardToken = "1";
    req.BillingName = "1";
    req.BillingAddress = "1";
    req.BillingAddress2 = "1";
    req.BillingCity = "1";
    req.BillingZip = "1";
    req.CvcCode = "1";
    req.IssueNumber = "1";

    //Add Orders
    var orders = new List<GroupOrder>();

    var order1 = new GroupOrder();
    order1.MaxAmount = 1;
    order1.OrderKey = "1";
    orders.Add(order1);

    var order2 = new GroupOrder();
    order2.MaxAmount = 2;
    order2.OrderKey = "2";
    orders.Add(order2);

    //Now attach the list to the request
    req.Orders = orders.ToArray();
    req.ClientIPAddress = "1";
    req.MasterOrderKey = "1";       //Unique alpha numeric identifier for master  order record. Exeption will occur if MasterOrderID & MasterOrderKey are provided.

    //Send Request to Server and Get Response
    var res = await api.ChargeGroupOrderCreditCardTokenAsync(req);

    //Now examine the results:
    Console.WriteLine("Amount: {0}", res.Amount);
    Console.WriteLine("AuthorizationCode: {0}", res.AuthorizationCode);
    Console.WriteLine("Payments: {0}", res.Payments);
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
    ChargeGroupOrderCreditCardTokenRequest req = new ChargeGroupOrderCreditCardTokenRequest();

    req.CreditCardToken = "1";
    req.BillingName = "1";
    req.BillingAddress = "1";
    req.BillingAddress2 = "1";
    req.BillingCity = "1";
    req.BillingZip = "1";
    req.CvcCode = "1";
    req.IssueNumber = "1";

    //Add Orders
    List<GroupOrder> orders = new List<GroupOrder>();

    GroupOrder order1 = new GroupOrder();
    order1.MaxAmount = 1;
    order1.OrderKey = "1";
    orders.Add(order1);

    GroupOrder order2 = new GroupOrder();
    order2.MaxAmount = 2;
    order2.OrderKey = "2";
    orders.Add(order2);

    //Now attach the list to the request
    req.Orders = orders.ToArray();
    req.ClientIPAddress = "1";
    req.MasterOrderKey = "1";       //Unique alpha numeric identifier for master  order record. Exeption will occur if MasterOrderID & MasterOrderKey are provided.

    //Send Request to Server and Get Response
    ChargeGroupOrderCreditCardTokenResponse res = api.ChargeGroupOrderCreditCardToken(req);

    //Now examine the results:
    Console.WriteLine("Amount: {0}", res.Amount);
    Console.WriteLine("AuthorizationCode: {0}", res.AuthorizationCode);
    Console.WriteLine("Payments: {0}", res.Payments);
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
    Dim req as new ChargeGroupOrderCreditCardTokenRequest()

    req.CreditCardToken = "1"
    req.BillingName = "1"
    req.BillingAddress = "1"
    req.BillingAddress2 = "1"
    req.BillingCity = "1"
    req.BillingZip = "1"
    req.CvcCode = "1"
    req.IssueNumber = "1"

    'Add Orders
    Dim orders As New List(Of GroupOrder)()

    Dim order1 as new GroupOrder()
    order1.MaxAmount = 1
    order1.OrderKey = "1"
    orders.Add(order1)

    Dim order2 as new GroupOrder()
    order2.MaxAmount = 2
    order2.OrderKey = "2"
    orders.Add(order2)

    'Now attach the list to the request
    req.Orders = orders.ToArray()
    req.ClientIPAddress = "1"
    req.MasterOrderKey = "1"

    'Send Request to Server and Get Response
    Dim res As ChargeGroupOrderCreditCardTokenResponse = api.ChargeGroupOrderCreditCardToken(req)

    'Now examine the results:
    Console.WriteLine("Amount: {0}", res.Amount)
    Console.WriteLine("AuthorizationCode: {0}", res.AuthorizationCode)
    Console.WriteLine("Payments: {0}", res.Payments)
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

    $req->CreditCardToken = "1";
    $req->BillingName = "1";
    $req->BillingAddress = "1";
    $req->BillingAddress2 = "1";
    $req->BillingCity = "1";
    $req->BillingZip = "1";
    $req->CvcCode = "1";
    $req->IssueNumber = "1";

    //Add Orders

    $order1->MaxAmount = 1;
    $order1->OrderKey = "1";

    $order2->MaxAmount = 2;
    $order2->OrderKey = "2";

    //Now attach the list to the request
    req.Orders = array(order1,order2);
    $req->ClientIPAddress = "1";
    $req->MasterOrderKey = "1";

    //Send Request to Server and Get Response
    $res = $api.ChargeGroupOrderCreditCardToken($req);

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
    ChargeGroupOrderCreditCardTokenRequest req = new ChargeGroupOrderCreditCardTokenRequest();

    req.setCreditCardToken("1");
    req.setBillingName("1");
    req.setBillingAddress("1");
    req.setBillingAddress2("1");
    req.setBillingCity("1");
    req.setBillingZip("1");
    req.setCvcCode("1");
    req.setIssueNumber("1");

    //Add Orders
    ArrayOfGroupOrder orders = new ArrayOfGroupOrder();

    GroupOrder order1 = new GroupOrder();
    order1.setMaxAmount(1);
    order1.setOrderKey("1");
    orders.Add(order1);

    GroupOrder order2 = new GroupOrder();
    order2.setMaxAmount(2);
    order2.setOrderKey("2");
    orders.Add(order2);

    //Now attach the list to the request
    req.setOrders(orders);
    req.setClientIPAddress("1");
    req.setMasterOrderKey("1");

    //Send Request to Server and Get Response
    ChargeGroupOrderCreditCardTokenResponse res = api.getExigoApiSoap().chargeGroupOrderCreditCardToken(req, auth);

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

### RefundPriorCreditCardCharge

> Refunds a prior charge. To be used with an order.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `POST /3.0/payment/refund/cc` |
| SOAP action | `https://api.exigo.com/RefundPriorCreditCardCharge` |
| WSDL elements | `RefundPriorCreditCardChargeRequest` → `RefundPriorCreditCardChargeResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=RefundPriorCreditCardCharge |

#### Input

**`RefundPriorCreditCardChargeRequest`**

| Property | Type | Notes |
|---|---|---|
| `ReturnPaymentID` | `Int32` |  |
| `OrderID` | `Int32` | Unique numeric identifier for order record. |
| `RefundOriginalOrder` | `Boolean` | Optional. Boolean value that allows payment to be applied directly to the original sales order. Defaults to False. |
| `MaxAmount` | `Decimal` | Optional. |
| `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided. |

#### Output

**`RefundPriorCreditCardChargeResponse`**

| Property | Type | Notes |
|---|---|---|
| `Amount` | `Decimal` |  |
| `AuthorizationCode` | `String` |  |
| `PaymentID` | `Int32` |  |
| `Message` | `String` |  |
| `DisplayMessage` | `String` |  |
| `MerchantTransactionKey` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/payment/refund/cc HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "returnPaymentID": 1,
  "orderID": 1,
  "maxAmount": null,
  "orderKey": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "amount": null,
  "authorizationCode": "",
  "paymentID": 1,
  "message": "",
  "displayMessage": "",
  "merchantTransactionKey": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/RefundPriorCreditCardCharge"

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
    <RefundPriorCreditCardChargeRequest xmlns="http://api.exigo.com/">
      <ReturnPaymentID>int</ReturnPaymentID>
      <OrderID>int</OrderID>
      <RefundOriginalOrder>boolean</RefundOriginalOrder>
      <MaxAmount>decimal</MaxAmount>
      <OrderKey>string</OrderKey>
    </RefundPriorCreditCardChargeRequest>
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
    <RefundPriorCreditCardChargeResult xmlns="http://api.exigo.com/">
      <Amount>decimal</Amount>
      <AuthorizationCode>string</AuthorizationCode>
    </RefundPriorCreditCardChargeResult>
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
    var req = new RefundPriorCreditCardChargeRequest();

    req.ReturnPaymentID = 1;
    req.OrderID = 1;                //Unique numeric identifier for order record.
    req.MaxAmount = 1;
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    var res = await api.RefundPriorCreditCardChargeAsync(req);

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
    RefundPriorCreditCardChargeRequest req = new RefundPriorCreditCardChargeRequest();

    req.ReturnPaymentID = 1;
    req.OrderID = 1;                //Unique numeric identifier for order record.
    req.MaxAmount = 1;
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    RefundPriorCreditCardChargeResponse res = api.RefundPriorCreditCardCharge(req);

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
    Dim req as new RefundPriorCreditCardChargeRequest()

    req.ReturnPaymentID = 1
    req.OrderID = 1
    req.MaxAmount = 1
    req.OrderKey = "1"

    'Send Request to Server and Get Response
    Dim res As RefundPriorCreditCardChargeResponse = api.RefundPriorCreditCardCharge(req)

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

    $req->ReturnPaymentID = 1;
    $req->OrderID = 1;
    $req->MaxAmount = 1;
    $req->OrderKey = "1";

    //Send Request to Server and Get Response
    $res = $api.RefundPriorCreditCardCharge($req);

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
    RefundPriorCreditCardChargeRequest req = new RefundPriorCreditCardChargeRequest();

    req.setReturnPaymentID(1);
    req.setOrderID(1);
    req.setMaxAmount(1);
    req.setOrderKey("1");

    //Send Request to Server and Get Response
    RefundPriorCreditCardChargeResponse res = api.getExigoApiSoap().refundPriorCreditCardCharge(req, auth);

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

### ChargeWalletAccount

>  Attempts to debit a wallet account with the amount found on an exiting order, or a new order in a transaction.
>  If the debit request is successful, the order is changed to accepted.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `POST /3.0/payment/charge/wallet` |
| SOAP action | `https://api.exigo.com/ChargeWalletAccount` |
| WSDL elements | `ChargeWalletAccountRequest` → `ChargeWalletAccountResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=ChargeWalletAccount |

#### Input

**`ChargeWalletAccountRequest`**

| Property | Type | Notes |
|---|---|---|
| `WalletAccountNumber` | `String` | Optional. |
| `WalletTy` | `Int32` |  |
| `OrderID` | `Int32` | Unique numeric identifier for order record. |
| `Memo` | `String` | Optional. |
| `MaxAmount` | `Decimal` | Optional. Only use if you are applying multiple payments. |
| `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided. |
| `OtherData1` | `String` | Optional. |
| `OtherData2` | `String` | Optional. |
| `OtherData3` | `String` | Optional. |
| `OtherData4` | `String` | Optional. |
| `OtherData5` | `String` | Optional. |
| `OtherData6` | `String` | Optional. |
| `OtherData7` | `String` | Optional. |
| `OtherData8` | `String` | Optional. |
| `OtherData9` | `String` | Optional. |
| `OtherData10` | `String` | Optional. |

#### Output

**`ChargeWalletAccountResponse`**

| Property | Type | Notes |
|---|---|---|
| `Amount` | `Decimal` |  |
| `AuthorizationCode` | `String` |  |
| `PaymentID` | `Int32` |  |
| `Message` | `String` |  |
| `DisplayMessage` | `String` |  |
| `MerchantTransactionKey` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/payment/charge/wallet HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "walletAccountNumber": "",
  "walletTy": 1,
  "memo": "",
  "orderKey": "1",
  "otherData1": "1",
  "otherData2": "1",
  "otherData3": "1",
  "otherData4": "1",
  "otherData5": "1",
  "otherData6": "1",
  "otherData7": "1",
  "otherData8": "1",
  "otherData9": "1",
  "otherData10": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "amount": null,
  "authorizationCode": "",
  "paymentID": 1,
  "message": "",
  "displayMessage": "",
  "merchantTransactionKey": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/ChargeWalletAccount"

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
    <ChargeWalletAccountRequest xmlns="http://api.exigo.com/">
      <WalletAccountNumber>string</WalletAccountNumber>
      <WalletTy>int</WalletTy>
      <OrderID>int</OrderID>
      <Memo>string</Memo>
      <MaxAmount>decimal</MaxAmount>
      <OrderKey>string</OrderKey>
    </ChargeWalletAccountRequest>
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
    <ChargeWalletAccountResult xmlns="http://api.exigo.com/">
      <Amount>decimal</Amount>
      <AuthorizationCode>string</AuthorizationCode>
    </ChargeWalletAccountResult>
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
    var req = new ChargeWalletAccountRequest();

    req.WalletAccountNumber = "1";
    req.WalletTy = 1;
    req.Memo = "1";
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.
    req.OtherData1 = "1";
    req.OtherData2 = "1";
    req.OtherData3 = "1";
    req.OtherData4 = "1";
    req.OtherData5 = "1";
    req.OtherData6 = "1";
    req.OtherData7 = "1";
    req.OtherData8 = "1";
    req.OtherData9 = "1";
    req.OtherData10 = "1";

    //Send Request to Server and Get Response
    var res = await api.ChargeWalletAccountAsync(req);

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
    ChargeWalletAccountRequest req = new ChargeWalletAccountRequest();

    req.WalletAccountNumber = "1";
    req.WalletTy = 1;
    req.Memo = "1";
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.
    req.OtherData1 = "1";
    req.OtherData2 = "1";
    req.OtherData3 = "1";
    req.OtherData4 = "1";
    req.OtherData5 = "1";
    req.OtherData6 = "1";
    req.OtherData7 = "1";
    req.OtherData8 = "1";
    req.OtherData9 = "1";
    req.OtherData10 = "1";

    //Send Request to Server and Get Response
    ChargeWalletAccountResponse res = api.ChargeWalletAccount(req);

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
    Dim req as new ChargeWalletAccountRequest()

    req.WalletAccountNumber = "1"
    req.WalletTy = 1
    req.Memo = "1"
    req.OrderKey = "1"
    req.OtherData1 = "1"
    req.OtherData2 = "1"
    req.OtherData3 = "1"
    req.OtherData4 = "1"
    req.OtherData5 = "1"
    req.OtherData6 = "1"
    req.OtherData7 = "1"
    req.OtherData8 = "1"
    req.OtherData9 = "1"
    req.OtherData10 = "1"

    'Send Request to Server and Get Response
    Dim res As ChargeWalletAccountResponse = api.ChargeWalletAccount(req)

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

    $req->WalletAccountNumber = "1";
    $req->WalletTy = 1;
    $req->Memo = "1";
    $req->OrderKey = "1";
    $req->OtherData1 = "1";
    $req->OtherData2 = "1";
    $req->OtherData3 = "1";
    $req->OtherData4 = "1";
    $req->OtherData5 = "1";
    $req->OtherData6 = "1";
    $req->OtherData7 = "1";
    $req->OtherData8 = "1";
    $req->OtherData9 = "1";
    $req->OtherData10 = "1";

    //Send Request to Server and Get Response
    $res = $api.ChargeWalletAccount($req);

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
    ChargeWalletAccountRequest req = new ChargeWalletAccountRequest();

    req.setWalletAccountNumber("1");
    req.setWalletTy(1);
    req.setMemo("1");
    req.setOrderKey("1");
    req.setOtherData1("1");
    req.setOtherData2("1");
    req.setOtherData3("1");
    req.setOtherData4("1");
    req.setOtherData5("1");
    req.setOtherData6("1");
    req.setOtherData7("1");
    req.setOtherData8("1");
    req.setOtherData9("1");
    req.setOtherData10("1");

    //Send Request to Server and Get Response
    ChargeWalletAccountResponse res = api.getExigoApiSoap().chargeWalletAccount(req, auth);

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

### ChargeWalletAccountOnFile

>  Attempts to debit a wallet account with the amount found on an exiting order, or a new order in a transaction.
>  If the debit request is successful, the order is changed to accepted.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `POST /3.0/payment/charge/walletonfile` |
| SOAP action | `https://api.exigo.com/ChargeWalletAccountOnFile` |
| WSDL elements | `ChargeWalletAccountOnFileRequest` → `ChargeWalletAccountOnFileResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=ChargeWalletAccountOnFile |

#### Input

**`ChargeWalletAccountOnFileRequest`**

| Property | Type | Notes |
|---|---|---|
| `WalletAccountType` | `AccountWalletType` | **Values:** `Primary`, `Secondary`, `Third`, `Fourth`, `Fifth` |
| `OrderID` | `Int32` | Unique numeric identifier for order record. |
| `Memo` | `String` | Optional. |
| `MaxAmount` | `Decimal` | Optional. Only use if you are applying multiple payments. |
| `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided. |
| `OtherData1` | `String` | Optional. |
| `OtherData2` | `String` | Optional. |
| `OtherData3` | `String` | Optional. |
| `OtherData4` | `String` | Optional. |
| `OtherData5` | `String` | Optional. |
| `OtherData6` | `String` | Optional. |
| `OtherData7` | `String` | Optional. |
| `OtherData8` | `String` | Optional. |
| `OtherData9` | `String` | Optional. |
| `OtherData10` | `String` | Optional. |

#### Output

**`ChargeWalletAccountResponse`**

| Property | Type | Notes |
|---|---|---|
| `Amount` | `Decimal` |  |
| `AuthorizationCode` | `String` |  |
| `PaymentID` | `Int32` |  |
| `Message` | `String` |  |
| `DisplayMessage` | `String` |  |
| `MerchantTransactionKey` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/payment/charge/walletonfile HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "walletAccountType": null,
  "memo": "",
  "orderKey": "1",
  "otherData1": "1",
  "otherData2": "1",
  "otherData3": "1",
  "otherData4": "1",
  "otherData5": "1",
  "otherData6": "1",
  "otherData7": "1",
  "otherData8": "1",
  "otherData9": "1",
  "otherData10": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "amount": null,
  "authorizationCode": "",
  "paymentID": 1,
  "message": "",
  "displayMessage": "",
  "merchantTransactionKey": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/ChargeWalletAccountOnFile"

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
    <ChargeWalletAccountOnFileRequest xmlns="http://api.exigo.com/">
      <WalletAccountType>Primary or Secondary or Third or Fourth or Fifth</WalletAccountType>
      <OrderID>int</OrderID>
      <Memo>string</Memo>
      <MaxAmount>decimal</MaxAmount>
      <OrderKey>string</OrderKey>
      <OtherData1>string</OtherData1>
      <OtherData2>string</OtherData2>
      <OtherData3>string</OtherData3>
      <OtherData4>string</OtherData4>
      <OtherData5>string</OtherData5>
      <OtherData6>string</OtherData6>
      <OtherData7>string</OtherData7>
      <OtherData8>string</OtherData8>
      <OtherData9>string</OtherData9>
      <OtherData10>string</OtherData10>
    </ChargeWalletAccountOnFileRequest>
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
    <ChargeWalletAccountOnFileResult xmlns="http://api.exigo.com/">
      <Amount>decimal</Amount>
      <AuthorizationCode>string</AuthorizationCode>
    </ChargeWalletAccountOnFileResult>
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
    var req = new ChargeWalletAccountOnFileRequest();

    req.WalletAccountType = AccountWalletType.Primary;
    req.Memo = "1";
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.
    req.OtherData1 = "1";
    req.OtherData2 = "1";
    req.OtherData3 = "1";
    req.OtherData4 = "1";
    req.OtherData5 = "1";
    req.OtherData6 = "1";
    req.OtherData7 = "1";
    req.OtherData8 = "1";
    req.OtherData9 = "1";
    req.OtherData10 = "1";

    //Send Request to Server and Get Response
    var res = await api.ChargeWalletAccountOnFileAsync(req);

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
    ChargeWalletAccountOnFileRequest req = new ChargeWalletAccountOnFileRequest();

    req.WalletAccountType = AccountWalletType.Primary;
    req.Memo = "1";
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.
    req.OtherData1 = "1";
    req.OtherData2 = "1";
    req.OtherData3 = "1";
    req.OtherData4 = "1";
    req.OtherData5 = "1";
    req.OtherData6 = "1";
    req.OtherData7 = "1";
    req.OtherData8 = "1";
    req.OtherData9 = "1";
    req.OtherData10 = "1";

    //Send Request to Server and Get Response
    ChargeWalletAccountResponse res = api.ChargeWalletAccountOnFile(req);

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
    Dim req as new ChargeWalletAccountOnFileRequest()

    req.WalletAccountType = AccountWalletType.Primary
    req.Memo = "1"
    req.OrderKey = "1"
    req.OtherData1 = "1"
    req.OtherData2 = "1"
    req.OtherData3 = "1"
    req.OtherData4 = "1"
    req.OtherData5 = "1"
    req.OtherData6 = "1"
    req.OtherData7 = "1"
    req.OtherData8 = "1"
    req.OtherData9 = "1"
    req.OtherData10 = "1"

    'Send Request to Server and Get Response
    Dim res As ChargeWalletAccountResponse = api.ChargeWalletAccountOnFile(req)

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

    $req->WalletAccountType = 1;
    $req->Memo = "1";
    $req->OrderKey = "1";
    $req->OtherData1 = "1";
    $req->OtherData2 = "1";
    $req->OtherData3 = "1";
    $req->OtherData4 = "1";
    $req->OtherData5 = "1";
    $req->OtherData6 = "1";
    $req->OtherData7 = "1";
    $req->OtherData8 = "1";
    $req->OtherData9 = "1";
    $req->OtherData10 = "1";

    //Send Request to Server and Get Response
    $res = $api.ChargeWalletAccountOnFile($req);

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
    ChargeWalletAccountOnFileRequest req = new ChargeWalletAccountOnFileRequest();

    req.setWalletAccountType(1);
    req.setMemo("1");
    req.setOrderKey("1");
    req.setOtherData1("1");
    req.setOtherData2("1");
    req.setOtherData3("1");
    req.setOtherData4("1");
    req.setOtherData5("1");
    req.setOtherData6("1");
    req.setOtherData7("1");
    req.setOtherData8("1");
    req.setOtherData9("1");
    req.setOtherData10("1");

    //Send Request to Server and Get Response
    ChargeWalletAccountResponse res = api.getExigoApiSoap().chargeWalletAccountOnFile(req, auth);

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

### DebitBankAccount

>  Attempts to debit a bank account with the amount found on an exiting order, or a new order in a transaction.
>  If the debit request is successful, the order is changed to accepted.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `POST /3.0/payment/charge/bank` |
| SOAP action | `https://api.exigo.com/DebitBankAccount` |
| WSDL elements | `DebitBankAccountRequest` → `DebitBankAccountResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DebitBankAccount |

#### Input

**`DebitBankAccountRequest`**

| Property | Type | Notes |
|---|---|---|
| `BankAccountNumber` | `String` | Optional. |
| `BankRoutingNumber` | `String` | Optional. |
| `BankName` | `String` | Optional. |
| `BankAccountType` | `BankAccountType` | **Values:** `CheckingPersonal`, `CheckingBusiness`, `SavingsPersonal`, `SavingsBusiness` |
| `CheckNumber` | `String` | Optional. Check number will be auto generated if pay by check. |
| `NameOnAccount` | `String` | Optional. |
| `BillingAddress` | `String` | Optional. |
| `BillingAddress2` | `String` | Optional. |
| `BillingCity` | `String` | Optional. |
| `BillingState` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `BillingZip` | `String` | Optional. |
| `BillingCountry` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Iban` | `String` | Optional. |
| `SwiftCode` | `String` | Optional. |
| `OrderID` | `Int32` | Unique numeric identifier for order record. |
| `MaxAmount` | `Decimal` | Optional. Only use if you are applying multiple payments. |
| `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided. |

#### Output

**`DebitBankAccountResponse`**

| Property | Type | Notes |
|---|---|---|
| `Amount` | `Decimal` |  |
| `AuthorizationCode` | `String` |  |
| `PaymentID` | `Int32` |  |
| `Message` | `String` |  |
| `DisplayMessage` | `String` |  |
| `MerchantTransactionKey` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/payment/charge/bank HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "bankAccountNumber": "",
  "bankRoutingNumber": "",
  "bankName": "",
  "bankAccountType": null,
  "checkNumber": "1",
  "nameOnAccount": "",
  "billingAddress": "",
  "billingAddress2": "",
  "billingCity": "",
  "billingZip": "",
  "maxAmount": null,
  "orderKey": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "amount": null,
  "authorizationCode": "",
  "paymentID": 1,
  "message": "",
  "displayMessage": "",
  "merchantTransactionKey": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/DebitBankAccount"

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
    <DebitBankAccountRequest xmlns="http://api.exigo.com/">
      <BankAccountNumber>string</BankAccountNumber>
      <BankRoutingNumber>string</BankRoutingNumber>
      <BankName>string</BankName>
      <BankAccountType>CheckingPersonal or CheckingBusiness or SavingsPersonal or SavingsBusiness</BankAccountType>
      <CheckNumber>string</CheckNumber>
      <NameOnAccount>string</NameOnAccount>
      <BillingAddress>string</BillingAddress>
      <BillingAddress2>string</BillingAddress2>
      <BillingCity>string</BillingCity>
      <BillingState>string</BillingState>
      <BillingZip>string</BillingZip>
      <BillingCountry>string</BillingCountry>
      <Iban>string</Iban>
      <SwiftCode>string</SwiftCode>
      <OrderID>int</OrderID>
      <MaxAmount>decimal</MaxAmount>
      <OrderKey>string</OrderKey>
    </DebitBankAccountRequest>
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
    <DebitBankAccountResult xmlns="http://api.exigo.com/">
      <Amount>decimal</Amount>
      <AuthorizationCode>string</AuthorizationCode>
    </DebitBankAccountResult>
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
    var req = new DebitBankAccountRequest();

    req.BankAccountNumber = "1";
    req.BankRoutingNumber = "1";
    req.BankName = "1";
    req.BankAccountType = BankAccountType.CheckingPersonal;
    req.CheckNumber = "1";          //Check number will be auto generated if pay by check
    req.NameOnAccount = "1";
    req.BillingAddress = "1";
    req.BillingAddress2 = "1";
    req.BillingCity = "1";
    req.BillingZip = "1";
    req.MaxAmount = 1;              //Only use if you are applying multiple payments.
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    var res = await api.DebitBankAccountAsync(req);

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
    DebitBankAccountRequest req = new DebitBankAccountRequest();

    req.BankAccountNumber = "1";
    req.BankRoutingNumber = "1";
    req.BankName = "1";
    req.BankAccountType = BankAccountType.CheckingPersonal;
    req.CheckNumber = "1";          //Check number will be auto generated if pay by check
    req.NameOnAccount = "1";
    req.BillingAddress = "1";
    req.BillingAddress2 = "1";
    req.BillingCity = "1";
    req.BillingZip = "1";
    req.MaxAmount = 1;              //Only use if you are applying multiple payments.
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    DebitBankAccountResponse res = api.DebitBankAccount(req);

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
    Dim req as new DebitBankAccountRequest()

    req.BankAccountNumber = "1"
    req.BankRoutingNumber = "1"
    req.BankName = "1"
    req.BankAccountType = BankAccountType.CheckingPersonal
    req.CheckNumber = "1"
    req.NameOnAccount = "1"
    req.BillingAddress = "1"
    req.BillingAddress2 = "1"
    req.BillingCity = "1"
    req.BillingZip = "1"
    req.MaxAmount = 1
    req.OrderKey = "1"

    'Send Request to Server and Get Response
    Dim res As DebitBankAccountResponse = api.DebitBankAccount(req)

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

    $req->BankAccountNumber = "1";
    $req->BankRoutingNumber = "1";
    $req->BankName = "1";
    $req->BankAccountType = 1;
    $req->CheckNumber = "1";
    $req->NameOnAccount = "1";
    $req->BillingAddress = "1";
    $req->BillingAddress2 = "1";
    $req->BillingCity = "1";
    $req->BillingZip = "1";
    $req->MaxAmount = 1;
    $req->OrderKey = "1";

    //Send Request to Server and Get Response
    $res = $api.DebitBankAccount($req);

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
    DebitBankAccountRequest req = new DebitBankAccountRequest();

    req.setBankAccountNumber("1");
    req.setBankRoutingNumber("1");
    req.setBankName("1");
    req.setBankAccountType(1);
    req.setCheckNumber("1");
    req.setNameOnAccount("1");
    req.setBillingAddress("1");
    req.setBillingAddress2("1");
    req.setBillingCity("1");
    req.setBillingZip("1");
    req.setMaxAmount(1);
    req.setOrderKey("1");

    //Send Request to Server and Get Response
    DebitBankAccountResponse res = api.getExigoApiSoap().debitBankAccount(req, auth);

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

### DebitBankAccountOnFile

>  Attempts to debit a bank account on file with the amount found on an exiting order, or a new order in a transaction.
>  If the debit request is successful, the order is changed to accepted.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `POST /3.0/payment/charge/bankonfile` |
| SOAP action | `https://api.exigo.com/DebitBankAccountOnFile` |
| WSDL elements | `DebitBankAccountOnFileRequest` → `DebitBankAccountOnFileResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DebitBankAccountOnFile |

#### Input

**`DebitBankAccountOnFileRequest`**

| Property | Type | Notes |
|---|---|---|
| `OrderID` | `Int32` | Unique numeric identifier for order record. |
| `MaxAmount` | `Decimal` | Optional. Only use if you are applying multiple payments. |
| `OrderKey` | `String` | Optional. Only use if you are applying multiple payments. |

#### Output

**`DebitBankAccountResponse`**

| Property | Type | Notes |
|---|---|---|
| `Amount` | `Decimal` |  |
| `AuthorizationCode` | `String` |  |
| `PaymentID` | `Int32` |  |
| `Message` | `String` |  |
| `DisplayMessage` | `String` |  |
| `MerchantTransactionKey` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/payment/charge/bankonfile HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "orderID": 1
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "amount": null,
  "authorizationCode": "",
  "paymentID": 1,
  "message": "",
  "displayMessage": "",
  "merchantTransactionKey": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/DebitBankAccountOnFile"

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
    <DebitBankAccountOnFileRequest xmlns="http://api.exigo.com/">
      <OrderID>int</OrderID>
      <MaxAmount>decimal</MaxAmount>
      <OrderKey>string</OrderKey>
    </DebitBankAccountOnFileRequest>
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
    <DebitBankAccountOnFileResult xmlns="http://api.exigo.com/">
      <Amount>decimal</Amount>
      <AuthorizationCode>string</AuthorizationCode>
    </DebitBankAccountOnFileResult>
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
    var req = new DebitBankAccountOnFileRequest();

    req.OrderID = 1;                //Unique numeric identifier for order record.

    //Send Request to Server and Get Response
    var res = await api.DebitBankAccountOnFileAsync(req);

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
    DebitBankAccountOnFileRequest req = new DebitBankAccountOnFileRequest();

    req.OrderID = 1;                //Unique numeric identifier for order record.

    //Send Request to Server and Get Response
    DebitBankAccountResponse res = api.DebitBankAccountOnFile(req);

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
    Dim req as new DebitBankAccountOnFileRequest()

    req.OrderID = 1

    'Send Request to Server and Get Response
    Dim res As DebitBankAccountResponse = api.DebitBankAccountOnFile(req)

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

    $req->OrderID = 1;

    //Send Request to Server and Get Response
    $res = $api.DebitBankAccountOnFile($req);

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
    DebitBankAccountOnFileRequest req = new DebitBankAccountOnFileRequest();

    req.setOrderID(1);

    //Send Request to Server and Get Response
    DebitBankAccountResponse res = api.getExigoApiSoap().debitBankAccountOnFile(req, auth);

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

### CreateExpectedPayment

> Creates a new expected payment type using cash, money order etc.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `POST /3.0/payment/expectedpayment` |
| SOAP action | `https://api.exigo.com/CreateExpectedPayment` |
| WSDL elements | `CreateExpectedPaymentRequest` → `CreateExpectedPaymentResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateExpectedPayment |

#### Input

**`CreateExpectedPaymentRequest`**

| Property | Type | Notes |
|---|---|---|
| `OrderID` | `Int32` | Unique numeric identifier for order record. |
| `PaymentDate` | `DateTime` |  |
| `Amount` | `Decimal` |  |
| `PaymentType` | `PaymentType` | Optional. Obsolete field. Please consider upgrading to PaymentTy. Defaults to Cash.<br>**Values:** `Cash`, `CreditCard`, `Check`, `CreditVoucher`, `Net30`, `Net60`, `UseCredit`, `ACHDebit`, `BankDraft`, `BankWire`, `PointRedemtion`, `COD`, `MoneyOrder`, `BankDeposit`, `Other1`, `Other2`, `Other3`, `Wallet`, `Other4`, `Other5`, `Other6`, `Other7`, `Other8`, `Other9`, `Other10`, `Other11`, `Other12`, `Other13`, `Other14`, `Other15` |
| `AuthorizationCode` | `String` | Optional. |
| `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided. |
| `PaymentTy` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |

#### Output

**`CreateExpectedPaymentResponse`**

| Property | Type | Notes |
|---|---|---|
| `ExpectedPaymentID` | `Int32` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/payment/expectedpayment HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "paymentDate": "2026-11-10T00:00:00-06:00",
  "amount": null,
  "orderKey": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "expectedPaymentID": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateExpectedPayment"

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
    <CreateExpectedPaymentRequest xmlns="http://api.exigo.com/">
      <OrderID>int</OrderID>
      <PaymentDate>dateTime</PaymentDate>
      <Amount>decimal</Amount>
      <PaymentType>Cash or CreditCard or Check or CreditVoucher or Net30 or Net60 or ACHDebit or UseCredit or BankDraft or BankWire or PointRedemtion or COD or MoneyOrder or BankDeposit or Other1 or Other2 or Other3 or Wallet or Other4 or Other5 or Other6 or Other7 or Other8 or Other9 or Other10 or Other11 or Other12 or Other13 or Other14 or Other15</PaymentType>
      <AuthorizationCode>string</AuthorizationCode>
      <OrderKey>string</OrderKey>
      <PaymentTy>string</PaymentTy>
    </CreateExpectedPaymentRequest>
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
    <CreateExpectedPaymentResult xmlns="http://api.exigo.com/">
      <ExpectedPaymentID>int</ExpectedPaymentID>
    </CreateExpectedPaymentResult>
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
    var req = new CreateExpectedPaymentRequest();

    req.PaymentDate = DateTime.Today;
    req.Amount = 1;
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    var res = await api.CreateExpectedPaymentAsync(req);

    //Now examine the results:
    Console.WriteLine("ExpectedPaymentID: {0}", res.ExpectedPaymentID);
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
    CreateExpectedPaymentRequest req = new CreateExpectedPaymentRequest();

    req.PaymentDate = DateTime.Today;
    req.Amount = 1;
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    CreateExpectedPaymentResponse res = api.CreateExpectedPayment(req);

    //Now examine the results:
    Console.WriteLine("ExpectedPaymentID: {0}", res.ExpectedPaymentID);
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
    Dim req as new CreateExpectedPaymentRequest()

    req.PaymentDate = DateTime.Today
    req.Amount = 1
    req.OrderKey = "1"

    'Send Request to Server and Get Response
    Dim res As CreateExpectedPaymentResponse = api.CreateExpectedPayment(req)

    'Now examine the results:
    Console.WriteLine("ExpectedPaymentID: {0}", res.ExpectedPaymentID)
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

    $req->PaymentDate = 1;
    $req->Amount = 1;
    $req->OrderKey = "1";

    //Send Request to Server and Get Response
    $res = $api.CreateExpectedPayment($req);

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
    CreateExpectedPaymentRequest req = new CreateExpectedPaymentRequest();

    req.setPaymentDate(1);
    req.setAmount(1);
    req.setOrderKey("1");

    //Send Request to Server and Get Response
    CreateExpectedPaymentResponse res = api.getExigoApiSoap().createExpectedPayment(req, auth);

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

### CreateExpectedBankWire

> Creates a new expected payment of type Bank Bire.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `POST /3.0/payment/wire` |
| SOAP action | `https://api.exigo.com/CreateExpectedBankWire` |
| WSDL elements | `CreateExpectedBankWireRequest` → `CreateExpectedBankWireResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateExpectedBankWire |

#### Input

**`CreateExpectedBankWireRequest`**

| Property | Type | Notes |
|---|---|---|
| `OrderID` | `Int32` | Unique numeric identifier for order record. |
| `PaymentDate` | `DateTime` |  |
| `Amount` | `Decimal` |  |
| `BankName` | `String` | Optional. |
| `NameOnAccount` | `String` | Optional. |
| `Memo` | `String` | Optional. |
| `AuthorizationCode` | `String` | Optional. |
| `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided. |

#### Output

**`CreateExpectedBankWireResponse`**

| Property | Type | Notes |
|---|---|---|
| `ExpectedPaymentID` | `Int32` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/payment/wire HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "paymentDate": "2026-11-10T00:00:00-06:00",
  "amount": null,
  "bankName": "",
  "nameOnAccount": "",
  "memo": "",
  "orderKey": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "expectedPaymentID": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateExpectedBankWire"

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
    <CreateExpectedBankWireRequest xmlns="http://api.exigo.com/">
      <OrderID>int</OrderID>
      <PaymentDate>dateTime</PaymentDate>
      <Amount>decimal</Amount>
      <BankName>string</BankName>
      <NameOnAccount>string</NameOnAccount>
      <Memo>string</Memo>
      <AuthorizationCode>string</AuthorizationCode>
      <OrderKey>string</OrderKey>
    </CreateExpectedBankWireRequest>
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
    <CreateExpectedBankWireResult xmlns="http://api.exigo.com/">
      <ExpectedPaymentID>int</ExpectedPaymentID>
    </CreateExpectedBankWireResult>
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
    var req = new CreateExpectedBankWireRequest();

    req.PaymentDate = DateTime.Today;
    req.Amount = 1;
    req.BankName = "1";
    req.NameOnAccount = "1";
    req.Memo = "1";
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    var res = await api.CreateExpectedBankWireAsync(req);

    //Now examine the results:
    Console.WriteLine("ExpectedPaymentID: {0}", res.ExpectedPaymentID);
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
    CreateExpectedBankWireRequest req = new CreateExpectedBankWireRequest();

    req.PaymentDate = DateTime.Today;
    req.Amount = 1;
    req.BankName = "1";
    req.NameOnAccount = "1";
    req.Memo = "1";
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    CreateExpectedBankWireResponse res = api.CreateExpectedBankWire(req);

    //Now examine the results:
    Console.WriteLine("ExpectedPaymentID: {0}", res.ExpectedPaymentID);
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
    Dim req as new CreateExpectedBankWireRequest()

    req.PaymentDate = DateTime.Today
    req.Amount = 1
    req.BankName = "1"
    req.NameOnAccount = "1"
    req.Memo = "1"
    req.OrderKey = "1"

    'Send Request to Server and Get Response
    Dim res As CreateExpectedBankWireResponse = api.CreateExpectedBankWire(req)

    'Now examine the results:
    Console.WriteLine("ExpectedPaymentID: {0}", res.ExpectedPaymentID)
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

    $req->PaymentDate = 1;
    $req->Amount = 1;
    $req->BankName = "1";
    $req->NameOnAccount = "1";
    $req->Memo = "1";
    $req->OrderKey = "1";

    //Send Request to Server and Get Response
    $res = $api.CreateExpectedBankWire($req);

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
    CreateExpectedBankWireRequest req = new CreateExpectedBankWireRequest();

    req.setPaymentDate(1);
    req.setAmount(1);
    req.setBankName("1");
    req.setNameOnAccount("1");
    req.setMemo("1");
    req.setOrderKey("1");

    //Send Request to Server and Get Response
    CreateExpectedBankWireResponse res = api.getExigoApiSoap().createExpectedBankWire(req, auth);

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

### GetOrders

> Returns one or more orders. You can submit several optional filter
>  fields to control the results.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `GET /3.0/orders?customerID=1` |
| SOAP action | `https://api.exigo.com/GetOrders` |
| WSDL elements | `GetOrdersRequest` → `GetOrdersResult` |
| CSV output | Yes — `GET https://api.exigo.com/3.0/csv/?method=GetOrders&ApiLoginName=…&ApiPassword=…&ApiCompany=…` |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetOrders |

#### Input

**`GetOrdersRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Optional. Unique numeric identifier for customer record. |
| `OrderID` | `Int32` | Optional. Unique numeric identifier for order record. |
| `OrderIDs` | `Int32[]` | Optionally supply a list to return off of. |
| `OrderDateStart` | `DateTime` | Optional. If supplied only orders with a date greater than or equal to will be returned.Format YYYY-MM-DDTHH:mm:ss. |
| `OrderDateEnd` | `DateTime` | Optional. If supplied only orders with a date less than or equal to will be returned. Format YYYY-MM-DDTHH:mm:ss. |
| `OrderStatus` | `OrderStatusType` | Optional.<br>**Values:** `Incomplete`, `Pending`, `CCDeclined`, `ACHDeclined`, `Canceled`, `CCPending`, `ACHPending`, `Accepted`, `Printed`, `Shipped`, `PendingInventory` |
| `OtherOrderStatuses` | `OrderStatusType[]` | Optional. Fill to filter by multiple order statuses. If OrderStatus is also supplied, it will be included. Defaults to OrderStatusType[].<br>**Values:** `Incomplete`, `Pending`, `CCDeclined`, `ACHDeclined`, `Canceled`, `CCPending`, `ACHPending`, `Accepted`, `Printed`, `Shipped`, `PendingInventory` |
| `OrderTypes` | `OrderType[]` | Optional. Obsolete field. Please consider upgrading to OrderTys. Defaults to OrderType[].<br>**Values:** `Default`, `CustomerService`, `ShoppingCart`, `WebWizard`, `AutoOrder`, `Import`, `BackOrder`, `ReplacementOrder`, `ReturnOrder`, `WebAutoOrder`, `TicketSystem`, `APIOrder`, `BackOrderParent`, `ChildOrder`, `Other1`, `Other2`, `Other3`, `Other4`, `Other5`, `Other6`, `Other7`, `Other8`, `Other9`, `Other10` |
| `WarehouseID` | `Int32` | Optional. Unique location for orders.<br>**Lookup:** company-specific list (see company-lists.md) |
| `CurrencyCode` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `ReturnCustomer` | `Boolean` | Optional. Optionally return full customer info with every order. |
| `ReturnKitDetails` | `Boolean` | Optional. Optionally return bill of material for kits. |
| `GreaterThanOrderID` | `Int32` | Optional. |
| `GreaterThanModifiedDate` | `DateTime` | Optional. |
| `BatchSize` | `Int32` | Optional. Defaults to 100 orders at a time. |
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
| `PartyID` | `Int32` | Optional. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |
| `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided. |
| `OrderKeys` | `String[]` | Optionally supply a list to return off of. |
| `OrderSubStatusTy` | `Int32` | Optional. |
| `BatchID` | `Int32` | Optional. |
| `OrderTys` | `String[]` | Optional. Fill to filter by OrderType(s). Defaults to System.String[].<br>**Lookup:** company-specific list (see company-lists.md) |
| `ReferralID` | `Int32` | Optional. |

**`OrderStatusType`**

_No properties._

**`OrderType`**

_No properties._

#### Output

**`GetOrdersResponse`**

| Property | Type | Notes |
|---|---|---|
| `Orders` | `OrderResponse[]` |  |
| `RecordCount` | `Int32` |  |

**`OrderResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `OrderID` | `Int32` | Unique numeric identifier for order record. |
| &nbsp;&nbsp;↳ `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| &nbsp;&nbsp;↳ `OrderStatus` | `OrderStatusType` | **Values:** `Incomplete`, `Pending`, `CCDeclined`, `ACHDeclined`, `Canceled`, `CCPending`, `ACHPending`, `Accepted`, `Printed`, `Shipped`, `PendingInventory` |
| &nbsp;&nbsp;↳ `OrderDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `CurrencyCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `WarehouseID` | `Int32` | Unique location for orders.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `ShipMethodID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `PriceType` | `Int32` | Controls which price band to use.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `FirstName` | `String` |  |
| &nbsp;&nbsp;↳ `LastName` | `String` |  |
| &nbsp;&nbsp;↳ `Company` | `String` |  |
| &nbsp;&nbsp;↳ `Address1` | `String` |  |
| &nbsp;&nbsp;↳ `Address2` | `String` |  |
| &nbsp;&nbsp;↳ `Address3` | `String` |  |
| &nbsp;&nbsp;↳ `City` | `String` |  |
| &nbsp;&nbsp;↳ `State` | `String` |  |
| &nbsp;&nbsp;↳ `Zip` | `String` |  |
| &nbsp;&nbsp;↳ `Country` | `String` |  |
| &nbsp;&nbsp;↳ `County` | `String` |  |
| &nbsp;&nbsp;↳ `Email` | `String` |  |
| &nbsp;&nbsp;↳ `Phone` | `String` |  |
| &nbsp;&nbsp;↳ `Notes` | `String` |  |
| &nbsp;&nbsp;↳ `Total` | `Decimal` |  |
| &nbsp;&nbsp;↳ `SubTotal` | `Decimal` |  |
| &nbsp;&nbsp;↳ `TaxTotal` | `Decimal` |  |
| &nbsp;&nbsp;↳ `ShippingTotal` | `Decimal` |  |
| &nbsp;&nbsp;↳ `DiscountTotal` | `Decimal` |  |
| &nbsp;&nbsp;↳ `DiscountPercent` | `Decimal` |  |
| &nbsp;&nbsp;↳ `WeightTotal` | `Decimal` |  |
| &nbsp;&nbsp;↳ `BusinessVolumeTotal` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CommissionableVolumeTotal` | `Decimal` |  |
| &nbsp;&nbsp;↳ `TrackingNumber1` | `String` |  |
| &nbsp;&nbsp;↳ `TrackingNumber2` | `String` |  |
| &nbsp;&nbsp;↳ `TrackingNumber3` | `String` |  |
| &nbsp;&nbsp;↳ `TrackingNumber4` | `String` |  |
| &nbsp;&nbsp;↳ `TrackingNumber5` | `String` |  |
| &nbsp;&nbsp;↳ `Other1Total` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other2Total` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other3Total` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other4Total` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other5Total` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other6Total` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other7Total` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other8Total` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other9Total` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other10Total` | `Decimal` |  |
| &nbsp;&nbsp;↳ `ShippingTax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `OrderTax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `FedTaxTotal` | `Decimal` |  |
| &nbsp;&nbsp;↳ `StateTaxTotal` | `Decimal` |  |
| &nbsp;&nbsp;↳ `FedShippingTax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `StateShippingTax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CityShippingTax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CityLocalShippingTax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CountyShippingTax` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CountyLocalShippingTax` | `Decimal` |  |
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
| &nbsp;&nbsp;↳ `ModifiedDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `OrderType` | `OrderType` | Obsolete field. Please consider upgrading to OrderTyID Or OrderTyDescription.<br>**Values:** `Default`, `CustomerService`, `ShoppingCart`, `WebWizard`, `AutoOrder`, `Import`, `BackOrder`, `ReplacementOrder`, `ReturnOrder`, `WebAutoOrder`, `TicketSystem`, `APIOrder`, `BackOrderParent`, `ChildOrder`, `Other1`, `Other2`, `Other3`, `Other4`, `Other5`, `Other6`, `Other7`, `Other8`, `Other9`, `Other10` |
| &nbsp;&nbsp;↳ `ShippedDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `CreatedDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `CreatedBy` | `String` |  |
| &nbsp;&nbsp;↳ `ModifiedBy` | `String` |  |
| &nbsp;&nbsp;↳ `TaxFedRate` | `Decimal` |  |
| &nbsp;&nbsp;↳ `TaxStateRate` | `Decimal` |  |
| &nbsp;&nbsp;↳ `TaxCityRate` | `Decimal` |  |
| &nbsp;&nbsp;↳ `TaxCityLocalRate` | `Decimal` |  |
| &nbsp;&nbsp;↳ `TaxCountyRate` | `Decimal` |  |
| &nbsp;&nbsp;↳ `TaxCountyLocalRate` | `Decimal` |  |
| &nbsp;&nbsp;↳ `TaxManualRate` | `Decimal` |  |
| &nbsp;&nbsp;↳ `TaxCity` | `String` |  |
| &nbsp;&nbsp;↳ `TaxCounty` | `String` |  |
| &nbsp;&nbsp;↳ `TaxState` | `String` |  |
| &nbsp;&nbsp;↳ `TaxZip` | `String` |  |
| &nbsp;&nbsp;↳ `TaxCountry` | `String` |  |
| &nbsp;&nbsp;↳ `TaxIsExempt` | `Boolean` |  |
| &nbsp;&nbsp;↳ `TaxIsOverRide` | `Boolean` |  |
| &nbsp;&nbsp;↳ `Details` | `OrderDetailResponse[]` |  |
| &nbsp;&nbsp;↳ `Payments` | `PaymentResponse[]` |  |
| &nbsp;&nbsp;↳ `ExpectedPayments` | `ExpectedPaymentResponse[]` |  |
| &nbsp;&nbsp;↳ `Customer` | `CustomerResponse` | Customer record. |
| &nbsp;&nbsp;↳ `MiddleName` | `String` |  |
| &nbsp;&nbsp;↳ `NameSuffix` | `String` |  |
| &nbsp;&nbsp;↳ `AutoOrderID` | `Int32` | AutoOrderID from which this order was generated, if applicable. |
| &nbsp;&nbsp;↳ `PartyID` | `Int32` | PartyID, if applicable. |
| &nbsp;&nbsp;↳ `Reference1` | `String` | Reference1. |
| &nbsp;&nbsp;↳ `IsRMA` | `Boolean` |  |
| &nbsp;&nbsp;↳ `BackOrderFromID` | `Int32` | Unique numeric identifier for transfer to order record. |
| &nbsp;&nbsp;↳ `TransferToID` | `Int32` | CustomerID of volume transfer, if applicable. |
| &nbsp;&nbsp;↳ `SuppressPackSlipPrice` | `Boolean` |  |
| &nbsp;&nbsp;↳ `ReturnOrderID` | `Int32` |  |
| &nbsp;&nbsp;↳ `OrderKey` | `String` | Unique alpha numeric identifier for order record. |
| &nbsp;&nbsp;↳ `CustomerKey` | `String` | Unique alpha numeric identifier for customer record. |
| &nbsp;&nbsp;↳ `ReplacementOrderID` | `Int32` |  |
| &nbsp;&nbsp;↳ `OrderSubStatusTy` | `Int32` |  |
| &nbsp;&nbsp;↳ `BatchID` | `Int32` |  |
| &nbsp;&nbsp;↳ `OrderTyID` | `Int32` |  |
| &nbsp;&nbsp;↳ `OrderTyDescription` | `String` |  |
| &nbsp;&nbsp;↳ `ReferralID` | `Int32` |  |

**`OrderDetailResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `OrderDetailID` | `Guid` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `ParentOrderDetailID` | `Guid` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `ItemCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Description` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Quantity` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `PriceEach` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `PriceTotal` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Tax` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `WeightEach` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Weight` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `BusinessVolumeEach` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `CommissionableVolumeEach` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `CommissionableVolume` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Other1Each` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Other1` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Other2Each` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Other2` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Other3Each` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Other3` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Other4Each` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Other4` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Other5Each` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Other5` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Other6Each` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Other6` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Other7Each` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Other7` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Other8Each` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Other8` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Other9Each` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Other9` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Other10Each` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Other10` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `ParentItemCode` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Taxable` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `FedTax` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `StateTax` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `CityTax` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `CityLocalTax` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `CountyTax` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `CountyLocalTax` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `ManualTax` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `IsStateTaxOverride` | `Boolean` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `OrderLine` | `Int32` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Reference1` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `ShippingPriceEach` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `HandlingFee` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `BusinessVolume` | `Decimal` |  |

**`PaymentResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `PaymentID` | `Int32` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `PaymentType` | `PaymentType` | Obsolete field. Please consider upgrading to PaymentTypeId.<br>**Values:** `Cash`, `CreditCard`, `Check`, `CreditVoucher`, `Net30`, `Net60`, `UseCredit`, `ACHDebit`, `BankDraft`, `BankWire`, `PointRedemtion`, `COD`, `MoneyOrder`, `BankDeposit`, `Other1`, `Other2`, `Other3`, `Wallet`, `Other4`, `Other5`, `Other6`, `Other7`, `Other8`, `Other9`, `Other10`, `Other11`, `Other12`, `Other13`, `Other14`, `Other15` |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `PaymentDate` | `DateTime` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Amount` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `OrderID` | `Int32` | Unique numeric identifier for order record. |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `CurrencyCode` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `BillingName` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `BillingAddress1` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `BillingAddress2` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `BillingCity` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `BillingState` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `BillingZip` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `BillingCountry` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `BankName` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Memo` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `CreditCardNumberDisplay` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `AuthorizationCode` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `CreditCardType` | `Int32` | Optionally pass in Visa, Master Card, etc.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `CreditCardTypeDescription` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `OrderKey` | `String` | Unique alpha numeric identifier for order record. |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `CustomerKey` | `String` | Unique alpha numeric identifier for customer record . |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `WalletTy` | `Int32` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `PaymentTypeId` | `Int32` |  |

**`ExpectedPaymentResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `ExpectedPaymentID` | `Int32` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `PaymentType` | `PaymentType` | Obsolete field. Please consider upgrading to PaymentTypeId.<br>**Values:** `Cash`, `CreditCard`, `Check`, `CreditVoucher`, `Net30`, `Net60`, `UseCredit`, `ACHDebit`, `BankDraft`, `BankWire`, `PointRedemtion`, `COD`, `MoneyOrder`, `BankDeposit`, `Other1`, `Other2`, `Other3`, `Wallet`, `Other4`, `Other5`, `Other6`, `Other7`, `Other8`, `Other9`, `Other10`, `Other11`, `Other12`, `Other13`, `Other14`, `Other15` |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `PaymentDate` | `DateTime` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Amount` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `OrderID` | `Int32` | Unique numeric identifier for order record. |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `CurrencyCode` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `BillingName` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `AuthorizationCode` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `OrderKey` | `String` | Unique alpha numeric identifier for order record. |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `CustomerKey` | `String` | Unique alpha numeric identifier for customer record . |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `PaymentTypeId` | `Int32` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/orders?customerID=1
  &orderID=1
  &orderDateStart=1
  &orderDateEnd=1
  &warehouseID=1
  &currencyCode=usd
  &customerKey=1
  &orderKey=1
  &orderSubStatusTy=1
  &batchID=1
  &referralID=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "orders": null,
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
SOAPAction: "https://api.exigo.com/GetOrders"

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
    <GetOrdersRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <OrderID>int</OrderID>
      <OrderIDs>
        <int>int</int>
      </OrderIDs>
      <OrderDateStart>dateTime</OrderDateStart>
      <OrderDateEnd>dateTime</OrderDateEnd>
      <OrderStatus>Incomplete or Pending or CCDeclined or ACHDeclined or Canceled or CCPending or ACHPending or Accepted or Printed or Shipped or PendingInventory</OrderStatus>
      <OtherOrderStatuses>
        <OrderStatusType>Incomplete or Pending or CCDeclined or ACHDeclined or Canceled or CCPending or ACHPending or Accepted or Printed or Shipped or PendingInventory</OrderStatusType>
      </OtherOrderStatuses>
      <OrderTypes>
        <OrderType>Default or CustomerService or ShoppingCart or WebWizard or AutoOrder or Import or BackOrder or ReplacementOrder or ReturnOrder or WebAutoOrder or TicketSystem or APIOrder or BackOrderParent or ChildOrder or Other1 or Other2 or Other3 or Other4 or Other5 or Other6 or Other7 or Other8 or Other9 or Other10</OrderType>
      </OrderTypes>
      <WarehouseID>int</WarehouseID>
      <CurrencyCode>string</CurrencyCode>
      <ReturnCustomer>boolean</ReturnCustomer>
      <ReturnKitDetails>boolean</ReturnKitDetails>
      <GreaterThanOrderID>int</GreaterThanOrderID>
      <GreaterThanModifiedDate>dateTime</GreaterThanModifiedDate>
      <BatchSize>int</BatchSize>
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
      <PartyID>int</PartyID>
      <CustomerKey>string</CustomerKey>
      <OrderKey>string</OrderKey>
      <OrderKeys>
        <string>string</string>
      </OrderKeys>
      <OrderSubStatusTy>int</OrderSubStatusTy>
      <BatchID>int</BatchID>
      <OrderTys>
        <string>string</string>
      </OrderTys>
      <ReferralID>int</ReferralID>
    </GetOrdersRequest>
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
    <GetOrdersResult xmlns="http://api.exigo.com/">
      <Orders>
        <OrderResponse>
          <OrderID>int</OrderID>
          <CustomerID>int</CustomerID>
          <OrderStatus>Incomplete or Pending or CCDeclined or ACHDeclined or Canceled or CCPending or ACHPending or Accepted or Printed or Shipped or PendingInventory</OrderStatus>
          <OrderDate>dateTime</OrderDate>
          <CurrencyCode>string</CurrencyCode>
          <WarehouseID>int</WarehouseID>
          <ShipMethodID>int</ShipMethodID>
          <PriceType>int</PriceType>
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
          <DiscountPercent>decimal</DiscountPercent>
          <WeightTotal>decimal</WeightTotal>
          <BusinessVolumeTotal>decimal</BusinessVolumeTotal>
          <CommissionableVolumeTotal>decimal</CommissionableVolumeTotal>
          <TrackingNumber1>string</TrackingNumber1>
          <TrackingNumber2>string</TrackingNumber2>
          <TrackingNumber3>string</TrackingNumber3>
          <TrackingNumber4>string</TrackingNumber4>
          <TrackingNumber5>string</TrackingNumber5>
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
          <FedTaxTotal>decimal</FedTaxTotal>
          <StateTaxTotal>decimal</StateTaxTotal>
          <FedShippingTax>decimal</FedShippingTax>
          <StateShippingTax>decimal</StateShippingTax>
          <CityShippingTax>decimal</CityShippingTax>
          <CityLocalShippingTax>decimal</CityLocalShippingTax>
          <CountyShippingTax>decimal</CountyShippingTax>
          <CountyLocalShippingTax>decimal</CountyLocalShippingTax>
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
          <ModifiedDate>dateTime</ModifiedDate>
          <OrderType>Default or CustomerService or ShoppingCart or WebWizard or AutoOrder or Import or BackOrder or ReplacementOrder or ReturnOrder or WebAutoOrder or TicketSystem or APIOrder or BackOrderParent or ChildOrder or Other1 or Other2 or Other3 or Other4 or Other5 or Other6 or Other7 or Other8 or Other9 or Other10</OrderType>
          <ShippedDate>dateTime</ShippedDate>
          <CreatedDate>dateTime</CreatedDate>
          <CreatedBy>string</CreatedBy>
          <ModifiedBy>string</ModifiedBy>
          <TaxFedRate>decimal</TaxFedRate>
          <TaxStateRate>decimal</TaxStateRate>
          <TaxCityRate>decimal</TaxCityRate>
          <TaxCityLocalRate>decimal</TaxCityLocalRate>
          <TaxCountyRate>decimal</TaxCountyRate>
          <TaxCountyLocalRate>decimal</TaxCountyLocalRate>
          <TaxManualRate>decimal</TaxManualRate>
          <TaxCity>string</TaxCity>
          <TaxCounty>string</TaxCounty>
          <TaxState>string</TaxState>
          <TaxZip>string</TaxZip>
          <TaxCountry>string</TaxCountry>
          <TaxIsExempt>boolean</TaxIsExempt>
          <TaxIsOverRide>boolean</TaxIsOverRide>
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
          <ExpectedPayments>
            <ExpectedPaymentResponse>
              <ExpectedPaymentID>int</ExpectedPaymentID>
              <CustomerID>int</CustomerID>
              <PaymentType>Cash or CreditCard or Check or CreditVoucher or Net30 or Net60 or ACHDebit or UseCredit or BankDraft or BankWire or PointRedemtion or COD or MoneyOrder or BankDeposit or Other1 or Other2 or Other3 or Wallet or Other4 or Other5 or Other6 or Other7 or Other8 or Other9 or Other10 or Other11 or Other12 or Other13 or Other14 or Other15</PaymentType>
              <PaymentDate>dateTime</PaymentDate>
              <Amount>decimal</Amount>
              <OrderID>int</OrderID>
              <CurrencyCode>string</CurrencyCode>
              <BillingName>string</BillingName>
              <AuthorizationCode>string</AuthorizationCode>
              <OrderKey>string</OrderKey>
              <CustomerKey>string</CustomerKey>
              <PaymentTypeId>int</PaymentTypeId>
            </ExpectedPaymentResponse>
          </ExpectedPayments>
          <Customer>
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
          </Customer>
          <MiddleName>string</MiddleName>
          <NameSuffix>string</NameSuffix>
          <AutoOrderID>int</AutoOrderID>
          <PartyID>int</PartyID>
          <Reference1>string</Reference1>
          <IsRMA>boolean</IsRMA>
          <BackOrderFromID>int</BackOrderFromID>
          <TransferToID>int</TransferToID>
          <SuppressPackSlipPrice>boolean</SuppressPackSlipPrice>
          <ReturnOrderID>int</ReturnOrderID>
          <OrderKey>string</OrderKey>
          <CustomerKey>string</CustomerKey>
          <ReplacementOrderID>int</ReplacementOrderID>
          <OrderSubStatusTy>int</OrderSubStatusTy>
          <BatchID>int</BatchID>
          <OrderTyID>int</OrderTyID>
          <OrderTyDescription>string</OrderTyDescription>
          <ReferralID>int</ReferralID>
        </OrderResponse>
      </Orders>
      <RecordCount>int</RecordCount>
    </GetOrdersResult>
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
    var req = new GetOrdersRequest();

    req.CustomerID = 1;             //Unique  numeric identifier for customer record.
    req.OrderID = 1;                //Unique  numeric identifier for order record.
    req.OrderDateStart = DateTime.Today;         //If supplied only orders with a date greater than or equal to will be returned.Format YYYY-MM-DDTHH:mm:ss
    req.OrderDateEnd = DateTime.Today;           //If supplied only orders with a date less than or equal to will be returned. Format YYYY-MM-DDTHH:mm:ss
    req.WarehouseID = 1;            //Unique location for orders
    req.CurrencyCode = "usd";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.
    req.OrderSubStatusTy = 1;
    req.BatchID = 1;
    req.ReferralID = 1;

    //Send Request to Server and Get Response
    var res = await api.GetOrdersAsync(req);

    //Now examine the results:

    foreach (var order  in res.Orders)
    {
        Console.WriteLine("OrderID: {0}", order.OrderID);
        Console.WriteLine("CustomerID: {0}", order.CustomerID);
        Console.WriteLine("OrderStatus: {0}", order.OrderStatus);
        Console.WriteLine("OrderDate: {0}", order.OrderDate);
        Console.WriteLine("CurrencyCode: {0}", order.CurrencyCode);
        Console.WriteLine("WarehouseID: {0}", order.WarehouseID);
        Console.WriteLine("ShipMethodID: {0}", order.ShipMethodID);
        Console.WriteLine("PriceType: {0}", order.PriceType);
        Console.WriteLine("Total: {0}", order.Total);

        foreach (var orderDetail  in order.Details)
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

        foreach (var payment  in order.Payments)
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
        Console.WriteLine("BackOrderFromID: {0}", order.BackOrderFromID);
        Console.WriteLine("OrderKey: {0}", order.OrderKey);
        Console.WriteLine("CustomerKey: {0}", order.CustomerKey);
        Console.WriteLine("OrderSubStatusTy: {0}", order.OrderSubStatusTy);
        Console.WriteLine("BatchID: {0}", order.BatchID);
        Console.WriteLine("OrderTyID: {0}", order.OrderTyID);
        Console.WriteLine("OrderTyDescription: {0}", order.OrderTyDescription);
        Console.WriteLine("ReferralID: {0}", order.ReferralID);
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
    GetOrdersRequest req = new GetOrdersRequest();

    req.CustomerID = 1;             //Unique  numeric identifier for customer record.
    req.OrderID = 1;                //Unique  numeric identifier for order record.
    req.OrderDateStart = DateTime.Today;         //If supplied only orders with a date greater than or equal to will be returned.Format YYYY-MM-DDTHH:mm:ss
    req.OrderDateEnd = DateTime.Today;           //If supplied only orders with a date less than or equal to will be returned. Format YYYY-MM-DDTHH:mm:ss
    req.WarehouseID = 1;            //Unique location for orders
    req.CurrencyCode = "usd";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.
    req.OrderSubStatusTy = 1;
    req.BatchID = 1;
    req.ReferralID = 1;

    //Send Request to Server and Get Response
    GetOrdersResponse res = api.GetOrders(req);

    //Now examine the results:

    foreach (OrderResponse order  in res.Orders)
    {
        Console.WriteLine("OrderID: {0}", order.OrderID);
        Console.WriteLine("CustomerID: {0}", order.CustomerID);
        Console.WriteLine("OrderStatus: {0}", order.OrderStatus);
        Console.WriteLine("OrderDate: {0}", order.OrderDate);
        Console.WriteLine("CurrencyCode: {0}", order.CurrencyCode);
        Console.WriteLine("WarehouseID: {0}", order.WarehouseID);
        Console.WriteLine("ShipMethodID: {0}", order.ShipMethodID);
        Console.WriteLine("PriceType: {0}", order.PriceType);
        Console.WriteLine("Total: {0}", order.Total);

        foreach (OrderDetailResponse orderDetail  in order.Details)
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

        foreach (PaymentResponse payment  in order.Payments)
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
        Console.WriteLine("BackOrderFromID: {0}", order.BackOrderFromID);
        Console.WriteLine("OrderKey: {0}", order.OrderKey);
        Console.WriteLine("CustomerKey: {0}", order.CustomerKey);
        Console.WriteLine("OrderSubStatusTy: {0}", order.OrderSubStatusTy);
        Console.WriteLine("BatchID: {0}", order.BatchID);
        Console.WriteLine("OrderTyID: {0}", order.OrderTyID);
        Console.WriteLine("OrderTyDescription: {0}", order.OrderTyDescription);
        Console.WriteLine("ReferralID: {0}", order.ReferralID);
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
    Dim req as new GetOrdersRequest()

    req.CustomerID = 1
    req.OrderID = 1
    req.OrderDateStart = DateTime.Today
    req.OrderDateEnd = DateTime.Today
    req.WarehouseID = 1
    req.CurrencyCode = "usd"
    req.CustomerKey = "1"
    req.OrderKey = "1"
    req.OrderSubStatusTy = 1
    req.BatchID = 1
    req.ReferralID = 1

    'Send Request to Server and Get Response
    Dim res As GetOrdersResponse = api.GetOrders(req)

    'Now examine the results:

    For Each order As OrderResponse In res.Orders
        Console.WriteLine("OrderID: {0}", order.OrderID)
        Console.WriteLine("CustomerID: {0}", order.CustomerID)
        Console.WriteLine("OrderStatus: {0}", order.OrderStatus)
        Console.WriteLine("OrderDate: {0}", order.OrderDate)
        Console.WriteLine("CurrencyCode: {0}", order.CurrencyCode)
        Console.WriteLine("WarehouseID: {0}", order.WarehouseID)
        Console.WriteLine("ShipMethodID: {0}", order.ShipMethodID)
        Console.WriteLine("PriceType: {0}", order.PriceType)
        Console.WriteLine("Total: {0}", order.Total)

        For Each orderDetail As OrderDetailResponse In order.Details
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

        For Each payment As PaymentResponse In order.Payments
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
        Console.WriteLine("BackOrderFromID: {0}", order.BackOrderFromID)
        Console.WriteLine("OrderKey: {0}", order.OrderKey)
        Console.WriteLine("CustomerKey: {0}", order.CustomerKey)
        Console.WriteLine("OrderSubStatusTy: {0}", order.OrderSubStatusTy)
        Console.WriteLine("BatchID: {0}", order.BatchID)
        Console.WriteLine("OrderTyID: {0}", order.OrderTyID)
        Console.WriteLine("OrderTyDescription: {0}", order.OrderTyDescription)
        Console.WriteLine("ReferralID: {0}", order.ReferralID)
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
    $req->OrderID = 1;
    $req->OrderDateStart = 1;
    $req->OrderDateEnd = 1;
    $req->WarehouseID = 1;
    $req->CurrencyCode = "usd";
    $req->CustomerKey = "1";
    $req->OrderKey = "1";
    $req->OrderSubStatusTy = 1;
    $req->BatchID = 1;
    $req->ReferralID = 1;

    //Send Request to Server and Get Response
    $res = $api.GetOrders($req);

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
    GetOrdersRequest req = new GetOrdersRequest();

    req.setCustomerID(1);
    req.setOrderID(1);
    req.setOrderDateStart(1);
    req.setOrderDateEnd(1);
    req.setWarehouseID(1);
    req.setCurrencyCode("usd");
    req.setCustomerKey("1");
    req.setOrderKey("1");
    req.setOrderSubStatusTy(1);
    req.setBatchID(1);
    req.setReferralID(1);

    //Send Request to Server and Get Response
    GetOrdersResponse res = api.getExigoApiSoap().getOrders(req, auth);

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
https://api.exigo.com/3.0/csv/?method=GetOrders
&ApiLoginName=String
&ApiPassword=String
&ApiCompany=String
&CustomerID=Nullable`1
&OrderID=Nullable`1
&OrderIDs=Int32[]
&OrderDateStart=Nullable`1
&OrderDateEnd=Nullable`1
&OrderStatus=Nullable`1
&OtherOrderStatuses=OrderStatusType[]
&OrderTypes=OrderType[]
&WarehouseID=Nullable`1
&CurrencyCode=String
&ReturnCustomer=Nullable`1
&ReturnKitDetails=Nullable`1
&GreaterThanOrderID=Nullable`1
&GreaterThanModifiedDate=Nullable`1
&BatchSize=Nullable`1
&Other11=String
&Other12=String
&Other13=String
&Other14=String
&Other15=String
&Other16=String
&Other17=String
&Other18=String
&Other19=String
&Other20=String
&PartyID=Nullable`1
&CustomerKey=String
&OrderKey=String
&OrderKeys=String[]
&OrderSubStatusTy=Nullable`1
&BatchID=Nullable`1
&OrderTys=String[]
&ReferralID=Nullable`1
Response FieldsOrderID,CustomerID,OrderStatus,OrderDate,CurrencyCode,WarehouseID,ShipMethodID,PriceType,FirstName,LastName,Company,Address1,Address2,Address3,City,State,Zip,Country,County,Email,Phone,Notes,Total,SubTotal,TaxTotal,ShippingTotal,DiscountTotal,DiscountPercent,WeightTotal,BusinessVolumeTotal,CommissionableVolumeTotal,TrackingNumber1,TrackingNumber2,TrackingNumber3,TrackingNumber4,TrackingNumber5,Other1Total,Other2Total,Other3Total,Other4Total,Other5Total,Other6Total,Other7Total,Other8Total,Other9Total,Other10Total,ShippingTax,OrderTax,FedTaxTotal,StateTaxTotal,FedShippingTax,StateShippingTax,CityShippingTax,CityLocalShippingTax,CountyShippingTax,CountyLocalShippingTax,Other11,Other12,Other13,Other14,Other15,Other16,Other17,Other18,Other19,Other20,ModifiedDate,OrderType,ShippedDate,CreatedDate,CreatedBy,ModifiedBy,TaxFedRate,TaxStateRate,TaxCityRate,TaxCityLocalRate,TaxCountyRate,TaxCountyLocalRate,TaxManualRate,TaxCity,TaxCounty,TaxState,TaxZip,TaxCountry,TaxIsExempt,TaxIsOverRide,OrderDetailID,ParentOrderDetailID,ItemCode,Description,Quantity,PriceEach,PriceTotal,Tax,WeightEach,Weight,BusinessVolumeEach,BusinesVolume,CommissionableVolumeEach,CommissionableVolume,Other1Each,Other1,Other2Each,Other2,Other3Each,Other3,Other4Each,Other4,Other5Each,Other5,Other6Each,Other6,Other7Each,Other7,Other8Each,Other8,Other9Each,Other9,Other10Each,Other10,ParentItemCode,Taxable,FedTax,StateTax,CityTax,CityLocalTax,CountyTax,CountyLocalTax,ManualTax,IsStateTaxOverride,OrderLine,Reference1,ShippingPriceEach,HandlingFee,BusinessVolume,PaymentID,CustomerID,PaymentType,PaymentDate,Amount,OrderID,CurrencyCode,BillingName,BillingAddress1,BillingAddress2,BillingCity,BillingState,BillingZip,BillingCountry,BankName,Memo,CreditCardNumberDisplay,AuthorizationCode,CreditCardType,CreditCardTypeDescription,OrderKey,CustomerKey,WalletTy,PaymentTypeId,ExpectedPaymentID,CustomerID,PaymentType,PaymentDate,Amount,OrderID,CurrencyCode,BillingName,AuthorizationCode,OrderKey,CustomerKey,PaymentTypeId,Customer,MiddleName,NameSuffix,AutoOrderID,PartyID,Reference1,IsRMA,BackOrderFromID,TransferToID,SuppressPackSlipPrice,ReturnOrderID,OrderKey,CustomerKey,ReplacementOrderID,OrderSubStatusTy,BatchID,OrderTyID,OrderTyDescription,ReferralID,RecordCount
Int32,Int32,OrderStatusType,DateTime,String,Int32,Int32,Int32,String,String,String,String,String,String,String,String,String,String,String,String,String,String,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,String,String,String,String,String,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,String,String,String,String,String,String,String,String,String,String,DateTime,OrderType,Nullable`1,DateTime,String,String,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,String,String,String,String,String,Boolean,Boolean,Nullable`1,Nullable`1,String,String,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,String,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Boolean,Int32,String,Decimal,Decimal,Decimal,Int32,Int32,PaymentType,DateTime,Decimal,Nullable`1,String,String,String,String,String,String,String,String,String,String,String,String,Int32,String,String,String,Int32,Int32,Int32,Int32,PaymentType,DateTime,Decimal,Nullable`1,String,String,String,String,String,Int32,CustomerResponse,String,String,Nullable`1,Nullable`1,String,Boolean,Nullable`1,Nullable`1,Boolean,Nullable`1,String,String,Nullable`1,Nullable`1,Nullable`1,Int32,String,Nullable`1,Int32

                    © 2026 Exigo.
```

</details>

---

### GetCountryRegions

>  Returns countries setup for company as well as the regions for a single country requested.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `GET /3.0/country/regionsAuthorization:` |
| SOAP action | `https://api.exigo.com/GetCountryRegions` |
| WSDL elements | `GetCountryRegionsRequest` → `GetCountryRegionsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetCountryRegions |

#### Input

**`GetCountryRegionsRequest`**

| Property | Type | Notes |
|---|---|---|
| `CountryCode` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |

#### Output

**`GetCountryRegionsResponse`**

| Property | Type | Notes |
|---|---|---|
| `Countries` | `CountryResponse[]` |  |
| `SelectedCountry` | `String` |  |
| `Regions` | `RegionResponse[]` |  |

**`CountryResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `CountryCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `CountryName` | `String` |  |

**`RegionResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `RegionCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `RegionName` | `String` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/country/regionsAuthorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "countries": null,
  "selectedCountry": "",
  "regions": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetCountryRegions"

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
    <GetCountryRegionsRequest xmlns="http://api.exigo.com/">
      <CountryCode>string</CountryCode>
    </GetCountryRegionsRequest>
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
    <GetCountryRegionsResult xmlns="http://api.exigo.com/">
      <Countries>
        <CountryResponse>
          <CountryCode>string</CountryCode>
          <CountryName>string</CountryName>
        </CountryResponse>
      </Countries>
      <SelectedCountry>string</SelectedCountry>
      <Regions>
        <RegionResponse>
          <RegionCode>string</RegionCode>
          <RegionName>string</RegionName>
        </RegionResponse>
      </Regions>
    </GetCountryRegionsResult>
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
    var req = new GetCountryRegionsRequest();

    //Send Request to Server and Get Response
    var res = await api.GetCountryRegionsAsync(req);

    //Now examine the results:

    foreach (var country  in res.Countries)
    {
        Console.WriteLine("CountryName: {0}", country.CountryName);
    }
    Console.WriteLine("SelectedCountry: {0}", res.SelectedCountry);

    foreach (var region  in res.Regions)
    {
        Console.WriteLine("RegionName: {0}", region.RegionName);
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
    GetCountryRegionsRequest req = new GetCountryRegionsRequest();

    //Send Request to Server and Get Response
    GetCountryRegionsResponse res = api.GetCountryRegions(req);

    //Now examine the results:

    foreach (CountryResponse country  in res.Countries)
    {
        Console.WriteLine("CountryName: {0}", country.CountryName);
    }
    Console.WriteLine("SelectedCountry: {0}", res.SelectedCountry);

    foreach (RegionResponse region  in res.Regions)
    {
        Console.WriteLine("RegionName: {0}", region.RegionName);
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
    Dim req as new GetCountryRegionsRequest()

    'Send Request to Server and Get Response
    Dim res As GetCountryRegionsResponse = api.GetCountryRegions(req)

    'Now examine the results:

    For Each country As CountryResponse In res.Countries
        Console.WriteLine("CountryName: {0}", country.CountryName)
    Next
    Console.WriteLine("SelectedCountry: {0}", res.SelectedCountry)

    For Each region As RegionResponse In res.Regions
        Console.WriteLine("RegionName: {0}", region.RegionName)
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
    $res = $api.GetCountryRegions($req);

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
    GetCountryRegionsRequest req = new GetCountryRegionsRequest();

    //Send Request to Server and Get Response
    GetCountryRegionsResponse res = api.getExigoApiSoap().getCountryRegions(req, auth);

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

### GetCustomerBalances

> Returns the sum of orders, payments, and adjustments per currency.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `GET /3.0/customers/balances?customerID=1` |
| SOAP action | `https://api.exigo.com/GetCustomerBalances` |
| WSDL elements | `GetCustomerBalancesRequest` → `GetCustomerBalancesResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetCustomerBalances |

#### Input

**`GetCustomerBalancesRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`GetCustomerBalancesResponse`**

| Property | Type | Notes |
|---|---|---|
| `CustomerBalances` | `CustomerBalanceResponse[]` |  |

**`CustomerBalanceResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `CurrencyCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `CurrencyDescription` | `String` |  |
| &nbsp;&nbsp;↳ `Balance` | `Decimal` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/customers/balances?customerID=1
  &customerKey=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "customerBalances": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetCustomerBalances"

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
    <GetCustomerBalancesRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
    </GetCustomerBalancesRequest>
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
    <GetCustomerBalancesResult xmlns="http://api.exigo.com/">
      <CustomerBalances>
        <CustomerBalanceResponse>
          <CurrencyCode>string</CurrencyCode>
          <CurrencyDescription>string</CurrencyDescription>
          <Balance>decimal</Balance>
        </CustomerBalanceResponse>
      </CustomerBalances>
    </GetCustomerBalancesResult>
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
    var req = new GetCustomerBalancesRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.GetCustomerBalancesAsync(req);

    //Now examine the results:

    foreach (var customerBalance  in res.CustomerBalances)
    {
        Console.WriteLine("CurrencyCode: {0}", customerBalance.CurrencyCode);
        Console.WriteLine("CurrencyDescription: {0}", customerBalance.CurrencyDescription);
        Console.WriteLine("Balance: {0}", customerBalance.Balance);
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
    GetCustomerBalancesRequest req = new GetCustomerBalancesRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    GetCustomerBalancesResponse res = api.GetCustomerBalances(req);

    //Now examine the results:

    foreach (CustomerBalanceResponse customerBalance  in res.CustomerBalances)
    {
        Console.WriteLine("CurrencyCode: {0}", customerBalance.CurrencyCode);
        Console.WriteLine("CurrencyDescription: {0}", customerBalance.CurrencyDescription);
        Console.WriteLine("Balance: {0}", customerBalance.Balance);
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
    Dim req as new GetCustomerBalancesRequest()

    req.CustomerID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As GetCustomerBalancesResponse = api.GetCustomerBalances(req)

    'Now examine the results:

    For Each customerBalance As CustomerBalanceResponse In res.CustomerBalances
        Console.WriteLine("CurrencyCode: {0}", customerBalance.CurrencyCode)
        Console.WriteLine("CurrencyDescription: {0}", customerBalance.CurrencyDescription)
        Console.WriteLine("Balance: {0}", customerBalance.Balance)
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
    $res = $api.GetCustomerBalances($req);

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
    GetCustomerBalancesRequest req = new GetCustomerBalancesRequest();

    req.setCustomerID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    GetCustomerBalancesResponse res = api.getExigoApiSoap().getCustomerBalances(req, auth);

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

### CreateCustomerBalanceAdjustment

> Create an adjustment for a customer's account in a currency.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `POST /3.0/customers/balances/adjustment` |
| SOAP action | `https://api.exigo.com/CreateCustomerBalanceAdjustment` |
| WSDL elements | `CreateCustomerBalanceAdjustmentRequest` → `CreateCustomerBalanceAdjustmentResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateCustomerBalanceAdjustment |

#### Input

**`CreateCustomerBalanceAdjustmentRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerTransactionTypeID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| `TransactionDate` | `DateTime` |  |
| `Amount` | `Decimal` |  |
| `CurrencyCode` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Notes` | `String` | Optional. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`CreateCustomerBalanceAdjustmentResponse`**

| Property | Type | Notes |
|---|---|---|
| `TransactionID` | `Int32` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/customers/balances/adjustment HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "transactionDate": "2026-11-10T00:00:00-06:00",
  "amount": null,
  "currencyCode": "usd",
  "notes": "",
  "customerKey": "1"
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
SOAPAction: "https://api.exigo.com/CreateCustomerBalanceAdjustment"

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
    <CreateCustomerBalanceAdjustmentRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerTransactionTypeID>int</CustomerTransactionTypeID>
      <TransactionDate>dateTime</TransactionDate>
      <Amount>decimal</Amount>
      <CurrencyCode>string</CurrencyCode>
      <Notes>string</Notes>
      <CustomerKey>string</CustomerKey>
    </CreateCustomerBalanceAdjustmentRequest>
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
    <CreateCustomerBalanceAdjustmentResult xmlns="http://api.exigo.com/">
      <TransactionID>int</TransactionID>
    </CreateCustomerBalanceAdjustmentResult>
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
    var req = new CreateCustomerBalanceAdjustmentRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.TransactionDate = DateTime.Today;
    req.Amount = 1;
    req.CurrencyCode = "usd";
    req.Notes = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.CreateCustomerBalanceAdjustmentAsync(req);

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
    CreateCustomerBalanceAdjustmentRequest req = new CreateCustomerBalanceAdjustmentRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.TransactionDate = DateTime.Today;
    req.Amount = 1;
    req.CurrencyCode = "usd";
    req.Notes = "1";
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    CreateCustomerBalanceAdjustmentResponse res = api.CreateCustomerBalanceAdjustment(req);

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
    Dim req as new CreateCustomerBalanceAdjustmentRequest()

    req.CustomerID = 1
    req.TransactionDate = DateTime.Today
    req.Amount = 1
    req.CurrencyCode = "usd"
    req.Notes = "1"
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As CreateCustomerBalanceAdjustmentResponse = api.CreateCustomerBalanceAdjustment(req)

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

    $req->CustomerID = 1;
    $req->TransactionDate = 1;
    $req->Amount = 1;
    $req->CurrencyCode = "usd";
    $req->Notes = "1";
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.CreateCustomerBalanceAdjustment($req);

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
    CreateCustomerBalanceAdjustmentRequest req = new CreateCustomerBalanceAdjustmentRequest();

    req.setCustomerID(1);
    req.setTransactionDate(1);
    req.setAmount(1);
    req.setCurrencyCode("usd");
    req.setNotes("1");
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    CreateCustomerBalanceAdjustmentResponse res = api.getExigoApiSoap().createCustomerBalanceAdjustment(req, auth);

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

### RefundPriorWalletCharge

> Refunds a prior wallet charge. To be used with an order.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `POST /3.0/payment/refund/wallet` |
| SOAP action | `https://api.exigo.com/RefundPriorWalletCharge` |
| WSDL elements | `RefundPriorWalletChargeRequest` → `RefundPriorWalletChargeResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=RefundPriorWalletCharge |

#### Input

**`RefundPriorWalletChargeRequest`**

| Property | Type | Notes |
|---|---|---|
| `ReturnPaymentID` | `Int32` |  |
| `OrderID` | `Int32` | Unique numeric identifier for order record. |
| `RefundOriginalOrder` | `Boolean` | Optional. Boolean value that allows payment to be applied directly to the original sales order. Defaults to False. |
| `MaxAmount` | `Decimal` | Optional. |
| `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided. |

#### Output

**`RefundPriorWalletChargeResponse`**

| Property | Type | Notes |
|---|---|---|
| `Amount` | `Decimal` |  |
| `AuthorizationCode` | `String` |  |
| `PaymentID` | `Int32` |  |
| `Message` | `String` |  |
| `DisplayMessage` | `String` |  |
| `MerchantTransactionKey` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/payment/refund/wallet HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "returnPaymentID": 1,
  "maxAmount": null,
  "orderKey": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "amount": null,
  "authorizationCode": "",
  "paymentID": 1,
  "message": "",
  "displayMessage": "",
  "merchantTransactionKey": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/RefundPriorWalletCharge"

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
    <RefundPriorWalletChargeRequest xmlns="http://api.exigo.com/">
      <ReturnPaymentID>int</ReturnPaymentID>
      <OrderID>int</OrderID>
      <RefundOriginalOrder>boolean</RefundOriginalOrder>
      <MaxAmount>decimal</MaxAmount>
      <OrderKey>string</OrderKey>
    </RefundPriorWalletChargeRequest>
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
    <RefundPriorWalletChargeResult xmlns="http://api.exigo.com/">
      <Amount>decimal</Amount>
      <AuthorizationCode>string</AuthorizationCode>
    </RefundPriorWalletChargeResult>
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
    var req = new RefundPriorWalletChargeRequest();

    req.ReturnPaymentID = 1;
    req.MaxAmount = 1;
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    var res = await api.RefundPriorWalletChargeAsync(req);

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
    RefundPriorWalletChargeRequest req = new RefundPriorWalletChargeRequest();

    req.ReturnPaymentID = 1;
    req.MaxAmount = 1;
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    RefundPriorWalletChargeResponse res = api.RefundPriorWalletCharge(req);

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
    Dim req as new RefundPriorWalletChargeRequest()

    req.ReturnPaymentID = 1
    req.MaxAmount = 1
    req.OrderKey = "1"

    'Send Request to Server and Get Response
    Dim res As RefundPriorWalletChargeResponse = api.RefundPriorWalletCharge(req)

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

    $req->ReturnPaymentID = 1;
    $req->MaxAmount = 1;
    $req->OrderKey = "1";

    //Send Request to Server and Get Response
    $res = $api.RefundPriorWalletCharge($req);

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
    RefundPriorWalletChargeRequest req = new RefundPriorWalletChargeRequest();

    req.setReturnPaymentID(1);
    req.setMaxAmount(1);
    req.setOrderKey("1");

    //Send Request to Server and Get Response
    RefundPriorWalletChargeResponse res = api.getExigoApiSoap().refundPriorWalletCharge(req, auth);

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

### GetOrderInvoice

> Returns an Rendered Order Invoice

| | |
|---|---|
| Category | Orders/Payments |
| REST | `GET /3.0/orders/invoice?orderID=1` |
| SOAP action | `https://api.exigo.com/GetOrderInvoice` |
| WSDL elements | `GetOrderInvoiceRequest` → `GetOrderInvoiceResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetOrderInvoice |

#### Input

**`GetOrderInvoiceRequest`**

| Property | Type | Notes |
|---|---|---|
| `OrderID` | `Int32` | Unique numeric identifier for order record. |
| `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. |
| `ReportlayoutID` | `Int32` | Optional. ReportlayoutID. Defaults to 0. |
| `Format` | `InvoiceRenderFormat` | Invoice Format.<br>**Values:** `HTML` |
| `AutoOrderID` | `Int32` | Optional. Unique numeric identifier for Auto Order record. |

#### Output

**`GetOrderInvoiceResponse`**

| Property | Type | Notes |
|---|---|---|
| `InvoiceData` | `Byte[]` | Rendered Order Byte Array. |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/orders/invoice?orderID=1
  &orderKey=1
  &reportlayoutID=1
  &format=1
  &autoOrderID=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "invoiceData": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetOrderInvoice"

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
    <GetOrderInvoiceRequest xmlns="http://api.exigo.com/">
      <OrderID>int</OrderID>
      <OrderKey>string</OrderKey>
      <ReportlayoutID>int</ReportlayoutID>
      <Format>HTML</Format>
      <AutoOrderID>int</AutoOrderID>
    </GetOrderInvoiceRequest>
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
    <GetOrderInvoiceResult xmlns="http://api.exigo.com/">
      <InvoiceData>base64Binary</InvoiceData>
    </GetOrderInvoiceResult>
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
    var req = new GetOrderInvoiceRequest();

    req.OrderID = 1;                //Unique numeric identifier for order record.
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record.
    req.ReportlayoutID = 1;         //ReportlayoutID.
    req.Format = InvoiceRenderFormat.HTML;                 //Invoice Format.
    req.AutoOrderID = 1;            //Unique numeric identifier for Auto Order record

    //Send Request to Server and Get Response
    var res = await api.GetOrderInvoiceAsync(req);

    //Now examine the results:

    foreach (var byte  in res.InvoiceData)
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
    GetOrderInvoiceRequest req = new GetOrderInvoiceRequest();

    req.OrderID = 1;                //Unique numeric identifier for order record.
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record.
    req.ReportlayoutID = 1;         //ReportlayoutID.
    req.Format = InvoiceRenderFormat.HTML;                 //Invoice Format.
    req.AutoOrderID = 1;            //Unique numeric identifier for Auto Order record

    //Send Request to Server and Get Response
    GetOrderInvoiceResponse res = api.GetOrderInvoice(req);

    //Now examine the results:

    foreach (Byte byte  in res.InvoiceData)
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
    Dim req as new GetOrderInvoiceRequest()

    req.OrderID = 1
    req.OrderKey = "1"
    req.ReportlayoutID = 1
    req.Format = InvoiceRenderFormat.HTML
    req.AutoOrderID = 1

    'Send Request to Server and Get Response
    Dim res As GetOrderInvoiceResponse = api.GetOrderInvoice(req)

    'Now examine the results:

    For Each byte As Byte In res.InvoiceData
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

    $req->OrderID = 1;
    $req->OrderKey = "1";
    $req->ReportlayoutID = 1;
    $req->Format = 1;
    $req->AutoOrderID = 1;

    //Send Request to Server and Get Response
    $res = $api.GetOrderInvoice($req);

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
    GetOrderInvoiceRequest req = new GetOrderInvoiceRequest();

    req.setOrderID(1);
    req.setOrderKey("1");
    req.setReportlayoutID(1);
    req.setFormat(1);
    req.setAutoOrderID(1);

    //Send Request to Server and Get Response
    GetOrderInvoiceResponse res = api.getExigoApiSoap().getOrderInvoice(req, auth);

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

### GetOrderInvoiceBatch

> Returns an rendered invoice of an orders batch

| | |
|---|---|
| Category | Orders/Payments |
| REST | `GET /3.0/orders/invoicebatch?reportlayoutID=1` |
| SOAP action | `https://api.exigo.com/GetOrderInvoiceBatch` |
| WSDL elements | `GetOrderInvoiceBatchRequest` → `GetOrderInvoiceBatchResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetOrderInvoiceBatch |

#### Input

**`GetOrderInvoiceBatchRequest`**

| Property | Type | Notes |
|---|---|---|
| `ReportlayoutID` | `Int32` | Optional. ReportlayoutID. Defaults to 0. |
| `BatchId` | `Int32` | Unique numeric identifier for the Batch. |
| `WarehouseId` | `Int32` | Unique numeric identifier for the batch's warehouse. |

#### Output

**`GetOrderInvoiceResponse`**

| Property | Type | Notes |
|---|---|---|
| `InvoiceData` | `Byte[]` | Rendered Order Byte Array. |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/orders/invoicebatch?reportlayoutID=1
  &batchId=1
  &warehouseId=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "invoiceData": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetOrderInvoiceBatch"

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
    <GetOrderInvoiceBatchRequest xmlns="http://api.exigo.com/">
      <ReportlayoutID>int</ReportlayoutID>
      <BatchId>int</BatchId>
      <WarehouseId>int</WarehouseId>
    </GetOrderInvoiceBatchRequest>
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
    <GetOrderInvoiceBatchResult xmlns="http://api.exigo.com/">
      <InvoiceData>base64Binary</InvoiceData>
    </GetOrderInvoiceBatchResult>
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
    var req = new GetOrderInvoiceBatchRequest();

    req.ReportlayoutID = 1;         //ReportlayoutID.
    req.BatchId = 1;                //Unique numeric identifier for the Batch
    req.WarehouseId = 1;            //Unique numeric identifier for the batch's warehouse

    //Send Request to Server and Get Response
    var res = await api.GetOrderInvoiceBatchAsync(req);

    //Now examine the results:

    foreach (var byte  in res.InvoiceData)
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
    GetOrderInvoiceBatchRequest req = new GetOrderInvoiceBatchRequest();

    req.ReportlayoutID = 1;         //ReportlayoutID.
    req.BatchId = 1;                //Unique numeric identifier for the Batch
    req.WarehouseId = 1;            //Unique numeric identifier for the batch's warehouse

    //Send Request to Server and Get Response
    GetOrderInvoiceResponse res = api.GetOrderInvoiceBatch(req);

    //Now examine the results:

    foreach (Byte byte  in res.InvoiceData)
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
    Dim req as new GetOrderInvoiceBatchRequest()

    req.ReportlayoutID = 1
    req.BatchId = 1
    req.WarehouseId = 1

    'Send Request to Server and Get Response
    Dim res As GetOrderInvoiceResponse = api.GetOrderInvoiceBatch(req)

    'Now examine the results:

    For Each byte As Byte In res.InvoiceData
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

    $req->ReportlayoutID = 1;
    $req->BatchId = 1;
    $req->WarehouseId = 1;

    //Send Request to Server and Get Response
    $res = $api.GetOrderInvoiceBatch($req);

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
    GetOrderInvoiceBatchRequest req = new GetOrderInvoiceBatchRequest();

    req.setReportlayoutID(1);
    req.setBatchId(1);
    req.setWarehouseId(1);

    //Send Request to Server and Get Response
    GetOrderInvoiceResponse res = api.getExigoApiSoap().getOrderInvoiceBatch(req, auth);

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

### ChargePriorAuthorization

>  Attempts to charge a prior authorization with the amount found on an existing order,
>  or a new order in a transaction. If the charge is successful, the order is changed to accepted.

| | |
|---|---|
| Category | Orders/Payments |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/ChargePriorAuthorization` |
| WSDL elements | `ChargePriorAuthorizationRequest` → `ChargePriorAuthorizationResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=ChargePriorAuthorization |

#### Input

**`ChargePriorAuthorizationRequest`**

| Property | Type | Notes |
|---|---|---|
| `MerchantTransactionKey` | `String` | Optional. |
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
SOAPAction: "https://api.exigo.com/ChargePriorAuthorization"

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
    <ChargePriorAuthorizationRequest xmlns="http://api.exigo.com/">
      <MerchantTransactionKey>string</MerchantTransactionKey>
      <OrderID>int</OrderID>
      <MaxAmount>decimal</MaxAmount>
      <OrderKey>string</OrderKey>
    </ChargePriorAuthorizationRequest>
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
    <ChargePriorAuthorizationResult xmlns="http://api.exigo.com/">
      <Amount>decimal</Amount>
      <AuthorizationCode>string</AuthorizationCode>
    </ChargePriorAuthorizationResult>
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
    var req = new ChargePriorAuthorizationRequest();

    req.MerchantTransactionKey = "1";
    req.OrderID = 1;                //Unique numeric identifier for order record.
    req.OrderKey = "DDks8235txcid"; //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    var res = await api.ChargePriorAuthorizationAsync(req);

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
    ChargePriorAuthorizationRequest req = new ChargePriorAuthorizationRequest();

    req.MerchantTransactionKey = "1";
    req.OrderID = 1;                //Unique numeric identifier for order record.
    req.OrderKey = "DDks8235txcid"; //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    ChargeCreditCardResponse res = api.ChargePriorAuthorization(req);

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
    Dim req as new ChargePriorAuthorizationRequest()

    req.MerchantTransactionKey = "1"
    req.OrderID = 1
    req.OrderKey = "DDks8235txcid"

    'Send Request to Server and Get Response
    Dim res As ChargeCreditCardResponse = api.ChargePriorAuthorization(req)

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

    $req->MerchantTransactionKey = "1";
    $req->OrderID = 1;
    $req->OrderKey = "DDks8235txcid";

    //Send Request to Server and Get Response
    $res = $api.ChargePriorAuthorization($req);

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
    ChargePriorAuthorizationRequest req = new ChargePriorAuthorizationRequest();

    req.setMerchantTransactionKey("1");
    req.setOrderID(1);
    req.setOrderKey("DDks8235txcid");

    //Send Request to Server and Get Response
    ChargeCreditCardResponse res = api.getExigoApiSoap().chargePriorAuthorization(req, auth);

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

### AuthorizeOnlyCreditCardToken

>  Attempts to authorize only a credit card token.
>  A follow up ChargePriorAuthorization will need to be issued to actually capture and settle the authorization.

| | |
|---|---|
| Category | Orders/Payments |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/AuthorizeOnlyCreditCardToken` |
| WSDL elements | `AuthorizeOnlyCreditCardTokenRequest` → `AuthorizeOnlyCreditCardTokenResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=AuthorizeOnlyCreditCardToken |

#### Input

**`AuthorizeOnlyCreditCardTokenRequest`**

| Property | Type | Notes |
|---|---|---|
| `CreditCardToken` | `String` | Optional. |
| `Amount` | `Decimal` |  |
| `BillingName` | `String` | Optional. |
| `BillingAddress` | `String` | Optional. |
| `BillingCity` | `String` | Optional. |
| `BillingState` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `BillingZip` | `String` | Optional. |
| `BillingCountry` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `WarehouseID` | `Int32` | Unique location for orders.<br>**Lookup:** company-specific list (see company-lists.md) |
| `CurrencyCode` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `CustomerID` | `Int32` | Unique numeric identifier for a customer record. |
| `CvcCode` | `String` | Optional. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`AuthorizeOnlyCreditCardResponse`**

| Property | Type | Notes |
|---|---|---|
| `AuthorizationCode` | `String` |  |
| `MerchantTransactionKey` | `String` |  |
| `Message` | `String` |  |
| `DisplayMessage` | `String` |  |

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/AuthorizeOnlyCreditCardToken"

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
    <AuthorizeOnlyCreditCardTokenRequest xmlns="http://api.exigo.com/">
      <CreditCardToken>string</CreditCardToken>
      <Amount>decimal</Amount>
      <BillingName>string</BillingName>
      <BillingAddress>string</BillingAddress>
      <BillingCity>string</BillingCity>
      <BillingState>string</BillingState>
      <BillingZip>string</BillingZip>
      <BillingCountry>string</BillingCountry>
      <WarehouseID>int</WarehouseID>
      <CurrencyCode>string</CurrencyCode>
      <CustomerID>int</CustomerID>
      <CvcCode>string</CvcCode>
      <CustomerKey>string</CustomerKey>
    </AuthorizeOnlyCreditCardTokenRequest>
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
    <AuthorizeOnlyCreditCardTokenResult xmlns="http://api.exigo.com/">
      <AuthorizationCode>string</AuthorizationCode>
      <MerchantTransactionKey>string</MerchantTransactionKey>
      <Message>string</Message>
      <DisplayMessage>string</DisplayMessage>
    </AuthorizeOnlyCreditCardTokenResult>
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
    var req = new AuthorizeOnlyCreditCardTokenRequest();

    req.CreditCardToken = "1";
    req.Amount = 1;
    req.BillingName = "1";
    req.BillingAddress = "1";
    req.BillingCity = "1";
    req.BillingZip = "1";
    req.WarehouseID = 1;            //Unique location for orders
    req.CurrencyCode = "usd";
    req.CustomerID = 1;             //Unique numeric identifier for a customer record.
    req.CvcCode = "1";
    req.CustomerKey = "DDks8235txcid";//Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.AuthorizeOnlyCreditCardTokenAsync(req);

    //Now examine the results:
    Console.WriteLine("AuthorizationCode: {0}", res.AuthorizationCode);
    Console.WriteLine("MerchantTransactionKey: {0}", res.MerchantTransactionKey);
    Console.WriteLine("Message: {0}", res.Message);
    Console.WriteLine("DisplayMessage: {0}", res.DisplayMessage);
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
    AuthorizeOnlyCreditCardTokenRequest req = new AuthorizeOnlyCreditCardTokenRequest();

    req.CreditCardToken = "1";
    req.Amount = 1;
    req.BillingName = "1";
    req.BillingAddress = "1";
    req.BillingCity = "1";
    req.BillingZip = "1";
    req.WarehouseID = 1;            //Unique location for orders
    req.CurrencyCode = "usd";
    req.CustomerID = 1;             //Unique numeric identifier for a customer record.
    req.CvcCode = "1";
    req.CustomerKey = "DDks8235txcid";//Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    AuthorizeOnlyCreditCardResponse res = api.AuthorizeOnlyCreditCardToken(req);

    //Now examine the results:
    Console.WriteLine("AuthorizationCode: {0}", res.AuthorizationCode);
    Console.WriteLine("MerchantTransactionKey: {0}", res.MerchantTransactionKey);
    Console.WriteLine("Message: {0}", res.Message);
    Console.WriteLine("DisplayMessage: {0}", res.DisplayMessage);
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
    Dim req as new AuthorizeOnlyCreditCardTokenRequest()

    req.CreditCardToken = "1"
    req.Amount = 1
    req.BillingName = "1"
    req.BillingAddress = "1"
    req.BillingCity = "1"
    req.BillingZip = "1"
    req.WarehouseID = 1
    req.CurrencyCode = "usd"
    req.CustomerID = 1
    req.CvcCode = "1"
    req.CustomerKey = "DDks8235txcid"

    'Send Request to Server and Get Response
    Dim res As AuthorizeOnlyCreditCardResponse = api.AuthorizeOnlyCreditCardToken(req)

    'Now examine the results:
    Console.WriteLine("AuthorizationCode: {0}", res.AuthorizationCode)
    Console.WriteLine("MerchantTransactionKey: {0}", res.MerchantTransactionKey)
    Console.WriteLine("Message: {0}", res.Message)
    Console.WriteLine("DisplayMessage: {0}", res.DisplayMessage)
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

    $req->CreditCardToken = "1";
    $req->Amount = 1;
    $req->BillingName = "1";
    $req->BillingAddress = "1";
    $req->BillingCity = "1";
    $req->BillingZip = "1";
    $req->WarehouseID = 1;
    $req->CurrencyCode = "usd";
    $req->CustomerID = 1;
    $req->CvcCode = "1";
    $req->CustomerKey = "DDks8235txcid";

    //Send Request to Server and Get Response
    $res = $api.AuthorizeOnlyCreditCardToken($req);

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
    AuthorizeOnlyCreditCardTokenRequest req = new AuthorizeOnlyCreditCardTokenRequest();

    req.setCreditCardToken("1");
    req.setAmount(1);
    req.setBillingName("1");
    req.setBillingAddress("1");
    req.setBillingCity("1");
    req.setBillingZip("1");
    req.setWarehouseID(1);
    req.setCurrencyCode("usd");
    req.setCustomerID(1);
    req.setCvcCode("1");
    req.setCustomerKey("DDks8235txcid");

    //Send Request to Server and Get Response
    AuthorizeOnlyCreditCardResponse res = api.getExigoApiSoap().authorizeOnlyCreditCardToken(req, auth);

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

### AuthorizeOnlyCreditCardTokenOnFile

>  Attempts to authorize only a credit card token on file.
>  A follow up ChargePriorAuthorization will need to be issued to actually capture and settle the authorization.

| | |
|---|---|
| Category | Orders/Payments |
| REST | Not available (docs: “Rest call not available for this method yet”) — use SOAP |
| SOAP action | `https://api.exigo.com/AuthorizeOnlyCreditCardTokenOnFile` |
| WSDL elements | `authorizeOnlyCreditCardTokenOnFileRequest` → `AuthorizeOnlyCreditCardTokenOnFileResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=AuthorizeOnlyCreditCardTokenOnFile |

#### Input

**`AuthorizeOnlyCreditCardTokenOnFileRequest`**

| Property | Type | Notes |
|---|---|---|
| `CreditCardAccountType` | `AccountCreditCardType` | **Values:** `Primary`, `Secondary` |
| `WarehouseID` | `Int32` | Unique location for orders.<br>**Lookup:** company-specific list (see company-lists.md) |
| `CurrencyCode` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `CustomerID` | `Int32` | Unique numeric identifier for a customer record. |
| `Amount` | `Decimal` |  |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`AuthorizeOnlyCreditCardResponse`**

| Property | Type | Notes |
|---|---|---|
| `AuthorizationCode` | `String` |  |
| `MerchantTransactionKey` | `String` |  |
| `Message` | `String` |  |
| `DisplayMessage` | `String` |  |

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/AuthorizeOnlyCreditCardTokenOnFile"

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
    <authorizeOnlyCreditCardTokenOnFileRequest xmlns="http://api.exigo.com/">
      <CreditCardAccountType>Primary or Secondary</CreditCardAccountType>
      <WarehouseID>int</WarehouseID>
      <CurrencyCode>string</CurrencyCode>
      <CustomerID>int</CustomerID>
      <Amount>decimal</Amount>
      <CustomerKey>string</CustomerKey>
    </authorizeOnlyCreditCardTokenOnFileRequest>
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
    <AuthorizeOnlyCreditCardTokenOnFileResult xmlns="http://api.exigo.com/">
      <AuthorizationCode>string</AuthorizationCode>
      <MerchantTransactionKey>string</MerchantTransactionKey>
      <Message>string</Message>
      <DisplayMessage>string</DisplayMessage>
    </AuthorizeOnlyCreditCardTokenOnFileResult>
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
    var req = new AuthorizeOnlyCreditCardTokenOnFileRequest();

    req.CreditCardAccountType = AccountCreditCardType.Primary;
    req.WarehouseID = 1;            //Unique location for orders
    req.CurrencyCode = "usd";
    req.CustomerID = 1;             //Unique numeric identifier for a customer record.
    req.Amount = 1;
    req.CustomerKey = "DDks8235txcid";//Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.AuthorizeOnlyCreditCardTokenOnFileAsync(req);

    //Now examine the results:
    Console.WriteLine("AuthorizationCode: {0}", res.AuthorizationCode);
    Console.WriteLine("MerchantTransactionKey: {0}", res.MerchantTransactionKey);
    Console.WriteLine("Message: {0}", res.Message);
    Console.WriteLine("DisplayMessage: {0}", res.DisplayMessage);
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
    AuthorizeOnlyCreditCardTokenOnFileRequest req = new AuthorizeOnlyCreditCardTokenOnFileRequest();

    req.CreditCardAccountType = AccountCreditCardType.Primary;
    req.WarehouseID = 1;            //Unique location for orders
    req.CurrencyCode = "usd";
    req.CustomerID = 1;             //Unique numeric identifier for a customer record.
    req.Amount = 1;
    req.CustomerKey = "DDks8235txcid";//Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    AuthorizeOnlyCreditCardResponse res = api.AuthorizeOnlyCreditCardTokenOnFile(req);

    //Now examine the results:
    Console.WriteLine("AuthorizationCode: {0}", res.AuthorizationCode);
    Console.WriteLine("MerchantTransactionKey: {0}", res.MerchantTransactionKey);
    Console.WriteLine("Message: {0}", res.Message);
    Console.WriteLine("DisplayMessage: {0}", res.DisplayMessage);
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
    Dim req as new AuthorizeOnlyCreditCardTokenOnFileRequest()

    req.CreditCardAccountType = AccountCreditCardType.Primary
    req.WarehouseID = 1
    req.CurrencyCode = "usd"
    req.CustomerID = 1
    req.Amount = 1
    req.CustomerKey = "DDks8235txcid"

    'Send Request to Server and Get Response
    Dim res As AuthorizeOnlyCreditCardResponse = api.AuthorizeOnlyCreditCardTokenOnFile(req)

    'Now examine the results:
    Console.WriteLine("AuthorizationCode: {0}", res.AuthorizationCode)
    Console.WriteLine("MerchantTransactionKey: {0}", res.MerchantTransactionKey)
    Console.WriteLine("Message: {0}", res.Message)
    Console.WriteLine("DisplayMessage: {0}", res.DisplayMessage)
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
    $req->WarehouseID = 1;
    $req->CurrencyCode = "usd";
    $req->CustomerID = 1;
    $req->Amount = 1;
    $req->CustomerKey = "DDks8235txcid";

    //Send Request to Server and Get Response
    $res = $api.AuthorizeOnlyCreditCardTokenOnFile($req);

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
    AuthorizeOnlyCreditCardTokenOnFileRequest req = new AuthorizeOnlyCreditCardTokenOnFileRequest();

    req.setCreditCardAccountType(1);
    req.setWarehouseID(1);
    req.setCurrencyCode("usd");
    req.setCustomerID(1);
    req.setAmount(1);
    req.setCustomerKey("DDks8235txcid");

    //Send Request to Server and Get Response
    AuthorizeOnlyCreditCardResponse res = api.getExigoApiSoap().authorizeOnlyCreditCardTokenOnFile(req, auth);

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

### RefundPriorDebitCharge

> Refunds a prior charge. To be used with an order.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `POST /3.0/payment/refund/debit` |
| SOAP action | `https://api.exigo.com/RefundPriorDebitCharge` |
| WSDL elements | `RefundPriorDebitChargeRequest` → `RefundPriorDebitChargeResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=RefundPriorDebitCharge |

#### Input

**`RefundPriorDebitChargeRequest`**

| Property | Type | Notes |
|---|---|---|
| `ReturnPaymentID` | `Int32` |  |
| `OrderID` | `Int32` | Unique numeric identifier for order record. |
| `RefundOriginalOrder` | `Boolean` | Optional. Boolean value that allows payment to be applied directly to the original sales order. Defaults to False. |
| `MaxAmount` | `Decimal` | Optional. |
| `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided. |

#### Output

**`RefundPriorDebitChargeResponse`**

| Property | Type | Notes |
|---|---|---|
| `Amount` | `Decimal` |  |
| `AuthorizationCode` | `String` |  |
| `PaymentID` | `Int32` |  |
| `Message` | `String` |  |
| `DisplayMessage` | `String` |  |
| `MerchantTransactionKey` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/payment/refund/debit HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "returnPaymentID": 1,
  "orderID": 1,
  "maxAmount": null,
  "orderKey": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "amount": null,
  "authorizationCode": "",
  "paymentID": 1,
  "message": "",
  "displayMessage": "",
  "merchantTransactionKey": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/RefundPriorDebitCharge"

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
    <RefundPriorDebitChargeRequest xmlns="http://api.exigo.com/">
      <ReturnPaymentID>int</ReturnPaymentID>
      <OrderID>int</OrderID>
      <RefundOriginalOrder>boolean</RefundOriginalOrder>
      <MaxAmount>decimal</MaxAmount>
      <OrderKey>string</OrderKey>
    </RefundPriorDebitChargeRequest>
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
    <RefundPriorDebitChargeResult xmlns="http://api.exigo.com/" />
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
    var req = new RefundPriorDebitChargeRequest();

    req.ReturnPaymentID = 1;
    req.OrderID = 1;                //Unique numeric identifier for order record.
    req.MaxAmount = 1;
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    var res = await api.RefundPriorDebitChargeAsync(req);

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
    RefundPriorDebitChargeRequest req = new RefundPriorDebitChargeRequest();

    req.ReturnPaymentID = 1;
    req.OrderID = 1;                //Unique numeric identifier for order record.
    req.MaxAmount = 1;
    req.OrderKey = "1";             //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.

    //Send Request to Server and Get Response
    RefundPriorDebitChargeResponse res = api.RefundPriorDebitCharge(req);

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
    Dim req as new RefundPriorDebitChargeRequest()

    req.ReturnPaymentID = 1
    req.OrderID = 1
    req.MaxAmount = 1
    req.OrderKey = "1"

    'Send Request to Server and Get Response
    Dim res As RefundPriorDebitChargeResponse = api.RefundPriorDebitCharge(req)

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

    $req->ReturnPaymentID = 1;
    $req->OrderID = 1;
    $req->MaxAmount = 1;
    $req->OrderKey = "1";

    //Send Request to Server and Get Response
    $res = $api.RefundPriorDebitCharge($req);

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
    RefundPriorDebitChargeRequest req = new RefundPriorDebitChargeRequest();

    req.setReturnPaymentID(1);
    req.setOrderID(1);
    req.setMaxAmount(1);
    req.setOrderKey("1");

    //Send Request to Server and Get Response
    RefundPriorDebitChargeResponse res = api.getExigoApiSoap().refundPriorDebitCharge(req, auth);

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

### ValidateWalletAccount

> Validates a Wallet Account.

| | |
|---|---|
| Category | Orders/Payments |
| REST | `POST /3.0/payment/validate/wallet` |
| SOAP action | `https://api.exigo.com/ValidateWalletAccount` |
| WSDL elements | `ValidateWalletAccountRequest` → `ValidateWalletAccountResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=ValidateWalletAccount |

#### Input

**`ValidateWalletAccountRequest`**

| Property | Type | Notes |
|---|---|---|
| `WalletAccountNumber` | `String` | Optional. |
| `WalletTy` | `Int32` | Required When ValidateWalletAccountOnFile = false.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Memo` | `String` | Optional. |
| `CustomerID` | `Int32` | Optional. Unique numeric identifier for a customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |
| `OrderID` | `Int32` | Optional. Unique numeric identifier for order record. |
| `OrderKey` | `String` | Optional. Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided. |
| `Other1` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other2` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other3` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other4` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other5` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other6` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other7` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other8` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other9` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Other10` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `ValidateWalletAccountOnFile` | `Boolean` | Optional. Use this option to validate information already on file. |
| `WalletAccountType` | `AccountWalletType` | Optional. To be used when ValidateWalletAccountOnFile = true. By Default will be Primary.<br>**Values:** `Primary`, `Secondary`, `Third`, `Fourth`, `Fifth` |
| `WarehouseID` | `Int32` | Optional. |
| `Email` | `String` | Optional. |
| `Phone` | `String` | Optional. |
| `CurrencyCode` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `ClientIpAddress` | `String` | Optional. |
| `BillingName` | `String` | Optional. |
| `BillingAddress1` | `String` | Optional. |
| `BillingAddress2` | `String` | Optional. |
| `BillingCity` | `String` | Optional. |
| `BillingState` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `BillingZip` | `String` | Optional. |
| `BillingCountry` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Amount` | `Decimal` | Optional. |

#### Output

**`ValidateWalletAccountResponse`**

| Property | Type | Notes |
|---|---|---|
| `AuthorizationCode` | `String` |  |
| `Message` | `String` |  |
| `Success` | `Boolean` |  |
| `DisplayMessage` | `String` |  |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/payment/validate/wallet HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "walletAccountNumber": "",
  "walletTy": 1,
  "memo": "",
  "customerID": 1,
  "customerKey": "DDks8235txcid",
  "orderID": 1,
  "orderKey": "DDks8235txcid",
  "validateWalletAccountOnFile": true,
  "walletAccountType": null,
  "warehouseID": 1,
  "email": "1",
  "phone": "1",
  "currencyCode": "usd",
  "clientIpAddress": "1",
  "billingName": "",
  "billingAddress1": "",
  "billingAddress2": "",
  "billingCity": "",
  "billingZip": "",
  "amount": null
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "authorizationCode": "",
  "message": "",
  "success": true,
  "displayMessage": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/ValidateWalletAccount"

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
    <ValidateWalletAccountRequest xmlns="http://api.exigo.com/">
      <WalletAccountNumber>string</WalletAccountNumber>
      <WalletTy>int</WalletTy>
      <Memo>string</Memo>
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
      <OrderID>int</OrderID>
      <OrderKey>string</OrderKey>
      <Other1>string</Other1>
      <Other2>string</Other2>
      <Other3>string</Other3>
      <Other4>string</Other4>
      <Other5>string</Other5>
      <Other6>string</Other6>
      <Other7>string</Other7>
      <Other8>string</Other8>
      <Other9>string</Other9>
      <Other10>string</Other10>
      <ValidateWalletAccountOnFile>boolean</ValidateWalletAccountOnFile>
      <WalletAccountType>Primary or Secondary or Third or Fourth or Fifth</WalletAccountType>
      <WarehouseID>int</WarehouseID>
      <Email>string</Email>
      <Phone>string</Phone>
      <CurrencyCode>string</CurrencyCode>
      <ClientIpAddress>string</ClientIpAddress>
      <BillingName>string</BillingName>
      <BillingAddress1>string</BillingAddress1>
      <BillingAddress2>string</BillingAddress2>
      <BillingCity>string</BillingCity>
      <BillingState>string</BillingState>
      <BillingZip>string</BillingZip>
      <BillingCountry>string</BillingCountry>
      <Amount>decimal</Amount>
    </ValidateWalletAccountRequest>
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
    <ValidateWalletAccountResult xmlns="http://api.exigo.com/">
      <AuthorizationCode>string</AuthorizationCode>
      <Message>string</Message>
      <Success>boolean</Success>
      <DisplayMessage>string</DisplayMessage>
    </ValidateWalletAccountResult>
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
    var req = new ValidateWalletAccountRequest();

    req.WalletAccountNumber = "1";
    req.WalletTy = 1;               //Required When ValidateWalletAccountOnFile = false
    req.Memo = "1";
    req.CustomerID = 1;             //Unique numeric identifier for a customer record.
    req.CustomerKey = "DDks8235txcid";//Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.OrderID = 1;                //Unique numeric identifier for order record.
    req.OrderKey = "DDks8235txcid"; //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.
    req.ValidateWalletAccountOnFile = true;//Optional. Use this option to validate information already on file
    req.WalletAccountType = AccountWalletType.Primary;      //Optional. To be used when ValidateWalletAccountOnFile = true. By Default will be Primary.
    req.WarehouseID = 1;            //Optional
    req.Email = "1";
    req.Phone = "1";
    req.CurrencyCode = "usd";
    req.ClientIpAddress = "1";
    req.BillingName = "1";
    req.BillingAddress1 = "1";
    req.BillingAddress2 = "1";
    req.BillingCity = "1";
    req.BillingZip = "1";
    req.Amount = 1;                 //Optional

    //Send Request to Server and Get Response
    var res = await api.ValidateWalletAccountAsync(req);

    //Now examine the results:
    Console.WriteLine("AuthorizationCode: {0}", res.AuthorizationCode);
    Console.WriteLine("Message: {0}", res.Message);
    Console.WriteLine("Success: {0}", res.Success);
    Console.WriteLine("DisplayMessage: {0}", res.DisplayMessage);
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
    ValidateWalletAccountRequest req = new ValidateWalletAccountRequest();

    req.WalletAccountNumber = "1";
    req.WalletTy = 1;               //Required When ValidateWalletAccountOnFile = false
    req.Memo = "1";
    req.CustomerID = 1;             //Unique numeric identifier for a customer record.
    req.CustomerKey = "DDks8235txcid";//Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.OrderID = 1;                //Unique numeric identifier for order record.
    req.OrderKey = "DDks8235txcid"; //Unique alpha numeric identifier for order record. Exeption will occur if OrderID & OrderKey are provided.
    req.ValidateWalletAccountOnFile = true;//Optional. Use this option to validate information already on file
    req.WalletAccountType = AccountWalletType.Primary;      //Optional. To be used when ValidateWalletAccountOnFile = true. By Default will be Primary.
    req.WarehouseID = 1;            //Optional
    req.Email = "1";
    req.Phone = "1";
    req.CurrencyCode = "usd";
    req.ClientIpAddress = "1";
    req.BillingName = "1";
    req.BillingAddress1 = "1";
    req.BillingAddress2 = "1";
    req.BillingCity = "1";
    req.BillingZip = "1";
    req.Amount = 1;                 //Optional

    //Send Request to Server and Get Response
    ValidateWalletAccountResponse res = api.ValidateWalletAccount(req);

    //Now examine the results:
    Console.WriteLine("AuthorizationCode: {0}", res.AuthorizationCode);
    Console.WriteLine("Message: {0}", res.Message);
    Console.WriteLine("Success: {0}", res.Success);
    Console.WriteLine("DisplayMessage: {0}", res.DisplayMessage);
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
    Dim req as new ValidateWalletAccountRequest()

    req.WalletAccountNumber = "1"
    req.WalletTy = 1
    req.Memo = "1"
    req.CustomerID = 1
    req.CustomerKey = "DDks8235txcid"
    req.OrderID = 1
    req.OrderKey = "DDks8235txcid"
    req.ValidateWalletAccountOnFile = true
    req.WalletAccountType = AccountWalletType.Primary
    req.WarehouseID = 1
    req.Email = "1"
    req.Phone = "1"
    req.CurrencyCode = "usd"
    req.ClientIpAddress = "1"
    req.BillingName = "1"
    req.BillingAddress1 = "1"
    req.BillingAddress2 = "1"
    req.BillingCity = "1"
    req.BillingZip = "1"
    req.Amount = 1

    'Send Request to Server and Get Response
    Dim res As ValidateWalletAccountResponse = api.ValidateWalletAccount(req)

    'Now examine the results:
    Console.WriteLine("AuthorizationCode: {0}", res.AuthorizationCode)
    Console.WriteLine("Message: {0}", res.Message)
    Console.WriteLine("Success: {0}", res.Success)
    Console.WriteLine("DisplayMessage: {0}", res.DisplayMessage)
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

    $req->WalletAccountNumber = "1";
    $req->WalletTy = 1;
    $req->Memo = "1";
    $req->CustomerID = 1;
    $req->CustomerKey = "DDks8235txcid";
    $req->OrderID = 1;
    $req->OrderKey = "DDks8235txcid";
    $req->ValidateWalletAccountOnFile = 1;
    $req->WalletAccountType = 1;
    $req->WarehouseID = 1;
    $req->Email = "1";
    $req->Phone = "1";
    $req->CurrencyCode = "usd";
    $req->ClientIpAddress = "1";
    $req->BillingName = "1";
    $req->BillingAddress1 = "1";
    $req->BillingAddress2 = "1";
    $req->BillingCity = "1";
    $req->BillingZip = "1";
    $req->Amount = 1;

    //Send Request to Server and Get Response
    $res = $api.ValidateWalletAccount($req);

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
    ValidateWalletAccountRequest req = new ValidateWalletAccountRequest();

    req.setWalletAccountNumber("1");
    req.setWalletTy(1);
    req.setMemo("1");
    req.setCustomerID(1);
    req.setCustomerKey("DDks8235txcid");
    req.setOrderID(1);
    req.setOrderKey("DDks8235txcid");
    req.setValidateWalletAccountOnFile(1);
    req.setWalletAccountType(1);
    req.setWarehouseID(1);
    req.setEmail("1");
    req.setPhone("1");
    req.setCurrencyCode("usd");
    req.setClientIpAddress("1");
    req.setBillingName("1");
    req.setBillingAddress1("1");
    req.setBillingAddress2("1");
    req.setBillingCity("1");
    req.setBillingZip("1");
    req.setAmount(1);

    //Send Request to Server and Get Response
    ValidateWalletAccountResponse res = api.getExigoApiSoap().validateWalletAccount(req, auth);

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
