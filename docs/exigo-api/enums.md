# Exigo API — Enums

Back to [index](README.md). Source: WSDL `simpleType` enumerations (authoritative names) plus the per-property value lists from the docs (`EnumHelp`).

## WSDL enumerations

### AccountCreditCardType

`Primary`, `Secondary`

### AccountWalletType

`Primary`, `Secondary`, `Third`, `Fourth`, `Fifth`

### AutoOrderPaymentType

`PrimaryCreditCard`, `SecondaryCreditCard`, `CheckingAccount`, `WillSendPayment`, `BankDraft`, `PrimaryWalletAccount`, `SecondaryWalletAccount`, `ThirdWalletAccount`, `FourthWalletAccount`, `FifthWalletAccount`

### AutoOrderProcessType

`AlwaysProcess`, `Conditional`

### AutoOrderStatusType

`Active`, `Inactive`, `Deleted`

### BankAccountType

`CheckingPersonal`, `CheckingBusiness`, `SavingsPersonal`, `SavingsBusiness`

### BannerClickEvent

`OpenInNewTab`, `OpenInCurrentWindow`, `None`

### BannerType

`TextOnImage`, `ImageTop`, `InvalidType`

### BinaryPlacementType

`StrategicPlacement`, `BuildLeft`, `BuildRight`, `BalancedBuild`, `EvenFill`, `WeakLeg`, `EnrollerPreference`, `LeftEvenFill`, `RightEvenFill`, `LesserVolumeLeg`, `LesserVolumeLegOutside`, `StrongLegOutside`, `LesserVolumeLegEvenFill`, `GreaterVolumeLegEvenFill`, `InsertRightMoveDownline`, `InsertLeftMoveDownline`, `BuildTeamLeg`

### CalendarItemPriorityType

`None`, `High`, `Medium`, `Low`

### CalendarItemStatusType

`Open`, `Closed`

### CalendarItemType

`Appointment`, `ToDo`, `Anniversary`

### CarouselType

`Bootstrap3`, `Bootstrap4`, `Bootstrap5`

### ContactPhoneType

`Office`, `Mobile`, `Home`

### CustomerSiteImageType

`Primary`, `Secondary`

### DepositAccountType

`Checking`, `Saving`, `Business`, `Personal`

### FilterType

`MaxDays`, `InList`

### FrequencyType

`Weekly`, `BiWeekly`, `Monthly`, `BiMonthly`, `Quarterly`, `SemiYearly`, `Yearly`, `EveryFourWeeks`, `EverySixWeeks`, `EveryEightWeeks`, `EveryTwelveWeeks`, `SpecificDays`, `Custom`

### Gender

`Unknown`, `Male`, `Female`

### InventoryStatusType

`Available`, `OnBackOrder`, `OutOfStock`, `Discontinued`

### InvoiceRenderFormat

`HTML`

### MailForderType

`SubFolder`, `Inbox`, `SentItems`, `Drafts`, `DeletedItems`, `JunkMail`, `FaxInbox`, `SentFaxes`, `PersonalFolders`

### MailPriority

`High`, `Low`, `Normal`

### MailStatusType

`New`, `Read`, `Forwarded`, `Replied`

### NewsCompanySettings

`AccessAllUsers`, `AccessByDepartment`, `AccessNotAvailable`

### NewsWebSettings

`AccessAvailable`, `AccessNotAvailable`

### NumericCompareType

`Equals`, `GreaterThan`, `LessThan`

### OrderShipCarrier

`FedEx`, `UPS`, `Purolator`, `CanadaPostRegular`, `CanadaPostExpress`, `DHL`, `USPS`, `Estafeta`, `RoyalMail`, `GLSHungary`, `PostenNorway`, `LandMarkGlobal`, `GDEX`

### OrderStatusType

`Incomplete`, `Pending`, `CCDeclined`, `ACHDeclined`, `Canceled`, `CCPending`, `ACHPending`, `Accepted`, `Printed`, `Shipped`, `PendingInventory`

### OrderType

`Default`, `CustomerService`, `ShoppingCart`, `WebWizard`, `AutoOrder`, `Import`, `BackOrder`, `ReplacementOrder`, `ReturnOrder`, `WebAutoOrder`, `TicketSystem`, `APIOrder`, `BackOrderParent`, `ChildOrder`, `Other1`, `Other2`, `Other3`, `Other4`, `Other5`, `Other6`, `Other7`, `Other8`, `Other9`, `Other10`

### PayableType

`Check`, `WireTransfer`, `PaymentCard`, `DirectDeposit`, `OnHold`, `BankWire`, `DebitCardHold`, `Other100`

### PaymentType

`Cash`, `CreditCard`, `Check`, `CreditVoucher`, `Net30`, `Net60`, `ACHDebit`, `UseCredit`, `BankDraft`, `BankWire`, `PointRedemtion`, `COD`, `MoneyOrder`, `BankDeposit`, `Other1`, `Other2`, `Other3`, `Wallet`, `Other4`, `Other5`, `Other6`, `Other7`, `Other8`, `Other9`, `Other10`, `Other11`, `Other12`, `Other13`, `Other14`, `Other15`

### PayoutQueueStatusType

`Processing`, `Complete`, `CompleteWithErrors`

### PointTransactionType

`Redemption`, `Adjustment`

### PropertyType

`Integer`, `DateTime2`, `DateTime`, `Decimal`, `Boolean`, `String`, `StringMax`, `Binary`, `Guid`

### ResourceType

`Text`, `Int`, `Decimal`, `Date`, `Boolean`, `DropDown`, `Image`, `Widget`, `Banner`, `DataSet`, `Carousel`

### ResultStatus

`Success`, `Failure`

### SandboxType

`Sandbox`, `Commission`, `Premium`

### SubscriptionStatus

`NotFound`, `Active`, `Expired`, `Cancelled`

### TableGroupID

`Misc`, `AutoOrder`, `Core`, `Commission`, `Customer`, `CustomersExtended`, `Item`, `Log`, `Messaging`, `Order`, `Payout`, `Tree`, `User`, `Image`

### TaxIDType

`SSN`, `EIN`, `OtherType3`, `OtherType4`, `OtherType5`, `OtherType6`, `OtherType7`, `OtherType8`, `OtherType9`, `OtherType10`, `OtherType11`, `OtherType12`, `OtherType13`, `OtherType14`, `OtherType15`, `OtherType16`, `OtherType17`, `OtherType18`, `OtherType19`, `OtherType20`

### TokenAccount

`Primary`, `Secondary`

### TreeType

`Enroller`, `UniLevel`, `Binary`, `Matrix`, `Stack`

## Property → enum values (as listed on each method page)

| Operation | Object | Property | Type | Values |
|---|---|---|---|---|
| [CreateCustomer](operations/01-customers.md#createcustomer) | `CreateCustomerRequest` | `PayableType` | `PayableType` | `Check`, `WireTransfer`, `PaymentCard`, `DirectDeposit`, `OnHold`, `BankWire`, `DebitCardHold`, `Other100` |
| [CreateCustomer](operations/01-customers.md#createcustomer) | `CreateCustomerRequest` | `Gender` | `Gender` | `Unknown`, `Male`, `Female` |
| [UpdateCustomer](operations/01-customers.md#updatecustomer) | `UpdateCustomerRequest` | `PayableType` | `PayableType` | `Check`, `WireTransfer`, `PaymentCard`, `DirectDeposit`, `OnHold`, `BankWire`, `DebitCardHold`, `Other100` |
| [UpdateCustomer](operations/01-customers.md#updatecustomer) | `UpdateCustomerRequest` | `TaxIDType` | `TaxIDType` | `SSN`, `EIN`, `OtherType3`, `OtherType4`, `OtherType5`, `OtherType6`, `OtherType7`, `OtherType8`, `OtherType9`, `OtherType10`, `OtherType11`, `OtherType12`, `OtherType13`, `OtherType14`, `OtherType15`, `OtherType16`, `OtherType17`, `OtherType18`, `OtherType19`, `OtherType20` |
| [UpdateCustomer](operations/01-customers.md#updatecustomer) | `UpdateCustomerRequest` | `Gender` | `Gender` | `Unknown`, `Male`, `Female` |
| [SetAccountCreditCardToken](operations/01-customers.md#setaccountcreditcardtoken) | `SetAccountCreditCardTokenRequest` | `CreditCardAccountType` | `AccountCreditCardType` | `Primary`, `Secondary` |
| [SetAccountChecking](operations/01-customers.md#setaccountchecking) | `SetAccountCheckingRequest` | `BankAccountType` | `BankAccountType` | `CheckingPersonal`, `CheckingBusiness`, `SavingsPersonal`, `SavingsBusiness` |
| [SetAccountDirectDeposit](operations/01-customers.md#setaccountdirectdeposit) | `SetAccountDirectDepositRequest` | `DepositAccountType` | `DepositAccountType` | `Checking`, `Saving`, `Business`, `Personal` |
| [SetAccountDirectDeposit](operations/01-customers.md#setaccountdirectdeposit) | `SetAccountDirectDepositRequest` | `BankAccountType` | `BankAccountType` | `CheckingPersonal`, `CheckingBusiness`, `SavingsPersonal`, `SavingsBusiness` |
| [SetAccountWallet](operations/01-customers.md#setaccountwallet) | `SetAccountWalletRequest` | `WalletAccountType` | `AccountWalletType` | `Primary`, `Secondary`, `Third`, `Fourth`, `Fifth` |
| [SetCustomerSiteImage](operations/01-customers.md#setcustomersiteimage) | `SetCustomerSiteImageRequest` | `CustomerSiteImageType` | `CustomerSiteImageType` | `Primary`, `Secondary` |
| [GetCustomers](operations/01-customers.md#getcustomers) | `CustomerResponse` | `PayableType` | `PayableType` | `Check`, `WireTransfer`, `PaymentCard`, `DirectDeposit`, `OnHold`, `BankWire`, `DebitCardHold`, `Other100` |
| [GetCustomers](operations/01-customers.md#getcustomers) | `CustomerResponse` | `Gender` | `Gender` | `Unknown`, `Male`, `Female` |
| [GetCustomerBilling](operations/01-customers.md#getcustomerbilling) | `BankAccountResponse` | `BankAccountType` | `BankAccountType` | `CheckingPersonal`, `CheckingBusiness`, `SavingsPersonal`, `SavingsBusiness` |
| [GetAccountDirectDeposit](operations/01-customers.md#getaccountdirectdeposit) | `GetAccountDirectDepositResponse` | `DepositAccountType` | `DepositAccountType` | `Checking`, `Saving`, `Business`, `Personal` |
| [GetAccountDirectDeposit](operations/01-customers.md#getaccountdirectdeposit) | `GetAccountDirectDepositResponse` | `BankAccountType` | `BankAccountType` | `CheckingPersonal`, `CheckingBusiness`, `SavingsPersonal`, `SavingsBusiness` |
| [CalculateOrder](operations/02-orders-payments.md#calculateorder) | `CalculateOrderRequest` | `OrderType` | `OrderType` | `Default`, `CustomerService`, `ShoppingCart`, `WebWizard`, `AutoOrder`, `Import`, `BackOrder`, `ReplacementOrder`, `ReturnOrder`, `WebAutoOrder`, `TicketSystem`, `APIOrder`, `BackOrderParent`, `ChildOrder`, `Other1`, `Other2`, `Other3`, `Other4`, `Other5`, `Other6`, `Other7`, `Other8`, `Other9`, `Other10` |
| [CreateOrder](operations/02-orders-payments.md#createorder) | `CreateOrderRequest` | `OrderStatus` | `OrderStatusType` | `Incomplete`, `Pending`, `CCDeclined`, `ACHDeclined`, `Canceled`, `CCPending`, `ACHPending`, `Accepted`, `Printed`, `Shipped`, `PendingInventory` |
| [CreateOrder](operations/02-orders-payments.md#createorder) | `CreateOrderRequest` | `OrderType` | `OrderType` | `Default`, `CustomerService`, `ShoppingCart`, `WebWizard`, `AutoOrder`, `Import`, `BackOrder`, `ReplacementOrder`, `ReturnOrder`, `WebAutoOrder`, `TicketSystem`, `APIOrder`, `BackOrderParent`, `ChildOrder`, `Other1`, `Other2`, `Other3`, `Other4`, `Other5`, `Other6`, `Other7`, `Other8`, `Other9`, `Other10` |
| [CreateOrderImport](operations/02-orders-payments.md#createorderimport) | `CreateOrderImportRequest` | `OrderStatus` | `OrderStatusType` | `Incomplete`, `Pending`, `CCDeclined`, `ACHDeclined`, `Canceled`, `CCPending`, `ACHPending`, `Accepted`, `Printed`, `Shipped`, `PendingInventory` |
| [CreateOrderImport](operations/02-orders-payments.md#createorderimport) | `CreateOrderImportRequest` | `OrderType` | `OrderType` | `Default`, `CustomerService`, `ShoppingCart`, `WebWizard`, `AutoOrder`, `Import`, `BackOrder`, `ReplacementOrder`, `ReturnOrder`, `WebAutoOrder`, `TicketSystem`, `APIOrder`, `BackOrderParent`, `ChildOrder`, `Other1`, `Other2`, `Other3`, `Other4`, `Other5`, `Other6`, `Other7`, `Other8`, `Other9`, `Other10` |
| [UpdateOrder](operations/02-orders-payments.md#updateorder) | `UpdateOrderRequest` | `WebCarrierID` | `OrderShipCarrier` | `FedEx`, `UPS`, `Purolator`, `CanadaPostRegular`, `CanadaPostExpress`, `DHL`, `USPS`, `Estafeta`, `RoyalMail`, `GLSHungary`, `PostenNorway`, `LandMarkGlobal`, `GDEX` |
| [UpdateOrder](operations/02-orders-payments.md#updateorder) | `UpdateOrderRequest` | `WebCarrierID2` | `OrderShipCarrier` | `FedEx`, `UPS`, `Purolator`, `CanadaPostRegular`, `CanadaPostExpress`, `DHL`, `USPS`, `Estafeta`, `RoyalMail`, `GLSHungary`, `PostenNorway`, `LandMarkGlobal`, `GDEX` |
| [UpdateOrder](operations/02-orders-payments.md#updateorder) | `UpdateOrderRequest` | `WebCarrierID3` | `OrderShipCarrier` | `FedEx`, `UPS`, `Purolator`, `CanadaPostRegular`, `CanadaPostExpress`, `DHL`, `USPS`, `Estafeta`, `RoyalMail`, `GLSHungary`, `PostenNorway`, `LandMarkGlobal`, `GDEX` |
| [UpdateOrder](operations/02-orders-payments.md#updateorder) | `UpdateOrderRequest` | `WebCarrierID4` | `OrderShipCarrier` | `FedEx`, `UPS`, `Purolator`, `CanadaPostRegular`, `CanadaPostExpress`, `DHL`, `USPS`, `Estafeta`, `RoyalMail`, `GLSHungary`, `PostenNorway`, `LandMarkGlobal`, `GDEX` |
| [UpdateOrder](operations/02-orders-payments.md#updateorder) | `UpdateOrderRequest` | `WebCarrierID5` | `OrderShipCarrier` | `FedEx`, `UPS`, `Purolator`, `CanadaPostRegular`, `CanadaPostExpress`, `DHL`, `USPS`, `Estafeta`, `RoyalMail`, `GLSHungary`, `PostenNorway`, `LandMarkGlobal`, `GDEX` |
| [ChangeOrderStatus](operations/02-orders-payments.md#changeorderstatus) | `ChangeOrderStatusRequest` | `OrderStatus` | `OrderStatusType` | `Incomplete`, `Pending`, `CCDeclined`, `ACHDeclined`, `Canceled`, `CCPending`, `ACHPending`, `Accepted`, `Printed`, `Shipped`, `PendingInventory` |
| [ChangeOrderStatusBatch](operations/02-orders-payments.md#changeorderstatusbatch) | `ChangeOrderStatusBatchRequest` | `OrderStatus` | `OrderStatusType` | `Incomplete`, `Pending`, `CCDeclined`, `ACHDeclined`, `Canceled`, `CCPending`, `ACHPending`, `Accepted`, `Printed`, `Shipped`, `PendingInventory` |
| [ValidateCreditCardToken](operations/02-orders-payments.md#validatecreditcardtoken) | `ValidateCreditCardTokenRequest` | `AccountOnFile` | `TokenAccount` | `Primary`, `Secondary` |
| [CreatePayment](operations/02-orders-payments.md#createpayment) | `CreatePaymentRequest` | `PaymentType` | `PaymentType` | `Cash`, `CreditCard`, `Check`, `CreditVoucher`, `Net30`, `Net60`, `UseCredit`, `ACHDebit`, `BankDraft`, `BankWire`, `PointRedemtion`, `COD`, `MoneyOrder`, `BankDeposit`, `Other1`, `Other2`, `Other3`, `Wallet`, `Other4`, `Other5`, `Other6`, `Other7`, `Other8`, `Other9`, `Other10`, `Other11`, `Other12`, `Other13`, `Other14`, `Other15` |
| [ChargeCreditCardTokenOnFile](operations/02-orders-payments.md#chargecreditcardtokenonfile) | `ChargeCreditCardTokenOnFileRequest` | `CreditCardAccountType` | `AccountCreditCardType` | `Primary`, `Secondary` |
| [ChargeWalletAccountOnFile](operations/02-orders-payments.md#chargewalletaccountonfile) | `ChargeWalletAccountOnFileRequest` | `WalletAccountType` | `AccountWalletType` | `Primary`, `Secondary`, `Third`, `Fourth`, `Fifth` |
| [DebitBankAccount](operations/02-orders-payments.md#debitbankaccount) | `DebitBankAccountRequest` | `BankAccountType` | `BankAccountType` | `CheckingPersonal`, `CheckingBusiness`, `SavingsPersonal`, `SavingsBusiness` |
| [CreateExpectedPayment](operations/02-orders-payments.md#createexpectedpayment) | `CreateExpectedPaymentRequest` | `PaymentType` | `PaymentType` | `Cash`, `CreditCard`, `Check`, `CreditVoucher`, `Net30`, `Net60`, `UseCredit`, `ACHDebit`, `BankDraft`, `BankWire`, `PointRedemtion`, `COD`, `MoneyOrder`, `BankDeposit`, `Other1`, `Other2`, `Other3`, `Wallet`, `Other4`, `Other5`, `Other6`, `Other7`, `Other8`, `Other9`, `Other10`, `Other11`, `Other12`, `Other13`, `Other14`, `Other15` |
| [GetOrders](operations/02-orders-payments.md#getorders) | `GetOrdersRequest` | `OrderStatus` | `OrderStatusType` | `Incomplete`, `Pending`, `CCDeclined`, `ACHDeclined`, `Canceled`, `CCPending`, `ACHPending`, `Accepted`, `Printed`, `Shipped`, `PendingInventory` |
| [GetOrders](operations/02-orders-payments.md#getorders) | `OrderResponse` | `OrderStatus` | `OrderStatusType` | `Incomplete`, `Pending`, `CCDeclined`, `ACHDeclined`, `Canceled`, `CCPending`, `ACHPending`, `Accepted`, `Printed`, `Shipped`, `PendingInventory` |
| [GetOrders](operations/02-orders-payments.md#getorders) | `OrderResponse` | `OrderType` | `OrderType` | `Default`, `CustomerService`, `ShoppingCart`, `WebWizard`, `AutoOrder`, `Import`, `BackOrder`, `ReplacementOrder`, `ReturnOrder`, `WebAutoOrder`, `TicketSystem`, `APIOrder`, `BackOrderParent`, `ChildOrder`, `Other1`, `Other2`, `Other3`, `Other4`, `Other5`, `Other6`, `Other7`, `Other8`, `Other9`, `Other10` |
| [GetOrders](operations/02-orders-payments.md#getorders) | `PaymentResponse` | `PaymentType` | `PaymentType` | `Cash`, `CreditCard`, `Check`, `CreditVoucher`, `Net30`, `Net60`, `UseCredit`, `ACHDebit`, `BankDraft`, `BankWire`, `PointRedemtion`, `COD`, `MoneyOrder`, `BankDeposit`, `Other1`, `Other2`, `Other3`, `Wallet`, `Other4`, `Other5`, `Other6`, `Other7`, `Other8`, `Other9`, `Other10`, `Other11`, `Other12`, `Other13`, `Other14`, `Other15` |
| [GetOrders](operations/02-orders-payments.md#getorders) | `ExpectedPaymentResponse` | `PaymentType` | `PaymentType` | `Cash`, `CreditCard`, `Check`, `CreditVoucher`, `Net30`, `Net60`, `UseCredit`, `ACHDebit`, `BankDraft`, `BankWire`, `PointRedemtion`, `COD`, `MoneyOrder`, `BankDeposit`, `Other1`, `Other2`, `Other3`, `Wallet`, `Other4`, `Other5`, `Other6`, `Other7`, `Other8`, `Other9`, `Other10`, `Other11`, `Other12`, `Other13`, `Other14`, `Other15` |
| [GetOrderInvoice](operations/02-orders-payments.md#getorderinvoice) | `GetOrderInvoiceRequest` | `Format` | `InvoiceRenderFormat` | `HTML` |
| [AuthorizeOnlyCreditCardTokenOnFile](operations/02-orders-payments.md#authorizeonlycreditcardtokenonfile) | `AuthorizeOnlyCreditCardTokenOnFileRequest` | `CreditCardAccountType` | `AccountCreditCardType` | `Primary`, `Secondary` |
| [ValidateWalletAccount](operations/02-orders-payments.md#validatewalletaccount) | `ValidateWalletAccountRequest` | `WalletAccountType` | `AccountWalletType` | `Primary`, `Secondary`, `Third`, `Fourth`, `Fifth` |
| [CreateAutoOrder](operations/03-recurring-orders.md#createautoorder) | `CreateAutoOrderRequest` | `Frequency` | `FrequencyType` | `Weekly`, `BiWeekly`, `Monthly`, `Quarterly`, `SemiYearly`, `Yearly`, `BiMonthly`, `EveryFourWeeks`, `EverySixWeeks`, `EveryEightWeeks`, `EveryTwelveWeeks`, `SpecificDays`, `Custom` |
| [CreateAutoOrder](operations/03-recurring-orders.md#createautoorder) | `CreateAutoOrderRequest` | `PaymentType` | `AutoOrderPaymentType` | `PrimaryCreditCard`, `SecondaryCreditCard`, `CheckingAccount`, `WillSendPayment`, `BankDraft`, `PrimaryWalletAccount`, `SecondaryWalletAccount`, `ThirdWalletAccount`, `FourthWalletAccount`, `FifthWalletAccount` |
| [CreateAutoOrder](operations/03-recurring-orders.md#createautoorder) | `CreateAutoOrderRequest` | `ProcessType` | `AutoOrderProcessType` | `AlwaysProcess`, `Conditional` |
| [UpdateAutoOrder](operations/03-recurring-orders.md#updateautoorder) | `UpdateAutoOrderRequest` | `Frequency` | `FrequencyType` | `Weekly`, `BiWeekly`, `Monthly`, `Quarterly`, `SemiYearly`, `Yearly`, `BiMonthly`, `EveryFourWeeks`, `EverySixWeeks`, `EveryEightWeeks`, `EveryTwelveWeeks`, `SpecificDays`, `Custom` |
| [UpdateAutoOrder](operations/03-recurring-orders.md#updateautoorder) | `UpdateAutoOrderRequest` | `PaymentType` | `AutoOrderPaymentType` | `PrimaryCreditCard`, `SecondaryCreditCard`, `CheckingAccount`, `WillSendPayment`, `BankDraft`, `PrimaryWalletAccount`, `SecondaryWalletAccount`, `ThirdWalletAccount`, `FourthWalletAccount`, `FifthWalletAccount` |
| [UpdateAutoOrder](operations/03-recurring-orders.md#updateautoorder) | `UpdateAutoOrderRequest` | `ProcessType` | `AutoOrderProcessType` | `AlwaysProcess`, `Conditional` |
| [ChangeAutoOrderStatus](operations/03-recurring-orders.md#changeautoorderstatus) | `ChangeAutoOrderStatusRequest` | `AutoOrderStatus` | `AutoOrderStatusType` | `Active`, `Inactive`, `Deleted` |
| [GetAutoOrders](operations/03-recurring-orders.md#getautoorders) | `GetAutoOrdersRequest` | `AutoOrderStatus` | `AutoOrderStatusType` | `Active`, `Inactive`, `Deleted` |
| [GetAutoOrders](operations/03-recurring-orders.md#getautoorders) | `AutoOrderResponse` | `AutoOrderStatus` | `AutoOrderStatusType` | `Active`, `Inactive`, `Deleted` |
| [GetAutoOrders](operations/03-recurring-orders.md#getautoorders) | `AutoOrderResponse` | `Frequency` | `FrequencyType` | `Weekly`, `BiWeekly`, `Monthly`, `Quarterly`, `SemiYearly`, `Yearly`, `BiMonthly`, `EveryFourWeeks`, `EverySixWeeks`, `EveryEightWeeks`, `EveryTwelveWeeks`, `SpecificDays`, `Custom` |
| [GetAutoOrders](operations/03-recurring-orders.md#getautoorders) | `AutoOrderResponse` | `PaymentType` | `AutoOrderPaymentType` | `PrimaryCreditCard`, `SecondaryCreditCard`, `CheckingAccount`, `WillSendPayment`, `BankDraft`, `PrimaryWalletAccount`, `SecondaryWalletAccount`, `ThirdWalletAccount`, `FourthWalletAccount`, `FifthWalletAccount` |
| [GetAutoOrders](operations/03-recurring-orders.md#getautoorders) | `AutoOrderResponse` | `ProcessType` | `AutoOrderProcessType` | `AlwaysProcess`, `Conditional` |
| [GetItems](operations/04-items.md#getitems) | `ItemResponse` | `InventoryStatus` | `InventoryStatusType` | `Available`, `OnBackOrder`, `OutOfStock`, `Discontinued` |
| [GetItems](operations/04-items.md#getitems) | `ItemMemberResponse` | `InventoryStatus` | `InventoryStatusType` | `Available`, `OnBackOrder`, `OutOfStock`, `Discontinued` |
| [GetItems](operations/04-items.md#getitems) | `KitMemberItemResponse` | `InventoryStatus` | `InventoryStatusType` | `Available`, `OnBackOrder`, `OutOfStock`, `Discontinued` |
| [PlaceBinaryNode](operations/05-tree-movement.md#placebinarynode) | `PlaceBinaryNodeRequest` | `PlacementType` | `BinaryPlacementType` | `StrategicPlacement`, `BuildLeft`, `BuildRight`, `BalancedBuild`, `EvenFill`, `WeakLeg`, `EnrollerPreference`, `LeftEvenFill`, `RightEvenFill`, `LesserVolumeLeg`, `LesserVolumeLegOutside`, `StrongLegOutside`, `LesserVolumeLegEvenFill`, `GreaterVolumeLegEvenFill`, `InsertRightMoveDownline`, `InsertLeftMoveDownline`, `BuildTeamLeg` |
| [GetBinaryPreference](operations/05-tree-movement.md#getbinarypreference) | `GetBinaryPreferenceResponse` | `PlacementType` | `BinaryPlacementType` | `StrategicPlacement`, `BuildLeft`, `BuildRight`, `BalancedBuild`, `EvenFill`, `WeakLeg`, `EnrollerPreference`, `LeftEvenFill`, `RightEvenFill`, `LesserVolumeLeg`, `LesserVolumeLegOutside`, `StrongLegOutside`, `LesserVolumeLegEvenFill`, `GreaterVolumeLegEvenFill`, `InsertRightMoveDownline`, `InsertLeftMoveDownline`, `BuildTeamLeg` |
| [SetBinaryPreference](operations/05-tree-movement.md#setbinarypreference) | `SetBinaryPreferenceRequest` | `PlacementType` | `BinaryPlacementType` | `StrategicPlacement`, `BuildLeft`, `BuildRight`, `BalancedBuild`, `EvenFill`, `WeakLeg`, `EnrollerPreference`, `LeftEvenFill`, `RightEvenFill`, `LesserVolumeLeg`, `LesserVolumeLegOutside`, `StrongLegOutside`, `LesserVolumeLegEvenFill`, `GreaterVolumeLegEvenFill`, `InsertRightMoveDownline`, `InsertLeftMoveDownline`, `BuildTeamLeg` |
| [GetBillPayoutQueue](operations/06-payout.md#getbillpayoutqueue) | `BillPayoutQueueItem` | `StatusType` | `PayoutQueueStatusType` | `Processing`, `Complete`, `CompleteWithErrors` |
| [GetDownline](operations/07-reporting.md#getdownline) | `GetDownlineRequest` | `TreeType` | `TreeType` | `Enroller`, `UniLevel`, `Binary`, `Matrix`, `Stack` |
| [GetDownline](operations/07-reporting.md#getdownline) | `VolumeFilter` | `Compare` | `NumericCompareType` | `Equals`, `GreaterThan`, `LessThan` |
| [GetUpline](operations/07-reporting.md#getupline) | `GetUplineRequest` | `TreeType` | `TreeType` | `Enroller`, `UniLevel`, `Binary`, `Matrix`, `Stack` |
| [GetCompanyNews](operations/08-communications.md#getcompanynews) | `CompanyNewsResponse` | `WebSettings` | `NewsWebSettings` | `AccessAvailable`, `AccessNotAvailable` |
| [GetCompanyNews](operations/08-communications.md#getcompanynews) | `CompanyNewsResponse` | `CompanySettings` | `NewsCompanySettings` | `AccessAllUsers`, `AccessByDepartment`, `AccessNotAvailable` |
| [GetCompanyNewsItem](operations/08-communications.md#getcompanynewsitem) | `GetCompanyNewsItemResponse` | `WebSettings` | `NewsWebSettings` | `AccessAvailable`, `AccessNotAvailable` |
| [GetCompanyNewsItem](operations/08-communications.md#getcompanynewsitem) | `GetCompanyNewsItemResponse` | `CompanySettings` | `NewsCompanySettings` | `AccessAllUsers`, `AccessByDepartment`, `AccessNotAvailable` |
| [GetPartyGuests](operations/09-party-plan.md#getpartyguests) | `GuestResponse` | `Gender` | `Gender` | `Unknown`, `Male`, `Female` |
| [CreateGuest](operations/09-party-plan.md#createguest) | `CreateGuestRequest` | `Gender` | `Gender` | `Unknown`, `Male`, `Female` |
| [UpdateGuest](operations/09-party-plan.md#updateguest) | `UpdateGuestRequest` | `Gender` | `Gender` | `Unknown`, `Male`, `Female` |
| [GetGuests](operations/09-party-plan.md#getguests) | `GuestResponse` | `Gender` | `Gender` | `Unknown`, `Male`, `Female` |
| [CreatePointTransaction](operations/10-points-subscriptions.md#createpointtransaction) | `CreatePointTransactionRequest` | `TransactionType` | `PointTransactionType` | `Redemption`, `Adjustment` |
| [GetSubscription](operations/10-points-subscriptions.md#getsubscription) | `GetSubscriptionResponse` | `Status` | `SubscriptionStatus` | `NotFound`, `Active`, `Expired`, `Cancelled` |
| [GetSubscriptions](operations/10-points-subscriptions.md#getsubscriptions) | `SubscriptionResponse` | `Status` | `SubscriptionStatus` | `NotFound`, `Active`, `Expired`, `Cancelled` |
| [CreateCalendarItem](operations/11-calendar.md#createcalendaritem) | `CreateCalendarItemRequest` | `CalendarItemType` | `CalendarItemType` | `Appointment`, `ToDo`, `Anniversary` |
| [CreateCalendarItem](operations/11-calendar.md#createcalendaritem) | `CreateCalendarItemRequest` | `CalendarItemStatusType` | `CalendarItemStatusType` | `Open`, `Closed` |
| [CreateCalendarItem](operations/11-calendar.md#createcalendaritem) | `CreateCalendarItemRequest` | `CalendarItemPriorityType` | `CalendarItemPriorityType` | `None`, `High`, `Medium`, `Low` |
| [CreateCalendarItem](operations/11-calendar.md#createcalendaritem) | `CreateCalendarItemRequest` | `ContactPhoneType` | `ContactPhoneType` | `Office`, `Mobile`, `Home` |
| [UpdateCalendarItem](operations/11-calendar.md#updatecalendaritem) | `UpdateCalendarItemRequest` | `CalendarItemType` | `CalendarItemType` | `Appointment`, `ToDo`, `Anniversary` |
| [UpdateCalendarItem](operations/11-calendar.md#updatecalendaritem) | `UpdateCalendarItemRequest` | `CalendarItemStatusType` | `CalendarItemStatusType` | `Open`, `Closed` |
| [UpdateCalendarItem](operations/11-calendar.md#updatecalendaritem) | `UpdateCalendarItemRequest` | `CalendarItemPriorityType` | `CalendarItemPriorityType` | `None`, `High`, `Medium`, `Low` |
| [UpdateCalendarItem](operations/11-calendar.md#updatecalendaritem) | `UpdateCalendarItemRequest` | `ContactPhoneType` | `ContactPhoneType` | `Office`, `Mobile`, `Home` |
| [CreateResourceSetIntItem](operations/15-web-content.md#createresourcesetintitem) | `CreateResourceSetIntItemRequest` | `ResourceType` | `ResourceType` | `Text`, `Int`, `Decimal`, `Date`, `Boolean`, `DropDown`, `Image`, `Widget`, `Banner`, `DataSet`, `Carousel` |
| [CreateResourceSetDecimalItem](operations/15-web-content.md#createresourcesetdecimalitem) | `CreateResourceSetDecimalItemRequest` | `ResourceType` | `ResourceType` | `Text`, `Int`, `Decimal`, `Date`, `Boolean`, `DropDown`, `Image`, `Widget`, `Banner`, `DataSet`, `Carousel` |
| [CreateResourceSetTextItem](operations/15-web-content.md#createresourcesettextitem) | `CreateResourceSetTextItemRequest` | `ResourceType` | `ResourceType` | `Text`, `Int`, `Decimal`, `Date`, `Boolean`, `DropDown`, `Image`, `Widget`, `Banner`, `DataSet`, `Carousel` |
| [CreateResourceSetBooleanItem](operations/15-web-content.md#createresourcesetbooleanitem) | `CreateResourceSetBooleanItemRequest` | `ResourceType` | `ResourceType` | `Text`, `Int`, `Decimal`, `Date`, `Boolean`, `DropDown`, `Image`, `Widget`, `Banner`, `DataSet`, `Carousel` |
| [CreateResourceSetDateItem](operations/15-web-content.md#createresourcesetdateitem) | `CreateResourceSetDateItemRequest` | `ResourceType` | `ResourceType` | `Text`, `Int`, `Decimal`, `Date`, `Boolean`, `DropDown`, `Image`, `Widget`, `Banner`, `DataSet`, `Carousel` |
| [CreateResourceSetImageItem](operations/15-web-content.md#createresourcesetimageitem) | `CreateResourceSetImageItemRequest` | `ResourceType` | `ResourceType` | `Text`, `Int`, `Decimal`, `Date`, `Boolean`, `DropDown`, `Image`, `Widget`, `Banner`, `DataSet`, `Carousel` |
| [CreateResourceSetDataSetItem](operations/15-web-content.md#createresourcesetdatasetitem) | `CreateResourceSetDataSetItemRequest` | `ResourceType` | `ResourceType` | `Text`, `Int`, `Decimal`, `Date`, `Boolean`, `DropDown`, `Image`, `Widget`, `Banner`, `DataSet`, `Carousel` |
| [CreateResourceSetBannerItem](operations/15-web-content.md#createresourcesetbanneritem) | `CreateResourceSetBannerItemRequest` | `BannerClickEvent` | `BannerClickEvent` | `OpenInNewTab`, `OpenInCurrentWindow`, `None` |
| [CreateResourceSetBannerItem](operations/15-web-content.md#createresourcesetbanneritem) | `CreateResourceSetBannerItemRequest` | `BannerType` | `BannerType` | `TextOnImage`, `ImageTop`, `InvalidType` |
| [CreateResourceSetBannerItem](operations/15-web-content.md#createresourcesetbanneritem) | `CreateResourceSetBannerItemRequest` | `ResourceType` | `ResourceType` | `Text`, `Int`, `Decimal`, `Date`, `Boolean`, `DropDown`, `Image`, `Widget`, `Banner`, `DataSet`, `Carousel` |
| [CreateResourceSetCarouselItem](operations/15-web-content.md#createresourcesetcarouselitem) | `CreateResourceSetCarouselItemRequest` | `CarouselType` | `CarouselType` | `Bootstrap3`, `Bootstrap4`, `Bootstrap5` |
| [CreateResourceSetCarouselItem](operations/15-web-content.md#createresourcesetcarouselitem) | `CreateResourceSetCarouselItemRequest` | `ResourceType` | `ResourceType` | `Text`, `Int`, `Decimal`, `Date`, `Boolean`, `DropDown`, `Image`, `Widget`, `Banner`, `DataSet`, `Carousel` |
| [CreateResourceSetWidgetItem](operations/15-web-content.md#createresourcesetwidgetitem) | `CreateResourceSetWidgetItemRequest` | `ResourceType` | `ResourceType` | `Text`, `Int`, `Decimal`, `Date`, `Boolean`, `DropDown`, `Image`, `Widget`, `Banner`, `DataSet`, `Carousel` |
| [CreateResourceSetDropDownItem](operations/15-web-content.md#createresourcesetdropdownitem) | `CreateResourceSetDropDownItemRequest` | `ResourceType` | `ResourceType` | `Text`, `Int`, `Decimal`, `Date`, `Boolean`, `DropDown`, `Image`, `Widget`, `Banner`, `DataSet`, `Carousel` |
| [GetResourceSetItems](operations/15-web-content.md#getresourcesetitems) | `ResourceItem` | `ResourceTypeID` | `ResourceType` | `Text`, `Int`, `Decimal`, `Date`, `Boolean`, `DropDown`, `Image`, `Widget`, `Banner`, `DataSet`, `Carousel` |
| [UpdateResourceSetBannerItem](operations/15-web-content.md#updateresourcesetbanneritem) | `UpdateResourceSetBannerItemRequest` | `NewBannerClickEvent` | `BannerClickEvent` | `OpenInNewTab`, `OpenInCurrentWindow`, `None` |
| [UpdateResourceSetBannerItem](operations/15-web-content.md#updateresourcesetbanneritem) | `UpdateResourceSetBannerItemRequest` | `NewBannerType` | `BannerType` | `TextOnImage`, `ImageTop`, `InvalidType` |
| [UpdateResourceSetCarouselItem](operations/15-web-content.md#updateresourcesetcarouselitem) | `UpdateResourceSetCarouselItemRequest` | `NewCarouselType` | `CarouselType` | `Bootstrap3`, `Bootstrap4`, `Bootstrap5` |
| [GetExtendedDbSchema](operations/16-extended-db.md#getextendeddbschema) | `PropertyDataResponse` | `Type` | `PropertyType` | `Guid`, `DateTime2`, `Integer`, `Decimal`, `DateTime`, `Boolean`, `Binary`, `String`, `StringMax` |
| [CreateExtendedDbEntity](operations/16-extended-db.md#createextendeddbentity) | `PropertyDataRequest` | `Type` | `PropertyType` | `Guid`, `DateTime2`, `Integer`, `Decimal`, `DateTime`, `Boolean`, `Binary`, `String`, `StringMax` |
| [CreateExtendedDbEntity](operations/16-extended-db.md#createextendeddbentity) | `PropertyDataResponse` | `Type` | `PropertyType` | `Guid`, `DateTime2`, `Integer`, `Decimal`, `DateTime`, `Boolean`, `Binary`, `String`, `StringMax` |
| [GetExtendedDbEntity](operations/16-extended-db.md#getextendeddbentity) | `PropertyDataResponse` | `Type` | `PropertyType` | `Guid`, `DateTime2`, `Integer`, `Decimal`, `DateTime`, `Boolean`, `Binary`, `String`, `StringMax` |
| [UpdateExtendedDbEntity](operations/16-extended-db.md#updateextendeddbentity) | `PropertyDataRequest` | `Type` | `PropertyType` | `Guid`, `DateTime2`, `Integer`, `Decimal`, `DateTime`, `Boolean`, `Binary`, `String`, `StringMax` |
| [UpdateExtendedDbEntity](operations/16-extended-db.md#updateextendeddbentity) | `PropertyDataResponse` | `Type` | `PropertyType` | `Guid`, `DateTime2`, `Integer`, `Decimal`, `DateTime`, `Boolean`, `Binary`, `String`, `StringMax` |
| [GetFilterGroup](operations/17-sync.md#getfiltergroup) | `TableFilterSetting` | `FilterType` | `FilterType` | `MaxDays`, `InList` |
| [EnableFilterGroup](operations/17-sync.md#enablefiltergroup) | `EnableFilterGroupRequest` | `FilterGroupID` | `TableGroupID` | `Misc`, `AutoOrder`, `Core`, `Commission`, `Customer`, `CustomersExtended`, `Item`, `Log`, `Messaging`, `Order`, `Payout`, `Tree`, `User`, `Image` |
| [DisableFilterGroup](operations/17-sync.md#disablefiltergroup) | `DisableFilterGroupRequest` | `FilterGroupID` | `TableGroupID` | `Misc`, `AutoOrder`, `Core`, `Commission`, `Customer`, `CustomersExtended`, `Item`, `Log`, `Messaging`, `Order`, `Payout`, `Tree`, `User`, `Image` |
| [UpdateTableFilterSettings](operations/17-sync.md#updatetablefiltersettings) | `UpdateTableFilterSettingsRequest` | `FilterGroupId` | `TableGroupID` | `Misc`, `AutoOrder`, `Core`, `Commission`, `Customer`, `CustomersExtended`, `Item`, `Log`, `Messaging`, `Order`, `Payout`, `Tree`, `User`, `Image` |
| [CreateTableFilterSettings](operations/17-sync.md#createtablefiltersettings) | `CreateTableFilterSettingsRequest` | `FilterGroupId` | `TableGroupID` | `Misc`, `AutoOrder`, `Core`, `Commission`, `Customer`, `CustomersExtended`, `Item`, `Log`, `Messaging`, `Order`, `Payout`, `Tree`, `User`, `Image` |
| [ChargeCreditCardOnFile](operations/19-unlisted-wsdl-only.md#chargecreditcardonfile) | `ChargeCreditCardOnFileRequest` | `CreditCardAccountType` | `AccountCreditCardType` | `Primary`, `Secondary` |
| [CreateEmail](operations/19-unlisted-wsdl-only.md#createemail) | `CreateEmailRequest` | `MailFolderType` | `MailForderType` | `SubFolder`, `Inbox`, `SentItems`, `Drafts`, `DeletedItems`, `JunkMail`, `FaxInbox`, `SentFaxes`, `PersonalFolders` |
| [CreateEmail](operations/19-unlisted-wsdl-only.md#createemail) | `CreateEmailRequest` | `Priority` | `MailPriority` | `Low`, `Normal`, `High` |
| [CreateEmail](operations/19-unlisted-wsdl-only.md#createemail) | `CreateEmailRequest` | `MailStatusType` | `MailStatusType` | `New`, `Read`, `Forwarded`, `Replied` |
| [GetPayments](operations/19-unlisted-wsdl-only.md#getpayments) | `PaymentResponse` | `PaymentType` | `PaymentType` | `Cash`, `CreditCard`, `Check`, `CreditVoucher`, `Net30`, `Net60`, `UseCredit`, `ACHDebit`, `BankDraft`, `BankWire`, `PointRedemtion`, `COD`, `MoneyOrder`, `BankDeposit`, `Other1`, `Other2`, `Other3`, `Wallet`, `Other4`, `Other5`, `Other6`, `Other7`, `Other8`, `Other9`, `Other10`, `Other11`, `Other12`, `Other13`, `Other14`, `Other15` |
| [Ping](operations/19-unlisted-wsdl-only.md#ping) | `CalculateOrderRequest` | `OrderType` | `OrderType` | `Default`, `CustomerService`, `ShoppingCart`, `WebWizard`, `AutoOrder`, `Import`, `BackOrder`, `ReplacementOrder`, `ReturnOrder`, `WebAutoOrder`, `TicketSystem`, `APIOrder`, `BackOrderParent`, `ChildOrder`, `Other1`, `Other2`, `Other3`, `Other4`, `Other5`, `Other6`, `Other7`, `Other8`, `Other9`, `Other10` |
| [SetAccountCreditCard](operations/19-unlisted-wsdl-only.md#setaccountcreditcard) | `SetAccountCreditCardRequest` | `CreditCardAccountType` | `AccountCreditCardType` | `Primary`, `Secondary` |
| [UpdateEmailStatus](operations/19-unlisted-wsdl-only.md#updateemailstatus) | `UpdateEmailStatusRequest` | `MailStatusType` | `MailStatusType` | `New`, `Read`, `Forwarded`, `Replied` |
