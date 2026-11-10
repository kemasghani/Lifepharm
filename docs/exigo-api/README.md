# Exigo Web Services API — knowledge base

Full crawl of **https://api.exigo.com/3.0/** (API version **v2025.11.7.6**), done 2026-11-11. Every menu category and sub-menu method was read, plus every method that exists in the WSDL but is not linked in the menu. Nothing was summarised away: each operation file keeps the full input/output tables, enum values, REST and SOAP examples and all code samples (C# REST, C# SOAP, VB.Net, PHP, Java, CSV).

## Coverage

| Item | Count |
|---|---|
| Operations in WSDL | 294 |
| Listed in docs menu | 252 (18 categories) |
| Unlisted but documented (WSDL only) | 42 |
| Operations with REST endpoint | 251 |
| SOAP-only operations | 43 |
| Operations with CSV output | 15 |
| Complex types (WSDL) | 792 → [types.md](types.md) |
| Enums (WSDL) | 43 → [enums.md](enums.md) |
| Company-specific lookup fields | 326 distinct → [company-lists.md](company-lists.md) |

Not publicly readable (needs an Exigo developer login): `doc/ChangeLog.aspx` (“Changes”) and `doc/ListHelp.aspx` (company-specific value lists).

## Transports and authentication

Exigo exposes the same operations over three transports:

**1. REST (JSON)** — `https://{company}-api.exigo.com/3.0/{resource}`

```http
POST https://yourcompany-api.exigo.com/3.0/orders HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)
```

- HTTP Basic auth where the user name is `login@company`.
- JSON property names are camelCase versions of the documented PascalCase properties (`CustomerID` → `customerID`).
- Not every operation has a REST route; SOAP-only operations are marked in the index.
- .NET helper: NuGet package `Exigo.Api.Client` (`new ExigoApiClient("company","login","password")`, async methods such as `CreateOrderAsync`).

**2. SOAP 1.1 / 1.2** — `POST https://api.exigo.com/3.0/ExigoApi.asmx`, namespace `http://api.exigo.com/`, `SOAPAction: "https://api.exigo.com/{Operation}"`. WSDL: `https://api.exigo.com/3.0/ExigoApi.asmx?WSDL`.

Every SOAP call carries an `ApiAuthentication` header:

| Field | Type | Notes |
|---|---|---|
| `LoginName` | string | API login |
| `Password` | string | API password |
| `Company` | string | Exigo company key |
| `Identity` | string | optional |
| `RequestTimeUtc` | dateTime | schema marks it required (minOccurs=1); the docs samples leave it as a placeholder |
| `Signature` | string | optional; the public docs do not describe a signing scheme |

**3. CSV (read operations)** — `GET https://api.exigo.com/3.0/csv/?method={Operation}&ApiLoginName=…&ApiPassword=…&ApiCompany=…&{params}`; supported only where the method page says so.

## Conventions seen across the docs

- Request/response objects are named `{Operation}Request` / `{Operation}Response`; SOAP result element is `{Operation}Result`.
- Customers can be addressed by `CustomerID` (Int32) **or** `CustomerKey` (string); sending both raises an exception.
- Many write operations “can participate in a transaction” — wrap them with `ProcessTransaction` to commit atomically (e.g. create customer + order + auto-order).
- Optional properties are marked “Optional.” in Notes; WSDL `min=0` fields are optional, `max=unbounded` are arrays.
- Fields with a lookup marker take company-configured IDs (see company-lists.md).

## Categories

| # | Category | Operations | Description |
|---|---|---|---|
| 1 | [Customers](operations/01-customers.md) | 28 | Customer management protocols for creating, updating, and administering customer entitys. This section also contains tools for tree placement, billing, and social media integration, along with customer site management. |
| 2 | [Orders/Payments](operations/02-orders-payments.md) | 36 | A robust API for handling all transaction functions, including batch orders, invoicing, payment methods, and more. Full authentication is provided to support credit, debit and ACH transactions. |
| 3 | [Recurring Orders](operations/03-recurring-orders.md) | 6 |  |
| 4 | [Items](operations/04-items.md) | 17 |  |
| 5 | [Tree Movement](operations/05-tree-movement.md) | 6 |  |
| 6 | [Payout](operations/06-payout.md) | 10 |  |
| 7 | [Reporting](operations/07-reporting.md) | 12 |  |
| 8 | [Communications](operations/08-communications.md) | 12 |  |
| 9 | [Party Plan](operations/09-party-plan.md) | 11 |  |
| 10 | [Points/Subscriptions](operations/10-points-subscriptions.md) | 4 |  |
| 11 | [Calendar](operations/11-calendar.md) | 3 |  |
| 12 | [Customer Leads](operations/12-customer-leads.md) | 6 |  |
| 13 | [Users](operations/13-users.md) | 2 |  |
| 14 | [Files/Folders](operations/14-files-folders.md) | 7 | Customer file and folder management operations |
| 15 | [Web Content](operations/15-web-content.md) | 45 | Language translations, content and resource set management operations |
| 16 | [Extended DB](operations/16-extended-db.md) | 7 |  |
| 17 | [Sync](operations/17-sync.md) | 24 |  |
| 18 | [Other](operations/18-other.md) | 16 |  |
| 19 | [Unlisted (WSDL only)](operations/19-unlisted-wsdl-only.md) | 42 |  |

## All operations

| Operation | Category | REST | Summary |
|---|---|---|---|
| [AddBankAccountType](operations/18-other.md#addbankaccounttype) | Other | `POST /3.0/settings/bankaccounttype` | Adds a Bank Account Type. |
| [AddPartyGuests](operations/09-party-plan.md#addpartyguests) | Party Plan | `POST /3.0/party/guest` | Adds one or more guests to a party. |
| [AddProductsToCategory](operations/04-items.md#addproductstocategory) | Items | `POST /3.0/webcategory/product` | Adds items/products to a web category. Note: This request can participate in a transaction. Learn more about transactions. |
| [AdjustInventory](operations/04-items.md#adjustinventory) | Items | `PUT /3.0/warehouse/inventory` | Posts an adjustment to item inventory. |
| [AppendCustomerNotes](operations/01-customers.md#appendcustomernotes) | Customers | `PATCH /3.0/customers/notes` | Appends a specified value to the specified Customer's Notes record Note: This request can participate in a transaction. Learn more about… |
| [AuthenticateCustomer](operations/01-customers.md#authenticatecustomer) | Customers | `POST /3.0/customers/authenticate` | Authenticates a customer for login using UserName and Password combination. |
| [AuthenticateUser](operations/13-users.md#authenticateuser) | Users | `POST /3.0/user/authenticate` | Authenticates a corporate user for login using UserName and Password combination. |
| [AuthorizeOnlyCreditCardToken](operations/02-orders-payments.md#authorizeonlycreditcardtoken) | Orders/Payments | SOAP only | Attempts to authorize only a credit card token. A follow up ChargePriorAuthorization will need to be issued to actually capture and settle… |
| [AuthorizeOnlyCreditCardTokenOnFile](operations/02-orders-payments.md#authorizeonlycreditcardtokenonfile) | Orders/Payments | SOAP only | Attempts to authorize only a credit card token on file. A follow up ChargePriorAuthorization will need to be issued to actually capture and… |
| [AutoOrderSkipNextShipment](operations/03-recurring-orders.md#autoorderskipnextshipment) | Recurring Orders | `POST /3.0/autoorder/skip` | Disables the auotorder next scheduled date |
| [CalculateOrder](operations/02-orders-payments.md#calculateorder) | Orders/Payments | `POST /3.0/orders/calculate` | Calculates pricing, tax, shipping and volume info for a potential order. This is for calculation only and does not store a permanent… |
| [ChangeAutoOrderStatus](operations/03-recurring-orders.md#changeautoorderstatus) | Recurring Orders | `POST /3.0/autoorder/status` | Changes the status of an AutoOrder. This is typically used to delete or suspend an auto order. |
| [ChangeOrderStatus](operations/02-orders-payments.md#changeorderstatus) | Orders/Payments | `POST /3.0/orders/status` | Changes an existing order from one status to another. |
| [ChangeOrderStatusBatch](operations/02-orders-payments.md#changeorderstatusbatch) | Orders/Payments | `POST /3.0/orders/statusbatch` | Changes existing orders from one status to another in a batch. Can optionally update tracking numbers as well. |
| [ChargeCreditCard](operations/19-unlisted-wsdl-only.md#chargecreditcard) | Unlisted (WSDL only) | SOAP only | Deprecated. Use ChargeCreditCardToken instead. |
| [ChargeCreditCardOnFile](operations/19-unlisted-wsdl-only.md#chargecreditcardonfile) | Unlisted (WSDL only) | SOAP only | Deprecated. Use ChargeCreditCardTokenOnFile instead. |
| [ChargeCreditCardToken](operations/02-orders-payments.md#chargecreditcardtoken) | Orders/Payments | `POST /3.0/payment/charge/token` | Attempts to charge a card token with the amount found on an exiting order, or a new order in a transaction.If the charge is successful, the… |
| [ChargeCreditCardTokenOnFile](operations/02-orders-payments.md#chargecreditcardtokenonfile) | Orders/Payments | `POST /3.0/payment/charge/tokenonfile` | Attempts to charge a card token on file with the amount found on an exiting order, or a new order in a transaction. If the charge is… |
| [ChargeGroupOrderCreditCardToken](operations/02-orders-payments.md#chargegroupordercreditcardtoken) | Orders/Payments | `POST /3.0/payment/charge/tokengroup` | Attempts to charge a card token with the amount found on the specified orders. |
| [ChargePriorAuthorization](operations/02-orders-payments.md#chargepriorauthorization) | Orders/Payments | SOAP only | Attempts to charge a prior authorization with the amount found on an existing order, or a new order in a transaction. If the charge is… |
| [ChargeWalletAccount](operations/02-orders-payments.md#chargewalletaccount) | Orders/Payments | `POST /3.0/payment/charge/wallet` | Attempts to debit a wallet account with the amount found on an exiting order, or a new order in a transaction. If the debit request is… |
| [ChargeWalletAccountOnFile](operations/02-orders-payments.md#chargewalletaccountonfile) | Orders/Payments | `POST /3.0/payment/charge/walletonfile` | Attempts to debit a wallet account with the amount found on an exiting order, or a new order in a transaction. If the debit request is… |
| [CreateAdminWhitelist](operations/18-other.md#createadminwhitelist) | Other | `POST /3.0/whitelist/admin` | Create a new Whitelisted IP range for Admin |
| [CreateApiWhitelist](operations/18-other.md#createapiwhitelist) | Other | `POST /3.0/whitelist/api` | Create a new Whitelisted IP range |
| [CreateAutoOrder](operations/03-recurring-orders.md#createautoorder) | Recurring Orders | `POST /3.0/autoorder` | Create a new Recurring Order template for an existing customer or a new customer as part of a transaction. Client provides schedule, item… |
| [CreateBill](operations/06-payout.md#createbill) | Payout | `POST /3.0/bill` | Creates a new bill |
| [CreateBillPayout](operations/06-payout.md#createbillpayout) | Payout | `POST /3.0/payout/createpayout` | Creates payment transaction records for customer bills. This method does not process third party transactions |
| [CreateBills](operations/06-payout.md#createbills) | Payout | `POST /3.0/bills` | Creates max 100 new bills |
| [CreateCalendarItem](operations/11-calendar.md#createcalendaritem) | Calendar | `POST /3.0/calendar/item` | Creates a new calendar item. Note: This request can participate in a transaction. Learn more about transactions. |
| [CreateCustomer](operations/01-customers.md#createcustomer) | Customers | `POST /3.0/customers` | Creates a new Customer. Can optionally be put in one or more trees. |
| [CreateCustomerBalanceAdjustment](operations/02-orders-payments.md#createcustomerbalanceadjustment) | Orders/Payments | `POST /3.0/customers/balances/adjustment` | Create an adjustment for a customer's account in a currency. |
| [CreateCustomerContact](operations/19-unlisted-wsdl-only.md#createcustomercontact) | Unlisted (WSDL only) | SOAP only | Creates a new customer contact. Note: This request can participate in a transaction. Learn more about transactions. |
| [CreateCustomerExtended](operations/01-customers.md#createcustomerextended) | Customers | `POST /3.0/customers/extended` | Creates a new customer extended record. Note: This request can participate in a transaction. Learn more about transactions. |
| [CreateCustomerFile](operations/14-files-folders.md#createcustomerfile) | Files/Folders | `POST /3.0/file` | Creates a file for the customer in their default directory |
| [CreateCustomerFolder](operations/14-files-folders.md#createcustomerfolder) | Files/Folders | `POST /3.0/folder` | Creates a folder for the customer in their default directory or a chosen parent folder. |
| [CreateCustomerInquiry](operations/01-customers.md#createcustomerinquiry) | Customers | `POST /3.0/customers/inquiry` | Creates a customer history record. |
| [CreateCustomerLead](operations/12-customer-leads.md#createcustomerlead) | Customer Leads | `POST /3.0/customerlead` | Creates a new customer lead. Note: This request can participate in a transaction. Learn more about transactions. |
| [CreateCustomerWallItem](operations/01-customers.md#createcustomerwallitem) | Customers | `POST /3.0/customers/wall` | Create new wall item in CustomerWall table. Note: This request can participate in a transaction. Learn more about transactions. |
| [CreateDestination](operations/17-sync.md#createdestination) | Sync | `POST /3.0/destination` | Creates a destination. |
| [CreateEmail](operations/19-unlisted-wsdl-only.md#createemail) | Unlisted (WSDL only) | SOAP only | Creates an email. Note: This request can participate in a transaction. Learn more about transactions. |
| [CreateEmailTemplate](operations/19-unlisted-wsdl-only.md#createemailtemplate) | Unlisted (WSDL only) | SOAP only | Creates an email template. Note: This request can participate in a transaction. Learn more about transactions. |
| [CreateExpectedBankWire](operations/02-orders-payments.md#createexpectedbankwire) | Orders/Payments | `POST /3.0/payment/wire` | Creates a new expected payment of type Bank Bire. Note: This request can participate in a transaction. Learn more about transactions. |
| [CreateExpectedPayment](operations/02-orders-payments.md#createexpectedpayment) | Orders/Payments | `POST /3.0/payment/expectedpayment` | Creates a new expected payment type using cash, money order etc. Note: This request can participate in a transaction. Learn more about… |
| [CreateExtendedDbEntity](operations/16-extended-db.md#createextendeddbentity) | Extended DB | `POST /3.0/extendeddb` | Create Extended DB Entity. |
| [CreateExtendedDbSchema](operations/16-extended-db.md#createextendeddbschema) | Extended DB | `POST /3.0/extendeddb/schema` | Create new Extended DB schema. |
| [CreateGuest](operations/09-party-plan.md#createguest) | Party Plan | `POST /3.0/guest` | Creates a new guest. Can optionally be put in a party. |
| [CreateItem](operations/04-items.md#createitem) | Items | `POST /3.0/item` | Adds an Item (and optional warehouse/price info) Note: This request can participate in a transaction. Learn more about transactions. |
| [CreateMailFolder](operations/19-unlisted-wsdl-only.md#createmailfolder) | Unlisted (WSDL only) | SOAP only | Creates a mail folder. Note: This request can participate in a transaction. Learn more about transactions. |
| [CreateOrder](operations/02-orders-payments.md#createorder) | Orders/Payments | `POST /3.0/orders` | Creates a new Order for an existing customer. Can create an order for a new customer if part of a transaction. Server will calculate all… |
| [CreateOrderDetail](operations/19-unlisted-wsdl-only.md#createorderdetail) | Unlisted (WSDL only) | SOAP only | Create a new Order Detail for an existing order without recalculating. Can participate in a transaction. Note: This request can participate… |
| [CreateOrderImport](operations/02-orders-payments.md#createorderimport) | Orders/Payments | `POST /3.0/orders/import` | Imports a new Order for an existing customer. Use this for import routines or other instances where you wish to supply all calculation… |
| [CreateParty](operations/09-party-plan.md#createparty) | Party Plan | `POST /3.0/party` | Creates a new Party |
| [CreatePayment](operations/02-orders-payments.md#createpayment) | Orders/Payments | `POST /3.0/payment` | Creates a new payment type using cash, money order etc. |
| [CreatePaymentCheck](operations/02-orders-payments.md#createpaymentcheck) | Orders/Payments | `POST /3.0/payment/check` | Creates a new payment using check information. |
| [CreatePaymentCreditCard](operations/02-orders-payments.md#createpaymentcreditcard) | Orders/Payments | `POST /3.0/payment/creditcard` | Creates a specific credit card payment for an existing order, or a new order in a transaction. Note: This does not charge a card, and you… |
| [CreatePaymentPointAccount](operations/02-orders-payments.md#createpaymentpointaccount) | Orders/Payments | `POST /3.0/payment/pointaccount` | Creates a new payment for point account. |
| [CreatePaymentWallet](operations/02-orders-payments.md#createpaymentwallet) | Orders/Payments | `POST /3.0/payment/wallet` | Creates a new payment for wallet account. |
| [CreatePayout](operations/19-unlisted-wsdl-only.md#createpayout) | Unlisted (WSDL only) | `POST /3.0/payout` | Creates a new payout for one or more bills and updates status |
| [CreatePointTransaction](operations/10-points-subscriptions.md#createpointtransaction) | Points/Subscriptions | `POST /3.0/point` | Create a transaction that adjusts or redeems points from a customer's point account. |
| [CreateRelease](operations/15-web-content.md#createrelease) | Web Content | `POST /3.0/resourceset/release` | Creates a Resource Set release |
| [CreateResourceSet](operations/15-web-content.md#createresourceset) | Web Content | `POST /3.0/resourceset` | Create a new ResourceSet |
| [CreateResourceSetBannerItem](operations/15-web-content.md#createresourcesetbanneritem) | Web Content | `POST /3.0/resourceitem/banner` | Adds a ResourceSet Banner Item to the ResourceSet |
| [CreateResourceSetBooleanItem](operations/15-web-content.md#createresourcesetbooleanitem) | Web Content | `POST /3.0/resourceitem/bool` | Adds a ResourceSet CheckBox Item to the ResourceSet |
| [CreateResourceSetCarouselItem](operations/15-web-content.md#createresourcesetcarouselitem) | Web Content | `POST /3.0/resourceitem/carousel` | Adds a ResourceSet Carousel Item to the ResourceSet |
| [CreateResourceSetCulture](operations/15-web-content.md#createresourcesetculture) | Web Content | `POST /3.0/resourceset/culture` | Adds a culture to a Resource Set |
| [CreateResourceSetDataSetItem](operations/15-web-content.md#createresourcesetdatasetitem) | Web Content | `POST /3.0/resourceitem/dataset` | Adds a ResourceSet DataSet Item to the ResourceSet |
| [CreateResourceSetDateItem](operations/15-web-content.md#createresourcesetdateitem) | Web Content | `POST /3.0/resourceitem/date` | Adds a ResourceSet Date Item to the ResourceSet |
| [CreateResourceSetDecimalItem](operations/15-web-content.md#createresourcesetdecimalitem) | Web Content | `POST /3.0/resourceitem/decimal` | Adds a ResourceSet Decimal Item to the ResourceSet |
| [CreateResourceSetDropDownItem](operations/15-web-content.md#createresourcesetdropdownitem) | Web Content | `POST /3.0/resourceitem/dropdown` | Adds a ResourceSet DropDown Item to the ResourceSet |
| [CreateResourceSetEnvironment](operations/15-web-content.md#createresourcesetenvironment) | Web Content | `POST /3.0/resourceset/environment` | Creates a ResourceSet Environment |
| [CreateResourceSetGroup](operations/15-web-content.md#createresourcesetgroup) | Web Content | `POST /3.0/resourceset/group` | Creates a ResourceSet Group |
| [CreateResourceSetImageItem](operations/15-web-content.md#createresourcesetimageitem) | Web Content | `POST /3.0/resourceitem/image` | Adds a ResourceSet Image Item to the ResourceSet |
| [CreateResourceSetIntItem](operations/15-web-content.md#createresourcesetintitem) | Web Content | `POST /3.0/resourceitem/int` | Adds a ResourceSet Number Item to the ResourceSet |
| [CreateResourceSetTextItem](operations/15-web-content.md#createresourcesettextitem) | Web Content | `POST /3.0/resourceitem/text` | Adds a ResourceSet Text Item to the ResourceSet |
| [CreateResourceSetWidgetItem](operations/15-web-content.md#createresourcesetwidgetitem) | Web Content | `POST /3.0/resourceitem/widget` | Adds a ResourceSet Widget Item to the ResourceSet |
| [CreateSilentLoginCipher](operations/01-customers.md#createsilentlogincipher) | Customers | `GET /3.0/customers/createsilentlogincipher?silentLoginKey=1` | Creates backoffice silent login authentication cipher |
| [CreateTableFilterSettings](operations/17-sync.md#createtablefiltersettings) | Sync | SOAP only | Creates Table Filter Settings. |
| [CreateVendorBill](operations/19-unlisted-wsdl-only.md#createvendorbill) | Unlisted (WSDL only) | SOAP only | Creates a new VendorBill for a customer on file. |
| [CreateWarehouse](operations/18-other.md#createwarehouse) | Other | `POST /3.0/warehouse` | Creates a new Warehouse |
| [CreateWebCategory](operations/04-items.md#createwebcategory) | Items | `POST /3.0/webcategory` | Creates a new product web category. Note: This request can participate in a transaction. Learn more about transactions. |
| [DebitBankAccount](operations/02-orders-payments.md#debitbankaccount) | Orders/Payments | `POST /3.0/payment/charge/bank` | Attempts to debit a bank account with the amount found on an exiting order, or a new order in a transaction. If the debit request is… |
| [DebitBankAccountOnFile](operations/02-orders-payments.md#debitbankaccountonfile) | Orders/Payments | `POST /3.0/payment/charge/bankonfile` | Attempts to debit a bank account on file with the amount found on an exiting order, or a new order in a transaction. If the debit request… |
| [DeleteBankAccountType](operations/18-other.md#deletebankaccounttype) | Other | `DELETE /3.0/settings/bankaccounttype` | Deletes a Bank Account Type. |
| [DeleteCalendarItem](operations/11-calendar.md#deletecalendaritem) | Calendar | `DELETE /3.0/calendar/item` | Deletes a calendar item. Note: This request can participate in a transaction. Learn more about transactions. |
| [DeleteCustomerContact](operations/19-unlisted-wsdl-only.md#deletecustomercontact) | Unlisted (WSDL only) | SOAP only | Deletes a customer contact. Note: This request can participate in a transaction. Learn more about transactions. |
| [DeleteCustomerExtended](operations/01-customers.md#deletecustomerextended) | Customers | `DELETE /3.0/customers/extended` | Removes one customer extended record. Note: This request can participate in a transaction. Learn more about transactions. |
| [DeleteCustomerFileFolder](operations/14-files-folders.md#deletecustomerfilefolder) | Files/Folders | `DELETE /3.0/folder` | Deletes a file or folder for the customer in their default directory or a chosen parent folder. |
| [DeleteCustomerLead](operations/12-customer-leads.md#deletecustomerlead) | Customer Leads | `DELETE /3.0/customerlead` | Deletes a customer lead. |
| [DeleteCustomerWallItem](operations/01-customers.md#deletecustomerwallitem) | Customers | `DELETE /3.0/customers/wall` | Delete wall item(s) from CustomerWall table. |
| [DeleteDestination](operations/17-sync.md#deletedestination) | Sync | `DELETE /3.0/destination` | Deletes a destination. |
| [DeleteEmail](operations/19-unlisted-wsdl-only.md#deleteemail) | Unlisted (WSDL only) | SOAP only | Deletes an email forever. Note: This request can participate in a transaction. Learn more about transactions. |
| [DeleteEmailTemplate](operations/19-unlisted-wsdl-only.md#deleteemailtemplate) | Unlisted (WSDL only) | SOAP only | Deletes an email template. Note: This request can participate in a transaction. Learn more about transactions. |
| [DeleteExtendedDbEntity](operations/16-extended-db.md#deleteextendeddbentity) | Extended DB | `DELETE /3.0/extendeddb` | Delete Extended DB Entity. |
| [DeleteExtendedDbSchema](operations/16-extended-db.md#deleteextendeddbschema) | Extended DB | `DELETE /3.0/extendeddb/schema` | Delete Extended DB schema. |
| [DeleteMailFolder](operations/19-unlisted-wsdl-only.md#deletemailfolder) | Unlisted (WSDL only) | SOAP only | Deletes a mail folder. Note: This request can participate in a transaction. Learn more about transactions. |
| [DeleteOrderDetail](operations/19-unlisted-wsdl-only.md#deleteorderdetail) | Unlisted (WSDL only) | SOAP only | Delete an existing Order Detail for an existing order without recalculating. Can participate in a transaction. Note: This request can… |
| [DeleteProductFromCategory](operations/04-items.md#deleteproductfromcategory) | Items | `DELETE /3.0/webcategory/product` | Deletes a product from a web category. Note: This request can participate in a transaction. Learn more about transactions. |
| [DeleteQualificationOverride](operations/07-reporting.md#deletequalificationoverride) | Reporting | `DELETE /3.0/qualification/override` | Delete a Customer Override |
| [DeleteRelease](operations/15-web-content.md#deleterelease) | Web Content | `DELETE /3.0/resourceset/release` | Deletes a Resource Set release |
| [DeleteResourceSetCulture](operations/15-web-content.md#deleteresourcesetculture) | Web Content | `DELETE /3.0/resourceset/culture` | Removes a cultue from a Resource Set |
| [DeleteResourceSetEnvironment](operations/15-web-content.md#deleteresourcesetenvironment) | Web Content | `DELETE /3.0/resourceset/environment` | Deletes a ResourceSet Environment |
| [DeleteResourceSetGroup](operations/15-web-content.md#deleteresourcesetgroup) | Web Content | `DELETE /3.0/resourceset/group` | Deletes a ResourceSet Group |
| [DeleteResourceSetItem](operations/15-web-content.md#deleteresourcesetitem) | Web Content | `DELETE /3.0/resourceitem` | Deletes a ResourceSet Item |
| [DeleteWebCategory](operations/04-items.md#deletewebcategory) | Items | `DELETE /3.0/webcategory` | Deletes a web category. Note: This request can participate in a transaction. Learn more about transactions. |
| [DeployRelease](operations/15-web-content.md#deployrelease) | Web Content | `POST /3.0/resourceset/release/deploy` | Deploys a Resource Set Release |
| [DequeueCustomerEvents](operations/01-customers.md#dequeuecustomerevents) | Customers | `POST /3.0/customers/events` | This will 'pop' the oldest 100 customer events off the event queue. |
| [DisableDestination](operations/17-sync.md#disabledestination) | Sync | `PUT /3.0/destination/disable` | Disables a destination. |
| [DisableFilterGroup](operations/17-sync.md#disablefiltergroup) | Sync | `PUT /3.0/filtergroup/disable` | Disables a group for filtering. |
| [DisableFiltering](operations/17-sync.md#disablefiltering) | Sync | `PUT /3.0/filtering/disable` | Disables Filtering. |
| [EditBankAccountType](operations/18-other.md#editbankaccounttype) | Other | `PUT /3.0/settings/bankaccounttype` | Edits an existing Bank Account Type. |
| [EmptyMailFolder](operations/19-unlisted-wsdl-only.md#emptymailfolder) | Unlisted (WSDL only) | SOAP only | Deletes all emails from a folder. Note: This request can participate in a transaction. Learn more about transactions. |
| [EnableDestination](operations/17-sync.md#enabledestination) | Sync | `PUT /3.0/destination/enable` | Enables a destination. |
| [EnableFilterGroup](operations/17-sync.md#enablefiltergroup) | Sync | `PUT /3.0/filtergroup/enable` | Enables a group for filtering. |
| [EnableFiltering](operations/17-sync.md#enablefiltering) | Sync | `PUT /3.0/filtering/enable` | Enables filtering. |
| [EnsureMailFolders](operations/19-unlisted-wsdl-only.md#ensuremailfolders) | Unlisted (WSDL only) | SOAP only | Ensures all the basic mail folders exist. Note: This request can participate in a transaction. Learn more about transactions. |
| [FireResponder](operations/08-communications.md#fireresponder) | Communications | `POST /3.0/autoresponder/fire` | Fires an email responder to customer or order email address on file. |
| [FundPaymentCard](operations/19-unlisted-wsdl-only.md#fundpaymentcard) | Unlisted (WSDL only) | `POST /3.0/payout/fund` | Creates a new payout and funds a payment card for one or more bills and updates status |
| [GetAccountDirectDeposit](operations/01-customers.md#getaccountdirectdeposit) | Customers | `GET /3.0/account/directdeposit?customerID=1` | Returns direct deposit info for an existing customer. |
| [GetAdminWhitelist](operations/18-other.md#getadminwhitelist) | Other | `GET /3.0/whitelist/adminAuthorization:` | Get List of Whitelisted IP ranges for Admin |
| [GetAlertSettings](operations/17-sync.md#getalertsettings) | Sync | `GET /3.0/alertsettingsAuthorization:` | Gets alert setings information. |
| [GetApiWhitelist](operations/18-other.md#getapiwhitelist) | Other | `GET /3.0/whitelist/api?ipRangeID=1` | Get List of Whitelisted IP ranges |
| [GetAutoOrders](operations/03-recurring-orders.md#getautoorders) | Recurring Orders | `GET /3.0/autoorder?customerID=1` | Returns any AutoOrders setup and active for a given customer. |
| [GetBankAccountTypes](operations/18-other.md#getbankaccounttypes) | Other | `GET /3.0/settings/bankaccounttypes?bankAccountTyId=1` | Gets the existing Bank Account Types. |
| [GetBillAmountsDue](operations/06-payout.md#getbillamountsdue) | Payout | `GET /3.0/payout/amountsdue?startDate=1` | Gets customer bill amounts due grouped by customer. |
| [GetBillPayments](operations/06-payout.md#getbillpayments) | Payout | `GET /3.0/payout/payments?paymentIDs=1` | Gets customer bill payments and associated bill records . |
| [GetBillPayoutQueue](operations/06-payout.md#getbillpayoutqueue) | Payout | `GET /3.0/payout/payoutqueue?payoutQueueRequestID=1` | Gets customer bill payout queue status and details |
| [GetBills](operations/06-payout.md#getbills) | Payout | `GET /3.0/payout/bills?customers=1` | Gets existing customer bills |
| [GetBinaryPreference](operations/05-tree-movement.md#getbinarypreference) | Tree Movement | `GET /3.0/tree/binary?customerID=1` | Returns the currently configured placement preference for new placements under a customer. |
| [GetCommissionReport](operations/07-reporting.md#getcommissionreport) | Reporting | `GET /3.0/commissions?periodType=1` | Returns a commission report in json format. |
| [GetCompanyLanguages](operations/19-unlisted-wsdl-only.md#getcompanylanguages) | Unlisted (WSDL only) | SOAP only | Gets languages list available to the company. |
| [GetCompanyNews](operations/08-communications.md#getcompanynews) | Communications | `GET /3.0/companynews?departmentType=1` | Gets a list of company news descriptions. |
| [GetCompanyNewsItem](operations/08-communications.md#getcompanynewsitem) | Communications | `GET /3.0/companynews/item?newsID=1` | Gets company news details. |
| [GetCountryRegions](operations/02-orders-payments.md#getcountryregions) | Orders/Payments | `GET /3.0/country/regionsAuthorization:` | Returns countries setup for company as well as the regions for a single country requested. |
| [GetCustomerBalances](operations/02-orders-payments.md#getcustomerbalances) | Orders/Payments | `GET /3.0/customers/balances?customerID=1` | Returns the sum of orders, payments, and adjustments per currency. |
| [GetCustomerBilling](operations/01-customers.md#getcustomerbilling) | Customers | `GET /3.0/account?customerID=1` | Returns billing accounts on file for a customer. Only => s last four digits of a credit card. |
| [GetCustomerExtended](operations/01-customers.md#getcustomerextended) | Customers | `GET /3.0/customers/extended?extendedGroupID=1` | Returns extended properties setup for a customer. |
| [GetCustomerFolders](operations/14-files-folders.md#getcustomerfolders) | Files/Folders | `GET /3.0/folderAuthorization:` | Gets a list of customer folders. |
| [GetCustomerLeads](operations/12-customer-leads.md#getcustomerleads) | Customer Leads | `GET /3.0/customerlead?customerID=1` | Gets a list of customer leads. |
| [GetCustomerLeadSocialNetworks](operations/12-customer-leads.md#getcustomerleadsocialnetworks) | Customer Leads | `GET /3.0/customerlead/socialnetworks?customerID=1` | Returns a list of social network(s) for the customer lead. |
| [GetCustomerNotes](operations/01-customers.md#getcustomernotes) | Customers | `GET /3.0/customers/notes?customerID=1` | Returns the notes field for one or more customers that match the filter critera passed in. |
| [GetCustomers](operations/01-customers.md#getcustomers) | Customers | `GET /3.0/customers?customerID=1` | Returns one or more customers that match the filter critera passed in. |
| [GetCustomerSite](operations/01-customers.md#getcustomersite) | Customers | `GET /3.0/customers/site?webAlias=1` | Returns the public web site info setup for a customer. Pass in CustomerID or WebAlias. If the customer's type has enabled Create Web Info… |
| [GetCustomerSocialNetworks](operations/01-customers.md#getcustomersocialnetworks) | Customers | `GET /3.0/customers/socialnetworks?customerID=1` | Returns a list of social network(s) for the customer. |
| [GetCustomerWall](operations/01-customers.md#getcustomerwall) | Customers | `GET /3.0/customers/wall?customerID=1` | Get wall item(s) from CustomerWall table. |
| [GetCustomReport](operations/07-reporting.md#getcustomreport) | Reporting | `GET /3.0/report?reportID=1` | Returns a custom report in dataset format. |
| [GetDestinations](operations/17-sync.md#getdestinations) | Sync | `GET /3.0/destinationAuthorization:` | Gets destinations. |
| [GetDestinationTest](operations/17-sync.md#getdestinationtest) | Sync | `GET /3.0/destination/gettest?requestId=1` | Gets result for testing a conection. |
| [GetDownline](operations/07-reporting.md#getdownline) | Reporting | `GET /3.0/commissions/downline?treeType=1` | Gets nodes in a downline. |
| [GetEmailAttachment](operations/19-unlisted-wsdl-only.md#getemailattachment) | Unlisted (WSDL only) | SOAP only | Gets an email attachment. Note: This request can participate in a transaction. Learn more about transactions. |
| [GetExtendedDbEntity](operations/16-extended-db.md#getextendeddbentity) | Extended DB | `GET /3.0/extendeddb?schemaName=1` | Get Extended DB Entity. |
| [GetExtendedDbSchema](operations/16-extended-db.md#getextendeddbschema) | Extended DB | `GET /3.0/extendeddb/schema?schemaName=1` | Get Extended DB schema. |
| [GetExtendedDbSettings](operations/17-sync.md#getextendeddbsettings) | Sync | `GET /3.0/extendeddbsettingsAuthorization:` | Gets settings for extended DB. |
| [GetFileContents](operations/14-files-folders.md#getfilecontents) | Files/Folders | `GET /3.0/file/content?customerID=1` | Returns a customer file for the given criteria Note: This request can participate in a transaction. Learn more about transactions. |
| [GetFiles](operations/14-files-folders.md#getfiles) | Files/Folders | `GET /3.0/file?customerID=1` | Returns an array of files Note: This request can participate in a transaction. Learn more about transactions. |
| [GetFilterGroup](operations/17-sync.md#getfiltergroup) | Sync | `GET /3.0/filtergroupAuthorization:` | Gets a filter group. Filtering MUST be enabled first. |
| [GetGuests](operations/09-party-plan.md#getguests) | Party Plan | `GET /3.0/guestAuthorization:` | Gets a list of guests |
| [GetGuestSocialNetworks](operations/09-party-plan.md#getguestsocialnetworks) | Party Plan | `GET /3.0/guest/socialnetwork?guestID=1` | Returns a list of social network(s) for the guest. |
| [GetItemCountryRegion](operations/19-unlisted-wsdl-only.md#getitemcountryregion) | Unlisted (WSDL only) | SOAP only | Returns item, country and region properties along with taxings for an item. |
| [GetItems](operations/04-items.md#getitems) | Items | `GET /3.0/item?currencyCode=usd` | Returns price, volume, and description for one or more item codes. |
| [GetLoginSession](operations/19-unlisted-wsdl-only.md#getloginsession) | Unlisted (WSDL only) | SOAP only | Deprecated. Use AuthenticateCustomer instead. |
| [GetOrderInvoice](operations/02-orders-payments.md#getorderinvoice) | Orders/Payments | `GET /3.0/orders/invoice?orderID=1` | Returns an Rendered Order Invoice |
| [GetOrderInvoiceBatch](operations/02-orders-payments.md#getorderinvoicebatch) | Orders/Payments | `GET /3.0/orders/invoicebatch?reportlayoutID=1` | Returns an rendered invoice of an orders batch |
| [GetOrders](operations/02-orders-payments.md#getorders) | Orders/Payments | `GET /3.0/orders?customerID=1` | Returns one or more orders. You can submit several optional filter fields to control the results. |
| [GetOrderTotals](operations/19-unlisted-wsdl-only.md#getordertotals) | Unlisted (WSDL only) | SOAP only | Returns the totals of accepted orders within a date range |
| [GetParties](operations/09-party-plan.md#getparties) | Party Plan | `GET /3.0/party?partyID=1` | Gets Parties list |
| [GetPartyGuests](operations/09-party-plan.md#getpartyguests) | Party Plan | `GET /3.0/party/guest?partyID=1` | Gets a list of guests belonging to a party |
| [GetPayments](operations/19-unlisted-wsdl-only.md#getpayments) | Unlisted (WSDL only) | `GET /3.0/payment?customerID=1` | Gets payment record(s) for a customer or order. |
| [GetPointAccount](operations/10-points-subscriptions.md#getpointaccount) | Points/Subscriptions | `GET /3.0/point/account?pointAccountID=1` | Get the balance of a point account for a customer. |
| [GetQualificationOverrides](operations/07-reporting.md#getqualificationoverrides) | Reporting | `GET /3.0/qualification/override?customerID=1` | Returns Customer Overrides |
| [GetRandomMessage](operations/08-communications.md#getrandommessage) | Communications | `GET /3.0/randommessage?languageID=1` | Gets a random message (defined in the Exigo Admin). |
| [GetRankQualifications](operations/07-reporting.md#getrankqualifications) | Reporting | `GET /3.0/qualification?customerID=1` | Returns rank qualification report card. |
| [GetRealTimeCommissionDetail](operations/07-reporting.md#getrealtimecommissiondetail) | Reporting | `GET /3.0/commissions/realtime/detail?customerID=1` | Returns realtime commission detail for a customer/bonus. |
| [GetRealTimeCommissions](operations/07-reporting.md#getrealtimecommissions) | Reporting | `GET /3.0/commissions/realtime?customerID=1` | Returns realtime commissions available for open periods. |
| [GetReIndexHistory](operations/17-sync.md#getreindexhistory) | Sync | `GET /3.0/reindexsettings/history?destinationId=1` | Gets ReIndexHistory. |
| [GetReIndexSettings](operations/17-sync.md#getreindexsettings) | Sync | `GET /3.0/reindexsettingsAuthorization:` | Gets Re-Index settings. |
| [GetReleases](operations/15-web-content.md#getreleases) | Web Content | `GET /3.0/resourceset/releaseAuthorization:` | Gets Resource Set releases |
| [GetReport](operations/19-unlisted-wsdl-only.md#getreport) | Unlisted (WSDL only) | SOAP only | Returns a custom report in dataset format. |
| [GetResourceSetCultures](operations/15-web-content.md#getresourcesetcultures) | Web Content | `GET /3.0/resourceset/cultureAuthorization:` | Determines the cultures available in the resource set, environment, and version the client server is subscribed to. |
| [GetResourceSetEnvironments](operations/15-web-content.md#getresourcesetenvironments) | Web Content | `GET /3.0/resourceset/environmentAuthorization:` | Gets ResourceSet Environments |
| [GetResourceSetGroups](operations/15-web-content.md#getresourcesetgroups) | Web Content | `GET /3.0/resourceset/groupAuthorization:` | Gets ResourceSet Groups |
| [GetResourceSetItems](operations/15-web-content.md#getresourcesetitems) | Web Content | `GET /3.0/resourceitemAuthorization:` | Gets ResourceSet Items |
| [GetResourceSets](operations/15-web-content.md#getresourcesets) | Web Content | `GET /3.0/resourcesetAuthorization:` | Get an existing Resource Set |
| [GetResourceSetSubscriptionUpdates](operations/19-unlisted-wsdl-only.md#getresourcesetsubscriptionupdates) | Unlisted (WSDL only) | `GET /3.0/resourceset/subscriptions/updatesAuthorization:` | Gets all resource item updates for a list of resource subscriptions |
| [GetSandbox](operations/19-unlisted-wsdl-only.md#getsandbox) | Unlisted (WSDL only) | SOAP only | Get List of Sandboxes |
| [GetSession](operations/18-other.md#getsession) | Other | `GET /3.0/session?sessionID=1` | Gets a generic session string for a unique sessionID. |
| [GetShipMethods](operations/19-unlisted-wsdl-only.md#getshipmethods) | Unlisted (WSDL only) | SOAP only | This has been deprecated. Use CalculateOrder with ReturnShipMethods=true instead. |
| [GetShoppingCart](operations/19-unlisted-wsdl-only.md#getshoppingcart) | Unlisted (WSDL only) | SOAP only | Gets a existing Shopping Cart Session. |
| [GetSQLReport](operations/07-reporting.md#getsqlreport) | Reporting | `GET /3.0/sqlreport?reportID=1` | Returns a SQL report in dataset format. |
| [GetSubscription](operations/10-points-subscriptions.md#getsubscription) | Points/Subscriptions | `GET /3.0/subscription?subscriptionID=1` | Get the subscription account for a customer. |
| [GetSubscriptions](operations/10-points-subscriptions.md#getsubscriptions) | Points/Subscriptions | `GET /3.0/subscriptions?customerID=1` | Get all subscriptions for a customer. |
| [GetTableSettings](operations/17-sync.md#gettablesettings) | Sync | `GET /3.0/tablesettingsAuthorization:` | Gets a table's settings. |
| [GetUpline](operations/07-reporting.md#getupline) | Reporting | `GET /3.0/commissions/upline?treeType=1` | Gets nodes in an upline. |
| [GetUserPermissions](operations/13-users.md#getuserpermissions) | Users | `GET /3.0/user/permissions?loginName=1` | Returns permissions associated with the corporate user account. |
| [GetVolumes](operations/07-reporting.md#getvolumes) | Reporting | `GET /3.0/commissions/volumes?periodType=1` | Returns volume records for a current period in a periodtype. |
| [GetWarehouses](operations/04-items.md#getwarehouses) | Items | `GET /3.0/warehouse` | Gets a list of warehouses setup in the system. |
| [LoginCustomer](operations/19-unlisted-wsdl-only.md#logincustomer) | Unlisted (WSDL only) | SOAP only | Deprecated. Use AuthenticateCustomer instead. |
| [MergeCustomer](operations/19-unlisted-wsdl-only.md#mergecustomer) | Unlisted (WSDL only) | SOAP only | Merges Order, Payments and AutoOrder data from two Customers |
| [MoveCustomerFile](operations/14-files-folders.md#movecustomerfile) | Files/Folders | `POST /3.0/file/move` | Moves a customer folder to a provided file. |
| [MoveEmail](operations/19-unlisted-wsdl-only.md#moveemail) | Unlisted (WSDL only) | SOAP only | Moves an email to a different folder. Note: This request can participate in a transaction. Learn more about transactions. |
| [OptInEmail](operations/08-communications.md#optinemail) | Communications | `POST /3.0/email/optin` | Setup opt in settings for Email by Email address. |
| [OptInPushNotification](operations/08-communications.md#optinpushnotification) | Communications | `POST /3.0/push/optin` | Setup opt in settings for Push Notifications to mobile devices. |
| [OptInSms](operations/08-communications.md#optinsms) | Communications | `POST /3.0/sms/optin` | Setup opt in settings for Sms messaging by phone number. |
| [OptOutEmail](operations/08-communications.md#optoutemail) | Communications | `POST /3.0/email/optout` | Opts out all customers and customer contacts with specified email from receiving broadcast emails. |
| [OptOutPushNotification](operations/08-communications.md#optoutpushnotification) | Communications | `POST /3.0/push/optout` | Setup opt out settings for Push Notifications to mobile devices. |
| [OptOutSms](operations/08-communications.md#optoutsms) | Communications | `POST /3.0/sms/optout` | Opts out all customers and customer contacts with specified phone number from receiving broadcast SMS messages. |
| [Ping](operations/19-unlisted-wsdl-only.md#ping) | Unlisted (WSDL only) | `POST /3.0/orders/calculate` | Ping to create a speed baseline |
| [PlaceBinaryNode](operations/05-tree-movement.md#placebinarynode) | Tree Movement | `POST /3.0/tree/binary` | Inserts/Moves a customer within the Binary Tree. |
| [PlaceEnrollerNode](operations/05-tree-movement.md#placeenrollernode) | Tree Movement | `POST /3.0/tree/enroller` | Inserts/Moves a customer within the Enroller Tree. |
| [PlaceMatrixNode](operations/05-tree-movement.md#placematrixnode) | Tree Movement | `POST /3.0/tree/matrix` | Inserts/Moves a customer within the Matrix Tree. |
| [PlaceStackNode](operations/19-unlisted-wsdl-only.md#placestacknode) | Unlisted (WSDL only) | SOAP only | Inserts/Moves a customer within the Stack Tree. |
| [PlaceUniLevelNode](operations/05-tree-movement.md#placeunilevelnode) | Tree Movement | `POST /3.0/tree/unilevel` | Inserts/Moves a customer within the UniLevel (Sponsor) Tree. |
| [ProcessTransaction](operations/02-orders-payments.md#processtransaction) | Orders/Payments | SOAP only | Commits multiple requests in one step. All business rules are checked before commit and it is a commit-all or fail-all. In your… |
| [QueueBillPayout](operations/06-payout.md#queuebillpayout) | Payout | `POST /3.0/payout/queuepayout` | Queues a new customer bill payout to be process by a third party. |
| [RefreshSandbox](operations/19-unlisted-wsdl-only.md#refreshsandbox) | Unlisted (WSDL only) | SOAP only | Refresh a Sandbox |
| [RefundPriorCreditCardCharge](operations/02-orders-payments.md#refundpriorcreditcardcharge) | Orders/Payments | `POST /3.0/payment/refund/cc` | Refunds a prior charge. To be used with an order. |
| [RefundPriorDebitCharge](operations/02-orders-payments.md#refundpriordebitcharge) | Orders/Payments | `POST /3.0/payment/refund/debit` | Refunds a prior charge. To be used with an order. |
| [RefundPriorWalletCharge](operations/02-orders-payments.md#refundpriorwalletcharge) | Orders/Payments | `POST /3.0/payment/refund/wallet` | Refunds a prior wallet charge. To be used with an order. |
| [RemoveAdminWhitelist](operations/18-other.md#removeadminwhitelist) | Other | `DELETE /3.0/whitelist/admin` | Remove an existing Whitelisted IP range from Admin |
| [RemoveApiWhitelist](operations/18-other.md#removeapiwhitelist) | Other | `DELETE /3.0/whitelist/api` | Remove an existing Whitelisted IP range |
| [RemovePartyGuests](operations/09-party-plan.md#removepartyguests) | Party Plan | `DELETE /3.0/party/guest` | Removes one or more guests from a party. |
| [ResourceSetCheckIn](operations/15-web-content.md#resourcesetcheckin) | Web Content | `POST /3.0/resourceset/checkin` | Keeps the client's version of the resource set up to date to the environment it is subscribed to. |
| [RetireResourceSet](operations/15-web-content.md#retireresourceset) | Web Content | `DELETE /3.0/resourceset` | Retire an existing ResourceSet |
| [RevertToRecentRelease](operations/15-web-content.md#reverttorecentrelease) | Web Content | `POST /3.0/resourceset/release/revert` | Reverts to most recent Resource Set Release |
| [SendAuthorizationMFACode](operations/08-communications.md#sendauthorizationmfacode) | Communications | `POST /3.0/sms/authorizationmfa` | Sends an Authorization MFA Code SMS message. |
| [SendEmail](operations/18-other.md#sendemail) | Other | `POST /3.0/email` | Sends a specified Email using SendGrid |
| [SendSms](operations/08-communications.md#sendsms) | Communications | `POST /3.0/sms` | Sends an SMS message. |
| [SetAccountChecking](operations/01-customers.md#setaccountchecking) | Customers | `PUT /3.0/account/checking` | Setup bank account on file an existing customer, or new customer in a transaction. You can also empty the account settings by simply… |
| [SetAccountCreditCard](operations/19-unlisted-wsdl-only.md#setaccountcreditcard) | Unlisted (WSDL only) | SOAP only | Setup primary or secondary credit card on file for an existing customer, or new customer in a transaction. Note: This request can… |
| [SetAccountCreditCardToken](operations/01-customers.md#setaccountcreditcardtoken) | Customers | `PUT /3.0/account/cctoken` | Setup primary or secondary credit card token on file for an existing customer, or new customer in a transaction. Note: This request can… |
| [SetAccountDirectDeposit](operations/01-customers.md#setaccountdirectdeposit) | Customers | `PUT /3.0/account/directdeposit` | Setup direct deposit info for an existing customer, or new customer in a transaction. You can also empty the account settings by simply… |
| [SetAccountWallet](operations/01-customers.md#setaccountwallet) | Customers | `PUT /3.0/account/wallet` | Setup primary or secondary wallet account on file for an existing customer, or new customer in a transaction. Note: This request can… |
| [SetBinaryPreference](operations/05-tree-movement.md#setbinarypreference) | Tree Movement | `PUT /3.0/tree/binary` | Sets the placement preference for new placements under a customer. |
| [SetCustomerLeadSocialNetworks](operations/12-customer-leads.md#setcustomerleadsocialnetworks) | Customer Leads | `PUT /3.0/customerlead/socialnetworks` | Deletes all existing social network(s) for the customer lead, then inserts the provided list of social network(s) for the customer lead.… |
| [SetCustomerSite](operations/01-customers.md#setcustomersite) | Customers | `PUT /3.0/customers/site` | Setup public web site info for an existing customer, or new customer in a transaction. |
| [SetCustomerSiteImage](operations/01-customers.md#setcustomersiteimage) | Customers | `PUT /3.0/customers/site/image` | Setup public web site image for an existing customer. |
| [SetCustomerSocialNetworks](operations/01-customers.md#setcustomersocialnetworks) | Customers | `PUT /3.0/customers/socialnetworks` | Deletes all existing social network(s) for the customer, then inserts the provided list of social network(s) for the customer. Note: This… |
| [SetGuestSocialNetworks](operations/09-party-plan.md#setguestsocialnetworks) | Party Plan | `PUT /3.0/guest/socialnetwork` | Deletes all existing social network(s) for the guest, then inserts the provided list of social network(s) for the guest. |
| [SetImageFile](operations/19-unlisted-wsdl-only.md#setimagefile) | Unlisted (WSDL only) | SOAP only | Set Images |
| [SetItemCountryRegion](operations/04-items.md#setitemcountryregion) | Items | `PUT /3.0/item/countryregion` | Sets country/region info for an item) Note: This request can participate in a transaction. Learn more about transactions. |
| [SetItemImage](operations/04-items.md#setitemimage) | Items | `PUT /3.0/item/image` | Set Images for an Item |
| [SetItemKitMembers](operations/04-items.md#setitemkitmembers) | Items | `PUT /3.0/item/kit/members` | Sets the children for a static kit Note: This request can participate in a transaction. Learn more about transactions. |
| [SetItemPointAccount](operations/04-items.md#setitempointaccount) | Items | `PUT /3.0/item/pointaccount` | Set Item Point Account Note: This request can participate in a transaction. Learn more about transactions. |
| [SetItemPrice](operations/04-items.md#setitemprice) | Items | `PUT /3.0/item/price` | Sets pricing info for an item) Note: This request can participate in a transaction. Learn more about transactions. |
| [SetItemSubscription](operations/04-items.md#setitemsubscription) | Items | `PUT /3.0/item/subscription` | Set Item Subscriptions Note: This request can participate in a transaction. Learn more about transactions. |
| [SetItemWarehouse](operations/04-items.md#setitemwarehouse) | Items | `PUT /3.0/item/warehouse` | Sets warehouse info for an item) Note: This request can participate in a transaction. Learn more about transactions. |
| [SetQualificationOverride](operations/07-reporting.md#setqualificationoverride) | Reporting | `PUT /3.0/qualification/override` | Create or Edit a Customer Override |
| [SetSession](operations/18-other.md#setsession) | Other | `PUT /3.0/session` | Sets a generic session string for a unique sessionID. |
| [StartSandbox](operations/19-unlisted-wsdl-only.md#startsandbox) | Unlisted (WSDL only) | SOAP only | Start a Sandbox |
| [StopSandbox](operations/19-unlisted-wsdl-only.md#stopsandbox) | Unlisted (WSDL only) | SOAP only | Stop a Sandbox |
| [SubmitDestinationTest](operations/17-sync.md#submitdestinationtest) | Sync | `POST /3.0/destination/submittest` | Begins process for testing a conection. |
| [TerminateCustomer](operations/01-customers.md#terminatecustomer) | Customers | `POST /3.0/customers/terminate` | Terminates a Customer |
| [UpdateAlertSettings](operations/17-sync.md#updatealertsettings) | Sync | `PATCH /3.0/alertsettings` | Updates te alert settings. |
| [UpdateAutoOrder](operations/03-recurring-orders.md#updateautoorder) | Recurring Orders | `PUT /3.0/autoorder` | Update a Recurring Order template in or out of a transaction. Client provides schedule, item codes, quantity, and shipping info. Server… |
| [UpdateAutoOrderDetail](operations/03-recurring-orders.md#updateautoorderdetail) | Recurring Orders | `PUT /3.0/autoorder/detail` | Update a Recurring Order template detail in or out of a transaction. Client provides quantity, pricing , volume and extended detail info.… |
| [UpdateBill](operations/06-payout.md#updatebill) | Payout | `PATCH /3.0/bill` | Updates one or more fields on an existing customer bill. |
| [UpdateCalendarItem](operations/11-calendar.md#updatecalendaritem) | Calendar | `PATCH /3.0/calendar/item` | Updates calendar item information. Note: This request can participate in a transaction. Learn more about transactions. |
| [UpdateCustomer](operations/01-customers.md#updatecustomer) | Customers | `PATCH /3.0/customers` | Updates one or more fields on an existing customer. Can participate in a transaction. |
| [UpdateCustomerContact](operations/19-unlisted-wsdl-only.md#updatecustomercontact) | Unlisted (WSDL only) | SOAP only | Updates customer contact information. Note: This request can participate in a transaction. Learn more about transactions. |
| [UpdateCustomerExtended](operations/01-customers.md#updatecustomerextended) | Customers | `PATCH /3.0/customers/extended` | Updates one customer extended record. Note: This request can participate in a transaction. Learn more about transactions. |
| [UpdateCustomerLead](operations/12-customer-leads.md#updatecustomerlead) | Customer Leads | `PATCH /3.0/customerlead` | Updates a customer leads. Note: This request can participate in a transaction. Learn more about transactions. |
| [UpdateDestination](operations/17-sync.md#updatedestination) | Sync | `PATCH /3.0/destination` | Updates a destination. |
| [UpdateEmailStatus](operations/19-unlisted-wsdl-only.md#updateemailstatus) | Unlisted (WSDL only) | SOAP only | Updates email's status. Note: This request can participate in a transaction. Learn more about transactions. |
| [UpdateEmailTemplate](operations/19-unlisted-wsdl-only.md#updateemailtemplate) | Unlisted (WSDL only) | SOAP only | Updates an email template. Note: This request can participate in a transaction. Learn more about transactions. |
| [UpdateExtendedDbEntity](operations/16-extended-db.md#updateextendeddbentity) | Extended DB | `PATCH /3.0/extendeddb` | Update Extended DB Entity. |
| [UpdateExtendedDbSettings](operations/17-sync.md#updateextendeddbsettings) | Sync | `PATCH /3.0/extendeddbsettings` | Updates settings for extended DB. |
| [UpdateGuest](operations/09-party-plan.md#updateguest) | Party Plan | `PATCH /3.0/guest` | Updates one or more fields on an existing guest. |
| [UpdateItem](operations/04-items.md#updateitem) | Items | `PUT /3.0/item` | Updates an Item (and optional warehouse/price info) Note: This request can participate in a transaction. Learn more about transactions. |
| [UpdateMailFolder](operations/19-unlisted-wsdl-only.md#updatemailfolder) | Unlisted (WSDL only) | SOAP only | Updates a mail folder. Note: This request can participate in a transaction. Learn more about transactions. |
| [UpdateOrder](operations/02-orders-payments.md#updateorder) | Orders/Payments | `PATCH /3.0/orders` | Updates one or more fields on an existing order. Can participate in a transaction. Note: This request can participate in a transaction.… |
| [UpdateOrderDetail](operations/02-orders-payments.md#updateorderdetail) | Orders/Payments | `PUT /3.0/orders/detail` | Update an existing Order Detail for an existing order without recalculating. Can participate in a transaction. Note: This request can… |
| [UpdateParty](operations/09-party-plan.md#updateparty) | Party Plan | `PUT /3.0/party` | Updates selected Party instance |
| [UpdateReIndexSettings](operations/17-sync.md#updatereindexsettings) | Sync | `PATCH /3.0/reindexsettings` | Updates Re-Index settings. |
| [UpdateResourceSet](operations/15-web-content.md#updateresourceset) | Web Content | `PATCH /3.0/resourceset` | Update an existing ResourceSet |
| [UpdateResourceSetBannerItem](operations/15-web-content.md#updateresourcesetbanneritem) | Web Content | `PATCH /3.0/resourceitem/banner` | Updates a ResourceSet Banner Item |
| [UpdateResourceSetBooleanItem](operations/15-web-content.md#updateresourcesetbooleanitem) | Web Content | `PATCH /3.0/resourceitem/bool` | Updates a ResourceSet Boolean Item |
| [UpdateResourceSetCarouselItem](operations/15-web-content.md#updateresourcesetcarouselitem) | Web Content | `PATCH /3.0/resourceitem/carousel` | Updates a ResourceSet Carousel Item |
| [UpdateResourceSetDataSetItem](operations/15-web-content.md#updateresourcesetdatasetitem) | Web Content | `PATCH /3.0/resourceitem/dataset` | Updates a ResourceSet DataSet Item |
| [UpdateResourceSetDateItem](operations/15-web-content.md#updateresourcesetdateitem) | Web Content | `PATCH /3.0/resourceitem/date` | Updates a ResourceSet Date Item |
| [UpdateResourceSetDecimalItem](operations/15-web-content.md#updateresourcesetdecimalitem) | Web Content | `PATCH /3.0/resourceitem/decimal` | Updates a ResourceSet Decimal Item |
| [UpdateResourceSetDropDownItem](operations/15-web-content.md#updateresourcesetdropdownitem) | Web Content | `PATCH /3.0/resourceitem/dropdown` | Updates a ResourceSet DropDown Item |
| [UpdateResourceSetEnvironment](operations/15-web-content.md#updateresourcesetenvironment) | Web Content | `PATCH /3.0/resourceset/environment` | Updates a ResourceSet Environment |
| [UpdateResourceSetGroup](operations/15-web-content.md#updateresourcesetgroup) | Web Content | `PATCH /3.0/resourceset/group` | Updates a ResourceSet Group |
| [UpdateResourceSetImageItem](operations/15-web-content.md#updateresourcesetimageitem) | Web Content | `PATCH /3.0/resourceitem/image` | Updates a ResourceSet Image Item |
| [UpdateResourceSetIntItem](operations/15-web-content.md#updateresourcesetintitem) | Web Content | `PATCH /3.0/resourceitem/int` | Updates a ResourceSet Int Item |
| [UpdateResourceSetTextItem](operations/15-web-content.md#updateresourcesettextitem) | Web Content | `PATCH /3.0/resourceitem/text` | Updates a ResourceSet Text Item |
| [UpdateResourceSetWidgetItem](operations/15-web-content.md#updateresourcesetwidgetitem) | Web Content | `PATCH /3.0/resourceitem/widget` | Updates a ResourceSet Widget Item |
| [UpdateTableFilterSettings](operations/17-sync.md#updatetablefiltersettings) | Sync | `PATCH /3.0/filtergroup/update` | Updates Table Filter Settings. |
| [UpdateTableSettings](operations/17-sync.md#updatetablesettings) | Sync | `PATCH /3.0/tablesettings` | Updates a table's settings. |
| [UpdateWebCategory](operations/04-items.md#updatewebcategory) | Items | `PUT /3.0/webcategory` | Updates web category information. Note: This request can participate in a transaction. Learn more about transactions. |
| [Validate](operations/18-other.md#validate) | Other | SOAP only | Validates Business Rules. |
| [ValidateCreditCardToken](operations/02-orders-payments.md#validatecreditcardtoken) | Orders/Payments | `POST /3.0/payment/validate/token` | Validates a credit card token. |
| [ValidateWalletAccount](operations/02-orders-payments.md#validatewalletaccount) | Orders/Payments | `POST /3.0/payment/validate/wallet` | Validates a Wallet Account. |
| [VerifyAddress](operations/18-other.md#verifyaddress) | Other | `POST /3.0/address/verify` | Verifies and cleans up an address. |
| [VoidPayments](operations/06-payout.md#voidpayments) | Payout | `POST /3.0/payment/void` | Voids payments |

## Machine-readable data

`exigo-api.json` holds the same crawl as structured data (operations with I/O tables, enum values, REST/SOAP examples and samples; WSDL types and enums) for code generation or tooling.

## Refreshing this crawl

The crawler and parser live in `docs/exigo-api/tools/`. Run `python3 tools/crawl.py && python3 tools/parse.py && python3 tools/gen.py`. Note: `doc/EnumHelp.aspx` returns HTTP 500 unless a `Referer` header pointing at the method page is sent.

