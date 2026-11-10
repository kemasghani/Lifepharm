# Exigo API — Items

API version v2025.11.7.6. Crawled 2026-11-11 from https://api.exigo.com/3.0/. Back to [index](../README.md).

| Operation | REST | Summary |
|---|---|---|
| [GetItems](#getitems) | `GET /3.0/item?currencyCode=usd` | Returns price, volume, and description for one or more item codes. |
| [CreateItem](#createitem) | `POST /3.0/item` | Adds an Item (and optional warehouse/price info) Note: This request can participate in a transaction. Learn more about transactions. |
| [UpdateItem](#updateitem) | `PUT /3.0/item` | Updates an Item (and optional warehouse/price info) Note: This request can participate in a transaction. Learn more about transactions. |
| [SetItemPrice](#setitemprice) | `PUT /3.0/item/price` | Sets pricing info for an item) Note: This request can participate in a transaction. Learn more about transactions. |
| [SetItemWarehouse](#setitemwarehouse) | `PUT /3.0/item/warehouse` | Sets warehouse info for an item) Note: This request can participate in a transaction. Learn more about transactions. |
| [SetItemCountryRegion](#setitemcountryregion) | `PUT /3.0/item/countryregion` | Sets country/region info for an item) Note: This request can participate in a transaction. Learn more about transactions. |
| [SetItemImage](#setitemimage) | `PUT /3.0/item/image` | Set Images for an Item |
| [CreateWebCategory](#createwebcategory) | `POST /3.0/webcategory` | Creates a new product web category. Note: This request can participate in a transaction. Learn more about transactions. |
| [UpdateWebCategory](#updatewebcategory) | `PUT /3.0/webcategory` | Updates web category information. Note: This request can participate in a transaction. Learn more about transactions. |
| [DeleteWebCategory](#deletewebcategory) | `DELETE /3.0/webcategory` | Deletes a web category. Note: This request can participate in a transaction. Learn more about transactions. |
| [AddProductsToCategory](#addproductstocategory) | `POST /3.0/webcategory/product` | Adds items/products to a web category. Note: This request can participate in a transaction. Learn more about transactions. |
| [DeleteProductFromCategory](#deleteproductfromcategory) | `DELETE /3.0/webcategory/product` | Deletes a product from a web category. Note: This request can participate in a transaction. Learn more about transactions. |
| [GetWarehouses](#getwarehouses) | `GET /3.0/warehouse` | Gets a list of warehouses setup in the system. |
| [AdjustInventory](#adjustinventory) | `PUT /3.0/warehouse/inventory` | Posts an adjustment to item inventory. |
| [SetItemKitMembers](#setitemkitmembers) | `PUT /3.0/item/kit/members` | Sets the children for a static kit Note: This request can participate in a transaction. Learn more about transactions. |
| [SetItemSubscription](#setitemsubscription) | `PUT /3.0/item/subscription` | Set Item Subscriptions Note: This request can participate in a transaction. Learn more about transactions. |
| [SetItemPointAccount](#setitempointaccount) | `PUT /3.0/item/pointaccount` | Set Item Point Account Note: This request can participate in a transaction. Learn more about transactions. |

---
### GetItems

> Returns price, volume, and description for one or more item codes.

| | |
|---|---|
| Category | Items |
| REST | `GET /3.0/item?currencyCode=usd` |
| SOAP action | `https://api.exigo.com/GetItems` |
| WSDL elements | `GetItemsRequest` → `GetItemsResult` |
| CSV output | Yes — `GET https://api.exigo.com/3.0/csv/?method=GetItems&ApiLoginName=…&ApiPassword=…&ApiCompany=…` |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetItems |

#### Input

**`GetItemsRequest`**

| Property | Type | Notes |
|---|---|---|
| `CurrencyCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| `PriceType` | `Int32` | Controls which price band to use.<br>**Lookup:** company-specific list (see company-lists.md) |
| `WarehouseID` | `Int32` | Unique location for orders.<br>**Lookup:** company-specific list (see company-lists.md) |
| `ItemCodes` | `String[]` | Array of item codes.<br>**Lookup:** company-specific list (see company-lists.md) |
| `WebID` | `Int32` | Optional. Optionally use categories from content engine.<br>**Lookup:** company-specific list (see company-lists.md) |
| `WebCategoryID` | `Int32` | Optional. Optionally use categories from content engine.<br>**Lookup:** company-specific list (see company-lists.md) |
| `ReturnLongDetail` | `Boolean` |  |
| `RestrictToWarehouse` | `Boolean` | Optional. Determines if the items returned must be available in the provided WarehouseID (Default: false). |
| `LanguageID` | `Int32` | Optional. Customize the web experience by setting this.<br>**Lookup:** company-specific list (see company-lists.md) |
| `ExcludeHideFromSearch` | `Boolean` | Optional. Will exclude Hide from Search items. (defaults to false). |

#### Output

**`GetItemsResponse`**

| Property | Type | Notes |
|---|---|---|
| `Items` | `ItemResponse[]` |  |

**`ItemResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `ItemCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Description` | `String` |  |
| &nbsp;&nbsp;↳ `Price` | `Decimal` | Price amount. |
| &nbsp;&nbsp;↳ `Weight` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CommissionableVolume` | `Decimal` |  |
| &nbsp;&nbsp;↳ `BusinessVolume` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other1Price` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other2Price` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other3Price` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other4Price` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other5Price` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other6Price` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other7Price` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other8Price` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other9Price` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Other10Price` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Category` | `String` |  |
| &nbsp;&nbsp;↳ `CategoryID` | `Int32` |  |
| &nbsp;&nbsp;↳ `TinyPicture` | `String` |  |
| &nbsp;&nbsp;↳ `SmallPicture` | `String` |  |
| &nbsp;&nbsp;↳ `LargePicture` | `String` |  |
| &nbsp;&nbsp;↳ `ShortDetail` | `String` |  |
| &nbsp;&nbsp;↳ `ShortDetail2` | `String` |  |
| &nbsp;&nbsp;↳ `ShortDetail3` | `String` |  |
| &nbsp;&nbsp;↳ `ShortDetail4` | `String` |  |
| &nbsp;&nbsp;↳ `LongDetail` | `String` |  |
| &nbsp;&nbsp;↳ `LongDetail2` | `String` |  |
| &nbsp;&nbsp;↳ `LongDetail3` | `String` |  |
| &nbsp;&nbsp;↳ `LongDetail4` | `String` |  |
| &nbsp;&nbsp;↳ `InventoryStatus` | `InventoryStatusType` | **Values:** `Available`, `OnBackOrder`, `OutOfStock`, `Discontinued` |
| &nbsp;&nbsp;↳ `StockLevel` | `Int32` |  |
| &nbsp;&nbsp;↳ `AvailableStockLevel` | `Int32` |  |
| &nbsp;&nbsp;↳ `MaxAllowedOnOrder` | `Int32` |  |
| &nbsp;&nbsp;↳ `Field1` | `String` |  |
| &nbsp;&nbsp;↳ `Field2` | `String` |  |
| &nbsp;&nbsp;↳ `Field3` | `String` |  |
| &nbsp;&nbsp;↳ `Field4` | `String` |  |
| &nbsp;&nbsp;↳ `Field5` | `String` |  |
| &nbsp;&nbsp;↳ `Field6` | `String` |  |
| &nbsp;&nbsp;↳ `Field7` | `String` |  |
| &nbsp;&nbsp;↳ `Field8` | `String` |  |
| &nbsp;&nbsp;↳ `Field9` | `String` |  |
| &nbsp;&nbsp;↳ `Field10` | `String` |  |
| &nbsp;&nbsp;↳ `OtherCheck1` | `Boolean` |  |
| &nbsp;&nbsp;↳ `OtherCheck2` | `Boolean` |  |
| &nbsp;&nbsp;↳ `OtherCheck3` | `Boolean` |  |
| &nbsp;&nbsp;↳ `OtherCheck4` | `Boolean` |  |
| &nbsp;&nbsp;↳ `OtherCheck5` | `Boolean` |  |
| &nbsp;&nbsp;↳ `IsVirtual` | `Boolean` |  |
| &nbsp;&nbsp;↳ `AllowOnAutoOrder` | `Boolean` |  |
| &nbsp;&nbsp;↳ `IsGroupMaster` | `Boolean` |  |
| &nbsp;&nbsp;↳ `GroupDescription` | `String` |  |
| &nbsp;&nbsp;↳ `GroupMembersDescription` | `String` |  |
| &nbsp;&nbsp;↳ `GroupMembers` | `ItemMemberResponse[]` |  |
| &nbsp;&nbsp;↳ `IsDynamicKitMaster` | `Boolean` |  |
| &nbsp;&nbsp;↳ `HideFromSearch` | `Boolean` |  |
| &nbsp;&nbsp;↳ `KitMembers` | `KitMemberResponse[]` |  |
| &nbsp;&nbsp;↳ `TaxablePrice` | `Decimal` |  |
| &nbsp;&nbsp;↳ `ShippingPrice` | `Decimal` |  |

**`ItemMemberResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `ItemCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `MemberDescription` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `ItemDescription` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `InventoryStatus` | `InventoryStatusType` | **Values:** `Available`, `OnBackOrder`, `OutOfStock`, `Discontinued` |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `StockLevel` | `Int32` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `AvailableStockLevel` | `Int32` |  |

**`KitMemberResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Description` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `KitMemberItems` | `KitMemberItemResponse[]` |  |

**`KitMemberItemResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ `ItemCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ `Description` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↳ `InventoryStatus` | `InventoryStatusType` | **Values:** `Available`, `OnBackOrder`, `OutOfStock`, `Discontinued` |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/item?currencyCode=usd
  &priceType=1
  &warehouseID=1
  &itemCodes=1
  &returnLongDetail=1
  &restrictToWarehouse=1
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
SOAPAction: "https://api.exigo.com/GetItems"

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
    <GetItemsRequest xmlns="http://api.exigo.com/">
      <CurrencyCode>string</CurrencyCode>
      <PriceType>int</PriceType>
      <WarehouseID>int</WarehouseID>
      <ItemCodes>
        <string>string</string>
      </ItemCodes>
      <WebID>int</WebID>
      <WebCategoryID>int</WebCategoryID>
      <ReturnLongDetail>boolean</ReturnLongDetail>
      <RestrictToWarehouse>boolean</RestrictToWarehouse>
      <LanguageID>int</LanguageID>
      <ExcludeHideFromSearch>boolean</ExcludeHideFromSearch>
    </GetItemsRequest>
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
    <GetItemsResult xmlns="http://api.exigo.com/">
      <Items>
        <ItemResponse>
          <ItemCode>string</ItemCode>
          <Description>string</Description>
          <Price>decimal</Price>
          <Weight>decimal</Weight>
          <CommissionableVolume>decimal</CommissionableVolume>
          <BusinessVolume>decimal</BusinessVolume>
          <Other1Price>decimal</Other1Price>
          <Other2Price>decimal</Other2Price>
          <Other3Price>decimal</Other3Price>
          <Other4Price>decimal</Other4Price>
          <Other5Price>decimal</Other5Price>
          <Other6Price>decimal</Other6Price>
          <Other7Price>decimal</Other7Price>
          <Other8Price>decimal</Other8Price>
          <Other9Price>decimal</Other9Price>
          <Other10Price>decimal</Other10Price>
          <Category>string</Category>
          <CategoryID>int</CategoryID>
          <TinyPicture>string</TinyPicture>
          <SmallPicture>string</SmallPicture>
          <LargePicture>string</LargePicture>
          <ShortDetail>string</ShortDetail>
          <ShortDetail2>string</ShortDetail2>
          <ShortDetail3>string</ShortDetail3>
          <ShortDetail4>string</ShortDetail4>
          <LongDetail>string</LongDetail>
          <LongDetail2>string</LongDetail2>
          <LongDetail3>string</LongDetail3>
          <LongDetail4>string</LongDetail4>
          <InventoryStatus>Available or OnBackOrder or OutOfStock or Discontinued</InventoryStatus>
          <StockLevel>int</StockLevel>
          <AvailableStockLevel>int</AvailableStockLevel>
          <MaxAllowedOnOrder>int</MaxAllowedOnOrder>
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
          <OtherCheck1>boolean</OtherCheck1>
          <OtherCheck2>boolean</OtherCheck2>
          <OtherCheck3>boolean</OtherCheck3>
          <OtherCheck4>boolean</OtherCheck4>
          <OtherCheck5>boolean</OtherCheck5>
          <IsVirtual>boolean</IsVirtual>
          <AllowOnAutoOrder>boolean</AllowOnAutoOrder>
          <IsGroupMaster>boolean</IsGroupMaster>
          <GroupDescription>string</GroupDescription>
          <GroupMembersDescription>string</GroupMembersDescription>
          <GroupMembers>
            <ItemMemberResponse>
              <ItemCode>string</ItemCode>
              <MemberDescription>string</MemberDescription>
              <ItemDescription>string</ItemDescription>
              <InventoryStatus>Available or OnBackOrder or OutOfStock or Discontinued</InventoryStatus>
              <StockLevel>int</StockLevel>
              <AvailableStockLevel>int</AvailableStockLevel>
            </ItemMemberResponse>
          </GroupMembers>
          <IsDynamicKitMaster>boolean</IsDynamicKitMaster>
          <HideFromSearch>boolean</HideFromSearch>
          <KitMembers>
            <KitMemberResponse>
              <Description>string</Description>
              <KitMemberItems
                xsi:nil="true" />
            </KitMemberResponse>
          </KitMembers>
          <TaxablePrice>decimal</TaxablePrice>
          <ShippingPrice>decimal</ShippingPrice>
        </ItemResponse>
      </Items>
    </GetItemsResult>
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
    var req = new GetItemsRequest();

    req.CurrencyCode = "usd";
    req.PriceType = 1;              //Controls which price band to use
    req.WarehouseID = 1;            //Unique location for orders

    //Add ItemCodes
    var itemcodes = new List<String>();
    itemcodes.Add("1");
    itemcodes.Add("2");

    //Now attach the list to the request
    req.ItemCodes = itemcodes.ToArray();
    req.ReturnLongDetail = true;
    req.RestrictToWarehouse = true;    //Determines if the items returned must be available in the provided WarehouseID (Default: false)

    //Send Request to Server and Get Response
    var res = await api.GetItemsAsync(req);

    //Now examine the results:

    foreach (var item  in res.Items)
    {
        Console.WriteLine("ItemCode: {0}", item.ItemCode);
        Console.WriteLine("Description: {0}", item.Description);
        Console.WriteLine("Price: {0}", item.Price);
        Console.WriteLine("Weight: {0}", item.Weight);
        Console.WriteLine("StockLevel: {0}", item.StockLevel);
        Console.WriteLine("AvailableStockLevel: {0}", item.AvailableStockLevel);
        Console.WriteLine("IsDynamicKitMaster: {0}", item.IsDynamicKitMaster);

        foreach (var kitMember  in item.KitMembers)
        {
            Console.WriteLine("Description: {0}", kitMember.Description);

            foreach (var kitMemberItem  in kitMember.KitMemberItems)
            {
                Console.WriteLine("ItemCode: {0}", kitMemberItem.ItemCode);
                Console.WriteLine("Description: {0}", kitMemberItem.Description);
                Console.WriteLine("InventoryStatus: {0}", kitMemberItem.InventoryStatus);
            }
        }
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
    GetItemsRequest req = new GetItemsRequest();

    req.CurrencyCode = "usd";
    req.PriceType = 1;              //Controls which price band to use
    req.WarehouseID = 1;            //Unique location for orders

    //Add ItemCodes
    List<String> itemcodes = new List<String>();
    itemcodes.Add("1");
    itemcodes.Add("2");

    //Now attach the list to the request
    req.ItemCodes = itemcodes.ToArray();
    req.ReturnLongDetail = true;
    req.RestrictToWarehouse = true;    //Determines if the items returned must be available in the provided WarehouseID (Default: false)

    //Send Request to Server and Get Response
    GetItemsResponse res = api.GetItems(req);

    //Now examine the results:

    foreach (ItemResponse item  in res.Items)
    {
        Console.WriteLine("ItemCode: {0}", item.ItemCode);
        Console.WriteLine("Description: {0}", item.Description);
        Console.WriteLine("Price: {0}", item.Price);
        Console.WriteLine("Weight: {0}", item.Weight);
        Console.WriteLine("StockLevel: {0}", item.StockLevel);
        Console.WriteLine("AvailableStockLevel: {0}", item.AvailableStockLevel);
        Console.WriteLine("IsDynamicKitMaster: {0}", item.IsDynamicKitMaster);

        foreach (KitMemberResponse kitMember  in item.KitMembers)
        {
            Console.WriteLine("Description: {0}", kitMember.Description);

            foreach (KitMemberItemResponse kitMemberItem  in kitMember.KitMemberItems)
            {
                Console.WriteLine("ItemCode: {0}", kitMemberItem.ItemCode);
                Console.WriteLine("Description: {0}", kitMemberItem.Description);
                Console.WriteLine("InventoryStatus: {0}", kitMemberItem.InventoryStatus);
            }
        }
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
    Dim req as new GetItemsRequest()

    req.CurrencyCode = "usd"
    req.PriceType = 1
    req.WarehouseID = 1

    'Add ItemCodes
    Dim itemcodes As New List(Of String)()
    itemcodes.Add("1")
    itemcodes.Add("2")

    'Now attach the list to the request
    req.ItemCodes = itemcodes.ToArray()
    req.ReturnLongDetail = true
    req.RestrictToWarehouse = true

    'Send Request to Server and Get Response
    Dim res As GetItemsResponse = api.GetItems(req)

    'Now examine the results:

    For Each item As ItemResponse In res.Items
        Console.WriteLine("ItemCode: {0}", item.ItemCode)
        Console.WriteLine("Description: {0}", item.Description)
        Console.WriteLine("Price: {0}", item.Price)
        Console.WriteLine("Weight: {0}", item.Weight)
        Console.WriteLine("StockLevel: {0}", item.StockLevel)
        Console.WriteLine("AvailableStockLevel: {0}", item.AvailableStockLevel)
        Console.WriteLine("IsDynamicKitMaster: {0}", item.IsDynamicKitMaster)

        For Each kitMember As KitMemberResponse In item.KitMembers
            Console.WriteLine("Description: {0}", kitMember.Description)

            For Each kitMemberItem As KitMemberItemResponse In kitMember.KitMemberItems
                Console.WriteLine("ItemCode: {0}", kitMemberItem.ItemCode)
                Console.WriteLine("Description: {0}", kitMemberItem.Description)
                Console.WriteLine("InventoryStatus: {0}", kitMemberItem.InventoryStatus)
            Next
        Next
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

    $req->CurrencyCode = "usd";
    $req->PriceType = 1;
    $req->WarehouseID = 1;

    //Add ItemCodes

    $itemCode1->Chars = 1;
    $itemCode1->Length = 1;

    $itemCode2->Chars = 2;
    $itemCode2->Length = 2;

    //Now attach the list to the request
    req.ItemCodes = array(itemCode1,itemCode2);
    $req->ReturnLongDetail = 1;
    $req->RestrictToWarehouse = 1;

    //Send Request to Server and Get Response
    $res = $api.GetItems($req);

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
    GetItemsRequest req = new GetItemsRequest();

    req.setCurrencyCode("usd");
    req.setPriceType(1);
    req.setWarehouseID(1);

    //Add ItemCodes
    ArrayOfSystem.String itemcodes = new ArrayOfSystem.String();

    String itemCode1 = new String();
    itemCode1.setChars(1);
    itemCode1.setLength(1);
    itemcodes.Add(itemCode1);

    String itemCode2 = new String();
    itemCode2.setChars(2);
    itemCode2.setLength(2);
    itemcodes.Add(itemCode2);

    //Now attach the list to the request
    req.setItemCodes(itemcodes);
    req.setReturnLongDetail(1);
    req.setRestrictToWarehouse(1);

    //Send Request to Server and Get Response
    GetItemsResponse res = api.getExigoApiSoap().getItems(req, auth);

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
https://api.exigo.com/3.0/csv/?method=GetItems
&ApiLoginName=String
&ApiPassword=String
&ApiCompany=String
&CurrencyCode=String
&PriceType=Int32
&WarehouseID=Int32
&ItemCodes=String[]
&WebID=Object
&WebCategoryID=Object
&ReturnLongDetail=Boolean
&RestrictToWarehouse=Nullable`1
&LanguageID=Object
&ExcludeHideFromSearch=Nullable`1
Response FieldsItemCode,Description,Price,Weight,CommissionableVolume,BusinessVolume,Other1Price,Other2Price,Other3Price,Other4Price,Other5Price,Other6Price,Other7Price,Other8Price,Other9Price,Other10Price,Category,CategoryID,TinyPicture,SmallPicture,LargePicture,ShortDetail,ShortDetail2,ShortDetail3,ShortDetail4,LongDetail,LongDetail2,LongDetail3,LongDetail4,InventoryStatus,StockLevel,AvailableStockLevel,MaxAllowedOnOrder,Field1,Field2,Field3,Field4,Field5,Field6,Field7,Field8,Field9,Field10,OtherCheck1,OtherCheck2,OtherCheck3,OtherCheck4,OtherCheck5,IsVirtual,AllowOnAutoOrder,IsGroupMaster,GroupDescription,GroupMembersDescription,ItemCode,MemberDescription,ItemDescription,InventoryStatus,StockLevel,AvailableStockLevel,IsDynamicKitMaster,HideFromSearch,Description,ItemCode,Description,InventoryStatus,TaxablePrice,ShippingPrice
String,String,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,String,Int32,String,String,String,String,String,String,String,String,String,String,String,InventoryStatusType,Int32,Int32,Int32,String,String,String,String,String,String,String,String,String,String,Boolean,Boolean,Boolean,Boolean,Boolean,Boolean,Boolean,Boolean,String,String,String,String,String,InventoryStatusType,Int32,Int32,Boolean,Boolean,String,String,String,InventoryStatusType,Decimal,Decimal

                    © 2026 Exigo.
```

</details>

---

### CreateItem

>  Adds an Item (and optional warehouse/price info)
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Items |
| REST | `POST /3.0/item` |
| SOAP action | `https://api.exigo.com/CreateItem` |
| WSDL elements | `CreateItemRequest` → `CreateItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateItem |

#### Input

**`CreateItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `ItemCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| `Description` | `String` | Optional. |
| `Weight` | `Decimal` |  |
| `Notes` | `String` | Optional. |
| `AvailableInAllCountryRegions` | `Boolean` |  |
| `TaxedInAllCountryRegions` | `Boolean` |  |
| `AvailableInAllWarehouses` | `Boolean` |  |
| `IsVirtual` | `Boolean` |  |
| `ItemTypeID` | `Int32` |  |
| `IsSubscriptionUpdate` | `Boolean` |  |
| `IsPointIncrement` | `Boolean` |  |
| `OtherCheck1` | `Boolean` |  |
| `OtherCheck2` | `Boolean` |  |
| `OtherCheck3` | `Boolean` |  |
| `OtherCheck4` | `Boolean` |  |
| `OtherCheck5` | `Boolean` |  |
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
| `HideFromSearch` | `Boolean` |  |
| `IsGroupMaster` | `Boolean` |  |
| `SuppressGroupMaster` | `Boolean` |  |

#### Output

**`CreateItemResponse`**

| Property | Type | Notes |
|---|---|---|
| `ItemID` | `Int32` | Newly created unique identifier for an item record. |
| `ItemCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/item HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "itemCode": "1",
  "description": "",
  "weight": null,
  "notes": "",
  "availableInAllCountryRegions": true,
  "taxedInAllCountryRegions": true,
  "availableInAllWarehouses": true,
  "isVirtual": true,
  "itemTypeID": 1,
  "isSubscriptionUpdate": true,
  "isPointIncrement": true,
  "otherCheck1": true,
  "otherCheck2": true,
  "otherCheck3": true,
  "otherCheck4": true,
  "otherCheck5": true,
  "field1": "1",
  "field2": "1",
  "field3": "1",
  "field4": "1",
  "field5": "1",
  "field6": "1",
  "field7": "1",
  "field8": "1",
  "field9": "1",
  "field10": "1",
  "hideFromSearch": true,
  "isGroupMaster": true,
  "suppressGroupMaster": true
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "itemID": 1,
  "itemCode": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateItem"

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
    <CreateItemRequest xmlns="http://api.exigo.com/">
      <ItemCode>string</ItemCode>
      <Description>string</Description>
      <Weight>decimal</Weight>
      <Notes>string</Notes>
      <AvailableInAllCountryRegions>boolean</AvailableInAllCountryRegions>
      <TaxedInAllCountryRegions>boolean</TaxedInAllCountryRegions>
      <AvailableInAllWarehouses>boolean</AvailableInAllWarehouses>
      <IsVirtual>boolean</IsVirtual>
      <ItemTypeID>int</ItemTypeID>
      <IsSubscriptionUpdate>boolean</IsSubscriptionUpdate>
      <IsPointIncrement>boolean</IsPointIncrement>
      <OtherCheck1>boolean</OtherCheck1>
      <OtherCheck2>boolean</OtherCheck2>
      <OtherCheck3>boolean</OtherCheck3>
      <OtherCheck4>boolean</OtherCheck4>
      <OtherCheck5>boolean</OtherCheck5>
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
      <HideFromSearch>boolean</HideFromSearch>
      <IsGroupMaster>boolean</IsGroupMaster>
      <SuppressGroupMaster>boolean</SuppressGroupMaster>
    </CreateItemRequest>
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
    <CreateItemResult xmlns="http://api.exigo.com/">
      <ItemID>int</ItemID>
      <ItemCode>string</ItemCode>
    </CreateItemResult>
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
    var req = new CreateItemRequest();

    req.ItemCode = "1";
    req.Description = "1";
    req.Weight = 1;
    req.Notes = "1";
    req.AvailableInAllCountryRegions = true;
    req.TaxedInAllCountryRegions = true;
    req.AvailableInAllWarehouses = true;
    req.IsVirtual = true;
    req.ItemTypeID = 1;
    req.IsSubscriptionUpdate = true;
    req.IsPointIncrement = true;
    req.OtherCheck1 = true;
    req.OtherCheck2 = true;
    req.OtherCheck3 = true;
    req.OtherCheck4 = true;
    req.OtherCheck5 = true;
    req.Field1 = "1";
    req.Field2 = "1";
    req.Field3 = "1";
    req.Field4 = "1";
    req.Field5 = "1";
    req.Field6 = "1";
    req.Field7 = "1";
    req.Field8 = "1";
    req.Field9 = "1";
    req.Field10 = "1";
    req.HideFromSearch = true;
    req.IsGroupMaster = true;
    req.SuppressGroupMaster = true;

    //Send Request to Server and Get Response
    var res = await api.CreateItemAsync(req);

    //Now examine the results:
    Console.WriteLine("ItemID: {0}", res.ItemID);
    Console.WriteLine("ItemCode: {0}", res.ItemCode);
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
    CreateItemRequest req = new CreateItemRequest();

    req.ItemCode = "1";
    req.Description = "1";
    req.Weight = 1;
    req.Notes = "1";
    req.AvailableInAllCountryRegions = true;
    req.TaxedInAllCountryRegions = true;
    req.AvailableInAllWarehouses = true;
    req.IsVirtual = true;
    req.ItemTypeID = 1;
    req.IsSubscriptionUpdate = true;
    req.IsPointIncrement = true;
    req.OtherCheck1 = true;
    req.OtherCheck2 = true;
    req.OtherCheck3 = true;
    req.OtherCheck4 = true;
    req.OtherCheck5 = true;
    req.Field1 = "1";
    req.Field2 = "1";
    req.Field3 = "1";
    req.Field4 = "1";
    req.Field5 = "1";
    req.Field6 = "1";
    req.Field7 = "1";
    req.Field8 = "1";
    req.Field9 = "1";
    req.Field10 = "1";
    req.HideFromSearch = true;
    req.IsGroupMaster = true;
    req.SuppressGroupMaster = true;

    //Send Request to Server and Get Response
    CreateItemResponse res = api.CreateItem(req);

    //Now examine the results:
    Console.WriteLine("ItemID: {0}", res.ItemID);
    Console.WriteLine("ItemCode: {0}", res.ItemCode);
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
    Dim req as new CreateItemRequest()

    req.ItemCode = "1"
    req.Description = "1"
    req.Weight = 1
    req.Notes = "1"
    req.AvailableInAllCountryRegions = true
    req.TaxedInAllCountryRegions = true
    req.AvailableInAllWarehouses = true
    req.IsVirtual = true
    req.ItemTypeID = 1
    req.IsSubscriptionUpdate = true
    req.IsPointIncrement = true
    req.OtherCheck1 = true
    req.OtherCheck2 = true
    req.OtherCheck3 = true
    req.OtherCheck4 = true
    req.OtherCheck5 = true
    req.Field1 = "1"
    req.Field2 = "1"
    req.Field3 = "1"
    req.Field4 = "1"
    req.Field5 = "1"
    req.Field6 = "1"
    req.Field7 = "1"
    req.Field8 = "1"
    req.Field9 = "1"
    req.Field10 = "1"
    req.HideFromSearch = true
    req.IsGroupMaster = true
    req.SuppressGroupMaster = true

    'Send Request to Server and Get Response
    Dim res As CreateItemResponse = api.CreateItem(req)

    'Now examine the results:
    Console.WriteLine("ItemID: {0}", res.ItemID)
    Console.WriteLine("ItemCode: {0}", res.ItemCode)
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
    $req->Description = "1";
    $req->Weight = 1;
    $req->Notes = "1";
    $req->AvailableInAllCountryRegions = 1;
    $req->TaxedInAllCountryRegions = 1;
    $req->AvailableInAllWarehouses = 1;
    $req->IsVirtual = 1;
    $req->ItemTypeID = 1;
    $req->IsSubscriptionUpdate = 1;
    $req->IsPointIncrement = 1;
    $req->OtherCheck1 = 1;
    $req->OtherCheck2 = 1;
    $req->OtherCheck3 = 1;
    $req->OtherCheck4 = 1;
    $req->OtherCheck5 = 1;
    $req->Field1 = "1";
    $req->Field2 = "1";
    $req->Field3 = "1";
    $req->Field4 = "1";
    $req->Field5 = "1";
    $req->Field6 = "1";
    $req->Field7 = "1";
    $req->Field8 = "1";
    $req->Field9 = "1";
    $req->Field10 = "1";
    $req->HideFromSearch = 1;
    $req->IsGroupMaster = 1;
    $req->SuppressGroupMaster = 1;

    //Send Request to Server and Get Response
    $res = $api.CreateItem($req);

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
    CreateItemRequest req = new CreateItemRequest();

    req.setItemCode("1");
    req.setDescription("1");
    req.setWeight(1);
    req.setNotes("1");
    req.setAvailableInAllCountryRegions(1);
    req.setTaxedInAllCountryRegions(1);
    req.setAvailableInAllWarehouses(1);
    req.setIsVirtual(1);
    req.setItemTypeID(1);
    req.setIsSubscriptionUpdate(1);
    req.setIsPointIncrement(1);
    req.setOtherCheck1(1);
    req.setOtherCheck2(1);
    req.setOtherCheck3(1);
    req.setOtherCheck4(1);
    req.setOtherCheck5(1);
    req.setField1("1");
    req.setField2("1");
    req.setField3("1");
    req.setField4("1");
    req.setField5("1");
    req.setField6("1");
    req.setField7("1");
    req.setField8("1");
    req.setField9("1");
    req.setField10("1");
    req.setHideFromSearch(1);
    req.setIsGroupMaster(1);
    req.setSuppressGroupMaster(1);

    //Send Request to Server and Get Response
    CreateItemResponse res = api.getExigoApiSoap().createItem(req, auth);

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

### UpdateItem

> Updates an Item (and optional warehouse/price info)
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Items |
| REST | `PUT /3.0/item` |
| SOAP action | `https://api.exigo.com/UpdateItem` |
| WSDL elements | `UpdateItemRequest` → `UpdateItemResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateItem |

#### Input

**`UpdateItemRequest`**

| Property | Type | Notes |
|---|---|---|
| `ItemCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| `Description` | `String` | Optional. |
| `Weight` | `Decimal` | Optional. |
| `Notes` | `String` | Optional. |
| `AvailableInAllCountryRegions` | `Boolean` | Optional. |
| `TaxedInAllCountryRegions` | `Boolean` | Optional. |
| `AvailableInAllWarehouses` | `Boolean` | Optional. |
| `IsVirtual` | `Boolean` | Optional. |
| `ItemTypeID` | `Int32` | Optional. |
| `ShortDetail` | `String` | Optional. |
| `ShortDetail2` | `String` | Optional. |
| `ShortDetail3` | `String` | Optional. |
| `ShortDetail4` | `String` | Optional. |
| `LongDetail` | `String` | Optional. |
| `LongDetail2` | `String` | Optional. |
| `LongDetail3` | `String` | Optional. |
| `LongDetail4` | `String` | Optional. |
| `OtherCheck1` | `Boolean` | Optional. |
| `OtherCheck2` | `Boolean` | Optional. |
| `OtherCheck3` | `Boolean` | Optional. |
| `OtherCheck4` | `Boolean` | Optional. |
| `OtherCheck5` | `Boolean` | Optional. |
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
| `HideFromSearch` | `Boolean` | Optional. |
| `IsSubscriptionUpdate` | `Boolean` | Optional. |
| `IsPointIncrement` | `Boolean` | Optional. |
| `IsGroupMaster` | `Boolean` | Optional. |
| `SuppressGroupMaster` | `Boolean` | Optional. |

#### Output

**`UpdateItemResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/item HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "itemCode": "1",
  "description": "",
  "weight": null,
  "notes": "",
  "availableInAllCountryRegions": true,
  "taxedInAllCountryRegions": true,
  "availableInAllWarehouses": true,
  "isVirtual": true,
  "itemTypeID": 1,
  "shortDetail": "",
  "shortDetail2": "",
  "shortDetail3": "",
  "shortDetail4": "",
  "longDetail": "",
  "longDetail2": "",
  "longDetail3": "",
  "longDetail4": "",
  "otherCheck1": true,
  "otherCheck2": true,
  "otherCheck3": true,
  "otherCheck4": true,
  "otherCheck5": true,
  "field1": "1",
  "field2": "1",
  "field3": "1",
  "field4": "1",
  "field5": "1",
  "field6": "1",
  "field7": "1",
  "field8": "1",
  "field9": "1",
  "field10": "1",
  "hideFromSearch": true,
  "isSubscriptionUpdate": true,
  "isPointIncrement": true,
  "isGroupMaster": true,
  "suppressGroupMaster": true
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
SOAPAction: "https://api.exigo.com/UpdateItem"

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
    <UpdateItemRequest xmlns="http://api.exigo.com/">
      <ItemCode>string</ItemCode>
      <Description>string</Description>
      <Weight>decimal</Weight>
      <Notes>string</Notes>
      <AvailableInAllCountryRegions>boolean</AvailableInAllCountryRegions>
      <TaxedInAllCountryRegions>boolean</TaxedInAllCountryRegions>
      <AvailableInAllWarehouses>boolean</AvailableInAllWarehouses>
      <IsVirtual>boolean</IsVirtual>
      <ItemTypeID>int</ItemTypeID>
      <ShortDetail>string</ShortDetail>
      <ShortDetail2>string</ShortDetail2>
      <ShortDetail3>string</ShortDetail3>
      <ShortDetail4>string</ShortDetail4>
      <LongDetail>string</LongDetail>
      <LongDetail2>string</LongDetail2>
      <LongDetail3>string</LongDetail3>
      <LongDetail4>string</LongDetail4>
      <OtherCheck1>boolean</OtherCheck1>
      <OtherCheck2>boolean</OtherCheck2>
      <OtherCheck3>boolean</OtherCheck3>
      <OtherCheck4>boolean</OtherCheck4>
      <OtherCheck5>boolean</OtherCheck5>
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
      <HideFromSearch>boolean</HideFromSearch>
      <IsSubscriptionUpdate>boolean</IsSubscriptionUpdate>
      <IsPointIncrement>boolean</IsPointIncrement>
      <IsGroupMaster>boolean</IsGroupMaster>
      <SuppressGroupMaster>boolean</SuppressGroupMaster>
    </UpdateItemRequest>
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
    <UpdateItemResult xmlns="http://api.exigo.com/" />
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
    var req = new UpdateItemRequest();

    req.ItemCode = "1";
    req.Description = "1";
    req.Weight = 1;
    req.Notes = "1";
    req.AvailableInAllCountryRegions = true;
    req.TaxedInAllCountryRegions = true;
    req.AvailableInAllWarehouses = true;
    req.IsVirtual = true;
    req.ItemTypeID = 1;
    req.ShortDetail = "1";
    req.ShortDetail2 = "1";
    req.ShortDetail3 = "1";
    req.ShortDetail4 = "1";
    req.LongDetail = "1";
    req.LongDetail2 = "1";
    req.LongDetail3 = "1";
    req.LongDetail4 = "1";
    req.OtherCheck1 = true;
    req.OtherCheck2 = true;
    req.OtherCheck3 = true;
    req.OtherCheck4 = true;
    req.OtherCheck5 = true;
    req.Field1 = "1";
    req.Field2 = "1";
    req.Field3 = "1";
    req.Field4 = "1";
    req.Field5 = "1";
    req.Field6 = "1";
    req.Field7 = "1";
    req.Field8 = "1";
    req.Field9 = "1";
    req.Field10 = "1";
    req.HideFromSearch = true;
    req.IsSubscriptionUpdate = true;
    req.IsPointIncrement = true;
    req.IsGroupMaster = true;
    req.SuppressGroupMaster = true;

    //Send Request to Server and Get Response
    var res = await api.UpdateItemAsync(req);

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
    UpdateItemRequest req = new UpdateItemRequest();

    req.ItemCode = "1";
    req.Description = "1";
    req.Weight = 1;
    req.Notes = "1";
    req.AvailableInAllCountryRegions = true;
    req.TaxedInAllCountryRegions = true;
    req.AvailableInAllWarehouses = true;
    req.IsVirtual = true;
    req.ItemTypeID = 1;
    req.ShortDetail = "1";
    req.ShortDetail2 = "1";
    req.ShortDetail3 = "1";
    req.ShortDetail4 = "1";
    req.LongDetail = "1";
    req.LongDetail2 = "1";
    req.LongDetail3 = "1";
    req.LongDetail4 = "1";
    req.OtherCheck1 = true;
    req.OtherCheck2 = true;
    req.OtherCheck3 = true;
    req.OtherCheck4 = true;
    req.OtherCheck5 = true;
    req.Field1 = "1";
    req.Field2 = "1";
    req.Field3 = "1";
    req.Field4 = "1";
    req.Field5 = "1";
    req.Field6 = "1";
    req.Field7 = "1";
    req.Field8 = "1";
    req.Field9 = "1";
    req.Field10 = "1";
    req.HideFromSearch = true;
    req.IsSubscriptionUpdate = true;
    req.IsPointIncrement = true;
    req.IsGroupMaster = true;
    req.SuppressGroupMaster = true;

    //Send Request to Server and Get Response
    UpdateItemResponse res = api.UpdateItem(req);

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
    Dim req as new UpdateItemRequest()

    req.ItemCode = "1"
    req.Description = "1"
    req.Weight = 1
    req.Notes = "1"
    req.AvailableInAllCountryRegions = true
    req.TaxedInAllCountryRegions = true
    req.AvailableInAllWarehouses = true
    req.IsVirtual = true
    req.ItemTypeID = 1
    req.ShortDetail = "1"
    req.ShortDetail2 = "1"
    req.ShortDetail3 = "1"
    req.ShortDetail4 = "1"
    req.LongDetail = "1"
    req.LongDetail2 = "1"
    req.LongDetail3 = "1"
    req.LongDetail4 = "1"
    req.OtherCheck1 = true
    req.OtherCheck2 = true
    req.OtherCheck3 = true
    req.OtherCheck4 = true
    req.OtherCheck5 = true
    req.Field1 = "1"
    req.Field2 = "1"
    req.Field3 = "1"
    req.Field4 = "1"
    req.Field5 = "1"
    req.Field6 = "1"
    req.Field7 = "1"
    req.Field8 = "1"
    req.Field9 = "1"
    req.Field10 = "1"
    req.HideFromSearch = true
    req.IsSubscriptionUpdate = true
    req.IsPointIncrement = true
    req.IsGroupMaster = true
    req.SuppressGroupMaster = true

    'Send Request to Server and Get Response
    Dim res As UpdateItemResponse = api.UpdateItem(req)

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

    $req->ItemCode = "1";
    $req->Description = "1";
    $req->Weight = 1;
    $req->Notes = "1";
    $req->AvailableInAllCountryRegions = 1;
    $req->TaxedInAllCountryRegions = 1;
    $req->AvailableInAllWarehouses = 1;
    $req->IsVirtual = 1;
    $req->ItemTypeID = 1;
    $req->ShortDetail = "1";
    $req->ShortDetail2 = "1";
    $req->ShortDetail3 = "1";
    $req->ShortDetail4 = "1";
    $req->LongDetail = "1";
    $req->LongDetail2 = "1";
    $req->LongDetail3 = "1";
    $req->LongDetail4 = "1";
    $req->OtherCheck1 = 1;
    $req->OtherCheck2 = 1;
    $req->OtherCheck3 = 1;
    $req->OtherCheck4 = 1;
    $req->OtherCheck5 = 1;
    $req->Field1 = "1";
    $req->Field2 = "1";
    $req->Field3 = "1";
    $req->Field4 = "1";
    $req->Field5 = "1";
    $req->Field6 = "1";
    $req->Field7 = "1";
    $req->Field8 = "1";
    $req->Field9 = "1";
    $req->Field10 = "1";
    $req->HideFromSearch = 1;
    $req->IsSubscriptionUpdate = 1;
    $req->IsPointIncrement = 1;
    $req->IsGroupMaster = 1;
    $req->SuppressGroupMaster = 1;

    //Send Request to Server and Get Response
    $res = $api.UpdateItem($req);

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
    UpdateItemRequest req = new UpdateItemRequest();

    req.setItemCode("1");
    req.setDescription("1");
    req.setWeight(1);
    req.setNotes("1");
    req.setAvailableInAllCountryRegions(1);
    req.setTaxedInAllCountryRegions(1);
    req.setAvailableInAllWarehouses(1);
    req.setIsVirtual(1);
    req.setItemTypeID(1);
    req.setShortDetail("1");
    req.setShortDetail2("1");
    req.setShortDetail3("1");
    req.setShortDetail4("1");
    req.setLongDetail("1");
    req.setLongDetail2("1");
    req.setLongDetail3("1");
    req.setLongDetail4("1");
    req.setOtherCheck1(1);
    req.setOtherCheck2(1);
    req.setOtherCheck3(1);
    req.setOtherCheck4(1);
    req.setOtherCheck5(1);
    req.setField1("1");
    req.setField2("1");
    req.setField3("1");
    req.setField4("1");
    req.setField5("1");
    req.setField6("1");
    req.setField7("1");
    req.setField8("1");
    req.setField9("1");
    req.setField10("1");
    req.setHideFromSearch(1);
    req.setIsSubscriptionUpdate(1);
    req.setIsPointIncrement(1);
    req.setIsGroupMaster(1);
    req.setSuppressGroupMaster(1);

    //Send Request to Server and Get Response
    UpdateItemResponse res = api.getExigoApiSoap().updateItem(req, auth);

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

### SetItemPrice

> Sets pricing info for an item)
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Items |
| REST | `PUT /3.0/item/price` |
| SOAP action | `https://api.exigo.com/SetItemPrice` |
| WSDL elements | `SetItemPriceRequest` → `SetItemPriceResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=SetItemPrice |

#### Input

**`SetItemPriceRequest`**

| Property | Type | Notes |
|---|---|---|
| `ItemCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| `CurrencyCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| `PriceType` | `Int32` | Controls which price band to use.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Price` | `Decimal` | Optional. Price amount. |
| `BusinessVolume` | `Decimal` | Optional. Price amount. |
| `CommissionableVolume` | `Decimal` | Optional. Price amount. |
| `TaxablePrice` | `Decimal` | Optional. Price amount. |
| `ShippingPrice` | `Decimal` | Optional. Price amount. |
| `Other1Price` | `Decimal` | Optional. Price amount. |
| `Other2Price` | `Decimal` | Optional. Price amount. |
| `Other3Price` | `Decimal` | Optional. Price amount. |
| `Other4Price` | `Decimal` | Optional. Price amount. |
| `Other5Price` | `Decimal` | Optional. Price amount. |
| `Other6Price` | `Decimal` | Optional. Price amount. |
| `Other7Price` | `Decimal` | Optional. Price amount. |
| `Other8Price` | `Decimal` | Optional. Price amount. |
| `Other9Price` | `Decimal` | Optional. Price amount. |
| `Other10Price` | `Decimal` | Optional. Price amount. |

#### Output

**`SetItemPriceResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/item/price HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "itemCode": "1",
  "currencyCode": "usd",
  "priceType": 1,
  "price": null,
  "businessVolume": null,
  "commissionableVolume": null,
  "taxablePrice": null,
  "shippingPrice": null,
  "other1Price": null,
  "other2Price": null,
  "other3Price": null,
  "other4Price": null,
  "other5Price": null,
  "other6Price": null,
  "other7Price": null,
  "other8Price": null,
  "other9Price": null,
  "other10Price": null
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
SOAPAction: "https://api.exigo.com/SetItemPrice"

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
    <SetItemPriceRequest xmlns="http://api.exigo.com/">
      <ItemCode>string</ItemCode>
      <CurrencyCode>string</CurrencyCode>
      <PriceType>int</PriceType>
      <Price>decimal</Price>
      <BusinessVolume>decimal</BusinessVolume>
      <CommissionableVolume>decimal</CommissionableVolume>
      <TaxablePrice>decimal</TaxablePrice>
      <ShippingPrice>decimal</ShippingPrice>
      <Other1Price>decimal</Other1Price>
      <Other2Price>decimal</Other2Price>
      <Other3Price>decimal</Other3Price>
      <Other4Price>decimal</Other4Price>
      <Other5Price>decimal</Other5Price>
      <Other6Price>decimal</Other6Price>
      <Other7Price>decimal</Other7Price>
      <Other8Price>decimal</Other8Price>
      <Other9Price>decimal</Other9Price>
      <Other10Price>decimal</Other10Price>
    </SetItemPriceRequest>
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
    <SetItemPriceResult xmlns="http://api.exigo.com/" />
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
    var req = new SetItemPriceRequest();

    req.ItemCode = "1";
    req.CurrencyCode = "usd";
    req.PriceType = 1;              //Controls which price band to use
    req.Price = 1;                  //Price amount
    req.BusinessVolume = 1;         //Price amount
    req.CommissionableVolume = 1;   //Price amount
    req.TaxablePrice = 1;           //Price amount
    req.ShippingPrice = 1;          //Price amount
    req.Other1Price = 1;            //Price amount
    req.Other2Price = 1;            //Price amount
    req.Other3Price = 1;            //Price amount
    req.Other4Price = 1;            //Price amount
    req.Other5Price = 1;            //Price amount
    req.Other6Price = 1;            //Price amount
    req.Other7Price = 1;            //Price amount
    req.Other8Price = 1;            //Price amount
    req.Other9Price = 1;            //Price amount
    req.Other10Price = 1;           //Price amount

    //Send Request to Server and Get Response
    var res = await api.SetItemPriceAsync(req);

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
    SetItemPriceRequest req = new SetItemPriceRequest();

    req.ItemCode = "1";
    req.CurrencyCode = "usd";
    req.PriceType = 1;              //Controls which price band to use
    req.Price = 1;                  //Price amount
    req.BusinessVolume = 1;         //Price amount
    req.CommissionableVolume = 1;   //Price amount
    req.TaxablePrice = 1;           //Price amount
    req.ShippingPrice = 1;          //Price amount
    req.Other1Price = 1;            //Price amount
    req.Other2Price = 1;            //Price amount
    req.Other3Price = 1;            //Price amount
    req.Other4Price = 1;            //Price amount
    req.Other5Price = 1;            //Price amount
    req.Other6Price = 1;            //Price amount
    req.Other7Price = 1;            //Price amount
    req.Other8Price = 1;            //Price amount
    req.Other9Price = 1;            //Price amount
    req.Other10Price = 1;           //Price amount

    //Send Request to Server and Get Response
    SetItemPriceResponse res = api.SetItemPrice(req);

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
    Dim req as new SetItemPriceRequest()

    req.ItemCode = "1"
    req.CurrencyCode = "usd"
    req.PriceType = 1
    req.Price = 1
    req.BusinessVolume = 1
    req.CommissionableVolume = 1
    req.TaxablePrice = 1
    req.ShippingPrice = 1
    req.Other1Price = 1
    req.Other2Price = 1
    req.Other3Price = 1
    req.Other4Price = 1
    req.Other5Price = 1
    req.Other6Price = 1
    req.Other7Price = 1
    req.Other8Price = 1
    req.Other9Price = 1
    req.Other10Price = 1

    'Send Request to Server and Get Response
    Dim res As SetItemPriceResponse = api.SetItemPrice(req)

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

    $req->ItemCode = "1";
    $req->CurrencyCode = "usd";
    $req->PriceType = 1;
    $req->Price = 1;
    $req->BusinessVolume = 1;
    $req->CommissionableVolume = 1;
    $req->TaxablePrice = 1;
    $req->ShippingPrice = 1;
    $req->Other1Price = 1;
    $req->Other2Price = 1;
    $req->Other3Price = 1;
    $req->Other4Price = 1;
    $req->Other5Price = 1;
    $req->Other6Price = 1;
    $req->Other7Price = 1;
    $req->Other8Price = 1;
    $req->Other9Price = 1;
    $req->Other10Price = 1;

    //Send Request to Server and Get Response
    $res = $api.SetItemPrice($req);

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
    SetItemPriceRequest req = new SetItemPriceRequest();

    req.setItemCode("1");
    req.setCurrencyCode("usd");
    req.setPriceType(1);
    req.setPrice(1);
    req.setBusinessVolume(1);
    req.setCommissionableVolume(1);
    req.setTaxablePrice(1);
    req.setShippingPrice(1);
    req.setOther1Price(1);
    req.setOther2Price(1);
    req.setOther3Price(1);
    req.setOther4Price(1);
    req.setOther5Price(1);
    req.setOther6Price(1);
    req.setOther7Price(1);
    req.setOther8Price(1);
    req.setOther9Price(1);
    req.setOther10Price(1);

    //Send Request to Server and Get Response
    SetItemPriceResponse res = api.getExigoApiSoap().setItemPrice(req, auth);

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

### SetItemWarehouse

> Sets warehouse info for an item)
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Items |
| REST | `PUT /3.0/item/warehouse` |
| SOAP action | `https://api.exigo.com/SetItemWarehouse` |
| WSDL elements | `SetItemWarehouseRequest` → `SetItemWarehouseResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=SetItemWarehouse |

#### Input

**`SetItemWarehouseRequest`**

| Property | Type | Notes |
|---|---|---|
| `ItemCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| `WarehouseID` | `Int32` | Unique location for orders.<br>**Lookup:** company-specific list (see company-lists.md) |
| `IsAvailable` | `Boolean` | Optional. |
| `ItemManageTypeID` | `Int32` | Optional. Item management type.<br>**Lookup:** company-specific list (see company-lists.md) |

#### Output

**`SetItemWarehouseResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/item/warehouse HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "itemCode": "1",
  "warehouseID": 1,
  "isAvailable": true,
  "itemManageTypeID": 1
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
SOAPAction: "https://api.exigo.com/SetItemWarehouse"

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
    <SetItemWarehouseRequest xmlns="http://api.exigo.com/">
      <AllowedUserWarehouses>
        <int>int</int>
      </AllowedUserWarehouses>
      <AllowedWarehouseManagementTypes>
        <int>int</int>
      </AllowedWarehouseManagementTypes>
      <ItemCode>string</ItemCode>
      <WarehouseID>int</WarehouseID>
      <IsAvailable>boolean</IsAvailable>
      <ItemManageTypeID>int</ItemManageTypeID>
    </SetItemWarehouseRequest>
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
    <SetItemWarehouseResult xmlns="http://api.exigo.com/" />
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
    var req = new SetItemWarehouseRequest();

    req.ItemCode = "1";
    req.WarehouseID = 1;            //Unique location for orders
    req.IsAvailable = true;
    req.ItemManageTypeID = 1;       //Item management type

    //Send Request to Server and Get Response
    var res = await api.SetItemWarehouseAsync(req);

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
    SetItemWarehouseRequest req = new SetItemWarehouseRequest();

    req.ItemCode = "1";
    req.WarehouseID = 1;            //Unique location for orders
    req.IsAvailable = true;
    req.ItemManageTypeID = 1;       //Item management type

    //Send Request to Server and Get Response
    SetItemWarehouseResponse res = api.SetItemWarehouse(req);

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
    Dim req as new SetItemWarehouseRequest()

    req.ItemCode = "1"
    req.WarehouseID = 1
    req.IsAvailable = true
    req.ItemManageTypeID = 1

    'Send Request to Server and Get Response
    Dim res As SetItemWarehouseResponse = api.SetItemWarehouse(req)

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

    $req->ItemCode = "1";
    $req->WarehouseID = 1;
    $req->IsAvailable = 1;
    $req->ItemManageTypeID = 1;

    //Send Request to Server and Get Response
    $res = $api.SetItemWarehouse($req);

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
    SetItemWarehouseRequest req = new SetItemWarehouseRequest();

    req.setItemCode("1");
    req.setWarehouseID(1);
    req.setIsAvailable(1);
    req.setItemManageTypeID(1);

    //Send Request to Server and Get Response
    SetItemWarehouseResponse res = api.getExigoApiSoap().setItemWarehouse(req, auth);

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

### SetItemCountryRegion

> Sets country/region info for an item)
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Items |
| REST | `PUT /3.0/item/countryregion` |
| SOAP action | `https://api.exigo.com/SetItemCountryRegion` |
| WSDL elements | `SetItemCountryRegionRequest` → `SetItemCountryRegionResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=SetItemCountryRegion |

#### Input

**`SetItemCountryRegionRequest`**

| Property | Type | Notes |
|---|---|---|
| `ItemCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| `CountryCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| `RegionCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| `Taxed` | `Boolean` |  |
| `TaxedFed` | `Boolean` |  |
| `TaxedState` | `Boolean` |  |
| `UseTaxOverride` | `Boolean` |  |
| `TaxOverridePct` | `Decimal` |  |
| `BulkUpdate` | `Boolean` |  |

#### Output

**`SetItemCountryRegionResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/item/countryregion HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "itemCode": "1",
  "countryCode": "1",
  "regionCode": "1",
  "taxed": true,
  "taxedFed": true,
  "taxedState": true,
  "useTaxOverride": true,
  "taxOverridePct": null,
  "bulkUpdate": true
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
SOAPAction: "https://api.exigo.com/SetItemCountryRegion"

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
    <SetItemCountryRegionRequest xmlns="http://api.exigo.com/">
      <ItemCode>string</ItemCode>
      <CountryCode>string</CountryCode>
      <RegionCode>string</RegionCode>
      <Taxed>boolean</Taxed>
      <TaxedFed>boolean</TaxedFed>
      <TaxedState>boolean</TaxedState>
      <UseTaxOverride>boolean</UseTaxOverride>
      <TaxOverridePct>decimal</TaxOverridePct>
      <BulkUpdate>boolean</BulkUpdate>
    </SetItemCountryRegionRequest>
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
    <SetItemCountryRegionResult xmlns="http://api.exigo.com/" />
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
    var req = new SetItemCountryRegionRequest();

    req.ItemCode = "1";
    req.CountryCode = "1";
    req.RegionCode = "1";
    req.Taxed = true;
    req.TaxedFed = true;
    req.TaxedState = true;
    req.UseTaxOverride = true;
    req.TaxOverridePct = 1;
    req.BulkUpdate = true;

    //Send Request to Server and Get Response
    var res = await api.SetItemCountryRegionAsync(req);

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
    SetItemCountryRegionRequest req = new SetItemCountryRegionRequest();

    req.ItemCode = "1";
    req.CountryCode = "1";
    req.RegionCode = "1";
    req.Taxed = true;
    req.TaxedFed = true;
    req.TaxedState = true;
    req.UseTaxOverride = true;
    req.TaxOverridePct = 1;
    req.BulkUpdate = true;

    //Send Request to Server and Get Response
    SetItemCountryRegionResponse res = api.SetItemCountryRegion(req);

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
    Dim req as new SetItemCountryRegionRequest()

    req.ItemCode = "1"
    req.CountryCode = "1"
    req.RegionCode = "1"
    req.Taxed = true
    req.TaxedFed = true
    req.TaxedState = true
    req.UseTaxOverride = true
    req.TaxOverridePct = 1
    req.BulkUpdate = true

    'Send Request to Server and Get Response
    Dim res As SetItemCountryRegionResponse = api.SetItemCountryRegion(req)

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

    $req->ItemCode = "1";
    $req->CountryCode = "1";
    $req->RegionCode = "1";
    $req->Taxed = 1;
    $req->TaxedFed = 1;
    $req->TaxedState = 1;
    $req->UseTaxOverride = 1;
    $req->TaxOverridePct = 1;
    $req->BulkUpdate = 1;

    //Send Request to Server and Get Response
    $res = $api.SetItemCountryRegion($req);

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
    SetItemCountryRegionRequest req = new SetItemCountryRegionRequest();

    req.setItemCode("1");
    req.setCountryCode("1");
    req.setRegionCode("1");
    req.setTaxed(1);
    req.setTaxedFed(1);
    req.setTaxedState(1);
    req.setUseTaxOverride(1);
    req.setTaxOverridePct(1);
    req.setBulkUpdate(1);

    //Send Request to Server and Get Response
    SetItemCountryRegionResponse res = api.getExigoApiSoap().setItemCountryRegion(req, auth);

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

### SetItemImage

> Set Images for an Item

| | |
|---|---|
| Category | Items |
| REST | `PUT /3.0/item/image` |
| SOAP action | `https://api.exigo.com/SetItemImage` |
| WSDL elements | `SetItemImageRequest` → `SetItemImageResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=SetItemImage |

#### Input

**`SetItemImageRequest`**

| Property | Type | Notes |
|---|---|---|
| `ItemCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| `TinyImageName` | `String` | Optional. |
| `TinyImageData` | `Byte[]` | Optional. |
| `SmallImageName` | `String` | Optional. |
| `SmallImageData` | `Byte[]` | Optional. |
| `LargeImageName` | `String` | Optional. |
| `LargeImageData` | `Byte[]` | Optional. |

#### Output

**`SetItemImageResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/item/image HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "itemCode": "1",
  "tinyImageName": "1",
  "tinyImageData": null,
  "smallImageName": "1",
  "smallImageData": null,
  "largeImageName": "1",
  "largeImageData": null
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
SOAPAction: "https://api.exigo.com/SetItemImage"

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
    <SetItemImageRequest xmlns="http://api.exigo.com/">
      <ItemCode>string</ItemCode>
      <TinyImageName>string</TinyImageName>
      <TinyImageData>base64Binary</TinyImageData>
      <SmallImageName>string</SmallImageName>
      <SmallImageData>base64Binary</SmallImageData>
      <LargeImageName>string</LargeImageName>
      <LargeImageData>base64Binary</LargeImageData>
    </SetItemImageRequest>
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
    <SetItemImageResult xmlns="http://api.exigo.com/" />
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
    var req = new SetItemImageRequest();

    req.ItemCode = "1";
    req.TinyImageName = "1";

    //Add TinyImageData
    var tinyimagedata = new List<Byte>();
    tinyimagedata.Add(1);
    tinyimagedata.Add(2);

    //Now attach the list to the request
    req.TinyImageData = tinyimagedata.ToArray();
    req.SmallImageName = "1";

    //Add SmallImageData
    var smallimagedata = new List<Byte>();
    smallimagedata.Add(1);
    smallimagedata.Add(2);

    //Now attach the list to the request
    req.SmallImageData = smallimagedata.ToArray();
    req.LargeImageName = "1";

    //Add LargeImageData
    var largeimagedata = new List<Byte>();
    largeimagedata.Add(1);
    largeimagedata.Add(2);

    //Now attach the list to the request
    req.LargeImageData = largeimagedata.ToArray();

    //Send Request to Server and Get Response
    var res = await api.SetItemImageAsync(req);

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
    SetItemImageRequest req = new SetItemImageRequest();

    req.ItemCode = "1";
    req.TinyImageName = "1";

    //Add TinyImageData
    List<Byte> tinyimagedata = new List<Byte>();
    tinyimagedata.Add(1);
    tinyimagedata.Add(2);

    //Now attach the list to the request
    req.TinyImageData = tinyimagedata.ToArray();
    req.SmallImageName = "1";

    //Add SmallImageData
    List<Byte> smallimagedata = new List<Byte>();
    smallimagedata.Add(1);
    smallimagedata.Add(2);

    //Now attach the list to the request
    req.SmallImageData = smallimagedata.ToArray();
    req.LargeImageName = "1";

    //Add LargeImageData
    List<Byte> largeimagedata = new List<Byte>();
    largeimagedata.Add(1);
    largeimagedata.Add(2);

    //Now attach the list to the request
    req.LargeImageData = largeimagedata.ToArray();

    //Send Request to Server and Get Response
    SetItemImageResponse res = api.SetItemImage(req);

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
    Dim req as new SetItemImageRequest()

    req.ItemCode = "1"
    req.TinyImageName = "1"

    'Add TinyImageData
    Dim tinyimagedata As New List(Of Byte)()
    tinyimagedata.Add(1)
    tinyimagedata.Add(2)

    'Now attach the list to the request
    req.TinyImageData = tinyimagedata.ToArray()
    req.SmallImageName = "1"

    'Add SmallImageData
    Dim smallimagedata As New List(Of Byte)()
    smallimagedata.Add(1)
    smallimagedata.Add(2)

    'Now attach the list to the request
    req.SmallImageData = smallimagedata.ToArray()
    req.LargeImageName = "1"

    'Add LargeImageData
    Dim largeimagedata As New List(Of Byte)()
    largeimagedata.Add(1)
    largeimagedata.Add(2)

    'Now attach the list to the request
    req.LargeImageData = largeimagedata.ToArray()

    'Send Request to Server and Get Response
    Dim res As SetItemImageResponse = api.SetItemImage(req)

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

    $req->ItemCode = "1";
    $req->TinyImageName = "1";

    //Add TinyImageData

    //Now attach the list to the request
    req.TinyImageData = array(tinyImageDat1,tinyImageDat2);
    $req->SmallImageName = "1";

    //Add SmallImageData

    //Now attach the list to the request
    req.SmallImageData = array(smallImageDat1,smallImageDat2);
    $req->LargeImageName = "1";

    //Add LargeImageData

    //Now attach the list to the request
    req.LargeImageData = array(largeImageDat1,largeImageDat2);

    //Send Request to Server and Get Response
    $res = $api.SetItemImage($req);

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
    SetItemImageRequest req = new SetItemImageRequest();

    req.setItemCode("1");
    req.setTinyImageName("1");

    //Add TinyImageData
    ArrayOfSystem.Byte tinyimagedata = new ArrayOfSystem.Byte();

    Byte tinyImageDat1 = new Byte();
    tinyimagedata.Add(tinyImageDat1);

    Byte tinyImageDat2 = new Byte();
    tinyimagedata.Add(tinyImageDat2);

    //Now attach the list to the request
    req.setTinyImageData(tinyimagedata);
    req.setSmallImageName("1");

    //Add SmallImageData
    ArrayOfSystem.Byte smallimagedata = new ArrayOfSystem.Byte();

    Byte smallImageDat1 = new Byte();
    smallimagedata.Add(smallImageDat1);

    Byte smallImageDat2 = new Byte();
    smallimagedata.Add(smallImageDat2);

    //Now attach the list to the request
    req.setSmallImageData(smallimagedata);
    req.setLargeImageName("1");

    //Add LargeImageData
    ArrayOfSystem.Byte largeimagedata = new ArrayOfSystem.Byte();

    Byte largeImageDat1 = new Byte();
    largeimagedata.Add(largeImageDat1);

    Byte largeImageDat2 = new Byte();
    largeimagedata.Add(largeImageDat2);

    //Now attach the list to the request
    req.setLargeImageData(largeimagedata);

    //Send Request to Server and Get Response
    SetItemImageResponse res = api.getExigoApiSoap().setItemImage(req, auth);

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

### CreateWebCategory

> Creates a new product web category.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Items |
| REST | `POST /3.0/webcategory` |
| SOAP action | `https://api.exigo.com/CreateWebCategory` |
| WSDL elements | `CreateWebCategoryRequest` → `CreateWebCategoryResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateWebCategory |

#### Input

**`CreateWebCategoryRequest`**

| Property | Type | Notes |
|---|---|---|
| `WebID` | `Int32` | WebID used in content engine. |
| `ParentID` | `Int32` | Optional. Parent category ID (use 0 for the root). Defaults to -1. |
| `Description` | `String` |  |

#### Output

**`CreateWebCategoryResponse`**

| Property | Type | Notes |
|---|---|---|
| `CategoryID` | `Int32` |  |
| `WebID` | `Int32` | Optionally use categories from content engine.<br>**Lookup:** company-specific list (see company-lists.md) |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/webcategory HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "webID": 1,
  "parentID": 1,
  "description": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "categoryID": 1,
  "webID": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateWebCategory"

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
    <CreateWebCategoryRequest xmlns="http://api.exigo.com/">
      <WebID>int</WebID>
      <ParentID>int</ParentID>
      <Description>string</Description>
    </CreateWebCategoryRequest>
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
    <CreateWebCategoryResult xmlns="http://api.exigo.com/">
      <CategoryID>int</CategoryID>
      <WebID>int</WebID>
    </CreateWebCategoryResult>
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
    var req = new CreateWebCategoryRequest();

    req.WebID = 1;                  //WebID used in content engine
    req.ParentID = 1;               //Parent category ID (use 0 for the root)
    req.Description = "1";

    //Send Request to Server and Get Response
    var res = await api.CreateWebCategoryAsync(req);

    //Now examine the results:
    Console.WriteLine("CategoryID: {0}", res.CategoryID);
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
    CreateWebCategoryRequest req = new CreateWebCategoryRequest();

    req.WebID = 1;                  //WebID used in content engine
    req.ParentID = 1;               //Parent category ID (use 0 for the root)
    req.Description = "1";

    //Send Request to Server and Get Response
    CreateWebCategoryResponse res = api.CreateWebCategory(req);

    //Now examine the results:
    Console.WriteLine("CategoryID: {0}", res.CategoryID);
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
    Dim req as new CreateWebCategoryRequest()

    req.WebID = 1
    req.ParentID = 1
    req.Description = "1"

    'Send Request to Server and Get Response
    Dim res As CreateWebCategoryResponse = api.CreateWebCategory(req)

    'Now examine the results:
    Console.WriteLine("CategoryID: {0}", res.CategoryID)
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

    $req->WebID = 1;
    $req->ParentID = 1;
    $req->Description = "1";

    //Send Request to Server and Get Response
    $res = $api.CreateWebCategory($req);

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
    CreateWebCategoryRequest req = new CreateWebCategoryRequest();

    req.setWebID(1);
    req.setParentID(1);
    req.setDescription("1");

    //Send Request to Server and Get Response
    CreateWebCategoryResponse res = api.getExigoApiSoap().createWebCategory(req, auth);

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

### UpdateWebCategory

>  Updates web category information.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Items |
| REST | `PUT /3.0/webcategory` |
| SOAP action | `https://api.exigo.com/UpdateWebCategory` |
| WSDL elements | `UpdateWebCategoryRequest` → `UpdateWebCategoryResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=UpdateWebCategory |

#### Input

**`UpdateWebCategoryRequest`**

| Property | Type | Notes |
|---|---|---|
| `WebID` | `Int32` | WebID used in content engine. |
| `CategoryID` | `Int32` |  |
| `Description` | `String` | Maximum length is 50. |

#### Output

**`UpdateWebCategoryResponse`**

| Property | Type | Notes |
|---|---|---|
| `CategoryID` | `Int32` |  |
| `WebID` | `Int32` | WebID used in content engine. |
| `Description` | `String` |  |

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/webcategory HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "webID": 1,
  "categoryID": 1,
  "description": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "categoryID": 1,
  "webID": 1,
  "description": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/UpdateWebCategory"

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
    <UpdateWebCategoryRequest xmlns="http://api.exigo.com/">
      <WebID>int</WebID>
      <CategoryID>int</CategoryID>
      <Description>string</Description>
    </UpdateWebCategoryRequest>
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
    <UpdateWebCategoryResult xmlns="http://api.exigo.com/">
      <CategoryID>int</CategoryID>
      <WebID>int</WebID>
      <Description>string</Description>
    </UpdateWebCategoryResult>
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
    var req = new UpdateWebCategoryRequest();

    req.WebID = 1;                  //WebID used in content engine
    req.CategoryID = 1;
    req.Description = "1";          //Maximum length is 50

    //Send Request to Server and Get Response
    var res = await api.UpdateWebCategoryAsync(req);

    //Now examine the results:
    Console.WriteLine("CategoryID: {0}", res.CategoryID);
    Console.WriteLine("WebID: {0}", res.WebID);
    Console.WriteLine("Description: {0}", res.Description);
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
    UpdateWebCategoryRequest req = new UpdateWebCategoryRequest();

    req.WebID = 1;                  //WebID used in content engine
    req.CategoryID = 1;
    req.Description = "1";          //Maximum length is 50

    //Send Request to Server and Get Response
    UpdateWebCategoryResponse res = api.UpdateWebCategory(req);

    //Now examine the results:
    Console.WriteLine("CategoryID: {0}", res.CategoryID);
    Console.WriteLine("WebID: {0}", res.WebID);
    Console.WriteLine("Description: {0}", res.Description);
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
    Dim req as new UpdateWebCategoryRequest()

    req.WebID = 1
    req.CategoryID = 1
    req.Description = "1"

    'Send Request to Server and Get Response
    Dim res As UpdateWebCategoryResponse = api.UpdateWebCategory(req)

    'Now examine the results:
    Console.WriteLine("CategoryID: {0}", res.CategoryID)
    Console.WriteLine("WebID: {0}", res.WebID)
    Console.WriteLine("Description: {0}", res.Description)
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

    $req->WebID = 1;
    $req->CategoryID = 1;
    $req->Description = "1";

    //Send Request to Server and Get Response
    $res = $api.UpdateWebCategory($req);

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
    UpdateWebCategoryRequest req = new UpdateWebCategoryRequest();

    req.setWebID(1);
    req.setCategoryID(1);
    req.setDescription("1");

    //Send Request to Server and Get Response
    UpdateWebCategoryResponse res = api.getExigoApiSoap().updateWebCategory(req, auth);

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

### DeleteWebCategory

> Deletes a web category.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Items |
| REST | `DELETE /3.0/webcategory` |
| SOAP action | `https://api.exigo.com/DeleteWebCategory` |
| WSDL elements | `DeleteWebCategoryRequest` → `DeleteWebCategoryResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DeleteWebCategory |

#### Input

**`DeleteWebCategoryRequest`**

| Property | Type | Notes |
|---|---|---|
| `WebID` | `Int32` | WebID used in content engine. |
| `CategoryID` | `Int32` |  |

#### Output

**`DeleteWebCategoryResponse`**

| Property | Type | Notes |
|---|---|---|
| `CategoryID` | `Int32` |  |
| `WebID` | `Int32` | WebID used in content engine. |

#### REST example

```http
DELETE https://yourcompany-api.exigo.com/3.0/webcategory HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "webID": 1,
  "categoryID": 1
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "categoryID": 1,
  "webID": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/DeleteWebCategory"

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
    <DeleteWebCategoryRequest xmlns="http://api.exigo.com/">
      <WebID>int</WebID>
      <CategoryID>int</CategoryID>
    </DeleteWebCategoryRequest>
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
    <DeleteWebCategoryResult xmlns="http://api.exigo.com/">
      <CategoryID>int</CategoryID>
      <WebID>int</WebID>
    </DeleteWebCategoryResult>
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
    var req = new DeleteWebCategoryRequest();

    req.WebID = 1;                  //WebID used in content engine
    req.CategoryID = 1;

    //Send Request to Server and Get Response
    var res = await api.DeleteWebCategoryAsync(req);

    //Now examine the results:
    Console.WriteLine("CategoryID: {0}", res.CategoryID);
    Console.WriteLine("WebID: {0}", res.WebID);
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
    DeleteWebCategoryRequest req = new DeleteWebCategoryRequest();

    req.WebID = 1;                  //WebID used in content engine
    req.CategoryID = 1;

    //Send Request to Server and Get Response
    DeleteWebCategoryResponse res = api.DeleteWebCategory(req);

    //Now examine the results:
    Console.WriteLine("CategoryID: {0}", res.CategoryID);
    Console.WriteLine("WebID: {0}", res.WebID);
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
    Dim req as new DeleteWebCategoryRequest()

    req.WebID = 1
    req.CategoryID = 1

    'Send Request to Server and Get Response
    Dim res As DeleteWebCategoryResponse = api.DeleteWebCategory(req)

    'Now examine the results:
    Console.WriteLine("CategoryID: {0}", res.CategoryID)
    Console.WriteLine("WebID: {0}", res.WebID)
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

    $req->WebID = 1;
    $req->CategoryID = 1;

    //Send Request to Server and Get Response
    $res = $api.DeleteWebCategory($req);

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
    DeleteWebCategoryRequest req = new DeleteWebCategoryRequest();

    req.setWebID(1);
    req.setCategoryID(1);

    //Send Request to Server and Get Response
    DeleteWebCategoryResponse res = api.getExigoApiSoap().deleteWebCategory(req, auth);

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

### AddProductsToCategory

> Adds items/products to a web category.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Items |
| REST | `POST /3.0/webcategory/product` |
| SOAP action | `https://api.exigo.com/AddProductsToCategory` |
| WSDL elements | `AddProductsToCategoryRequest` → `AddProductsToCategoryResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=AddProductsToCategory |

#### Input

**`AddProductsToCategoryRequest`**

| Property | Type | Notes |
|---|---|---|
| `WebID` | `Int32` | WebID used in content engine. |
| `CategoryID` | `Int32` |  |
| `ItemCodes` | `String[]` | List of Item Codes to be added. |

#### Output

**`AddProductsToCategoryResponse`**

| Property | Type | Notes |
|---|---|---|
| `CategoryID` | `Int32` |  |
| `WebID` | `Int32` | WebID used in content engine. |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/webcategory/product HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "webID": 1,
  "categoryID": 1,
  "itemCodes": null
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "categoryID": 1,
  "webID": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/AddProductsToCategory"

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
    var req = new AddProductsToCategoryRequest();

    req.WebID = 1;                  //WebID used in content engine
    req.CategoryID = 1;

    //Add ItemCodes
    var itemcodes = new List<String>();
    itemcodes.Add("1");
    itemcodes.Add("2");

    //Now attach the list to the request
    req.ItemCodes = itemcodes.ToArray();

    //Send Request to Server and Get Response
    var res = await api.AddProductsToCategoryAsync(req);

    //Now examine the results:
    Console.WriteLine("CategoryID: {0}", res.CategoryID);
    Console.WriteLine("WebID: {0}", res.WebID);
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
    AddProductsToCategoryRequest req = new AddProductsToCategoryRequest();

    req.WebID = 1;                  //WebID used in content engine
    req.CategoryID = 1;

    //Add ItemCodes
    List<String> itemcodes = new List<String>();
    itemcodes.Add("1");
    itemcodes.Add("2");

    //Now attach the list to the request
    req.ItemCodes = itemcodes.ToArray();

    //Send Request to Server and Get Response
    AddProductsToCategoryResponse res = api.AddProductsToCategory(req);

    //Now examine the results:
    Console.WriteLine("CategoryID: {0}", res.CategoryID);
    Console.WriteLine("WebID: {0}", res.WebID);
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
    Dim req as new AddProductsToCategoryRequest()

    req.WebID = 1
    req.CategoryID = 1

    'Add ItemCodes
    Dim itemcodes As New List(Of String)()
    itemcodes.Add("1")
    itemcodes.Add("2")

    'Now attach the list to the request
    req.ItemCodes = itemcodes.ToArray()

    'Send Request to Server and Get Response
    Dim res As AddProductsToCategoryResponse = api.AddProductsToCategory(req)

    'Now examine the results:
    Console.WriteLine("CategoryID: {0}", res.CategoryID)
    Console.WriteLine("WebID: {0}", res.WebID)
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

    $req->WebID = 1;
    $req->CategoryID = 1;

    //Add ItemCodes

    $itemCode1->Length = 1;
    $itemCode1->Chars = 1;

    $itemCode2->Length = 2;
    $itemCode2->Chars = 2;

    //Now attach the list to the request
    req.ItemCodes = array(itemCode1,itemCode2);

    //Send Request to Server and Get Response
    $res = $api.AddProductsToCategory($req);

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
    AddProductsToCategoryRequest req = new AddProductsToCategoryRequest();

    req.setWebID(1);
    req.setCategoryID(1);

    //Add ItemCodes
    ArrayOfSystem.String itemcodes = new ArrayOfSystem.String();

    String itemCode1 = new String();
    itemCode1.setLength(1);
    itemCode1.setChars(1);
    itemcodes.Add(itemCode1);

    String itemCode2 = new String();
    itemCode2.setLength(2);
    itemCode2.setChars(2);
    itemcodes.Add(itemCode2);

    //Now attach the list to the request
    req.setItemCodes(itemcodes);

    //Send Request to Server and Get Response
    AddProductsToCategoryResponse res = api.getExigoApiSoap().addProductsToCategory(req, auth);

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

### DeleteProductFromCategory

> Deletes a product from a web category.
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Items |
| REST | `DELETE /3.0/webcategory/product` |
| SOAP action | `https://api.exigo.com/DeleteProductFromCategory` |
| WSDL elements | `DeleteProductFromCategoryRequest` → `DeleteProductFromCategoryResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DeleteProductFromCategory |

#### Input

**`DeleteProductFromCategoryRequest`**

| Property | Type | Notes |
|---|---|---|
| `WebID` | `Int32` | WebID used in content engine. |
| `CategoryID` | `Int32` |  |
| `ItemCode` | `String` | Item code to be removed. |

#### Output

**`DeleteProductFromCategoryResponse`**

| Property | Type | Notes |
|---|---|---|
| `CategoryID` | `Int32` |  |
| `WebID` | `Int32` | WebID used in content engine. |
| `ItemCode` | `String` | Item code that was removed. |

#### REST example

```http
DELETE https://yourcompany-api.exigo.com/3.0/webcategory/product HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "webID": 1,
  "categoryID": 1,
  "itemCode": "1"
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "categoryID": 1,
  "webID": 1,
  "itemCode": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/DeleteProductFromCategory"

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
    <DeleteProductFromCategoryRequest xmlns="http://api.exigo.com/">
      <WebID>int</WebID>
      <CategoryID>int</CategoryID>
      <ItemCode>string</ItemCode>
    </DeleteProductFromCategoryRequest>
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
    <DeleteProductFromCategoryResult xmlns="http://api.exigo.com/">
      <CategoryID>int</CategoryID>
      <WebID>int</WebID>
      <ItemCode>string</ItemCode>
    </DeleteProductFromCategoryResult>
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
    var req = new DeleteProductFromCategoryRequest();

    req.WebID = 1;                  //WebID used in content engine
    req.CategoryID = 1;
    req.ItemCode = "1";             //Item code to be removed

    //Send Request to Server and Get Response
    var res = await api.DeleteProductFromCategoryAsync(req);

    //Now examine the results:
    Console.WriteLine("CategoryID: {0}", res.CategoryID);
    Console.WriteLine("WebID: {0}", res.WebID);
    Console.WriteLine("ItemCode: {0}", res.ItemCode);
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
    DeleteProductFromCategoryRequest req = new DeleteProductFromCategoryRequest();

    req.WebID = 1;                  //WebID used in content engine
    req.CategoryID = 1;
    req.ItemCode = "1";             //Item code to be removed

    //Send Request to Server and Get Response
    DeleteProductFromCategoryResponse res = api.DeleteProductFromCategory(req);

    //Now examine the results:
    Console.WriteLine("CategoryID: {0}", res.CategoryID);
    Console.WriteLine("WebID: {0}", res.WebID);
    Console.WriteLine("ItemCode: {0}", res.ItemCode);
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
    Dim req as new DeleteProductFromCategoryRequest()

    req.WebID = 1
    req.CategoryID = 1
    req.ItemCode = "1"

    'Send Request to Server and Get Response
    Dim res As DeleteProductFromCategoryResponse = api.DeleteProductFromCategory(req)

    'Now examine the results:
    Console.WriteLine("CategoryID: {0}", res.CategoryID)
    Console.WriteLine("WebID: {0}", res.WebID)
    Console.WriteLine("ItemCode: {0}", res.ItemCode)
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

    $req->WebID = 1;
    $req->CategoryID = 1;
    $req->ItemCode = "1";

    //Send Request to Server and Get Response
    $res = $api.DeleteProductFromCategory($req);

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
    DeleteProductFromCategoryRequest req = new DeleteProductFromCategoryRequest();

    req.setWebID(1);
    req.setCategoryID(1);
    req.setItemCode("1");

    //Send Request to Server and Get Response
    DeleteProductFromCategoryResponse res = api.getExigoApiSoap().deleteProductFromCategory(req, auth);

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

### GetWarehouses

> Gets a list of warehouses setup in the system.

| | |
|---|---|
| Category | Items |
| REST | `GET /3.0/warehouse` |
| SOAP action | `https://api.exigo.com/GetWarehouses` |
| WSDL elements | `GetWarehousesRequest` → `GetWarehousesResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetWarehouses |

#### Input

**`GetWarehousesRequest`**

_No properties._

#### Output

**`GetWarehousesResponse`**

| Property | Type | Notes |
|---|---|---|
| `Warehouses` | `WarehouseResponse[]` |  |

**`WarehouseResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `WarehouseID` | `Int32` | Unique location for orders.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Description` | `String` |  |
| &nbsp;&nbsp;↳ `Address1` | `String` |  |
| &nbsp;&nbsp;↳ `Address2` | `String` |  |
| &nbsp;&nbsp;↳ `City` | `String` |  |
| &nbsp;&nbsp;↳ `State` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Zip` | `String` |  |
| &nbsp;&nbsp;↳ `Country` | `String` | **Lookup:** company-specific list (see company-lists.md) |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/warehouse
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "warehouses": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetWarehouses"

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
    <GetWarehousesRequest xmlns="http://api.exigo.com/" />
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
    <GetWarehousesResult xmlns="http://api.exigo.com/">
      <Warehouses>
        <WarehouseResponse>
          <WarehouseID>int</WarehouseID>
          <Description>string</Description>
          <Address1>string</Address1>
          <Address2>string</Address2>
          <City>string</City>
          <State>string</State>
          <Zip>string</Zip>
          <Country>string</Country>
        </WarehouseResponse>
      </Warehouses>
    </GetWarehousesResult>
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
    var req = new GetWarehousesRequest();

    //Send Request to Server and Get Response
    var res = await api.GetWarehousesAsync(req);

    //Now examine the results:

    foreach (var warehouse  in res.Warehouses)
    {
        Console.WriteLine("WarehouseID: {0}", warehouse.WarehouseID);
        Console.WriteLine("Description: {0}", warehouse.Description);
        Console.WriteLine("Address1: {0}", warehouse.Address1);
        Console.WriteLine("Address2: {0}", warehouse.Address2);
        Console.WriteLine("City: {0}", warehouse.City);
        Console.WriteLine("Zip: {0}", warehouse.Zip);
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
    GetWarehousesRequest req = new GetWarehousesRequest();

    //Send Request to Server and Get Response
    GetWarehousesResponse res = api.GetWarehouses(req);

    //Now examine the results:

    foreach (WarehouseResponse warehouse  in res.Warehouses)
    {
        Console.WriteLine("WarehouseID: {0}", warehouse.WarehouseID);
        Console.WriteLine("Description: {0}", warehouse.Description);
        Console.WriteLine("Address1: {0}", warehouse.Address1);
        Console.WriteLine("Address2: {0}", warehouse.Address2);
        Console.WriteLine("City: {0}", warehouse.City);
        Console.WriteLine("Zip: {0}", warehouse.Zip);
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
    Dim req as new GetWarehousesRequest()

    'Send Request to Server and Get Response
    Dim res As GetWarehousesResponse = api.GetWarehouses(req)

    'Now examine the results:

    For Each warehouse As WarehouseResponse In res.Warehouses
        Console.WriteLine("WarehouseID: {0}", warehouse.WarehouseID)
        Console.WriteLine("Description: {0}", warehouse.Description)
        Console.WriteLine("Address1: {0}", warehouse.Address1)
        Console.WriteLine("Address2: {0}", warehouse.Address2)
        Console.WriteLine("City: {0}", warehouse.City)
        Console.WriteLine("Zip: {0}", warehouse.Zip)
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
    $res = $api.GetWarehouses($req);

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
    GetWarehousesRequest req = new GetWarehousesRequest();

    //Send Request to Server and Get Response
    GetWarehousesResponse res = api.getExigoApiSoap().getWarehouses(req, auth);

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

### AdjustInventory

> Posts an adjustment to item inventory.

| | |
|---|---|
| Category | Items |
| REST | `PUT /3.0/warehouse/inventory` |
| SOAP action | `https://api.exigo.com/AdjustInventory` |
| WSDL elements | `AdjustInventoryRequest` → `AdjustInventoryResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=AdjustInventory |

#### Input

**`AdjustInventoryRequest`**

| Property | Type | Notes |
|---|---|---|
| `WarehouseID` | `Int32` | Unique location for orders.<br>**Lookup:** company-specific list (see company-lists.md) |
| `ItemCode` | `String` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Quantity` | `Int32` |  |
| `Notes` | `String` | Optional. |

#### Output

**`AdjustInventoryResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/warehouse/inventory HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "warehouseID": 1,
  "itemCode": "1",
  "quantity": 1,
  "notes": ""
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
SOAPAction: "https://api.exigo.com/AdjustInventory"

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
    <AdjustInventoryRequest xmlns="http://api.exigo.com/">
      <WarehouseID>int</WarehouseID>
      <ItemCode>string</ItemCode>
      <Quantity>int</Quantity>
      <Notes>string</Notes>
    </AdjustInventoryRequest>
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
    <AdjustInventoryResult xmlns="http://api.exigo.com/" />
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
    var req = new AdjustInventoryRequest();

    req.WarehouseID = 1;            //Unique location for orders
    req.ItemCode = "1";
    req.Quantity = 1;
    req.Notes = "1";

    //Send Request to Server and Get Response
    var res = await api.AdjustInventoryAsync(req);

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
    AdjustInventoryRequest req = new AdjustInventoryRequest();

    req.WarehouseID = 1;            //Unique location for orders
    req.ItemCode = "1";
    req.Quantity = 1;
    req.Notes = "1";

    //Send Request to Server and Get Response
    AdjustInventoryResponse res = api.AdjustInventory(req);

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
    Dim req as new AdjustInventoryRequest()

    req.WarehouseID = 1
    req.ItemCode = "1"
    req.Quantity = 1
    req.Notes = "1"

    'Send Request to Server and Get Response
    Dim res As AdjustInventoryResponse = api.AdjustInventory(req)

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

    $req->WarehouseID = 1;
    $req->ItemCode = "1";
    $req->Quantity = 1;
    $req->Notes = "1";

    //Send Request to Server and Get Response
    $res = $api.AdjustInventory($req);

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
    AdjustInventoryRequest req = new AdjustInventoryRequest();

    req.setWarehouseID(1);
    req.setItemCode("1");
    req.setQuantity(1);
    req.setNotes("1");

    //Send Request to Server and Get Response
    AdjustInventoryResponse res = api.getExigoApiSoap().adjustInventory(req, auth);

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

### SetItemKitMembers

> Sets the children for a static kit
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Items |
| REST | `PUT /3.0/item/kit/members` |
| SOAP action | `https://api.exigo.com/SetItemKitMembers` |
| WSDL elements | `SetItemKitMembersRequest` → `SetItemKitMembersResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=SetItemKitMembers |

#### Input

**`SetItemKitMembersRequest`**

| Property | Type | Notes |
|---|---|---|
| `ParentItemCode` | `String` | Unique identifier for an item record. |
| `ItemKitMembers` | `KitMember[]` |  |

**`KitMember`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `ItemCode` | `String` | Unique identifier for an item record. |
| &nbsp;&nbsp;↳ `Quantity` | `Int32` |  |

#### Output

**`SetItemKitMembersResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/item/kit/members HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "parentItemCode": "1",
  "itemKitMembers": null
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
SOAPAction: "https://api.exigo.com/SetItemKitMembers"

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
    <SetItemKitMembersRequest xmlns="http://api.exigo.com/">
      <ParentItemCode>string</ParentItemCode>
      <ItemKitMembers>
        <KitMember>
          <ItemID>int</ItemID>
          <ItemCode>string</ItemCode>
          <Quantity>int</Quantity>
        </KitMember>
      </ItemKitMembers>
    </SetItemKitMembersRequest>
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
    <SetItemKitMembersResult xmlns="http://api.exigo.com/" />
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
    var req = new SetItemKitMembersRequest();

    req.ParentItemCode = "1";       //Unique identifier for an item record

    //Add ItemKitMembers
    var itemkitmembers = new List<KitMember>();

    var itemKitMember1 = new KitMember();
    itemKitMember1.ItemCode = "1";
    itemKitMember1.Quantity = 1;
    itemkitmembers.Add(itemKitMember1);

    var itemKitMember2 = new KitMember();
    itemKitMember2.ItemCode = "2";
    itemKitMember2.Quantity = 2;
    itemkitmembers.Add(itemKitMember2);

    //Now attach the list to the request
    req.ItemKitMembers = itemkitmembers.ToArray();

    //Send Request to Server and Get Response
    var res = await api.SetItemKitMembersAsync(req);

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
    SetItemKitMembersRequest req = new SetItemKitMembersRequest();

    req.ParentItemCode = "1";       //Unique identifier for an item record

    //Add ItemKitMembers
    List<KitMember> itemkitmembers = new List<KitMember>();

    KitMember itemKitMember1 = new KitMember();
    itemKitMember1.ItemCode = "1";
    itemKitMember1.Quantity = 1;
    itemkitmembers.Add(itemKitMember1);

    KitMember itemKitMember2 = new KitMember();
    itemKitMember2.ItemCode = "2";
    itemKitMember2.Quantity = 2;
    itemkitmembers.Add(itemKitMember2);

    //Now attach the list to the request
    req.ItemKitMembers = itemkitmembers.ToArray();

    //Send Request to Server and Get Response
    SetItemKitMembersResponse res = api.SetItemKitMembers(req);

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
    Dim req as new SetItemKitMembersRequest()

    req.ParentItemCode = "1"

    'Add ItemKitMembers
    Dim itemkitmembers As New List(Of KitMember)()

    Dim itemKitMember1 as new KitMember()
    itemKitMember1.ItemCode = "1"
    itemKitMember1.Quantity = 1
    itemkitmembers.Add(itemKitMember1)

    Dim itemKitMember2 as new KitMember()
    itemKitMember2.ItemCode = "2"
    itemKitMember2.Quantity = 2
    itemkitmembers.Add(itemKitMember2)

    'Now attach the list to the request
    req.ItemKitMembers = itemkitmembers.ToArray()

    'Send Request to Server and Get Response
    Dim res As SetItemKitMembersResponse = api.SetItemKitMembers(req)

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

    $req->ParentItemCode = "1";

    //Add ItemKitMembers

    $itemKitMember1->ItemCode = "1";
    $itemKitMember1->Quantity = 1;

    $itemKitMember2->ItemCode = "2";
    $itemKitMember2->Quantity = 2;

    //Now attach the list to the request
    req.ItemKitMembers = array(itemKitMember1,itemKitMember2);

    //Send Request to Server and Get Response
    $res = $api.SetItemKitMembers($req);

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
    SetItemKitMembersRequest req = new SetItemKitMembersRequest();

    req.setParentItemCode("1");

    //Add ItemKitMembers
    ArrayOfSetItemKitMembersRequest+KitMember itemkitmembers = new ArrayOfSetItemKitMembersRequest+KitMember();

    KitMember itemKitMember1 = new KitMember();
    itemKitMember1.setItemCode("1");
    itemKitMember1.setQuantity(1);
    itemkitmembers.Add(itemKitMember1);

    KitMember itemKitMember2 = new KitMember();
    itemKitMember2.setItemCode("2");
    itemKitMember2.setQuantity(2);
    itemkitmembers.Add(itemKitMember2);

    //Now attach the list to the request
    req.setItemKitMembers(itemkitmembers);

    //Send Request to Server and Get Response
    SetItemKitMembersResponse res = api.getExigoApiSoap().setItemKitMembers(req, auth);

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

### SetItemSubscription

> Set Item Subscriptions
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Items |
| REST | `PUT /3.0/item/subscription` |
| SOAP action | `https://api.exigo.com/SetItemSubscription` |
| WSDL elements | `SetItemSubscriptionRequest` → `SetItemSubscriptionResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=SetItemSubscription |

#### Input

**`SetItemSubscriptionRequest`**

| Property | Type | Notes |
|---|---|---|
| `ItemCode` | `String` | Optional. Unique identifier for an item record. Either ItemCode or ItemID must be provided. |
| `ItemID` | `Int32` | Optional. Unique identifier for an item record. Either ItemCode or ItemID must be provided. |
| `Subscriptions` | `Subscription[]` | Optional. Leave empty to remove all subscriptions from the given item. |

**`Subscription`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `SubscriptionID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `TimeAdjustmentDays` | `Int32` |  |

#### Output

**`SetItemSubscriptionResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/item/subscription HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
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
SOAPAction: "https://api.exigo.com/SetItemSubscription"

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
    <SetItemSubscriptionRequest xmlns="http://api.exigo.com/">
      <ItemCode>string</ItemCode>
      <ItemID>int</ItemID>
      <Subscriptions>
        <Subscription>
          <SubscriptionID>int</SubscriptionID>
          <TimeAdjustmentDays>int</TimeAdjustmentDays>
        </Subscription>
      </Subscriptions>
    </SetItemSubscriptionRequest>
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
    <SetItemSubscriptionResult xmlns="http://api.exigo.com/" />
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
    var req = new SetItemSubscriptionRequest();

    //Send Request to Server and Get Response
    var res = await api.SetItemSubscriptionAsync(req);

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
    SetItemSubscriptionRequest req = new SetItemSubscriptionRequest();

    //Send Request to Server and Get Response
    SetItemSubscriptionResponse res = api.SetItemSubscription(req);

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
    Dim req as new SetItemSubscriptionRequest()

    'Send Request to Server and Get Response
    Dim res As SetItemSubscriptionResponse = api.SetItemSubscription(req)

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
    $res = $api.SetItemSubscription($req);

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
    SetItemSubscriptionRequest req = new SetItemSubscriptionRequest();

    //Send Request to Server and Get Response
    SetItemSubscriptionResponse res = api.getExigoApiSoap().setItemSubscription(req, auth);

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

### SetItemPointAccount

> Set Item Point Account
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Items |
| REST | `PUT /3.0/item/pointaccount` |
| SOAP action | `https://api.exigo.com/SetItemPointAccount` |
| WSDL elements | `SetItemPointAccountRequest` → `SetItemPointAccountResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=SetItemPointAccount |

#### Input

**`SetItemPointAccountRequest`**

| Property | Type | Notes |
|---|---|---|
| `ItemCode` | `String` | Optional. Unique identifier for an item record. Either ItemCode or ItemID must be provided. |
| `ItemID` | `Int32` | Optional. Unique identifier for an item record. Either ItemCode or ItemID must be provided. |
| `PointAccounts` | `PointAccount[]` | Optional. Leave empty to remove all point accounts from the given item. |

**`PointAccount`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `PointAccountID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Increment` | `Decimal` |  |

#### Output

**`SetItemPointAccountResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/item/pointaccount HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
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
SOAPAction: "https://api.exigo.com/SetItemPointAccount"

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
    <SetItemPointAccountRequest xmlns="http://api.exigo.com/">
      <ItemCode>string</ItemCode>
      <ItemID>int</ItemID>
      <PointAccounts>
        <PointAccount>
          <PointAccountID>int</PointAccountID>
          <Increment>decimal</Increment>
        </PointAccount>
      </PointAccounts>
    </SetItemPointAccountRequest>
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
    <SetItemPointAccountResult xmlns="http://api.exigo.com/" />
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
    var req = new SetItemPointAccountRequest();

    //Send Request to Server and Get Response
    var res = await api.SetItemPointAccountAsync(req);

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
    SetItemPointAccountRequest req = new SetItemPointAccountRequest();

    //Send Request to Server and Get Response
    SetItemPointAccountResponse res = api.SetItemPointAccount(req);

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
    Dim req as new SetItemPointAccountRequest()

    'Send Request to Server and Get Response
    Dim res As SetItemPointAccountResponse = api.SetItemPointAccount(req)

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
    $res = $api.SetItemPointAccount($req);

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
    SetItemPointAccountRequest req = new SetItemPointAccountRequest();

    //Send Request to Server and Get Response
    SetItemPointAccountResponse res = api.getExigoApiSoap().setItemPointAccount(req, auth);

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
