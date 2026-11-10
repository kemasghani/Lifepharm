# Exigo API — Data types (WSDL)

Back to [index](README.md). All 792 complex types from `https://api.exigo.com/3.0/ExigoApi.asmx?WSDL`. `min=0` means optional; `max=unbounded` means array. Enum types are in [enums.md](enums.md).

| Type | Fields |
|---|---|
| [AddBankAccountTypeRequest](#addbankaccounttyperequest) | 1 |
| [AddBankAccountTypeResponse](#addbankaccounttyperesponse) | 1 |
| [AddPartyGuestsRequest](#addpartyguestsrequest) | 2 |
| [AddPartyGuestsResponse](#addpartyguestsresponse) | 0 |
| [AddProductsToCategoryRequest](#addproductstocategoryrequest) | 3 |
| [AddProductsToCategoryResponse](#addproductstocategoryresponse) | 2 |
| [AdjustInventoryRequest](#adjustinventoryrequest) | 4 |
| [AdjustInventoryResponse](#adjustinventoryresponse) | 0 |
| [AdminWhitelistResponse](#adminwhitelistresponse) | 3 |
| [AdvancedAutoOptionsRequest](#advancedautooptionsrequest) | 5 |
| [AlertSettings](#alertsettings) | 3 |
| [ApiAuthentication](#apiauthentication) | 6 |
| [ApiRequest](#apirequest) | 0 |
| [ApiResponse](#apiresponse) | 1 |
| [ApiResult](#apiresult) | 3 |
| [ApiWhitelistResponse](#apiwhitelistresponse) | 4 |
| [AppendCustomerNotesRequest](#appendcustomernotesrequest) | 3 |
| [AppendCustomerNotesResponse](#appendcustomernotesresponse) | 2 |
| [ArrayOfAdminWhitelistResponse](#arrayofadminwhitelistresponse) | 1 |
| [ArrayOfApiRequest](#arrayofapirequest) | 1 |
| [ArrayOfApiResponse](#arrayofapiresponse) | 1 |
| [ArrayOfApiWhitelistResponse](#arrayofapiwhitelistresponse) | 1 |
| [ArrayOfArrayOfQualificationResponse](#arrayofarrayofqualificationresponse) | 1 |
| [ArrayOfAutoOrderDetailResponse](#arrayofautoorderdetailresponse) | 1 |
| [ArrayOfAutoOrderResponse](#arrayofautoorderresponse) | 1 |
| [ArrayOfBankAccountTypeResponse](#arrayofbankaccounttyperesponse) | 1 |
| [ArrayOfBill](#arrayofbill) | 1 |
| [ArrayOfBillAmount](#arrayofbillamount) | 1 |
| [ArrayOfBillDetail](#arrayofbilldetail) | 1 |
| [ArrayOfBillItem](#arrayofbillitem) | 1 |
| [ArrayOfBillPayment](#arrayofbillpayment) | 1 |
| [ArrayOfBillPayoutQueueItem](#arrayofbillpayoutqueueitem) | 1 |
| [ArrayOfBillResponse](#arrayofbillresponse) | 1 |
| [ArrayOfCommissionBonusResponse](#arrayofcommissionbonusresponse) | 1 |
| [ArrayOfCommissionDetailResponse](#arrayofcommissiondetailresponse) | 1 |
| [ArrayOfCommissionResponse](#arrayofcommissionresponse) | 1 |
| [ArrayOfCompanyNewsResponse](#arrayofcompanynewsresponse) | 1 |
| [ArrayOfCountryResponse](#arrayofcountryresponse) | 1 |
| [ArrayOfCultureCodeItem](#arrayofculturecodeitem) | 1 |
| [ArrayOfCustomerBalanceResponse](#arrayofcustomerbalanceresponse) | 1 |
| [ArrayOfCustomerEventField](#arrayofcustomereventfield) | 1 |
| [ArrayOfCustomerEventResponse](#arrayofcustomereventresponse) | 1 |
| [ArrayOfCustomerExtendedResponse](#arrayofcustomerextendedresponse) | 1 |
| [ArrayOfCustomerFilesResponse](#arrayofcustomerfilesresponse) | 1 |
| [ArrayOfCustomerFoldersResponse](#arrayofcustomerfoldersresponse) | 1 |
| [ArrayOfCustomerLeadSocialNetworkRequest](#arrayofcustomerleadsocialnetworkrequest) | 1 |
| [ArrayOfCustomerLeadSocialNetworksResponse](#arrayofcustomerleadsocialnetworksresponse) | 1 |
| [ArrayOfCustomerLeadsResponse](#arrayofcustomerleadsresponse) | 1 |
| [ArrayOfCustomerNotesResponse](#arrayofcustomernotesresponse) | 1 |
| [ArrayOfCustomerResponse](#arrayofcustomerresponse) | 1 |
| [ArrayOfCustomerSocialNetworkRequest](#arrayofcustomersocialnetworkrequest) | 1 |
| [ArrayOfCustomerSocialNetworksResponse](#arrayofcustomersocialnetworksresponse) | 1 |
| [ArrayOfCustomerWallItemResponse](#arrayofcustomerwallitemresponse) | 1 |
| [ArrayOfDepartmentInfo](#arrayofdepartmentinfo) | 1 |
| [ArrayOfDestination](#arrayofdestination) | 1 |
| [ArrayOfDestinationTestResponseDetail](#arrayofdestinationtestresponsedetail) | 1 |
| [ArrayOfEmailAttachment](#arrayofemailattachment) | 1 |
| [ArrayOfEntityDataResponse](#arrayofentitydataresponse) | 1 |
| [ArrayOfExpectedPaymentResponse](#arrayofexpectedpaymentresponse) | 1 |
| [ArrayOfFilterGroup](#arrayoffiltergroup) | 1 |
| [ArrayOfForwardedAttachment](#arrayofforwardedattachment) | 1 |
| [ArrayOfGetQualificationOverrideResponse](#arrayofgetqualificationoverrideresponse) | 1 |
| [ArrayOfGroupOrder](#arrayofgrouporder) | 1 |
| [ArrayOfGuestResponse](#arrayofguestresponse) | 1 |
| [ArrayOfGuestSocialNetworkRequest](#arrayofguestsocialnetworkrequest) | 1 |
| [ArrayOfGuestSocialNetworksResponse](#arrayofguestsocialnetworksresponse) | 1 |
| [ArrayOfInt](#arrayofint) | 1 |
| [ArrayOfItemCountryRegionResponse](#arrayofitemcountryregionresponse) | 1 |
| [ArrayOfItemMemberResponse](#arrayofitemmemberresponse) | 1 |
| [ArrayOfItemResponse](#arrayofitemresponse) | 1 |
| [ArrayOfKitMember](#arrayofkitmember) | 1 |
| [ArrayOfKitMemberItemResponse](#arrayofkitmemberitemresponse) | 1 |
| [ArrayOfKitMemberResponse](#arrayofkitmemberresponse) | 1 |
| [ArrayOfLanguageResponse](#arrayoflanguageresponse) | 1 |
| [ArrayOfNodeResponse](#arrayofnoderesponse) | 1 |
| [ArrayOfOrderBatchDetailRequest](#arrayoforderbatchdetailrequest) | 1 |
| [ArrayOfOrderDetailIDs](#arrayoforderdetailids) | 1 |
| [ArrayOfOrderDetailRequest](#arrayoforderdetailrequest) | 1 |
| [ArrayOfOrderDetailResponse](#arrayoforderdetailresponse) | 1 |
| [ArrayOfOrderImportDetail](#arrayoforderimportdetail) | 1 |
| [ArrayOfOrderResponse](#arrayoforderresponse) | 1 |
| [ArrayOfOrderStatusType](#arrayoforderstatustype) | 1 |
| [ArrayOfOrderTotalByCurrency](#arrayofordertotalbycurrency) | 1 |
| [ArrayOfOrderType](#arrayofordertype) | 1 |
| [ArrayOfParameterRequest](#arrayofparameterrequest) | 1 |
| [ArrayOfPartyResponse](#arrayofpartyresponse) | 1 |
| [ArrayOfPaymentResponse](#arrayofpaymentresponse) | 1 |
| [ArrayOfPaymentsResponse](#arrayofpaymentsresponse) | 1 |
| [ArrayOfPointAccount](#arrayofpointaccount) | 1 |
| [ArrayOfPropertyDataRequest](#arrayofpropertydatarequest) | 1 |
| [ArrayOfPropertyDataResponse](#arrayofpropertydataresponse) | 1 |
| [ArrayOfPropertyDataUpdateRequest](#arrayofpropertydataupdaterequest) | 1 |
| [ArrayOfQualificationResponse](#arrayofqualificationresponse) | 1 |
| [ArrayOfReIndexHistoryItem](#arrayofreindexhistoryitem) | 1 |
| [ArrayOfRegionResponse](#arrayofregionresponse) | 1 |
| [ArrayOfReportParameterRequest](#arrayofreportparameterrequest) | 1 |
| [ArrayOfResourceGroup](#arrayofresourcegroup) | 1 |
| [ArrayOfResourceItem](#arrayofresourceitem) | 1 |
| [ArrayOfResourceSet](#arrayofresourceset) | 1 |
| [ArrayOfResourceSetCulture](#arrayofresourcesetculture) | 1 |
| [ArrayOfResourceSetEnvironment](#arrayofresourcesetenvironment) | 1 |
| [ArrayOfResourceSetRelease](#arrayofresourcesetrelease) | 1 |
| [ArrayOfResourceSetSubscriptionCheckIn](#arrayofresourcesetsubscriptioncheckin) | 1 |
| [ArrayOfResourceSubscriptionUpdate](#arrayofresourcesubscriptionupdate) | 1 |
| [ArrayOfSandbox](#arrayofsandbox) | 1 |
| [ArrayOfShipMethodResponse](#arrayofshipmethodresponse) | 1 |
| [ArrayOfString](#arrayofstring) | 1 |
| [ArrayOfSubscription](#arrayofsubscription) | 1 |
| [ArrayOfSubscriptionResponse](#arrayofsubscriptionresponse) | 1 |
| [ArrayOfTableFilterSetting](#arrayoftablefiltersetting) | 1 |
| [ArrayOfTableGroupID](#arrayoftablegroupid) | 1 |
| [ArrayOfTableName](#arrayoftablename) | 1 |
| [ArrayOfTableSettings](#arrayoftablesettings) | 1 |
| [ArrayOfVolumeFilter](#arrayofvolumefilter) | 1 |
| [ArrayOfVolumeResponse](#arrayofvolumeresponse) | 1 |
| [ArrayOfWarehouseResponse](#arrayofwarehouseresponse) | 1 |
| [AuthenticateCustomerRequest](#authenticatecustomerrequest) | 2 |
| [AuthenticateCustomerResponse](#authenticatecustomerresponse) | 4 |
| [AuthenticateUserRequest](#authenticateuserrequest) | 2 |
| [AuthenticateUserResponse](#authenticateuserresponse) | 2 |
| [AuthorizeOnlyCreditCardResponse](#authorizeonlycreditcardresponse) | 4 |
| [AuthorizeOnlyCreditCardTokenOnFileRequest](#authorizeonlycreditcardtokenonfilerequest) | 6 |
| [AuthorizeOnlyCreditCardTokenRequest](#authorizeonlycreditcardtokenrequest) | 13 |
| [AutoOrderDetailResponse](#autoorderdetailresponse) | 25 |
| [AutoOrderResponse](#autoorderresponse) | 55 |
| [AutoOrderSkipNextShipmentRequest](#autoorderskipnextshipmentrequest) | 1 |
| [AutoOrderSkipNextShipmentResponse](#autoorderskipnextshipmentresponse) | 1 |
| [BankAccountResponse](#bankaccountresponse) | 13 |
| [BankAccountTypeResponse](#bankaccounttyperesponse) | 2 |
| [BaseAuthorizeOnlyCreditCardTokenRequest](#baseauthorizeonlycreditcardtokenrequest) | 0 |
| [BaseBillPayoutOperationRequest](#basebillpayoutoperationrequest) | 0 |
| [BaseCalculateOrderRequest](#basecalculateorderrequest) | 0 |
| [BaseCalculateOrderResponse](#basecalculateorderresponse) | 0 |
| [BaseChargeCreditCardRequest](#basechargecreditcardrequest) | 0 |
| [BaseChargeWalletAccountRequest](#basechargewalletaccountrequest) | 10 |
| [BaseCreateExpectedPaymentRequest](#basecreateexpectedpaymentrequest) | 0 |
| [BaseCreateExpectedPaymentResponse](#basecreateexpectedpaymentresponse) | 0 |
| [BaseCreatePaymentCreditCardRequest](#basecreatepaymentcreditcardrequest) | 0 |
| [BaseCreatePaymentRequest](#basecreatepaymentrequest) | 0 |
| [BaseCreatePaymentResponse](#basecreatepaymentresponse) | 0 |
| [BaseCreatePayoutRequest](#basecreatepayoutrequest) | 6 |
| [BaseCreateResourceSetItemRequest](#basecreateresourcesetitemrequest) | 9 |
| [BaseDebitBankAccountRequest](#basedebitbankaccountrequest) | 0 |
| [BaseGetOrderInvoiceRequest](#basegetorderinvoicerequest) | 0 |
| [BaseProcessPayoutRequest](#baseprocesspayoutrequest) | 19 |
| [BaseUpdateResourceSetItemRequest](#baseupdateresourcesetitemrequest) | 9 |
| [Bill](#bill) | 13 |
| [BillAmount](#billamount) | 5 |
| [BillDetail](#billdetail) | 2 |
| [BillItem](#billitem) | 26 |
| [BillPayment](#billpayment) | 34 |
| [BillPayoutQueueItem](#billpayoutqueueitem) | 26 |
| [BillResponse](#billresponse) | 2 |
| [CalculateOrderRequest](#calculateorderrequest) | 46 |
| [CalculateOrderResponse](#calculateorderresponse) | 49 |
| [ChangeAutoOrderStatusRequest](#changeautoorderstatusrequest) | 2 |
| [ChangeAutoOrderStatusResponse](#changeautoorderstatusresponse) | 0 |
| [ChangeOrderStatusBatchRequest](#changeorderstatusbatchrequest) | 3 |
| [ChangeOrderStatusBatchResponse](#changeorderstatusbatchresponse) | 0 |
| [ChangeOrderStatusRequest](#changeorderstatusrequest) | 4 |
| [ChangeOrderStatusResponse](#changeorderstatusresponse) | 0 |
| [ChargeCreditCardOnFileRequest](#chargecreditcardonfilerequest) | 4 |
| [ChargeCreditCardRequest](#chargecreditcardrequest) | 16 |
| [ChargeCreditCardResponse](#chargecreditcardresponse) | 2 |
| [ChargeCreditCardTokenOnFileRequest](#chargecreditcardtokenonfilerequest) | 17 |
| [ChargeCreditCardTokenRequest](#chargecreditcardtokenrequest) | 30 |
| [ChargeGroupOrderCreditCardTokenRequest](#chargegroupordercreditcardtokenrequest) | 28 |
| [ChargeGroupOrderCreditCardTokenResponse](#chargegroupordercreditcardtokenresponse) | 4 |
| [ChargePriorAuthorizationRequest](#chargepriorauthorizationrequest) | 4 |
| [ChargeWalletAccountOnFileRequest](#chargewalletaccountonfilerequest) | 15 |
| [ChargeWalletAccountRequest](#chargewalletaccountrequest) | 6 |
| [ChargeWalletAccountResponse](#chargewalletaccountresponse) | 2 |
| [CommissionBonusResponse](#commissionbonusresponse) | 3 |
| [CommissionDetailResponse](#commissiondetailresponse) | 10 |
| [CommissionResponse](#commissionresponse) | 8 |
| [CompanyNewsResponse](#companynewsresponse) | 5 |
| [CountryResponse](#countryresponse) | 2 |
| [CreateAdminWhitelistRequest](#createadminwhitelistrequest) | 3 |
| [CreateAdminWhitelistResponse](#createadminwhitelistresponse) | 1 |
| [CreateApiWhitelistRequest](#createapiwhitelistrequest) | 3 |
| [CreateApiWhitelistResponse](#createapiwhitelistresponse) | 1 |
| [CreateAutoOrderRequest](#createautoorderrequest) | 43 |
| [CreateAutoOrderResponse](#createautoorderresponse) | 23 |
| [CreateBillPayoutRequest](#createbillpayoutrequest) | 0 |
| [CreateBillPayoutResponse](#createbillpayoutresponse) | 5 |
| [CreateBillRequest](#createbillrequest) | 13 |
| [CreateBillResponse](#createbillresponse) | 1 |
| [CreateBillsRequest](#createbillsrequest) | 1 |
| [CreateBillsResponse](#createbillsresponse) | 1 |
| [CreateCalendarItemRequest](#createcalendaritemrequest) | 29 |
| [CreateCalendarItemResponse](#createcalendaritemresponse) | 2 |
| [CreateCustomerBalanceAdjustmentRequest](#createcustomerbalanceadjustmentrequest) | 7 |
| [CreateCustomerBalanceAdjustmentResponse](#createcustomerbalanceadjustmentresponse) | 1 |
| [CreateCustomerContactRequest](#createcustomercontactrequest) | 25 |
| [CreateCustomerContactResponse](#createcustomercontactresponse) | 3 |
| [CreateCustomerExtendedRequest](#createcustomerextendedrequest) | 33 |
| [CreateCustomerExtendedResponse](#createcustomerextendedresponse) | 1 |
| [CreateCustomerFileRequest](#createcustomerfilerequest) | 7 |
| [CreateCustomerFileResponse](#createcustomerfileresponse) | 2 |
| [CreateCustomerFolderRequest](#createcustomerfolderrequest) | 4 |
| [CreateCustomerFolderResponse](#createcustomerfolderresponse) | 1 |
| [CreateCustomerInquiryRequest](#createcustomerinquiryrequest) | 8 |
| [CreateCustomerInquiryResponse](#createcustomerinquiryresponse) | 1 |
| [CreateCustomerLeadRequest](#createcustomerleadrequest) | 19 |
| [CreateCustomerLeadResponse](#createcustomerleadresponse) | 1 |
| [CreateCustomerRequest](#createcustomerrequest) | 93 |
| [CreateCustomerResponse](#createcustomerresponse) | 2 |
| [CreateCustomerWallItemRequest](#createcustomerwallitemrequest) | 6 |
| [CreateCustomerWallItemResponse](#createcustomerwallitemresponse) | 3 |
| [CreateDestinationRequest](#createdestinationrequest) | 2 |
| [CreateDestinationResponse](#createdestinationresponse) | 2 |
| [CreateEmailRequest](#createemailrequest) | 15 |
| [CreateEmailResponse](#createemailresponse) | 0 |
| [CreateEmailTemplateRequest](#createemailtemplaterequest) | 4 |
| [CreateEmailTemplateResponse](#createemailtemplateresponse) | 1 |
| [CreateEntityRequest](#createentityrequest) | 8 |
| [CreateEntityResponse](#createentityresponse) | 1 |
| [CreateExpectedBankWireRequest](#createexpectedbankwirerequest) | 8 |
| [CreateExpectedBankWireResponse](#createexpectedbankwireresponse) | 1 |
| [CreateExpectedCODRequest](#createexpectedcodrequest) | 4 |
| [CreateExpectedCODResponse](#createexpectedcodresponse) | 1 |
| [CreateExpectedPaymentRequest](#createexpectedpaymentrequest) | 7 |
| [CreateExpectedPaymentResponse](#createexpectedpaymentresponse) | 1 |
| [CreateExtendedDbSchemaRequest](#createextendeddbschemarequest) | 1 |
| [CreateExtendedDbSchemaResponse](#createextendeddbschemaresponse) | 0 |
| [CreateGuestRequest](#createguestrequest) | 47 |
| [CreateGuestResponse](#createguestresponse) | 1 |
| [CreateItemRequest](#createitemrequest) | 29 |
| [CreateItemResponse](#createitemresponse) | 2 |
| [CreateMailFolderRequest](#createmailfolderrequest) | 3 |
| [CreateMailFolderResponse](#createmailfolderresponse) | 0 |
| [CreateOrderDetailRequest](#createorderdetailrequest) | 58 |
| [CreateOrderDetailResponse](#createorderdetailresponse) | 3 |
| [CreateOrderImportRequest](#createorderimportrequest) | 54 |
| [CreateOrderImportResponse](#createorderimportresponse) | 3 |
| [CreateOrderRequest](#createorderrequest) | 52 |
| [CreateOrderResponse](#createorderresponse) | 26 |
| [CreatePartyRequest](#createpartyrequest) | 22 |
| [CreatePartyResponse](#createpartyresponse) | 1 |
| [CreatePaymentCheckRequest](#createpaymentcheckrequest) | 13 |
| [CreatePaymentCheckResponse](#createpaymentcheckresponse) | 0 |
| [CreatePaymentCreditCardRequest](#createpaymentcreditcardrequest) | 20 |
| [CreatePaymentCreditCardResponse](#createpaymentcreditcardresponse) | 0 |
| [CreatePaymentPointAccountRequest](#createpaymentpointaccountrequest) | 6 |
| [CreatePaymentPointAccountResponse](#createpaymentpointaccountresponse) | 0 |
| [CreatePaymentRequest](#createpaymentrequest) | 18 |
| [CreatePaymentResponse](#createpaymentresponse) | 4 |
| [CreatePaymentWalletRequest](#createpaymentwalletrequest) | 12 |
| [CreatePayoutRequest](#createpayoutrequest) | 2 |
| [CreatePayoutResponse](#createpayoutresponse) | 2 |
| [CreatePointTransactionRequest](#createpointtransactionrequest) | 7 |
| [CreatePointTransactionResponse](#createpointtransactionresponse) | 1 |
| [CreateReleaseRequest](#createreleaserequest) | 1 |
| [CreateReleaseResponse](#createreleaseresponse) | 3 |
| [CreateResourceSetBannerItemRequest](#createresourcesetbanneritemrequest) | 8 |
| [CreateResourceSetBooleanItemRequest](#createresourcesetbooleanitemrequest) | 1 |
| [CreateResourceSetCarouselItemRequest](#createresourcesetcarouselitemrequest) | 2 |
| [CreateResourceSetCultureRequest](#createresourcesetculturerequest) | 2 |
| [CreateResourceSetCultureResponse](#createresourcesetcultureresponse) | 3 |
| [CreateResourceSetDataSetItemRequest](#createresourcesetdatasetitemrequest) | 2 |
| [CreateResourceSetDateItemRequest](#createresourcesetdateitemrequest) | 1 |
| [CreateResourceSetDecimalItemRequest](#createresourcesetdecimalitemrequest) | 1 |
| [CreateResourceSetDropDownItemRequest](#createresourcesetdropdownitemrequest) | 2 |
| [CreateResourceSetEnvironmentRequest](#createresourcesetenvironmentrequest) | 6 |
| [CreateResourceSetEnvironmentResponse](#createresourcesetenvironmentresponse) | 6 |
| [CreateResourceSetGroupRequest](#createresourcesetgrouprequest) | 2 |
| [CreateResourceSetGroupResponse](#createresourcesetgroupresponse) | 3 |
| [CreateResourceSetImageItemRequest](#createresourcesetimageitemrequest) | 1 |
| [CreateResourceSetIntItemRequest](#createresourcesetintitemrequest) | 1 |
| [CreateResourceSetItemResponse](#createresourcesetitemresponse) | 3 |
| [CreateResourceSetRequest](#createresourcesetrequest) | 4 |
| [CreateResourceSetResponse](#createresourcesetresponse) | 5 |
| [CreateResourceSetTextItemRequest](#createresourcesettextitemrequest) | 1 |
| [CreateResourceSetWidgetItemRequest](#createresourcesetwidgetitemrequest) | 3 |
| [CreateSilentLoginCipherRequest](#createsilentlogincipherrequest) | 5 |
| [CreateSilentLoginCipherResponse](#createsilentlogincipherresponse) | 1 |
| [CreateTableFilterSettingsRequest](#createtablefiltersettingsrequest) | 6 |
| [CreateTableFilterSettingsResponse](#createtablefiltersettingsresponse) | 0 |
| [CreateVendorBillRequest](#createvendorbillrequest) | 10 |
| [CreateVendorBillResponse](#createvendorbillresponse) | 1 |
| [CreateWarehouseRequest](#createwarehouserequest) | 8 |
| [CreateWarehouseResponse](#createwarehouseresponse) | 1 |
| [CreateWebCategoryRequest](#createwebcategoryrequest) | 3 |
| [CreateWebCategoryResponse](#createwebcategoryresponse) | 2 |
| [CreditCardAccountResponse](#creditcardaccountresponse) | 13 |
| [CultureCodeItem](#culturecodeitem) | 2 |
| [CustomerBalanceResponse](#customerbalanceresponse) | 3 |
| [CustomerEventField](#customereventfield) | 2 |
| [CustomerEventResponse](#customereventresponse) | 6 |
| [CustomerExtendedResponse](#customerextendedresponse) | 35 |
| [CustomerFilesResponse](#customerfilesresponse) | 4 |
| [CustomerFoldersResponse](#customerfoldersresponse) | 4 |
| [CustomerLeadSocialNetworkRequest](#customerleadsocialnetworkrequest) | 2 |
| [CustomerLeadSocialNetworksResponse](#customerleadsocialnetworksresponse) | 3 |
| [CustomerLeadsResponse](#customerleadsresponse) | 20 |
| [CustomerNotesResponse](#customernotesresponse) | 3 |
| [CustomerResponse](#customerresponse) | 88 |
| [CustomerSocialNetworkRequest](#customersocialnetworkrequest) | 2 |
| [CustomerSocialNetworksResponse](#customersocialnetworksresponse) | 3 |
| [CustomerWallItemResponse](#customerwallitemresponse) | 8 |
| [DateTimeOffset](#datetimeoffset) | 0 |
| [DebitBankAccountOnFileRequest](#debitbankaccountonfilerequest) | 3 |
| [DebitBankAccountRequest](#debitbankaccountrequest) | 17 |
| [DebitBankAccountResponse](#debitbankaccountresponse) | 2 |
| [DeleteBankAccountTypeRequest](#deletebankaccounttyperequest) | 1 |
| [DeleteBankAccountTypeResponse](#deletebankaccounttyperesponse) | 0 |
| [DeleteCalendarItemRequest](#deletecalendaritemrequest) | 3 |
| [DeleteCalendarItemResponse](#deletecalendaritemresponse) | 2 |
| [DeleteCustomerContactRequest](#deletecustomercontactrequest) | 3 |
| [DeleteCustomerContactResponse](#deletecustomercontactresponse) | 3 |
| [DeleteCustomerExtendedRequest](#deletecustomerextendedrequest) | 4 |
| [DeleteCustomerExtendedResponse](#deletecustomerextendedresponse) | 1 |
| [DeleteCustomerFileFolderRequest](#deletecustomerfilefolderrequest) | 4 |
| [DeleteCustomerFileFolderResponse](#deletecustomerfilefolderresponse) | 0 |
| [DeleteCustomerLeadRequest](#deletecustomerleadrequest) | 3 |
| [DeleteCustomerLeadResponse](#deletecustomerleadresponse) | 0 |
| [DeleteCustomerWallItemRequest](#deletecustomerwallitemrequest) | 4 |
| [DeleteCustomerWallItemResponse](#deletecustomerwallitemresponse) | 1 |
| [DeleteDestinationRequest](#deletedestinationrequest) | 1 |
| [DeleteDestinationResponse](#deletedestinationresponse) | 0 |
| [DeleteEmailRequest](#deleteemailrequest) | 3 |
| [DeleteEmailResponse](#deleteemailresponse) | 0 |
| [DeleteEmailTemplateRequest](#deleteemailtemplaterequest) | 3 |
| [DeleteEmailTemplateResponse](#deleteemailtemplateresponse) | 0 |
| [DeleteEntityRequest](#deleteentityrequest) | 2 |
| [DeleteEntityResponse](#deleteentityresponse) | 0 |
| [DeleteMailFolderRequest](#deletemailfolderrequest) | 3 |
| [DeleteMailFolderResponse](#deletemailfolderresponse) | 0 |
| [DeleteOrderDetailRequest](#deleteorderdetailrequest) | 3 |
| [DeleteOrderDetailResponse](#deleteorderdetailresponse) | 0 |
| [DeleteProductFromCategoryRequest](#deleteproductfromcategoryrequest) | 3 |
| [DeleteProductFromCategoryResponse](#deleteproductfromcategoryresponse) | 3 |
| [DeleteQualificationOverrideRequest](#deletequalificationoverriderequest) | 3 |
| [DeleteQualificationOverrideResponse](#deletequalificationoverrideresponse) | 0 |
| [DeleteReleaseRequest](#deletereleaserequest) | 2 |
| [DeleteReleaseResponse](#deletereleaseresponse) | 0 |
| [DeleteResourceSetCultureRequest](#deleteresourcesetculturerequest) | 2 |
| [DeleteResourceSetCultureResponse](#deleteresourcesetcultureresponse) | 0 |
| [DeleteResourceSetEnvironmentRequest](#deleteresourcesetenvironmentrequest) | 2 |
| [DeleteResourceSetEnvironmentResponse](#deleteresourcesetenvironmentresponse) | 0 |
| [DeleteResourceSetGroupRequest](#deleteresourcesetgrouprequest) | 3 |
| [DeleteResourceSetGroupResponse](#deleteresourcesetgroupresponse) | 0 |
| [DeleteResourceSetItemRequest](#deleteresourcesetitemrequest) | 3 |
| [DeleteResourceSetItemResponse](#deleteresourcesetitemresponse) | 0 |
| [DeleteSchemaRequest](#deleteschemarequest) | 1 |
| [DeleteSchemaResponse](#deleteschemaresponse) | 0 |
| [DeleteWebCategoryRequest](#deletewebcategoryrequest) | 2 |
| [DeleteWebCategoryResponse](#deletewebcategoryresponse) | 2 |
| [DepartmentInfo](#departmentinfo) | 2 |
| [DeployReleaseRequest](#deployreleaserequest) | 3 |
| [DeployReleaseResponse](#deployreleaseresponse) | 2 |
| [DequeueCustomerEventsRequest](#dequeuecustomereventsrequest) | 0 |
| [DequeueCustomerEventsResponse](#dequeuecustomereventsresponse) | 1 |
| [Destination](#destination) | 8 |
| [DestinationTestResponse](#destinationtestresponse) | 9 |
| [DestinationTestResponseDetail](#destinationtestresponsedetail) | 4 |
| [DisableDestinationRequest](#disabledestinationrequest) | 1 |
| [DisableDestinationResponse](#disabledestinationresponse) | 0 |
| [DisableFilterGroupRequest](#disablefiltergrouprequest) | 2 |
| [DisableFilterGroupResponse](#disablefiltergroupresponse) | 0 |
| [DisableFilteringRequest](#disablefilteringrequest) | 1 |
| [DisableFilteringResponse](#disablefilteringresponse) | 0 |
| [EditBankAccountTypeRequest](#editbankaccounttyperequest) | 2 |
| [EditBankAccountTypeResponse](#editbankaccounttyperesponse) | 0 |
| [EmailAttachment](#emailattachment) | 3 |
| [EmptyMailFolderRequest](#emptymailfolderrequest) | 3 |
| [EmptyMailFolderResponse](#emptymailfolderresponse) | 0 |
| [EnableDestinationRequest](#enabledestinationrequest) | 1 |
| [EnableDestinationResponse](#enabledestinationresponse) | 0 |
| [EnableFilterGroupRequest](#enablefiltergrouprequest) | 2 |
| [EnableFilterGroupResponse](#enablefiltergroupresponse) | 0 |
| [EnableFilteringRequest](#enablefilteringrequest) | 1 |
| [EnableFilteringResponse](#enablefilteringresponse) | 0 |
| [EnsureMailFoldersRequest](#ensuremailfoldersrequest) | 2 |
| [EnsureMailFoldersResponse](#ensuremailfoldersresponse) | 0 |
| [EntityDataResponse](#entitydataresponse) | 8 |
| [ExpectedPaymentResponse](#expectedpaymentresponse) | 12 |
| [FilterGroup](#filtergroup) | 5 |
| [FireResponderRequest](#fireresponderrequest) | 5 |
| [FireResponderResponse](#fireresponderresponse) | 0 |
| [ForwardedAttachment](#forwardedattachment) | 2 |
| [FundPaymentCardRequest](#fundpaymentcardrequest) | 2 |
| [FundPaymentCardResponse](#fundpaymentcardresponse) | 0 |
| [GetAccountDirectDepositRequest](#getaccountdirectdepositrequest) | 2 |
| [GetAccountDirectDepositResponse](#getaccountdirectdepositresponse) | 14 |
| [GetAdminWhitelistRequest](#getadminwhitelistrequest) | 1 |
| [GetAdminWhitelistResponse](#getadminwhitelistresponse) | 1 |
| [GetAlertSettingsRequest](#getalertsettingsrequest) | 1 |
| [GetAlertSettingsResponse](#getalertsettingsresponse) | 3 |
| [GetApiWhitelistRequest](#getapiwhitelistrequest) | 1 |
| [GetApiWhitelistResponse](#getapiwhitelistresponse) | 1 |
| [GetAutoOrdersRequest](#getautoordersrequest) | 4 |
| [GetAutoOrdersResponse](#getautoordersresponse) | 1 |
| [GetBankAccountTypesRequest](#getbankaccounttypesrequest) | 2 |
| [GetBankAccountTypesResponse](#getbankaccounttypesresponse) | 1 |
| [GetBillAmountsDueRequest](#getbillamountsduerequest) | 9 |
| [GetBillAmountsDueResponse](#getbillamountsdueresponse) | 1 |
| [GetBillPaymentsRequest](#getbillpaymentsrequest) | 3 |
| [GetBillPaymentsResponse](#getbillpaymentsresponse) | 1 |
| [GetBillPayoutQueueRequest](#getbillpayoutqueuerequest) | 7 |
| [GetBillPayoutQueueResponse](#getbillpayoutqueueresponse) | 1 |
| [GetBillsRequest](#getbillsrequest) | 12 |
| [GetBillsResponse](#getbillsresponse) | 1 |
| [GetBinaryPreferenceRequest](#getbinarypreferencerequest) | 2 |
| [GetBinaryPreferenceResponse](#getbinarypreferenceresponse) | 3 |
| [GetCommissionReportRequest](#getcommissionreportrequest) | 4 |
| [GetCommissionReportResponse](#getcommissionreportresponse) | 1 |
| [GetCompanyNewsItemRequest](#getcompanynewsitemrequest) | 1 |
| [GetCompanyNewsItemResponse](#getcompanynewsitemresponse) | 7 |
| [GetCompanyNewsRequest](#getcompanynewsrequest) | 3 |
| [GetCompanyNewsResponse](#getcompanynewsresponse) | 1 |
| [GetCountryRegionsRequest](#getcountryregionsrequest) | 1 |
| [GetCountryRegionsResponse](#getcountryregionsresponse) | 3 |
| [GetCustomReportRequest](#getcustomreportrequest) | 2 |
| [GetCustomReportResponse](#getcustomreportresponse) | 2 |
| [GetCustomerBalancesRequest](#getcustomerbalancesrequest) | 2 |
| [GetCustomerBalancesResponse](#getcustomerbalancesresponse) | 1 |
| [GetCustomerBillingRequest](#getcustomerbillingrequest) | 2 |
| [GetCustomerBillingResponse](#getcustomerbillingresponse) | 8 |
| [GetCustomerExtendedRequest](#getcustomerextendedrequest) | 37 |
| [GetCustomerExtendedResponse](#getcustomerextendedresponse) | 1 |
| [GetCustomerFoldersRequest](#getcustomerfoldersrequest) | 3 |
| [GetCustomerFoldersResponse](#getcustomerfoldersresponse) | 4 |
| [GetCustomerLeadSocialNetworksRequest](#getcustomerleadsocialnetworksrequest) | 3 |
| [GetCustomerLeadSocialNetworksResponse](#getcustomerleadsocialnetworksresponse) | 1 |
| [GetCustomerLeadsRequest](#getcustomerleadsrequest) | 5 |
| [GetCustomerLeadsResponse](#getcustomerleadsresponse) | 1 |
| [GetCustomerNotesRequest](#getcustomernotesrequest) | 2 |
| [GetCustomerNotesResponse](#getcustomernotesresponse) | 1 |
| [GetCustomerSiteRequest](#getcustomersiterequest) | 3 |
| [GetCustomerSiteResponse](#getcustomersiteresponse) | 46 |
| [GetCustomerSocialNetworksRequest](#getcustomersocialnetworksrequest) | 2 |
| [GetCustomerSocialNetworksResponse](#getcustomersocialnetworksresponse) | 1 |
| [GetCustomerWallRequest](#getcustomerwallrequest) | 5 |
| [GetCustomerWallResponse](#getcustomerwallresponse) | 1 |
| [GetCustomersRequest](#getcustomersrequest) | 46 |
| [GetCustomersResponse](#getcustomersresponse) | 2 |
| [GetDestinationTestRequest](#getdestinationtestrequest) | 1 |
| [GetDestinationTestResponse](#getdestinationtestresponse) | 3 |
| [GetDestinationsRequest](#getdestinationsrequest) | 1 |
| [GetDestinationsResponse](#getdestinationsresponse) | 1 |
| [GetDownlineRequest](#getdownlinerequest) | 14 |
| [GetDownlineResponse](#getdownlineresponse) | 2 |
| [GetEmailAttachmentRequest](#getemailattachmentrequest) | 4 |
| [GetEmailAttachmentResponse](#getemailattachmentresponse) | 4 |
| [GetEntityRequest](#getentityrequest) | 2 |
| [GetEntityResponse](#getentityresponse) | 1 |
| [GetExtendedDbSettingsRequest](#getextendeddbsettingsrequest) | 1 |
| [GetExtendedDbSettingsResponse](#getextendeddbsettingsresponse) | 1 |
| [GetFileContentsRequest](#getfilecontentsrequest) | 5 |
| [GetFileContentsResponse](#getfilecontentsresponse) | 1 |
| [GetFilesRequest](#getfilesrequest) | 3 |
| [GetFilesResponse](#getfilesresponse) | 4 |
| [GetFilterGroupRequest](#getfiltergrouprequest) | 2 |
| [GetFilterGroupResponse](#getfiltergroupresponse) | 1 |
| [GetGuestSocialNetworksRequest](#getguestsocialnetworksrequest) | 1 |
| [GetGuestSocialNetworksResponse](#getguestsocialnetworksresponse) | 1 |
| [GetGuestsRequest](#getguestsrequest) | 45 |
| [GetGuestsResponse](#getguestsresponse) | 1 |
| [GetItemCountryRegionRequest](#getitemcountryregionrequest) | 1 |
| [GetItemCountryRegionResponse](#getitemcountryregionresponse) | 1 |
| [GetItemsRequest](#getitemsrequest) | 10 |
| [GetItemsResponse](#getitemsresponse) | 1 |
| [GetLanguagesRequest](#getlanguagesrequest) | 0 |
| [GetLanguagesResponse](#getlanguagesresponse) | 1 |
| [GetLoginSessionRequest](#getloginsessionrequest) | 1 |
| [GetLoginSessionResponse](#getloginsessionresponse) | 4 |
| [GetOrderInvoiceBatchRequest](#getorderinvoicebatchrequest) | 3 |
| [GetOrderInvoiceRequest](#getorderinvoicerequest) | 5 |
| [GetOrderInvoiceResponse](#getorderinvoiceresponse) | 1 |
| [GetOrderTotalsRequest](#getordertotalsrequest) | 2 |
| [GetOrderTotalsResponse](#getordertotalsresponse) | 3 |
| [GetOrdersRequest](#getordersrequest) | 33 |
| [GetOrdersResponse](#getordersresponse) | 2 |
| [GetPartiesRequest](#getpartiesrequest) | 11 |
| [GetPartiesResponse](#getpartiesresponse) | 1 |
| [GetPartyGuestsRequest](#getpartyguestsrequest) | 1 |
| [GetPartyGuestsResponse](#getpartyguestsresponse) | 1 |
| [GetPaymentsRequest](#getpaymentsrequest) | 4 |
| [GetPaymentsResponse](#getpaymentsresponse) | 1 |
| [GetPointAccountRequest](#getpointaccountrequest) | 3 |
| [GetPointAccountResponse](#getpointaccountresponse) | 1 |
| [GetQualificationOverrideResponse](#getqualificationoverrideresponse) | 10 |
| [GetQualificationOverridesRequest](#getqualificationoverridesrequest) | 4 |
| [GetQualitificationOverridesResponse](#getqualitificationoverridesresponse) | 1 |
| [GetRandomMessageRequest](#getrandommessagerequest) | 1 |
| [GetRandomMessageResponse](#getrandommessageresponse) | 2 |
| [GetRankQualificationsRequest](#getrankqualificationsrequest) | 7 |
| [GetRankQualificationsResponse](#getrankqualificationsresponse) | 12 |
| [GetReIndexHistoryRequest](#getreindexhistoryrequest) | 2 |
| [GetReIndexHistoryResponse](#getreindexhistoryresponse) | 1 |
| [GetReIndexSettingsRequest](#getreindexsettingsrequest) | 1 |
| [GetReIndexSettingsResponse](#getreindexsettingsresponse) | 4 |
| [GetRealTimeCommissionDetailRequest](#getrealtimecommissiondetailrequest) | 5 |
| [GetRealTimeCommissionDetailResponse](#getrealtimecommissiondetailresponse) | 1 |
| [GetRealTimeCommissionsRequest](#getrealtimecommissionsrequest) | 2 |
| [GetRealTimeCommissionsResponse](#getrealtimecommissionsresponse) | 1 |
| [GetReleasesRequest](#getreleasesrequest) | 1 |
| [GetReleasesResponse](#getreleasesresponse) | 1 |
| [GetReportRequest](#getreportrequest) | 2 |
| [GetReportResponse](#getreportresponse) | 2 |
| [GetResourceSetCulturesRequest](#getresourcesetculturesrequest) | 3 |
| [GetResourceSetCulturesResponse](#getresourcesetculturesresponse) | 1 |
| [GetResourceSetEnvironmentsRequest](#getresourcesetenvironmentsrequest) | 1 |
| [GetResourceSetEnvironmentsResponse](#getresourcesetenvironmentsresponse) | 1 |
| [GetResourceSetGroupsRequest](#getresourcesetgroupsrequest) | 1 |
| [GetResourceSetGroupsResponse](#getresourcesetgroupsresponse) | 1 |
| [GetResourceSetItemsRequest](#getresourcesetitemsrequest) | 4 |
| [GetResourceSetItemsResponse](#getresourcesetitemsresponse) | 1 |
| [GetResourceSetSubscriptionUpdatesRequest](#getresourcesetsubscriptionupdatesrequest) | 2 |
| [GetResourceSetSubscriptionUpdatesResponse](#getresourcesetsubscriptionupdatesresponse) | 1 |
| [GetResourceSetsRequest](#getresourcesetsrequest) | 1 |
| [GetResourceSetsResponse](#getresourcesetsresponse) | 1 |
| [GetSQLReportRequest](#getsqlreportrequest) | 3 |
| [GetSQLReportResponse](#getsqlreportresponse) | 2 |
| [GetSandboxRequest](#getsandboxrequest) | 1 |
| [GetSandboxResponse](#getsandboxresponse) | 2 |
| [GetSchemaRequest](#getschemarequest) | 1 |
| [GetSchemaResponse](#getschemaresponse) | 1 |
| [GetSessionRequest](#getsessionrequest) | 1 |
| [GetSessionResponse](#getsessionresponse) | 1 |
| [GetShipMethodsRequest](#getshipmethodsrequest) | 4 |
| [GetShipMethodsResponse](#getshipmethodsresponse) | 1 |
| [GetShoppingCartRequest](#getshoppingcartrequest) | 1 |
| [GetShoppingCartResponse](#getshoppingcartresponse) | 3 |
| [GetSubscriptionRequest](#getsubscriptionrequest) | 3 |
| [GetSubscriptionResponse](#getsubscriptionresponse) | 3 |
| [GetSubscriptionsRequest](#getsubscriptionsrequest) | 3 |
| [GetSubscriptionsResponse](#getsubscriptionsresponse) | 1 |
| [GetTableSettingsRequest](#gettablesettingsrequest) | 1 |
| [GetTableSettingsResponse](#gettablesettingsresponse) | 1 |
| [GetUplineRequest](#getuplinerequest) | 7 |
| [GetUplineResponse](#getuplineresponse) | 1 |
| [GetUserPermissionsRequest](#getuserpermissionsrequest) | 1 |
| [GetUserPermissionsResponse](#getuserpermissionsresponse) | 12 |
| [GetVolumesRequest](#getvolumesrequest) | 4 |
| [GetVolumesResponse](#getvolumesresponse) | 1 |
| [GetWarehousesRequest](#getwarehousesrequest) | 0 |
| [GetWarehousesResponse](#getwarehousesresponse) | 1 |
| [GroupOrder](#grouporder) | 3 |
| [GuestResponse](#guestresponse) | 48 |
| [GuestSocialNetworkRequest](#guestsocialnetworkrequest) | 2 |
| [GuestSocialNetworksResponse](#guestsocialnetworksresponse) | 3 |
| [IsEnrollerChildValidateRequest](#isenrollerchildvalidaterequest) | 2 |
| [IsLoginNameAvailableValidateRequest](#isloginnameavailablevalidaterequest) | 1 |
| [IsMatrixChildValidateRequest](#ismatrixchildvalidaterequest) | 2 |
| [IsTaxIDAvailableValidateRequest](#istaxidavailablevalidaterequest) | 3 |
| [IsUniLevelChildValidateRequest](#isunilevelchildvalidaterequest) | 4 |
| [ItemCountryRegionResponse](#itemcountryregionresponse) | 8 |
| [ItemMemberResponse](#itemmemberresponse) | 6 |
| [ItemResponse](#itemresponse) | 59 |
| [KitMember](#kitmember) | 3 |
| [KitMemberItemResponse](#kitmemberitemresponse) | 3 |
| [KitMemberResponse](#kitmemberresponse) | 2 |
| [LanguageResponse](#languageresponse) | 3 |
| [LoginCustomerRequest](#logincustomerrequest) | 4 |
| [LoginCustomerResponse](#logincustomerresponse) | 1 |
| [MaskTypeDataResponse](#masktypedataresponse) | 3 |
| [MergeCustomerRequest](#mergecustomerrequest) | 4 |
| [MergeCustomerResponse](#mergecustomerresponse) | 0 |
| [MoveCustomerFileRequest](#movecustomerfilerequest) | 4 |
| [MoveCustomerFileResponse](#movecustomerfileresponse) | 2 |
| [MoveEmailRequest](#moveemailrequest) | 4 |
| [MoveEmailResponse](#moveemailresponse) | 0 |
| [NodeResponse](#noderesponse) | 216 |
| [OptInEmailRequest](#optinemailrequest) | 1 |
| [OptInEmailResponse](#optinemailresponse) | 1 |
| [OptInPushNotificationRequest](#optinpushnotificationrequest) | 2 |
| [OptInPushNotificationResponse](#optinpushnotificationresponse) | 1 |
| [OptInSmsRequest](#optinsmsrequest) | 3 |
| [OptInSmsResponse](#optinsmsresponse) | 1 |
| [OptOutEmailRequest](#optoutemailrequest) | 1 |
| [OptOutEmailResponse](#optoutemailresponse) | 1 |
| [OptOutPushNotificationRequest](#optoutpushnotificationrequest) | 2 |
| [OptOutPushNotificationResponse](#optoutpushnotificationresponse) | 1 |
| [OptOutSmsRequest](#optoutsmsrequest) | 3 |
| [OptOutSmsResponse](#optoutsmsresponse) | 1 |
| [OrderBatchDetailRequest](#orderbatchdetailrequest) | 8 |
| [OrderDetailIDs](#orderdetailids) | 2 |
| [OrderDetailRequest](#orderdetailrequest) | 24 |
| [OrderDetailResponse](#orderdetailresponse) | 49 |
| [OrderImportDetail](#orderimportdetail) | 29 |
| [OrderResponse](#orderresponse) | 108 |
| [OrderTotalByCurrency](#ordertotalbycurrency) | 3 |
| [ParameterRequest](#parameterrequest) | 2 |
| [PartyAddress](#partyaddress) | 6 |
| [PartyResponse](#partyresponse) | 23 |
| [PaymentResponse](#paymentresponse) | 24 |
| [PaymentsResponse](#paymentsresponse) | 2 |
| [PlaceBinaryNodeRequest](#placebinarynoderequest) | 6 |
| [PlaceBinaryNodeResponse](#placebinarynoderesponse) | 0 |
| [PlaceEnrollerNodeRequest](#placeenrollernoderequest) | 5 |
| [PlaceEnrollerNodeResponse](#placeenrollernoderesponse) | 0 |
| [PlaceMatrixNodeRequest](#placematrixnoderequest) | 8 |
| [PlaceMatrixNodeResponse](#placematrixnoderesponse) | 0 |
| [PlaceStackNodeRequest](#placestacknoderequest) | 5 |
| [PlaceStackNodeResponse](#placestacknoderesponse) | 0 |
| [PlaceUniLevelNodeRequest](#placeunilevelnoderequest) | 8 |
| [PlaceUniLevelNodeResponse](#placeunilevelnoderesponse) | 0 |
| [PointAccount](#pointaccount) | 2 |
| [PropertyDataRequest](#propertydatarequest) | 9 |
| [PropertyDataResponse](#propertydataresponse) | 9 |
| [PropertyDataUpdateRequest](#propertydataupdaterequest) | 4 |
| [QualificationResponse](#qualificationresponse) | 9 |
| [QueueBillPayoutRequest](#queuebillpayoutrequest) | 0 |
| [QueueBillPayoutResponse](#queuebillpayoutresponse) | 1 |
| [ReIndexHistoryItem](#reindexhistoryitem) | 7 |
| [ReIndexSettings](#reindexsettings) | 3 |
| [RefreshSandboxRequest](#refreshsandboxrequest) | 1 |
| [RefreshSandboxResponse](#refreshsandboxresponse) | 1 |
| [RefundPriorCreditCardChargeRequest](#refundpriorcreditcardchargerequest) | 5 |
| [RefundPriorCreditCardChargeResponse](#refundpriorcreditcardchargeresponse) | 2 |
| [RefundPriorDebitChargeRequest](#refundpriordebitchargerequest) | 5 |
| [RefundPriorDebitChargeResponse](#refundpriordebitchargeresponse) | 0 |
| [RefundPriorWalletChargeRequest](#refundpriorwalletchargerequest) | 5 |
| [RefundPriorWalletChargeResponse](#refundpriorwalletchargeresponse) | 2 |
| [RegionResponse](#regionresponse) | 2 |
| [RemoveAdminWhitelistRequest](#removeadminwhitelistrequest) | 1 |
| [RemoveAdminWhitelistResponse](#removeadminwhitelistresponse) | 0 |
| [RemoveApiWhitelistRequest](#removeapiwhitelistrequest) | 1 |
| [RemoveApiWhitelistResponse](#removeapiwhitelistresponse) | 0 |
| [RemovePartyGuestsRequest](#removepartyguestsrequest) | 2 |
| [RemovePartyGuestsResponse](#removepartyguestsresponse) | 0 |
| [ReportParameterRequest](#reportparameterrequest) | 2 |
| [ResourceBanner](#resourcebanner) | 8 |
| [ResourceCarousel](#resourcecarousel) | 2 |
| [ResourceCheckBox](#resourcecheckbox) | 0 |
| [ResourceDataSet](#resourcedataset) | 2 |
| [ResourceDate](#resourcedate) | 0 |
| [ResourceDecimal](#resourcedecimal) | 0 |
| [ResourceDropDown](#resourcedropdown) | 0 |
| [ResourceGroup](#resourcegroup) | 3 |
| [ResourceImage](#resourceimage) | 0 |
| [ResourceItem](#resourceitem) | 12 |
| [ResourceNumber](#resourcenumber) | 0 |
| [ResourceSet](#resourceset) | 7 |
| [ResourceSetCheckInRequest](#resourcesetcheckinrequest) | 7 |
| [ResourceSetCheckInResponse](#resourcesetcheckinresponse) | 6 |
| [ResourceSetCulture](#resourcesetculture) | 3 |
| [ResourceSetEnvironment](#resourcesetenvironment) | 8 |
| [ResourceSetRelease](#resourcesetrelease) | 5 |
| [ResourceSetSubscriptionCheckIn](#resourcesetsubscriptioncheckin) | 7 |
| [ResourceString](#resourcestring) | 0 |
| [ResourceSubscription](#resourcesubscription) | 6 |
| [ResourceSubscriptionUpdate](#resourcesubscriptionupdate) | 2 |
| [ResourceWidget](#resourcewidget) | 3 |
| [RetireResourceSetRequest](#retireresourcesetrequest) | 1 |
| [RetireResourceSetResponse](#retireresourcesetresponse) | 0 |
| [RevertToRecentReleaseRequest](#reverttorecentreleaserequest) | 1 |
| [RevertToRecentReleaseResponse](#reverttorecentreleaseresponse) | 3 |
| [Sandbox](#sandbox) | 12 |
| [SchemaDataResponse](#schemadataresponse) | 2 |
| [SendAuthorizationMFACodeRequest](#sendauthorizationmfacoderequest) | 3 |
| [SendAuthorizationMFACodeResponse](#sendauthorizationmfacoderesponse) | 0 |
| [SendEmailRequest](#sendemailrequest) | 6 |
| [SendEmailResponse](#sendemailresponse) | 0 |
| [SendSmsRequest](#sendsmsrequest) | 4 |
| [SendSmsResponse](#sendsmsresponse) | 0 |
| [SetAccountCheckingRequest](#setaccountcheckingrequest) | 16 |
| [SetAccountCreditCardRequest](#setaccountcreditcardrequest) | 17 |
| [SetAccountCreditCardTokenRequest](#setaccountcreditcardtokenrequest) | 20 |
| [SetAccountDirectDepositRequest](#setaccountdirectdepositrequest) | 16 |
| [SetAccountResponse](#setaccountresponse) | 0 |
| [SetAccountWalletRequest](#setaccountwalletrequest) | 8 |
| [SetBinaryPreferenceRequest](#setbinarypreferencerequest) | 3 |
| [SetBinaryPreferenceResponse](#setbinarypreferenceresponse) | 0 |
| [SetCustomerLeadSocialNetworksRequest](#setcustomerleadsocialnetworksrequest) | 4 |
| [SetCustomerLeadSocialNetworksResponse](#setcustomerleadsocialnetworksresponse) | 0 |
| [SetCustomerSiteImageRequest](#setcustomersiteimagerequest) | 5 |
| [SetCustomerSiteImageResponse](#setcustomersiteimageresponse) | 0 |
| [SetCustomerSiteRequest](#setcustomersiterequest) | 40 |
| [SetCustomerSiteResponse](#setcustomersiteresponse) | 0 |
| [SetCustomerSocialNetworksRequest](#setcustomersocialnetworksrequest) | 3 |
| [SetCustomerSocialNetworksResponse](#setcustomersocialnetworksresponse) | 0 |
| [SetGuestSocialNetworksRequest](#setguestsocialnetworksrequest) | 2 |
| [SetGuestSocialNetworksResponse](#setguestsocialnetworksresponse) | 0 |
| [SetImageFileRequest](#setimagefilerequest) | 3 |
| [SetImageFileResponse](#setimagefileresponse) | 0 |
| [SetItemCountryRegionRequest](#setitemcountryregionrequest) | 9 |
| [SetItemCountryRegionResponse](#setitemcountryregionresponse) | 0 |
| [SetItemImageRequest](#setitemimagerequest) | 7 |
| [SetItemImageResponse](#setitemimageresponse) | 0 |
| [SetItemKitMembersRequest](#setitemkitmembersrequest) | 2 |
| [SetItemKitMembersResponse](#setitemkitmembersresponse) | 0 |
| [SetItemPointAccountRequest](#setitempointaccountrequest) | 3 |
| [SetItemPointAccountResponse](#setitempointaccountresponse) | 0 |
| [SetItemPriceRequest](#setitempricerequest) | 18 |
| [SetItemPriceResponse](#setitempriceresponse) | 0 |
| [SetItemSubscriptionRequest](#setitemsubscriptionrequest) | 3 |
| [SetItemSubscriptionResponse](#setitemsubscriptionresponse) | 0 |
| [SetItemWarehouseRequest](#setitemwarehouserequest) | 6 |
| [SetItemWarehouseResponse](#setitemwarehouseresponse) | 0 |
| [SetQualificationOverrideRequest](#setqualificationoverriderequest) | 8 |
| [SetQualificationOverrideResponse](#setqualificationoverrideresponse) | 0 |
| [SetSessionRequest](#setsessionrequest) | 2 |
| [SetSessionResponse](#setsessionresponse) | 0 |
| [ShipMethodResponse](#shipmethodresponse) | 3 |
| [StartSandboxRequest](#startsandboxrequest) | 6 |
| [StartSandboxResponse](#startsandboxresponse) | 1 |
| [StopSandboxRequest](#stopsandboxrequest) | 1 |
| [StopSandboxResponse](#stopsandboxresponse) | 1 |
| [SubmitDestinationTestRequest](#submitdestinationtestrequest) | 4 |
| [SubmitDestinationTestResponse](#submitdestinationtestresponse) | 1 |
| [Subscription](#subscription) | 2 |
| [SubscriptionResponse](#subscriptionresponse) | 4 |
| [TableFilterSetting](#tablefiltersetting) | 6 |
| [TableName](#tablename) | 2 |
| [TableSettings](#tablesettings) | 5 |
| [TerminateCustomerRequest](#terminatecustomerrequest) | 4 |
| [TerminateCustomerResponse](#terminatecustomerresponse) | 0 |
| [TransactionalRequest](#transactionalrequest) | 1 |
| [TransactionalResponse](#transactionalresponse) | 1 |
| [UpdateAlertSettingsRequest](#updatealertsettingsrequest) | 4 |
| [UpdateAlertSettingsResponse](#updatealertsettingsresponse) | 0 |
| [UpdateAutoOrderDetailRequest](#updateautoorderdetailrequest) | 19 |
| [UpdateAutoOrderDetailResponse](#updateautoorderdetailresponse) | 0 |
| [UpdateAutoOrderRequest](#updateautoorderrequest) | 38 |
| [UpdateAutoOrderResponse](#updateautoorderresponse) | 0 |
| [UpdateBillRequest](#updatebillrequest) | 16 |
| [UpdateBillResponse](#updatebillresponse) | 0 |
| [UpdateCalendarItemRequest](#updatecalendaritemrequest) | 30 |
| [UpdateCalendarItemResponse](#updatecalendaritemresponse) | 2 |
| [UpdateCustomerContactRequest](#updatecustomercontactrequest) | 26 |
| [UpdateCustomerContactResponse](#updatecustomercontactresponse) | 3 |
| [UpdateCustomerExtendedRequest](#updatecustomerextendedrequest) | 34 |
| [UpdateCustomerExtendedResponse](#updatecustomerextendedresponse) | 0 |
| [UpdateCustomerLeadRequest](#updatecustomerleadrequest) | 20 |
| [UpdateCustomerLeadResponse](#updatecustomerleadresponse) | 0 |
| [UpdateCustomerRequest](#updatecustomerrequest) | 87 |
| [UpdateCustomerResponse](#updatecustomerresponse) | 0 |
| [UpdateDestinationRequest](#updatedestinationrequest) | 3 |
| [UpdateDestinationResponse](#updatedestinationresponse) | 0 |
| [UpdateEmailStatusRequest](#updateemailstatusrequest) | 4 |
| [UpdateEmailStatusResponse](#updateemailstatusresponse) | 0 |
| [UpdateEmailTemplateRequest](#updateemailtemplaterequest) | 5 |
| [UpdateEmailTemplateResponse](#updateemailtemplateresponse) | 0 |
| [UpdateEntityRequest](#updateentityrequest) | 11 |
| [UpdateEntityResponse](#updateentityresponse) | 1 |
| [UpdateExtendedDbSettingsRequest](#updateextendeddbsettingsrequest) | 2 |
| [UpdateExtendedDbSettingsResponse](#updateextendeddbsettingsresponse) | 0 |
| [UpdateGuestRequest](#updateguestrequest) | 45 |
| [UpdateGuestResponse](#updateguestresponse) | 0 |
| [UpdateItemRequest](#updateitemrequest) | 37 |
| [UpdateItemResponse](#updateitemresponse) | 0 |
| [UpdateMailFolderRequest](#updatemailfolderrequest) | 4 |
| [UpdateMailFolderResponse](#updatemailfolderresponse) | 0 |
| [UpdateOrderDetailRequest](#updateorderdetailrequest) | 59 |
| [UpdateOrderDetailResponse](#updateorderdetailresponse) | 0 |
| [UpdateOrderRequest](#updateorderrequest) | 125 |
| [UpdateOrderResponse](#updateorderresponse) | 0 |
| [UpdatePartyRequest](#updatepartyrequest) | 23 |
| [UpdatePartyResponse](#updatepartyresponse) | 0 |
| [UpdateReIndexSettingsRequest](#updatereindexsettingsrequest) | 4 |
| [UpdateReIndexSettingsResponse](#updatereindexsettingsresponse) | 0 |
| [UpdateResourceSetBannerItemRequest](#updateresourcesetbanneritemrequest) | 8 |
| [UpdateResourceSetBooleanItemRequest](#updateresourcesetbooleanitemrequest) | 1 |
| [UpdateResourceSetCarouselItemRequest](#updateresourcesetcarouselitemrequest) | 2 |
| [UpdateResourceSetDataSetItemRequest](#updateresourcesetdatasetitemrequest) | 2 |
| [UpdateResourceSetDateItemRequest](#updateresourcesetdateitemrequest) | 1 |
| [UpdateResourceSetDecimalItemRequest](#updateresourcesetdecimalitemrequest) | 1 |
| [UpdateResourceSetDropDownItemRequest](#updateresourcesetdropdownitemrequest) | 2 |
| [UpdateResourceSetEnvironmentRequest](#updateresourcesetenvironmentrequest) | 7 |
| [UpdateResourceSetEnvironmentResponse](#updateresourcesetenvironmentresponse) | 6 |
| [UpdateResourceSetGroupRequest](#updateresourcesetgrouprequest) | 3 |
| [UpdateResourceSetGroupResponse](#updateresourcesetgroupresponse) | 3 |
| [UpdateResourceSetImageItemRequest](#updateresourcesetimageitemrequest) | 0 |
| [UpdateResourceSetIntItemRequest](#updateresourcesetintitemrequest) | 1 |
| [UpdateResourceSetItemResponse](#updateresourcesetitemresponse) | 3 |
| [UpdateResourceSetRequest](#updateresourcesetrequest) | 5 |
| [UpdateResourceSetResponse](#updateresourcesetresponse) | 5 |
| [UpdateResourceSetTextItemRequest](#updateresourcesettextitemrequest) | 1 |
| [UpdateResourceSetWidgetItemRequest](#updateresourcesetwidgetitemrequest) | 3 |
| [UpdateTableFilterSettingsRequest](#updatetablefiltersettingsrequest) | 6 |
| [UpdateTableFilterSettingsResponse](#updatetablefiltersettingsresponse) | 0 |
| [UpdateTableSettingsRequest](#updatetablesettingsrequest) | 5 |
| [UpdateTableSettingsResponse](#updatetablesettingsresponse) | 0 |
| [UpdateWebCategoryRequest](#updatewebcategoryrequest) | 3 |
| [UpdateWebCategoryResponse](#updatewebcategoryresponse) | 3 |
| [ValidateCreditCardTokenRequest](#validatecreditcardtokenrequest) | 32 |
| [ValidateCreditCardTokenResponse](#validatecreditcardtokenresponse) | 4 |
| [ValidateRequest](#validaterequest) | 0 |
| [ValidateResponse](#validateresponse) | 1 |
| [ValidateWalletAccountRequest](#validatewalletaccountrequest) | 32 |
| [ValidateWalletAccountResponse](#validatewalletaccountresponse) | 4 |
| [VerifyAddressRequest](#verifyaddressrequest) | 5 |
| [VerifyAddressResponse](#verifyaddressresponse) | 6 |
| [VoidPaymentsRequest](#voidpaymentsrequest) | 4 |
| [VoidPaymentsResponse](#voidpaymentsresponse) | 0 |
| [VolumeFilter](#volumefilter) | 3 |
| [VolumeResponse](#volumeresponse) | 207 |
| [WalletAccountResponse](#walletaccountresponse) | 5 |
| [WarehouseResponse](#warehouseresponse) | 8 |

### AddBankAccountTypeRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Description` | `string` | 0 | 1 | false |

### AddBankAccountTypeResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `BankAccountTyId` | `int` | 1 | 1 | false |

### AddPartyGuestsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PartyID` | `int` | 1 | 1 | false |
| `GuestIDs` | `ArrayOfInt` | 0 | 1 | false |

### AddPartyGuestsResponse
Extends `ApiResponse`.

_No fields._

### AddProductsToCategoryRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `WebID` | `int` | 1 | 1 | false |
| `CategoryID` | `int` | 1 | 1 | false |
| `ItemCodes` | `ArrayOfString` | 0 | 1 | false |

### AddProductsToCategoryResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CategoryID` | `int` | 1 | 1 | false |
| `WebID` | `int` | 1 | 1 | false |

### AdjustInventoryRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `WarehouseID` | `int` | 1 | 1 | false |
| `ItemCode` | `string` | 0 | 1 | false |
| `Quantity` | `int` | 1 | 1 | false |
| `Notes` | `string` | 0 | 1 | false |

### AdjustInventoryResponse
Extends `ApiResponse`.

_No fields._

### AdminWhitelistResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `IpRangeID` | `int` | 1 | 1 | false |
| `MinIP` | `string` | 0 | 1 | false |
| `MaxIP` | `string` | 0 | 1 | false |

### AdvancedAutoOptionsRequest

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ProcessWhileDate` | `dateTime` | 1 | 1 | true |
| `SkipUntilDate` | `dateTime` | 1 | 1 | true |
| `DetailStartDate` | `dateTime` | 1 | 1 | true |
| `DetailEndDate` | `dateTime` | 1 | 1 | true |
| `DetailInterval` | `int` | 1 | 1 | true |

### AlertSettings

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `AlertOptIn` | `boolean` | 1 | 1 | false |
| `AlertEmail` | `ArrayOfString` | 0 | 1 | false |
| `AlertPhone` | `ArrayOfString` | 0 | 1 | false |

### ApiAuthentication

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `LoginName` | `string` | 0 | 1 | false |
| `Password` | `string` | 0 | 1 | false |
| `Company` | `string` | 0 | 1 | false |
| `Identity` | `string` | 0 | 1 | false |
| `RequestTimeUtc` | `dateTime` | 1 | 1 | false |
| `Signature` | `string` | 0 | 1 | false |

### ApiRequest

_No fields._

### ApiResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Result` | `ApiResult` | 0 | 1 | false |

### ApiResult

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Status` | `ResultStatus` | 1 | 1 | false |
| `Errors` | `ArrayOfString` | 0 | 1 | false |
| `TransactionKey` | `string` | 0 | 1 | false |

### ApiWhitelistResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `IpRangeID` | `int` | 1 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `MinIP` | `string` | 0 | 1 | false |
| `MaxIP` | `string` | 0 | 1 | false |

### AppendCustomerNotesRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Notes` | `string` | 0 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### AppendCustomerNotesResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### ArrayOfAdminWhitelistResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `AdminWhitelistResponse` | `AdminWhitelistResponse` | 0 | unbounded | true |

### ArrayOfApiRequest

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ApiRequest` | `ApiRequest` | 0 | unbounded | true |

### ArrayOfApiResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ApiResponse` | `ApiResponse` | 0 | unbounded | true |

### ArrayOfApiWhitelistResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ApiWhitelistResponse` | `ApiWhitelistResponse` | 0 | unbounded | true |

### ArrayOfArrayOfQualificationResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ArrayOfQualificationResponse` | `ArrayOfQualificationResponse` | 0 | unbounded | true |

### ArrayOfAutoOrderDetailResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `AutoOrderDetailResponse` | `AutoOrderDetailResponse` | 0 | unbounded | true |

### ArrayOfAutoOrderResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `AutoOrderResponse` | `AutoOrderResponse` | 0 | unbounded | true |

### ArrayOfBankAccountTypeResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `BankAccountTypeResponse` | `BankAccountTypeResponse` | 0 | unbounded | true |

### ArrayOfBill

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Bill` | `Bill` | 0 | unbounded | true |

### ArrayOfBillAmount

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `BillAmount` | `BillAmount` | 0 | unbounded | true |

### ArrayOfBillDetail

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `BillDetail` | `BillDetail` | 0 | unbounded | true |

### ArrayOfBillItem

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `BillItem` | `BillItem` | 0 | unbounded | true |

### ArrayOfBillPayment

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `BillPayment` | `BillPayment` | 0 | unbounded | true |

### ArrayOfBillPayoutQueueItem

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `BillPayoutQueueItem` | `BillPayoutQueueItem` | 0 | unbounded | true |

### ArrayOfBillResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `BillResponse` | `BillResponse` | 0 | unbounded | true |

### ArrayOfCommissionBonusResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CommissionBonusResponse` | `CommissionBonusResponse` | 0 | unbounded | true |

### ArrayOfCommissionDetailResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CommissionDetailResponse` | `CommissionDetailResponse` | 0 | unbounded | true |

### ArrayOfCommissionResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CommissionResponse` | `CommissionResponse` | 0 | unbounded | true |

### ArrayOfCompanyNewsResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CompanyNewsResponse` | `CompanyNewsResponse` | 0 | unbounded | true |

### ArrayOfCountryResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CountryResponse` | `CountryResponse` | 0 | unbounded | true |

### ArrayOfCultureCodeItem

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CultureCodeItem` | `CultureCodeItem` | 0 | unbounded | true |

### ArrayOfCustomerBalanceResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerBalanceResponse` | `CustomerBalanceResponse` | 0 | unbounded | true |

### ArrayOfCustomerEventField

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerEventField` | `CustomerEventField` | 0 | unbounded | true |

### ArrayOfCustomerEventResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerEventResponse` | `CustomerEventResponse` | 0 | unbounded | true |

### ArrayOfCustomerExtendedResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerExtendedResponse` | `CustomerExtendedResponse` | 0 | unbounded | true |

### ArrayOfCustomerFilesResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerFilesResponse` | `CustomerFilesResponse` | 0 | unbounded | true |

### ArrayOfCustomerFoldersResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerFoldersResponse` | `CustomerFoldersResponse` | 0 | unbounded | true |

### ArrayOfCustomerLeadSocialNetworkRequest

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerLeadSocialNetworkRequest` | `CustomerLeadSocialNetworkRequest` | 0 | unbounded | true |

### ArrayOfCustomerLeadSocialNetworksResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerLeadSocialNetworksResponse` | `CustomerLeadSocialNetworksResponse` | 0 | unbounded | true |

### ArrayOfCustomerLeadsResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerLeadsResponse` | `CustomerLeadsResponse` | 0 | unbounded | true |

### ArrayOfCustomerNotesResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerNotesResponse` | `CustomerNotesResponse` | 0 | unbounded | true |

### ArrayOfCustomerResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerResponse` | `CustomerResponse` | 0 | unbounded | true |

### ArrayOfCustomerSocialNetworkRequest

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerSocialNetworkRequest` | `CustomerSocialNetworkRequest` | 0 | unbounded | true |

### ArrayOfCustomerSocialNetworksResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerSocialNetworksResponse` | `CustomerSocialNetworksResponse` | 0 | unbounded | true |

### ArrayOfCustomerWallItemResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerWallItemResponse` | `CustomerWallItemResponse` | 0 | unbounded | true |

### ArrayOfDepartmentInfo

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DepartmentInfo` | `DepartmentInfo` | 0 | unbounded | true |

### ArrayOfDestination

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Destination` | `Destination` | 0 | unbounded | true |

### ArrayOfDestinationTestResponseDetail

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DestinationTestResponseDetail` | `DestinationTestResponseDetail` | 0 | unbounded | true |

### ArrayOfEmailAttachment

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `EmailAttachment` | `EmailAttachment` | 0 | unbounded | true |

### ArrayOfEntityDataResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `EntityDataResponse` | `EntityDataResponse` | 0 | unbounded | true |

### ArrayOfExpectedPaymentResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ExpectedPaymentResponse` | `ExpectedPaymentResponse` | 0 | unbounded | true |

### ArrayOfFilterGroup

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `FilterGroup` | `FilterGroup` | 0 | unbounded | true |

### ArrayOfForwardedAttachment

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ForwardedAttachment` | `ForwardedAttachment` | 0 | unbounded | true |

### ArrayOfGetQualificationOverrideResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `GetQualificationOverrideResponse` | `GetQualificationOverrideResponse` | 0 | unbounded | true |

### ArrayOfGroupOrder

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `GroupOrder` | `GroupOrder` | 0 | unbounded | true |

### ArrayOfGuestResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `GuestResponse` | `GuestResponse` | 0 | unbounded | true |

### ArrayOfGuestSocialNetworkRequest

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `GuestSocialNetworkRequest` | `GuestSocialNetworkRequest` | 0 | unbounded | true |

### ArrayOfGuestSocialNetworksResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `GuestSocialNetworksResponse` | `GuestSocialNetworksResponse` | 0 | unbounded | true |

### ArrayOfInt

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `int` | `int` | 0 | unbounded | false |

### ArrayOfItemCountryRegionResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ItemCountryRegionResponse` | `ItemCountryRegionResponse` | 0 | unbounded | true |

### ArrayOfItemMemberResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ItemMemberResponse` | `ItemMemberResponse` | 0 | unbounded | true |

### ArrayOfItemResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ItemResponse` | `ItemResponse` | 0 | unbounded | true |

### ArrayOfKitMember

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `KitMember` | `KitMember` | 0 | unbounded | true |

### ArrayOfKitMemberItemResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `KitMemberItemResponse` | `KitMemberItemResponse` | 0 | unbounded | true |

### ArrayOfKitMemberResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `KitMemberResponse` | `KitMemberResponse` | 0 | unbounded | true |

### ArrayOfLanguageResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `LanguageResponse` | `LanguageResponse` | 0 | unbounded | true |

### ArrayOfNodeResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `NodeResponse` | `NodeResponse` | 0 | unbounded | true |

### ArrayOfOrderBatchDetailRequest

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderBatchDetailRequest` | `OrderBatchDetailRequest` | 0 | unbounded | true |

### ArrayOfOrderDetailIDs

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderDetailIDs` | `OrderDetailIDs` | 0 | unbounded | true |

### ArrayOfOrderDetailRequest

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderDetailRequest` | `OrderDetailRequest` | 0 | unbounded | true |

### ArrayOfOrderDetailResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderDetailResponse` | `OrderDetailResponse` | 0 | unbounded | true |

### ArrayOfOrderImportDetail

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderImportDetail` | `OrderImportDetail` | 0 | unbounded | true |

### ArrayOfOrderResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderResponse` | `OrderResponse` | 0 | unbounded | true |

### ArrayOfOrderStatusType

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderStatusType` | `OrderStatusType` | 0 | unbounded | false |

### ArrayOfOrderTotalByCurrency

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderTotalByCurrency` | `OrderTotalByCurrency` | 0 | unbounded | true |

### ArrayOfOrderType

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderType` | `OrderType` | 0 | unbounded | false |

### ArrayOfParameterRequest

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ParameterRequest` | `ParameterRequest` | 0 | unbounded | true |

### ArrayOfPartyResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PartyResponse` | `PartyResponse` | 0 | unbounded | true |

### ArrayOfPaymentResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PaymentResponse` | `PaymentResponse` | 0 | unbounded | true |

### ArrayOfPaymentsResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PaymentsResponse` | `PaymentsResponse` | 0 | unbounded | true |

### ArrayOfPointAccount

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PointAccount` | `PointAccount` | 0 | unbounded | true |

### ArrayOfPropertyDataRequest

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PropertyDataRequest` | `PropertyDataRequest` | 0 | unbounded | true |

### ArrayOfPropertyDataResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PropertyDataResponse` | `PropertyDataResponse` | 0 | unbounded | true |

### ArrayOfPropertyDataUpdateRequest

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PropertyDataUpdateRequest` | `PropertyDataUpdateRequest` | 0 | unbounded | true |

### ArrayOfQualificationResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `QualificationResponse` | `QualificationResponse` | 0 | unbounded | true |

### ArrayOfReIndexHistoryItem

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ReIndexHistoryItem` | `ReIndexHistoryItem` | 0 | unbounded | true |

### ArrayOfRegionResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `RegionResponse` | `RegionResponse` | 0 | unbounded | true |

### ArrayOfReportParameterRequest

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ReportParameterRequest` | `ReportParameterRequest` | 0 | unbounded | true |

### ArrayOfResourceGroup

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceGroup` | `ResourceGroup` | 0 | unbounded | true |

### ArrayOfResourceItem

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceItem` | `ResourceItem` | 0 | unbounded | true |

### ArrayOfResourceSet

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSet` | `ResourceSet` | 0 | unbounded | true |

### ArrayOfResourceSetCulture

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetCulture` | `ResourceSetCulture` | 0 | unbounded | true |

### ArrayOfResourceSetEnvironment

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetEnvironment` | `ResourceSetEnvironment` | 0 | unbounded | true |

### ArrayOfResourceSetRelease

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetRelease` | `ResourceSetRelease` | 0 | unbounded | true |

### ArrayOfResourceSetSubscriptionCheckIn

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetSubscriptionCheckIn` | `ResourceSetSubscriptionCheckIn` | 0 | unbounded | true |

### ArrayOfResourceSubscriptionUpdate

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSubscriptionUpdate` | `ResourceSubscriptionUpdate` | 0 | unbounded | true |

### ArrayOfSandbox

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Sandbox` | `Sandbox` | 0 | unbounded | true |

### ArrayOfShipMethodResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ShipMethodResponse` | `ShipMethodResponse` | 0 | unbounded | true |

### ArrayOfString

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `string` | `string` | 0 | unbounded | true |

### ArrayOfSubscription

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Subscription` | `Subscription` | 0 | unbounded | true |

### ArrayOfSubscriptionResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SubscriptionResponse` | `SubscriptionResponse` | 0 | unbounded | true |

### ArrayOfTableFilterSetting

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `TableFilterSetting` | `TableFilterSetting` | 0 | unbounded | true |

### ArrayOfTableGroupID

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `TableGroupID` | `TableGroupID` | 0 | unbounded | false |

### ArrayOfTableName

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `TableName` | `TableName` | 0 | unbounded | true |

### ArrayOfTableSettings

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `TableSettings` | `TableSettings` | 0 | unbounded | true |

### ArrayOfVolumeFilter

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `VolumeFilter` | `VolumeFilter` | 0 | unbounded | true |

### ArrayOfVolumeResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `VolumeResponse` | `VolumeResponse` | 0 | unbounded | true |

### ArrayOfWarehouseResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `WarehouseResponse` | `WarehouseResponse` | 0 | unbounded | true |

### AuthenticateCustomerRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `LoginName` | `string` | 0 | 1 | false |
| `Password` | `string` | 0 | 1 | false |

### AuthenticateCustomerResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `FirstName` | `string` | 0 | 1 | false |
| `LastName` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### AuthenticateUserRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `LoginName` | `string` | 0 | 1 | false |
| `Password` | `string` | 0 | 1 | false |

### AuthenticateUserResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `FirstName` | `string` | 0 | 1 | false |
| `LastName` | `string` | 0 | 1 | false |

### AuthorizeOnlyCreditCardResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `AuthorizationCode` | `string` | 0 | 1 | false |
| `MerchantTransactionKey` | `string` | 0 | 1 | false |
| `Message` | `string` | 0 | 1 | false |
| `DisplayMessage` | `string` | 0 | 1 | false |

### AuthorizeOnlyCreditCardTokenOnFileRequest
Extends `BaseAuthorizeOnlyCreditCardTokenRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CreditCardAccountType` | `AccountCreditCardType` | 1 | 1 | false |
| `WarehouseID` | `int` | 1 | 1 | false |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | false |
| `Amount` | `decimal` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### AuthorizeOnlyCreditCardTokenRequest
Extends `BaseAuthorizeOnlyCreditCardTokenRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CreditCardToken` | `string` | 0 | 1 | false |
| `Amount` | `decimal` | 1 | 1 | false |
| `BillingName` | `string` | 0 | 1 | false |
| `BillingAddress` | `string` | 0 | 1 | false |
| `BillingCity` | `string` | 0 | 1 | false |
| `BillingState` | `string` | 0 | 1 | false |
| `BillingZip` | `string` | 0 | 1 | false |
| `BillingCountry` | `string` | 0 | 1 | false |
| `WarehouseID` | `int` | 1 | 1 | false |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | false |
| `CvcCode` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### AutoOrderDetailResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ItemCode` | `string` | 0 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `Quantity` | `decimal` | 1 | 1 | false |
| `PriceEach` | `decimal` | 1 | 1 | false |
| `PriceTotal` | `decimal` | 1 | 1 | false |
| `BusinessVolumeEach` | `decimal` | 1 | 1 | false |
| `BusinesVolume` | `decimal` | 1 | 1 | false |
| `CommissionableVolumeEach` | `decimal` | 1 | 1 | false |
| `CommissionableVolume` | `decimal` | 1 | 1 | false |
| `ParentItemCode` | `string` | 0 | 1 | false |
| `PriceEachOverride` | `decimal` | 1 | 1 | true |
| `TaxableEachOverride` | `decimal` | 1 | 1 | true |
| `ShippingPriceEachOverride` | `decimal` | 1 | 1 | true |
| `BusinessVolumeEachOverride` | `decimal` | 1 | 1 | true |
| `CommissionableVolumeEachOverride` | `decimal` | 1 | 1 | true |
| `Reference1` | `string` | 0 | 1 | false |
| `ProcessWhileDate` | `dateTime` | 1 | 1 | true |
| `SkipUntilDate` | `dateTime` | 1 | 1 | true |
| `DetailStartDate` | `dateTime` | 1 | 1 | true |
| `DetailEndDate` | `dateTime` | 1 | 1 | true |
| `DetailInterval` | `int` | 1 | 1 | true |
| `OrderLine` | `int` | 1 | 1 | false |
| `BusinessVolume` | `decimal` | 1 | 1 | false |
| `AutoOrderDetailID` | `guid` | 1 | 1 | true |
| `ParentAutoOrderDetailID` | `guid` | 1 | 1 | true |

### AutoOrderResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `AutoOrderID` | `int` | 1 | 1 | false |
| `AutoOrderStatus` | `AutoOrderStatusType` | 1 | 1 | false |
| `Frequency` | `FrequencyType` | 1 | 1 | false |
| `StartDate` | `dateTime` | 1 | 1 | false |
| `StopDate` | `dateTime` | 1 | 1 | true |
| `LastRunDate` | `dateTime` | 1 | 1 | false |
| `NextRunDate` | `dateTime` | 1 | 1 | false |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `WarehouseID` | `int` | 1 | 1 | false |
| `ShipMethodID` | `int` | 1 | 1 | false |
| `PaymentType` | `AutoOrderPaymentType` | 1 | 1 | false |
| `ProcessType` | `AutoOrderProcessType` | 1 | 1 | false |
| `FirstName` | `string` | 0 | 1 | false |
| `LastName` | `string` | 0 | 1 | false |
| `Company` | `string` | 0 | 1 | false |
| `Address1` | `string` | 0 | 1 | false |
| `Address2` | `string` | 0 | 1 | false |
| `Address3` | `string` | 0 | 1 | false |
| `City` | `string` | 0 | 1 | false |
| `State` | `string` | 0 | 1 | false |
| `Zip` | `string` | 0 | 1 | false |
| `Country` | `string` | 0 | 1 | false |
| `County` | `string` | 0 | 1 | false |
| `Email` | `string` | 0 | 1 | false |
| `Phone` | `string` | 0 | 1 | false |
| `Notes` | `string` | 0 | 1 | false |
| `Total` | `decimal` | 1 | 1 | false |
| `SubTotal` | `decimal` | 1 | 1 | false |
| `TaxTotal` | `decimal` | 1 | 1 | false |
| `ShippingTotal` | `decimal` | 1 | 1 | false |
| `DiscountTotal` | `decimal` | 1 | 1 | false |
| `BusinessVolumeTotal` | `decimal` | 1 | 1 | false |
| `CommissionableVolumeTotal` | `decimal` | 1 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `Other11` | `string` | 0 | 1 | false |
| `Other12` | `string` | 0 | 1 | false |
| `Other13` | `string` | 0 | 1 | false |
| `Other14` | `string` | 0 | 1 | false |
| `Other15` | `string` | 0 | 1 | false |
| `Other16` | `string` | 0 | 1 | false |
| `Other17` | `string` | 0 | 1 | false |
| `Other18` | `string` | 0 | 1 | false |
| `Other19` | `string` | 0 | 1 | false |
| `Other20` | `string` | 0 | 1 | false |
| `Details` | `ArrayOfAutoOrderDetailResponse` | 0 | 1 | false |
| `ModifiedDate` | `dateTime` | 1 | 1 | false |
| `ModifiedBy` | `string` | 0 | 1 | false |
| `MiddleName` | `string` | 0 | 1 | false |
| `NameSuffix` | `string` | 0 | 1 | false |
| `SpecificDayInterval` | `int` | 1 | 1 | true |
| `CreatedDate` | `dateTime` | 1 | 1 | false |
| `CreatedBy` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `CustomFrequencyTy` | `int` | 1 | 1 | true |

### AutoOrderSkipNextShipmentRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `AutoOrderId` | `int` | 1 | 1 | false |

### AutoOrderSkipNextShipmentResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `NextRunDate` | `dateTime` | 1 | 1 | false |

### BankAccountResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `BankAccountNumberDisplay` | `string` | 0 | 1 | false |
| `BankRoutingNumber` | `string` | 0 | 1 | false |
| `BankName` | `string` | 0 | 1 | false |
| `BankAccountType` | `BankAccountType` | 1 | 1 | false |
| `NameOnAccount` | `string` | 0 | 1 | false |
| `BillingAddress` | `string` | 0 | 1 | false |
| `BillingCity` | `string` | 0 | 1 | false |
| `BillingState` | `string` | 0 | 1 | false |
| `BillingZip` | `string` | 0 | 1 | false |
| `BillingCountry` | `string` | 0 | 1 | false |
| `BillingAddress2` | `string` | 0 | 1 | false |
| `CheckIban` | `string` | 0 | 1 | false |
| `CheckSwiftCode` | `string` | 0 | 1 | false |

### BankAccountTypeResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `BankAccountTyId` | `int` | 1 | 1 | false |
| `Description` | `string` | 0 | 1 | false |

### BaseAuthorizeOnlyCreditCardTokenRequest
Extends `ApiRequest`.

_No fields._

### BaseBillPayoutOperationRequest
Extends `ApiRequest`.

_No fields._

### BaseCalculateOrderRequest
Extends `ApiRequest`.

_No fields._

### BaseCalculateOrderResponse
Extends `ApiResponse`.

_No fields._

### BaseChargeCreditCardRequest
Extends `BaseCreatePaymentCreditCardRequest`.

_No fields._

### BaseChargeWalletAccountRequest
Extends `BaseCreatePaymentRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OtherData1` | `string` | 0 | 1 | false |
| `OtherData2` | `string` | 0 | 1 | false |
| `OtherData3` | `string` | 0 | 1 | false |
| `OtherData4` | `string` | 0 | 1 | false |
| `OtherData5` | `string` | 0 | 1 | false |
| `OtherData6` | `string` | 0 | 1 | false |
| `OtherData7` | `string` | 0 | 1 | false |
| `OtherData8` | `string` | 0 | 1 | false |
| `OtherData9` | `string` | 0 | 1 | false |
| `OtherData10` | `string` | 0 | 1 | false |

### BaseCreateExpectedPaymentRequest
Extends `ApiRequest`.

_No fields._

### BaseCreateExpectedPaymentResponse
Extends `ApiResponse`.

_No fields._

### BaseCreatePaymentCreditCardRequest
Extends `BaseCreatePaymentRequest`.

_No fields._

### BaseCreatePaymentRequest
Extends `ApiRequest`.

_No fields._

### BaseCreatePaymentResponse
Extends `ApiResponse`.

_No fields._

### BaseCreatePayoutRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `BankAccountID` | `int` | 1 | 1 | false |
| `Reference` | `string` | 0 | 1 | false |
| `TransactionNote` | `string` | 0 | 1 | false |
| `PaymentDate` | `dateTime` | 1 | 1 | true |
| `CustomerKey` | `string` | 0 | 1 | false |

### BaseCreateResourceSetItemRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `ResourceName` | `string` | 0 | 1 | false |
| `ResourceType` | `ResourceType` | 1 | 1 | false |
| `CultureCode` | `string` | 0 | 1 | false |
| `ResourceGroupID` | `int` | 1 | 1 | true |
| `Comment` | `string` | 0 | 1 | false |
| `Enabled` | `boolean` | 1 | 1 | false |
| `EnabledStartDate` | `dateTime` | 1 | 1 | true |
| `EnabledEndDate` | `dateTime` | 1 | 1 | true |

### BaseDebitBankAccountRequest
Extends `BaseCreatePaymentRequest`.

_No fields._

### BaseGetOrderInvoiceRequest
Extends `ApiRequest`.

_No fields._

### BaseProcessPayoutRequest
Extends `BaseBillPayoutOperationRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `StartDate` | `dateTime` | 1 | 1 | false |
| `EndDate` | `dateTime` | 1 | 1 | false |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `CountryCode` | `string` | 0 | 1 | false |
| `PayableType` | `int` | 1 | 1 | false |
| `PaymentCardType` | `int` | 1 | 1 | true |
| `Reference` | `string` | 0 | 1 | false |
| `BatchDescription` | `string` | 0 | 1 | false |
| `UseBatchPayout` | `boolean` | 1 | 1 | false |
| `BankAccountID` | `int` | 1 | 1 | true |
| `Fee` | `decimal` | 1 | 1 | true |
| `FeeDescription` | `string` | 0 | 1 | false |
| `StartCheckNumber` | `int` | 1 | 1 | true |
| `CustomerID` | `ArrayOfInt` | 0 | 1 | false |
| `CustomerKey` | `ArrayOfString` | 0 | 1 | false |
| `PaymentDate` | `dateTime` | 1 | 1 | true |
| `MinimumAmount` | `decimal` | 1 | 1 | false |
| `MaximumAmount` | `decimal` | 1 | 1 | true |
| `GroupPaymentByVendor` | `boolean` | 1 | 1 | false |

### BaseUpdateResourceSetItemRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `ResourceName` | `string` | 0 | 1 | false |
| `CultureCode` | `string` | 0 | 1 | false |
| `NewResourceName` | `string` | 0 | 1 | false |
| `NewResourceGroupID` | `int` | 1 | 1 | true |
| `NewComment` | `string` | 0 | 1 | false |
| `NewEnabled` | `boolean` | 1 | 1 | true |
| `NewEnabledStartDate` | `dateTime` | 1 | 1 | true |
| `NewEnabledEndDate` | `dateTime` | 1 | 1 | true |

### Bill

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `IsOtherIncome` | `boolean` | 1 | 1 | false |
| `DueDate` | `dateTime` | 1 | 1 | false |
| `Amount` | `decimal` | 1 | 1 | false |
| `Reference` | `string` | 0 | 1 | false |
| `Notes` | `string` | 0 | 1 | false |
| `BillStatusTypeID` | `int` | 1 | 1 | true |
| `PayableTypeIDOverride` | `int` | 1 | 1 | true |
| `CustomerKey` | `string` | 0 | 1 | false |
| `TaxablePeriodTy` | `int` | 1 | 1 | true |
| `TaxablePeriodID` | `int` | 1 | 1 | true |
| `WarehouseID` | `int` | 1 | 1 | true |

### BillAmount

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `Name` | `string` | 0 | 1 | false |
| `BillDetails` | `ArrayOfBillDetail` | 0 | 1 | false |
| `AmountDue` | `decimal` | 1 | 1 | false |
| `TotalBills` | `int` | 1 | 1 | false |

### BillDetail

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `BillID` | `int` | 1 | 1 | false |
| `AmountDue` | `decimal` | 1 | 1 | false |

### BillItem

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `BillID` | `int` | 1 | 1 | false |
| `BillType` | `int` | 1 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | false |
| `WarehouseID` | `int` | 1 | 1 | false |
| `PeriodID` | `int` | 1 | 1 | false |
| `RunID` | `int` | 1 | 1 | false |
| `StatusType` | `int` | 1 | 1 | false |
| `Reference` | `string` | 0 | 1 | false |
| `Notes` | `string` | 0 | 1 | false |
| `SubTotal` | `decimal` | 1 | 1 | false |
| `Shipping` | `decimal` | 1 | 1 | false |
| `Tax` | `decimal` | 1 | 1 | false |
| `Amount` | `decimal` | 1 | 1 | false |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `DateReceived` | `dateTime` | 1 | 1 | true |
| `DatePaymentDue` | `dateTime` | 1 | 1 | true |
| `DateEntered` | `dateTime` | 1 | 1 | true |
| `CreatedBy` | `string` | 0 | 1 | false |
| `ModifiedBy` | `string` | 0 | 1 | false |
| `ModifiedDate` | `dateTime` | 1 | 1 | true |
| `BillImage` | `string` | 0 | 1 | false |
| `IsOtherIncome` | `boolean` | 1 | 1 | false |
| `SourceType` | `int` | 1 | 1 | false |
| `PayableType` | `int` | 1 | 1 | false |
| `TaxablePeriodType` | `int` | 1 | 1 | false |
| `TaxablePeriodID` | `int` | 1 | 1 | false |

### BillPayment

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `BillItems` | `ArrayOfBillItem` | 0 | 1 | false |
| `PaymentID` | `int` | 1 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | false |
| `PaymentType` | `int` | 1 | 1 | false |
| `PaymentDate` | `dateTime` | 1 | 1 | false |
| `Amount` | `decimal` | 1 | 1 | false |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `BankAccountID` | `int` | 1 | 1 | false |
| `PayeeName` | `string` | 0 | 1 | false |
| `PayeeAddress1` | `string` | 0 | 1 | false |
| `PayeeAddress2` | `string` | 0 | 1 | false |
| `PayeeCity` | `string` | 0 | 1 | false |
| `PayeeState` | `string` | 0 | 1 | false |
| `PayeeZip` | `string` | 0 | 1 | false |
| `PayeeCountry` | `string` | 0 | 1 | false |
| `CheckNumber` | `string` | 0 | 1 | false |
| `CheckDate` | `dateTime` | 1 | 1 | false |
| `ClearedDate` | `dateTime` | 1 | 1 | false |
| `VoidedDate` | `dateTime` | 1 | 1 | false |
| `DeductionType` | `int` | 1 | 1 | false |
| `DeductionNotes` | `string` | 0 | 1 | false |
| `IsTaxable` | `boolean` | 1 | 1 | false |
| `PeriodID` | `int` | 1 | 1 | false |
| `Reference` | `string` | 0 | 1 | false |
| `TransactionDate` | `dateTime` | 1 | 1 | false |
| `ModifiedDate` | `dateTime` | 1 | 1 | false |
| `CreatedBy` | `string` | 0 | 1 | false |
| `ModifiedBy` | `string` | 0 | 1 | false |
| `PayeeCompany` | `string` | 0 | 1 | false |
| `DepositNumber` | `string` | 0 | 1 | false |
| `Other1` | `string` | 0 | 1 | false |
| `Other2` | `string` | 0 | 1 | false |
| `Other3` | `string` | 0 | 1 | false |
| `Other4` | `string` | 0 | 1 | false |

### BillPayoutQueueItem

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PayoutQueueRequestID` | `guid` | 1 | 1 | false |
| `Count` | `int` | 1 | 1 | false |
| `Amount` | `decimal` | 1 | 1 | false |
| `MinimumAmount` | `decimal` | 1 | 1 | false |
| `MaximumAmount` | `decimal` | 1 | 1 | false |
| `CountryCode` | `string` | 0 | 1 | false |
| `Fee` | `decimal` | 1 | 1 | false |
| `FeeDescription` | `string` | 0 | 1 | false |
| `PayableType` | `int` | 1 | 1 | false |
| `PaymentCardType` | `int` | 1 | 1 | false |
| `StartCheckNumber` | `int` | 1 | 1 | false |
| `EndCheckNumber` | `int` | 1 | 1 | false |
| `StartDate` | `dateTime` | 1 | 1 | false |
| `EndDate` | `dateTime` | 1 | 1 | false |
| `StartPaymentID` | `int` | 1 | 1 | false |
| `EndPaymentID` | `int` | 1 | 1 | false |
| `PaymentDate` | `dateTime` | 1 | 1 | false |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `BankAccountID` | `int` | 1 | 1 | false |
| `Reference` | `string` | 0 | 1 | false |
| `RequestByUserID` | `int` | 1 | 1 | false |
| `RequestDate` | `dateTime` | 1 | 1 | false |
| `RequestCompleteDate` | `dateTime` | 1 | 1 | false |
| `BatchDescription` | `string` | 0 | 1 | false |
| `UseBatchPayout` | `boolean` | 1 | 1 | false |
| `StatusType` | `PayoutQueueStatusType` | 1 | 1 | false |

### BillResponse
Extends `Bill`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `BillID` | `int` | 1 | 1 | true |
| `Errors` | `ArrayOfString` | 0 | 1 | false |

### CalculateOrderRequest
Extends `BaseCalculateOrderRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CurrencyCode` | `string` | 0 | 1 | false |
| `WarehouseID` | `int` | 1 | 1 | false |
| `ShipMethodID` | `int` | 1 | 1 | false |
| `PriceType` | `int` | 1 | 1 | false |
| `Address1` | `string` | 0 | 1 | false |
| `Address2` | `string` | 0 | 1 | false |
| `Address3` | `string` | 0 | 1 | false |
| `City` | `string` | 0 | 1 | false |
| `State` | `string` | 0 | 1 | false |
| `Zip` | `string` | 0 | 1 | false |
| `Country` | `string` | 0 | 1 | false |
| `County` | `string` | 0 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | false |
| `TaxRateOverride` | `decimal` | 1 | 1 | true |
| `ShippingAmountOverride` | `decimal` | 1 | 1 | true |
| `ReturnOrderID` | `int` | 1 | 1 | true |
| `Other11` | `string` | 0 | 1 | false |
| `Other12` | `string` | 0 | 1 | false |
| `Other13` | `string` | 0 | 1 | false |
| `Other14` | `string` | 0 | 1 | false |
| `Other15` | `string` | 0 | 1 | false |
| `Other16` | `string` | 0 | 1 | false |
| `Other17` | `string` | 0 | 1 | false |
| `Other18` | `string` | 0 | 1 | false |
| `Other19` | `string` | 0 | 1 | false |
| `Other20` | `string` | 0 | 1 | false |
| `Details` | `ArrayOfOrderDetailRequest` | 0 | 1 | false |
| `ReturnShipMethods` | `boolean` | 1 | 1 | false |
| `PartyID` | `int` | 1 | 1 | true |
| `ReturnTrace` | `boolean` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `ReturnOrderKey` | `string` | 0 | 1 | false |
| `OrderID` | `int` | 1 | 1 | false |
| `OrderType` | `OrderType` | 1 | 1 | false |
| `OrderSubStatusTy` | `int` | 1 | 1 | true |
| `AutoOrderId` | `int` | 1 | 1 | true |
| `ReplacementOrderId` | `int` | 1 | 1 | true |
| `DeclineCount` | `int` | 1 | 1 | false |
| `IsRMA` | `boolean` | 1 | 1 | false |
| `BackOrderFromId` | `int` | 1 | 1 | true |
| `IsCommissionable` | `boolean` | 1 | 1 | false |
| `Flag1` | `boolean` | 1 | 1 | false |
| `Flag2` | `boolean` | 1 | 1 | false |
| `Flag3` | `boolean` | 1 | 1 | false |
| `ReturnCategoryId` | `int` | 1 | 1 | true |
| `ReplacementCategoryId` | `int` | 1 | 1 | true |

### CalculateOrderResponse
Extends `BaseCalculateOrderResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Total` | `decimal` | 1 | 1 | false |
| `SubTotal` | `decimal` | 1 | 1 | false |
| `TaxTotal` | `decimal` | 1 | 1 | false |
| `ShippingTotal` | `decimal` | 1 | 1 | false |
| `DiscountTotal` | `decimal` | 1 | 1 | false |
| `DiscountPercent` | `decimal` | 1 | 1 | false |
| `WeightTotal` | `decimal` | 1 | 1 | false |
| `BusinessVolumeTotal` | `decimal` | 1 | 1 | false |
| `CommissionableVolumeTotal` | `decimal` | 1 | 1 | false |
| `Other1Total` | `decimal` | 1 | 1 | false |
| `Other2Total` | `decimal` | 1 | 1 | false |
| `Other3Total` | `decimal` | 1 | 1 | false |
| `Other4Total` | `decimal` | 1 | 1 | false |
| `Other5Total` | `decimal` | 1 | 1 | false |
| `Other6Total` | `decimal` | 1 | 1 | false |
| `Other7Total` | `decimal` | 1 | 1 | false |
| `Other8Total` | `decimal` | 1 | 1 | false |
| `Other9Total` | `decimal` | 1 | 1 | false |
| `Other10Total` | `decimal` | 1 | 1 | false |
| `Other11` | `string` | 0 | 1 | false |
| `Other12` | `string` | 0 | 1 | false |
| `Other13` | `string` | 0 | 1 | false |
| `Other14` | `string` | 0 | 1 | false |
| `Other15` | `string` | 0 | 1 | false |
| `Other16` | `string` | 0 | 1 | false |
| `Other17` | `string` | 0 | 1 | false |
| `Other18` | `string` | 0 | 1 | false |
| `Other19` | `string` | 0 | 1 | false |
| `Other20` | `string` | 0 | 1 | false |
| `ShippingTax` | `decimal` | 1 | 1 | false |
| `OrderTax` | `decimal` | 1 | 1 | false |
| `FedTaxTotal` | `decimal` | 1 | 1 | false |
| `StateTaxTotal` | `decimal` | 1 | 1 | false |
| `Details` | `ArrayOfOrderDetailResponse` | 0 | 1 | false |
| `ShipMethods` | `ArrayOfShipMethodResponse` | 0 | 1 | false |
| `Warnings` | `ArrayOfString` | 0 | 1 | false |
| `Trace` | `string` | 0 | 1 | false |
| `HandlingFeeTotal` | `decimal` | 1 | 1 | false |
| `AutoOrderId` | `int` | 1 | 1 | true |
| `ReplacementOrderId` | `int` | 1 | 1 | true |
| `DeclineCount` | `int` | 1 | 1 | false |
| `IsRMA` | `boolean` | 1 | 1 | false |
| `BackOrderFromId` | `int` | 1 | 1 | true |
| `IsCommissionable` | `boolean` | 1 | 1 | false |
| `Flag1` | `boolean` | 1 | 1 | false |
| `Flag2` | `boolean` | 1 | 1 | false |
| `Flag3` | `boolean` | 1 | 1 | false |
| `ReturnCategoryId` | `int` | 1 | 1 | true |
| `ReplacementCategoryId` | `int` | 1 | 1 | true |

### ChangeAutoOrderStatusRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `AutoOrderID` | `int` | 1 | 1 | false |
| `AutoOrderStatus` | `AutoOrderStatusType` | 1 | 1 | false |

### ChangeAutoOrderStatusResponse
Extends `ApiResponse`.

_No fields._

### ChangeOrderStatusBatchRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderStatus` | `OrderStatusType` | 1 | 1 | false |
| `Details` | `ArrayOfOrderBatchDetailRequest` | 0 | 1 | false |
| `OrderStatusTy` | `string` | 0 | 1 | false |

### ChangeOrderStatusBatchResponse
Extends `ApiResponse`.

_No fields._

### ChangeOrderStatusRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderID` | `int` | 1 | 1 | false |
| `OrderStatus` | `OrderStatusType` | 1 | 1 | false |
| `OrderKey` | `string` | 0 | 1 | false |
| `OrderSubStatusTy` | `int` | 1 | 1 | true |

### ChangeOrderStatusResponse
Extends `ApiResponse`.

_No fields._

### ChargeCreditCardOnFileRequest
Extends `BaseChargeCreditCardRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CreditCardAccountType` | `AccountCreditCardType` | 1 | 1 | false |
| `OrderID` | `int` | 1 | 1 | false |
| `MaxAmount` | `decimal` | 1 | 1 | true |
| `OrderKey` | `string` | 0 | 1 | false |

### ChargeCreditCardRequest
Extends `BaseChargeCreditCardRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CreditCardNumber` | `string` | 0 | 1 | false |
| `ExpirationMonth` | `int` | 1 | 1 | false |
| `ExpirationYear` | `int` | 1 | 1 | false |
| `BillingName` | `string` | 0 | 1 | false |
| `BillingAddress` | `string` | 0 | 1 | false |
| `BillingAddress2` | `string` | 0 | 1 | false |
| `BillingCity` | `string` | 0 | 1 | false |
| `BillingState` | `string` | 0 | 1 | false |
| `BillingZip` | `string` | 0 | 1 | false |
| `BillingCountry` | `string` | 0 | 1 | false |
| `CvcCode` | `string` | 0 | 1 | false |
| `IssueNumber` | `string` | 0 | 1 | false |
| `CreditCardType` | `int` | 1 | 1 | true |
| `OrderID` | `int` | 1 | 1 | false |
| `MaxAmount` | `decimal` | 1 | 1 | true |
| `OrderKey` | `string` | 0 | 1 | false |

### ChargeCreditCardResponse
Extends `CreatePaymentCreditCardResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Amount` | `decimal` | 1 | 1 | false |
| `AuthorizationCode` | `string` | 0 | 1 | false |

### ChargeCreditCardTokenOnFileRequest
Extends `BaseChargeCreditCardRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CreditCardAccountType` | `AccountCreditCardType` | 1 | 1 | false |
| `OrderID` | `int` | 1 | 1 | false |
| `CvcCode` | `string` | 0 | 1 | false |
| `MaxAmount` | `decimal` | 1 | 1 | true |
| `MerchantWarehouseIDOverride` | `int` | 1 | 1 | true |
| `ClientIPAddress` | `string` | 0 | 1 | false |
| `OtherData1` | `string` | 0 | 1 | false |
| `OtherData2` | `string` | 0 | 1 | false |
| `OtherData3` | `string` | 0 | 1 | false |
| `OtherData4` | `string` | 0 | 1 | false |
| `OtherData5` | `string` | 0 | 1 | false |
| `OtherData6` | `string` | 0 | 1 | false |
| `OtherData7` | `string` | 0 | 1 | false |
| `OtherData8` | `string` | 0 | 1 | false |
| `OtherData9` | `string` | 0 | 1 | false |
| `OtherData10` | `string` | 0 | 1 | false |
| `OrderKey` | `string` | 0 | 1 | false |

### ChargeCreditCardTokenRequest
Extends `BaseChargeCreditCardRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CreditCardToken` | `string` | 0 | 1 | false |
| `BillingName` | `string` | 0 | 1 | false |
| `BillingAddress` | `string` | 0 | 1 | false |
| `BillingAddress2` | `string` | 0 | 1 | false |
| `BillingCity` | `string` | 0 | 1 | false |
| `BillingState` | `string` | 0 | 1 | false |
| `BillingZip` | `string` | 0 | 1 | false |
| `BillingCountry` | `string` | 0 | 1 | false |
| `CvcCode` | `string` | 0 | 1 | false |
| `IssueNumber` | `string` | 0 | 1 | false |
| `CreditCardType` | `int` | 1 | 1 | true |
| `ExpirationMonth` | `int` | 1 | 1 | true |
| `ExpirationYear` | `int` | 1 | 1 | true |
| `OrderID` | `int` | 1 | 1 | false |
| `MaxAmount` | `decimal` | 1 | 1 | true |
| `MerchantWarehouseIDOverride` | `int` | 1 | 1 | true |
| `ClientIPAddress` | `string` | 0 | 1 | false |
| `OtherData1` | `string` | 0 | 1 | false |
| `OtherData2` | `string` | 0 | 1 | false |
| `OtherData3` | `string` | 0 | 1 | false |
| `OtherData4` | `string` | 0 | 1 | false |
| `OtherData5` | `string` | 0 | 1 | false |
| `OtherData6` | `string` | 0 | 1 | false |
| `OtherData7` | `string` | 0 | 1 | false |
| `OtherData8` | `string` | 0 | 1 | false |
| `OtherData9` | `string` | 0 | 1 | false |
| `OtherData10` | `string` | 0 | 1 | false |
| `OrderKey` | `string` | 0 | 1 | false |
| `Phone` | `string` | 0 | 1 | false |
| `Email` | `string` | 0 | 1 | false |

### ChargeGroupOrderCreditCardTokenRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `_orders` | `ArrayOfGroupOrder` | 0 | 1 | false |
| `CreditCardToken` | `string` | 0 | 1 | false |
| `BillingName` | `string` | 0 | 1 | false |
| `BillingAddress` | `string` | 0 | 1 | false |
| `BillingAddress2` | `string` | 0 | 1 | false |
| `BillingCity` | `string` | 0 | 1 | false |
| `BillingState` | `string` | 0 | 1 | false |
| `BillingZip` | `string` | 0 | 1 | false |
| `BillingCountry` | `string` | 0 | 1 | false |
| `CvcCode` | `string` | 0 | 1 | false |
| `IssueNumber` | `string` | 0 | 1 | false |
| `CreditCardType` | `int` | 1 | 1 | true |
| `MasterOrderID` | `int` | 1 | 1 | false |
| `Orders` | `ArrayOfGroupOrder` | 0 | 1 | false |
| `MerchantWarehouseIDOverride` | `int` | 1 | 1 | true |
| `ClientIPAddress` | `string` | 0 | 1 | false |
| `OtherData1` | `string` | 0 | 1 | false |
| `OtherData2` | `string` | 0 | 1 | false |
| `OtherData3` | `string` | 0 | 1 | false |
| `OtherData4` | `string` | 0 | 1 | false |
| `OtherData5` | `string` | 0 | 1 | false |
| `OtherData6` | `string` | 0 | 1 | false |
| `OtherData7` | `string` | 0 | 1 | false |
| `OtherData8` | `string` | 0 | 1 | false |
| `OtherData9` | `string` | 0 | 1 | false |
| `OtherData10` | `string` | 0 | 1 | false |
| `PaymentMemo` | `string` | 0 | 1 | false |
| `MasterOrderKey` | `string` | 0 | 1 | false |

### ChargeGroupOrderCreditCardTokenResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `_paymentIDs` | `ArrayOfPaymentsResponse` | 0 | 1 | false |
| `Amount` | `decimal` | 1 | 1 | false |
| `AuthorizationCode` | `string` | 0 | 1 | false |
| `Payments` | `ArrayOfPaymentsResponse` | 0 | 1 | false |

### ChargePriorAuthorizationRequest
Extends `BaseCreatePaymentRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `MerchantTransactionKey` | `string` | 0 | 1 | false |
| `OrderID` | `int` | 1 | 1 | false |
| `MaxAmount` | `decimal` | 1 | 1 | true |
| `OrderKey` | `string` | 0 | 1 | false |

### ChargeWalletAccountOnFileRequest
Extends `BaseCreatePaymentRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `WalletAccountType` | `AccountWalletType` | 1 | 1 | false |
| `OrderID` | `int` | 1 | 1 | false |
| `Memo` | `string` | 0 | 1 | false |
| `MaxAmount` | `decimal` | 1 | 1 | true |
| `OrderKey` | `string` | 0 | 1 | false |
| `OtherData1` | `string` | 0 | 1 | false |
| `OtherData2` | `string` | 0 | 1 | false |
| `OtherData3` | `string` | 0 | 1 | false |
| `OtherData4` | `string` | 0 | 1 | false |
| `OtherData5` | `string` | 0 | 1 | false |
| `OtherData6` | `string` | 0 | 1 | false |
| `OtherData7` | `string` | 0 | 1 | false |
| `OtherData8` | `string` | 0 | 1 | false |
| `OtherData9` | `string` | 0 | 1 | false |
| `OtherData10` | `string` | 0 | 1 | false |

### ChargeWalletAccountRequest
Extends `BaseChargeWalletAccountRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `WalletAccountNumber` | `string` | 0 | 1 | false |
| `WalletTy` | `int` | 1 | 1 | false |
| `OrderID` | `int` | 1 | 1 | false |
| `Memo` | `string` | 0 | 1 | false |
| `MaxAmount` | `decimal` | 1 | 1 | true |
| `OrderKey` | `string` | 0 | 1 | false |

### ChargeWalletAccountResponse
Extends `CreatePaymentResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Amount` | `decimal` | 1 | 1 | false |
| `AuthorizationCode` | `string` | 0 | 1 | false |

### CommissionBonusResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Description` | `string` | 0 | 1 | false |
| `Amount` | `decimal` | 1 | 1 | false |
| `BonusID` | `int` | 1 | 1 | false |

### CommissionDetailResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `FromCustomerID` | `int` | 1 | 1 | false |
| `FromCustomerName` | `string` | 0 | 1 | false |
| `OrderID` | `int` | 1 | 1 | false |
| `Level` | `int` | 1 | 1 | false |
| `PaidLevel` | `int` | 1 | 1 | false |
| `SourceAmount` | `decimal` | 1 | 1 | false |
| `Percentage` | `decimal` | 1 | 1 | false |
| `CommissionAmount` | `decimal` | 1 | 1 | false |
| `FromCustomerKey` | `string` | 0 | 1 | false |
| `OrderKey` | `string` | 0 | 1 | false |

### CommissionResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `PeriodType` | `int` | 1 | 1 | false |
| `PeriodID` | `int` | 1 | 1 | false |
| `PeriodDescription` | `string` | 0 | 1 | false |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `CommissionTotal` | `decimal` | 1 | 1 | false |
| `Bonuses` | `ArrayOfCommissionBonusResponse` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### CompanyNewsResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Description` | `string` | 0 | 1 | false |
| `NewsID` | `int` | 1 | 1 | false |
| `CreatedDate` | `dateTime` | 1 | 1 | false |
| `WebSettings` | `NewsWebSettings` | 1 | 1 | false |
| `CompanySettings` | `NewsCompanySettings` | 1 | 1 | false |

### CountryResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CountryCode` | `string` | 0 | 1 | false |
| `CountryName` | `string` | 0 | 1 | false |

### CreateAdminWhitelistRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Description` | `string` | 0 | 1 | false |
| `MinIP` | `string` | 0 | 1 | false |
| `MaxIP` | `string` | 0 | 1 | false |

### CreateAdminWhitelistResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `IPRangeID` | `int` | 1 | 1 | false |

### CreateApiWhitelistRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Description` | `string` | 0 | 1 | false |
| `MinIP` | `string` | 0 | 1 | false |
| `MaxIP` | `string` | 0 | 1 | false |

### CreateApiWhitelistResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `IPRangeID` | `int` | 1 | 1 | false |

### CreateAutoOrderRequest
Extends `BaseCalculateOrderRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `Frequency` | `FrequencyType` | 1 | 1 | false |
| `StartDate` | `dateTime` | 1 | 1 | false |
| `StopDate` | `dateTime` | 1 | 1 | true |
| `SpecificDayInterval` | `int` | 1 | 1 | true |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `WarehouseID` | `int` | 1 | 1 | false |
| `ShipMethodID` | `int` | 1 | 1 | false |
| `PriceType` | `int` | 1 | 1 | false |
| `PaymentType` | `AutoOrderPaymentType` | 1 | 1 | false |
| `ProcessType` | `AutoOrderProcessType` | 1 | 1 | true |
| `FirstName` | `string` | 0 | 1 | false |
| `MiddleName` | `string` | 0 | 1 | false |
| `LastName` | `string` | 0 | 1 | false |
| `NameSuffix` | `string` | 0 | 1 | false |
| `Company` | `string` | 0 | 1 | false |
| `Address1` | `string` | 0 | 1 | false |
| `Address2` | `string` | 0 | 1 | false |
| `Address3` | `string` | 0 | 1 | false |
| `City` | `string` | 0 | 1 | false |
| `State` | `string` | 0 | 1 | false |
| `Zip` | `string` | 0 | 1 | false |
| `Country` | `string` | 0 | 1 | false |
| `County` | `string` | 0 | 1 | false |
| `Email` | `string` | 0 | 1 | false |
| `Phone` | `string` | 0 | 1 | false |
| `Notes` | `string` | 0 | 1 | false |
| `Other11` | `string` | 0 | 1 | false |
| `Other12` | `string` | 0 | 1 | false |
| `Other13` | `string` | 0 | 1 | false |
| `Other14` | `string` | 0 | 1 | false |
| `Other15` | `string` | 0 | 1 | false |
| `Other16` | `string` | 0 | 1 | false |
| `Other17` | `string` | 0 | 1 | false |
| `Other18` | `string` | 0 | 1 | false |
| `Other19` | `string` | 0 | 1 | false |
| `Other20` | `string` | 0 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `OverwriteExistingAutoOrder` | `boolean` | 1 | 1 | false |
| `ExistingAutoOrderID` | `int` | 1 | 1 | false |
| `Details` | `ArrayOfOrderDetailRequest` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `CustomFrequencyTy` | `int` | 1 | 1 | true |

### CreateAutoOrderResponse
Extends `BaseCalculateOrderResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `AutoOrderID` | `int` | 1 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `Total` | `decimal` | 1 | 1 | false |
| `SubTotal` | `decimal` | 1 | 1 | false |
| `TaxTotal` | `decimal` | 1 | 1 | false |
| `ShippingTotal` | `decimal` | 1 | 1 | false |
| `DiscountTotal` | `decimal` | 1 | 1 | false |
| `WeightTotal` | `decimal` | 1 | 1 | false |
| `BusinessVolumeTotal` | `decimal` | 1 | 1 | false |
| `CommissionableVolumeTotal` | `decimal` | 1 | 1 | false |
| `Other1Total` | `decimal` | 1 | 1 | false |
| `Other2Total` | `decimal` | 1 | 1 | false |
| `Other3Total` | `decimal` | 1 | 1 | false |
| `Other4Total` | `decimal` | 1 | 1 | false |
| `Other5Total` | `decimal` | 1 | 1 | false |
| `Other6Total` | `decimal` | 1 | 1 | false |
| `Other7Total` | `decimal` | 1 | 1 | false |
| `Other8Total` | `decimal` | 1 | 1 | false |
| `Other9Total` | `decimal` | 1 | 1 | false |
| `Other10Total` | `decimal` | 1 | 1 | false |
| `ShippingTax` | `decimal` | 1 | 1 | false |
| `OrderTax` | `decimal` | 1 | 1 | false |
| `Details` | `ArrayOfOrderDetailResponse` | 0 | 1 | false |

### CreateBillPayoutRequest
Extends `BaseProcessPayoutRequest`.

_No fields._

### CreateBillPayoutResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `StartCheckNumber` | `int` | 1 | 1 | false |
| `EndCheckNumber` | `int` | 1 | 1 | false |
| `StartPaymentID` | `int` | 1 | 1 | false |
| `EndPaymentID` | `int` | 1 | 1 | false |
| `PayoutTotal` | `decimal` | 1 | 1 | false |

### CreateBillRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `IsOtherIncome` | `boolean` | 1 | 1 | false |
| `DueDate` | `dateTime` | 1 | 1 | false |
| `Amount` | `decimal` | 1 | 1 | false |
| `Reference` | `string` | 0 | 1 | false |
| `Notes` | `string` | 0 | 1 | false |
| `BillStatusTypeID` | `int` | 1 | 1 | true |
| `PayableTypeIDOverride` | `int` | 1 | 1 | true |
| `CustomerKey` | `string` | 0 | 1 | false |
| `TaxablePeriodTy` | `int` | 1 | 1 | true |
| `TaxablePeriodID` | `int` | 1 | 1 | true |
| `WarehouseID` | `int` | 1 | 1 | true |

### CreateBillResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `BillID` | `int` | 1 | 1 | false |

### CreateBillsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Bills` | `ArrayOfBill` | 0 | 1 | false |

### CreateBillsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Bills` | `ArrayOfBillResponse` | 0 | 1 | false |

### CreateCalendarItemRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `UserID` | `int` | 1 | 1 | false |
| `CalendarID` | `int` | 1 | 1 | false |
| `CalendarItemType` | `CalendarItemType` | 1 | 1 | false |
| `CalendarItemStatusType` | `CalendarItemStatusType` | 1 | 1 | false |
| `CalendarItemPriorityType` | `CalendarItemPriorityType` | 1 | 1 | false |
| `Subject` | `string` | 0 | 1 | false |
| `Location` | `string` | 0 | 1 | false |
| `Notes` | `string` | 0 | 1 | false |
| `StartDate` | `dateTime` | 1 | 1 | false |
| `EndDate` | `dateTime` | 1 | 1 | false |
| `TimeZone` | `int` | 1 | 1 | false |
| `Address1` | `string` | 0 | 1 | false |
| `Address2` | `string` | 0 | 1 | false |
| `City` | `string` | 0 | 1 | false |
| `State` | `string` | 0 | 1 | false |
| `Country` | `string` | 0 | 1 | false |
| `PostalCode` | `string` | 0 | 1 | false |
| `ContactInfo` | `string` | 0 | 1 | false |
| `ContactPhone` | `string` | 0 | 1 | false |
| `ContactPhoneType` | `ContactPhoneType` | 1 | 1 | false |
| `ContactEmail` | `string` | 0 | 1 | false |
| `EventHost` | `string` | 0 | 1 | false |
| `SpecialGuests` | `string` | 0 | 1 | false |
| `EventFlyer` | `string` | 0 | 1 | false |
| `EventCostInfo` | `string` | 0 | 1 | false |
| `EventConferenceCallOrWebinar` | `string` | 0 | 1 | false |
| `EventRegistrationInfo` | `string` | 0 | 1 | false |
| `EventTags` | `string` | 0 | 1 | false |
| `IsShared` | `boolean` | 1 | 1 | false |

### CreateCalendarItemResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CalendarID` | `int` | 1 | 1 | false |
| `CalendarItemID` | `int` | 1 | 1 | false |

### CreateCustomerBalanceAdjustmentRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerTransactionTypeID` | `int` | 1 | 1 | false |
| `TransactionDate` | `dateTime` | 1 | 1 | false |
| `Amount` | `decimal` | 1 | 1 | false |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `Notes` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### CreateCustomerBalanceAdjustmentResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `TransactionID` | `int` | 1 | 1 | false |

### CreateCustomerContactRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `FirstName` | `string` | 0 | 1 | false |
| `LastName` | `string` | 0 | 1 | false |
| `MiddleName` | `string` | 0 | 1 | false |
| `Company` | `string` | 0 | 1 | false |
| `BusinessPhone` | `string` | 0 | 1 | false |
| `HomePhone` | `string` | 0 | 1 | false |
| `Mobile` | `string` | 0 | 1 | false |
| `Fax` | `string` | 0 | 1 | false |
| `Email` | `string` | 0 | 1 | false |
| `Address1` | `string` | 0 | 1 | false |
| `Address2` | `string` | 0 | 1 | false |
| `City` | `string` | 0 | 1 | false |
| `State` | `string` | 0 | 1 | false |
| `Zip` | `string` | 0 | 1 | false |
| `Country` | `string` | 0 | 1 | false |
| `BirthDate` | `dateTime` | 1 | 1 | true |
| `Notes` | `string` | 0 | 1 | false |
| `LinkedIn` | `string` | 0 | 1 | false |
| `Facebook` | `string` | 0 | 1 | false |
| `Blog` | `string` | 0 | 1 | false |
| `MySpace` | `string` | 0 | 1 | false |
| `GooglePlus` | `string` | 0 | 1 | false |
| `Twitter` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### CreateCustomerContactResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerContactID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### CreateCustomerExtendedRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `ExtendedGroupID` | `int` | 1 | 1 | false |
| `Field1` | `string` | 0 | 1 | false |
| `Field2` | `string` | 0 | 1 | false |
| `Field3` | `string` | 0 | 1 | false |
| `Field4` | `string` | 0 | 1 | false |
| `Field5` | `string` | 0 | 1 | false |
| `Field6` | `string` | 0 | 1 | false |
| `Field7` | `string` | 0 | 1 | false |
| `Field8` | `string` | 0 | 1 | false |
| `Field9` | `string` | 0 | 1 | false |
| `Field10` | `string` | 0 | 1 | false |
| `Field11` | `string` | 0 | 1 | false |
| `Field12` | `string` | 0 | 1 | false |
| `Field13` | `string` | 0 | 1 | false |
| `Field14` | `string` | 0 | 1 | false |
| `Field15` | `string` | 0 | 1 | false |
| `Field16` | `string` | 0 | 1 | false |
| `Field17` | `string` | 0 | 1 | false |
| `Field18` | `string` | 0 | 1 | false |
| `Field19` | `string` | 0 | 1 | false |
| `Field20` | `string` | 0 | 1 | false |
| `Field21` | `string` | 0 | 1 | false |
| `Field22` | `string` | 0 | 1 | false |
| `Field23` | `string` | 0 | 1 | false |
| `Field24` | `string` | 0 | 1 | false |
| `Field25` | `string` | 0 | 1 | false |
| `Field26` | `string` | 0 | 1 | false |
| `Field27` | `string` | 0 | 1 | false |
| `Field28` | `string` | 0 | 1 | false |
| `Field29` | `string` | 0 | 1 | false |
| `Field30` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### CreateCustomerExtendedResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerExtendedID` | `int` | 1 | 1 | false |

### CreateCustomerFileRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `FileName` | `string` | 0 | 1 | false |
| `FileData` | `base64Binary` | 0 | 1 | false |
| `OverwriteExistingFile` | `boolean` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `FolderName` | `string` | 0 | 1 | false |
| `ParentFolderID` | `int` | 1 | 1 | true |

### CreateCustomerFileResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `FolderID` | `int` | 1 | 1 | false |
| `FileID` | `int` | 1 | 1 | false |

### CreateCustomerFolderRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `FolderName` | `string` | 0 | 1 | false |
| `ParentFolderID` | `int` | 1 | 1 | true |

### CreateCustomerFolderResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `FolderID` | `int` | 1 | 1 | false |

### CreateCustomerInquiryRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `Detail` | `string` | 0 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `AssignToUser` | `string` | 0 | 1 | false |
| `CustomerInquiryStatusID` | `int` | 1 | 1 | false |
| `CustomerInquiryCategoryID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `ParentID` | `int` | 1 | 1 | true |

### CreateCustomerInquiryResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `NewCustomerHistoryID` | `int` | 1 | 1 | false |

### CreateCustomerLeadRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `FirstName` | `string` | 0 | 1 | false |
| `LastName` | `string` | 0 | 1 | false |
| `MiddleName` | `string` | 0 | 1 | false |
| `Company` | `string` | 0 | 1 | false |
| `Phone` | `string` | 0 | 1 | false |
| `Phone2` | `string` | 0 | 1 | false |
| `MobilePhone` | `string` | 0 | 1 | false |
| `Fax` | `string` | 0 | 1 | false |
| `Email` | `string` | 0 | 1 | false |
| `Address1` | `string` | 0 | 1 | false |
| `Address2` | `string` | 0 | 1 | false |
| `City` | `string` | 0 | 1 | false |
| `State` | `string` | 0 | 1 | false |
| `Zip` | `string` | 0 | 1 | false |
| `Country` | `string` | 0 | 1 | false |
| `BirthDate` | `dateTime` | 1 | 1 | true |
| `Notes` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### CreateCustomerLeadResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerLeadID` | `int` | 1 | 1 | false |

### CreateCustomerRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `FirstName` | `string` | 0 | 1 | false |
| `LastName` | `string` | 0 | 1 | false |
| `Company` | `string` | 0 | 1 | false |
| `CustomerType` | `int` | 1 | 1 | false |
| `CustomerStatus` | `int` | 1 | 1 | true |
| `Email` | `string` | 0 | 1 | false |
| `Phone` | `string` | 0 | 1 | false |
| `Phone2` | `string` | 0 | 1 | false |
| `MobilePhone` | `string` | 0 | 1 | false |
| `Fax` | `string` | 0 | 1 | false |
| `Notes` | `string` | 0 | 1 | false |
| `MainAddress1` | `string` | 0 | 1 | false |
| `MainAddress2` | `string` | 0 | 1 | false |
| `MainAddress3` | `string` | 0 | 1 | false |
| `MainCity` | `string` | 0 | 1 | false |
| `MainState` | `string` | 0 | 1 | false |
| `MainZip` | `string` | 0 | 1 | false |
| `MainCountry` | `string` | 0 | 1 | false |
| `MainCounty` | `string` | 0 | 1 | false |
| `MailAddress1` | `string` | 0 | 1 | false |
| `MailAddress2` | `string` | 0 | 1 | false |
| `MailAddress3` | `string` | 0 | 1 | false |
| `MailCity` | `string` | 0 | 1 | false |
| `MailState` | `string` | 0 | 1 | false |
| `MailZip` | `string` | 0 | 1 | false |
| `MailCountry` | `string` | 0 | 1 | false |
| `MailCounty` | `string` | 0 | 1 | false |
| `OtherAddress1` | `string` | 0 | 1 | false |
| `OtherAddress2` | `string` | 0 | 1 | false |
| `OtherAddress3` | `string` | 0 | 1 | false |
| `OtherCity` | `string` | 0 | 1 | false |
| `OtherState` | `string` | 0 | 1 | false |
| `OtherZip` | `string` | 0 | 1 | false |
| `OtherCountry` | `string` | 0 | 1 | false |
| `OtherCounty` | `string` | 0 | 1 | false |
| `CanLogin` | `boolean` | 1 | 1 | false |
| `LoginName` | `string` | 0 | 1 | false |
| `LoginPassword` | `string` | 0 | 1 | false |
| `InsertEnrollerTree` | `boolean` | 1 | 1 | false |
| `EnrollerID` | `int` | 1 | 1 | false |
| `InsertUnilevelTree` | `boolean` | 1 | 1 | false |
| `SponsorID` | `int` | 1 | 1 | false |
| `UseManualCustomerID` | `boolean` | 1 | 1 | false |
| `ManualCustomerID` | `int` | 1 | 1 | false |
| `TaxID` | `string` | 0 | 1 | false |
| `SalesTaxID` | `string` | 0 | 1 | false |
| `SalesTaxExemptExpireDate` | `dateTime` | 1 | 1 | true |
| `IsSalesTaxExempt` | `boolean` | 1 | 1 | true |
| `BirthDate` | `dateTime` | 1 | 1 | false |
| `Field1` | `string` | 0 | 1 | false |
| `Field2` | `string` | 0 | 1 | false |
| `Field3` | `string` | 0 | 1 | false |
| `Field4` | `string` | 0 | 1 | false |
| `Field5` | `string` | 0 | 1 | false |
| `Field6` | `string` | 0 | 1 | false |
| `Field7` | `string` | 0 | 1 | false |
| `Field8` | `string` | 0 | 1 | false |
| `Field9` | `string` | 0 | 1 | false |
| `Field10` | `string` | 0 | 1 | false |
| `Field11` | `string` | 0 | 1 | false |
| `Field12` | `string` | 0 | 1 | false |
| `Field13` | `string` | 0 | 1 | false |
| `Field14` | `string` | 0 | 1 | false |
| `Field15` | `string` | 0 | 1 | false |
| `SubscribeToBroadcasts` | `boolean` | 1 | 1 | false |
| `SubscribeFromIPAddress` | `string` | 0 | 1 | false |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `PayableToName` | `string` | 0 | 1 | false |
| `EntryDate` | `dateTime` | 1 | 1 | false |
| `DefaultWarehouseID` | `int` | 1 | 1 | true |
| `PayableType` | `PayableType` | 1 | 1 | true |
| `CheckThreshold` | `decimal` | 1 | 1 | true |
| `TaxIDType` | `string` | 0 | 1 | false |
| `LanguageID` | `int` | 1 | 1 | false |
| `Gender` | `Gender` | 1 | 1 | true |
| `VatRegistration` | `string` | 0 | 1 | false |
| `Date1` | `dateTime` | 1 | 1 | true |
| `Date2` | `dateTime` | 1 | 1 | true |
| `Date3` | `dateTime` | 1 | 1 | true |
| `Date4` | `dateTime` | 1 | 1 | true |
| `Date5` | `dateTime` | 1 | 1 | true |
| `MiddleName` | `string` | 0 | 1 | false |
| `NameSuffix` | `string` | 0 | 1 | false |
| `BinaryPlacementPreference` | `int` | 1 | 1 | true |
| `UseBinaryHoldingTank` | `boolean` | 1 | 1 | true |
| `MainAddressVerified` | `boolean` | 1 | 1 | true |
| `MailAddressVerified` | `boolean` | 1 | 1 | true |
| `OtherAddressVerified` | `boolean` | 1 | 1 | true |
| `SponsorKey` | `string` | 0 | 1 | false |
| `EnrollerKey` | `string` | 0 | 1 | false |
| `ManualCustomerKey` | `string` | 0 | 1 | false |
| `PayableTy` | `string` | 0 | 1 | false |
| `GenderID` | `string` | 0 | 1 | false |

### CreateCustomerResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### CreateCustomerWallItemRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `Text` | `string` | 0 | 1 | false |
| `Field1` | `string` | 0 | 1 | false |
| `Field2` | `string` | 0 | 1 | false |
| `Field3` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### CreateCustomerWallItemResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `WallItemID` | `int` | 1 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### CreateDestinationRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Name` | `string` | 0 | 1 | false |
| `ConnectionString` | `string` | 0 | 1 | false |

### CreateDestinationResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DestinationID` | `int` | 1 | 1 | false |
| `Name` | `string` | 0 | 1 | false |

### CreateEmailRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `MailFolderType` | `MailForderType` | 1 | 1 | false |
| `Priority` | `MailPriority` | 1 | 1 | false |
| `MailStatusType` | `MailStatusType` | 1 | 1 | false |
| `Subject` | `string` | 0 | 1 | false |
| `MailFrom` | `string` | 0 | 1 | false |
| `MailTo` | `string` | 0 | 1 | false |
| `ReplyTo` | `string` | 0 | 1 | false |
| `MailCC` | `string` | 0 | 1 | false |
| `MailBCC` | `string` | 0 | 1 | false |
| `Content` | `string` | 0 | 1 | false |
| `SmtpServer` | `string` | 0 | 1 | false |
| `Attachments` | `ArrayOfEmailAttachment` | 0 | 1 | false |
| `ForwardedAttachments` | `ArrayOfForwardedAttachment` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### CreateEmailResponse
Extends `ApiResponse`.

_No fields._

### CreateEmailTemplateRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `Content` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### CreateEmailTemplateResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `TemplateID` | `int` | 1 | 1 | false |

### CreateEntityRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `EntityName` | `string` | 0 | 1 | false |
| `EntitySetName` | `string` | 0 | 1 | false |
| `SchemaName` | `string` | 0 | 1 | false |
| `IsLog` | `boolean` | 1 | 1 | false |
| `MaxLogDays` | `int` | 1 | 1 | false |
| `LogDateField` | `string` | 0 | 1 | false |
| `Navigations` | `ArrayOfString` | 0 | 1 | false |
| `Properties` | `ArrayOfPropertyDataRequest` | 0 | 1 | false |

### CreateEntityResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Entity` | `EntityDataResponse` | 0 | 1 | false |

### CreateExpectedBankWireRequest
Extends `BaseCreateExpectedPaymentRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderID` | `int` | 1 | 1 | false |
| `PaymentDate` | `dateTime` | 1 | 1 | false |
| `Amount` | `decimal` | 1 | 1 | false |
| `BankName` | `string` | 0 | 1 | false |
| `NameOnAccount` | `string` | 0 | 1 | false |
| `Memo` | `string` | 0 | 1 | false |
| `AuthorizationCode` | `string` | 0 | 1 | false |
| `OrderKey` | `string` | 0 | 1 | false |

### CreateExpectedBankWireResponse
Extends `BaseCreateExpectedPaymentResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ExpectedPaymentID` | `int` | 1 | 1 | false |

### CreateExpectedCODRequest
Extends `BaseCreateExpectedPaymentRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderID` | `int` | 1 | 1 | false |
| `PaymentDate` | `dateTime` | 1 | 1 | false |
| `Amount` | `decimal` | 1 | 1 | false |
| `OrderKey` | `string` | 0 | 1 | false |

### CreateExpectedCODResponse
Extends `BaseCreateExpectedPaymentResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ExpectedPaymentID` | `int` | 1 | 1 | false |

### CreateExpectedPaymentRequest
Extends `BaseCreateExpectedPaymentRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderID` | `int` | 1 | 1 | false |
| `PaymentDate` | `dateTime` | 1 | 1 | false |
| `Amount` | `decimal` | 1 | 1 | false |
| `PaymentType` | `PaymentType` | 1 | 1 | false |
| `AuthorizationCode` | `string` | 0 | 1 | false |
| `OrderKey` | `string` | 0 | 1 | false |
| `PaymentTy` | `string` | 0 | 1 | false |

### CreateExpectedPaymentResponse
Extends `BaseCreateExpectedPaymentResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ExpectedPaymentID` | `int` | 1 | 1 | false |

### CreateExtendedDbSchemaRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SchemaName` | `string` | 0 | 1 | false |

### CreateExtendedDbSchemaResponse
Extends `ApiResponse`.

_No fields._

### CreateGuestRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Date1` | `dateTime` | 1 | 1 | true |
| `Date2` | `dateTime` | 1 | 1 | true |
| `Date3` | `dateTime` | 1 | 1 | true |
| `Date4` | `dateTime` | 1 | 1 | true |
| `Date5` | `dateTime` | 1 | 1 | true |
| `HostID` | `int` | 1 | 1 | false |
| `PartyID` | `int` | 1 | 1 | true |
| `CustomerID` | `int` | 1 | 1 | true |
| `FirstName` | `string` | 0 | 1 | false |
| `MiddleName` | `string` | 0 | 1 | false |
| `LastName` | `string` | 0 | 1 | false |
| `NameSuffix` | `string` | 0 | 1 | false |
| `Company` | `string` | 0 | 1 | false |
| `Gender` | `Gender` | 1 | 1 | true |
| `LanguageID` | `int` | 1 | 1 | false |
| `GuestStatus` | `int` | 1 | 1 | true |
| `Address1` | `string` | 0 | 1 | false |
| `Address2` | `string` | 0 | 1 | false |
| `Address3` | `string` | 0 | 1 | false |
| `City` | `string` | 0 | 1 | false |
| `County` | `string` | 0 | 1 | false |
| `State` | `string` | 0 | 1 | false |
| `Zip` | `string` | 0 | 1 | false |
| `Country` | `string` | 0 | 1 | false |
| `Phone` | `string` | 0 | 1 | false |
| `Phone2` | `string` | 0 | 1 | false |
| `MobilePhone` | `string` | 0 | 1 | false |
| `Email` | `string` | 0 | 1 | false |
| `Field1` | `string` | 0 | 1 | false |
| `Field2` | `string` | 0 | 1 | false |
| `Field3` | `string` | 0 | 1 | false |
| `Field4` | `string` | 0 | 1 | false |
| `Field5` | `string` | 0 | 1 | false |
| `Field6` | `string` | 0 | 1 | false |
| `Field7` | `string` | 0 | 1 | false |
| `Field8` | `string` | 0 | 1 | false |
| `Field9` | `string` | 0 | 1 | false |
| `Field10` | `string` | 0 | 1 | false |
| `Field11` | `string` | 0 | 1 | false |
| `Field12` | `string` | 0 | 1 | false |
| `Field13` | `string` | 0 | 1 | false |
| `Field14` | `string` | 0 | 1 | false |
| `Field15` | `string` | 0 | 1 | false |
| `Notes` | `string` | 0 | 1 | false |
| `EntryDate` | `dateTime` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `GenderID` | `string` | 0 | 1 | false |

### CreateGuestResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `GuestID` | `int` | 1 | 1 | false |

### CreateItemRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ItemCode` | `string` | 0 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `Weight` | `decimal` | 1 | 1 | false |
| `Notes` | `string` | 0 | 1 | false |
| `AvailableInAllCountryRegions` | `boolean` | 1 | 1 | false |
| `TaxedInAllCountryRegions` | `boolean` | 1 | 1 | false |
| `AvailableInAllWarehouses` | `boolean` | 1 | 1 | false |
| `IsVirtual` | `boolean` | 0 | 1 | false |
| `ItemTypeID` | `int` | 0 | 1 | false |
| `IsSubscriptionUpdate` | `boolean` | 0 | 1 | false |
| `IsPointIncrement` | `boolean` | 0 | 1 | false |
| `OtherCheck1` | `boolean` | 0 | 1 | false |
| `OtherCheck2` | `boolean` | 0 | 1 | false |
| `OtherCheck3` | `boolean` | 0 | 1 | false |
| `OtherCheck4` | `boolean` | 0 | 1 | false |
| `OtherCheck5` | `boolean` | 0 | 1 | false |
| `Field1` | `string` | 0 | 1 | false |
| `Field2` | `string` | 0 | 1 | false |
| `Field3` | `string` | 0 | 1 | false |
| `Field4` | `string` | 0 | 1 | false |
| `Field5` | `string` | 0 | 1 | false |
| `Field6` | `string` | 0 | 1 | false |
| `Field7` | `string` | 0 | 1 | false |
| `Field8` | `string` | 0 | 1 | false |
| `Field9` | `string` | 0 | 1 | false |
| `Field10` | `string` | 0 | 1 | false |
| `HideFromSearch` | `boolean` | 0 | 1 | false |
| `IsGroupMaster` | `boolean` | 0 | 1 | false |
| `SuppressGroupMaster` | `boolean` | 0 | 1 | false |

### CreateItemResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ItemID` | `int` | 1 | 1 | false |
| `ItemCode` | `string` | 0 | 1 | false |

### CreateMailFolderRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `MailFolderName` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### CreateMailFolderResponse
Extends `ApiResponse`.

_No fields._

### CreateOrderDetailRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderID` | `int` | 1 | 1 | false |
| `OrderLine` | `int` | 1 | 1 | false |
| `ItemCode` | `string` | 0 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `Qty` | `decimal` | 1 | 1 | false |
| `PriceEach` | `decimal` | 1 | 1 | true |
| `PriceExt` | `decimal` | 1 | 1 | true |
| `BVEach` | `decimal` | 1 | 1 | true |
| `BusinessVolume` | `decimal` | 1 | 1 | true |
| `CVEach` | `decimal` | 1 | 1 | true |
| `CommissionableVolume` | `decimal` | 1 | 1 | true |
| `ShippingPriceEach` | `decimal` | 1 | 1 | true |
| `ChargeShippingOn` | `decimal` | 1 | 1 | true |
| `IsTaxedInRegion` | `boolean` | 1 | 1 | true |
| `IsTaxedInRegionFed` | `boolean` | 1 | 1 | true |
| `IsTaxedInRegionState` | `boolean` | 1 | 1 | true |
| `TaxablePriceEach` | `decimal` | 1 | 1 | true |
| `Taxable` | `decimal` | 1 | 1 | true |
| `CombinedTax` | `decimal` | 1 | 1 | true |
| `FedTax` | `decimal` | 1 | 1 | true |
| `StateTax` | `decimal` | 1 | 1 | true |
| `CityTax` | `decimal` | 1 | 1 | true |
| `CityLocalTax` | `decimal` | 1 | 1 | true |
| `CountyTax` | `decimal` | 1 | 1 | true |
| `CountyLocalTax` | `decimal` | 1 | 1 | true |
| `ManualTax` | `decimal` | 1 | 1 | true |
| `IsBackOrder` | `boolean` | 1 | 1 | true |
| `WeightEach` | `decimal` | 1 | 1 | true |
| `Other1Each` | `decimal` | 1 | 1 | true |
| `Other1` | `decimal` | 1 | 1 | true |
| `Other2Each` | `decimal` | 1 | 1 | true |
| `Other2` | `decimal` | 1 | 1 | true |
| `Other3Each` | `decimal` | 1 | 1 | true |
| `Other3` | `decimal` | 1 | 1 | true |
| `Other4Each` | `decimal` | 1 | 1 | true |
| `Other4` | `decimal` | 1 | 1 | true |
| `Other5Each` | `decimal` | 1 | 1 | true |
| `Other5` | `decimal` | 1 | 1 | true |
| `Other6Each` | `decimal` | 1 | 1 | true |
| `Other6` | `decimal` | 1 | 1 | true |
| `Other7Each` | `decimal` | 1 | 1 | true |
| `Other7` | `decimal` | 1 | 1 | true |
| `Other8Each` | `decimal` | 1 | 1 | true |
| `Other8` | `decimal` | 1 | 1 | true |
| `Other9Each` | `decimal` | 1 | 1 | true |
| `Other9` | `decimal` | 1 | 1 | true |
| `Other10Each` | `decimal` | 1 | 1 | true |
| `Other10` | `decimal` | 1 | 1 | true |
| `DiscountExt` | `decimal` | 1 | 1 | true |
| `OriginalTaxableEach` | `decimal` | 1 | 1 | true |
| `OriginalBVEach` | `decimal` | 1 | 1 | true |
| `OriginalCVEach` | `decimal` | 1 | 1 | true |
| `StateTaxable` | `decimal` | 1 | 1 | true |
| `IsStateTaxOverride` | `boolean` | 1 | 1 | true |
| `DynamicKitItemID` | `int` | 1 | 1 | true |
| `HandlingFee` | `decimal` | 1 | 1 | true |
| `Reference1` | `string` | 0 | 1 | false |
| `OrderKey` | `string` | 0 | 1 | false |

### CreateOrderDetailResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderID` | `int` | 1 | 1 | false |
| `OrderLine` | `int` | 1 | 1 | false |
| `OrderKey` | `string` | 0 | 1 | false |

### CreateOrderImportRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `FirstName` | `string` | 0 | 1 | false |
| `LastName` | `string` | 0 | 1 | false |
| `Company` | `string` | 0 | 1 | false |
| `Phone` | `string` | 0 | 1 | false |
| `Email` | `string` | 0 | 1 | false |
| `ShipMethodID` | `int` | 1 | 1 | false |
| `Address1` | `string` | 0 | 1 | false |
| `Address2` | `string` | 0 | 1 | false |
| `Address3` | `string` | 0 | 1 | false |
| `City` | `string` | 0 | 1 | false |
| `State` | `string` | 0 | 1 | false |
| `Zip` | `string` | 0 | 1 | false |
| `Country` | `string` | 0 | 1 | false |
| `County` | `string` | 0 | 1 | false |
| `Notes` | `string` | 0 | 1 | false |
| `WarehouseID` | `int` | 1 | 1 | false |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `ShippingStateTax` | `decimal` | 1 | 1 | false |
| `ShippingFedTax` | `decimal` | 1 | 1 | false |
| `ShippingCountyLocalTax` | `decimal` | 1 | 1 | false |
| `ShippingCountyTax` | `decimal` | 1 | 1 | false |
| `ShippingCityLocalTax` | `decimal` | 1 | 1 | false |
| `ShippingCityTax` | `decimal` | 1 | 1 | false |
| `Shipping` | `decimal` | 1 | 1 | false |
| `PriceType` | `int` | 1 | 1 | false |
| `OrderStatus` | `OrderStatusType` | 1 | 1 | false |
| `OrderDate` | `dateTime` | 1 | 1 | false |
| `Other11` | `string` | 0 | 1 | false |
| `Other12` | `string` | 0 | 1 | false |
| `Other13` | `string` | 0 | 1 | false |
| `Other14` | `string` | 0 | 1 | false |
| `Other15` | `string` | 0 | 1 | false |
| `Other16` | `string` | 0 | 1 | false |
| `Other17` | `string` | 0 | 1 | false |
| `Other18` | `string` | 0 | 1 | false |
| `Other19` | `string` | 0 | 1 | false |
| `Other20` | `string` | 0 | 1 | false |
| `OrderType` | `OrderType` | 1 | 1 | false |
| `UseManualOrderID` | `boolean` | 1 | 1 | true |
| `ManualOrderID` | `int` | 1 | 1 | true |
| `ReturnOrderID` | `int` | 1 | 1 | true |
| `OrderDetails` | `ArrayOfOrderImportDetail` | 0 | 1 | false |
| `PartyID` | `int` | 1 | 1 | true |
| `ManualOrderKey` | `string` | 0 | 1 | false |
| `ReturnOrderKey` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `OverwriteExistingOrder` | `boolean` | 1 | 1 | false |
| `ExistingOrderID` | `int` | 1 | 1 | true |
| `ExistingOrderKey` | `string` | 0 | 1 | false |
| `IsCommissionable` | `boolean` | 1 | 1 | false |
| `HandlingFee` | `decimal` | 1 | 1 | true |
| `PreserveOrderCreateDate` | `boolean` | 1 | 1 | false |
| `ParentOrderID` | `int` | 1 | 1 | false |

### CreateOrderImportResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderID` | `int` | 1 | 1 | false |
| `OrderKey` | `string` | 0 | 1 | false |
| `DetailIDs` | `ArrayOfOrderDetailIDs` | 0 | 1 | false |

### CreateOrderRequest
Extends `BaseCalculateOrderRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `OrderStatus` | `OrderStatusType` | 1 | 1 | false |
| `OrderDate` | `dateTime` | 1 | 1 | false |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `WarehouseID` | `int` | 1 | 1 | false |
| `ShipMethodID` | `int` | 1 | 1 | false |
| `PriceType` | `int` | 1 | 1 | false |
| `FirstName` | `string` | 0 | 1 | false |
| `MiddleName` | `string` | 0 | 1 | false |
| `LastName` | `string` | 0 | 1 | false |
| `NameSuffix` | `string` | 0 | 1 | false |
| `Company` | `string` | 0 | 1 | false |
| `Address1` | `string` | 0 | 1 | false |
| `Address2` | `string` | 0 | 1 | false |
| `Address3` | `string` | 0 | 1 | false |
| `City` | `string` | 0 | 1 | false |
| `State` | `string` | 0 | 1 | false |
| `Zip` | `string` | 0 | 1 | false |
| `Country` | `string` | 0 | 1 | false |
| `County` | `string` | 0 | 1 | false |
| `Email` | `string` | 0 | 1 | false |
| `Phone` | `string` | 0 | 1 | false |
| `Notes` | `string` | 0 | 1 | false |
| `Other11` | `string` | 0 | 1 | false |
| `Other12` | `string` | 0 | 1 | false |
| `Other13` | `string` | 0 | 1 | false |
| `Other14` | `string` | 0 | 1 | false |
| `Other15` | `string` | 0 | 1 | false |
| `Other16` | `string` | 0 | 1 | false |
| `Other17` | `string` | 0 | 1 | false |
| `Other18` | `string` | 0 | 1 | false |
| `Other19` | `string` | 0 | 1 | false |
| `Other20` | `string` | 0 | 1 | false |
| `OrderType` | `OrderType` | 1 | 1 | false |
| `TaxRateOverride` | `decimal` | 1 | 1 | true |
| `ShippingAmountOverride` | `decimal` | 1 | 1 | true |
| `UseManualOrderID` | `boolean` | 1 | 1 | true |
| `ManualOrderID` | `int` | 1 | 1 | true |
| `TransferVolumeToID` | `int` | 1 | 1 | true |
| `ReturnOrderID` | `int` | 1 | 1 | true |
| `OverwriteExistingOrder` | `boolean` | 1 | 1 | false |
| `ExistingOrderID` | `int` | 1 | 1 | false |
| `PartyID` | `int` | 1 | 1 | true |
| `Details` | `ArrayOfOrderDetailRequest` | 0 | 1 | false |
| `SuppressPackSlipPrice` | `boolean` | 1 | 1 | false |
| `TransferVolumeToKey` | `string` | 0 | 1 | false |
| `ReturnOrderKey` | `string` | 0 | 1 | false |
| `ManualOrderKey` | `string` | 0 | 1 | false |
| `ExistingOrderKey` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `OrderSubStatusTy` | `int` | 1 | 1 | true |
| `ReferralID` | `int` | 1 | 1 | true |

### CreateOrderResponse
Extends `BaseCalculateOrderResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderID` | `int` | 1 | 1 | false |
| `Total` | `decimal` | 1 | 1 | false |
| `SubTotal` | `decimal` | 1 | 1 | false |
| `TaxTotal` | `decimal` | 1 | 1 | false |
| `ShippingTotal` | `decimal` | 1 | 1 | false |
| `DiscountTotal` | `decimal` | 1 | 1 | false |
| `WeightTotal` | `decimal` | 1 | 1 | false |
| `BusinessVolumeTotal` | `decimal` | 1 | 1 | false |
| `CommissionableVolumeTotal` | `decimal` | 1 | 1 | false |
| `Other1Total` | `decimal` | 1 | 1 | false |
| `Other2Total` | `decimal` | 1 | 1 | false |
| `Other3Total` | `decimal` | 1 | 1 | false |
| `Other4Total` | `decimal` | 1 | 1 | false |
| `Other5Total` | `decimal` | 1 | 1 | false |
| `Other6Total` | `decimal` | 1 | 1 | false |
| `Other7Total` | `decimal` | 1 | 1 | false |
| `Other8Total` | `decimal` | 1 | 1 | false |
| `Other9Total` | `decimal` | 1 | 1 | false |
| `Other10Total` | `decimal` | 1 | 1 | false |
| `ShippingTax` | `decimal` | 1 | 1 | false |
| `OrderTax` | `decimal` | 1 | 1 | false |
| `HandlingFeeTotal` | `decimal` | 1 | 1 | false |
| `Details` | `ArrayOfOrderDetailResponse` | 0 | 1 | false |
| `Warnings` | `ArrayOfString` | 0 | 1 | false |
| `OrderKey` | `string` | 0 | 1 | false |
| `ReferralID` | `int` | 1 | 1 | true |

### CreatePartyRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PartyType` | `int` | 1 | 1 | false |
| `PartyStatusType` | `int` | 1 | 1 | false |
| `HostID` | `int` | 1 | 1 | false |
| `DistributorID` | `int` | 1 | 1 | false |
| `StartDate` | `dateTime` | 1 | 1 | false |
| `CloseDate` | `dateTime` | 1 | 1 | true |
| `Description` | `string` | 0 | 1 | false |
| `EventStart` | `dateTime` | 1 | 1 | true |
| `EventEnd` | `dateTime` | 1 | 1 | true |
| `LanguageID` | `int` | 1 | 1 | false |
| `Information` | `string` | 0 | 1 | false |
| `Address` | `PartyAddress` | 0 | 1 | false |
| `BookingPartyID` | `int` | 1 | 1 | true |
| `Field1` | `string` | 0 | 1 | false |
| `Field2` | `string` | 0 | 1 | false |
| `Field3` | `string` | 0 | 1 | false |
| `Field4` | `string` | 0 | 1 | false |
| `Field5` | `string` | 0 | 1 | false |
| `TimeZoneID` | `string` | 0 | 1 | false |
| `VirtualMeetingLink` | `string` | 0 | 1 | false |
| `PartyShoppingUrl` | `string` | 0 | 1 | false |
| `PartyExternalID` | `guid` | 1 | 1 | true |

### CreatePartyResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PartyID` | `int` | 1 | 1 | false |

### CreatePaymentCheckRequest
Extends `BaseCreatePaymentRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderID` | `int` | 1 | 1 | false |
| `PaymentDate` | `dateTime` | 1 | 1 | false |
| `Amount` | `decimal` | 1 | 1 | false |
| `Memo` | `string` | 0 | 1 | false |
| `CheckNumber` | `string` | 0 | 1 | false |
| `CheckAccountNumber` | `string` | 0 | 1 | false |
| `CheckRoutingNumber` | `string` | 0 | 1 | false |
| `CheckDate` | `dateTime` | 1 | 1 | true |
| `OrderKey` | `string` | 0 | 1 | false |
| `MerchantTy` | `int` | 1 | 1 | false |
| `MerchantAccount` | `string` | 0 | 1 | false |
| `MerchantTransactionKey` | `string` | 0 | 1 | false |
| `PayeeName` | `string` | 0 | 1 | false |

### CreatePaymentCheckResponse
Extends `CreatePaymentResponse`.

_No fields._

### CreatePaymentCreditCardRequest
Extends `BaseCreatePaymentCreditCardRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderID` | `int` | 1 | 1 | false |
| `PaymentDate` | `dateTime` | 1 | 1 | false |
| `Amount` | `decimal` | 1 | 1 | false |
| `CreditCardNumber` | `string` | 0 | 1 | false |
| `ExpirationMonth` | `int` | 1 | 1 | false |
| `ExpirationYear` | `int` | 1 | 1 | false |
| `BillingName` | `string` | 0 | 1 | false |
| `BillingAddress` | `string` | 0 | 1 | false |
| `BillingAddress2` | `string` | 0 | 1 | false |
| `BillingCity` | `string` | 0 | 1 | false |
| `BillingState` | `string` | 0 | 1 | false |
| `BillingZip` | `string` | 0 | 1 | false |
| `BillingCountry` | `string` | 0 | 1 | false |
| `CreditCardType` | `int` | 1 | 1 | true |
| `AuthorizationCode` | `string` | 0 | 1 | false |
| `Memo` | `string` | 0 | 1 | false |
| `OrderKey` | `string` | 0 | 1 | false |
| `MerchantTransactionKey` | `string` | 0 | 1 | false |
| `MerchantTy` | `int` | 1 | 1 | false |
| `MerchantAccount` | `string` | 0 | 1 | false |

### CreatePaymentCreditCardResponse
Extends `CreatePaymentResponse`.

_No fields._

### CreatePaymentPointAccountRequest
Extends `BaseCreatePaymentRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderID` | `int` | 1 | 1 | false |
| `PointAccountID` | `int` | 1 | 1 | false |
| `PaymentDate` | `dateTime` | 1 | 1 | false |
| `Amount` | `decimal` | 1 | 1 | false |
| `Memo` | `string` | 0 | 1 | false |
| `OrderKey` | `string` | 0 | 1 | false |

### CreatePaymentPointAccountResponse
Extends `CreatePaymentResponse`.

_No fields._

### CreatePaymentRequest
Extends `BaseCreatePaymentRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderID` | `int` | 1 | 1 | false |
| `PaymentDate` | `dateTime` | 1 | 1 | false |
| `Amount` | `decimal` | 1 | 1 | false |
| `PaymentType` | `PaymentType` | 1 | 1 | false |
| `AuthorizationCode` | `string` | 0 | 1 | false |
| `Memo` | `string` | 0 | 1 | false |
| `BillingName` | `string` | 0 | 1 | false |
| `BillingAddress` | `string` | 0 | 1 | false |
| `BillingAddress2` | `string` | 0 | 1 | false |
| `BillingCity` | `string` | 0 | 1 | false |
| `BillingState` | `string` | 0 | 1 | false |
| `BillingZip` | `string` | 0 | 1 | false |
| `BillingCountry` | `string` | 0 | 1 | false |
| `OrderKey` | `string` | 0 | 1 | false |
| `PaymentTy` | `string` | 0 | 1 | false |
| `MerchantTy` | `int` | 1 | 1 | false |
| `MerchantAccount` | `string` | 0 | 1 | false |
| `MerchantTransactionKey` | `string` | 0 | 1 | false |

### CreatePaymentResponse
Extends `BaseCreatePaymentResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PaymentID` | `int` | 1 | 1 | false |
| `Message` | `string` | 0 | 1 | false |
| `DisplayMessage` | `string` | 0 | 1 | false |
| `MerchantTransactionKey` | `string` | 0 | 1 | false |

### CreatePaymentWalletRequest
Extends `BaseCreatePaymentRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderID` | `int` | 1 | 1 | false |
| `PaymentDate` | `dateTime` | 1 | 1 | false |
| `Amount` | `decimal` | 1 | 1 | false |
| `WalletType` | `int` | 1 | 1 | false |
| `WalletAccount` | `string` | 0 | 1 | false |
| `AuthorizationCode` | `string` | 0 | 1 | false |
| `Memo` | `string` | 0 | 1 | false |
| `BillingName` | `string` | 0 | 1 | false |
| `OrderKey` | `string` | 0 | 1 | false |
| `MerchantTy` | `int` | 1 | 1 | false |
| `MerchantAccount` | `string` | 0 | 1 | false |
| `MerchantTransactionKey` | `string` | 0 | 1 | false |

### CreatePayoutRequest
Extends `BaseCreatePayoutRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `BillIDs_ToPay` | `ArrayOfInt` | 0 | 1 | false |
| `VendorPaymentTypeID` | `int` | 1 | 1 | false |

### CreatePayoutResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PayoutID` | `int` | 1 | 1 | false |
| `TotalDollarAmount` | `decimal` | 1 | 1 | false |

### CreatePointTransactionRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PointAccountID` | `int` | 1 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | false |
| `Amount` | `decimal` | 1 | 1 | false |
| `Reference` | `string` | 0 | 1 | false |
| `TransactionType` | `PointTransactionType` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `PointTransactionTy` | `string` | 0 | 1 | false |

### CreatePointTransactionResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `TransactionID` | `int` | 1 | 1 | false |

### CreateReleaseRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |

### CreateReleaseResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `ReleaseDate` | `dateTime` | 1 | 1 | false |
| `Version` | `string` | 0 | 1 | false |

### CreateResourceSetBannerItemRequest
Extends `BaseCreateResourceSetItemRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Title` | `string` | 0 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `BannerImageBase64` | `string` | 0 | 1 | false |
| `BannerHoverText` | `string` | 0 | 1 | false |
| `BannerURL` | `string` | 0 | 1 | false |
| `BannerClickEvent` | `BannerClickEvent` | 1 | 1 | false |
| `BannerType` | `BannerType` | 1 | 1 | false |
| `AssociatedDataSets` | `ArrayOfString` | 0 | 1 | false |

### CreateResourceSetBooleanItemRequest
Extends `BaseCreateResourceSetItemRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `BooleanValue` | `boolean` | 1 | 1 | false |

### CreateResourceSetCarouselItemRequest
Extends `BaseCreateResourceSetItemRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CarouselSlides` | `ArrayOfString` | 0 | 1 | false |
| `CarouselType` | `CarouselType` | 1 | 1 | false |

### CreateResourceSetCultureRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `CultureCode` | `string` | 0 | 1 | false |

### CreateResourceSetCultureResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `CultureCode` | `string` | 0 | 1 | false |
| `Description` | `string` | 0 | 1 | false |

### CreateResourceSetDataSetItemRequest
Extends `BaseCreateResourceSetItemRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DataSetType` | `string` | 0 | 1 | false |
| `DataSetValues` | `ArrayOfString` | 0 | 1 | false |

### CreateResourceSetDateItemRequest
Extends `BaseCreateResourceSetItemRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Date` | `dateTime` | 1 | 1 | false |

### CreateResourceSetDecimalItemRequest
Extends `BaseCreateResourceSetItemRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DecimalValue` | `decimal` | 1 | 1 | false |

### CreateResourceSetDropDownItemRequest
Extends `BaseCreateResourceSetItemRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DropDownValues` | `string` | 0 | 1 | false |
| `DefaultSelectedValue` | `string` | 0 | 1 | false |

### CreateResourceSetEnvironmentRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `EnvironmentCode` | `string` | 0 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `Version` | `string` | 0 | 1 | false |
| `ScheduledVersion` | `string` | 0 | 1 | false |
| `ScheduledVersionDate` | `dateTime` | 1 | 1 | true |

### CreateResourceSetEnvironmentResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `EnvironmentCode` | `string` | 0 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `Version` | `string` | 0 | 1 | false |
| `ScheduledVersion` | `string` | 0 | 1 | false |
| `ScheduledVersionDate` | `dateTime` | 1 | 1 | true |

### CreateResourceSetGroupRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `Description` | `string` | 0 | 1 | false |

### CreateResourceSetGroupResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `ResourceGroupID` | `int` | 1 | 1 | false |
| `Decription` | `string` | 0 | 1 | false |

### CreateResourceSetImageItemRequest
Extends `BaseCreateResourceSetItemRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Base64ImageData` | `string` | 0 | 1 | false |

### CreateResourceSetIntItemRequest
Extends `BaseCreateResourceSetItemRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `IntegerValue` | `int` | 1 | 1 | false |

### CreateResourceSetItemResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `ResourceName` | `string` | 0 | 1 | false |
| `CultureCode` | `string` | 0 | 1 | false |

### CreateResourceSetRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ClassName` | `string` | 0 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `Namespace` | `string` | 0 | 1 | false |
| `SubscriptionKey` | `string` | 0 | 1 | false |

### CreateResourceSetResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `ClassName` | `string` | 0 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `Namespace` | `string` | 0 | 1 | false |
| `SubscriptionKey` | `string` | 0 | 1 | false |

### CreateResourceSetTextItemRequest
Extends `BaseCreateResourceSetItemRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Text` | `string` | 0 | 1 | false |

### CreateResourceSetWidgetItemRequest
Extends `BaseCreateResourceSetItemRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Html` | `string` | 0 | 1 | false |
| `Javascript` | `string` | 0 | 1 | false |
| `Css` | `string` | 0 | 1 | false |

### CreateSilentLoginCipherRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SilentLoginKey` | `string` | 0 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `UserID` | `string` | 0 | 1 | false |
| `Route` | `string` | 0 | 1 | false |

### CreateSilentLoginCipherResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SilentLoginCipher` | `string` | 0 | 1 | false |

### CreateTableFilterSettingsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DestinationId` | `int` | 1 | 1 | false |
| `FilterGroupId` | `TableGroupID` | 1 | 1 | false |
| `ColumnName` | `string` | 0 | 1 | false |
| `SchemaName` | `string` | 0 | 1 | false |
| `TableName` | `string` | 0 | 1 | false |
| `FilterValue` | `string` | 0 | 1 | false |

### CreateTableFilterSettingsResponse
Extends `ApiResponse`.

_No fields._

### CreateVendorBillRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `VendorBillStatusTypeID` | `int` | 1 | 1 | true |
| `CustomerID` | `int` | 1 | 1 | false |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `DueDate` | `dateTime` | 1 | 1 | false |
| `Amount` | `decimal` | 1 | 1 | false |
| `Reference` | `string` | 0 | 1 | false |
| `Notes` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `TaxablePeriodTy` | `int` | 1 | 1 | true |
| `TaxablePeriodID` | `int` | 1 | 1 | true |

### CreateVendorBillResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `VendorBillID` | `int` | 1 | 1 | false |

### CreateWarehouseRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Description` | `string` | 0 | 1 | false |
| `Address1` | `string` | 0 | 1 | false |
| `Address2` | `string` | 0 | 1 | false |
| `City` | `string` | 0 | 1 | false |
| `State` | `string` | 0 | 1 | false |
| `Zip` | `string` | 0 | 1 | false |
| `Country` | `string` | 0 | 1 | false |
| `Currencies` | `ArrayOfString` | 0 | 1 | false |

### CreateWarehouseResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Warehouse` | `WarehouseResponse` | 0 | 1 | false |

### CreateWebCategoryRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `WebID` | `int` | 1 | 1 | false |
| `ParentID` | `int` | 1 | 1 | false |
| `Description` | `string` | 0 | 1 | false |

### CreateWebCategoryResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CategoryID` | `int` | 1 | 1 | false |
| `WebID` | `int` | 1 | 1 | false |

### CreditCardAccountResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CreditCardNumberDisplay` | `string` | 0 | 1 | false |
| `CreditCardToken` | `string` | 0 | 1 | false |
| `ExpirationMonth` | `int` | 1 | 1 | false |
| `ExpirationYear` | `int` | 1 | 1 | false |
| `CreditCardType` | `int` | 1 | 1 | false |
| `CreditCardTypeDescription` | `string` | 0 | 1 | false |
| `BillingName` | `string` | 0 | 1 | false |
| `BillingAddress` | `string` | 0 | 1 | false |
| `BillingCity` | `string` | 0 | 1 | false |
| `BillingState` | `string` | 0 | 1 | false |
| `BillingZip` | `string` | 0 | 1 | false |
| `BillingCountry` | `string` | 0 | 1 | false |
| `BillingAddress2` | `string` | 0 | 1 | false |

### CultureCodeItem

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CultureCode` | `string` | 0 | 1 | false |
| `ResourceItems` | `ArrayOfResourceItem` | 0 | 1 | false |

### CustomerBalanceResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CurrencyCode` | `string` | 0 | 1 | false |
| `CurrencyDescription` | `string` | 0 | 1 | false |
| `Balance` | `decimal` | 1 | 1 | false |

### CustomerEventField

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Name` | `string` | 0 | 1 | false |
| `Value` | `int` | 1 | 1 | false |

### CustomerEventResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `EventID` | `int` | 1 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | false |
| `EventDescription` | `string` | 0 | 1 | false |
| `Fields` | `ArrayOfCustomerEventField` | 0 | 1 | false |
| `EventDate` | `dateTime` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### CustomerExtendedResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `ExtendedGroupID` | `int` | 1 | 1 | false |
| `CustomerExtendedID` | `int` | 1 | 1 | false |
| `Field1` | `string` | 0 | 1 | false |
| `Field2` | `string` | 0 | 1 | false |
| `Field3` | `string` | 0 | 1 | false |
| `Field4` | `string` | 0 | 1 | false |
| `Field5` | `string` | 0 | 1 | false |
| `Field6` | `string` | 0 | 1 | false |
| `Field7` | `string` | 0 | 1 | false |
| `Field8` | `string` | 0 | 1 | false |
| `Field9` | `string` | 0 | 1 | false |
| `Field10` | `string` | 0 | 1 | false |
| `Field11` | `string` | 0 | 1 | false |
| `Field12` | `string` | 0 | 1 | false |
| `Field13` | `string` | 0 | 1 | false |
| `Field14` | `string` | 0 | 1 | false |
| `Field15` | `string` | 0 | 1 | false |
| `Field16` | `string` | 0 | 1 | false |
| `Field17` | `string` | 0 | 1 | false |
| `Field18` | `string` | 0 | 1 | false |
| `Field19` | `string` | 0 | 1 | false |
| `Field20` | `string` | 0 | 1 | false |
| `Field21` | `string` | 0 | 1 | false |
| `Field22` | `string` | 0 | 1 | false |
| `Field23` | `string` | 0 | 1 | false |
| `Field24` | `string` | 0 | 1 | false |
| `Field25` | `string` | 0 | 1 | false |
| `Field26` | `string` | 0 | 1 | false |
| `Field27` | `string` | 0 | 1 | false |
| `Field28` | `string` | 0 | 1 | false |
| `Field29` | `string` | 0 | 1 | false |
| `Field30` | `string` | 0 | 1 | false |
| `ModifiedDate` | `dateTime` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### CustomerFilesResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `FileName` | `string` | 0 | 1 | false |
| `FileID` | `int` | 1 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### CustomerFoldersResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `FolderID` | `int` | 1 | 1 | false |
| `FolderName` | `string` | 0 | 1 | false |
| `SubFoldersCount` | `int` | 1 | 1 | false |
| `SubFilesCount` | `int` | 1 | 1 | false |

### CustomerLeadSocialNetworkRequest

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SocialNetworkID` | `int` | 1 | 1 | false |
| `Url` | `string` | 0 | 1 | false |

### CustomerLeadSocialNetworksResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SocialNetworkID` | `int` | 1 | 1 | false |
| `SocialNetworkDescription` | `string` | 0 | 1 | false |
| `Url` | `string` | 0 | 1 | false |

### CustomerLeadsResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerLeadID` | `int` | 1 | 1 | false |
| `FirstName` | `string` | 0 | 1 | false |
| `LastName` | `string` | 0 | 1 | false |
| `MiddleName` | `string` | 0 | 1 | false |
| `Company` | `string` | 0 | 1 | false |
| `Phone` | `string` | 0 | 1 | false |
| `Phone2` | `string` | 0 | 1 | false |
| `MobilePhone` | `string` | 0 | 1 | false |
| `Fax` | `string` | 0 | 1 | false |
| `Email` | `string` | 0 | 1 | false |
| `Address1` | `string` | 0 | 1 | false |
| `Address2` | `string` | 0 | 1 | false |
| `City` | `string` | 0 | 1 | false |
| `State` | `string` | 0 | 1 | false |
| `Zip` | `string` | 0 | 1 | false |
| `Country` | `string` | 0 | 1 | false |
| `BirthDate` | `dateTime` | 1 | 1 | true |
| `Notes` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### CustomerNotesResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `Notes` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### CustomerResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `FirstName` | `string` | 0 | 1 | false |
| `LastName` | `string` | 0 | 1 | false |
| `Company` | `string` | 0 | 1 | false |
| `CustomerType` | `int` | 1 | 1 | false |
| `CustomerStatus` | `int` | 1 | 1 | false |
| `Email` | `string` | 0 | 1 | false |
| `Phone` | `string` | 0 | 1 | false |
| `Phone2` | `string` | 0 | 1 | false |
| `MobilePhone` | `string` | 0 | 1 | false |
| `Fax` | `string` | 0 | 1 | false |
| `MainAddress1` | `string` | 0 | 1 | false |
| `MainAddress2` | `string` | 0 | 1 | false |
| `MainCity` | `string` | 0 | 1 | false |
| `MainState` | `string` | 0 | 1 | false |
| `MainZip` | `string` | 0 | 1 | false |
| `MainCountry` | `string` | 0 | 1 | false |
| `MainCounty` | `string` | 0 | 1 | false |
| `MailAddress1` | `string` | 0 | 1 | false |
| `MailAddress2` | `string` | 0 | 1 | false |
| `MailCity` | `string` | 0 | 1 | false |
| `MailState` | `string` | 0 | 1 | false |
| `MailZip` | `string` | 0 | 1 | false |
| `MailCountry` | `string` | 0 | 1 | false |
| `MailCounty` | `string` | 0 | 1 | false |
| `OtherAddress1` | `string` | 0 | 1 | false |
| `OtherAddress2` | `string` | 0 | 1 | false |
| `OtherCity` | `string` | 0 | 1 | false |
| `OtherState` | `string` | 0 | 1 | false |
| `OtherZip` | `string` | 0 | 1 | false |
| `OtherCountry` | `string` | 0 | 1 | false |
| `OtherCounty` | `string` | 0 | 1 | false |
| `LoginName` | `string` | 0 | 1 | false |
| `EnrollerID` | `int` | 1 | 1 | false |
| `SponsorID` | `int` | 1 | 1 | false |
| `RankID` | `int` | 1 | 1 | false |
| `BirthDate` | `dateTime` | 1 | 1 | false |
| `Field1` | `string` | 0 | 1 | false |
| `Field2` | `string` | 0 | 1 | false |
| `Field3` | `string` | 0 | 1 | false |
| `Field4` | `string` | 0 | 1 | false |
| `Field5` | `string` | 0 | 1 | false |
| `Field6` | `string` | 0 | 1 | false |
| `Field7` | `string` | 0 | 1 | false |
| `Field8` | `string` | 0 | 1 | false |
| `Field9` | `string` | 0 | 1 | false |
| `Field10` | `string` | 0 | 1 | false |
| `Field11` | `string` | 0 | 1 | false |
| `Field12` | `string` | 0 | 1 | false |
| `Field13` | `string` | 0 | 1 | false |
| `Field14` | `string` | 0 | 1 | false |
| `Field15` | `string` | 0 | 1 | false |
| `Date1` | `dateTime` | 1 | 1 | true |
| `Date2` | `dateTime` | 1 | 1 | true |
| `Date3` | `dateTime` | 1 | 1 | true |
| `Date4` | `dateTime` | 1 | 1 | true |
| `Date5` | `dateTime` | 1 | 1 | true |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `PayableToName` | `string` | 0 | 1 | false |
| `DefaultWarehouseID` | `int` | 1 | 1 | false |
| `PayableType` | `PayableType` | 1 | 1 | false |
| `CheckThreshold` | `decimal` | 1 | 1 | false |
| `PriceType` | `int` | 1 | 1 | false |
| `LanguageID` | `int` | 1 | 1 | false |
| `Gender` | `Gender` | 1 | 1 | false |
| `SalesTaxID` | `string` | 0 | 1 | false |
| `VatRegistration` | `string` | 0 | 1 | false |
| `IsSalesTaxExempt` | `boolean` | 1 | 1 | false |
| `IsSubscribedToBroadcasts` | `boolean` | 1 | 1 | false |
| `CreatedDate` | `dateTime` | 1 | 1 | false |
| `ModifiedDate` | `dateTime` | 1 | 1 | false |
| `MiddleName` | `string` | 0 | 1 | false |
| `NameSuffix` | `string` | 0 | 1 | false |
| `MainAddress3` | `string` | 0 | 1 | false |
| `MailAddress3` | `string` | 0 | 1 | false |
| `OtherAddress3` | `string` | 0 | 1 | false |
| `BinaryPlacementPreference` | `int` | 1 | 1 | false |
| `UseBinaryHoldingTank` | `boolean` | 1 | 1 | false |
| `MainAddressVerified` | `boolean` | 1 | 1 | false |
| `MailAddressVerified` | `boolean` | 1 | 1 | false |
| `OtherAddressVerified` | `boolean` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `EnrollerKey` | `string` | 0 | 1 | false |
| `SponsorKey` | `string` | 0 | 1 | false |
| `PayableTyID` | `int` | 1 | 1 | false |
| `CanLogin` | `boolean` | 1 | 1 | false |
| `GenderID` | `string` | 0 | 1 | false |
| `GenderDescription` | `string` | 0 | 1 | false |

### CustomerSocialNetworkRequest

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SocialNetworkID` | `int` | 1 | 1 | false |
| `Url` | `string` | 0 | 1 | false |

### CustomerSocialNetworksResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SocialNetworkID` | `int` | 1 | 1 | false |
| `SocialNetworkDescription` | `string` | 0 | 1 | false |
| `Url` | `string` | 0 | 1 | false |

### CustomerWallItemResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `WallItemID` | `int` | 1 | 1 | false |
| `Text` | `string` | 0 | 1 | false |
| `EntryDate` | `dateTime` | 1 | 1 | false |
| `Field1` | `string` | 0 | 1 | false |
| `Field2` | `string` | 0 | 1 | false |
| `Field3` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### DateTimeOffset

_No fields._

### DebitBankAccountOnFileRequest
Extends `BaseDebitBankAccountRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderID` | `int` | 1 | 1 | false |
| `MaxAmount` | `decimal` | 1 | 1 | true |
| `OrderKey` | `string` | 0 | 1 | false |

### DebitBankAccountRequest
Extends `BaseDebitBankAccountRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `BankAccountNumber` | `string` | 0 | 1 | false |
| `BankRoutingNumber` | `string` | 0 | 1 | false |
| `BankName` | `string` | 0 | 1 | false |
| `BankAccountType` | `BankAccountType` | 1 | 1 | false |
| `CheckNumber` | `string` | 0 | 1 | false |
| `NameOnAccount` | `string` | 0 | 1 | false |
| `BillingAddress` | `string` | 0 | 1 | false |
| `BillingAddress2` | `string` | 0 | 1 | false |
| `BillingCity` | `string` | 0 | 1 | false |
| `BillingState` | `string` | 0 | 1 | false |
| `BillingZip` | `string` | 0 | 1 | false |
| `BillingCountry` | `string` | 0 | 1 | false |
| `Iban` | `string` | 0 | 1 | false |
| `SwiftCode` | `string` | 0 | 1 | false |
| `OrderID` | `int` | 1 | 1 | false |
| `MaxAmount` | `decimal` | 1 | 1 | true |
| `OrderKey` | `string` | 0 | 1 | false |

### DebitBankAccountResponse
Extends `CreatePaymentResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Amount` | `decimal` | 1 | 1 | false |
| `AuthorizationCode` | `string` | 0 | 1 | false |

### DeleteBankAccountTypeRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `BankAccountTyId` | `int` | 1 | 1 | false |

### DeleteBankAccountTypeResponse
Extends `ApiResponse`.

_No fields._

### DeleteCalendarItemRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `UserID` | `int` | 1 | 1 | false |
| `CalendarID` | `int` | 1 | 1 | false |
| `CalendarItemID` | `int` | 1 | 1 | false |

### DeleteCalendarItemResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CalendarID` | `int` | 1 | 1 | false |
| `CalendarItemID` | `int` | 1 | 1 | false |

### DeleteCustomerContactRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerContactID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### DeleteCustomerContactResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerContactID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### DeleteCustomerExtendedRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `ExtendedGroupID` | `int` | 1 | 1 | false |
| `CustomerExtendedID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### DeleteCustomerExtendedResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerExtendedID` | `int` | 1 | 1 | false |

### DeleteCustomerFileFolderRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `FileID` | `int` | 1 | 1 | true |
| `FolderID` | `int` | 1 | 1 | true |

### DeleteCustomerFileFolderResponse
Extends `ApiResponse`.

_No fields._

### DeleteCustomerLeadRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerLeadID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### DeleteCustomerLeadResponse
Extends `ApiResponse`.

_No fields._

### DeleteCustomerWallItemRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `WallItemID` | `int` | 1 | 1 | true |
| `OlderThanEntryDate` | `dateTime` | 1 | 1 | true |
| `CustomerKey` | `string` | 0 | 1 | false |

### DeleteCustomerWallItemResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CountOfDeletedRows` | `int` | 1 | 1 | false |

### DeleteDestinationRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DestinationID` | `int` | 1 | 1 | false |

### DeleteDestinationResponse
Extends `ApiResponse`.

_No fields._

### DeleteEmailRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `MailID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### DeleteEmailResponse
Extends `ApiResponse`.

_No fields._

### DeleteEmailTemplateRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `TemplateID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### DeleteEmailTemplateResponse
Extends `ApiResponse`.

_No fields._

### DeleteEntityRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SchemaName` | `string` | 0 | 1 | false |
| `EntityName` | `string` | 0 | 1 | false |

### DeleteEntityResponse
Extends `ApiResponse`.

_No fields._

### DeleteMailFolderRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `MailFolderID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### DeleteMailFolderResponse
Extends `ApiResponse`.

_No fields._

### DeleteOrderDetailRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderID` | `int` | 1 | 1 | false |
| `OrderLine` | `int` | 1 | 1 | false |
| `OrderKey` | `string` | 0 | 1 | false |

### DeleteOrderDetailResponse
Extends `ApiResponse`.

_No fields._

### DeleteProductFromCategoryRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `WebID` | `int` | 1 | 1 | false |
| `CategoryID` | `int` | 1 | 1 | false |
| `ItemCode` | `string` | 0 | 1 | false |

### DeleteProductFromCategoryResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CategoryID` | `int` | 1 | 1 | false |
| `WebID` | `int` | 1 | 1 | false |
| `ItemCode` | `string` | 0 | 1 | false |

### DeleteQualificationOverrideRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `OverrideID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### DeleteQualificationOverrideResponse
Extends `ApiResponse`.

_No fields._

### DeleteReleaseRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `Version` | `string` | 0 | 1 | false |

### DeleteReleaseResponse
Extends `ApiResponse`.

_No fields._

### DeleteResourceSetCultureRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `CultureCode` | `string` | 0 | 1 | false |

### DeleteResourceSetCultureResponse
Extends `ApiResponse`.

_No fields._

### DeleteResourceSetEnvironmentRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `EnvironmentCode` | `string` | 0 | 1 | false |

### DeleteResourceSetEnvironmentResponse
Extends `ApiResponse`.

_No fields._

### DeleteResourceSetGroupRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `ResourceGroupID` | `int` | 1 | 1 | false |
| `DeleteResources` | `boolean` | 1 | 1 | false |

### DeleteResourceSetGroupResponse
Extends `ApiResponse`.

_No fields._

### DeleteResourceSetItemRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `ResourceName` | `string` | 0 | 1 | false |
| `CultureCode` | `string` | 0 | 1 | false |

### DeleteResourceSetItemResponse
Extends `ApiResponse`.

_No fields._

### DeleteSchemaRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SchemaName` | `string` | 0 | 1 | false |

### DeleteSchemaResponse
Extends `ApiResponse`.

_No fields._

### DeleteWebCategoryRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `WebID` | `int` | 1 | 1 | false |
| `CategoryID` | `int` | 1 | 1 | false |

### DeleteWebCategoryResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CategoryID` | `int` | 1 | 1 | false |
| `WebID` | `int` | 1 | 1 | false |

### DepartmentInfo

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Description` | `string` | 0 | 1 | false |
| `DepartmentType` | `int` | 1 | 1 | false |

### DeployReleaseRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `EnvironmentCode` | `string` | 0 | 1 | false |
| `Version` | `string` | 0 | 1 | false |

### DeployReleaseResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `Version` | `string` | 0 | 1 | false |

### DequeueCustomerEventsRequest
Extends `ApiRequest`.

_No fields._

### DequeueCustomerEventsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerEvents` | `ArrayOfCustomerEventResponse` | 0 | 1 | false |

### Destination

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DestinationID` | `int` | 1 | 1 | false |
| `Name` | `string` | 0 | 1 | false |
| `Enabled` | `boolean` | 1 | 1 | false |
| `ConnectionString` | `string` | 0 | 1 | false |
| `ModifiedBy` | `string` | 0 | 1 | false |
| `ModifiedDate` | `dateTime` | 1 | 1 | false |
| `AlertSettings` | `AlertSettings` | 0 | 1 | false |
| `ReIndexSettings` | `ReIndexSettings` | 0 | 1 | false |

### DestinationTestResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CompanyId` | `int` | 1 | 1 | false |
| `RequestId` | `guid` | 1 | 1 | false |
| `RequestDate` | `dateTime` | 1 | 1 | false |
| `RequestedBy` | `string` | 0 | 1 | false |
| `ProcessMachine` | `string` | 0 | 1 | false |
| `ProcessDate` | `dateTime` | 1 | 1 | false |
| `CompleteDate` | `dateTime` | 1 | 1 | true |
| `Exception` | `string` | 0 | 1 | false |
| `Details` | `ArrayOfDestinationTestResponseDetail` | 0 | 1 | false |

### DestinationTestResponseDetail

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `RequestId` | `guid` | 1 | 1 | false |
| `Success` | `boolean` | 1 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `Exception` | `string` | 0 | 1 | false |

### DisableDestinationRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DestinationID` | `int` | 1 | 1 | false |

### DisableDestinationResponse
Extends `ApiResponse`.

_No fields._

### DisableFilterGroupRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DestinationID` | `int` | 1 | 1 | false |
| `FilterGroupID` | `TableGroupID` | 1 | 1 | false |

### DisableFilterGroupResponse
Extends `ApiResponse`.

_No fields._

### DisableFilteringRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DestinationID` | `int` | 1 | 1 | false |

### DisableFilteringResponse
Extends `ApiResponse`.

_No fields._

### EditBankAccountTypeRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `BankAccountTyId` | `int` | 1 | 1 | false |
| `Description` | `string` | 0 | 1 | false |

### EditBankAccountTypeResponse
Extends `ApiResponse`.

_No fields._

### EmailAttachment

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `BinaryData` | `base64Binary` | 0 | 1 | false |
| `FileName` | `string` | 0 | 1 | false |
| `ContentLength` | `int` | 1 | 1 | false |

### EmptyMailFolderRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `MailFolderID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### EmptyMailFolderResponse
Extends `ApiResponse`.

_No fields._

### EnableDestinationRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DestinationID` | `int` | 1 | 1 | false |

### EnableDestinationResponse
Extends `ApiResponse`.

_No fields._

### EnableFilterGroupRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DestinationID` | `int` | 1 | 1 | false |
| `FilterGroupID` | `TableGroupID` | 1 | 1 | false |

### EnableFilterGroupResponse
Extends `ApiResponse`.

_No fields._

### EnableFilteringRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DestinationID` | `int` | 1 | 1 | false |

### EnableFilteringResponse
Extends `ApiResponse`.

_No fields._

### EnsureMailFoldersRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### EnsureMailFoldersResponse
Extends `ApiResponse`.

_No fields._

### EntityDataResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `EntityName` | `string` | 0 | 1 | false |
| `EntitySetName` | `string` | 0 | 1 | false |
| `SchemaName` | `string` | 0 | 1 | false |
| `IsLog` | `boolean` | 1 | 1 | false |
| `MaxLogDays` | `int` | 1 | 1 | false |
| `LogDateField` | `string` | 0 | 1 | false |
| `Navigations` | `ArrayOfString` | 0 | 1 | false |
| `Properties` | `ArrayOfPropertyDataResponse` | 0 | 1 | false |

### ExpectedPaymentResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ExpectedPaymentID` | `int` | 1 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | false |
| `PaymentType` | `PaymentType` | 1 | 1 | false |
| `PaymentDate` | `dateTime` | 1 | 1 | false |
| `Amount` | `decimal` | 1 | 1 | false |
| `OrderID` | `int` | 1 | 1 | true |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `BillingName` | `string` | 0 | 1 | false |
| `AuthorizationCode` | `string` | 0 | 1 | false |
| `OrderKey` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `PaymentTypeId` | `int` | 1 | 1 | false |

### FilterGroup

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `TableGroupId` | `int` | 1 | 1 | false |
| `Enabled` | `boolean` | 1 | 1 | false |
| `TrueUp` | `boolean` | 1 | 1 | false |
| `Tables` | `ArrayOfTableName` | 0 | 1 | false |
| `TableFilterSettings` | `ArrayOfTableFilterSetting` | 0 | 1 | false |

### FireResponderRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResponderID` | `int` | 1 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | false |
| `OrderID` | `int` | 1 | 1 | true |
| `CustomerKey` | `string` | 0 | 1 | false |
| `OrderKey` | `string` | 0 | 1 | false |

### FireResponderResponse
Extends `ApiResponse`.

_No fields._

### ForwardedAttachment

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `MailID` | `int` | 1 | 1 | false |
| `AttachmentID` | `int` | 1 | 1 | false |

### FundPaymentCardRequest
Extends `BaseCreatePayoutRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PaymentCardTypeID` | `int` | 1 | 1 | false |
| `BillIDList` | `ArrayOfInt` | 0 | 1 | false |

### FundPaymentCardResponse
Extends `CreatePayoutResponse`.

_No fields._

### GetAccountDirectDepositRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### GetAccountDirectDepositResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `NameOnAccount` | `string` | 0 | 1 | false |
| `BankAccountNumberDisplay` | `string` | 0 | 1 | false |
| `BankRoutingNumber` | `string` | 0 | 1 | false |
| `DepositAccountType` | `DepositAccountType` | 1 | 1 | false |
| `BankName` | `string` | 0 | 1 | false |
| `BankAddress` | `string` | 0 | 1 | false |
| `BankCity` | `string` | 0 | 1 | false |
| `BankState` | `string` | 0 | 1 | false |
| `BankZip` | `string` | 0 | 1 | false |
| `BankCountry` | `string` | 0 | 1 | false |
| `BankAccountType` | `BankAccountType` | 1 | 1 | false |
| `Iban` | `string` | 0 | 1 | false |
| `SwiftCode` | `string` | 0 | 1 | false |
| `DepositAccountTypeID` | `int` | 1 | 1 | true |

### GetAdminWhitelistRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `IpRangeID` | `int` | 1 | 1 | true |

### GetAdminWhitelistResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `WhitelistRanges` | `ArrayOfAdminWhitelistResponse` | 0 | 1 | false |

### GetAlertSettingsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DestinationID` | `int` | 1 | 1 | false |

### GetAlertSettingsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `AlertOptIn` | `boolean` | 1 | 1 | false |
| `AlertEmail` | `ArrayOfString` | 0 | 1 | false |
| `AlertPhone` | `ArrayOfString` | 0 | 1 | false |

### GetApiWhitelistRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `IpRangeID` | `int` | 1 | 1 | true |

### GetApiWhitelistResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `WhitelistRanges` | `ArrayOfApiWhitelistResponse` | 0 | 1 | false |

### GetAutoOrdersRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `AutoOrderID` | `int` | 1 | 1 | true |
| `AutoOrderStatus` | `AutoOrderStatusType` | 1 | 1 | true |
| `CustomerKey` | `string` | 0 | 1 | false |

### GetAutoOrdersResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `AutoOrders` | `ArrayOfAutoOrderResponse` | 0 | 1 | false |

### GetBankAccountTypesRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `BankAccountTyId` | `int` | 1 | 1 | true |
| `Description` | `string` | 0 | 1 | false |

### GetBankAccountTypesResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `BankAccountTypes` | `ArrayOfBankAccountTypeResponse` | 0 | 1 | false |

### GetBillAmountsDueRequest
Extends `BaseBillPayoutOperationRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `StartDate` | `dateTime` | 1 | 1 | false |
| `EndDate` | `dateTime` | 1 | 1 | false |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `CountryCode` | `string` | 0 | 1 | false |
| `PayableType` | `int` | 1 | 1 | false |
| `PaymentCardType` | `int` | 1 | 1 | true |
| `MinimumAmount` | `decimal` | 1 | 1 | false |
| `MaximumAmount` | `decimal` | 1 | 1 | true |
| `Customers` | `ArrayOfInt` | 0 | 1 | false |

### GetBillAmountsDueResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `AmountsDue` | `ArrayOfBillAmount` | 0 | 1 | false |

### GetBillPaymentsRequest
Extends `BaseBillPayoutOperationRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PaymentIDs` | `ArrayOfInt` | 0 | 1 | false |
| `StartPaymentID` | `int` | 1 | 1 | true |
| `EndPaymentID` | `int` | 1 | 1 | true |

### GetBillPaymentsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `BillPayments` | `ArrayOfBillPayment` | 0 | 1 | false |

### GetBillPayoutQueueRequest
Extends `BaseBillPayoutOperationRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PayoutQueueRequestID` | `guid` | 1 | 1 | true |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `CountryCode` | `string` | 0 | 1 | false |
| `PayableType` | `int` | 1 | 1 | true |
| `PaymentCardType` | `int` | 1 | 1 | true |
| `StartDate` | `dateTime` | 1 | 1 | true |
| `EndDate` | `dateTime` | 1 | 1 | true |

### GetBillPayoutQueueResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `BillPayoutQueueItems` | `ArrayOfBillPayoutQueueItem` | 0 | 1 | false |

### GetBillsRequest
Extends `BaseBillPayoutOperationRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Customers` | `ArrayOfInt` | 0 | 1 | false |
| `Bills` | `ArrayOfInt` | 0 | 1 | false |
| `StartBillID` | `int` | 1 | 1 | true |
| `EndBillID` | `int` | 1 | 1 | true |
| `WarehouseID` | `int` | 1 | 1 | true |
| `StatusType` | `int` | 1 | 1 | true |
| `DatePaymentDueStart` | `dateTime` | 1 | 1 | true |
| `DatePaymentDueEnd` | `dateTime` | 1 | 1 | true |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `PayableType` | `int` | 1 | 1 | true |
| `TaxablePeriodType` | `int` | 1 | 1 | true |
| `TaxablePeriodID` | `int` | 1 | 1 | true |

### GetBillsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `BillItems` | `ArrayOfBillItem` | 0 | 1 | false |

### GetBinaryPreferenceRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### GetBinaryPreferenceResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `PlacementType` | `BinaryPlacementType` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### GetCommissionReportRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PeriodType` | `int` | 1 | 1 | false |
| `PeriodID` | `int` | 1 | 1 | true |
| `ReportName` | `string` | 0 | 1 | false |
| `ParameterData` | `string` | 0 | 1 | false |

### GetCommissionReportResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ReportData` | `string` | 0 | 1 | false |

### GetCompanyNewsItemRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `NewsID` | `int` | 1 | 1 | false |

### GetCompanyNewsItemResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Description` | `string` | 0 | 1 | false |
| `NewsID` | `int` | 1 | 1 | false |
| `CreatedDate` | `dateTime` | 1 | 1 | false |
| `WebSettings` | `NewsWebSettings` | 1 | 1 | false |
| `CompanySettings` | `NewsCompanySettings` | 1 | 1 | false |
| `Content` | `string` | 0 | 1 | false |
| `Departments` | `ArrayOfDepartmentInfo` | 0 | 1 | false |

### GetCompanyNewsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `StartDate` | `dateTime` | 1 | 1 | true |
| `EndDate` | `dateTime` | 1 | 1 | true |
| `DepartmentType` | `int` | 1 | 1 | true |

### GetCompanyNewsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CompanyNews` | `ArrayOfCompanyNewsResponse` | 0 | 1 | false |

### GetCountryRegionsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CountryCode` | `string` | 0 | 1 | false |

### GetCountryRegionsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Countries` | `ArrayOfCountryResponse` | 0 | 1 | false |
| `SelectedCountry` | `string` | 0 | 1 | false |
| `Regions` | `ArrayOfRegionResponse` | 0 | 1 | false |

### GetCustomReportRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ReportID` | `int` | 1 | 1 | false |
| `Parameters` | `ArrayOfParameterRequest` | 0 | 1 | false |

### GetCustomReportResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ReportData` | `` | 0 | 1 | false |
| `s:schema` | `` | 1 | 1 | false |

### GetCustomerBalancesRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### GetCustomerBalancesResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerBalances` | `ArrayOfCustomerBalanceResponse` | 0 | 1 | false |

### GetCustomerBillingRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### GetCustomerBillingResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PrimaryCreditCard` | `CreditCardAccountResponse` | 0 | 1 | false |
| `SecondaryCreditCard` | `CreditCardAccountResponse` | 0 | 1 | false |
| `BankAccount` | `BankAccountResponse` | 0 | 1 | false |
| `PrimaryWalletAccount` | `WalletAccountResponse` | 0 | 1 | false |
| `SecondaryWallletAccount` | `WalletAccountResponse` | 0 | 1 | false |
| `ThirdWalletAccount` | `WalletAccountResponse` | 0 | 1 | false |
| `FourthWalletAccount` | `WalletAccountResponse` | 0 | 1 | false |
| `FifthWalletAccount` | `WalletAccountResponse` | 0 | 1 | false |

### GetCustomerExtendedRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ExtendedGroupID` | `int` | 1 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | true |
| `CustomerExtendedID` | `int` | 1 | 1 | true |
| `Field1` | `string` | 1 | 1 | true |
| `Field2` | `string` | 1 | 1 | true |
| `Field3` | `string` | 1 | 1 | true |
| `Field4` | `string` | 1 | 1 | true |
| `Field5` | `string` | 1 | 1 | true |
| `Field6` | `string` | 1 | 1 | true |
| `Field7` | `string` | 1 | 1 | true |
| `Field8` | `string` | 1 | 1 | true |
| `Field9` | `string` | 1 | 1 | true |
| `Field10` | `string` | 1 | 1 | true |
| `Field11` | `string` | 1 | 1 | true |
| `Field12` | `string` | 1 | 1 | true |
| `Field13` | `string` | 1 | 1 | true |
| `Field14` | `string` | 1 | 1 | true |
| `Field15` | `string` | 1 | 1 | true |
| `Field16` | `string` | 1 | 1 | true |
| `Field17` | `string` | 1 | 1 | true |
| `Field18` | `string` | 1 | 1 | true |
| `Field19` | `string` | 1 | 1 | true |
| `Field20` | `string` | 1 | 1 | true |
| `Field21` | `string` | 1 | 1 | true |
| `Field22` | `string` | 1 | 1 | true |
| `Field23` | `string` | 1 | 1 | true |
| `Field24` | `string` | 1 | 1 | true |
| `Field25` | `string` | 1 | 1 | true |
| `Field26` | `string` | 1 | 1 | true |
| `Field27` | `string` | 1 | 1 | true |
| `Field28` | `string` | 1 | 1 | true |
| `Field29` | `string` | 1 | 1 | true |
| `Field30` | `string` | 1 | 1 | true |
| `GreaterThanCustomerExtendedID` | `int` | 1 | 1 | true |
| `GreaterThanModifiedDate` | `dateTime` | 1 | 1 | true |
| `BatchSize` | `int` | 1 | 1 | true |
| `CustomerKey` | `string` | 0 | 1 | false |

### GetCustomerExtendedResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Items` | `ArrayOfCustomerExtendedResponse` | 0 | 1 | false |

### GetCustomerFoldersRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `ParentFolderID` | `int` | 1 | 1 | true |

### GetCustomerFoldersResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `FolderCount` | `int` | 1 | 1 | false |
| `ParentFolderID` | `int` | 1 | 1 | false |
| `ParentFolderName` | `string` | 0 | 1 | false |
| `CustomerFolderList` | `ArrayOfCustomerFoldersResponse` | 0 | 1 | false |

### GetCustomerLeadSocialNetworksRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerLeadID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### GetCustomerLeadSocialNetworksResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerLeadSocialNetwork` | `ArrayOfCustomerLeadSocialNetworksResponse` | 0 | 1 | false |

### GetCustomerLeadsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerLeadID` | `int` | 1 | 1 | true |
| `GreaterThanCustomerLeadID` | `int` | 1 | 1 | true |
| `BatchSize` | `int` | 1 | 1 | true |
| `CustomerKey` | `string` | 0 | 1 | false |

### GetCustomerLeadsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerLeads` | `ArrayOfCustomerLeadsResponse` | 0 | 1 | false |

### GetCustomerNotesRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### GetCustomerNotesResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerNotes` | `ArrayOfCustomerNotesResponse` | 0 | 1 | false |

### GetCustomerSiteRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `WebAlias` | `string` | 0 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | true |
| `CustomerKey` | `string` | 0 | 1 | false |

### GetCustomerSiteResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `WebAlias` | `string` | 0 | 1 | false |
| `FirstName` | `string` | 0 | 1 | false |
| `LastName` | `string` | 0 | 1 | false |
| `Company` | `string` | 0 | 1 | false |
| `Address1` | `string` | 0 | 1 | false |
| `Address2` | `string` | 0 | 1 | false |
| `City` | `string` | 0 | 1 | false |
| `State` | `string` | 0 | 1 | false |
| `Zip` | `string` | 0 | 1 | false |
| `Country` | `string` | 0 | 1 | false |
| `Email` | `string` | 0 | 1 | false |
| `Phone` | `string` | 0 | 1 | false |
| `Phone2` | `string` | 0 | 1 | false |
| `Fax` | `string` | 0 | 1 | false |
| `Notes1` | `string` | 0 | 1 | false |
| `Notes2` | `string` | 0 | 1 | false |
| `Notes3` | `string` | 0 | 1 | false |
| `Notes4` | `string` | 0 | 1 | false |
| `Url1` | `string` | 0 | 1 | false |
| `Url2` | `string` | 0 | 1 | false |
| `Url3` | `string` | 0 | 1 | false |
| `Url4` | `string` | 0 | 1 | false |
| `Url5` | `string` | 0 | 1 | false |
| `Url6` | `string` | 0 | 1 | false |
| `Url7` | `string` | 0 | 1 | false |
| `Url8` | `string` | 0 | 1 | false |
| `Url9` | `string` | 0 | 1 | false |
| `Url10` | `string` | 0 | 1 | false |
| `Url1Description` | `string` | 0 | 1 | false |
| `Url2Description` | `string` | 0 | 1 | false |
| `Url3Description` | `string` | 0 | 1 | false |
| `Url4Description` | `string` | 0 | 1 | false |
| `Url5Description` | `string` | 0 | 1 | false |
| `Url6Description` | `string` | 0 | 1 | false |
| `Url7Description` | `string` | 0 | 1 | false |
| `Url8Description` | `string` | 0 | 1 | false |
| `Url9Description` | `string` | 0 | 1 | false |
| `Url10Description` | `string` | 0 | 1 | false |
| `Image1` | `string` | 0 | 1 | false |
| `Image2` | `string` | 0 | 1 | false |
| `ImageUrl1` | `string` | 0 | 1 | false |
| `ImageUrl2` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `DataImage1` | `base64Binary` | 0 | 1 | false |
| `DataImage2` | `base64Binary` | 0 | 1 | false |

### GetCustomerSocialNetworksRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### GetCustomerSocialNetworksResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerSocialNetwork` | `ArrayOfCustomerSocialNetworksResponse` | 0 | 1 | false |

### GetCustomerWallRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `WallItemID` | `int` | 1 | 1 | true |
| `OlderThanEntryDate` | `dateTime` | 1 | 1 | true |
| `BatchSize` | `int` | 1 | 1 | true |
| `CustomerKey` | `string` | 0 | 1 | false |

### GetCustomerWallResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerWallItems` | `ArrayOfCustomerWallItemResponse` | 0 | 1 | false |

### GetCustomersRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | true |
| `Company` | `string` | 1 | 1 | true |
| `FirstName` | `string` | 1 | 1 | true |
| `LastName` | `string` | 1 | 1 | true |
| `Email` | `string` | 1 | 1 | true |
| `Phone` | `string` | 1 | 1 | true |
| `Phone2` | `string` | 1 | 1 | true |
| `MobilePhone` | `string` | 1 | 1 | true |
| `Fax` | `string` | 1 | 1 | true |
| `MainAddress1` | `string` | 1 | 1 | true |
| `MainAddress2` | `string` | 1 | 1 | true |
| `MainAddress3` | `string` | 1 | 1 | true |
| `MainCity` | `string` | 1 | 1 | true |
| `MainState` | `string` | 1 | 1 | true |
| `MainZip` | `string` | 1 | 1 | true |
| `MainCountry` | `string` | 1 | 1 | true |
| `TaxID` | `string` | 1 | 1 | true |
| `CustomerTypes` | `ArrayOfInt` | 0 | 1 | false |
| `CustomerStatuses` | `ArrayOfInt` | 0 | 1 | false |
| `EnrollerID` | `int` | 1 | 1 | true |
| `SponsorID` | `int` | 1 | 1 | true |
| `Field1` | `string` | 1 | 1 | true |
| `Field10` | `string` | 1 | 1 | true |
| `Field11` | `string` | 1 | 1 | true |
| `Field12` | `string` | 1 | 1 | true |
| `Field13` | `string` | 1 | 1 | true |
| `Field14` | `string` | 1 | 1 | true |
| `Field15` | `string` | 1 | 1 | true |
| `Field2` | `string` | 1 | 1 | true |
| `Field3` | `string` | 1 | 1 | true |
| `Field4` | `string` | 1 | 1 | true |
| `Field5` | `string` | 1 | 1 | true |
| `Field6` | `string` | 1 | 1 | true |
| `Field7` | `string` | 1 | 1 | true |
| `Field8` | `string` | 1 | 1 | true |
| `Field9` | `string` | 1 | 1 | true |
| `GreaterThanCustomerID` | `int` | 1 | 1 | true |
| `GreaterThanModifiedDate` | `dateTime` | 1 | 1 | true |
| `BatchSize` | `int` | 1 | 1 | true |
| `LoginName` | `string` | 1 | 1 | true |
| `CreatedDateEnd` | `dateTime` | 1 | 1 | true |
| `CreatedDateStart` | `dateTime` | 1 | 1 | true |
| `CustomerKey` | `string` | 0 | 1 | false |
| `EnrollerKey` | `string` | 0 | 1 | false |
| `SponsorKey` | `string` | 0 | 1 | false |
| `SalesTaxID` | `string` | 1 | 1 | true |

### GetCustomersResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Customers` | `ArrayOfCustomerResponse` | 0 | 1 | false |
| `RecordCount` | `int` | 1 | 1 | false |

### GetDestinationTestRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `RequestId` | `guid` | 1 | 1 | false |

### GetDestinationTestResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Success` | `boolean` | 1 | 1 | false |
| `RequestId` | `guid` | 1 | 1 | false |
| `Data` | `DestinationTestResponse` | 0 | 1 | false |

### GetDestinationsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DestinationID` | `int` | 1 | 1 | true |

### GetDestinationsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Destinations` | `ArrayOfDestination` | 0 | 1 | false |

### GetDownlineRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `TreeType` | `TreeType` | 1 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | false |
| `PeriodType` | `int` | 1 | 1 | false |
| `PeriodID` | `int` | 1 | 1 | true |
| `MaxLevelDepth` | `int` | 1 | 1 | false |
| `CustomerTypes` | `ArrayOfInt` | 0 | 1 | false |
| `Ranks` | `ArrayOfInt` | 0 | 1 | false |
| `PayRanks` | `ArrayOfInt` | 0 | 1 | false |
| `VolumeFilters` | `ArrayOfVolumeFilter` | 0 | 1 | false |
| `CustomerStatusTypes` | `ArrayOfInt` | 0 | 1 | false |
| `BatchSize` | `int` | 1 | 1 | true |
| `SortByLevel` | `boolean` | 1 | 1 | false |
| `BatchOffset` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### GetDownlineResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Nodes` | `ArrayOfNodeResponse` | 0 | 1 | false |
| `RecordCount` | `int` | 1 | 1 | false |

### GetEmailAttachmentRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `MailID` | `int` | 1 | 1 | false |
| `AttachmentID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### GetEmailAttachmentResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `MailID` | `int` | 1 | 1 | false |
| `Attachment` | `EmailAttachment` | 0 | 1 | false |

### GetEntityRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SchemaName` | `string` | 0 | 1 | false |
| `EntityName` | `string` | 0 | 1 | false |

### GetEntityResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Entity` | `EntityDataResponse` | 0 | 1 | false |

### GetExtendedDbSettingsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DestinationID` | `int` | 1 | 1 | false |

### GetExtendedDbSettingsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ExcludedSchemas` | `ArrayOfString` | 0 | 1 | false |

### GetFileContentsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `FileName` | `string` | 0 | 1 | false |
| `FileID` | `int` | 1 | 1 | true |
| `ParentFolderID` | `int` | 1 | 1 | true |
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### GetFileContentsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `File` | `base64Binary` | 0 | 1 | false |

### GetFilesRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `ParentFolderID` | `int` | 1 | 1 | true |

### GetFilesResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `FileCount` | `int` | 1 | 1 | false |
| `ParentFolderID` | `int` | 1 | 1 | false |
| `ParentFolderName` | `string` | 0 | 1 | false |
| `CustomerFileList` | `ArrayOfCustomerFilesResponse` | 0 | 1 | false |

### GetFilterGroupRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DestinationID` | `int` | 1 | 1 | false |
| `FilterGroups` | `ArrayOfTableGroupID` | 0 | 1 | false |

### GetFilterGroupResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `FilterGroups` | `ArrayOfFilterGroup` | 0 | 1 | false |

### GetGuestSocialNetworksRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `GuestID` | `int` | 1 | 1 | false |

### GetGuestSocialNetworksResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `GuestSocialNetworks` | `ArrayOfGuestSocialNetworksResponse` | 0 | 1 | false |

### GetGuestsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `GuestID` | `int` | 1 | 1 | true |
| `CustomerID` | `int` | 1 | 1 | true |
| `HostID` | `int` | 1 | 1 | true |
| `GuestStatuses` | `ArrayOfInt` | 0 | 1 | false |
| `LanguageID` | `int` | 1 | 1 | true |
| `FirstName` | `string` | 1 | 1 | true |
| `MiddleName` | `string` | 1 | 1 | true |
| `LastName` | `string` | 1 | 1 | true |
| `NameSuffix` | `string` | 1 | 1 | true |
| `Company` | `string` | 1 | 1 | true |
| `Email` | `string` | 1 | 1 | true |
| `Phone` | `string` | 1 | 1 | true |
| `Phone2` | `string` | 1 | 1 | true |
| `MobilePhone` | `string` | 1 | 1 | true |
| `Address1` | `string` | 1 | 1 | true |
| `Address2` | `string` | 1 | 1 | true |
| `Address3` | `string` | 1 | 1 | true |
| `City` | `string` | 1 | 1 | true |
| `County` | `string` | 1 | 1 | true |
| `State` | `string` | 1 | 1 | true |
| `Zip` | `string` | 1 | 1 | true |
| `Country` | `string` | 1 | 1 | true |
| `Field1` | `string` | 1 | 1 | true |
| `Field2` | `string` | 1 | 1 | true |
| `Field3` | `string` | 1 | 1 | true |
| `Field4` | `string` | 1 | 1 | true |
| `Field5` | `string` | 1 | 1 | true |
| `Field6` | `string` | 1 | 1 | true |
| `Field7` | `string` | 1 | 1 | true |
| `Field8` | `string` | 1 | 1 | true |
| `Field9` | `string` | 1 | 1 | true |
| `Field10` | `string` | 1 | 1 | true |
| `Field11` | `string` | 1 | 1 | true |
| `Field12` | `string` | 1 | 1 | true |
| `Field13` | `string` | 1 | 1 | true |
| `Field14` | `string` | 1 | 1 | true |
| `Field15` | `string` | 1 | 1 | true |
| `Date1` | `dateTime` | 1 | 1 | true |
| `Date2` | `dateTime` | 1 | 1 | true |
| `Date3` | `dateTime` | 1 | 1 | true |
| `Date4` | `dateTime` | 1 | 1 | true |
| `Date5` | `dateTime` | 1 | 1 | true |
| `CreatedDateStart` | `dateTime` | 1 | 1 | true |
| `CreatedDateEnd` | `dateTime` | 1 | 1 | true |
| `CustomerKey` | `string` | 0 | 1 | false |

### GetGuestsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Guests` | `ArrayOfGuestResponse` | 0 | 1 | false |

### GetItemCountryRegionRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ItemCode` | `string` | 0 | 1 | false |

### GetItemCountryRegionResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ItemCountryRegions` | `ArrayOfItemCountryRegionResponse` | 0 | 1 | false |

### GetItemsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CurrencyCode` | `string` | 0 | 1 | false |
| `PriceType` | `int` | 1 | 1 | false |
| `WarehouseID` | `int` | 1 | 1 | false |
| `ItemCodes` | `ArrayOfString` | 0 | 1 | false |
| `WebID` | `int` | 1 | 1 | true |
| `WebCategoryID` | `int` | 1 | 1 | true |
| `ReturnLongDetail` | `boolean` | 1 | 1 | false |
| `RestrictToWarehouse` | `boolean` | 1 | 1 | true |
| `LanguageID` | `int` | 1 | 1 | true |
| `ExcludeHideFromSearch` | `boolean` | 1 | 1 | true |

### GetItemsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Items` | `ArrayOfItemResponse` | 0 | 1 | false |

### GetLanguagesRequest
Extends `ApiRequest`.

_No fields._

### GetLanguagesResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CompanyLanguages` | `ArrayOfLanguageResponse` | 0 | 1 | false |

### GetLoginSessionRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SessionID` | `string` | 0 | 1 | false |

### GetLoginSessionResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `FirstName` | `string` | 0 | 1 | false |
| `LastName` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### GetOrderInvoiceBatchRequest
Extends `BaseGetOrderInvoiceRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ReportlayoutID` | `int` | 1 | 1 | false |
| `BatchId` | `int` | 1 | 1 | false |
| `WarehouseId` | `int` | 1 | 1 | false |

### GetOrderInvoiceRequest
Extends `BaseGetOrderInvoiceRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderID` | `int` | 1 | 1 | false |
| `OrderKey` | `string` | 0 | 1 | false |
| `ReportlayoutID` | `int` | 1 | 1 | false |
| `Format` | `InvoiceRenderFormat` | 1 | 1 | false |
| `AutoOrderID` | `int` | 1 | 1 | true |

### GetOrderInvoiceResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `InvoiceData` | `base64Binary` | 0 | 1 | false |

### GetOrderTotalsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `StartDate` | `dateTime` | 1 | 1 | false |
| `EndDate` | `dateTime` | 1 | 1 | false |

### GetOrderTotalsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `StartDate` | `dateTime` | 1 | 1 | false |
| `EndDate` | `dateTime` | 1 | 1 | false |
| `AcceptedByCurrency` | `ArrayOfOrderTotalByCurrency` | 0 | 1 | false |

### GetOrdersRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | true |
| `OrderID` | `int` | 1 | 1 | true |
| `OrderIDs` | `ArrayOfInt` | 0 | 1 | false |
| `OrderDateStart` | `dateTime` | 1 | 1 | true |
| `OrderDateEnd` | `dateTime` | 1 | 1 | true |
| `OrderStatus` | `OrderStatusType` | 1 | 1 | true |
| `OtherOrderStatuses` | `ArrayOfOrderStatusType` | 0 | 1 | false |
| `OrderTypes` | `ArrayOfOrderType` | 0 | 1 | false |
| `WarehouseID` | `int` | 1 | 1 | true |
| `CurrencyCode` | `string` | 1 | 1 | true |
| `ReturnCustomer` | `boolean` | 1 | 1 | true |
| `ReturnKitDetails` | `boolean` | 1 | 1 | true |
| `GreaterThanOrderID` | `int` | 1 | 1 | true |
| `GreaterThanModifiedDate` | `dateTime` | 1 | 1 | true |
| `BatchSize` | `int` | 1 | 1 | true |
| `Other11` | `string` | 0 | 1 | false |
| `Other12` | `string` | 0 | 1 | false |
| `Other13` | `string` | 0 | 1 | false |
| `Other14` | `string` | 0 | 1 | false |
| `Other15` | `string` | 0 | 1 | false |
| `Other16` | `string` | 0 | 1 | false |
| `Other17` | `string` | 0 | 1 | false |
| `Other18` | `string` | 0 | 1 | false |
| `Other19` | `string` | 0 | 1 | false |
| `Other20` | `string` | 0 | 1 | false |
| `PartyID` | `int` | 1 | 1 | true |
| `CustomerKey` | `string` | 0 | 1 | false |
| `OrderKey` | `string` | 0 | 1 | false |
| `OrderKeys` | `ArrayOfString` | 0 | 1 | false |
| `OrderSubStatusTy` | `int` | 1 | 1 | true |
| `BatchID` | `int` | 1 | 1 | true |
| `OrderTys` | `ArrayOfString` | 0 | 1 | false |
| `ReferralID` | `int` | 1 | 1 | true |

### GetOrdersResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Orders` | `ArrayOfOrderResponse` | 0 | 1 | false |
| `RecordCount` | `int` | 1 | 1 | false |

### GetPartiesRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PartyID` | `int` | 1 | 1 | true |
| `HostID` | `int` | 1 | 1 | true |
| `DistributorID` | `int` | 1 | 1 | true |
| `PartyStatusType` | `int` | 1 | 1 | true |
| `BookingPartyID` | `int` | 1 | 1 | true |
| `Field1` | `string` | 0 | 1 | false |
| `Field2` | `string` | 0 | 1 | false |
| `Field3` | `string` | 0 | 1 | false |
| `Field4` | `string` | 0 | 1 | false |
| `Field5` | `string` | 0 | 1 | false |
| `PartyExternalID` | `guid` | 1 | 1 | true |

### GetPartiesResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Parties` | `ArrayOfPartyResponse` | 0 | 1 | false |

### GetPartyGuestsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PartyID` | `int` | 1 | 1 | false |

### GetPartyGuestsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Guests` | `ArrayOfGuestResponse` | 0 | 1 | false |

### GetPaymentsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | true |
| `OrderID` | `int` | 1 | 1 | true |
| `CustomerKey` | `string` | 0 | 1 | false |
| `OrderKey` | `string` | 0 | 1 | false |

### GetPaymentsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Payments` | `ArrayOfPaymentResponse` | 0 | 1 | false |

### GetPointAccountRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PointAccountID` | `int` | 1 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### GetPointAccountResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Balance` | `decimal` | 1 | 1 | false |

### GetQualificationOverrideResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `OverrideID` | `int` | 1 | 1 | false |
| `Qualifies` | `boolean` | 1 | 1 | false |
| `PeriodType` | `int` | 1 | 1 | true |
| `StartPeriodID` | `int` | 1 | 1 | true |
| `EndPeriodID` | `int` | 1 | 1 | true |
| `ModifiedDate` | `dateTime` | 1 | 1 | false |
| `ModifiedBy` | `string` | 0 | 1 | false |
| `Amount` | `decimal` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### GetQualificationOverridesRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | true |
| `OverrideID` | `int` | 1 | 1 | true |
| `BatchSize` | `int` | 1 | 1 | true |
| `CustomerKey` | `string` | 0 | 1 | false |

### GetQualitificationOverridesResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `QualificationOverrides` | `ArrayOfGetQualificationOverrideResponse` | 0 | 1 | false |

### GetRandomMessageRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `LanguageID` | `int` | 1 | 1 | false |

### GetRandomMessageResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `RandomMessageID` | `int` | 1 | 1 | false |
| `Content` | `string` | 0 | 1 | false |

### GetRankQualificationsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `RankID` | `int` | 1 | 1 | false |
| `PeriodType` | `int` | 1 | 1 | false |
| `PeriodID` | `int` | 1 | 1 | true |
| `CultureCode` | `string` | 0 | 1 | false |
| `RankGroupID` | `int` | 1 | 1 | true |
| `CustomerKey` | `string` | 0 | 1 | false |

### GetRankQualificationsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `RankID` | `int` | 1 | 1 | false |
| `RankDescription` | `string` | 0 | 1 | false |
| `Qualifies` | `boolean` | 1 | 1 | false |
| `QualifiesOverride` | `boolean` | 1 | 1 | true |
| `PayeeQualificationLegs` | `ArrayOfArrayOfQualificationResponse` | 0 | 1 | false |
| `BackRankID` | `int` | 1 | 1 | true |
| `BackRankDescription` | `string` | 0 | 1 | false |
| `NextRankID` | `int` | 1 | 1 | true |
| `NextRankDescription` | `string` | 0 | 1 | false |
| `Score` | `decimal` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### GetReIndexHistoryRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DestinationId` | `int` | 1 | 1 | false |
| `PageNumber` | `int` | 1 | 1 | false |

### GetReIndexHistoryResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ReIndexHistoryItems` | `ArrayOfReIndexHistoryItem` | 0 | 1 | false |

### GetReIndexSettingsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DestinationID` | `int` | 1 | 1 | false |

### GetReIndexSettingsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ReIndexStartTime` | `dateTime` | 1 | 1 | true |
| `ReIndexMaxDuration` | `int` | 1 | 1 | true |
| `LastReIndexed` | `dateTime` | 1 | 1 | true |
| `ReIndexError` | `string` | 0 | 1 | false |

### GetRealTimeCommissionDetailRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `PeriodType` | `int` | 1 | 1 | false |
| `PeriodID` | `int` | 1 | 1 | false |
| `BonusID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### GetRealTimeCommissionDetailResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CommissionDetails` | `ArrayOfCommissionDetailResponse` | 0 | 1 | false |

### GetRealTimeCommissionsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### GetRealTimeCommissionsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Commissions` | `ArrayOfCommissionResponse` | 0 | 1 | false |

### GetReleasesRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |

### GetReleasesResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Releases` | `ArrayOfResourceSetRelease` | 0 | 1 | false |

### GetReportRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ReportID` | `int` | 1 | 1 | false |
| `Parameters` | `ArrayOfReportParameterRequest` | 0 | 1 | false |

### GetReportResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ReportData` | `` | 0 | 1 | false |
| `s:schema` | `` | 1 | 1 | false |

### GetResourceSetCulturesRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SubscriptionKey` | `string` | 0 | 1 | false |
| `Version` | `string` | 0 | 1 | false |
| `ResourceSetID` | `int` | 1 | 1 | true |

### GetResourceSetCulturesResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Cultures` | `ArrayOfResourceSetCulture` | 0 | 1 | false |

### GetResourceSetEnvironmentsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |

### GetResourceSetEnvironmentsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Environments` | `ArrayOfResourceSetEnvironment` | 0 | 1 | false |

### GetResourceSetGroupsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |

### GetResourceSetGroupsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Groups` | `ArrayOfResourceGroup` | 0 | 1 | false |

### GetResourceSetItemsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SubscriptionKey` | `string` | 0 | 1 | false |
| `Version` | `string` | 0 | 1 | false |
| `CultureCode` | `string` | 0 | 1 | false |
| `ResourceSetID` | `int` | 1 | 1 | true |

### GetResourceSetItemsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Items` | `ArrayOfResourceItem` | 0 | 1 | false |

### GetResourceSetSubscriptionUpdatesRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSubscriptions` | `ArrayOfResourceSetSubscriptionCheckIn` | 0 | 1 | false |
| `Full` | `boolean` | 1 | 1 | false |

### GetResourceSetSubscriptionUpdatesResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Updates` | `ArrayOfResourceSubscriptionUpdate` | 0 | 1 | false |

### GetResourceSetsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | true |

### GetResourceSetsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSets` | `ArrayOfResourceSet` | 0 | 1 | false |

### GetSQLReportRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ReportID` | `int` | 1 | 1 | false |
| `ReportEngineVersion` | `int` | 1 | 1 | false |
| `Parameters` | `ArrayOfParameterRequest` | 0 | 1 | false |

### GetSQLReportResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ReportData` | `` | 0 | 1 | false |
| `s:schema` | `` | 1 | 1 | false |

### GetSandboxRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SandboxID` | `int` | 1 | 1 | true |

### GetSandboxResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Sandbox` | `Sandbox` | 0 | 1 | false |
| `Sandboxes` | `ArrayOfSandbox` | 0 | 1 | false |

### GetSchemaRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SchemaName` | `string` | 0 | 1 | false |

### GetSchemaResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Schema` | `SchemaDataResponse` | 0 | 1 | false |

### GetSessionRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SessionID` | `string` | 0 | 1 | false |

### GetSessionResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SessionData` | `string` | 0 | 1 | false |

### GetShipMethodsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `WarehouseID` | `int` | 1 | 1 | false |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `OrderSubTotal` | `decimal` | 1 | 1 | false |
| `OrderWieght` | `decimal` | 1 | 1 | false |

### GetShipMethodsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ShipMethods` | `ArrayOfShipMethodResponse` | 0 | 1 | false |

### GetShoppingCartRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ShoppingID` | `string` | 0 | 1 | false |

### GetShoppingCartResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ExistingOrderID` | `int` | 1 | 1 | false |
| `ExistingAutoOrderID` | `int` | 1 | 1 | false |
| `Details` | `ArrayOfOrderDetailResponse` | 0 | 1 | false |

### GetSubscriptionRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SubscriptionID` | `int` | 1 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### GetSubscriptionResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Status` | `SubscriptionStatus` | 1 | 1 | false |
| `StartDate` | `dateTime` | 1 | 1 | false |
| `ExpireDate` | `dateTime` | 1 | 1 | false |

### GetSubscriptionsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `IncludeInactive` | `boolean` | 1 | 1 | false |

### GetSubscriptionsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Subscriptions` | `ArrayOfSubscriptionResponse` | 0 | 1 | false |

### GetTableSettingsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DestinationID` | `int` | 1 | 1 | false |

### GetTableSettingsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `TableSettings` | `ArrayOfTableSettings` | 0 | 1 | false |

### GetUplineRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `TreeType` | `TreeType` | 1 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | false |
| `PeriodType` | `int` | 1 | 1 | false |
| `PeriodID` | `int` | 1 | 1 | true |
| `CustomerKey` | `string` | 0 | 1 | false |
| `BatchSize` | `int` | 1 | 1 | true |
| `BatchOffset` | `int` | 1 | 1 | true |

### GetUplineResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Nodes` | `ArrayOfNodeResponse` | 0 | 1 | false |

### GetUserPermissionsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `LoginName` | `string` | 0 | 1 | false |

### GetUserPermissionsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `RestrictToCustomerTypes` | `ArrayOfInt` | 0 | 1 | false |
| `RestrictToCustomerStatuses` | `ArrayOfInt` | 0 | 1 | false |
| `RestrictToWarehouses` | `ArrayOfInt` | 0 | 1 | false |
| `RestrictToCountries` | `ArrayOfString` | 0 | 1 | false |
| `RestrictToCurrencies` | `ArrayOfString` | 0 | 1 | false |
| `ViewDeletedCustomers` | `boolean` | 1 | 1 | false |
| `AllowRemoteCheckPrint` | `boolean` | 1 | 1 | false |
| `AllowOverrideItemPrice` | `boolean` | 1 | 1 | false |
| `AllowStatementPrint` | `boolean` | 1 | 1 | false |
| `DefaultWarehouseID` | `int` | 1 | 1 | false |
| `LanguageID` | `int` | 1 | 1 | false |
| `CultureCode` | `string` | 0 | 1 | false |

### GetVolumesRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PeriodType` | `int` | 1 | 1 | false |
| `PeriodID` | `int` | 1 | 1 | true |
| `CustomerID` | `int` | 1 | 1 | true |
| `CustomerKey` | `string` | 0 | 1 | false |

### GetVolumesResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Volumes` | `ArrayOfVolumeResponse` | 0 | 1 | false |

### GetWarehousesRequest
Extends `ApiRequest`.

_No fields._

### GetWarehousesResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Warehouses` | `ArrayOfWarehouseResponse` | 0 | 1 | false |

### GroupOrder

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderID` | `int` | 1 | 1 | false |
| `MaxAmount` | `decimal` | 1 | 1 | true |
| `OrderKey` | `string` | 0 | 1 | false |

### GuestResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `GuestID` | `int` | 1 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | false |
| `HostID` | `int` | 1 | 1 | false |
| `FirstName` | `string` | 0 | 1 | false |
| `MiddleName` | `string` | 0 | 1 | false |
| `LastName` | `string` | 0 | 1 | false |
| `NameSuffix` | `string` | 0 | 1 | false |
| `Company` | `string` | 0 | 1 | false |
| `Gender` | `Gender` | 1 | 1 | false |
| `GuestStatus` | `int` | 1 | 1 | false |
| `LanguageID` | `int` | 1 | 1 | true |
| `Address1` | `string` | 0 | 1 | false |
| `Address2` | `string` | 0 | 1 | false |
| `Address3` | `string` | 0 | 1 | false |
| `City` | `string` | 0 | 1 | false |
| `County` | `string` | 0 | 1 | false |
| `State` | `string` | 0 | 1 | false |
| `Zip` | `string` | 0 | 1 | false |
| `Country` | `string` | 0 | 1 | false |
| `Phone` | `string` | 0 | 1 | false |
| `Phone2` | `string` | 0 | 1 | false |
| `MobilePhone` | `string` | 0 | 1 | false |
| `Email` | `string` | 0 | 1 | false |
| `Field1` | `string` | 0 | 1 | false |
| `Field2` | `string` | 0 | 1 | false |
| `Field3` | `string` | 0 | 1 | false |
| `Field4` | `string` | 0 | 1 | false |
| `Field5` | `string` | 0 | 1 | false |
| `Field6` | `string` | 0 | 1 | false |
| `Field7` | `string` | 0 | 1 | false |
| `Field8` | `string` | 0 | 1 | false |
| `Field9` | `string` | 0 | 1 | false |
| `Field10` | `string` | 0 | 1 | false |
| `Field11` | `string` | 0 | 1 | false |
| `Field12` | `string` | 0 | 1 | false |
| `Field13` | `string` | 0 | 1 | false |
| `Field14` | `string` | 0 | 1 | false |
| `Field15` | `string` | 0 | 1 | false |
| `Date1` | `dateTime` | 1 | 1 | true |
| `Date2` | `dateTime` | 1 | 1 | true |
| `Date3` | `dateTime` | 1 | 1 | true |
| `Date4` | `dateTime` | 1 | 1 | true |
| `Date5` | `dateTime` | 1 | 1 | true |
| `CreatedDate` | `dateTime` | 1 | 1 | false |
| `ModifiedDate` | `dateTime` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `GenderID` | `string` | 0 | 1 | false |
| `GenderDescription` | `string` | 0 | 1 | false |

### GuestSocialNetworkRequest

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SocialNetworkID` | `int` | 1 | 1 | false |
| `Url` | `string` | 0 | 1 | false |

### GuestSocialNetworksResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SocialNetworkID` | `int` | 1 | 1 | false |
| `SocialNetworkDescription` | `string` | 0 | 1 | false |
| `Url` | `string` | 0 | 1 | false |

### IsEnrollerChildValidateRequest
Extends `ValidateRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ParentID` | `int` | 1 | 1 | false |
| `ChildID` | `int` | 1 | 1 | false |

### IsLoginNameAvailableValidateRequest
Extends `ValidateRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `LoginName` | `string` | 0 | 1 | false |

### IsMatrixChildValidateRequest
Extends `ValidateRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ParentID` | `int` | 1 | 1 | false |
| `ChildID` | `int` | 1 | 1 | false |

### IsTaxIDAvailableValidateRequest
Extends `ValidateRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `TaxID` | `string` | 0 | 1 | false |
| `TaxTypeID` | `int` | 1 | 1 | false |
| `ExcludeCustomerID` | `int` | 1 | 1 | false |

### IsUniLevelChildValidateRequest
Extends `ValidateRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ParentID` | `int` | 1 | 1 | false |
| `ParentKey` | `string` | 0 | 1 | false |
| `ChildID` | `int` | 1 | 1 | false |
| `ChildKey` | `string` | 0 | 1 | false |

### ItemCountryRegionResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ItemCode` | `string` | 0 | 1 | false |
| `CountryCode` | `string` | 0 | 1 | false |
| `RegionCode` | `string` | 0 | 1 | false |
| `Taxed` | `boolean` | 1 | 1 | true |
| `TaxedFed` | `boolean` | 1 | 1 | true |
| `TaxedState` | `boolean` | 1 | 1 | true |
| `UseTaxOverride` | `boolean` | 1 | 1 | true |
| `TaxOverridePct` | `decimal` | 1 | 1 | true |

### ItemMemberResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ItemCode` | `string` | 0 | 1 | false |
| `MemberDescription` | `string` | 0 | 1 | false |
| `ItemDescription` | `string` | 0 | 1 | false |
| `InventoryStatus` | `InventoryStatusType` | 1 | 1 | false |
| `StockLevel` | `int` | 1 | 1 | false |
| `AvailableStockLevel` | `int` | 1 | 1 | false |

### ItemResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ItemCode` | `string` | 0 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `Price` | `decimal` | 1 | 1 | false |
| `Weight` | `decimal` | 1 | 1 | false |
| `CommissionableVolume` | `decimal` | 1 | 1 | false |
| `BusinessVolume` | `decimal` | 1 | 1 | false |
| `Other1Price` | `decimal` | 1 | 1 | false |
| `Other2Price` | `decimal` | 1 | 1 | false |
| `Other3Price` | `decimal` | 1 | 1 | false |
| `Other4Price` | `decimal` | 1 | 1 | false |
| `Other5Price` | `decimal` | 1 | 1 | false |
| `Other6Price` | `decimal` | 1 | 1 | false |
| `Other7Price` | `decimal` | 1 | 1 | false |
| `Other8Price` | `decimal` | 1 | 1 | false |
| `Other9Price` | `decimal` | 1 | 1 | false |
| `Other10Price` | `decimal` | 1 | 1 | false |
| `Category` | `string` | 0 | 1 | false |
| `CategoryID` | `int` | 1 | 1 | false |
| `TinyPicture` | `string` | 0 | 1 | false |
| `SmallPicture` | `string` | 0 | 1 | false |
| `LargePicture` | `string` | 0 | 1 | false |
| `ShortDetail` | `string` | 0 | 1 | false |
| `ShortDetail2` | `string` | 0 | 1 | false |
| `ShortDetail3` | `string` | 0 | 1 | false |
| `ShortDetail4` | `string` | 0 | 1 | false |
| `LongDetail` | `string` | 0 | 1 | false |
| `LongDetail2` | `string` | 0 | 1 | false |
| `LongDetail3` | `string` | 0 | 1 | false |
| `LongDetail4` | `string` | 0 | 1 | false |
| `InventoryStatus` | `InventoryStatusType` | 1 | 1 | false |
| `StockLevel` | `int` | 1 | 1 | false |
| `AvailableStockLevel` | `int` | 1 | 1 | false |
| `MaxAllowedOnOrder` | `int` | 1 | 1 | false |
| `Field1` | `string` | 0 | 1 | false |
| `Field2` | `string` | 0 | 1 | false |
| `Field3` | `string` | 0 | 1 | false |
| `Field4` | `string` | 0 | 1 | false |
| `Field5` | `string` | 0 | 1 | false |
| `Field6` | `string` | 0 | 1 | false |
| `Field7` | `string` | 0 | 1 | false |
| `Field8` | `string` | 0 | 1 | false |
| `Field9` | `string` | 0 | 1 | false |
| `Field10` | `string` | 0 | 1 | false |
| `OtherCheck1` | `boolean` | 1 | 1 | false |
| `OtherCheck2` | `boolean` | 1 | 1 | false |
| `OtherCheck3` | `boolean` | 1 | 1 | false |
| `OtherCheck4` | `boolean` | 1 | 1 | false |
| `OtherCheck5` | `boolean` | 1 | 1 | false |
| `IsVirtual` | `boolean` | 1 | 1 | false |
| `AllowOnAutoOrder` | `boolean` | 1 | 1 | false |
| `IsGroupMaster` | `boolean` | 1 | 1 | false |
| `GroupDescription` | `string` | 0 | 1 | false |
| `GroupMembersDescription` | `string` | 0 | 1 | false |
| `GroupMembers` | `ArrayOfItemMemberResponse` | 0 | 1 | false |
| `IsDynamicKitMaster` | `boolean` | 1 | 1 | false |
| `HideFromSearch` | `boolean` | 1 | 1 | false |
| `KitMembers` | `ArrayOfKitMemberResponse` | 0 | 1 | false |
| `TaxablePrice` | `decimal` | 1 | 1 | false |
| `ShippingPrice` | `decimal` | 1 | 1 | false |

### KitMember

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ItemID` | `int` | 1 | 1 | false |
| `ItemCode` | `string` | 0 | 1 | false |
| `Quantity` | `int` | 1 | 1 | false |

### KitMemberItemResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ItemCode` | `string` | 0 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `InventoryStatus` | `InventoryStatusType` | 1 | 1 | false |

### KitMemberResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Description` | `string` | 0 | 1 | false |
| `KitMemberItems` | `ArrayOfKitMemberItemResponse` | 0 | 1 | false |

### LanguageResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `LanguageID` | `int` | 1 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `CultureCode` | `string` | 0 | 1 | false |

### LoginCustomerRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `LoginName` | `string` | 0 | 1 | false |
| `Password` | `string` | 0 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### LoginCustomerResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SessionID` | `string` | 0 | 1 | false |

### MaskTypeDataResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `MaskTypeId` | `int` | 1 | 1 | false |
| `Name` | `string` | 0 | 1 | false |
| `Description` | `string` | 0 | 1 | false |

### MergeCustomerRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ToCustomerID` | `int` | 1 | 1 | false |
| `FromCustomerID` | `int` | 1 | 1 | false |
| `ToCustomerKey` | `string` | 0 | 1 | false |
| `FromCustomerKey` | `string` | 0 | 1 | false |

### MergeCustomerResponse
Extends `ApiResponse`.

_No fields._

### MoveCustomerFileRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `FileID` | `int` | 1 | 1 | true |
| `FolderID` | `int` | 1 | 1 | true |

### MoveCustomerFileResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `FileID` | `int` | 1 | 1 | false |
| `FolderID` | `int` | 1 | 1 | false |

### MoveEmailRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `MailID` | `int` | 1 | 1 | false |
| `ToMailFolderID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### MoveEmailResponse
Extends `ApiResponse`.

_No fields._

### NodeResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `NodeID` | `int` | 1 | 1 | false |
| `ParentID` | `int` | 1 | 1 | false |
| `Level` | `int` | 1 | 1 | false |
| `Position` | `int` | 1 | 1 | false |
| `CustomerType` | `int` | 1 | 1 | false |
| `CustomerStatus` | `int` | 1 | 1 | false |
| `RankID` | `int` | 1 | 1 | false |
| `PayRankID` | `int` | 1 | 1 | false |
| `FirstName` | `string` | 0 | 1 | false |
| `LastName` | `string` | 0 | 1 | false |
| `Company` | `string` | 0 | 1 | false |
| `Email` | `string` | 0 | 1 | false |
| `Phone` | `string` | 0 | 1 | false |
| `CreatedDate` | `dateTime` | 1 | 1 | false |
| `Volume1` | `decimal` | 1 | 1 | false |
| `Volume2` | `decimal` | 1 | 1 | false |
| `Volume3` | `decimal` | 1 | 1 | false |
| `Volume4` | `decimal` | 1 | 1 | false |
| `Volume5` | `decimal` | 1 | 1 | false |
| `Volume6` | `decimal` | 1 | 1 | false |
| `Volume7` | `decimal` | 1 | 1 | false |
| `Volume8` | `decimal` | 1 | 1 | false |
| `Volume9` | `decimal` | 1 | 1 | false |
| `Volume10` | `decimal` | 1 | 1 | false |
| `Volume11` | `decimal` | 1 | 1 | false |
| `Volume12` | `decimal` | 1 | 1 | false |
| `Volume13` | `decimal` | 1 | 1 | false |
| `Volume14` | `decimal` | 1 | 1 | false |
| `Volume15` | `decimal` | 1 | 1 | false |
| `Volume16` | `decimal` | 1 | 1 | false |
| `Volume17` | `decimal` | 1 | 1 | false |
| `Volume18` | `decimal` | 1 | 1 | false |
| `Volume19` | `decimal` | 1 | 1 | false |
| `Volume20` | `decimal` | 1 | 1 | false |
| `Volume21` | `decimal` | 1 | 1 | false |
| `Volume22` | `decimal` | 1 | 1 | false |
| `Volume23` | `decimal` | 1 | 1 | false |
| `Volume24` | `decimal` | 1 | 1 | false |
| `Volume25` | `decimal` | 1 | 1 | false |
| `Volume26` | `decimal` | 1 | 1 | false |
| `Volume27` | `decimal` | 1 | 1 | false |
| `Volume28` | `decimal` | 1 | 1 | false |
| `Volume29` | `decimal` | 1 | 1 | false |
| `Volume30` | `decimal` | 1 | 1 | false |
| `Volume31` | `decimal` | 1 | 1 | false |
| `Volume32` | `decimal` | 1 | 1 | false |
| `Volume33` | `decimal` | 1 | 1 | false |
| `Volume34` | `decimal` | 1 | 1 | false |
| `Volume35` | `decimal` | 1 | 1 | false |
| `Volume36` | `decimal` | 1 | 1 | false |
| `Volume37` | `decimal` | 1 | 1 | false |
| `Volume38` | `decimal` | 1 | 1 | false |
| `Volume39` | `decimal` | 1 | 1 | false |
| `Volume40` | `decimal` | 1 | 1 | false |
| `Volume41` | `decimal` | 1 | 1 | false |
| `Volume42` | `decimal` | 1 | 1 | false |
| `Volume43` | `decimal` | 1 | 1 | false |
| `Volume44` | `decimal` | 1 | 1 | false |
| `Volume45` | `decimal` | 1 | 1 | false |
| `Volume46` | `decimal` | 1 | 1 | false |
| `Volume47` | `decimal` | 1 | 1 | false |
| `Volume48` | `decimal` | 1 | 1 | false |
| `Volume49` | `decimal` | 1 | 1 | false |
| `Volume50` | `decimal` | 1 | 1 | false |
| `Volume51` | `decimal` | 1 | 1 | false |
| `Volume52` | `decimal` | 1 | 1 | false |
| `Volume53` | `decimal` | 1 | 1 | false |
| `Volume54` | `decimal` | 1 | 1 | false |
| `Volume55` | `decimal` | 1 | 1 | false |
| `Volume56` | `decimal` | 1 | 1 | false |
| `Volume57` | `decimal` | 1 | 1 | false |
| `Volume58` | `decimal` | 1 | 1 | false |
| `Volume59` | `decimal` | 1 | 1 | false |
| `Volume60` | `decimal` | 1 | 1 | false |
| `Volume61` | `decimal` | 1 | 1 | false |
| `Volume62` | `decimal` | 1 | 1 | false |
| `Volume63` | `decimal` | 1 | 1 | false |
| `Volume64` | `decimal` | 1 | 1 | false |
| `Volume65` | `decimal` | 1 | 1 | false |
| `Volume66` | `decimal` | 1 | 1 | false |
| `Volume67` | `decimal` | 1 | 1 | false |
| `Volume68` | `decimal` | 1 | 1 | false |
| `Volume69` | `decimal` | 1 | 1 | false |
| `Volume70` | `decimal` | 1 | 1 | false |
| `Volume71` | `decimal` | 1 | 1 | false |
| `Volume72` | `decimal` | 1 | 1 | false |
| `Volume73` | `decimal` | 1 | 1 | false |
| `Volume74` | `decimal` | 1 | 1 | false |
| `Volume75` | `decimal` | 1 | 1 | false |
| `Volume76` | `decimal` | 1 | 1 | false |
| `Volume77` | `decimal` | 1 | 1 | false |
| `Volume78` | `decimal` | 1 | 1 | false |
| `Volume79` | `decimal` | 1 | 1 | false |
| `Volume80` | `decimal` | 1 | 1 | false |
| `Volume81` | `decimal` | 1 | 1 | false |
| `Volume82` | `decimal` | 1 | 1 | false |
| `Volume83` | `decimal` | 1 | 1 | false |
| `Volume84` | `decimal` | 1 | 1 | false |
| `Volume85` | `decimal` | 1 | 1 | false |
| `Volume86` | `decimal` | 1 | 1 | false |
| `Volume87` | `decimal` | 1 | 1 | false |
| `Volume88` | `decimal` | 1 | 1 | false |
| `Volume89` | `decimal` | 1 | 1 | false |
| `Volume90` | `decimal` | 1 | 1 | false |
| `Volume91` | `decimal` | 1 | 1 | false |
| `Volume92` | `decimal` | 1 | 1 | false |
| `Volume93` | `decimal` | 1 | 1 | false |
| `Volume94` | `decimal` | 1 | 1 | false |
| `Volume95` | `decimal` | 1 | 1 | false |
| `Volume96` | `decimal` | 1 | 1 | false |
| `Volume97` | `decimal` | 1 | 1 | false |
| `Volume98` | `decimal` | 1 | 1 | false |
| `Volume99` | `decimal` | 1 | 1 | false |
| `Volume100` | `decimal` | 1 | 1 | false |
| `Volume101` | `decimal` | 1 | 1 | false |
| `Volume102` | `decimal` | 1 | 1 | false |
| `Volume103` | `decimal` | 1 | 1 | false |
| `Volume104` | `decimal` | 1 | 1 | false |
| `Volume105` | `decimal` | 1 | 1 | false |
| `Volume106` | `decimal` | 1 | 1 | false |
| `Volume107` | `decimal` | 1 | 1 | false |
| `Volume108` | `decimal` | 1 | 1 | false |
| `Volume109` | `decimal` | 1 | 1 | false |
| `Volume110` | `decimal` | 1 | 1 | false |
| `Volume111` | `decimal` | 1 | 1 | false |
| `Volume112` | `decimal` | 1 | 1 | false |
| `Volume113` | `decimal` | 1 | 1 | false |
| `Volume114` | `decimal` | 1 | 1 | false |
| `Volume115` | `decimal` | 1 | 1 | false |
| `Volume116` | `decimal` | 1 | 1 | false |
| `Volume117` | `decimal` | 1 | 1 | false |
| `Volume118` | `decimal` | 1 | 1 | false |
| `Volume119` | `decimal` | 1 | 1 | false |
| `Volume120` | `decimal` | 1 | 1 | false |
| `Volume121` | `decimal` | 1 | 1 | false |
| `Volume122` | `decimal` | 1 | 1 | false |
| `Volume123` | `decimal` | 1 | 1 | false |
| `Volume124` | `decimal` | 1 | 1 | false |
| `Volume125` | `decimal` | 1 | 1 | false |
| `Volume126` | `decimal` | 1 | 1 | false |
| `Volume127` | `decimal` | 1 | 1 | false |
| `Volume128` | `decimal` | 1 | 1 | false |
| `Volume129` | `decimal` | 1 | 1 | false |
| `Volume130` | `decimal` | 1 | 1 | false |
| `Volume131` | `decimal` | 1 | 1 | false |
| `Volume132` | `decimal` | 1 | 1 | false |
| `Volume133` | `decimal` | 1 | 1 | false |
| `Volume134` | `decimal` | 1 | 1 | false |
| `Volume135` | `decimal` | 1 | 1 | false |
| `Volume136` | `decimal` | 1 | 1 | false |
| `Volume137` | `decimal` | 1 | 1 | false |
| `Volume138` | `decimal` | 1 | 1 | false |
| `Volume139` | `decimal` | 1 | 1 | false |
| `Volume140` | `decimal` | 1 | 1 | false |
| `Volume141` | `decimal` | 1 | 1 | false |
| `Volume142` | `decimal` | 1 | 1 | false |
| `Volume143` | `decimal` | 1 | 1 | false |
| `Volume144` | `decimal` | 1 | 1 | false |
| `Volume145` | `decimal` | 1 | 1 | false |
| `Volume146` | `decimal` | 1 | 1 | false |
| `Volume147` | `decimal` | 1 | 1 | false |
| `Volume148` | `decimal` | 1 | 1 | false |
| `Volume149` | `decimal` | 1 | 1 | false |
| `Volume150` | `decimal` | 1 | 1 | false |
| `Volume151` | `decimal` | 1 | 1 | false |
| `Volume152` | `decimal` | 1 | 1 | false |
| `Volume153` | `decimal` | 1 | 1 | false |
| `Volume154` | `decimal` | 1 | 1 | false |
| `Volume155` | `decimal` | 1 | 1 | false |
| `Volume156` | `decimal` | 1 | 1 | false |
| `Volume157` | `decimal` | 1 | 1 | false |
| `Volume158` | `decimal` | 1 | 1 | false |
| `Volume159` | `decimal` | 1 | 1 | false |
| `Volume160` | `decimal` | 1 | 1 | false |
| `Volume161` | `decimal` | 1 | 1 | false |
| `Volume162` | `decimal` | 1 | 1 | false |
| `Volume163` | `decimal` | 1 | 1 | false |
| `Volume164` | `decimal` | 1 | 1 | false |
| `Volume165` | `decimal` | 1 | 1 | false |
| `Volume166` | `decimal` | 1 | 1 | false |
| `Volume167` | `decimal` | 1 | 1 | false |
| `Volume168` | `decimal` | 1 | 1 | false |
| `Volume169` | `decimal` | 1 | 1 | false |
| `Volume170` | `decimal` | 1 | 1 | false |
| `Volume171` | `decimal` | 1 | 1 | false |
| `Volume172` | `decimal` | 1 | 1 | false |
| `Volume173` | `decimal` | 1 | 1 | false |
| `Volume174` | `decimal` | 1 | 1 | false |
| `Volume175` | `decimal` | 1 | 1 | false |
| `Volume176` | `decimal` | 1 | 1 | false |
| `Volume177` | `decimal` | 1 | 1 | false |
| `Volume178` | `decimal` | 1 | 1 | false |
| `Volume179` | `decimal` | 1 | 1 | false |
| `Volume180` | `decimal` | 1 | 1 | false |
| `Volume181` | `decimal` | 1 | 1 | false |
| `Volume182` | `decimal` | 1 | 1 | false |
| `Volume183` | `decimal` | 1 | 1 | false |
| `Volume184` | `decimal` | 1 | 1 | false |
| `Volume185` | `decimal` | 1 | 1 | false |
| `Volume186` | `decimal` | 1 | 1 | false |
| `Volume187` | `decimal` | 1 | 1 | false |
| `Volume188` | `decimal` | 1 | 1 | false |
| `Volume189` | `decimal` | 1 | 1 | false |
| `Volume190` | `decimal` | 1 | 1 | false |
| `Volume191` | `decimal` | 1 | 1 | false |
| `Volume192` | `decimal` | 1 | 1 | false |
| `Volume193` | `decimal` | 1 | 1 | false |
| `Volume194` | `decimal` | 1 | 1 | false |
| `Volume195` | `decimal` | 1 | 1 | false |
| `Volume196` | `decimal` | 1 | 1 | false |
| `Volume197` | `decimal` | 1 | 1 | false |
| `Volume198` | `decimal` | 1 | 1 | false |
| `Volume199` | `decimal` | 1 | 1 | false |
| `Volume200` | `decimal` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### OptInEmailRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Email` | `string` | 0 | 1 | false |

### OptInEmailResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `RecordsAffected` | `int` | 1 | 1 | false |

### OptInPushNotificationRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### OptInPushNotificationResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `RecordsAffected` | `int` | 1 | 1 | false |

### OptInSmsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | true |
| `PhoneNumber` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### OptInSmsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `RecordsAffected` | `int` | 1 | 1 | false |

### OptOutEmailRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Email` | `string` | 0 | 1 | false |

### OptOutEmailResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `RecordsAffected` | `int` | 1 | 1 | false |

### OptOutPushNotificationRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### OptOutPushNotificationResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `RecordsAffected` | `int` | 1 | 1 | false |

### OptOutSmsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | true |
| `PhoneNumber` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### OptOutSmsResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `RecordsAffected` | `int` | 1 | 1 | false |

### OrderBatchDetailRequest

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderID` | `int` | 1 | 1 | false |
| `TrackingNumber1` | `string` | 1 | 1 | true |
| `TrackingNumber2` | `string` | 1 | 1 | true |
| `TrackingNumber3` | `string` | 1 | 1 | true |
| `TrackingNumber4` | `string` | 1 | 1 | true |
| `TrackingNumber5` | `string` | 1 | 1 | true |
| `ShippedDate` | `dateTime` | 1 | 1 | true |
| `OrderKey` | `string` | 0 | 1 | false |

### OrderDetailIDs

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderDetailID` | `guid` | 1 | 1 | true |
| `ParentOrderDetailID` | `guid` | 1 | 1 | true |

### OrderDetailRequest

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ItemCode` | `string` | 0 | 1 | false |
| `OrderDetailID` | `guid` | 1 | 1 | true |
| `ParentOrderDetailID` | `guid` | 1 | 1 | true |
| `Quantity` | `decimal` | 1 | 1 | false |
| `ParentItemCode` | `string` | 1 | 1 | true |
| `PriceEachOverride` | `decimal` | 1 | 1 | true |
| `TaxableEachOverride` | `decimal` | 1 | 1 | true |
| `ShippingPriceEachOverride` | `decimal` | 1 | 1 | true |
| `BusinessVolumeEachOverride` | `decimal` | 1 | 1 | true |
| `CommissionableVolumeEachOverride` | `decimal` | 1 | 1 | true |
| `Other1EachOverride` | `decimal` | 1 | 1 | true |
| `Other2EachOverride` | `decimal` | 1 | 1 | true |
| `Other3EachOverride` | `decimal` | 1 | 1 | true |
| `Other4EachOverride` | `decimal` | 1 | 1 | true |
| `Other5EachOverride` | `decimal` | 1 | 1 | true |
| `Other6EachOverride` | `decimal` | 1 | 1 | true |
| `Other7EachOverride` | `decimal` | 1 | 1 | true |
| `Other8EachOverride` | `decimal` | 1 | 1 | true |
| `Other9EachOverride` | `decimal` | 1 | 1 | true |
| `Other10EachOverride` | `decimal` | 1 | 1 | true |
| `DescriptionOverride` | `string` | 1 | 1 | true |
| `Reference1` | `string` | 1 | 1 | true |
| `AdvancedAutoOptions` | `AdvancedAutoOptionsRequest` | 0 | 1 | false |
| `OrderLine` | `int` | 1 | 1 | true |

### OrderDetailResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderDetailID` | `guid` | 1 | 1 | true |
| `ParentOrderDetailID` | `guid` | 1 | 1 | true |
| `ItemCode` | `string` | 0 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `Quantity` | `decimal` | 1 | 1 | false |
| `PriceEach` | `decimal` | 1 | 1 | false |
| `PriceTotal` | `decimal` | 1 | 1 | false |
| `Tax` | `decimal` | 1 | 1 | false |
| `WeightEach` | `decimal` | 1 | 1 | false |
| `Weight` | `decimal` | 1 | 1 | false |
| `BusinessVolumeEach` | `decimal` | 1 | 1 | false |
| `BusinesVolume` | `decimal` | 1 | 1 | false |
| `CommissionableVolumeEach` | `decimal` | 1 | 1 | false |
| `CommissionableVolume` | `decimal` | 1 | 1 | false |
| `Other1Each` | `decimal` | 1 | 1 | false |
| `Other1` | `decimal` | 1 | 1 | false |
| `Other2Each` | `decimal` | 1 | 1 | false |
| `Other2` | `decimal` | 1 | 1 | false |
| `Other3Each` | `decimal` | 1 | 1 | false |
| `Other3` | `decimal` | 1 | 1 | false |
| `Other4Each` | `decimal` | 1 | 1 | false |
| `Other4` | `decimal` | 1 | 1 | false |
| `Other5Each` | `decimal` | 1 | 1 | false |
| `Other5` | `decimal` | 1 | 1 | false |
| `Other6Each` | `decimal` | 1 | 1 | false |
| `Other6` | `decimal` | 1 | 1 | false |
| `Other7Each` | `decimal` | 1 | 1 | false |
| `Other7` | `decimal` | 1 | 1 | false |
| `Other8Each` | `decimal` | 1 | 1 | false |
| `Other8` | `decimal` | 1 | 1 | false |
| `Other9Each` | `decimal` | 1 | 1 | false |
| `Other9` | `decimal` | 1 | 1 | false |
| `Other10Each` | `decimal` | 1 | 1 | false |
| `Other10` | `decimal` | 1 | 1 | false |
| `ParentItemCode` | `string` | 0 | 1 | false |
| `Taxable` | `decimal` | 1 | 1 | false |
| `FedTax` | `decimal` | 1 | 1 | false |
| `StateTax` | `decimal` | 1 | 1 | false |
| `CityTax` | `decimal` | 1 | 1 | false |
| `CityLocalTax` | `decimal` | 1 | 1 | false |
| `CountyTax` | `decimal` | 1 | 1 | false |
| `CountyLocalTax` | `decimal` | 1 | 1 | false |
| `ManualTax` | `decimal` | 1 | 1 | false |
| `IsStateTaxOverride` | `boolean` | 1 | 1 | false |
| `OrderLine` | `int` | 1 | 1 | false |
| `Reference1` | `string` | 0 | 1 | false |
| `ShippingPriceEach` | `decimal` | 1 | 1 | false |
| `HandlingFee` | `decimal` | 1 | 1 | false |
| `BusinessVolume` | `decimal` | 1 | 1 | false |

### OrderImportDetail

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ParentItemCode` | `string` | 0 | 1 | false |
| `ItemCode` | `string` | 0 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `Qty` | `decimal` | 1 | 1 | false |
| `WeightEach` | `decimal` | 1 | 1 | false |
| `CountyLocalTax` | `decimal` | 1 | 1 | false |
| `CountyTax` | `decimal` | 1 | 1 | false |
| `CityTax` | `decimal` | 1 | 1 | false |
| `StateTax` | `decimal` | 1 | 1 | false |
| `FedTax` | `decimal` | 1 | 1 | false |
| `TaxablePriceEach` | `decimal` | 1 | 1 | false |
| `CVEach` | `decimal` | 1 | 1 | false |
| `BVEach` | `decimal` | 1 | 1 | false |
| `PriceEach` | `decimal` | 1 | 1 | false |
| `Other10Each` | `decimal` | 1 | 1 | false |
| `Other9Each` | `decimal` | 1 | 1 | false |
| `Other8Each` | `decimal` | 1 | 1 | false |
| `Other7Each` | `decimal` | 1 | 1 | false |
| `Other6Each` | `decimal` | 1 | 1 | false |
| `Other5Each` | `decimal` | 1 | 1 | false |
| `Other4Each` | `decimal` | 1 | 1 | false |
| `Other3Each` | `decimal` | 1 | 1 | false |
| `Other2Each` | `decimal` | 1 | 1 | false |
| `Other1Each` | `decimal` | 1 | 1 | false |
| `Reference1` | `string` | 0 | 1 | false |
| `CityLocalTax` | `decimal` | 1 | 1 | false |
| `OrderLine` | `int` | 1 | 1 | true |
| `OrderDetailID` | `guid` | 1 | 1 | true |
| `ParentOrderDetailID` | `guid` | 1 | 1 | true |

### OrderResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderID` | `int` | 1 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | false |
| `OrderStatus` | `OrderStatusType` | 1 | 1 | false |
| `OrderDate` | `dateTime` | 1 | 1 | false |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `WarehouseID` | `int` | 1 | 1 | false |
| `ShipMethodID` | `int` | 1 | 1 | false |
| `PriceType` | `int` | 1 | 1 | false |
| `FirstName` | `string` | 0 | 1 | false |
| `LastName` | `string` | 0 | 1 | false |
| `Company` | `string` | 0 | 1 | false |
| `Address1` | `string` | 0 | 1 | false |
| `Address2` | `string` | 0 | 1 | false |
| `Address3` | `string` | 0 | 1 | false |
| `City` | `string` | 0 | 1 | false |
| `State` | `string` | 0 | 1 | false |
| `Zip` | `string` | 0 | 1 | false |
| `Country` | `string` | 0 | 1 | false |
| `County` | `string` | 0 | 1 | false |
| `Email` | `string` | 0 | 1 | false |
| `Phone` | `string` | 0 | 1 | false |
| `Notes` | `string` | 0 | 1 | false |
| `Total` | `decimal` | 1 | 1 | false |
| `SubTotal` | `decimal` | 1 | 1 | false |
| `TaxTotal` | `decimal` | 1 | 1 | false |
| `ShippingTotal` | `decimal` | 1 | 1 | false |
| `DiscountTotal` | `decimal` | 1 | 1 | false |
| `DiscountPercent` | `decimal` | 1 | 1 | false |
| `WeightTotal` | `decimal` | 1 | 1 | false |
| `BusinessVolumeTotal` | `decimal` | 1 | 1 | false |
| `CommissionableVolumeTotal` | `decimal` | 1 | 1 | false |
| `TrackingNumber1` | `string` | 0 | 1 | false |
| `TrackingNumber2` | `string` | 0 | 1 | false |
| `TrackingNumber3` | `string` | 0 | 1 | false |
| `TrackingNumber4` | `string` | 0 | 1 | false |
| `TrackingNumber5` | `string` | 0 | 1 | false |
| `Other1Total` | `decimal` | 1 | 1 | false |
| `Other2Total` | `decimal` | 1 | 1 | false |
| `Other3Total` | `decimal` | 1 | 1 | false |
| `Other4Total` | `decimal` | 1 | 1 | false |
| `Other5Total` | `decimal` | 1 | 1 | false |
| `Other6Total` | `decimal` | 1 | 1 | false |
| `Other7Total` | `decimal` | 1 | 1 | false |
| `Other8Total` | `decimal` | 1 | 1 | false |
| `Other9Total` | `decimal` | 1 | 1 | false |
| `Other10Total` | `decimal` | 1 | 1 | false |
| `ShippingTax` | `decimal` | 1 | 1 | false |
| `OrderTax` | `decimal` | 1 | 1 | false |
| `FedTaxTotal` | `decimal` | 1 | 1 | false |
| `StateTaxTotal` | `decimal` | 1 | 1 | false |
| `FedShippingTax` | `decimal` | 1 | 1 | false |
| `StateShippingTax` | `decimal` | 1 | 1 | false |
| `CityShippingTax` | `decimal` | 1 | 1 | false |
| `CityLocalShippingTax` | `decimal` | 1 | 1 | false |
| `CountyShippingTax` | `decimal` | 1 | 1 | false |
| `CountyLocalShippingTax` | `decimal` | 1 | 1 | false |
| `Other11` | `string` | 0 | 1 | false |
| `Other12` | `string` | 0 | 1 | false |
| `Other13` | `string` | 0 | 1 | false |
| `Other14` | `string` | 0 | 1 | false |
| `Other15` | `string` | 0 | 1 | false |
| `Other16` | `string` | 0 | 1 | false |
| `Other17` | `string` | 0 | 1 | false |
| `Other18` | `string` | 0 | 1 | false |
| `Other19` | `string` | 0 | 1 | false |
| `Other20` | `string` | 0 | 1 | false |
| `ModifiedDate` | `dateTime` | 1 | 1 | false |
| `OrderType` | `OrderType` | 1 | 1 | false |
| `ShippedDate` | `dateTime` | 1 | 1 | true |
| `CreatedDate` | `dateTime` | 1 | 1 | false |
| `CreatedBy` | `string` | 0 | 1 | false |
| `ModifiedBy` | `string` | 0 | 1 | false |
| `TaxFedRate` | `decimal` | 1 | 1 | false |
| `TaxStateRate` | `decimal` | 1 | 1 | false |
| `TaxCityRate` | `decimal` | 1 | 1 | false |
| `TaxCityLocalRate` | `decimal` | 1 | 1 | false |
| `TaxCountyRate` | `decimal` | 1 | 1 | false |
| `TaxCountyLocalRate` | `decimal` | 1 | 1 | false |
| `TaxManualRate` | `decimal` | 1 | 1 | false |
| `TaxCity` | `string` | 0 | 1 | false |
| `TaxCounty` | `string` | 0 | 1 | false |
| `TaxState` | `string` | 0 | 1 | false |
| `TaxZip` | `string` | 0 | 1 | false |
| `TaxCountry` | `string` | 0 | 1 | false |
| `TaxIsExempt` | `boolean` | 1 | 1 | false |
| `TaxIsOverRide` | `boolean` | 1 | 1 | false |
| `Details` | `ArrayOfOrderDetailResponse` | 0 | 1 | false |
| `Payments` | `ArrayOfPaymentResponse` | 0 | 1 | false |
| `ExpectedPayments` | `ArrayOfExpectedPaymentResponse` | 0 | 1 | false |
| `Customer` | `CustomerResponse` | 0 | 1 | false |
| `MiddleName` | `string` | 0 | 1 | false |
| `NameSuffix` | `string` | 0 | 1 | false |
| `AutoOrderID` | `int` | 1 | 1 | true |
| `PartyID` | `int` | 1 | 1 | true |
| `Reference1` | `string` | 0 | 1 | false |
| `IsRMA` | `boolean` | 1 | 1 | false |
| `BackOrderFromID` | `int` | 1 | 1 | true |
| `TransferToID` | `int` | 1 | 1 | true |
| `SuppressPackSlipPrice` | `boolean` | 1 | 1 | false |
| `ReturnOrderID` | `int` | 1 | 1 | true |
| `OrderKey` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `ReplacementOrderID` | `int` | 1 | 1 | true |
| `OrderSubStatusTy` | `int` | 1 | 1 | true |
| `BatchID` | `int` | 1 | 1 | true |
| `OrderTyID` | `int` | 1 | 1 | false |
| `OrderTyDescription` | `string` | 0 | 1 | false |
| `ReferralID` | `int` | 1 | 1 | true |

### OrderTotalByCurrency

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CurrencyCode` | `string` | 0 | 1 | false |
| `Amount` | `decimal` | 1 | 1 | false |
| `Count` | `int` | 1 | 1 | false |

### ParameterRequest

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ParameterName` | `string` | 0 | 1 | false |
| `Value` | `` | 0 | 1 | false |

### PartyAddress

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Address1` | `string` | 0 | 1 | false |
| `Address2` | `string` | 0 | 1 | false |
| `City` | `string` | 0 | 1 | false |
| `State` | `string` | 0 | 1 | false |
| `Zip` | `string` | 0 | 1 | false |
| `Country` | `string` | 0 | 1 | false |

### PartyResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PartyID` | `int` | 1 | 1 | false |
| `PartyType` | `int` | 1 | 1 | false |
| `PartyStatusType` | `int` | 1 | 1 | false |
| `HostID` | `int` | 1 | 1 | false |
| `DistributorID` | `int` | 1 | 1 | false |
| `StartDate` | `dateTime` | 1 | 1 | false |
| `CloseDate` | `dateTime` | 1 | 1 | true |
| `Description` | `string` | 0 | 1 | false |
| `EventStart` | `dateTime` | 1 | 1 | true |
| `EventEnd` | `dateTime` | 1 | 1 | true |
| `LanguageID` | `int` | 1 | 1 | true |
| `Information` | `string` | 0 | 1 | false |
| `Address` | `PartyAddress` | 0 | 1 | false |
| `BookingPartyID` | `int` | 1 | 1 | true |
| `Field1` | `string` | 0 | 1 | false |
| `Field2` | `string` | 0 | 1 | false |
| `Field3` | `string` | 0 | 1 | false |
| `Field4` | `string` | 0 | 1 | false |
| `Field5` | `string` | 0 | 1 | false |
| `PartyShoppingUrl` | `string` | 0 | 1 | false |
| `PartyExternalID` | `guid` | 1 | 1 | false |
| `TimeZoneID` | `string` | 0 | 1 | false |
| `VirtualMeetingLink` | `string` | 0 | 1 | false |

### PaymentResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PaymentID` | `int` | 1 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | false |
| `PaymentType` | `PaymentType` | 1 | 1 | false |
| `PaymentDate` | `dateTime` | 1 | 1 | false |
| `Amount` | `decimal` | 1 | 1 | false |
| `OrderID` | `int` | 1 | 1 | true |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `BillingName` | `string` | 0 | 1 | false |
| `BillingAddress1` | `string` | 0 | 1 | false |
| `BillingAddress2` | `string` | 0 | 1 | false |
| `BillingCity` | `string` | 0 | 1 | false |
| `BillingState` | `string` | 0 | 1 | false |
| `BillingZip` | `string` | 0 | 1 | false |
| `BillingCountry` | `string` | 0 | 1 | false |
| `BankName` | `string` | 0 | 1 | false |
| `Memo` | `string` | 0 | 1 | false |
| `CreditCardNumberDisplay` | `string` | 0 | 1 | false |
| `AuthorizationCode` | `string` | 0 | 1 | false |
| `CreditCardType` | `int` | 1 | 1 | false |
| `CreditCardTypeDescription` | `string` | 0 | 1 | false |
| `OrderKey` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `WalletTy` | `int` | 1 | 1 | false |
| `PaymentTypeId` | `int` | 1 | 1 | false |

### PaymentsResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `_PaymentID` | `int` | 1 | 1 | false |
| `_OrderID` | `int` | 1 | 1 | false |

### PlaceBinaryNodeRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `ToParentID` | `int` | 1 | 1 | false |
| `PlacementType` | `BinaryPlacementType` | 1 | 1 | false |
| `Reason` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `ToParentKey` | `string` | 0 | 1 | false |

### PlaceBinaryNodeResponse
Extends `ApiResponse`.

_No fields._

### PlaceEnrollerNodeRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `ToEnrollerID` | `int` | 1 | 1 | false |
| `Reason` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `ToEnrollerKey` | `string` | 0 | 1 | false |

### PlaceEnrollerNodeResponse
Extends `ApiResponse`.

_No fields._

### PlaceMatrixNodeRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `ToParentCustomerID` | `int` | 1 | 1 | false |
| `ToParentMatrixID` | `int` | 1 | 1 | true |
| `Reason` | `string` | 0 | 1 | false |
| `Placement` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `ToParentCustomerKey` | `string` | 0 | 1 | false |
| `ToParentMatrixKey` | `string` | 0 | 1 | false |

### PlaceMatrixNodeResponse
Extends `ApiResponse`.

_No fields._

### PlaceStackNodeRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `ToParentID` | `int` | 1 | 1 | false |
| `ToParentKey` | `string` | 0 | 1 | false |
| `Reason` | `string` | 0 | 1 | false |

### PlaceStackNodeResponse
Extends `ApiResponse`.

_No fields._

### PlaceUniLevelNodeRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `ToSponsorID` | `int` | 1 | 1 | false |
| `Reason` | `string` | 0 | 1 | false |
| `OptionalPlacement` | `int` | 1 | 1 | false |
| `OptionalFindAvailable` | `boolean` | 1 | 1 | false |
| `OptionalUnilevelBuildTypeID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `ToSponsorKey` | `string` | 0 | 1 | false |

### PlaceUniLevelNodeResponse
Extends `ApiResponse`.

_No fields._

### PointAccount

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PointAccountID` | `int` | 1 | 1 | false |
| `Increment` | `decimal` | 1 | 1 | false |

### PropertyDataRequest

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PropertyName` | `string` | 0 | 1 | false |
| `IsKey` | `boolean` | 1 | 1 | false |
| `IsNew` | `boolean` | 1 | 1 | false |
| `IsAutoNumber` | `boolean` | 1 | 1 | false |
| `AllowDbNull` | `boolean` | 1 | 1 | false |
| `Type` | `PropertyType` | 1 | 1 | false |
| `DefaultValue` | `string` | 0 | 1 | false |
| `Size` | `int` | 1 | 1 | true |
| `MaskTypeId` | `int` | 1 | 1 | true |

### PropertyDataResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PropertyName` | `string` | 0 | 1 | false |
| `IsKey` | `boolean` | 1 | 1 | false |
| `IsNew` | `boolean` | 1 | 1 | false |
| `IsAutoNumber` | `boolean` | 1 | 1 | false |
| `AllowDbNull` | `boolean` | 1 | 1 | false |
| `Type` | `PropertyType` | 1 | 1 | false |
| `DefaultValue` | `string` | 0 | 1 | false |
| `Size` | `int` | 1 | 1 | true |
| `MaskType` | `MaskTypeDataResponse` | 0 | 1 | false |

### PropertyDataUpdateRequest

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PropertyName` | `string` | 0 | 1 | false |
| `AllowDbNull` | `boolean` | 1 | 1 | true |
| `Size` | `int` | 1 | 1 | true |
| `MaskTypeId` | `int` | 1 | 1 | true |

### QualificationResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `QualificationDescription` | `string` | 0 | 1 | false |
| `Required` | `string` | 0 | 1 | false |
| `Actual` | `string` | 0 | 1 | false |
| `Qualifies` | `boolean` | 1 | 1 | false |
| `QualifiesOverride` | `boolean` | 1 | 1 | true |
| `SupportingTable` | `` | 0 | 1 | false |
| `Completed` | `decimal` | 1 | 1 | false |
| `Weight` | `decimal` | 1 | 1 | false |
| `Score` | `decimal` | 1 | 1 | false |

### QueueBillPayoutRequest
Extends `BaseProcessPayoutRequest`.

_No fields._

### QueueBillPayoutResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PaymentQueueRequestId` | `guid` | 1 | 1 | false |

### ReIndexHistoryItem

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `TableName` | `string` | 0 | 1 | false |
| `IndexName` | `string` | 0 | 1 | false |
| `Fragmentation` | `double` | 1 | 1 | false |
| `PageCount` | `long` | 1 | 1 | false |
| `StartDate` | `dateTime` | 1 | 1 | false |
| `EndDate` | `dateTime` | 1 | 1 | true |
| `ErrorMessage` | `string` | 0 | 1 | false |

### ReIndexSettings

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ReIndexStartTime` | `dateTime` | 1 | 1 | true |
| `ReIndexMaxDuration` | `int` | 1 | 1 | true |
| `LastReIndexed` | `dateTime` | 1 | 1 | true |

### RefreshSandboxRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SandboxID` | `int` | 1 | 1 | false |

### RefreshSandboxResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Sandbox` | `Sandbox` | 0 | 1 | false |

### RefundPriorCreditCardChargeRequest
Extends `BaseCreatePaymentCreditCardRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ReturnPaymentID` | `int` | 1 | 1 | false |
| `OrderID` | `int` | 1 | 1 | false |
| `RefundOriginalOrder` | `boolean` | 1 | 1 | false |
| `MaxAmount` | `decimal` | 1 | 1 | true |
| `OrderKey` | `string` | 0 | 1 | false |

### RefundPriorCreditCardChargeResponse
Extends `CreatePaymentCreditCardResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Amount` | `decimal` | 1 | 1 | false |
| `AuthorizationCode` | `string` | 0 | 1 | false |

### RefundPriorDebitChargeRequest
Extends `BaseDebitBankAccountRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ReturnPaymentID` | `int` | 1 | 1 | false |
| `OrderID` | `int` | 1 | 1 | false |
| `RefundOriginalOrder` | `boolean` | 1 | 1 | false |
| `MaxAmount` | `decimal` | 1 | 1 | true |
| `OrderKey` | `string` | 0 | 1 | false |

### RefundPriorDebitChargeResponse
Extends `DebitBankAccountResponse`.

_No fields._

### RefundPriorWalletChargeRequest
Extends `BaseCreatePaymentRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ReturnPaymentID` | `int` | 1 | 1 | false |
| `OrderID` | `int` | 1 | 1 | false |
| `RefundOriginalOrder` | `boolean` | 1 | 1 | false |
| `MaxAmount` | `decimal` | 1 | 1 | true |
| `OrderKey` | `string` | 0 | 1 | false |

### RefundPriorWalletChargeResponse
Extends `CreatePaymentResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Amount` | `decimal` | 1 | 1 | false |
| `AuthorizationCode` | `string` | 0 | 1 | false |

### RegionResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `RegionCode` | `string` | 0 | 1 | false |
| `RegionName` | `string` | 0 | 1 | false |

### RemoveAdminWhitelistRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `IPRangeID` | `int` | 1 | 1 | false |

### RemoveAdminWhitelistResponse
Extends `ApiResponse`.

_No fields._

### RemoveApiWhitelistRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `IPRangeID` | `int` | 1 | 1 | false |

### RemoveApiWhitelistResponse
Extends `ApiResponse`.

_No fields._

### RemovePartyGuestsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PartyID` | `int` | 1 | 1 | false |
| `GuestIDs` | `ArrayOfInt` | 0 | 1 | false |

### RemovePartyGuestsResponse
Extends `ApiResponse`.

_No fields._

### ReportParameterRequest

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ParameterName` | `string` | 0 | 1 | false |
| `Value` | `string` | 0 | 1 | false |

### ResourceBanner
Extends `ResourceItem`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Title` | `string` | 0 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `BannerImageBase64` | `string` | 0 | 1 | false |
| `BannerHoverText` | `string` | 0 | 1 | false |
| `BannerUrl` | `string` | 0 | 1 | false |
| `BannerClickEvent` | `BannerClickEvent` | 1 | 1 | false |
| `BannerType` | `BannerType` | 1 | 1 | false |
| `AssociatedDataSets` | `ArrayOfString` | 0 | 1 | false |

### ResourceCarousel
Extends `ResourceItem`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CarouselSlides` | `ArrayOfString` | 0 | 1 | false |
| `CarouselType` | `CarouselType` | 1 | 1 | false |

### ResourceCheckBox
Extends `ResourceItem`.

_No fields._

### ResourceDataSet
Extends `ResourceItem`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DataSetType` | `string` | 0 | 1 | false |
| `DataSetValues` | `ArrayOfString` | 0 | 1 | false |

### ResourceDate
Extends `ResourceItem`.

_No fields._

### ResourceDecimal
Extends `ResourceItem`.

_No fields._

### ResourceDropDown
Extends `ResourceItem`.

_No fields._

### ResourceGroup

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `ResourceGroupID` | `int` | 1 | 1 | false |
| `Description` | `string` | 0 | 1 | false |

### ResourceImage
Extends `ResourceItem`.

_No fields._

### ResourceItem

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceName` | `string` | 0 | 1 | false |
| `InvariantValue` | `string` | 0 | 1 | false |
| `Comment` | `string` | 0 | 1 | false |
| `Enabled` | `boolean` | 1 | 1 | false |
| `EnabledStartDate` | `dateTime` | 1 | 1 | true |
| `EnabledEndDate` | `dateTime` | 1 | 1 | true |
| `ModifiedDate` | `dateTime` | 1 | 1 | false |
| `ResourceTypeID` | `ResourceType` | 1 | 1 | false |
| `ResourceSetID` | `int` | 1 | 1 | false |
| `CultureCode` | `string` | 0 | 1 | false |
| `ResourceGroupID` | `int` | 1 | 1 | true |
| `DropDownValues` | `string` | 0 | 1 | false |

### ResourceNumber
Extends `ResourceItem`.

_No fields._

### ResourceSet

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `ClassName` | `string` | 0 | 1 | false |
| `Namespace` | `string` | 0 | 1 | false |
| `SubscriptionKey` | `string` | 0 | 1 | false |
| `IsDeleted` | `boolean` | 1 | 1 | false |
| `ModifiedDate` | `DateTimeOffset` | 1 | 1 | false |

### ResourceSetCheckInRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SubscriptionKey` | `string` | 0 | 1 | false |
| `EnvironmentCode` | `string` | 0 | 1 | false |
| `InstalledVersion` | `string` | 0 | 1 | false |
| `InstalledReleaseDate` | `dateTime` | 1 | 1 | true |
| `MachineName` | `string` | 0 | 1 | false |
| `HostAssemblyName` | `string` | 0 | 1 | false |
| `ComponentVersion` | `string` | 0 | 1 | false |

### ResourceSetCheckInResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SubscriptionKey` | `string` | 0 | 1 | false |
| `EnvironmentCode` | `string` | 0 | 1 | false |
| `Version` | `string` | 0 | 1 | false |
| `ReleaseDate` | `dateTime` | 1 | 1 | false |
| `ClassName` | `string` | 0 | 1 | false |
| `Namespace` | `string` | 0 | 1 | false |

### ResourceSetCulture

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `CultureCode` | `string` | 0 | 1 | false |
| `Description` | `string` | 0 | 1 | false |

### ResourceSetEnvironment

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `EnvironmentCode` | `string` | 0 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `Version` | `string` | 0 | 1 | false |
| `ScheduledVersion` | `string` | 0 | 1 | false |
| `ScheduledVersionDate` | `dateTime` | 1 | 1 | true |
| `ModifiedDate` | `dateTime` | 1 | 1 | true |
| `ModifiedBy` | `string` | 0 | 1 | false |

### ResourceSetRelease

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `Version` | `string` | 0 | 1 | false |
| `ReleaseDate` | `dateTime` | 1 | 1 | false |
| `IsArchived` | `boolean` | 1 | 1 | false |
| `HasArchiveStarted` | `boolean` | 1 | 1 | false |

### ResourceSetSubscriptionCheckIn

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SubscriptionKey` | `string` | 0 | 1 | false |
| `EnvironmentCode` | `string` | 0 | 1 | false |
| `InstalledVersion` | `string` | 0 | 1 | false |
| `InstalledReleaseDate` | `dateTime` | 1 | 1 | true |
| `MachineName` | `string` | 0 | 1 | false |
| `HostAssemblyName` | `string` | 0 | 1 | false |
| `ComponentVersion` | `string` | 0 | 1 | false |

### ResourceString
Extends `ResourceItem`.

_No fields._

### ResourceSubscription

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SubscriptionKey` | `string` | 0 | 1 | false |
| `EnvironmentCode` | `string` | 0 | 1 | false |
| `Version` | `string` | 0 | 1 | false |
| `ReleaseDate` | `dateTime` | 1 | 1 | false |
| `ClassName` | `string` | 0 | 1 | false |
| `Namespace` | `string` | 0 | 1 | false |

### ResourceSubscriptionUpdate

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Subscription` | `ResourceSubscription` | 0 | 1 | false |
| `CultureCodeItems` | `ArrayOfCultureCodeItem` | 0 | 1 | false |

### ResourceWidget
Extends `ResourceItem`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Html` | `string` | 0 | 1 | false |
| `Javascript` | `string` | 0 | 1 | false |
| `Css` | `string` | 0 | 1 | false |

### RetireResourceSetRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |

### RetireResourceSetResponse
Extends `ApiResponse`.

_No fields._

### RevertToRecentReleaseRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |

### RevertToRecentReleaseResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `ReleaseDate` | `dateTime` | 1 | 1 | false |
| `Version` | `string` | 0 | 1 | false |

### Sandbox

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CompanyID` | `int` | 1 | 1 | false |
| `SandboxID` | `int` | 1 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `Type` | `SandboxType` | 1 | 1 | false |
| `Status` | `string` | 0 | 1 | false |
| `StartDate` | `dateTime` | 1 | 1 | true |
| `PercentComplete` | `decimal` | 1 | 1 | true |
| `Hours` | `decimal` | 1 | 1 | false |
| `AllowVolumePush` | `boolean` | 1 | 1 | false |
| `AllowBiSync` | `boolean` | 1 | 1 | false |
| `SyncFilterDays` | `int` | 1 | 1 | true |
| `UseRealTimeBackup` | `boolean` | 1 | 1 | false |

### SchemaDataResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Name` | `string` | 0 | 1 | false |
| `Entities` | `ArrayOfEntityDataResponse` | 0 | 1 | false |

### SendAuthorizationMFACodeRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ToNumber` | `string` | 0 | 1 | false |
| `Message` | `string` | 0 | 1 | false |
| `Code` | `string` | 0 | 1 | false |

### SendAuthorizationMFACodeResponse
Extends `ApiResponse`.

_No fields._

### SendEmailRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | true |
| `MailFrom` | `string` | 0 | 1 | false |
| `MailTo` | `string` | 0 | 1 | false |
| `Subject` | `string` | 0 | 1 | false |
| `Body` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### SendEmailResponse
Extends `ApiResponse`.

_No fields._

### SendSmsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `Message` | `string` | 0 | 1 | false |
| `Phone` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### SendSmsResponse
Extends `ApiResponse`.

_No fields._

### SetAccountCheckingRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `BankAccountNumber` | `string` | 0 | 1 | false |
| `BankRoutingNumber` | `string` | 0 | 1 | false |
| `BankName` | `string` | 0 | 1 | false |
| `BankAccountType` | `BankAccountType` | 1 | 1 | false |
| `NameOnAccount` | `string` | 0 | 1 | false |
| `UseMainAddress` | `boolean` | 1 | 1 | false |
| `BillingAddress` | `string` | 0 | 1 | false |
| `BillingCity` | `string` | 0 | 1 | false |
| `BillingState` | `string` | 0 | 1 | false |
| `BillingZip` | `string` | 0 | 1 | false |
| `BillingCountry` | `string` | 0 | 1 | false |
| `DriversLicenseNumber` | `string` | 0 | 1 | false |
| `Iban` | `string` | 0 | 1 | false |
| `SwiftCode` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### SetAccountCreditCardRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CreditCardAccountType` | `AccountCreditCardType` | 1 | 1 | false |
| `CreditCardNumber` | `string` | 0 | 1 | false |
| `ExpirationMonth` | `int` | 1 | 1 | false |
| `ExpirationYear` | `int` | 1 | 1 | false |
| `CvcCode` | `string` | 0 | 1 | false |
| `IssueCode` | `string` | 0 | 1 | false |
| `CreditCardType` | `int` | 1 | 1 | true |
| `BillingName` | `string` | 0 | 1 | false |
| `UseMainAddress` | `boolean` | 1 | 1 | false |
| `BillingAddress` | `string` | 0 | 1 | false |
| `BillingCity` | `string` | 0 | 1 | false |
| `BillingState` | `string` | 0 | 1 | false |
| `BillingZip` | `string` | 0 | 1 | false |
| `BillingCountry` | `string` | 0 | 1 | false |
| `HideFromWeb` | `boolean` | 1 | 1 | true |
| `CustomerKey` | `string` | 0 | 1 | false |

### SetAccountCreditCardTokenRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CreditCardAccountType` | `AccountCreditCardType` | 1 | 1 | false |
| `CreditCardToken` | `string` | 0 | 1 | false |
| `ExpirationMonth` | `int` | 1 | 1 | false |
| `ExpirationYear` | `int` | 1 | 1 | false |
| `CreditCardType` | `int` | 1 | 1 | true |
| `BillingName` | `string` | 0 | 1 | false |
| `UseMainAddress` | `boolean` | 1 | 1 | false |
| `BillingAddress` | `string` | 0 | 1 | false |
| `BillingAddress2` | `string` | 0 | 1 | false |
| `BillingCity` | `string` | 0 | 1 | false |
| `BillingState` | `string` | 0 | 1 | false |
| `BillingZip` | `string` | 0 | 1 | false |
| `BillingCountry` | `string` | 0 | 1 | false |
| `HideFromWeb` | `boolean` | 1 | 1 | true |
| `CustomerKey` | `string` | 0 | 1 | false |
| `MovePrimaryToSecondary` | `boolean` | 1 | 1 | false |
| `TokenType` | `int` | 1 | 1 | true |
| `FirstSix` | `string` | 0 | 1 | false |
| `LastFour` | `string` | 0 | 1 | false |

### SetAccountDirectDepositRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `NameOnAccount` | `string` | 0 | 1 | false |
| `BankAccountNumber` | `string` | 0 | 1 | false |
| `BankRoutingNumber` | `string` | 0 | 1 | false |
| `DepositAccountType` | `DepositAccountType` | 1 | 1 | false |
| `BankName` | `string` | 0 | 1 | false |
| `BankAddress` | `string` | 0 | 1 | false |
| `BankCity` | `string` | 0 | 1 | false |
| `BankState` | `string` | 0 | 1 | false |
| `BankZip` | `string` | 0 | 1 | false |
| `BankCountry` | `string` | 0 | 1 | false |
| `Iban` | `string` | 0 | 1 | false |
| `SwiftCode` | `string` | 0 | 1 | false |
| `BankAccountType` | `BankAccountType` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `DepositAccountTypeID` | `int` | 1 | 1 | true |

### SetAccountResponse
Extends `ApiResponse`.

_No fields._

### SetAccountWalletRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `WalletAccountType` | `AccountWalletType` | 1 | 1 | false |
| `WalletType` | `int` | 1 | 1 | false |
| `WalletAccount` | `string` | 0 | 1 | false |
| `WalletOther1` | `string` | 0 | 1 | false |
| `WalletOther2` | `string` | 0 | 1 | false |
| `WalletOther3` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### SetBinaryPreferenceRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `PlacementType` | `BinaryPlacementType` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### SetBinaryPreferenceResponse
Extends `ApiResponse`.

_No fields._

### SetCustomerLeadSocialNetworksRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerLeadID` | `int` | 1 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerLeadSocialNetworks` | `ArrayOfCustomerLeadSocialNetworkRequest` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### SetCustomerLeadSocialNetworksResponse
Extends `ApiResponse`.

_No fields._

### SetCustomerSiteImageRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `ImageName` | `string` | 0 | 1 | false |
| `ImageData` | `base64Binary` | 0 | 1 | false |
| `CustomerSiteImageType` | `CustomerSiteImageType` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### SetCustomerSiteImageResponse
Extends `ApiResponse`.

_No fields._

### SetCustomerSiteRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `WebAlias` | `string` | 0 | 1 | false |
| `FirstName` | `string` | 0 | 1 | false |
| `LastName` | `string` | 0 | 1 | false |
| `Company` | `string` | 0 | 1 | false |
| `Address1` | `string` | 0 | 1 | false |
| `Address2` | `string` | 0 | 1 | false |
| `City` | `string` | 0 | 1 | false |
| `State` | `string` | 0 | 1 | false |
| `Zip` | `string` | 0 | 1 | false |
| `Country` | `string` | 0 | 1 | false |
| `Email` | `string` | 0 | 1 | false |
| `Phone` | `string` | 0 | 1 | false |
| `Phone2` | `string` | 0 | 1 | false |
| `Fax` | `string` | 0 | 1 | false |
| `Notes1` | `string` | 0 | 1 | false |
| `Notes2` | `string` | 0 | 1 | false |
| `Notes3` | `string` | 0 | 1 | false |
| `Notes4` | `string` | 0 | 1 | false |
| `Url1` | `string` | 0 | 1 | false |
| `Url2` | `string` | 0 | 1 | false |
| `Url3` | `string` | 0 | 1 | false |
| `Url4` | `string` | 0 | 1 | false |
| `Url5` | `string` | 0 | 1 | false |
| `Url6` | `string` | 0 | 1 | false |
| `Url7` | `string` | 0 | 1 | false |
| `Url8` | `string` | 0 | 1 | false |
| `Url9` | `string` | 0 | 1 | false |
| `Url10` | `string` | 0 | 1 | false |
| `Url1Description` | `string` | 0 | 1 | false |
| `Url2Description` | `string` | 0 | 1 | false |
| `Url3Description` | `string` | 0 | 1 | false |
| `Url4Description` | `string` | 0 | 1 | false |
| `Url5Description` | `string` | 0 | 1 | false |
| `Url6Description` | `string` | 0 | 1 | false |
| `Url7Description` | `string` | 0 | 1 | false |
| `Url8Description` | `string` | 0 | 1 | false |
| `Url9Description` | `string` | 0 | 1 | false |
| `Url10Description` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### SetCustomerSiteResponse
Extends `ApiResponse`.

_No fields._

### SetCustomerSocialNetworksRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerSocialNetworks` | `ArrayOfCustomerSocialNetworkRequest` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### SetCustomerSocialNetworksResponse
Extends `ApiResponse`.

_No fields._

### SetGuestSocialNetworksRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `GuestID` | `int` | 1 | 1 | false |
| `GuestSocialNetworks` | `ArrayOfGuestSocialNetworkRequest` | 0 | 1 | false |

### SetGuestSocialNetworksResponse
Extends `ApiResponse`.

_No fields._

### SetImageFileRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Path` | `string` | 0 | 1 | false |
| `Name` | `string` | 0 | 1 | false |
| `ImageData` | `base64Binary` | 0 | 1 | false |

### SetImageFileResponse
Extends `ApiResponse`.

_No fields._

### SetItemCountryRegionRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ItemCode` | `string` | 0 | 1 | false |
| `CountryCode` | `string` | 0 | 1 | false |
| `RegionCode` | `string` | 0 | 1 | false |
| `Taxed` | `boolean` | 1 | 1 | true |
| `TaxedFed` | `boolean` | 1 | 1 | true |
| `TaxedState` | `boolean` | 1 | 1 | true |
| `UseTaxOverride` | `boolean` | 1 | 1 | true |
| `TaxOverridePct` | `decimal` | 1 | 1 | true |
| `BulkUpdate` | `boolean` | 1 | 1 | false |

### SetItemCountryRegionResponse
Extends `ApiResponse`.

_No fields._

### SetItemImageRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ItemCode` | `string` | 0 | 1 | false |
| `TinyImageName` | `string` | 0 | 1 | false |
| `TinyImageData` | `base64Binary` | 0 | 1 | false |
| `SmallImageName` | `string` | 0 | 1 | false |
| `SmallImageData` | `base64Binary` | 0 | 1 | false |
| `LargeImageName` | `string` | 0 | 1 | false |
| `LargeImageData` | `base64Binary` | 0 | 1 | false |

### SetItemImageResponse
Extends `ApiResponse`.

_No fields._

### SetItemKitMembersRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ParentItemCode` | `string` | 0 | 1 | false |
| `ItemKitMembers` | `ArrayOfKitMember` | 0 | 1 | false |

### SetItemKitMembersResponse
Extends `ApiResponse`.

_No fields._

### SetItemPointAccountRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ItemCode` | `string` | 0 | 1 | false |
| `ItemID` | `int` | 1 | 1 | true |
| `PointAccounts` | `ArrayOfPointAccount` | 0 | 1 | false |

### SetItemPointAccountResponse
Extends `ApiResponse`.

_No fields._

### SetItemPriceRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ItemCode` | `string` | 0 | 1 | false |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `PriceType` | `int` | 1 | 1 | false |
| `Price` | `decimal` | 1 | 1 | true |
| `BusinessVolume` | `decimal` | 1 | 1 | true |
| `CommissionableVolume` | `decimal` | 1 | 1 | true |
| `TaxablePrice` | `decimal` | 1 | 1 | true |
| `ShippingPrice` | `decimal` | 1 | 1 | true |
| `Other1Price` | `decimal` | 1 | 1 | true |
| `Other2Price` | `decimal` | 1 | 1 | true |
| `Other3Price` | `decimal` | 1 | 1 | true |
| `Other4Price` | `decimal` | 1 | 1 | true |
| `Other5Price` | `decimal` | 1 | 1 | true |
| `Other6Price` | `decimal` | 1 | 1 | true |
| `Other7Price` | `decimal` | 1 | 1 | true |
| `Other8Price` | `decimal` | 1 | 1 | true |
| `Other9Price` | `decimal` | 1 | 1 | true |
| `Other10Price` | `decimal` | 1 | 1 | true |

### SetItemPriceResponse
Extends `ApiResponse`.

_No fields._

### SetItemSubscriptionRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ItemCode` | `string` | 0 | 1 | false |
| `ItemID` | `int` | 1 | 1 | true |
| `Subscriptions` | `ArrayOfSubscription` | 0 | 1 | false |

### SetItemSubscriptionResponse
Extends `ApiResponse`.

_No fields._

### SetItemWarehouseRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `AllowedUserWarehouses` | `ArrayOfInt` | 0 | 1 | false |
| `AllowedWarehouseManagementTypes` | `ArrayOfInt` | 0 | 1 | false |
| `ItemCode` | `string` | 0 | 1 | false |
| `WarehouseID` | `int` | 1 | 1 | false |
| `IsAvailable` | `boolean` | 1 | 1 | true |
| `ItemManageTypeID` | `int` | 1 | 1 | true |

### SetItemWarehouseResponse
Extends `ApiResponse`.

_No fields._

### SetQualificationOverrideRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `OverrideID` | `int` | 1 | 1 | false |
| `Qualifies` | `boolean` | 1 | 1 | false |
| `PeriodType` | `int` | 1 | 1 | true |
| `StartPeriodID` | `int` | 1 | 1 | true |
| `EndPeriodID` | `int` | 1 | 1 | true |
| `Amount` | `decimal` | 1 | 1 | true |
| `CustomerKey` | `string` | 0 | 1 | false |

### SetQualificationOverrideResponse
Extends `ApiResponse`.

_No fields._

### SetSessionRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SessionID` | `string` | 0 | 1 | false |
| `SessionData` | `string` | 0 | 1 | false |

### SetSessionResponse
Extends `ApiResponse`.

_No fields._

### ShipMethodResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ShipMethodID` | `int` | 1 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `ShippingAmount` | `decimal` | 1 | 1 | false |

### StartSandboxRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SandboxID` | `int` | 1 | 1 | false |
| `EnableRevolvingCommissionRun` | `boolean` | 1 | 1 | false |
| `EnableBiSync` | `boolean` | 1 | 1 | false |
| `UseRealTimeBackup` | `boolean` | 1 | 1 | false |
| `SyncFilterDays` | `int` | 1 | 1 | false |
| `SyncSettingsEnable` | `string` | 0 | 1 | false |

### StartSandboxResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Sandbox` | `Sandbox` | 0 | 1 | false |

### StopSandboxRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SandboxID` | `int` | 1 | 1 | false |

### StopSandboxResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SandboxID` | `int` | 1 | 1 | false |

### SubmitDestinationTestRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ServerName` | `string` | 0 | 1 | false |
| `DatabaseName` | `string` | 0 | 1 | false |
| `UserId` | `string` | 0 | 1 | false |
| `Password` | `string` | 0 | 1 | false |

### SubmitDestinationTestResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `RequestId` | `guid` | 1 | 1 | false |

### Subscription

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SubscriptionID` | `int` | 1 | 1 | false |
| `TimeAdjustmentDays` | `int` | 1 | 1 | false |

### SubscriptionResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SubscriptionID` | `int` | 1 | 1 | false |
| `Status` | `SubscriptionStatus` | 1 | 1 | false |
| `StartDate` | `dateTime` | 1 | 1 | false |
| `ExpireDate` | `dateTime` | 1 | 1 | false |

### TableFilterSetting

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SchemaName` | `string` | 0 | 1 | false |
| `TableName` | `string` | 0 | 1 | false |
| `ColumnName` | `string` | 0 | 1 | false |
| `FilterType` | `FilterType` | 1 | 1 | false |
| `FilterValue` | `string` | 0 | 1 | false |
| `IsKey` | `boolean` | 1 | 1 | false |

### TableName

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SchemaName` | `string` | 0 | 1 | false |
| `Name` | `string` | 0 | 1 | false |

### TableSettings

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `SchemaName` | `string` | 0 | 1 | false |
| `TableName` | `string` | 0 | 1 | false |
| `IsMemoryOptimized` | `boolean` | 1 | 1 | false |
| `UseColumnStore` | `boolean` | 1 | 1 | false |
| `ModifiedDate` | `dateTime` | 1 | 1 | false |

### TerminateCustomerRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `AgreedToTerminate` | `boolean` | 1 | 1 | false |
| `TerminationSettingID` | `int` | 1 | 1 | true |

### TerminateCustomerResponse
Extends `ApiResponse`.

_No fields._

### TransactionalRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `TransactionRequests` | `ArrayOfApiRequest` | 0 | 1 | false |

### TransactionalResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `TransactionResponses` | `ArrayOfApiResponse` | 0 | 1 | false |

### UpdateAlertSettingsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DestinationID` | `int` | 1 | 1 | false |
| `AlertOptIn` | `boolean` | 1 | 1 | false |
| `AlertEmails` | `ArrayOfString` | 0 | 1 | false |
| `AlertPhones` | `ArrayOfString` | 0 | 1 | false |

### UpdateAlertSettingsResponse
Extends `ApiResponse`.

_No fields._

### UpdateAutoOrderDetailRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `AutoOrderID` | `int` | 1 | 1 | false |
| `OrderLine` | `int` | 1 | 1 | false |
| `ItemID` | `int` | 1 | 1 | false |
| `Qty` | `decimal` | 1 | 1 | false |
| `ManualPriceEach` | `decimal` | 1 | 1 | true |
| `ManualTaxablePriceEach` | `decimal` | 1 | 1 | true |
| `ManualShippingPriceEach` | `decimal` | 1 | 1 | true |
| `ManualBVEach` | `decimal` | 1 | 1 | true |
| `ManualCVEach` | `decimal` | 1 | 1 | true |
| `Description` | `string` | 0 | 1 | false |
| `PeriodDescriptionTy` | `int` | 1 | 1 | true |
| `PriceEach` | `decimal` | 1 | 1 | true |
| `PriceExt` | `decimal` | 1 | 1 | true |
| `BVEach` | `decimal` | 1 | 1 | true |
| `BusinessVolume` | `decimal` | 1 | 1 | true |
| `CVEach` | `decimal` | 1 | 1 | true |
| `CommissionableVolume` | `decimal` | 1 | 1 | true |
| `DynamicKitItemID` | `int` | 1 | 1 | true |
| `Reference1` | `string` | 0 | 1 | false |

### UpdateAutoOrderDetailResponse
Extends `ApiResponse`.

_No fields._

### UpdateAutoOrderRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `AutoOrderID` | `int` | 1 | 1 | false |
| `Frequency` | `FrequencyType` | 1 | 1 | true |
| `StartDate` | `dateTime` | 1 | 1 | true |
| `StopDate` | `dateTime` | 1 | 1 | true |
| `SpecificDayInterval` | `int` | 1 | 1 | true |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `WarehouseID` | `int` | 1 | 1 | true |
| `ShipMethodID` | `int` | 1 | 1 | true |
| `PaymentType` | `AutoOrderPaymentType` | 1 | 1 | true |
| `ProcessType` | `AutoOrderProcessType` | 1 | 1 | true |
| `FirstName` | `string` | 0 | 1 | false |
| `MiddleName` | `string` | 0 | 1 | false |
| `LastName` | `string` | 0 | 1 | false |
| `NameSuffix` | `string` | 0 | 1 | false |
| `Company` | `string` | 0 | 1 | false |
| `Address1` | `string` | 0 | 1 | false |
| `Address2` | `string` | 0 | 1 | false |
| `Address3` | `string` | 0 | 1 | false |
| `City` | `string` | 0 | 1 | false |
| `State` | `string` | 0 | 1 | false |
| `Zip` | `string` | 0 | 1 | false |
| `Country` | `string` | 0 | 1 | false |
| `County` | `string` | 0 | 1 | false |
| `Email` | `string` | 0 | 1 | false |
| `Phone` | `string` | 0 | 1 | false |
| `Notes` | `string` | 0 | 1 | false |
| `Other11` | `string` | 0 | 1 | false |
| `Other12` | `string` | 0 | 1 | false |
| `Other13` | `string` | 0 | 1 | false |
| `Other14` | `string` | 0 | 1 | false |
| `Other15` | `string` | 0 | 1 | false |
| `Other16` | `string` | 0 | 1 | false |
| `Other17` | `string` | 0 | 1 | false |
| `Other18` | `string` | 0 | 1 | false |
| `Other19` | `string` | 0 | 1 | false |
| `Other20` | `string` | 0 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `CustomFrequencyTy` | `int` | 1 | 1 | true |

### UpdateAutoOrderResponse
Extends `ApiResponse`.

_No fields._

### UpdateBillRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `VendorBillID` | `int` | 1 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |
| `WarehouseID` | `int` | 1 | 1 | true |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `DatePaymentDue` | `dateTime` | 1 | 1 | true |
| `Reference` | `string` | 0 | 1 | false |
| `DateReceived` | `dateTime` | 1 | 1 | true |
| `Amount` | `decimal` | 1 | 1 | true |
| `IsOtherIncome` | `boolean` | 1 | 1 | true |
| `Notes` | `string` | 0 | 1 | false |
| `StatusType` | `int` | 1 | 1 | true |
| `PayableType` | `int` | 1 | 1 | true |
| `TaxablePeriodTy` | `int` | 1 | 1 | true |
| `TaxablePeriodID` | `int` | 1 | 1 | true |
| `VendorBillTy` | `int` | 1 | 1 | true |

### UpdateBillResponse
Extends `ApiResponse`.

_No fields._

### UpdateCalendarItemRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `UserID` | `int` | 1 | 1 | false |
| `CalendarID` | `int` | 1 | 1 | false |
| `CalendarItemID` | `int` | 1 | 1 | false |
| `CalendarItemType` | `CalendarItemType` | 1 | 1 | false |
| `CalendarItemStatusType` | `CalendarItemStatusType` | 1 | 1 | true |
| `CalendarItemPriorityType` | `CalendarItemPriorityType` | 1 | 1 | true |
| `Subject` | `string` | 0 | 1 | false |
| `Location` | `string` | 0 | 1 | false |
| `Notes` | `string` | 0 | 1 | false |
| `StartDate` | `dateTime` | 1 | 1 | false |
| `EndDate` | `dateTime` | 1 | 1 | false |
| `TimeZone` | `int` | 1 | 1 | false |
| `Address1` | `string` | 0 | 1 | false |
| `Address2` | `string` | 0 | 1 | false |
| `City` | `string` | 0 | 1 | false |
| `State` | `string` | 0 | 1 | false |
| `Country` | `string` | 0 | 1 | false |
| `PostalCode` | `string` | 0 | 1 | false |
| `ContactInfo` | `string` | 0 | 1 | false |
| `ContactPhone` | `string` | 0 | 1 | false |
| `ContactPhoneType` | `ContactPhoneType` | 1 | 1 | false |
| `ContactEmail` | `string` | 0 | 1 | false |
| `EventHost` | `string` | 0 | 1 | false |
| `SpecialGuests` | `string` | 0 | 1 | false |
| `EventFlyer` | `string` | 0 | 1 | false |
| `EventCostInfo` | `string` | 0 | 1 | false |
| `EventConferenceCallOrWebinar` | `string` | 0 | 1 | false |
| `EventRegistrationInfo` | `string` | 0 | 1 | false |
| `EventTags` | `string` | 0 | 1 | false |
| `IsShared` | `boolean` | 1 | 1 | false |

### UpdateCalendarItemResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CalendarID` | `int` | 1 | 1 | false |
| `CalendarItemID` | `int` | 1 | 1 | false |

### UpdateCustomerContactRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerContactID` | `int` | 1 | 1 | false |
| `FirstName` | `string` | 0 | 1 | false |
| `LastName` | `string` | 0 | 1 | false |
| `MiddleName` | `string` | 0 | 1 | false |
| `Company` | `string` | 0 | 1 | false |
| `BusinessPhone` | `string` | 0 | 1 | false |
| `HomePhone` | `string` | 0 | 1 | false |
| `Mobile` | `string` | 0 | 1 | false |
| `Fax` | `string` | 0 | 1 | false |
| `Email` | `string` | 0 | 1 | false |
| `Address1` | `string` | 0 | 1 | false |
| `Address2` | `string` | 0 | 1 | false |
| `City` | `string` | 0 | 1 | false |
| `State` | `string` | 0 | 1 | false |
| `Zip` | `string` | 0 | 1 | false |
| `Country` | `string` | 0 | 1 | false |
| `BirthDate` | `dateTime` | 1 | 1 | true |
| `Notes` | `string` | 0 | 1 | false |
| `LinkedIn` | `string` | 0 | 1 | false |
| `Facebook` | `string` | 0 | 1 | false |
| `Blog` | `string` | 0 | 1 | false |
| `MySpace` | `string` | 0 | 1 | false |
| `GooglePlus` | `string` | 0 | 1 | false |
| `Twitter` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### UpdateCustomerContactResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerContactID` | `int` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### UpdateCustomerExtendedRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `ExtendedGroupID` | `int` | 1 | 1 | false |
| `CustomerExtendedID` | `int` | 1 | 1 | false |
| `Field1` | `string` | 1 | 1 | true |
| `Field2` | `string` | 1 | 1 | true |
| `Field3` | `string` | 1 | 1 | true |
| `Field4` | `string` | 1 | 1 | true |
| `Field5` | `string` | 1 | 1 | true |
| `Field6` | `string` | 1 | 1 | true |
| `Field7` | `string` | 1 | 1 | true |
| `Field8` | `string` | 1 | 1 | true |
| `Field9` | `string` | 1 | 1 | true |
| `Field10` | `string` | 1 | 1 | true |
| `Field11` | `string` | 1 | 1 | true |
| `Field12` | `string` | 1 | 1 | true |
| `Field13` | `string` | 1 | 1 | true |
| `Field14` | `string` | 1 | 1 | true |
| `Field15` | `string` | 1 | 1 | true |
| `Field16` | `string` | 1 | 1 | true |
| `Field17` | `string` | 1 | 1 | true |
| `Field18` | `string` | 1 | 1 | true |
| `Field19` | `string` | 1 | 1 | true |
| `Field20` | `string` | 1 | 1 | true |
| `Field21` | `string` | 1 | 1 | true |
| `Field22` | `string` | 1 | 1 | true |
| `Field23` | `string` | 1 | 1 | true |
| `Field24` | `string` | 1 | 1 | true |
| `Field25` | `string` | 1 | 1 | true |
| `Field26` | `string` | 1 | 1 | true |
| `Field27` | `string` | 1 | 1 | true |
| `Field28` | `string` | 1 | 1 | true |
| `Field29` | `string` | 1 | 1 | true |
| `Field30` | `string` | 1 | 1 | true |
| `CustomerKey` | `string` | 0 | 1 | false |

### UpdateCustomerExtendedResponse
Extends `ApiResponse`.

_No fields._

### UpdateCustomerLeadRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `CustomerLeadID` | `int` | 1 | 1 | false |
| `FirstName` | `string` | 0 | 1 | false |
| `LastName` | `string` | 0 | 1 | false |
| `MiddleName` | `string` | 0 | 1 | false |
| `Company` | `string` | 0 | 1 | false |
| `Phone` | `string` | 0 | 1 | false |
| `Phone2` | `string` | 0 | 1 | false |
| `MobilePhone` | `string` | 0 | 1 | false |
| `Fax` | `string` | 0 | 1 | false |
| `Email` | `string` | 0 | 1 | false |
| `Address1` | `string` | 0 | 1 | false |
| `Address2` | `string` | 0 | 1 | false |
| `City` | `string` | 0 | 1 | false |
| `State` | `string` | 0 | 1 | false |
| `Zip` | `string` | 0 | 1 | false |
| `Country` | `string` | 0 | 1 | false |
| `BirthDate` | `dateTime` | 1 | 1 | true |
| `Notes` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### UpdateCustomerLeadResponse
Extends `ApiResponse`.

_No fields._

### UpdateCustomerRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `FirstName` | `string` | 1 | 1 | true |
| `LastName` | `string` | 1 | 1 | true |
| `Company` | `string` | 1 | 1 | true |
| `CustomerType` | `int` | 1 | 1 | true |
| `CustomerStatus` | `int` | 1 | 1 | true |
| `Email` | `string` | 1 | 1 | true |
| `Phone` | `string` | 1 | 1 | true |
| `Phone2` | `string` | 1 | 1 | true |
| `MobilePhone` | `string` | 1 | 1 | true |
| `Fax` | `string` | 1 | 1 | true |
| `MainAddress1` | `string` | 1 | 1 | true |
| `MainAddress2` | `string` | 1 | 1 | true |
| `MainAddress3` | `string` | 1 | 1 | true |
| `MainCity` | `string` | 1 | 1 | true |
| `MainState` | `string` | 1 | 1 | true |
| `MainZip` | `string` | 1 | 1 | true |
| `MainCountry` | `string` | 1 | 1 | true |
| `MainCounty` | `string` | 1 | 1 | true |
| `MailAddress1` | `string` | 1 | 1 | true |
| `MailAddress2` | `string` | 1 | 1 | true |
| `MailAddress3` | `string` | 1 | 1 | true |
| `MailCity` | `string` | 1 | 1 | true |
| `MailState` | `string` | 1 | 1 | true |
| `MailZip` | `string` | 1 | 1 | true |
| `MailCountry` | `string` | 1 | 1 | true |
| `MailCounty` | `string` | 1 | 1 | true |
| `OtherAddress1` | `string` | 1 | 1 | true |
| `OtherAddress2` | `string` | 1 | 1 | true |
| `OtherAddress3` | `string` | 1 | 1 | true |
| `OtherCity` | `string` | 1 | 1 | true |
| `OtherState` | `string` | 1 | 1 | true |
| `OtherZip` | `string` | 1 | 1 | true |
| `OtherCountry` | `string` | 1 | 1 | true |
| `OtherCounty` | `string` | 1 | 1 | true |
| `CanLogin` | `boolean` | 1 | 1 | true |
| `LoginName` | `string` | 1 | 1 | true |
| `LoginPassword` | `string` | 1 | 1 | true |
| `TaxID` | `string` | 1 | 1 | true |
| `SalesTaxID` | `string` | 1 | 1 | true |
| `SalesTaxExemptExpireDate` | `dateTime` | 1 | 1 | true |
| `IsSalesTaxExempt` | `boolean` | 1 | 1 | true |
| `BirthDate` | `dateTime` | 1 | 1 | true |
| `Field1` | `string` | 1 | 1 | true |
| `Field2` | `string` | 1 | 1 | true |
| `Field3` | `string` | 1 | 1 | true |
| `Field4` | `string` | 1 | 1 | true |
| `Field5` | `string` | 1 | 1 | true |
| `Field6` | `string` | 1 | 1 | true |
| `Field7` | `string` | 1 | 1 | true |
| `Field8` | `string` | 1 | 1 | true |
| `Field9` | `string` | 1 | 1 | true |
| `Field10` | `string` | 1 | 1 | true |
| `Field11` | `string` | 1 | 1 | true |
| `Field12` | `string` | 1 | 1 | true |
| `Field13` | `string` | 1 | 1 | true |
| `Field14` | `string` | 1 | 1 | true |
| `Field15` | `string` | 1 | 1 | true |
| `SubscribeToBroadcasts` | `boolean` | 1 | 1 | true |
| `SubscribeFromIPAddress` | `string` | 1 | 1 | true |
| `CurrencyCode` | `string` | 1 | 1 | true |
| `PayableToName` | `string` | 1 | 1 | true |
| `PayableType` | `PayableType` | 1 | 1 | true |
| `DefaultWarehouseID` | `int` | 1 | 1 | true |
| `CheckThreshold` | `decimal` | 1 | 1 | true |
| `CreatedDate` | `dateTime` | 1 | 1 | true |
| `TaxIDType` | `TaxIDType` | 1 | 1 | true |
| `LanguageID` | `int` | 1 | 1 | true |
| `Gender` | `Gender` | 1 | 1 | true |
| `VatRegistration` | `string` | 1 | 1 | true |
| `Date1` | `dateTime` | 1 | 1 | true |
| `Date2` | `dateTime` | 1 | 1 | true |
| `Date3` | `dateTime` | 1 | 1 | true |
| `Date4` | `dateTime` | 1 | 1 | true |
| `Date5` | `dateTime` | 1 | 1 | true |
| `MiddleName` | `string` | 1 | 1 | true |
| `NameSuffix` | `string` | 1 | 1 | true |
| `BinaryPlacementPreference` | `int` | 1 | 1 | true |
| `UseBinaryHoldingTank` | `boolean` | 1 | 1 | true |
| `MainAddressVerified` | `boolean` | 1 | 1 | true |
| `MailAddressVerified` | `boolean` | 1 | 1 | true |
| `OtherAddressVerified` | `boolean` | 1 | 1 | true |
| `CustomerKey` | `string` | 1 | 1 | true |
| `PayableTy` | `string` | 0 | 1 | false |
| `TaxIDTy` | `string` | 0 | 1 | false |
| `GenderID` | `string` | 0 | 1 | false |
| `EntryDate` | `dateTime` | 1 | 1 | true |

### UpdateCustomerResponse
Extends `ApiResponse`.

_No fields._

### UpdateDestinationRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DestinationID` | `int` | 1 | 1 | false |
| `Name` | `string` | 0 | 1 | false |
| `ConnectionString` | `string` | 0 | 1 | false |

### UpdateDestinationResponse
Extends `ApiResponse`.

_No fields._

### UpdateEmailStatusRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `MailID` | `int` | 1 | 1 | false |
| `MailStatusType` | `MailStatusType` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### UpdateEmailStatusResponse
Extends `ApiResponse`.

_No fields._

### UpdateEmailTemplateRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `TemplateID` | `int` | 1 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `Content` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### UpdateEmailTemplateResponse
Extends `ApiResponse`.

_No fields._

### UpdateEntityRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `EntityNameToUpdate` | `string` | 0 | 1 | false |
| `SchemaName` | `string` | 0 | 1 | false |
| `NewEntityName` | `string` | 0 | 1 | false |
| `NewEntitySetName` | `string` | 0 | 1 | false |
| `NewIsLog` | `boolean` | 1 | 1 | true |
| `NewMaxLogDays` | `int` | 1 | 1 | true |
| `NewLogDateField` | `string` | 0 | 1 | false |
| `NewNavigations` | `ArrayOfString` | 0 | 1 | false |
| `NewProperties` | `ArrayOfPropertyDataRequest` | 0 | 1 | false |
| `PropertiesToUpdate` | `ArrayOfPropertyDataUpdateRequest` | 0 | 1 | false |
| `PropertiesToDelete` | `ArrayOfString` | 0 | 1 | false |

### UpdateEntityResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Entity` | `EntityDataResponse` | 0 | 1 | false |

### UpdateExtendedDbSettingsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DestinationID` | `int` | 1 | 1 | false |
| `ExcludedSchemas` | `ArrayOfString` | 0 | 1 | false |

### UpdateExtendedDbSettingsResponse
Extends `ApiResponse`.

_No fields._

### UpdateGuestRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `GuestID` | `int` | 1 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | true |
| `CustomerKey` | `string` | 0 | 1 | false |
| `FirstName` | `string` | 1 | 1 | true |
| `MiddleName` | `string` | 1 | 1 | true |
| `LastName` | `string` | 1 | 1 | true |
| `NameSuffix` | `string` | 1 | 1 | true |
| `Company` | `string` | 1 | 1 | true |
| `Gender` | `Gender` | 1 | 1 | true |
| `GuestStatus` | `int` | 1 | 1 | true |
| `LanguageID` | `int` | 1 | 1 | true |
| `Address1` | `string` | 1 | 1 | true |
| `Address2` | `string` | 1 | 1 | true |
| `Address3` | `string` | 1 | 1 | true |
| `City` | `string` | 1 | 1 | true |
| `County` | `string` | 1 | 1 | true |
| `State` | `string` | 1 | 1 | true |
| `Zip` | `string` | 1 | 1 | true |
| `Country` | `string` | 1 | 1 | true |
| `Phone` | `string` | 1 | 1 | true |
| `Phone2` | `string` | 1 | 1 | true |
| `MobilePhone` | `string` | 1 | 1 | true |
| `Email` | `string` | 1 | 1 | true |
| `Field1` | `string` | 1 | 1 | true |
| `Field2` | `string` | 1 | 1 | true |
| `Field3` | `string` | 1 | 1 | true |
| `Field4` | `string` | 1 | 1 | true |
| `Field5` | `string` | 1 | 1 | true |
| `Field6` | `string` | 1 | 1 | true |
| `Field7` | `string` | 1 | 1 | true |
| `Field8` | `string` | 1 | 1 | true |
| `Field9` | `string` | 1 | 1 | true |
| `Field10` | `string` | 1 | 1 | true |
| `Field11` | `string` | 1 | 1 | true |
| `Field12` | `string` | 1 | 1 | true |
| `Field13` | `string` | 1 | 1 | true |
| `Field14` | `string` | 1 | 1 | true |
| `Field15` | `string` | 1 | 1 | true |
| `Date1` | `dateTime` | 1 | 1 | true |
| `Date2` | `dateTime` | 1 | 1 | true |
| `Date3` | `dateTime` | 1 | 1 | true |
| `Date4` | `dateTime` | 1 | 1 | true |
| `Date5` | `dateTime` | 1 | 1 | true |
| `Notes` | `string` | 1 | 1 | true |
| `GenderID` | `string` | 0 | 1 | false |

### UpdateGuestResponse
Extends `ApiResponse`.

_No fields._

### UpdateItemRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ItemCode` | `string` | 0 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `Weight` | `decimal` | 1 | 1 | true |
| `Notes` | `string` | 0 | 1 | false |
| `AvailableInAllCountryRegions` | `boolean` | 1 | 1 | true |
| `TaxedInAllCountryRegions` | `boolean` | 1 | 1 | true |
| `AvailableInAllWarehouses` | `boolean` | 1 | 1 | true |
| `IsVirtual` | `boolean` | 1 | 1 | true |
| `ItemTypeID` | `int` | 1 | 1 | true |
| `ShortDetail` | `string` | 0 | 1 | false |
| `ShortDetail2` | `string` | 0 | 1 | false |
| `ShortDetail3` | `string` | 0 | 1 | false |
| `ShortDetail4` | `string` | 0 | 1 | false |
| `LongDetail` | `string` | 0 | 1 | false |
| `LongDetail2` | `string` | 0 | 1 | false |
| `LongDetail3` | `string` | 0 | 1 | false |
| `LongDetail4` | `string` | 0 | 1 | false |
| `OtherCheck1` | `boolean` | 1 | 1 | true |
| `OtherCheck2` | `boolean` | 1 | 1 | true |
| `OtherCheck3` | `boolean` | 1 | 1 | true |
| `OtherCheck4` | `boolean` | 1 | 1 | true |
| `OtherCheck5` | `boolean` | 1 | 1 | true |
| `Field1` | `string` | 0 | 1 | false |
| `Field2` | `string` | 0 | 1 | false |
| `Field3` | `string` | 0 | 1 | false |
| `Field4` | `string` | 0 | 1 | false |
| `Field5` | `string` | 0 | 1 | false |
| `Field6` | `string` | 0 | 1 | false |
| `Field7` | `string` | 0 | 1 | false |
| `Field8` | `string` | 0 | 1 | false |
| `Field9` | `string` | 0 | 1 | false |
| `Field10` | `string` | 0 | 1 | false |
| `HideFromSearch` | `boolean` | 1 | 1 | true |
| `IsSubscriptionUpdate` | `boolean` | 1 | 1 | true |
| `IsPointIncrement` | `boolean` | 1 | 1 | true |
| `IsGroupMaster` | `boolean` | 1 | 1 | true |
| `SuppressGroupMaster` | `boolean` | 1 | 1 | true |

### UpdateItemResponse
Extends `ApiResponse`.

_No fields._

### UpdateMailFolderRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `MailFolderID` | `int` | 1 | 1 | false |
| `MailFolderName` | `string` | 0 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### UpdateMailFolderResponse
Extends `ApiResponse`.

_No fields._

### UpdateOrderDetailRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderID` | `int` | 1 | 1 | false |
| `ItemID` | `int` | 1 | 1 | true |
| `ItemCode` | `string` | 0 | 1 | false |
| `OrderLine` | `int` | 1 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `Qty` | `decimal` | 1 | 1 | true |
| `PriceEach` | `decimal` | 1 | 1 | true |
| `PriceExt` | `decimal` | 1 | 1 | true |
| `BVEach` | `decimal` | 1 | 1 | true |
| `BusinessVolume` | `decimal` | 1 | 1 | true |
| `CVEach` | `decimal` | 1 | 1 | true |
| `CommissionableVolume` | `decimal` | 1 | 1 | true |
| `ShippingPriceEach` | `decimal` | 1 | 1 | true |
| `ChargeShippingOn` | `decimal` | 1 | 1 | true |
| `IsTaxedInRegion` | `boolean` | 1 | 1 | true |
| `IsTaxedInRegionFed` | `boolean` | 1 | 1 | true |
| `IsTaxedInRegionState` | `boolean` | 1 | 1 | true |
| `TaxablePriceEach` | `decimal` | 1 | 1 | true |
| `Taxable` | `decimal` | 1 | 1 | true |
| `CombinedTax` | `decimal` | 1 | 1 | true |
| `FedTax` | `decimal` | 1 | 1 | true |
| `StateTax` | `decimal` | 1 | 1 | true |
| `CityTax` | `decimal` | 1 | 1 | true |
| `CityLocalTax` | `decimal` | 1 | 1 | true |
| `CountyTax` | `decimal` | 1 | 1 | true |
| `CountyLocalTax` | `decimal` | 1 | 1 | true |
| `ManualTax` | `decimal` | 1 | 1 | true |
| `IsBackOrder` | `boolean` | 1 | 1 | true |
| `WeightEach` | `decimal` | 1 | 1 | true |
| `Other1Each` | `decimal` | 1 | 1 | true |
| `Other1` | `decimal` | 1 | 1 | true |
| `Other2Each` | `decimal` | 1 | 1 | true |
| `Other2` | `decimal` | 1 | 1 | true |
| `Other3Each` | `decimal` | 1 | 1 | true |
| `Other3` | `decimal` | 1 | 1 | true |
| `Other4Each` | `decimal` | 1 | 1 | true |
| `Other4` | `decimal` | 1 | 1 | true |
| `Other5Each` | `decimal` | 1 | 1 | true |
| `Other5` | `decimal` | 1 | 1 | true |
| `Other6Each` | `decimal` | 1 | 1 | true |
| `Other6` | `decimal` | 1 | 1 | true |
| `Other7Each` | `decimal` | 1 | 1 | true |
| `Other7` | `decimal` | 1 | 1 | true |
| `Other8Each` | `decimal` | 1 | 1 | true |
| `Other8` | `decimal` | 1 | 1 | true |
| `Other9Each` | `decimal` | 1 | 1 | true |
| `Other9` | `decimal` | 1 | 1 | true |
| `Other10Each` | `decimal` | 1 | 1 | true |
| `Other10` | `decimal` | 1 | 1 | true |
| `DiscountExt` | `decimal` | 1 | 1 | true |
| `OriginalTaxableEach` | `decimal` | 1 | 1 | true |
| `OriginalBVEach` | `decimal` | 1 | 1 | true |
| `OriginalCVEach` | `decimal` | 1 | 1 | true |
| `StateTaxable` | `decimal` | 1 | 1 | true |
| `IsStateTaxOverride` | `boolean` | 1 | 1 | true |
| `DynamicKitItemID` | `int` | 1 | 1 | true |
| `HandlingFee` | `decimal` | 1 | 1 | true |
| `Reference1` | `string` | 0 | 1 | false |
| `OrderKey` | `string` | 0 | 1 | false |

### UpdateOrderDetailResponse
Extends `ApiResponse`.

_No fields._

### UpdateOrderRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `OrderID` | `int` | 1 | 1 | false |
| `OrderDate` | `dateTime` | 1 | 1 | true |
| `DeclineCount` | `int` | 1 | 1 | true |
| `OrderTy` | `int` | 1 | 1 | true |
| `OrderStatus` | `int` | 1 | 1 | true |
| `PriceTy` | `int` | 1 | 1 | true |
| `Total` | `decimal` | 1 | 1 | true |
| `SubTotal` | `decimal` | 1 | 1 | true |
| `Shipping` | `decimal` | 1 | 1 | true |
| `OrderTax` | `decimal` | 1 | 1 | true |
| `ShippingTax` | `decimal` | 1 | 1 | true |
| `FedShippingTax` | `decimal` | 1 | 1 | true |
| `StateShippingTax` | `decimal` | 1 | 1 | true |
| `CityShippingTax` | `decimal` | 1 | 1 | true |
| `CityLocalShippingTax` | `decimal` | 1 | 1 | true |
| `CountyShippingTax` | `decimal` | 1 | 1 | true |
| `CountyLocalShippingTax` | `decimal` | 1 | 1 | true |
| `ManualTaxRate` | `decimal` | 1 | 1 | true |
| `TotalTax` | `decimal` | 1 | 1 | true |
| `CurrencyCode` | `string` | 1 | 1 | true |
| `PaymentMethod` | `int` | 1 | 1 | true |
| `WarehouseID` | `int` | 1 | 1 | true |
| `BatchID` | `int` | 1 | 1 | true |
| `PreviousBalance` | `decimal` | 1 | 1 | true |
| `OverrideShipping` | `boolean` | 1 | 1 | true |
| `OverrideTax` | `boolean` | 1 | 1 | true |
| `BusinessVolume` | `decimal` | 1 | 1 | true |
| `CommissionableVolume` | `decimal` | 1 | 1 | true |
| `Other1` | `decimal` | 1 | 1 | true |
| `Other2` | `decimal` | 1 | 1 | true |
| `Other3` | `decimal` | 1 | 1 | true |
| `Other4` | `decimal` | 1 | 1 | true |
| `Other5` | `decimal` | 1 | 1 | true |
| `Discount` | `decimal` | 1 | 1 | true |
| `DiscountPercent` | `decimal` | 1 | 1 | true |
| `Weight` | `decimal` | 1 | 1 | true |
| `Sourcety` | `int` | 1 | 1 | true |
| `Notes` | `string` | 1 | 1 | true |
| `Usr` | `string` | 1 | 1 | true |
| `FirstName` | `string` | 1 | 1 | true |
| `LastName` | `string` | 1 | 1 | true |
| `Company` | `string` | 1 | 1 | true |
| `Address1` | `string` | 1 | 1 | true |
| `Address2` | `string` | 1 | 1 | true |
| `City` | `string` | 1 | 1 | true |
| `State` | `string` | 1 | 1 | true |
| `Zip` | `string` | 1 | 1 | true |
| `Country` | `string` | 1 | 1 | true |
| `Email` | `string` | 1 | 1 | true |
| `Phone` | `string` | 1 | 1 | true |
| `SuppressPackSlipPrice` | `boolean` | 1 | 1 | true |
| `ShipMethodID` | `int` | 1 | 1 | true |
| `AutoOrderID` | `int` | 1 | 1 | true |
| `CreatedBy` | `string` | 1 | 1 | true |
| `ReturnOrderID` | `int` | 1 | 1 | true |
| `OrderRankID` | `int` | 1 | 1 | true |
| `OrderPayRankID` | `int` | 1 | 1 | true |
| `AddressIsVerified` | `boolean` | 1 | 1 | true |
| `County` | `string` | 1 | 1 | true |
| `IsRMA` | `boolean` | 1 | 1 | true |
| `BackOrderFromID` | `int` | 1 | 1 | true |
| `CreditsEarned` | `decimal` | 1 | 1 | true |
| `TotalFedTax` | `decimal` | 1 | 1 | true |
| `TotalStateTax` | `decimal` | 1 | 1 | true |
| `ManualShippingTax` | `decimal` | 1 | 1 | true |
| `ReplacementOrderID` | `int` | 1 | 1 | true |
| `LockedDate` | `dateTime` | 1 | 1 | true |
| `CommissionedDate` | `dateTime` | 1 | 1 | true |
| `Flag1` | `boolean` | 1 | 1 | true |
| `Flag2` | `boolean` | 1 | 1 | true |
| `Flag3` | `boolean` | 1 | 1 | true |
| `Other6` | `decimal` | 1 | 1 | true |
| `Other7` | `decimal` | 1 | 1 | true |
| `Other8` | `decimal` | 1 | 1 | true |
| `Other9` | `decimal` | 1 | 1 | true |
| `Other10` | `decimal` | 1 | 1 | true |
| `OriginalWarehouseID` | `int` | 1 | 1 | true |
| `PickupName` | `string` | 1 | 1 | true |
| `TransferToID` | `int` | 1 | 1 | true |
| `IsCommissionable` | `boolean` | 1 | 1 | true |
| `FulfilledBy` | `string` | 1 | 1 | true |
| `CreditApplied` | `decimal` | 1 | 1 | true |
| `ShippedDate` | `dateTime` | 1 | 1 | true |
| `TaxLockDate` | `dateTime` | 1 | 1 | true |
| `TotalTaxable` | `decimal` | 1 | 1 | true |
| `ReturnCategoryID` | `int` | 1 | 1 | true |
| `ReplacementCategoryID` | `int` | 1 | 1 | true |
| `CalculatedShipping` | `decimal` | 1 | 1 | true |
| `HandlingFee` | `decimal` | 1 | 1 | true |
| `OrderProcessTy` | `int` | 1 | 1 | true |
| `ActualCarrier` | `int` | 1 | 1 | true |
| `ParentOrderID` | `int` | 1 | 1 | true |
| `CustomerTy` | `int` | 1 | 1 | true |
| `Reference` | `string` | 1 | 1 | true |
| `MiddleName` | `string` | 1 | 1 | true |
| `NameSuffix` | `string` | 1 | 1 | true |
| `Address3` | `string` | 1 | 1 | true |
| `PartyID` | `int` | 1 | 1 | true |
| `TrackingNumber1` | `string` | 1 | 1 | true |
| `TrackingNumber2` | `string` | 1 | 1 | true |
| `TrackingNumber3` | `string` | 1 | 1 | true |
| `TrackingNumber4` | `string` | 1 | 1 | true |
| `TrackingNumber5` | `string` | 1 | 1 | true |
| `WebCarrierID` | `OrderShipCarrier` | 1 | 1 | true |
| `WebCarrierID2` | `OrderShipCarrier` | 1 | 1 | true |
| `WebCarrierID3` | `OrderShipCarrier` | 1 | 1 | true |
| `WebCarrierID4` | `OrderShipCarrier` | 1 | 1 | true |
| `WebCarrierID5` | `OrderShipCarrier` | 1 | 1 | true |
| `Other11` | `string` | 1 | 1 | true |
| `Other12` | `string` | 1 | 1 | true |
| `Other13` | `string` | 1 | 1 | true |
| `Other14` | `string` | 1 | 1 | true |
| `Other15` | `string` | 1 | 1 | true |
| `Other16` | `string` | 1 | 1 | true |
| `Other17` | `string` | 1 | 1 | true |
| `Other18` | `string` | 1 | 1 | true |
| `Other19` | `string` | 1 | 1 | true |
| `Other20` | `string` | 1 | 1 | true |
| `TransferToKey` | `string` | 0 | 1 | false |
| `OrderKey` | `string` | 0 | 1 | false |
| `ReturnOrderKey` | `string` | 0 | 1 | false |
| `ReplacementOrderKey` | `string` | 0 | 1 | false |
| `ParentOrderKey` | `string` | 0 | 1 | false |
| `BackOrderFromKey` | `string` | 0 | 1 | false |
| `OrderSubStatusTy` | `int` | 1 | 1 | true |

### UpdateOrderResponse
Extends `ApiResponse`.

_No fields._

### UpdatePartyRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PartyID` | `int` | 1 | 1 | false |
| `PartyType` | `int` | 1 | 1 | true |
| `PartyStatusType` | `int` | 1 | 1 | true |
| `HostID` | `int` | 1 | 1 | true |
| `DistributorID` | `int` | 1 | 1 | true |
| `StartDate` | `dateTime` | 1 | 1 | true |
| `CloseDate` | `dateTime` | 1 | 1 | true |
| `Description` | `string` | 0 | 1 | false |
| `EventStart` | `dateTime` | 1 | 1 | true |
| `EventEnd` | `dateTime` | 1 | 1 | true |
| `LanguageID` | `int` | 1 | 1 | true |
| `Information` | `string` | 0 | 1 | false |
| `Address` | `PartyAddress` | 0 | 1 | false |
| `BookingPartyID` | `int` | 1 | 1 | true |
| `Field1` | `string` | 0 | 1 | false |
| `Field2` | `string` | 0 | 1 | false |
| `Field3` | `string` | 0 | 1 | false |
| `Field4` | `string` | 0 | 1 | false |
| `Field5` | `string` | 0 | 1 | false |
| `TimeZoneID` | `string` | 0 | 1 | false |
| `VirtualMeetingLink` | `string` | 0 | 1 | false |
| `PartyShoppingUrl` | `string` | 0 | 1 | false |
| `PartyExternalID` | `guid` | 1 | 1 | true |

### UpdatePartyResponse
Extends `ApiResponse`.

_No fields._

### UpdateReIndexSettingsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DestinationID` | `int` | 1 | 1 | false |
| `ReIndexStartTime` | `dateTime` | 1 | 1 | true |
| `ReIndexMaxDuration` | `int` | 1 | 1 | true |
| `LastReIndexed` | `dateTime` | 1 | 1 | true |

### UpdateReIndexSettingsResponse
Extends `ApiResponse`.

_No fields._

### UpdateResourceSetBannerItemRequest
Extends `BaseUpdateResourceSetItemRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `NewTitle` | `string` | 0 | 1 | false |
| `NewDescription` | `string` | 0 | 1 | false |
| `NewBannerImageBase64` | `string` | 0 | 1 | false |
| `NewBannerHoverText` | `string` | 0 | 1 | false |
| `NewBannerURL` | `string` | 0 | 1 | false |
| `NewBannerClickEvent` | `BannerClickEvent` | 1 | 1 | true |
| `NewBannerType` | `BannerType` | 1 | 1 | true |
| `NewAssociatedDataSets` | `ArrayOfString` | 0 | 1 | false |

### UpdateResourceSetBooleanItemRequest
Extends `BaseUpdateResourceSetItemRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `NewBooleanValue` | `boolean` | 1 | 1 | true |

### UpdateResourceSetCarouselItemRequest
Extends `BaseUpdateResourceSetItemRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `NewCarouselSlides` | `ArrayOfString` | 0 | 1 | false |
| `NewCarouselType` | `CarouselType` | 1 | 1 | true |

### UpdateResourceSetDataSetItemRequest
Extends `BaseUpdateResourceSetItemRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `NewDataSetType` | `string` | 0 | 1 | false |
| `NewDataSetValues` | `ArrayOfString` | 0 | 1 | false |

### UpdateResourceSetDateItemRequest
Extends `BaseUpdateResourceSetItemRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `NewDate` | `dateTime` | 1 | 1 | true |

### UpdateResourceSetDecimalItemRequest
Extends `BaseUpdateResourceSetItemRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `NewDecimalValue` | `decimal` | 1 | 1 | true |

### UpdateResourceSetDropDownItemRequest
Extends `BaseUpdateResourceSetItemRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `NewDropDownValues` | `string` | 0 | 1 | false |
| `NewDefaultSelectedValue` | `string` | 0 | 1 | false |

### UpdateResourceSetEnvironmentRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `EnvironmentCode` | `string` | 0 | 1 | false |
| `NewEnvironmentCode` | `string` | 0 | 1 | false |
| `NewDescription` | `string` | 0 | 1 | false |
| `NewVersion` | `string` | 0 | 1 | false |
| `NewScheduledVersion` | `string` | 0 | 1 | false |
| `NewScheduledVersionDate` | `dateTime` | 1 | 1 | true |

### UpdateResourceSetEnvironmentResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `EnvironmentCode` | `string` | 0 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `Version` | `string` | 0 | 1 | false |
| `ScheduledVersion` | `string` | 0 | 1 | false |
| `ScheduledVersionDate` | `dateTime` | 1 | 1 | true |

### UpdateResourceSetGroupRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `ResourceGroupID` | `int` | 1 | 1 | false |
| `NewDescription` | `string` | 0 | 1 | false |

### UpdateResourceSetGroupResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `ResourceGroupID` | `int` | 1 | 1 | false |
| `Decription` | `string` | 0 | 1 | false |

### UpdateResourceSetImageItemRequest
Extends `BaseUpdateResourceSetItemRequest`.

_No fields._

### UpdateResourceSetIntItemRequest
Extends `BaseUpdateResourceSetItemRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `NewIntegerValue` | `int` | 1 | 1 | true |

### UpdateResourceSetItemResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `CultureCode` | `string` | 0 | 1 | false |
| `ResourceName` | `string` | 0 | 1 | false |

### UpdateResourceSetRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `ClassName` | `string` | 0 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `Namespace` | `string` | 0 | 1 | false |
| `SubscriptionKey` | `string` | 0 | 1 | false |

### UpdateResourceSetResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `ResourceSetID` | `int` | 1 | 1 | false |
| `ClassName` | `string` | 0 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `Namespace` | `string` | 0 | 1 | false |
| `SubscriptionKey` | `string` | 0 | 1 | false |

### UpdateResourceSetTextItemRequest
Extends `BaseUpdateResourceSetItemRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `NewText` | `string` | 0 | 1 | false |

### UpdateResourceSetWidgetItemRequest
Extends `BaseUpdateResourceSetItemRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `NewHtml` | `string` | 0 | 1 | false |
| `NewJavascript` | `string` | 0 | 1 | false |
| `NewCss` | `string` | 0 | 1 | false |

### UpdateTableFilterSettingsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DestinationId` | `int` | 1 | 1 | false |
| `FilterGroupId` | `TableGroupID` | 1 | 1 | false |
| `ColumnName` | `string` | 0 | 1 | false |
| `SchemaName` | `string` | 0 | 1 | false |
| `TableName` | `string` | 0 | 1 | false |
| `FilterValue` | `string` | 0 | 1 | false |

### UpdateTableFilterSettingsResponse
Extends `ApiResponse`.

_No fields._

### UpdateTableSettingsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `DestinationID` | `int` | 1 | 1 | false |
| `SchemaName` | `string` | 0 | 1 | false |
| `TableName` | `string` | 0 | 1 | false |
| `IsMemoryOptimized` | `boolean` | 1 | 1 | false |
| `UseColumnStore` | `boolean` | 1 | 1 | false |

### UpdateTableSettingsResponse
Extends `ApiResponse`.

_No fields._

### UpdateWebCategoryRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `WebID` | `int` | 1 | 1 | false |
| `CategoryID` | `int` | 1 | 1 | false |
| `Description` | `string` | 0 | 1 | false |

### UpdateWebCategoryResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CategoryID` | `int` | 1 | 1 | false |
| `WebID` | `int` | 1 | 1 | false |
| `Description` | `string` | 0 | 1 | false |

### ValidateCreditCardTokenRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CreditCardIdentifier` | `string` | 0 | 1 | false |
| `ExpirationYear` | `int` | 1 | 1 | true |
| `ExpirationMonth` | `int` | 1 | 1 | true |
| `CvcCode` | `string` | 0 | 1 | false |
| `BillingName` | `string` | 0 | 1 | false |
| `BillingAddress1` | `string` | 0 | 1 | false |
| `BillingAddress2` | `string` | 0 | 1 | false |
| `BillingCity` | `string` | 0 | 1 | false |
| `BillingState` | `string` | 0 | 1 | false |
| `BillingZip` | `string` | 0 | 1 | false |
| `BillingCountry` | `string` | 0 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | true |
| `CustomerKey` | `string` | 0 | 1 | false |
| `OrderID` | `int` | 1 | 1 | true |
| `OrderKey` | `string` | 0 | 1 | false |
| `Other1` | `string` | 0 | 1 | false |
| `Other2` | `string` | 0 | 1 | false |
| `Other3` | `string` | 0 | 1 | false |
| `Other4` | `string` | 0 | 1 | false |
| `Other5` | `string` | 0 | 1 | false |
| `Other6` | `string` | 0 | 1 | false |
| `Other7` | `string` | 0 | 1 | false |
| `Other8` | `string` | 0 | 1 | false |
| `Other9` | `string` | 0 | 1 | false |
| `Other10` | `string` | 0 | 1 | false |
| `ValidateTokenOnFile` | `boolean` | 1 | 1 | false |
| `AccountOnFile` | `TokenAccount` | 1 | 1 | false |
| `WarehouseID` | `int` | 1 | 1 | false |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `Email` | `string` | 0 | 1 | false |
| `Phone` | `string` | 0 | 1 | false |
| `ClientIpAddress` | `string` | 0 | 1 | false |

### ValidateCreditCardTokenResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `AuthorizationCode` | `string` | 0 | 1 | false |
| `Message` | `string` | 0 | 1 | false |
| `Success` | `boolean` | 1 | 1 | false |
| `DisplayMessage` | `string` | 0 | 1 | false |

### ValidateRequest
Extends `ApiRequest`.

_No fields._

### ValidateResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `IsValid` | `boolean` | 1 | 1 | false |

### ValidateWalletAccountRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `WalletAccountNumber` | `string` | 0 | 1 | false |
| `WalletTy` | `int` | 1 | 1 | false |
| `Memo` | `string` | 0 | 1 | false |
| `CustomerID` | `int` | 1 | 1 | true |
| `CustomerKey` | `string` | 0 | 1 | false |
| `OrderID` | `int` | 1 | 1 | true |
| `OrderKey` | `string` | 0 | 1 | false |
| `Other1` | `string` | 0 | 1 | false |
| `Other2` | `string` | 0 | 1 | false |
| `Other3` | `string` | 0 | 1 | false |
| `Other4` | `string` | 0 | 1 | false |
| `Other5` | `string` | 0 | 1 | false |
| `Other6` | `string` | 0 | 1 | false |
| `Other7` | `string` | 0 | 1 | false |
| `Other8` | `string` | 0 | 1 | false |
| `Other9` | `string` | 0 | 1 | false |
| `Other10` | `string` | 0 | 1 | false |
| `ValidateWalletAccountOnFile` | `boolean` | 1 | 1 | false |
| `WalletAccountType` | `AccountWalletType` | 1 | 1 | false |
| `WarehouseID` | `int` | 1 | 1 | false |
| `Email` | `string` | 0 | 1 | false |
| `Phone` | `string` | 0 | 1 | false |
| `CurrencyCode` | `string` | 0 | 1 | false |
| `ClientIpAddress` | `string` | 0 | 1 | false |
| `BillingName` | `string` | 0 | 1 | false |
| `BillingAddress1` | `string` | 0 | 1 | false |
| `BillingAddress2` | `string` | 0 | 1 | false |
| `BillingCity` | `string` | 0 | 1 | false |
| `BillingState` | `string` | 0 | 1 | false |
| `BillingZip` | `string` | 0 | 1 | false |
| `BillingCountry` | `string` | 0 | 1 | false |
| `Amount` | `decimal` | 1 | 1 | false |

### ValidateWalletAccountResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `AuthorizationCode` | `string` | 0 | 1 | false |
| `Message` | `string` | 0 | 1 | false |
| `Success` | `boolean` | 1 | 1 | false |
| `DisplayMessage` | `string` | 0 | 1 | false |

### VerifyAddressRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Address` | `string` | 0 | 1 | false |
| `City` | `string` | 0 | 1 | false |
| `State` | `string` | 0 | 1 | false |
| `Zip` | `string` | 0 | 1 | false |
| `Country` | `string` | 0 | 1 | false |

### VerifyAddressResponse
Extends `ApiResponse`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `Address` | `string` | 0 | 1 | false |
| `City` | `string` | 0 | 1 | false |
| `County` | `string` | 0 | 1 | false |
| `State` | `string` | 0 | 1 | false |
| `Zip` | `string` | 0 | 1 | false |
| `Country` | `string` | 0 | 1 | false |

### VoidPaymentsRequest
Extends `ApiRequest`.

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `PaymentIdStart` | `int` | 1 | 1 | false |
| `PaymentIdEnd` | `int` | 1 | 1 | false |
| `PaymentIds` | `ArrayOfInt` | 0 | 1 | false |
| `Memo` | `string` | 0 | 1 | false |

### VoidPaymentsResponse
Extends `ApiResponse`.

_No fields._

### VolumeFilter

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `VolumeID` | `int` | 1 | 1 | false |
| `Compare` | `NumericCompareType` | 1 | 1 | false |
| `Value` | `decimal` | 1 | 1 | false |

### VolumeResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `CustomerID` | `int` | 1 | 1 | false |
| `PeriodType` | `int` | 1 | 1 | false |
| `PeriodID` | `int` | 1 | 1 | false |
| `PeriodDescription` | `string` | 0 | 1 | false |
| `Volume1` | `decimal` | 1 | 1 | false |
| `Volume2` | `decimal` | 1 | 1 | false |
| `Volume3` | `decimal` | 1 | 1 | false |
| `Volume4` | `decimal` | 1 | 1 | false |
| `Volume5` | `decimal` | 1 | 1 | false |
| `Volume6` | `decimal` | 1 | 1 | false |
| `Volume7` | `decimal` | 1 | 1 | false |
| `Volume8` | `decimal` | 1 | 1 | false |
| `Volume9` | `decimal` | 1 | 1 | false |
| `Volume10` | `decimal` | 1 | 1 | false |
| `Volume11` | `decimal` | 1 | 1 | false |
| `Volume12` | `decimal` | 1 | 1 | false |
| `Volume13` | `decimal` | 1 | 1 | false |
| `Volume14` | `decimal` | 1 | 1 | false |
| `Volume15` | `decimal` | 1 | 1 | false |
| `Volume16` | `decimal` | 1 | 1 | false |
| `Volume17` | `decimal` | 1 | 1 | false |
| `Volume18` | `decimal` | 1 | 1 | false |
| `Volume19` | `decimal` | 1 | 1 | false |
| `Volume20` | `decimal` | 1 | 1 | false |
| `Volume21` | `decimal` | 1 | 1 | false |
| `Volume22` | `decimal` | 1 | 1 | false |
| `Volume23` | `decimal` | 1 | 1 | false |
| `Volume24` | `decimal` | 1 | 1 | false |
| `Volume25` | `decimal` | 1 | 1 | false |
| `Volume26` | `decimal` | 1 | 1 | false |
| `Volume27` | `decimal` | 1 | 1 | false |
| `Volume28` | `decimal` | 1 | 1 | false |
| `Volume29` | `decimal` | 1 | 1 | false |
| `Volume30` | `decimal` | 1 | 1 | false |
| `Volume31` | `decimal` | 1 | 1 | false |
| `Volume32` | `decimal` | 1 | 1 | false |
| `Volume33` | `decimal` | 1 | 1 | false |
| `Volume34` | `decimal` | 1 | 1 | false |
| `Volume35` | `decimal` | 1 | 1 | false |
| `Volume36` | `decimal` | 1 | 1 | false |
| `Volume37` | `decimal` | 1 | 1 | false |
| `Volume38` | `decimal` | 1 | 1 | false |
| `Volume39` | `decimal` | 1 | 1 | false |
| `Volume40` | `decimal` | 1 | 1 | false |
| `Volume41` | `decimal` | 1 | 1 | false |
| `Volume42` | `decimal` | 1 | 1 | false |
| `Volume43` | `decimal` | 1 | 1 | false |
| `Volume44` | `decimal` | 1 | 1 | false |
| `Volume45` | `decimal` | 1 | 1 | false |
| `Volume46` | `decimal` | 1 | 1 | false |
| `Volume47` | `decimal` | 1 | 1 | false |
| `Volume48` | `decimal` | 1 | 1 | false |
| `Volume49` | `decimal` | 1 | 1 | false |
| `Volume50` | `decimal` | 1 | 1 | false |
| `Volume51` | `decimal` | 1 | 1 | false |
| `Volume52` | `decimal` | 1 | 1 | false |
| `Volume53` | `decimal` | 1 | 1 | false |
| `Volume54` | `decimal` | 1 | 1 | false |
| `Volume55` | `decimal` | 1 | 1 | false |
| `Volume56` | `decimal` | 1 | 1 | false |
| `Volume57` | `decimal` | 1 | 1 | false |
| `Volume58` | `decimal` | 1 | 1 | false |
| `Volume59` | `decimal` | 1 | 1 | false |
| `Volume60` | `decimal` | 1 | 1 | false |
| `Volume61` | `decimal` | 1 | 1 | false |
| `Volume62` | `decimal` | 1 | 1 | false |
| `Volume63` | `decimal` | 1 | 1 | false |
| `Volume64` | `decimal` | 1 | 1 | false |
| `Volume65` | `decimal` | 1 | 1 | false |
| `Volume66` | `decimal` | 1 | 1 | false |
| `Volume67` | `decimal` | 1 | 1 | false |
| `Volume68` | `decimal` | 1 | 1 | false |
| `Volume69` | `decimal` | 1 | 1 | false |
| `Volume70` | `decimal` | 1 | 1 | false |
| `Volume71` | `decimal` | 1 | 1 | false |
| `Volume72` | `decimal` | 1 | 1 | false |
| `Volume73` | `decimal` | 1 | 1 | false |
| `Volume74` | `decimal` | 1 | 1 | false |
| `Volume75` | `decimal` | 1 | 1 | false |
| `Volume76` | `decimal` | 1 | 1 | false |
| `Volume77` | `decimal` | 1 | 1 | false |
| `Volume78` | `decimal` | 1 | 1 | false |
| `Volume79` | `decimal` | 1 | 1 | false |
| `Volume80` | `decimal` | 1 | 1 | false |
| `Volume81` | `decimal` | 1 | 1 | false |
| `Volume82` | `decimal` | 1 | 1 | false |
| `Volume83` | `decimal` | 1 | 1 | false |
| `Volume84` | `decimal` | 1 | 1 | false |
| `Volume85` | `decimal` | 1 | 1 | false |
| `Volume86` | `decimal` | 1 | 1 | false |
| `Volume87` | `decimal` | 1 | 1 | false |
| `Volume88` | `decimal` | 1 | 1 | false |
| `Volume89` | `decimal` | 1 | 1 | false |
| `Volume90` | `decimal` | 1 | 1 | false |
| `Volume91` | `decimal` | 1 | 1 | false |
| `Volume92` | `decimal` | 1 | 1 | false |
| `Volume93` | `decimal` | 1 | 1 | false |
| `Volume94` | `decimal` | 1 | 1 | false |
| `Volume95` | `decimal` | 1 | 1 | false |
| `Volume96` | `decimal` | 1 | 1 | false |
| `Volume97` | `decimal` | 1 | 1 | false |
| `Volume98` | `decimal` | 1 | 1 | false |
| `Volume99` | `decimal` | 1 | 1 | false |
| `Volume100` | `decimal` | 1 | 1 | false |
| `RankID` | `int` | 1 | 1 | false |
| `PaidRankID` | `int` | 1 | 1 | false |
| `Volume101` | `decimal` | 1 | 1 | false |
| `Volume102` | `decimal` | 1 | 1 | false |
| `Volume103` | `decimal` | 1 | 1 | false |
| `Volume104` | `decimal` | 1 | 1 | false |
| `Volume105` | `decimal` | 1 | 1 | false |
| `Volume106` | `decimal` | 1 | 1 | false |
| `Volume107` | `decimal` | 1 | 1 | false |
| `Volume108` | `decimal` | 1 | 1 | false |
| `Volume109` | `decimal` | 1 | 1 | false |
| `Volume110` | `decimal` | 1 | 1 | false |
| `Volume111` | `decimal` | 1 | 1 | false |
| `Volume112` | `decimal` | 1 | 1 | false |
| `Volume113` | `decimal` | 1 | 1 | false |
| `Volume114` | `decimal` | 1 | 1 | false |
| `Volume115` | `decimal` | 1 | 1 | false |
| `Volume116` | `decimal` | 1 | 1 | false |
| `Volume117` | `decimal` | 1 | 1 | false |
| `Volume118` | `decimal` | 1 | 1 | false |
| `Volume119` | `decimal` | 1 | 1 | false |
| `Volume120` | `decimal` | 1 | 1 | false |
| `Volume121` | `decimal` | 1 | 1 | false |
| `Volume122` | `decimal` | 1 | 1 | false |
| `Volume123` | `decimal` | 1 | 1 | false |
| `Volume124` | `decimal` | 1 | 1 | false |
| `Volume125` | `decimal` | 1 | 1 | false |
| `Volume126` | `decimal` | 1 | 1 | false |
| `Volume127` | `decimal` | 1 | 1 | false |
| `Volume128` | `decimal` | 1 | 1 | false |
| `Volume129` | `decimal` | 1 | 1 | false |
| `Volume130` | `decimal` | 1 | 1 | false |
| `Volume131` | `decimal` | 1 | 1 | false |
| `Volume132` | `decimal` | 1 | 1 | false |
| `Volume133` | `decimal` | 1 | 1 | false |
| `Volume134` | `decimal` | 1 | 1 | false |
| `Volume135` | `decimal` | 1 | 1 | false |
| `Volume136` | `decimal` | 1 | 1 | false |
| `Volume137` | `decimal` | 1 | 1 | false |
| `Volume138` | `decimal` | 1 | 1 | false |
| `Volume139` | `decimal` | 1 | 1 | false |
| `Volume140` | `decimal` | 1 | 1 | false |
| `Volume141` | `decimal` | 1 | 1 | false |
| `Volume142` | `decimal` | 1 | 1 | false |
| `Volume143` | `decimal` | 1 | 1 | false |
| `Volume144` | `decimal` | 1 | 1 | false |
| `Volume145` | `decimal` | 1 | 1 | false |
| `Volume146` | `decimal` | 1 | 1 | false |
| `Volume147` | `decimal` | 1 | 1 | false |
| `Volume148` | `decimal` | 1 | 1 | false |
| `Volume149` | `decimal` | 1 | 1 | false |
| `Volume150` | `decimal` | 1 | 1 | false |
| `Volume151` | `decimal` | 1 | 1 | false |
| `Volume152` | `decimal` | 1 | 1 | false |
| `Volume153` | `decimal` | 1 | 1 | false |
| `Volume154` | `decimal` | 1 | 1 | false |
| `Volume155` | `decimal` | 1 | 1 | false |
| `Volume156` | `decimal` | 1 | 1 | false |
| `Volume157` | `decimal` | 1 | 1 | false |
| `Volume158` | `decimal` | 1 | 1 | false |
| `Volume159` | `decimal` | 1 | 1 | false |
| `Volume160` | `decimal` | 1 | 1 | false |
| `Volume161` | `decimal` | 1 | 1 | false |
| `Volume162` | `decimal` | 1 | 1 | false |
| `Volume163` | `decimal` | 1 | 1 | false |
| `Volume164` | `decimal` | 1 | 1 | false |
| `Volume165` | `decimal` | 1 | 1 | false |
| `Volume166` | `decimal` | 1 | 1 | false |
| `Volume167` | `decimal` | 1 | 1 | false |
| `Volume168` | `decimal` | 1 | 1 | false |
| `Volume169` | `decimal` | 1 | 1 | false |
| `Volume170` | `decimal` | 1 | 1 | false |
| `Volume171` | `decimal` | 1 | 1 | false |
| `Volume172` | `decimal` | 1 | 1 | false |
| `Volume173` | `decimal` | 1 | 1 | false |
| `Volume174` | `decimal` | 1 | 1 | false |
| `Volume175` | `decimal` | 1 | 1 | false |
| `Volume176` | `decimal` | 1 | 1 | false |
| `Volume177` | `decimal` | 1 | 1 | false |
| `Volume178` | `decimal` | 1 | 1 | false |
| `Volume179` | `decimal` | 1 | 1 | false |
| `Volume180` | `decimal` | 1 | 1 | false |
| `Volume181` | `decimal` | 1 | 1 | false |
| `Volume182` | `decimal` | 1 | 1 | false |
| `Volume183` | `decimal` | 1 | 1 | false |
| `Volume184` | `decimal` | 1 | 1 | false |
| `Volume185` | `decimal` | 1 | 1 | false |
| `Volume186` | `decimal` | 1 | 1 | false |
| `Volume187` | `decimal` | 1 | 1 | false |
| `Volume188` | `decimal` | 1 | 1 | false |
| `Volume189` | `decimal` | 1 | 1 | false |
| `Volume190` | `decimal` | 1 | 1 | false |
| `Volume191` | `decimal` | 1 | 1 | false |
| `Volume192` | `decimal` | 1 | 1 | false |
| `Volume193` | `decimal` | 1 | 1 | false |
| `Volume194` | `decimal` | 1 | 1 | false |
| `Volume195` | `decimal` | 1 | 1 | false |
| `Volume196` | `decimal` | 1 | 1 | false |
| `Volume197` | `decimal` | 1 | 1 | false |
| `Volume198` | `decimal` | 1 | 1 | false |
| `Volume199` | `decimal` | 1 | 1 | false |
| `Volume200` | `decimal` | 1 | 1 | false |
| `CustomerKey` | `string` | 0 | 1 | false |

### WalletAccountResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `WalletType` | `int` | 1 | 1 | false |
| `WalletAccountDisplay` | `string` | 0 | 1 | false |
| `WalletOther1` | `string` | 0 | 1 | false |
| `WalletOther2` | `string` | 0 | 1 | false |
| `WalletOther3` | `string` | 0 | 1 | false |

### WarehouseResponse

| Field | Type | min | max | nillable |
|---|---|---|---|---|
| `WarehouseID` | `int` | 1 | 1 | false |
| `Description` | `string` | 0 | 1 | false |
| `Address1` | `string` | 0 | 1 | false |
| `Address2` | `string` | 0 | 1 | false |
| `City` | `string` | 0 | 1 | false |
| `State` | `string` | 0 | 1 | false |
| `Zip` | `string` | 0 | 1 | false |
| `Country` | `string` | 0 | 1 | false |

