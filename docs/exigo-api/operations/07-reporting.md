# Exigo API — Reporting

API version v2025.11.7.6. Crawled 2026-11-11 from https://api.exigo.com/3.0/. Back to [index](../README.md).

| Operation | REST | Summary |
|---|---|---|
| [GetDownline](#getdownline) | `GET /3.0/commissions/downline?treeType=1` | Gets nodes in a downline. |
| [GetUpline](#getupline) | `GET /3.0/commissions/upline?treeType=1` | Gets nodes in an upline. |
| [GetVolumes](#getvolumes) | `GET /3.0/commissions/volumes?periodType=1` | Returns volume records for a current period in a periodtype. |
| [GetRealTimeCommissions](#getrealtimecommissions) | `GET /3.0/commissions/realtime?customerID=1` | Returns realtime commissions available for open periods. |
| [GetRealTimeCommissionDetail](#getrealtimecommissiondetail) | `GET /3.0/commissions/realtime/detail?customerID=1` | Returns realtime commission detail for a customer/bonus. |
| [GetRankQualifications](#getrankqualifications) | `GET /3.0/qualification?customerID=1` | Returns rank qualification report card. |
| [GetQualificationOverrides](#getqualificationoverrides) | `GET /3.0/qualification/override?customerID=1` | Returns Customer Overrides |
| [SetQualificationOverride](#setqualificationoverride) | `PUT /3.0/qualification/override` | Create or Edit a Customer Override |
| [DeleteQualificationOverride](#deletequalificationoverride) | `DELETE /3.0/qualification/override` | Delete a Customer Override |
| [GetCustomReport](#getcustomreport) | `GET /3.0/report?reportID=1` | Returns a custom report in dataset format. |
| [GetCommissionReport](#getcommissionreport) | `GET /3.0/commissions?periodType=1` | Returns a commission report in json format. |
| [GetSQLReport](#getsqlreport) | `GET /3.0/sqlreport?reportID=1` | Returns a SQL report in dataset format. |

---
### GetDownline

> Gets nodes in a downline.

| | |
|---|---|
| Category | Reporting |
| REST | `GET /3.0/commissions/downline?treeType=1` |
| SOAP action | `https://api.exigo.com/GetDownline` |
| WSDL elements | `GetDownlineRequest` → `GetDownlineResult` |
| CSV output | Yes — `GET https://api.exigo.com/3.0/csv/?method=GetDownline&ApiLoginName=…&ApiPassword=…&ApiCompany=…` |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetDownline |

#### Input

**`GetDownlineRequest`**

| Property | Type | Notes |
|---|---|---|
| `TreeType` | `TreeType` | **Values:** `Enroller`, `UniLevel`, `Binary`, `Matrix`, `Stack` |
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `PeriodType` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| `PeriodID` | `Int32` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `MaxLevelDepth` | `Int32` |  |
| `CustomerTypes` | `Int32[]` | Classification of a customer as defined by the company.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Ranks` | `Int32[]` | **Lookup:** company-specific list (see company-lists.md) |
| `PayRanks` | `Int32[]` | **Lookup:** company-specific list (see company-lists.md) |
| `VolumeFilters` | `VolumeFilter[]` | **Lookup:** company-specific list (see company-lists.md) |
| `CustomerStatusTypes` | `Int32[]` |  |
| `BatchSize` | `Int32` | Optional. Defaults to 1000 at a time. |
| `SortByLevel` | `Boolean` |  |
| `BatchOffset` | `Int32` |  |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

**`VolumeFilter`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `VolumeID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Compare` | `NumericCompareType` | **Values:** `Equals`, `GreaterThan`, `LessThan` |
| &nbsp;&nbsp;↳ `Value` | `Decimal` |  |

#### Output

**`GetDownlineResponse`**

| Property | Type | Notes |
|---|---|---|
| `Nodes` | `NodeResponse[]` |  |
| `RecordCount` | `Int32` |  |

**`NodeResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| &nbsp;&nbsp;↳ `NodeID` | `Int32` |  |
| &nbsp;&nbsp;↳ `ParentID` | `Int32` |  |
| &nbsp;&nbsp;↳ `Level` | `Int32` |  |
| &nbsp;&nbsp;↳ `Position` | `Int32` |  |
| &nbsp;&nbsp;↳ `CustomerType` | `Int32` | Classification of a customer as defined by the company.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `CustomerStatus` | `Int32` | Current status of a customer as defined by the company.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `RankID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `PayRankID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `FirstName` | `String` |  |
| &nbsp;&nbsp;↳ `LastName` | `String` |  |
| &nbsp;&nbsp;↳ `Company` | `String` |  |
| &nbsp;&nbsp;↳ `Email` | `String` |  |
| &nbsp;&nbsp;↳ `Phone` | `String` |  |
| &nbsp;&nbsp;↳ `CreatedDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `Volume1` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume2` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume3` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume4` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume5` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume6` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume7` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume8` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume9` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume10` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume11` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume12` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume13` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume14` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume15` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume16` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume17` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume18` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume19` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume20` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume21` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume22` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume23` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume24` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume25` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume26` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume27` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume28` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume29` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume30` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume31` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume32` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume33` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume34` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume35` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume36` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume37` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume38` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume39` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume40` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume41` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume42` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume43` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume44` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume45` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume46` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume47` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume48` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume49` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume50` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume51` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume52` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume53` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume54` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume55` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume56` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume57` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume58` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume59` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume60` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume61` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume62` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume63` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume64` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume65` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume66` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume67` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume68` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume69` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume70` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume71` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume72` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume73` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume74` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume75` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume76` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume77` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume78` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume79` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume80` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume81` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume82` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume83` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume84` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume85` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume86` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume87` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume88` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume89` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume90` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume91` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume92` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume93` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume94` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume95` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume96` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume97` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume98` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume99` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume100` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume101` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume102` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume103` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume104` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume105` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume106` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume107` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume108` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume109` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume110` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume111` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume112` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume113` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume114` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume115` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume116` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume117` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume118` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume119` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume120` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume121` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume122` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume123` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume124` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume125` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume126` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume127` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume128` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume129` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume130` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume131` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume132` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume133` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume134` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume135` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume136` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume137` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume138` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume139` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume140` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume141` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume142` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume143` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume144` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume145` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume146` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume147` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume148` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume149` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume150` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume151` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume152` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume153` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume154` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume155` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume156` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume157` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume158` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume159` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume160` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume161` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume162` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume163` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume164` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume165` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume166` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume167` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume168` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume169` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume170` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume171` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume172` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume173` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume174` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume175` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume176` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume177` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume178` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume179` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume180` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume181` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume182` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume183` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume184` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume185` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume186` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume187` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume188` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume189` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume190` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume191` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume192` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume193` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume194` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume195` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume196` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume197` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume198` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume199` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume200` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `CustomerKey` | `String` | Unique alpha numeric identifier for customer record . |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/commissions/downline?treeType=1
  &customerID=1
  &periodType=1
  &periodID=1
  &maxLevelDepth=1
  &customerTypes=1
  &ranks=1
  &payRanks=1
  &volumeFilters[0][VolumeID]=1
  &volumeFilters[0][Compare]=1
  &volumeFilters[0][Value]=1
  &customerStatusTypes=1
  &sortByLevel=1
  &batchOffset=1
  &customerKey=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "nodes": null,
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
SOAPAction: "https://api.exigo.com/GetDownline"

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
    <GetDownlineRequest xmlns="http://api.exigo.com/">
      <TreeType>Enroller or UniLevel or Binary or Matrix or Stack</TreeType>
      <CustomerID>int</CustomerID>
      <PeriodType>int</PeriodType>
      <PeriodID>int</PeriodID>
      <MaxLevelDepth>int</MaxLevelDepth>
      <CustomerTypes>
        <int>int</int>
      </CustomerTypes>
      <Ranks>
        <int>int</int>
      </Ranks>
      <PayRanks>
        <int>int</int>
      </PayRanks>
      <VolumeFilters>
        <VolumeFilter>
          <VolumeID>int</VolumeID>
          <Compare>Equals or GreaterThan or LessThan</Compare>
          <Value>decimal</Value>
        </VolumeFilter>
      </VolumeFilters>
      <CustomerStatusTypes>
        <int>int</int>
      </CustomerStatusTypes>
      <BatchSize>int</BatchSize>
      <SortByLevel>boolean</SortByLevel>
      <BatchOffset>int</BatchOffset>
      <CustomerKey>string</CustomerKey>
    </GetDownlineRequest>
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
    <GetDownlineResult xmlns="http://api.exigo.com/">
      <Nodes>
        <NodeResponse>
          <CustomerID>int</CustomerID>
          <NodeID>int</NodeID>
          <ParentID>int</ParentID>
          <Level>int</Level>
          <Position>int</Position>
          <CustomerType>int</CustomerType>
          <CustomerStatus>int</CustomerStatus>
          <RankID>int</RankID>
          <PayRankID>int</PayRankID>
          <FirstName>string</FirstName>
          <LastName>string</LastName>
          <Company>string</Company>
          <Email>string</Email>
          <Phone>string</Phone>
          <CreatedDate>dateTime</CreatedDate>
          <Volume1>decimal</Volume1>
          <Volume2>decimal</Volume2>
          <Volume3>decimal</Volume3>
          <Volume4>decimal</Volume4>
          <Volume5>decimal</Volume5>
          <Volume6>decimal</Volume6>
          <Volume7>decimal</Volume7>
          <Volume8>decimal</Volume8>
          <Volume9>decimal</Volume9>
          <Volume10>decimal</Volume10>
          <Volume11>decimal</Volume11>
          <Volume12>decimal</Volume12>
          <Volume13>decimal</Volume13>
          <Volume14>decimal</Volume14>
          <Volume15>decimal</Volume15>
          <Volume16>decimal</Volume16>
          <Volume17>decimal</Volume17>
          <Volume18>decimal</Volume18>
          <Volume19>decimal</Volume19>
          <Volume20>decimal</Volume20>
          <Volume21>decimal</Volume21>
          <Volume22>decimal</Volume22>
          <Volume23>decimal</Volume23>
          <Volume24>decimal</Volume24>
          <Volume25>decimal</Volume25>
          <Volume26>decimal</Volume26>
          <Volume27>decimal</Volume27>
          <Volume28>decimal</Volume28>
          <Volume29>decimal</Volume29>
          <Volume30>decimal</Volume30>
          <Volume31>decimal</Volume31>
          <Volume32>decimal</Volume32>
          <Volume33>decimal</Volume33>
          <Volume34>decimal</Volume34>
          <Volume35>decimal</Volume35>
          <Volume36>decimal</Volume36>
          <Volume37>decimal</Volume37>
          <Volume38>decimal</Volume38>
          <Volume39>decimal</Volume39>
          <Volume40>decimal</Volume40>
          <Volume41>decimal</Volume41>
          <Volume42>decimal</Volume42>
          <Volume43>decimal</Volume43>
          <Volume44>decimal</Volume44>
          <Volume45>decimal</Volume45>
          <Volume46>decimal</Volume46>
          <Volume47>decimal</Volume47>
          <Volume48>decimal</Volume48>
          <Volume49>decimal</Volume49>
          <Volume50>decimal</Volume50>
          <Volume51>decimal</Volume51>
          <Volume52>decimal</Volume52>
          <Volume53>decimal</Volume53>
          <Volume54>decimal</Volume54>
          <Volume55>decimal</Volume55>
          <Volume56>decimal</Volume56>
          <Volume57>decimal</Volume57>
          <Volume58>decimal</Volume58>
          <Volume59>decimal</Volume59>
          <Volume60>decimal</Volume60>
          <Volume61>decimal</Volume61>
          <Volume62>decimal</Volume62>
          <Volume63>decimal</Volume63>
          <Volume64>decimal</Volume64>
          <Volume65>decimal</Volume65>
          <Volume66>decimal</Volume66>
          <Volume67>decimal</Volume67>
          <Volume68>decimal</Volume68>
          <Volume69>decimal</Volume69>
          <Volume70>decimal</Volume70>
          <Volume71>decimal</Volume71>
          <Volume72>decimal</Volume72>
          <Volume73>decimal</Volume73>
          <Volume74>decimal</Volume74>
          <Volume75>decimal</Volume75>
          <Volume76>decimal</Volume76>
          <Volume77>decimal</Volume77>
          <Volume78>decimal</Volume78>
          <Volume79>decimal</Volume79>
          <Volume80>decimal</Volume80>
          <Volume81>decimal</Volume81>
          <Volume82>decimal</Volume82>
          <Volume83>decimal</Volume83>
          <Volume84>decimal</Volume84>
          <Volume85>decimal</Volume85>
          <Volume86>decimal</Volume86>
          <Volume87>decimal</Volume87>
          <Volume88>decimal</Volume88>
          <Volume89>decimal</Volume89>
          <Volume90>decimal</Volume90>
          <Volume91>decimal</Volume91>
          <Volume92>decimal</Volume92>
          <Volume93>decimal</Volume93>
          <Volume94>decimal</Volume94>
          <Volume95>decimal</Volume95>
          <Volume96>decimal</Volume96>
          <Volume97>decimal</Volume97>
          <Volume98>decimal</Volume98>
          <Volume99>decimal</Volume99>
          <Volume100>decimal</Volume100>
          <Volume101>decimal</Volume101>
          <Volume102>decimal</Volume102>
          <Volume103>decimal</Volume103>
          <Volume104>decimal</Volume104>
          <Volume105>decimal</Volume105>
          <Volume106>decimal</Volume106>
          <Volume107>decimal</Volume107>
          <Volume108>decimal</Volume108>
          <Volume109>decimal</Volume109>
          <Volume110>decimal</Volume110>
          <Volume111>decimal</Volume111>
          <Volume112>decimal</Volume112>
          <Volume113>decimal</Volume113>
          <Volume114>decimal</Volume114>
          <Volume115>decimal</Volume115>
          <Volume116>decimal</Volume116>
          <Volume117>decimal</Volume117>
          <Volume118>decimal</Volume118>
          <Volume119>decimal</Volume119>
          <Volume120>decimal</Volume120>
          <Volume121>decimal</Volume121>
          <Volume122>decimal</Volume122>
          <Volume123>decimal</Volume123>
          <Volume124>decimal</Volume124>
          <Volume125>decimal</Volume125>
          <Volume126>decimal</Volume126>
          <Volume127>decimal</Volume127>
          <Volume128>decimal</Volume128>
          <Volume129>decimal</Volume129>
          <Volume130>decimal</Volume130>
          <Volume131>decimal</Volume131>
          <Volume132>decimal</Volume132>
          <Volume133>decimal</Volume133>
          <Volume134>decimal</Volume134>
          <Volume135>decimal</Volume135>
          <Volume136>decimal</Volume136>
          <Volume137>decimal</Volume137>
          <Volume138>decimal</Volume138>
          <Volume139>decimal</Volume139>
          <Volume140>decimal</Volume140>
          <Volume141>decimal</Volume141>
          <Volume142>decimal</Volume142>
          <Volume143>decimal</Volume143>
          <Volume144>decimal</Volume144>
          <Volume145>decimal</Volume145>
          <Volume146>decimal</Volume146>
          <Volume147>decimal</Volume147>
          <Volume148>decimal</Volume148>
          <Volume149>decimal</Volume149>
          <Volume150>decimal</Volume150>
          <Volume151>decimal</Volume151>
          <Volume152>decimal</Volume152>
          <Volume153>decimal</Volume153>
          <Volume154>decimal</Volume154>
          <Volume155>decimal</Volume155>
          <Volume156>decimal</Volume156>
          <Volume157>decimal</Volume157>
          <Volume158>decimal</Volume158>
          <Volume159>decimal</Volume159>
          <Volume160>decimal</Volume160>
          <Volume161>decimal</Volume161>
          <Volume162>decimal</Volume162>
          <Volume163>decimal</Volume163>
          <Volume164>decimal</Volume164>
          <Volume165>decimal</Volume165>
          <Volume166>decimal</Volume166>
          <Volume167>decimal</Volume167>
          <Volume168>decimal</Volume168>
          <Volume169>decimal</Volume169>
          <Volume170>decimal</Volume170>
          <Volume171>decimal</Volume171>
          <Volume172>decimal</Volume172>
          <Volume173>decimal</Volume173>
          <Volume174>decimal</Volume174>
          <Volume175>decimal</Volume175>
          <Volume176>decimal</Volume176>
          <Volume177>decimal</Volume177>
          <Volume178>decimal</Volume178>
          <Volume179>decimal</Volume179>
          <Volume180>decimal</Volume180>
          <Volume181>decimal</Volume181>
          <Volume182>decimal</Volume182>
          <Volume183>decimal</Volume183>
          <Volume184>decimal</Volume184>
          <Volume185>decimal</Volume185>
          <Volume186>decimal</Volume186>
          <Volume187>decimal</Volume187>
          <Volume188>decimal</Volume188>
          <Volume189>decimal</Volume189>
          <Volume190>decimal</Volume190>
          <Volume191>decimal</Volume191>
          <Volume192>decimal</Volume192>
          <Volume193>decimal</Volume193>
          <Volume194>decimal</Volume194>
          <Volume195>decimal</Volume195>
          <Volume196>decimal</Volume196>
          <Volume197>decimal</Volume197>
          <Volume198>decimal</Volume198>
          <Volume199>decimal</Volume199>
          <Volume200>decimal</Volume200>
          <CustomerKey>string</CustomerKey>
        </NodeResponse>
      </Nodes>
      <RecordCount>int</RecordCount>
    </GetDownlineResult>
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
    var req = new GetDownlineRequest();

    req.TreeType = TreeType.Enroller;
    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.PeriodType = 1;
    req.PeriodID = 1;
    req.MaxLevelDepth = 1;

    //Add CustomerTypes
    var customertypes = new List<Int32>();
    customertypes.Add(1);
    customertypes.Add(2);

    //Now attach the list to the request
    req.CustomerTypes = customertypes.ToArray();

    //Add Ranks
    var ranks = new List<Int32>();
    ranks.Add(1);
    ranks.Add(2);

    //Now attach the list to the request
    req.Ranks = ranks.ToArray();

    //Add PayRanks
    var payranks = new List<Int32>();
    payranks.Add(1);
    payranks.Add(2);

    //Now attach the list to the request
    req.PayRanks = payranks.ToArray();

    //Add VolumeFilters
    var volumefilters = new List<VolumeFilter>();

    var volumeFilter1 = new VolumeFilter();
    volumeFilter1.VolumeID = 1;
    volumeFilter1.Compare = NumericCompareType.Equals;
    volumeFilter1.Value = 1;
    volumefilters.Add(volumeFilter1);

    var volumeFilter2 = new VolumeFilter();
    volumeFilter2.VolumeID = 2;
    volumeFilter2.Compare = NumericCompareType.Equals;
    volumeFilter2.Value = 2;
    volumefilters.Add(volumeFilter2);

    //Now attach the list to the request
    req.VolumeFilters = volumefilters.ToArray();

    //Add CustomerStatusTypes
    var customerstatustypes = new List<Int32>();
    customerstatustypes.Add(1);
    customerstatustypes.Add(2);

    //Now attach the list to the request
    req.CustomerStatusTypes = customerstatustypes.ToArray();
    req.SortByLevel = true;
    req.BatchOffset = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.GetDownlineAsync(req);

    //Now examine the results:

    foreach (var node  in res.Nodes)
    {
        Console.WriteLine("CustomerID: {0}", node.CustomerID);
        Console.WriteLine("NodeID: {0}", node.NodeID);
        Console.WriteLine("ParentID: {0}", node.ParentID);
        Console.WriteLine("Level: {0}", node.Level);
        Console.WriteLine("Position: {0}", node.Position);
        Console.WriteLine("CustomerType: {0}", node.CustomerType);
        Console.WriteLine("CustomerStatus: {0}", node.CustomerStatus);
        Console.WriteLine("RankID: {0}", node.RankID);
        Console.WriteLine("PayRankID: {0}", node.PayRankID);
        Console.WriteLine("FirstName: {0}", node.FirstName);
        Console.WriteLine("LastName: {0}", node.LastName);
        Console.WriteLine("Company: {0}", node.Company);
        Console.WriteLine("Email: {0}", node.Email);
        Console.WriteLine("Phone: {0}", node.Phone);
        Console.WriteLine("CreatedDate: {0}", node.CreatedDate);
        Console.WriteLine("Volume1: {0}", node.Volume1);
        Console.WriteLine("Volume2: {0}", node.Volume2);
        Console.WriteLine("Volume3: {0}", node.Volume3);
        Console.WriteLine("Volume4: {0}", node.Volume4);
        Console.WriteLine("Volume5: {0}", node.Volume5);
        Console.WriteLine("Volume6: {0}", node.Volume6);
        Console.WriteLine("Volume7: {0}", node.Volume7);
        Console.WriteLine("Volume8: {0}", node.Volume8);
        Console.WriteLine("Volume9: {0}", node.Volume9);
        Console.WriteLine("Volume10: {0}", node.Volume10);
        Console.WriteLine("Volume11: {0}", node.Volume11);
        Console.WriteLine("Volume12: {0}", node.Volume12);
        Console.WriteLine("Volume13: {0}", node.Volume13);
        Console.WriteLine("Volume14: {0}", node.Volume14);
        Console.WriteLine("Volume15: {0}", node.Volume15);
        Console.WriteLine("Volume16: {0}", node.Volume16);
        Console.WriteLine("Volume17: {0}", node.Volume17);
        Console.WriteLine("Volume18: {0}", node.Volume18);
        Console.WriteLine("Volume19: {0}", node.Volume19);
        Console.WriteLine("Volume20: {0}", node.Volume20);
        Console.WriteLine("Volume21: {0}", node.Volume21);
        Console.WriteLine("Volume22: {0}", node.Volume22);
        Console.WriteLine("Volume23: {0}", node.Volume23);
        Console.WriteLine("Volume24: {0}", node.Volume24);
        Console.WriteLine("Volume25: {0}", node.Volume25);
        Console.WriteLine("Volume26: {0}", node.Volume26);
        Console.WriteLine("Volume27: {0}", node.Volume27);
        Console.WriteLine("Volume28: {0}", node.Volume28);
        Console.WriteLine("Volume29: {0}", node.Volume29);
        Console.WriteLine("Volume30: {0}", node.Volume30);
        Console.WriteLine("Volume31: {0}", node.Volume31);
        Console.WriteLine("Volume32: {0}", node.Volume32);
        Console.WriteLine("Volume33: {0}", node.Volume33);
        Console.WriteLine("Volume34: {0}", node.Volume34);
        Console.WriteLine("Volume35: {0}", node.Volume35);
        Console.WriteLine("Volume36: {0}", node.Volume36);
        Console.WriteLine("Volume37: {0}", node.Volume37);
        Console.WriteLine("Volume38: {0}", node.Volume38);
        Console.WriteLine("Volume39: {0}", node.Volume39);
        Console.WriteLine("Volume40: {0}", node.Volume40);
        Console.WriteLine("Volume41: {0}", node.Volume41);
        Console.WriteLine("Volume42: {0}", node.Volume42);
        Console.WriteLine("Volume43: {0}", node.Volume43);
        Console.WriteLine("Volume44: {0}", node.Volume44);
        Console.WriteLine("Volume45: {0}", node.Volume45);
        Console.WriteLine("Volume46: {0}", node.Volume46);
        Console.WriteLine("Volume47: {0}", node.Volume47);
        Console.WriteLine("Volume48: {0}", node.Volume48);
        Console.WriteLine("Volume49: {0}", node.Volume49);
        Console.WriteLine("Volume50: {0}", node.Volume50);
        Console.WriteLine("Volume51: {0}", node.Volume51);
        Console.WriteLine("Volume52: {0}", node.Volume52);
        Console.WriteLine("Volume53: {0}", node.Volume53);
        Console.WriteLine("Volume54: {0}", node.Volume54);
        Console.WriteLine("Volume55: {0}", node.Volume55);
        Console.WriteLine("Volume56: {0}", node.Volume56);
        Console.WriteLine("Volume57: {0}", node.Volume57);
        Console.WriteLine("Volume58: {0}", node.Volume58);
        Console.WriteLine("Volume59: {0}", node.Volume59);
        Console.WriteLine("Volume60: {0}", node.Volume60);
        Console.WriteLine("Volume61: {0}", node.Volume61);
        Console.WriteLine("Volume62: {0}", node.Volume62);
        Console.WriteLine("Volume63: {0}", node.Volume63);
        Console.WriteLine("Volume64: {0}", node.Volume64);
        Console.WriteLine("Volume65: {0}", node.Volume65);
        Console.WriteLine("Volume66: {0}", node.Volume66);
        Console.WriteLine("Volume67: {0}", node.Volume67);
        Console.WriteLine("Volume68: {0}", node.Volume68);
        Console.WriteLine("Volume69: {0}", node.Volume69);
        Console.WriteLine("Volume70: {0}", node.Volume70);
        Console.WriteLine("Volume71: {0}", node.Volume71);
        Console.WriteLine("Volume72: {0}", node.Volume72);
        Console.WriteLine("Volume73: {0}", node.Volume73);
        Console.WriteLine("Volume74: {0}", node.Volume74);
        Console.WriteLine("Volume75: {0}", node.Volume75);
        Console.WriteLine("Volume76: {0}", node.Volume76);
        Console.WriteLine("Volume77: {0}", node.Volume77);
        Console.WriteLine("Volume78: {0}", node.Volume78);
        Console.WriteLine("Volume79: {0}", node.Volume79);
        Console.WriteLine("Volume80: {0}", node.Volume80);
        Console.WriteLine("Volume81: {0}", node.Volume81);
        Console.WriteLine("Volume82: {0}", node.Volume82);
        Console.WriteLine("Volume83: {0}", node.Volume83);
        Console.WriteLine("Volume84: {0}", node.Volume84);
        Console.WriteLine("Volume85: {0}", node.Volume85);
        Console.WriteLine("Volume86: {0}", node.Volume86);
        Console.WriteLine("Volume87: {0}", node.Volume87);
        Console.WriteLine("Volume88: {0}", node.Volume88);
        Console.WriteLine("Volume89: {0}", node.Volume89);
        Console.WriteLine("Volume90: {0}", node.Volume90);
        Console.WriteLine("Volume91: {0}", node.Volume91);
        Console.WriteLine("Volume92: {0}", node.Volume92);
        Console.WriteLine("Volume93: {0}", node.Volume93);
        Console.WriteLine("Volume94: {0}", node.Volume94);
        Console.WriteLine("Volume95: {0}", node.Volume95);
        Console.WriteLine("Volume96: {0}", node.Volume96);
        Console.WriteLine("Volume97: {0}", node.Volume97);
        Console.WriteLine("Volume98: {0}", node.Volume98);
        Console.WriteLine("Volume99: {0}", node.Volume99);
        Console.WriteLine("Volume100: {0}", node.Volume100);
        Console.WriteLine("Volume101: {0}", node.Volume101);
        Console.WriteLine("Volume102: {0}", node.Volume102);
        Console.WriteLine("Volume103: {0}", node.Volume103);
        Console.WriteLine("Volume104: {0}", node.Volume104);
        Console.WriteLine("Volume105: {0}", node.Volume105);
        Console.WriteLine("Volume106: {0}", node.Volume106);
        Console.WriteLine("Volume107: {0}", node.Volume107);
        Console.WriteLine("Volume108: {0}", node.Volume108);
        Console.WriteLine("Volume109: {0}", node.Volume109);
        Console.WriteLine("Volume110: {0}", node.Volume110);
        Console.WriteLine("Volume111: {0}", node.Volume111);
        Console.WriteLine("Volume112: {0}", node.Volume112);
        Console.WriteLine("Volume113: {0}", node.Volume113);
        Console.WriteLine("Volume114: {0}", node.Volume114);
        Console.WriteLine("Volume115: {0}", node.Volume115);
        Console.WriteLine("Volume116: {0}", node.Volume116);
        Console.WriteLine("Volume117: {0}", node.Volume117);
        Console.WriteLine("Volume118: {0}", node.Volume118);
        Console.WriteLine("Volume119: {0}", node.Volume119);
        Console.WriteLine("Volume120: {0}", node.Volume120);
        Console.WriteLine("Volume121: {0}", node.Volume121);
        Console.WriteLine("Volume122: {0}", node.Volume122);
        Console.WriteLine("Volume123: {0}", node.Volume123);
        Console.WriteLine("Volume124: {0}", node.Volume124);
        Console.WriteLine("Volume125: {0}", node.Volume125);
        Console.WriteLine("Volume126: {0}", node.Volume126);
        Console.WriteLine("Volume127: {0}", node.Volume127);
        Console.WriteLine("Volume128: {0}", node.Volume128);
        Console.WriteLine("Volume129: {0}", node.Volume129);
        Console.WriteLine("Volume130: {0}", node.Volume130);
        Console.WriteLine("Volume131: {0}", node.Volume131);
        Console.WriteLine("Volume132: {0}", node.Volume132);
        Console.WriteLine("Volume133: {0}", node.Volume133);
        Console.WriteLine("Volume134: {0}", node.Volume134);
        Console.WriteLine("Volume135: {0}", node.Volume135);
        Console.WriteLine("Volume136: {0}", node.Volume136);
        Console.WriteLine("Volume137: {0}", node.Volume137);
        Console.WriteLine("Volume138: {0}", node.Volume138);
        Console.WriteLine("Volume139: {0}", node.Volume139);
        Console.WriteLine("Volume140: {0}", node.Volume140);
        Console.WriteLine("Volume141: {0}", node.Volume141);
        Console.WriteLine("Volume142: {0}", node.Volume142);
        Console.WriteLine("Volume143: {0}", node.Volume143);
        Console.WriteLine("Volume144: {0}", node.Volume144);
        Console.WriteLine("Volume145: {0}", node.Volume145);
        Console.WriteLine("Volume146: {0}", node.Volume146);
        Console.WriteLine("Volume147: {0}", node.Volume147);
        Console.WriteLine("Volume148: {0}", node.Volume148);
        Console.WriteLine("Volume149: {0}", node.Volume149);
        Console.WriteLine("Volume150: {0}", node.Volume150);
        Console.WriteLine("Volume151: {0}", node.Volume151);
        Console.WriteLine("Volume152: {0}", node.Volume152);
        Console.WriteLine("Volume153: {0}", node.Volume153);
        Console.WriteLine("Volume154: {0}", node.Volume154);
        Console.WriteLine("Volume155: {0}", node.Volume155);
        Console.WriteLine("Volume156: {0}", node.Volume156);
        Console.WriteLine("Volume157: {0}", node.Volume157);
        Console.WriteLine("Volume158: {0}", node.Volume158);
        Console.WriteLine("Volume159: {0}", node.Volume159);
        Console.WriteLine("Volume160: {0}", node.Volume160);
        Console.WriteLine("Volume161: {0}", node.Volume161);
        Console.WriteLine("Volume162: {0}", node.Volume162);
        Console.WriteLine("Volume163: {0}", node.Volume163);
        Console.WriteLine("Volume164: {0}", node.Volume164);
        Console.WriteLine("Volume165: {0}", node.Volume165);
        Console.WriteLine("Volume166: {0}", node.Volume166);
        Console.WriteLine("Volume167: {0}", node.Volume167);
        Console.WriteLine("Volume168: {0}", node.Volume168);
        Console.WriteLine("Volume169: {0}", node.Volume169);
        Console.WriteLine("Volume170: {0}", node.Volume170);
        Console.WriteLine("Volume171: {0}", node.Volume171);
        Console.WriteLine("Volume172: {0}", node.Volume172);
        Console.WriteLine("Volume173: {0}", node.Volume173);
        Console.WriteLine("Volume174: {0}", node.Volume174);
        Console.WriteLine("Volume175: {0}", node.Volume175);
        Console.WriteLine("Volume176: {0}", node.Volume176);
        Console.WriteLine("Volume177: {0}", node.Volume177);
        Console.WriteLine("Volume178: {0}", node.Volume178);
        Console.WriteLine("Volume179: {0}", node.Volume179);
        Console.WriteLine("Volume180: {0}", node.Volume180);
        Console.WriteLine("Volume181: {0}", node.Volume181);
        Console.WriteLine("Volume182: {0}", node.Volume182);
        Console.WriteLine("Volume183: {0}", node.Volume183);
        Console.WriteLine("Volume184: {0}", node.Volume184);
        Console.WriteLine("Volume185: {0}", node.Volume185);
        Console.WriteLine("Volume186: {0}", node.Volume186);
        Console.WriteLine("Volume187: {0}", node.Volume187);
        Console.WriteLine("Volume188: {0}", node.Volume188);
        Console.WriteLine("Volume189: {0}", node.Volume189);
        Console.WriteLine("Volume190: {0}", node.Volume190);
        Console.WriteLine("Volume191: {0}", node.Volume191);
        Console.WriteLine("Volume192: {0}", node.Volume192);
        Console.WriteLine("Volume193: {0}", node.Volume193);
        Console.WriteLine("Volume194: {0}", node.Volume194);
        Console.WriteLine("Volume195: {0}", node.Volume195);
        Console.WriteLine("Volume196: {0}", node.Volume196);
        Console.WriteLine("Volume197: {0}", node.Volume197);
        Console.WriteLine("Volume198: {0}", node.Volume198);
        Console.WriteLine("Volume199: {0}", node.Volume199);
        Console.WriteLine("Volume200: {0}", node.Volume200);
        Console.WriteLine("CustomerKey: {0}", node.CustomerKey);
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
    GetDownlineRequest req = new GetDownlineRequest();

    req.TreeType = TreeType.Enroller;
    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.PeriodType = 1;
    req.PeriodID = 1;
    req.MaxLevelDepth = 1;

    //Add CustomerTypes
    List<Int32> customertypes = new List<Int32>();
    customertypes.Add(1);
    customertypes.Add(2);

    //Now attach the list to the request
    req.CustomerTypes = customertypes.ToArray();

    //Add Ranks
    List<Int32> ranks = new List<Int32>();
    ranks.Add(1);
    ranks.Add(2);

    //Now attach the list to the request
    req.Ranks = ranks.ToArray();

    //Add PayRanks
    List<Int32> payranks = new List<Int32>();
    payranks.Add(1);
    payranks.Add(2);

    //Now attach the list to the request
    req.PayRanks = payranks.ToArray();

    //Add VolumeFilters
    List<VolumeFilter> volumefilters = new List<VolumeFilter>();

    VolumeFilter volumeFilter1 = new VolumeFilter();
    volumeFilter1.VolumeID = 1;
    volumeFilter1.Compare = NumericCompareType.Equals;
    volumeFilter1.Value = 1;
    volumefilters.Add(volumeFilter1);

    VolumeFilter volumeFilter2 = new VolumeFilter();
    volumeFilter2.VolumeID = 2;
    volumeFilter2.Compare = NumericCompareType.Equals;
    volumeFilter2.Value = 2;
    volumefilters.Add(volumeFilter2);

    //Now attach the list to the request
    req.VolumeFilters = volumefilters.ToArray();

    //Add CustomerStatusTypes
    List<Int32> customerstatustypes = new List<Int32>();
    customerstatustypes.Add(1);
    customerstatustypes.Add(2);

    //Now attach the list to the request
    req.CustomerStatusTypes = customerstatustypes.ToArray();
    req.SortByLevel = true;
    req.BatchOffset = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    GetDownlineResponse res = api.GetDownline(req);

    //Now examine the results:

    foreach (NodeResponse node  in res.Nodes)
    {
        Console.WriteLine("CustomerID: {0}", node.CustomerID);
        Console.WriteLine("NodeID: {0}", node.NodeID);
        Console.WriteLine("ParentID: {0}", node.ParentID);
        Console.WriteLine("Level: {0}", node.Level);
        Console.WriteLine("Position: {0}", node.Position);
        Console.WriteLine("CustomerType: {0}", node.CustomerType);
        Console.WriteLine("CustomerStatus: {0}", node.CustomerStatus);
        Console.WriteLine("RankID: {0}", node.RankID);
        Console.WriteLine("PayRankID: {0}", node.PayRankID);
        Console.WriteLine("FirstName: {0}", node.FirstName);
        Console.WriteLine("LastName: {0}", node.LastName);
        Console.WriteLine("Company: {0}", node.Company);
        Console.WriteLine("Email: {0}", node.Email);
        Console.WriteLine("Phone: {0}", node.Phone);
        Console.WriteLine("CreatedDate: {0}", node.CreatedDate);
        Console.WriteLine("Volume1: {0}", node.Volume1);
        Console.WriteLine("Volume2: {0}", node.Volume2);
        Console.WriteLine("Volume3: {0}", node.Volume3);
        Console.WriteLine("Volume4: {0}", node.Volume4);
        Console.WriteLine("Volume5: {0}", node.Volume5);
        Console.WriteLine("Volume6: {0}", node.Volume6);
        Console.WriteLine("Volume7: {0}", node.Volume7);
        Console.WriteLine("Volume8: {0}", node.Volume8);
        Console.WriteLine("Volume9: {0}", node.Volume9);
        Console.WriteLine("Volume10: {0}", node.Volume10);
        Console.WriteLine("Volume11: {0}", node.Volume11);
        Console.WriteLine("Volume12: {0}", node.Volume12);
        Console.WriteLine("Volume13: {0}", node.Volume13);
        Console.WriteLine("Volume14: {0}", node.Volume14);
        Console.WriteLine("Volume15: {0}", node.Volume15);
        Console.WriteLine("Volume16: {0}", node.Volume16);
        Console.WriteLine("Volume17: {0}", node.Volume17);
        Console.WriteLine("Volume18: {0}", node.Volume18);
        Console.WriteLine("Volume19: {0}", node.Volume19);
        Console.WriteLine("Volume20: {0}", node.Volume20);
        Console.WriteLine("Volume21: {0}", node.Volume21);
        Console.WriteLine("Volume22: {0}", node.Volume22);
        Console.WriteLine("Volume23: {0}", node.Volume23);
        Console.WriteLine("Volume24: {0}", node.Volume24);
        Console.WriteLine("Volume25: {0}", node.Volume25);
        Console.WriteLine("Volume26: {0}", node.Volume26);
        Console.WriteLine("Volume27: {0}", node.Volume27);
        Console.WriteLine("Volume28: {0}", node.Volume28);
        Console.WriteLine("Volume29: {0}", node.Volume29);
        Console.WriteLine("Volume30: {0}", node.Volume30);
        Console.WriteLine("Volume31: {0}", node.Volume31);
        Console.WriteLine("Volume32: {0}", node.Volume32);
        Console.WriteLine("Volume33: {0}", node.Volume33);
        Console.WriteLine("Volume34: {0}", node.Volume34);
        Console.WriteLine("Volume35: {0}", node.Volume35);
        Console.WriteLine("Volume36: {0}", node.Volume36);
        Console.WriteLine("Volume37: {0}", node.Volume37);
        Console.WriteLine("Volume38: {0}", node.Volume38);
        Console.WriteLine("Volume39: {0}", node.Volume39);
        Console.WriteLine("Volume40: {0}", node.Volume40);
        Console.WriteLine("Volume41: {0}", node.Volume41);
        Console.WriteLine("Volume42: {0}", node.Volume42);
        Console.WriteLine("Volume43: {0}", node.Volume43);
        Console.WriteLine("Volume44: {0}", node.Volume44);
        Console.WriteLine("Volume45: {0}", node.Volume45);
        Console.WriteLine("Volume46: {0}", node.Volume46);
        Console.WriteLine("Volume47: {0}", node.Volume47);
        Console.WriteLine("Volume48: {0}", node.Volume48);
        Console.WriteLine("Volume49: {0}", node.Volume49);
        Console.WriteLine("Volume50: {0}", node.Volume50);
        Console.WriteLine("Volume51: {0}", node.Volume51);
        Console.WriteLine("Volume52: {0}", node.Volume52);
        Console.WriteLine("Volume53: {0}", node.Volume53);
        Console.WriteLine("Volume54: {0}", node.Volume54);
        Console.WriteLine("Volume55: {0}", node.Volume55);
        Console.WriteLine("Volume56: {0}", node.Volume56);
        Console.WriteLine("Volume57: {0}", node.Volume57);
        Console.WriteLine("Volume58: {0}", node.Volume58);
        Console.WriteLine("Volume59: {0}", node.Volume59);
        Console.WriteLine("Volume60: {0}", node.Volume60);
        Console.WriteLine("Volume61: {0}", node.Volume61);
        Console.WriteLine("Volume62: {0}", node.Volume62);
        Console.WriteLine("Volume63: {0}", node.Volume63);
        Console.WriteLine("Volume64: {0}", node.Volume64);
        Console.WriteLine("Volume65: {0}", node.Volume65);
        Console.WriteLine("Volume66: {0}", node.Volume66);
        Console.WriteLine("Volume67: {0}", node.Volume67);
        Console.WriteLine("Volume68: {0}", node.Volume68);
        Console.WriteLine("Volume69: {0}", node.Volume69);
        Console.WriteLine("Volume70: {0}", node.Volume70);
        Console.WriteLine("Volume71: {0}", node.Volume71);
        Console.WriteLine("Volume72: {0}", node.Volume72);
        Console.WriteLine("Volume73: {0}", node.Volume73);
        Console.WriteLine("Volume74: {0}", node.Volume74);
        Console.WriteLine("Volume75: {0}", node.Volume75);
        Console.WriteLine("Volume76: {0}", node.Volume76);
        Console.WriteLine("Volume77: {0}", node.Volume77);
        Console.WriteLine("Volume78: {0}", node.Volume78);
        Console.WriteLine("Volume79: {0}", node.Volume79);
        Console.WriteLine("Volume80: {0}", node.Volume80);
        Console.WriteLine("Volume81: {0}", node.Volume81);
        Console.WriteLine("Volume82: {0}", node.Volume82);
        Console.WriteLine("Volume83: {0}", node.Volume83);
        Console.WriteLine("Volume84: {0}", node.Volume84);
        Console.WriteLine("Volume85: {0}", node.Volume85);
        Console.WriteLine("Volume86: {0}", node.Volume86);
        Console.WriteLine("Volume87: {0}", node.Volume87);
        Console.WriteLine("Volume88: {0}", node.Volume88);
        Console.WriteLine("Volume89: {0}", node.Volume89);
        Console.WriteLine("Volume90: {0}", node.Volume90);
        Console.WriteLine("Volume91: {0}", node.Volume91);
        Console.WriteLine("Volume92: {0}", node.Volume92);
        Console.WriteLine("Volume93: {0}", node.Volume93);
        Console.WriteLine("Volume94: {0}", node.Volume94);
        Console.WriteLine("Volume95: {0}", node.Volume95);
        Console.WriteLine("Volume96: {0}", node.Volume96);
        Console.WriteLine("Volume97: {0}", node.Volume97);
        Console.WriteLine("Volume98: {0}", node.Volume98);
        Console.WriteLine("Volume99: {0}", node.Volume99);
        Console.WriteLine("Volume100: {0}", node.Volume100);
        Console.WriteLine("Volume101: {0}", node.Volume101);
        Console.WriteLine("Volume102: {0}", node.Volume102);
        Console.WriteLine("Volume103: {0}", node.Volume103);
        Console.WriteLine("Volume104: {0}", node.Volume104);
        Console.WriteLine("Volume105: {0}", node.Volume105);
        Console.WriteLine("Volume106: {0}", node.Volume106);
        Console.WriteLine("Volume107: {0}", node.Volume107);
        Console.WriteLine("Volume108: {0}", node.Volume108);
        Console.WriteLine("Volume109: {0}", node.Volume109);
        Console.WriteLine("Volume110: {0}", node.Volume110);
        Console.WriteLine("Volume111: {0}", node.Volume111);
        Console.WriteLine("Volume112: {0}", node.Volume112);
        Console.WriteLine("Volume113: {0}", node.Volume113);
        Console.WriteLine("Volume114: {0}", node.Volume114);
        Console.WriteLine("Volume115: {0}", node.Volume115);
        Console.WriteLine("Volume116: {0}", node.Volume116);
        Console.WriteLine("Volume117: {0}", node.Volume117);
        Console.WriteLine("Volume118: {0}", node.Volume118);
        Console.WriteLine("Volume119: {0}", node.Volume119);
        Console.WriteLine("Volume120: {0}", node.Volume120);
        Console.WriteLine("Volume121: {0}", node.Volume121);
        Console.WriteLine("Volume122: {0}", node.Volume122);
        Console.WriteLine("Volume123: {0}", node.Volume123);
        Console.WriteLine("Volume124: {0}", node.Volume124);
        Console.WriteLine("Volume125: {0}", node.Volume125);
        Console.WriteLine("Volume126: {0}", node.Volume126);
        Console.WriteLine("Volume127: {0}", node.Volume127);
        Console.WriteLine("Volume128: {0}", node.Volume128);
        Console.WriteLine("Volume129: {0}", node.Volume129);
        Console.WriteLine("Volume130: {0}", node.Volume130);
        Console.WriteLine("Volume131: {0}", node.Volume131);
        Console.WriteLine("Volume132: {0}", node.Volume132);
        Console.WriteLine("Volume133: {0}", node.Volume133);
        Console.WriteLine("Volume134: {0}", node.Volume134);
        Console.WriteLine("Volume135: {0}", node.Volume135);
        Console.WriteLine("Volume136: {0}", node.Volume136);
        Console.WriteLine("Volume137: {0}", node.Volume137);
        Console.WriteLine("Volume138: {0}", node.Volume138);
        Console.WriteLine("Volume139: {0}", node.Volume139);
        Console.WriteLine("Volume140: {0}", node.Volume140);
        Console.WriteLine("Volume141: {0}", node.Volume141);
        Console.WriteLine("Volume142: {0}", node.Volume142);
        Console.WriteLine("Volume143: {0}", node.Volume143);
        Console.WriteLine("Volume144: {0}", node.Volume144);
        Console.WriteLine("Volume145: {0}", node.Volume145);
        Console.WriteLine("Volume146: {0}", node.Volume146);
        Console.WriteLine("Volume147: {0}", node.Volume147);
        Console.WriteLine("Volume148: {0}", node.Volume148);
        Console.WriteLine("Volume149: {0}", node.Volume149);
        Console.WriteLine("Volume150: {0}", node.Volume150);
        Console.WriteLine("Volume151: {0}", node.Volume151);
        Console.WriteLine("Volume152: {0}", node.Volume152);
        Console.WriteLine("Volume153: {0}", node.Volume153);
        Console.WriteLine("Volume154: {0}", node.Volume154);
        Console.WriteLine("Volume155: {0}", node.Volume155);
        Console.WriteLine("Volume156: {0}", node.Volume156);
        Console.WriteLine("Volume157: {0}", node.Volume157);
        Console.WriteLine("Volume158: {0}", node.Volume158);
        Console.WriteLine("Volume159: {0}", node.Volume159);
        Console.WriteLine("Volume160: {0}", node.Volume160);
        Console.WriteLine("Volume161: {0}", node.Volume161);
        Console.WriteLine("Volume162: {0}", node.Volume162);
        Console.WriteLine("Volume163: {0}", node.Volume163);
        Console.WriteLine("Volume164: {0}", node.Volume164);
        Console.WriteLine("Volume165: {0}", node.Volume165);
        Console.WriteLine("Volume166: {0}", node.Volume166);
        Console.WriteLine("Volume167: {0}", node.Volume167);
        Console.WriteLine("Volume168: {0}", node.Volume168);
        Console.WriteLine("Volume169: {0}", node.Volume169);
        Console.WriteLine("Volume170: {0}", node.Volume170);
        Console.WriteLine("Volume171: {0}", node.Volume171);
        Console.WriteLine("Volume172: {0}", node.Volume172);
        Console.WriteLine("Volume173: {0}", node.Volume173);
        Console.WriteLine("Volume174: {0}", node.Volume174);
        Console.WriteLine("Volume175: {0}", node.Volume175);
        Console.WriteLine("Volume176: {0}", node.Volume176);
        Console.WriteLine("Volume177: {0}", node.Volume177);
        Console.WriteLine("Volume178: {0}", node.Volume178);
        Console.WriteLine("Volume179: {0}", node.Volume179);
        Console.WriteLine("Volume180: {0}", node.Volume180);
        Console.WriteLine("Volume181: {0}", node.Volume181);
        Console.WriteLine("Volume182: {0}", node.Volume182);
        Console.WriteLine("Volume183: {0}", node.Volume183);
        Console.WriteLine("Volume184: {0}", node.Volume184);
        Console.WriteLine("Volume185: {0}", node.Volume185);
        Console.WriteLine("Volume186: {0}", node.Volume186);
        Console.WriteLine("Volume187: {0}", node.Volume187);
        Console.WriteLine("Volume188: {0}", node.Volume188);
        Console.WriteLine("Volume189: {0}", node.Volume189);
        Console.WriteLine("Volume190: {0}", node.Volume190);
        Console.WriteLine("Volume191: {0}", node.Volume191);
        Console.WriteLine("Volume192: {0}", node.Volume192);
        Console.WriteLine("Volume193: {0}", node.Volume193);
        Console.WriteLine("Volume194: {0}", node.Volume194);
        Console.WriteLine("Volume195: {0}", node.Volume195);
        Console.WriteLine("Volume196: {0}", node.Volume196);
        Console.WriteLine("Volume197: {0}", node.Volume197);
        Console.WriteLine("Volume198: {0}", node.Volume198);
        Console.WriteLine("Volume199: {0}", node.Volume199);
        Console.WriteLine("Volume200: {0}", node.Volume200);
        Console.WriteLine("CustomerKey: {0}", node.CustomerKey);
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
    Dim req as new GetDownlineRequest()

    req.TreeType = TreeType.Enroller
    req.CustomerID = 1
    req.PeriodType = 1
    req.PeriodID = 1
    req.MaxLevelDepth = 1

    'Add CustomerTypes
    Dim customertypes As New List(Of Int32)()
    customertypes.Add(1)
    customertypes.Add(2)

    'Now attach the list to the request
    req.CustomerTypes = customertypes.ToArray()

    'Add Ranks
    Dim ranks As New List(Of Int32)()
    ranks.Add(1)
    ranks.Add(2)

    'Now attach the list to the request
    req.Ranks = ranks.ToArray()

    'Add PayRanks
    Dim payranks As New List(Of Int32)()
    payranks.Add(1)
    payranks.Add(2)

    'Now attach the list to the request
    req.PayRanks = payranks.ToArray()

    'Add VolumeFilters
    Dim volumefilters As New List(Of VolumeFilter)()

    Dim volumeFilter1 as new VolumeFilter()
    volumeFilter1.VolumeID = 1
    volumeFilter1.Compare = NumericCompareType.Equals
    volumeFilter1.Value = 1
    volumefilters.Add(volumeFilter1)

    Dim volumeFilter2 as new VolumeFilter()
    volumeFilter2.VolumeID = 2
    volumeFilter2.Compare = NumericCompareType.Equals
    volumeFilter2.Value = 2
    volumefilters.Add(volumeFilter2)

    'Now attach the list to the request
    req.VolumeFilters = volumefilters.ToArray()

    'Add CustomerStatusTypes
    Dim customerstatustypes As New List(Of Int32)()
    customerstatustypes.Add(1)
    customerstatustypes.Add(2)

    'Now attach the list to the request
    req.CustomerStatusTypes = customerstatustypes.ToArray()
    req.SortByLevel = true
    req.BatchOffset = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As GetDownlineResponse = api.GetDownline(req)

    'Now examine the results:

    For Each node As NodeResponse In res.Nodes
        Console.WriteLine("CustomerID: {0}", node.CustomerID)
        Console.WriteLine("NodeID: {0}", node.NodeID)
        Console.WriteLine("ParentID: {0}", node.ParentID)
        Console.WriteLine("Level: {0}", node.Level)
        Console.WriteLine("Position: {0}", node.Position)
        Console.WriteLine("CustomerType: {0}", node.CustomerType)
        Console.WriteLine("CustomerStatus: {0}", node.CustomerStatus)
        Console.WriteLine("RankID: {0}", node.RankID)
        Console.WriteLine("PayRankID: {0}", node.PayRankID)
        Console.WriteLine("FirstName: {0}", node.FirstName)
        Console.WriteLine("LastName: {0}", node.LastName)
        Console.WriteLine("Company: {0}", node.Company)
        Console.WriteLine("Email: {0}", node.Email)
        Console.WriteLine("Phone: {0}", node.Phone)
        Console.WriteLine("CreatedDate: {0}", node.CreatedDate)
        Console.WriteLine("Volume1: {0}", node.Volume1)
        Console.WriteLine("Volume2: {0}", node.Volume2)
        Console.WriteLine("Volume3: {0}", node.Volume3)
        Console.WriteLine("Volume4: {0}", node.Volume4)
        Console.WriteLine("Volume5: {0}", node.Volume5)
        Console.WriteLine("Volume6: {0}", node.Volume6)
        Console.WriteLine("Volume7: {0}", node.Volume7)
        Console.WriteLine("Volume8: {0}", node.Volume8)
        Console.WriteLine("Volume9: {0}", node.Volume9)
        Console.WriteLine("Volume10: {0}", node.Volume10)
        Console.WriteLine("Volume11: {0}", node.Volume11)
        Console.WriteLine("Volume12: {0}", node.Volume12)
        Console.WriteLine("Volume13: {0}", node.Volume13)
        Console.WriteLine("Volume14: {0}", node.Volume14)
        Console.WriteLine("Volume15: {0}", node.Volume15)
        Console.WriteLine("Volume16: {0}", node.Volume16)
        Console.WriteLine("Volume17: {0}", node.Volume17)
        Console.WriteLine("Volume18: {0}", node.Volume18)
        Console.WriteLine("Volume19: {0}", node.Volume19)
        Console.WriteLine("Volume20: {0}", node.Volume20)
        Console.WriteLine("Volume21: {0}", node.Volume21)
        Console.WriteLine("Volume22: {0}", node.Volume22)
        Console.WriteLine("Volume23: {0}", node.Volume23)
        Console.WriteLine("Volume24: {0}", node.Volume24)
        Console.WriteLine("Volume25: {0}", node.Volume25)
        Console.WriteLine("Volume26: {0}", node.Volume26)
        Console.WriteLine("Volume27: {0}", node.Volume27)
        Console.WriteLine("Volume28: {0}", node.Volume28)
        Console.WriteLine("Volume29: {0}", node.Volume29)
        Console.WriteLine("Volume30: {0}", node.Volume30)
        Console.WriteLine("Volume31: {0}", node.Volume31)
        Console.WriteLine("Volume32: {0}", node.Volume32)
        Console.WriteLine("Volume33: {0}", node.Volume33)
        Console.WriteLine("Volume34: {0}", node.Volume34)
        Console.WriteLine("Volume35: {0}", node.Volume35)
        Console.WriteLine("Volume36: {0}", node.Volume36)
        Console.WriteLine("Volume37: {0}", node.Volume37)
        Console.WriteLine("Volume38: {0}", node.Volume38)
        Console.WriteLine("Volume39: {0}", node.Volume39)
        Console.WriteLine("Volume40: {0}", node.Volume40)
        Console.WriteLine("Volume41: {0}", node.Volume41)
        Console.WriteLine("Volume42: {0}", node.Volume42)
        Console.WriteLine("Volume43: {0}", node.Volume43)
        Console.WriteLine("Volume44: {0}", node.Volume44)
        Console.WriteLine("Volume45: {0}", node.Volume45)
        Console.WriteLine("Volume46: {0}", node.Volume46)
        Console.WriteLine("Volume47: {0}", node.Volume47)
        Console.WriteLine("Volume48: {0}", node.Volume48)
        Console.WriteLine("Volume49: {0}", node.Volume49)
        Console.WriteLine("Volume50: {0}", node.Volume50)
        Console.WriteLine("Volume51: {0}", node.Volume51)
        Console.WriteLine("Volume52: {0}", node.Volume52)
        Console.WriteLine("Volume53: {0}", node.Volume53)
        Console.WriteLine("Volume54: {0}", node.Volume54)
        Console.WriteLine("Volume55: {0}", node.Volume55)
        Console.WriteLine("Volume56: {0}", node.Volume56)
        Console.WriteLine("Volume57: {0}", node.Volume57)
        Console.WriteLine("Volume58: {0}", node.Volume58)
        Console.WriteLine("Volume59: {0}", node.Volume59)
        Console.WriteLine("Volume60: {0}", node.Volume60)
        Console.WriteLine("Volume61: {0}", node.Volume61)
        Console.WriteLine("Volume62: {0}", node.Volume62)
        Console.WriteLine("Volume63: {0}", node.Volume63)
        Console.WriteLine("Volume64: {0}", node.Volume64)
        Console.WriteLine("Volume65: {0}", node.Volume65)
        Console.WriteLine("Volume66: {0}", node.Volume66)
        Console.WriteLine("Volume67: {0}", node.Volume67)
        Console.WriteLine("Volume68: {0}", node.Volume68)
        Console.WriteLine("Volume69: {0}", node.Volume69)
        Console.WriteLine("Volume70: {0}", node.Volume70)
        Console.WriteLine("Volume71: {0}", node.Volume71)
        Console.WriteLine("Volume72: {0}", node.Volume72)
        Console.WriteLine("Volume73: {0}", node.Volume73)
        Console.WriteLine("Volume74: {0}", node.Volume74)
        Console.WriteLine("Volume75: {0}", node.Volume75)
        Console.WriteLine("Volume76: {0}", node.Volume76)
        Console.WriteLine("Volume77: {0}", node.Volume77)
        Console.WriteLine("Volume78: {0}", node.Volume78)
        Console.WriteLine("Volume79: {0}", node.Volume79)
        Console.WriteLine("Volume80: {0}", node.Volume80)
        Console.WriteLine("Volume81: {0}", node.Volume81)
        Console.WriteLine("Volume82: {0}", node.Volume82)
        Console.WriteLine("Volume83: {0}", node.Volume83)
        Console.WriteLine("Volume84: {0}", node.Volume84)
        Console.WriteLine("Volume85: {0}", node.Volume85)
        Console.WriteLine("Volume86: {0}", node.Volume86)
        Console.WriteLine("Volume87: {0}", node.Volume87)
        Console.WriteLine("Volume88: {0}", node.Volume88)
        Console.WriteLine("Volume89: {0}", node.Volume89)
        Console.WriteLine("Volume90: {0}", node.Volume90)
        Console.WriteLine("Volume91: {0}", node.Volume91)
        Console.WriteLine("Volume92: {0}", node.Volume92)
        Console.WriteLine("Volume93: {0}", node.Volume93)
        Console.WriteLine("Volume94: {0}", node.Volume94)
        Console.WriteLine("Volume95: {0}", node.Volume95)
        Console.WriteLine("Volume96: {0}", node.Volume96)
        Console.WriteLine("Volume97: {0}", node.Volume97)
        Console.WriteLine("Volume98: {0}", node.Volume98)
        Console.WriteLine("Volume99: {0}", node.Volume99)
        Console.WriteLine("Volume100: {0}", node.Volume100)
        Console.WriteLine("Volume101: {0}", node.Volume101)
        Console.WriteLine("Volume102: {0}", node.Volume102)
        Console.WriteLine("Volume103: {0}", node.Volume103)
        Console.WriteLine("Volume104: {0}", node.Volume104)
        Console.WriteLine("Volume105: {0}", node.Volume105)
        Console.WriteLine("Volume106: {0}", node.Volume106)
        Console.WriteLine("Volume107: {0}", node.Volume107)
        Console.WriteLine("Volume108: {0}", node.Volume108)
        Console.WriteLine("Volume109: {0}", node.Volume109)
        Console.WriteLine("Volume110: {0}", node.Volume110)
        Console.WriteLine("Volume111: {0}", node.Volume111)
        Console.WriteLine("Volume112: {0}", node.Volume112)
        Console.WriteLine("Volume113: {0}", node.Volume113)
        Console.WriteLine("Volume114: {0}", node.Volume114)
        Console.WriteLine("Volume115: {0}", node.Volume115)
        Console.WriteLine("Volume116: {0}", node.Volume116)
        Console.WriteLine("Volume117: {0}", node.Volume117)
        Console.WriteLine("Volume118: {0}", node.Volume118)
        Console.WriteLine("Volume119: {0}", node.Volume119)
        Console.WriteLine("Volume120: {0}", node.Volume120)
        Console.WriteLine("Volume121: {0}", node.Volume121)
        Console.WriteLine("Volume122: {0}", node.Volume122)
        Console.WriteLine("Volume123: {0}", node.Volume123)
        Console.WriteLine("Volume124: {0}", node.Volume124)
        Console.WriteLine("Volume125: {0}", node.Volume125)
        Console.WriteLine("Volume126: {0}", node.Volume126)
        Console.WriteLine("Volume127: {0}", node.Volume127)
        Console.WriteLine("Volume128: {0}", node.Volume128)
        Console.WriteLine("Volume129: {0}", node.Volume129)
        Console.WriteLine("Volume130: {0}", node.Volume130)
        Console.WriteLine("Volume131: {0}", node.Volume131)
        Console.WriteLine("Volume132: {0}", node.Volume132)
        Console.WriteLine("Volume133: {0}", node.Volume133)
        Console.WriteLine("Volume134: {0}", node.Volume134)
        Console.WriteLine("Volume135: {0}", node.Volume135)
        Console.WriteLine("Volume136: {0}", node.Volume136)
        Console.WriteLine("Volume137: {0}", node.Volume137)
        Console.WriteLine("Volume138: {0}", node.Volume138)
        Console.WriteLine("Volume139: {0}", node.Volume139)
        Console.WriteLine("Volume140: {0}", node.Volume140)
        Console.WriteLine("Volume141: {0}", node.Volume141)
        Console.WriteLine("Volume142: {0}", node.Volume142)
        Console.WriteLine("Volume143: {0}", node.Volume143)
        Console.WriteLine("Volume144: {0}", node.Volume144)
        Console.WriteLine("Volume145: {0}", node.Volume145)
        Console.WriteLine("Volume146: {0}", node.Volume146)
        Console.WriteLine("Volume147: {0}", node.Volume147)
        Console.WriteLine("Volume148: {0}", node.Volume148)
        Console.WriteLine("Volume149: {0}", node.Volume149)
        Console.WriteLine("Volume150: {0}", node.Volume150)
        Console.WriteLine("Volume151: {0}", node.Volume151)
        Console.WriteLine("Volume152: {0}", node.Volume152)
        Console.WriteLine("Volume153: {0}", node.Volume153)
        Console.WriteLine("Volume154: {0}", node.Volume154)
        Console.WriteLine("Volume155: {0}", node.Volume155)
        Console.WriteLine("Volume156: {0}", node.Volume156)
        Console.WriteLine("Volume157: {0}", node.Volume157)
        Console.WriteLine("Volume158: {0}", node.Volume158)
        Console.WriteLine("Volume159: {0}", node.Volume159)
        Console.WriteLine("Volume160: {0}", node.Volume160)
        Console.WriteLine("Volume161: {0}", node.Volume161)
        Console.WriteLine("Volume162: {0}", node.Volume162)
        Console.WriteLine("Volume163: {0}", node.Volume163)
        Console.WriteLine("Volume164: {0}", node.Volume164)
        Console.WriteLine("Volume165: {0}", node.Volume165)
        Console.WriteLine("Volume166: {0}", node.Volume166)
        Console.WriteLine("Volume167: {0}", node.Volume167)
        Console.WriteLine("Volume168: {0}", node.Volume168)
        Console.WriteLine("Volume169: {0}", node.Volume169)
        Console.WriteLine("Volume170: {0}", node.Volume170)
        Console.WriteLine("Volume171: {0}", node.Volume171)
        Console.WriteLine("Volume172: {0}", node.Volume172)
        Console.WriteLine("Volume173: {0}", node.Volume173)
        Console.WriteLine("Volume174: {0}", node.Volume174)
        Console.WriteLine("Volume175: {0}", node.Volume175)
        Console.WriteLine("Volume176: {0}", node.Volume176)
        Console.WriteLine("Volume177: {0}", node.Volume177)
        Console.WriteLine("Volume178: {0}", node.Volume178)
        Console.WriteLine("Volume179: {0}", node.Volume179)
        Console.WriteLine("Volume180: {0}", node.Volume180)
        Console.WriteLine("Volume181: {0}", node.Volume181)
        Console.WriteLine("Volume182: {0}", node.Volume182)
        Console.WriteLine("Volume183: {0}", node.Volume183)
        Console.WriteLine("Volume184: {0}", node.Volume184)
        Console.WriteLine("Volume185: {0}", node.Volume185)
        Console.WriteLine("Volume186: {0}", node.Volume186)
        Console.WriteLine("Volume187: {0}", node.Volume187)
        Console.WriteLine("Volume188: {0}", node.Volume188)
        Console.WriteLine("Volume189: {0}", node.Volume189)
        Console.WriteLine("Volume190: {0}", node.Volume190)
        Console.WriteLine("Volume191: {0}", node.Volume191)
        Console.WriteLine("Volume192: {0}", node.Volume192)
        Console.WriteLine("Volume193: {0}", node.Volume193)
        Console.WriteLine("Volume194: {0}", node.Volume194)
        Console.WriteLine("Volume195: {0}", node.Volume195)
        Console.WriteLine("Volume196: {0}", node.Volume196)
        Console.WriteLine("Volume197: {0}", node.Volume197)
        Console.WriteLine("Volume198: {0}", node.Volume198)
        Console.WriteLine("Volume199: {0}", node.Volume199)
        Console.WriteLine("Volume200: {0}", node.Volume200)
        Console.WriteLine("CustomerKey: {0}", node.CustomerKey)
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

    $req->TreeType = 1;
    $req->CustomerID = 1;
    $req->PeriodType = 1;
    $req->PeriodID = 1;
    $req->MaxLevelDepth = 1;

    //Add CustomerTypes

    //Now attach the list to the request
    req.CustomerTypes = array(customerType1,customerType2);

    //Add Ranks

    //Now attach the list to the request
    req.Ranks = array(rank1,rank2);

    //Add PayRanks

    //Now attach the list to the request
    req.PayRanks = array(payRank1,payRank2);

    //Add VolumeFilters

    $volumeFilter1->VolumeID = 1;
    $volumeFilter1->Compare = 1;
    $volumeFilter1->Value = 1;

    $volumeFilter2->VolumeID = 2;
    $volumeFilter2->Compare = 2;
    $volumeFilter2->Value = 2;

    //Now attach the list to the request
    req.VolumeFilters = array(volumeFilter1,volumeFilter2);

    //Add CustomerStatusTypes

    //Now attach the list to the request
    req.CustomerStatusTypes = array(customerStatusType1,customerStatusType2);
    $req->SortByLevel = 1;
    $req->BatchOffset = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.GetDownline($req);

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
    GetDownlineRequest req = new GetDownlineRequest();

    req.setTreeType(1);
    req.setCustomerID(1);
    req.setPeriodType(1);
    req.setPeriodID(1);
    req.setMaxLevelDepth(1);

    //Add CustomerTypes
    ArrayOfSystem.Int32 customertypes = new ArrayOfSystem.Int32();

    Int32 customerType1 = new Int32();
    customertypes.Add(customerType1);

    Int32 customerType2 = new Int32();
    customertypes.Add(customerType2);

    //Now attach the list to the request
    req.setCustomerTypes(customertypes);

    //Add Ranks
    ArrayOfSystem.Int32 ranks = new ArrayOfSystem.Int32();

    Int32 rank1 = new Int32();
    ranks.Add(rank1);

    Int32 rank2 = new Int32();
    ranks.Add(rank2);

    //Now attach the list to the request
    req.setRanks(ranks);

    //Add PayRanks
    ArrayOfSystem.Int32 payranks = new ArrayOfSystem.Int32();

    Int32 payRank1 = new Int32();
    payranks.Add(payRank1);

    Int32 payRank2 = new Int32();
    payranks.Add(payRank2);

    //Now attach the list to the request
    req.setPayRanks(payranks);

    //Add VolumeFilters
    ArrayOfVolumeFilter volumefilters = new ArrayOfVolumeFilter();

    VolumeFilter volumeFilter1 = new VolumeFilter();
    volumeFilter1.setVolumeID(1);
    volumeFilter1.setCompare(1);
    volumeFilter1.setValue(1);
    volumefilters.Add(volumeFilter1);

    VolumeFilter volumeFilter2 = new VolumeFilter();
    volumeFilter2.setVolumeID(2);
    volumeFilter2.setCompare(2);
    volumeFilter2.setValue(2);
    volumefilters.Add(volumeFilter2);

    //Now attach the list to the request
    req.setVolumeFilters(volumefilters);

    //Add CustomerStatusTypes
    ArrayOfSystem.Int32 customerstatustypes = new ArrayOfSystem.Int32();

    Int32 customerStatusType1 = new Int32();
    customerstatustypes.Add(customerStatusType1);

    Int32 customerStatusType2 = new Int32();
    customerstatustypes.Add(customerStatusType2);

    //Now attach the list to the request
    req.setCustomerStatusTypes(customerstatustypes);
    req.setSortByLevel(1);
    req.setBatchOffset(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    GetDownlineResponse res = api.getExigoApiSoap().getDownline(req, auth);

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
https://api.exigo.com/3.0/csv/?method=GetDownline
&ApiLoginName=String
&ApiPassword=String
&ApiCompany=String
&TreeType=TreeType
&CustomerID=Int32
&PeriodType=Int32
&PeriodID=Nullable`1
&MaxLevelDepth=Int32
&CustomerTypes=Int32[]
&Ranks=Int32[]
&PayRanks=Int32[]
&VolumeFilters=VolumeFilter[]
&CustomerStatusTypes=Int32[]
&BatchSize=Nullable`1
&SortByLevel=Boolean
&BatchOffset=Int32
&CustomerKey=String
Response FieldsCustomerID,NodeID,ParentID,Level,Position,CustomerType,CustomerStatus,RankID,PayRankID,FirstName,LastName,Company,Email,Phone,CreatedDate,Volume1,Volume2,Volume3,Volume4,Volume5,Volume6,Volume7,Volume8,Volume9,Volume10,Volume11,Volume12,Volume13,Volume14,Volume15,Volume16,Volume17,Volume18,Volume19,Volume20,Volume21,Volume22,Volume23,Volume24,Volume25,Volume26,Volume27,Volume28,Volume29,Volume30,Volume31,Volume32,Volume33,Volume34,Volume35,Volume36,Volume37,Volume38,Volume39,Volume40,Volume41,Volume42,Volume43,Volume44,Volume45,Volume46,Volume47,Volume48,Volume49,Volume50,Volume51,Volume52,Volume53,Volume54,Volume55,Volume56,Volume57,Volume58,Volume59,Volume60,Volume61,Volume62,Volume63,Volume64,Volume65,Volume66,Volume67,Volume68,Volume69,Volume70,Volume71,Volume72,Volume73,Volume74,Volume75,Volume76,Volume77,Volume78,Volume79,Volume80,Volume81,Volume82,Volume83,Volume84,Volume85,Volume86,Volume87,Volume88,Volume89,Volume90,Volume91,Volume92,Volume93,Volume94,Volume95,Volume96,Volume97,Volume98,Volume99,Volume100,Volume101,Volume102,Volume103,Volume104,Volume105,Volume106,Volume107,Volume108,Volume109,Volume110,Volume111,Volume112,Volume113,Volume114,Volume115,Volume116,Volume117,Volume118,Volume119,Volume120,Volume121,Volume122,Volume123,Volume124,Volume125,Volume126,Volume127,Volume128,Volume129,Volume130,Volume131,Volume132,Volume133,Volume134,Volume135,Volume136,Volume137,Volume138,Volume139,Volume140,Volume141,Volume142,Volume143,Volume144,Volume145,Volume146,Volume147,Volume148,Volume149,Volume150,Volume151,Volume152,Volume153,Volume154,Volume155,Volume156,Volume157,Volume158,Volume159,Volume160,Volume161,Volume162,Volume163,Volume164,Volume165,Volume166,Volume167,Volume168,Volume169,Volume170,Volume171,Volume172,Volume173,Volume174,Volume175,Volume176,Volume177,Volume178,Volume179,Volume180,Volume181,Volume182,Volume183,Volume184,Volume185,Volume186,Volume187,Volume188,Volume189,Volume190,Volume191,Volume192,Volume193,Volume194,Volume195,Volume196,Volume197,Volume198,Volume199,Volume200,CustomerKey,RecordCount
Int32,Int32,Int32,Int32,Int32,Int32,Int32,Int32,Int32,String,String,String,String,String,DateTime,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,String,Int32

                    © 2026 Exigo.
```

</details>

---

### GetUpline

> Gets nodes in an upline.

| | |
|---|---|
| Category | Reporting |
| REST | `GET /3.0/commissions/upline?treeType=1` |
| SOAP action | `https://api.exigo.com/GetUpline` |
| WSDL elements | `GetUplineRequest` → `GetUplineResult` |
| CSV output | Yes — `GET https://api.exigo.com/3.0/csv/?method=GetUpline&ApiLoginName=…&ApiPassword=…&ApiCompany=…` |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetUpline |

#### Input

**`GetUplineRequest`**

| Property | Type | Notes |
|---|---|---|
| `TreeType` | `TreeType` | **Values:** `Enroller`, `UniLevel`, `Binary`, `Matrix`, `Stack` |
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `PeriodType` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| `PeriodID` | `Int32` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |
| `BatchSize` | `Int32` | Optional. Defaults to 1000 at a time. |
| `BatchOffset` | `Int32` | Optional. |

#### Output

**`GetUplineResponse`**

| Property | Type | Notes |
|---|---|---|
| `Nodes` | `NodeResponse[]` |  |

**`NodeResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| &nbsp;&nbsp;↳ `NodeID` | `Int32` |  |
| &nbsp;&nbsp;↳ `ParentID` | `Int32` |  |
| &nbsp;&nbsp;↳ `Level` | `Int32` |  |
| &nbsp;&nbsp;↳ `Position` | `Int32` |  |
| &nbsp;&nbsp;↳ `CustomerType` | `Int32` | Classification of a customer as defined by the company.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `CustomerStatus` | `Int32` | Current status of a customer as defined by the company.<br>**Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `RankID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `PayRankID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `FirstName` | `String` |  |
| &nbsp;&nbsp;↳ `LastName` | `String` |  |
| &nbsp;&nbsp;↳ `Company` | `String` |  |
| &nbsp;&nbsp;↳ `Email` | `String` |  |
| &nbsp;&nbsp;↳ `Phone` | `String` |  |
| &nbsp;&nbsp;↳ `CreatedDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `Volume1` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume2` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume3` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume4` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume5` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume6` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume7` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume8` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume9` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume10` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume11` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume12` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume13` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume14` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume15` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume16` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume17` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume18` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume19` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume20` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume21` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume22` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume23` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume24` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume25` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume26` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume27` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume28` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume29` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume30` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume31` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume32` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume33` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume34` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume35` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume36` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume37` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume38` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume39` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume40` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume41` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume42` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume43` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume44` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume45` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume46` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume47` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume48` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume49` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume50` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume51` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume52` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume53` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume54` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume55` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume56` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume57` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume58` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume59` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume60` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume61` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume62` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume63` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume64` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume65` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume66` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume67` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume68` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume69` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume70` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume71` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume72` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume73` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume74` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume75` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume76` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume77` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume78` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume79` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume80` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume81` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume82` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume83` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume84` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume85` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume86` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume87` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume88` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume89` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume90` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume91` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume92` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume93` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume94` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume95` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume96` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume97` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume98` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume99` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume100` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume101` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume102` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume103` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume104` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume105` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume106` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume107` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume108` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume109` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume110` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume111` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume112` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume113` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume114` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume115` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume116` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume117` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume118` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume119` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume120` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume121` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume122` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume123` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume124` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume125` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume126` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume127` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume128` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume129` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume130` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume131` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume132` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume133` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume134` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume135` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume136` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume137` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume138` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume139` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume140` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume141` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume142` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume143` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume144` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume145` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume146` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume147` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume148` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume149` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume150` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume151` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume152` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume153` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume154` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume155` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume156` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume157` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume158` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume159` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume160` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume161` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume162` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume163` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume164` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume165` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume166` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume167` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume168` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume169` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume170` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume171` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume172` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume173` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume174` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume175` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume176` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume177` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume178` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume179` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume180` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume181` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume182` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume183` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume184` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume185` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume186` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume187` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume188` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume189` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume190` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume191` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume192` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume193` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume194` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume195` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume196` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume197` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume198` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume199` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume200` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `CustomerKey` | `String` | Unique alpha numeric identifier for customer record . |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/commissions/upline?treeType=1
  &customerID=1
  &periodType=1
  &periodID=1
  &customerKey=1
  &batchOffset=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "nodes": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetUpline"

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
    <GetUplineRequest xmlns="http://api.exigo.com/">
      <TreeType>Enroller or UniLevel or Binary or Matrix or Stack</TreeType>
      <CustomerID>int</CustomerID>
      <PeriodType>int</PeriodType>
      <PeriodID>int</PeriodID>
      <CustomerKey>string</CustomerKey>
      <BatchSize>int</BatchSize>
      <BatchOffset>int</BatchOffset>
    </GetUplineRequest>
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
    <GetUplineResult xmlns="http://api.exigo.com/">
      <Nodes>
        <NodeResponse>
          <CustomerID>int</CustomerID>
          <NodeID>int</NodeID>
          <ParentID>int</ParentID>
          <Level>int</Level>
          <Position>int</Position>
          <CustomerType>int</CustomerType>
          <CustomerStatus>int</CustomerStatus>
          <RankID>int</RankID>
          <PayRankID>int</PayRankID>
          <FirstName>string</FirstName>
          <LastName>string</LastName>
          <Company>string</Company>
          <Email>string</Email>
          <Phone>string</Phone>
          <CreatedDate>dateTime</CreatedDate>
          <Volume1>decimal</Volume1>
          <Volume2>decimal</Volume2>
          <Volume3>decimal</Volume3>
          <Volume4>decimal</Volume4>
          <Volume5>decimal</Volume5>
          <Volume6>decimal</Volume6>
          <Volume7>decimal</Volume7>
          <Volume8>decimal</Volume8>
          <Volume9>decimal</Volume9>
          <Volume10>decimal</Volume10>
          <Volume11>decimal</Volume11>
          <Volume12>decimal</Volume12>
          <Volume13>decimal</Volume13>
          <Volume14>decimal</Volume14>
          <Volume15>decimal</Volume15>
          <Volume16>decimal</Volume16>
          <Volume17>decimal</Volume17>
          <Volume18>decimal</Volume18>
          <Volume19>decimal</Volume19>
          <Volume20>decimal</Volume20>
          <Volume21>decimal</Volume21>
          <Volume22>decimal</Volume22>
          <Volume23>decimal</Volume23>
          <Volume24>decimal</Volume24>
          <Volume25>decimal</Volume25>
          <Volume26>decimal</Volume26>
          <Volume27>decimal</Volume27>
          <Volume28>decimal</Volume28>
          <Volume29>decimal</Volume29>
          <Volume30>decimal</Volume30>
          <Volume31>decimal</Volume31>
          <Volume32>decimal</Volume32>
          <Volume33>decimal</Volume33>
          <Volume34>decimal</Volume34>
          <Volume35>decimal</Volume35>
          <Volume36>decimal</Volume36>
          <Volume37>decimal</Volume37>
          <Volume38>decimal</Volume38>
          <Volume39>decimal</Volume39>
          <Volume40>decimal</Volume40>
          <Volume41>decimal</Volume41>
          <Volume42>decimal</Volume42>
          <Volume43>decimal</Volume43>
          <Volume44>decimal</Volume44>
          <Volume45>decimal</Volume45>
          <Volume46>decimal</Volume46>
          <Volume47>decimal</Volume47>
          <Volume48>decimal</Volume48>
          <Volume49>decimal</Volume49>
          <Volume50>decimal</Volume50>
          <Volume51>decimal</Volume51>
          <Volume52>decimal</Volume52>
          <Volume53>decimal</Volume53>
          <Volume54>decimal</Volume54>
          <Volume55>decimal</Volume55>
          <Volume56>decimal</Volume56>
          <Volume57>decimal</Volume57>
          <Volume58>decimal</Volume58>
          <Volume59>decimal</Volume59>
          <Volume60>decimal</Volume60>
          <Volume61>decimal</Volume61>
          <Volume62>decimal</Volume62>
          <Volume63>decimal</Volume63>
          <Volume64>decimal</Volume64>
          <Volume65>decimal</Volume65>
          <Volume66>decimal</Volume66>
          <Volume67>decimal</Volume67>
          <Volume68>decimal</Volume68>
          <Volume69>decimal</Volume69>
          <Volume70>decimal</Volume70>
          <Volume71>decimal</Volume71>
          <Volume72>decimal</Volume72>
          <Volume73>decimal</Volume73>
          <Volume74>decimal</Volume74>
          <Volume75>decimal</Volume75>
          <Volume76>decimal</Volume76>
          <Volume77>decimal</Volume77>
          <Volume78>decimal</Volume78>
          <Volume79>decimal</Volume79>
          <Volume80>decimal</Volume80>
          <Volume81>decimal</Volume81>
          <Volume82>decimal</Volume82>
          <Volume83>decimal</Volume83>
          <Volume84>decimal</Volume84>
          <Volume85>decimal</Volume85>
          <Volume86>decimal</Volume86>
          <Volume87>decimal</Volume87>
          <Volume88>decimal</Volume88>
          <Volume89>decimal</Volume89>
          <Volume90>decimal</Volume90>
          <Volume91>decimal</Volume91>
          <Volume92>decimal</Volume92>
          <Volume93>decimal</Volume93>
          <Volume94>decimal</Volume94>
          <Volume95>decimal</Volume95>
          <Volume96>decimal</Volume96>
          <Volume97>decimal</Volume97>
          <Volume98>decimal</Volume98>
          <Volume99>decimal</Volume99>
          <Volume100>decimal</Volume100>
          <Volume101>decimal</Volume101>
          <Volume102>decimal</Volume102>
          <Volume103>decimal</Volume103>
          <Volume104>decimal</Volume104>
          <Volume105>decimal</Volume105>
          <Volume106>decimal</Volume106>
          <Volume107>decimal</Volume107>
          <Volume108>decimal</Volume108>
          <Volume109>decimal</Volume109>
          <Volume110>decimal</Volume110>
          <Volume111>decimal</Volume111>
          <Volume112>decimal</Volume112>
          <Volume113>decimal</Volume113>
          <Volume114>decimal</Volume114>
          <Volume115>decimal</Volume115>
          <Volume116>decimal</Volume116>
          <Volume117>decimal</Volume117>
          <Volume118>decimal</Volume118>
          <Volume119>decimal</Volume119>
          <Volume120>decimal</Volume120>
          <Volume121>decimal</Volume121>
          <Volume122>decimal</Volume122>
          <Volume123>decimal</Volume123>
          <Volume124>decimal</Volume124>
          <Volume125>decimal</Volume125>
          <Volume126>decimal</Volume126>
          <Volume127>decimal</Volume127>
          <Volume128>decimal</Volume128>
          <Volume129>decimal</Volume129>
          <Volume130>decimal</Volume130>
          <Volume131>decimal</Volume131>
          <Volume132>decimal</Volume132>
          <Volume133>decimal</Volume133>
          <Volume134>decimal</Volume134>
          <Volume135>decimal</Volume135>
          <Volume136>decimal</Volume136>
          <Volume137>decimal</Volume137>
          <Volume138>decimal</Volume138>
          <Volume139>decimal</Volume139>
          <Volume140>decimal</Volume140>
          <Volume141>decimal</Volume141>
          <Volume142>decimal</Volume142>
          <Volume143>decimal</Volume143>
          <Volume144>decimal</Volume144>
          <Volume145>decimal</Volume145>
          <Volume146>decimal</Volume146>
          <Volume147>decimal</Volume147>
          <Volume148>decimal</Volume148>
          <Volume149>decimal</Volume149>
          <Volume150>decimal</Volume150>
          <Volume151>decimal</Volume151>
          <Volume152>decimal</Volume152>
          <Volume153>decimal</Volume153>
          <Volume154>decimal</Volume154>
          <Volume155>decimal</Volume155>
          <Volume156>decimal</Volume156>
          <Volume157>decimal</Volume157>
          <Volume158>decimal</Volume158>
          <Volume159>decimal</Volume159>
          <Volume160>decimal</Volume160>
          <Volume161>decimal</Volume161>
          <Volume162>decimal</Volume162>
          <Volume163>decimal</Volume163>
          <Volume164>decimal</Volume164>
          <Volume165>decimal</Volume165>
          <Volume166>decimal</Volume166>
          <Volume167>decimal</Volume167>
          <Volume168>decimal</Volume168>
          <Volume169>decimal</Volume169>
          <Volume170>decimal</Volume170>
          <Volume171>decimal</Volume171>
          <Volume172>decimal</Volume172>
          <Volume173>decimal</Volume173>
          <Volume174>decimal</Volume174>
          <Volume175>decimal</Volume175>
          <Volume176>decimal</Volume176>
          <Volume177>decimal</Volume177>
          <Volume178>decimal</Volume178>
          <Volume179>decimal</Volume179>
          <Volume180>decimal</Volume180>
          <Volume181>decimal</Volume181>
          <Volume182>decimal</Volume182>
          <Volume183>decimal</Volume183>
          <Volume184>decimal</Volume184>
          <Volume185>decimal</Volume185>
          <Volume186>decimal</Volume186>
          <Volume187>decimal</Volume187>
          <Volume188>decimal</Volume188>
          <Volume189>decimal</Volume189>
          <Volume190>decimal</Volume190>
          <Volume191>decimal</Volume191>
          <Volume192>decimal</Volume192>
          <Volume193>decimal</Volume193>
          <Volume194>decimal</Volume194>
          <Volume195>decimal</Volume195>
          <Volume196>decimal</Volume196>
          <Volume197>decimal</Volume197>
          <Volume198>decimal</Volume198>
          <Volume199>decimal</Volume199>
          <Volume200>decimal</Volume200>
          <CustomerKey>string</CustomerKey>
        </NodeResponse>
      </Nodes>
    </GetUplineResult>
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
    var req = new GetUplineRequest();

    req.TreeType = TreeType.Enroller;
    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.PeriodType = 1;
    req.PeriodID = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.BatchOffset = 1;

    //Send Request to Server and Get Response
    var res = await api.GetUplineAsync(req);

    //Now examine the results:

    foreach (var node  in res.Nodes)
    {
        Console.WriteLine("CustomerID: {0}", node.CustomerID);
        Console.WriteLine("NodeID: {0}", node.NodeID);
        Console.WriteLine("ParentID: {0}", node.ParentID);
        Console.WriteLine("Level: {0}", node.Level);
        Console.WriteLine("Position: {0}", node.Position);
        Console.WriteLine("CustomerType: {0}", node.CustomerType);
        Console.WriteLine("CustomerStatus: {0}", node.CustomerStatus);
        Console.WriteLine("RankID: {0}", node.RankID);
        Console.WriteLine("PayRankID: {0}", node.PayRankID);
        Console.WriteLine("FirstName: {0}", node.FirstName);
        Console.WriteLine("LastName: {0}", node.LastName);
        Console.WriteLine("Company: {0}", node.Company);
        Console.WriteLine("Email: {0}", node.Email);
        Console.WriteLine("Phone: {0}", node.Phone);
        Console.WriteLine("CreatedDate: {0}", node.CreatedDate);
        Console.WriteLine("Volume1: {0}", node.Volume1);
        Console.WriteLine("Volume2: {0}", node.Volume2);
        Console.WriteLine("Volume3: {0}", node.Volume3);
        Console.WriteLine("Volume4: {0}", node.Volume4);
        Console.WriteLine("Volume5: {0}", node.Volume5);
        Console.WriteLine("Volume6: {0}", node.Volume6);
        Console.WriteLine("Volume7: {0}", node.Volume7);
        Console.WriteLine("Volume8: {0}", node.Volume8);
        Console.WriteLine("Volume9: {0}", node.Volume9);
        Console.WriteLine("Volume10: {0}", node.Volume10);
        Console.WriteLine("Volume11: {0}", node.Volume11);
        Console.WriteLine("Volume12: {0}", node.Volume12);
        Console.WriteLine("Volume13: {0}", node.Volume13);
        Console.WriteLine("Volume14: {0}", node.Volume14);
        Console.WriteLine("Volume15: {0}", node.Volume15);
        Console.WriteLine("Volume16: {0}", node.Volume16);
        Console.WriteLine("Volume17: {0}", node.Volume17);
        Console.WriteLine("Volume18: {0}", node.Volume18);
        Console.WriteLine("Volume19: {0}", node.Volume19);
        Console.WriteLine("Volume20: {0}", node.Volume20);
        Console.WriteLine("Volume21: {0}", node.Volume21);
        Console.WriteLine("Volume22: {0}", node.Volume22);
        Console.WriteLine("Volume23: {0}", node.Volume23);
        Console.WriteLine("Volume24: {0}", node.Volume24);
        Console.WriteLine("Volume25: {0}", node.Volume25);
        Console.WriteLine("Volume26: {0}", node.Volume26);
        Console.WriteLine("Volume27: {0}", node.Volume27);
        Console.WriteLine("Volume28: {0}", node.Volume28);
        Console.WriteLine("Volume29: {0}", node.Volume29);
        Console.WriteLine("Volume30: {0}", node.Volume30);
        Console.WriteLine("Volume31: {0}", node.Volume31);
        Console.WriteLine("Volume32: {0}", node.Volume32);
        Console.WriteLine("Volume33: {0}", node.Volume33);
        Console.WriteLine("Volume34: {0}", node.Volume34);
        Console.WriteLine("Volume35: {0}", node.Volume35);
        Console.WriteLine("Volume36: {0}", node.Volume36);
        Console.WriteLine("Volume37: {0}", node.Volume37);
        Console.WriteLine("Volume38: {0}", node.Volume38);
        Console.WriteLine("Volume39: {0}", node.Volume39);
        Console.WriteLine("Volume40: {0}", node.Volume40);
        Console.WriteLine("Volume41: {0}", node.Volume41);
        Console.WriteLine("Volume42: {0}", node.Volume42);
        Console.WriteLine("Volume43: {0}", node.Volume43);
        Console.WriteLine("Volume44: {0}", node.Volume44);
        Console.WriteLine("Volume45: {0}", node.Volume45);
        Console.WriteLine("Volume46: {0}", node.Volume46);
        Console.WriteLine("Volume47: {0}", node.Volume47);
        Console.WriteLine("Volume48: {0}", node.Volume48);
        Console.WriteLine("Volume49: {0}", node.Volume49);
        Console.WriteLine("Volume50: {0}", node.Volume50);
        Console.WriteLine("Volume51: {0}", node.Volume51);
        Console.WriteLine("Volume52: {0}", node.Volume52);
        Console.WriteLine("Volume53: {0}", node.Volume53);
        Console.WriteLine("Volume54: {0}", node.Volume54);
        Console.WriteLine("Volume55: {0}", node.Volume55);
        Console.WriteLine("Volume56: {0}", node.Volume56);
        Console.WriteLine("Volume57: {0}", node.Volume57);
        Console.WriteLine("Volume58: {0}", node.Volume58);
        Console.WriteLine("Volume59: {0}", node.Volume59);
        Console.WriteLine("Volume60: {0}", node.Volume60);
        Console.WriteLine("Volume61: {0}", node.Volume61);
        Console.WriteLine("Volume62: {0}", node.Volume62);
        Console.WriteLine("Volume63: {0}", node.Volume63);
        Console.WriteLine("Volume64: {0}", node.Volume64);
        Console.WriteLine("Volume65: {0}", node.Volume65);
        Console.WriteLine("Volume66: {0}", node.Volume66);
        Console.WriteLine("Volume67: {0}", node.Volume67);
        Console.WriteLine("Volume68: {0}", node.Volume68);
        Console.WriteLine("Volume69: {0}", node.Volume69);
        Console.WriteLine("Volume70: {0}", node.Volume70);
        Console.WriteLine("Volume71: {0}", node.Volume71);
        Console.WriteLine("Volume72: {0}", node.Volume72);
        Console.WriteLine("Volume73: {0}", node.Volume73);
        Console.WriteLine("Volume74: {0}", node.Volume74);
        Console.WriteLine("Volume75: {0}", node.Volume75);
        Console.WriteLine("Volume76: {0}", node.Volume76);
        Console.WriteLine("Volume77: {0}", node.Volume77);
        Console.WriteLine("Volume78: {0}", node.Volume78);
        Console.WriteLine("Volume79: {0}", node.Volume79);
        Console.WriteLine("Volume80: {0}", node.Volume80);
        Console.WriteLine("Volume81: {0}", node.Volume81);
        Console.WriteLine("Volume82: {0}", node.Volume82);
        Console.WriteLine("Volume83: {0}", node.Volume83);
        Console.WriteLine("Volume84: {0}", node.Volume84);
        Console.WriteLine("Volume85: {0}", node.Volume85);
        Console.WriteLine("Volume86: {0}", node.Volume86);
        Console.WriteLine("Volume87: {0}", node.Volume87);
        Console.WriteLine("Volume88: {0}", node.Volume88);
        Console.WriteLine("Volume89: {0}", node.Volume89);
        Console.WriteLine("Volume90: {0}", node.Volume90);
        Console.WriteLine("Volume91: {0}", node.Volume91);
        Console.WriteLine("Volume92: {0}", node.Volume92);
        Console.WriteLine("Volume93: {0}", node.Volume93);
        Console.WriteLine("Volume94: {0}", node.Volume94);
        Console.WriteLine("Volume95: {0}", node.Volume95);
        Console.WriteLine("Volume96: {0}", node.Volume96);
        Console.WriteLine("Volume97: {0}", node.Volume97);
        Console.WriteLine("Volume98: {0}", node.Volume98);
        Console.WriteLine("Volume99: {0}", node.Volume99);
        Console.WriteLine("Volume100: {0}", node.Volume100);
        Console.WriteLine("Volume101: {0}", node.Volume101);
        Console.WriteLine("Volume102: {0}", node.Volume102);
        Console.WriteLine("Volume103: {0}", node.Volume103);
        Console.WriteLine("Volume104: {0}", node.Volume104);
        Console.WriteLine("Volume105: {0}", node.Volume105);
        Console.WriteLine("Volume106: {0}", node.Volume106);
        Console.WriteLine("Volume107: {0}", node.Volume107);
        Console.WriteLine("Volume108: {0}", node.Volume108);
        Console.WriteLine("Volume109: {0}", node.Volume109);
        Console.WriteLine("Volume110: {0}", node.Volume110);
        Console.WriteLine("Volume111: {0}", node.Volume111);
        Console.WriteLine("Volume112: {0}", node.Volume112);
        Console.WriteLine("Volume113: {0}", node.Volume113);
        Console.WriteLine("Volume114: {0}", node.Volume114);
        Console.WriteLine("Volume115: {0}", node.Volume115);
        Console.WriteLine("Volume116: {0}", node.Volume116);
        Console.WriteLine("Volume117: {0}", node.Volume117);
        Console.WriteLine("Volume118: {0}", node.Volume118);
        Console.WriteLine("Volume119: {0}", node.Volume119);
        Console.WriteLine("Volume120: {0}", node.Volume120);
        Console.WriteLine("Volume121: {0}", node.Volume121);
        Console.WriteLine("Volume122: {0}", node.Volume122);
        Console.WriteLine("Volume123: {0}", node.Volume123);
        Console.WriteLine("Volume124: {0}", node.Volume124);
        Console.WriteLine("Volume125: {0}", node.Volume125);
        Console.WriteLine("Volume126: {0}", node.Volume126);
        Console.WriteLine("Volume127: {0}", node.Volume127);
        Console.WriteLine("Volume128: {0}", node.Volume128);
        Console.WriteLine("Volume129: {0}", node.Volume129);
        Console.WriteLine("Volume130: {0}", node.Volume130);
        Console.WriteLine("Volume131: {0}", node.Volume131);
        Console.WriteLine("Volume132: {0}", node.Volume132);
        Console.WriteLine("Volume133: {0}", node.Volume133);
        Console.WriteLine("Volume134: {0}", node.Volume134);
        Console.WriteLine("Volume135: {0}", node.Volume135);
        Console.WriteLine("Volume136: {0}", node.Volume136);
        Console.WriteLine("Volume137: {0}", node.Volume137);
        Console.WriteLine("Volume138: {0}", node.Volume138);
        Console.WriteLine("Volume139: {0}", node.Volume139);
        Console.WriteLine("Volume140: {0}", node.Volume140);
        Console.WriteLine("Volume141: {0}", node.Volume141);
        Console.WriteLine("Volume142: {0}", node.Volume142);
        Console.WriteLine("Volume143: {0}", node.Volume143);
        Console.WriteLine("Volume144: {0}", node.Volume144);
        Console.WriteLine("Volume145: {0}", node.Volume145);
        Console.WriteLine("Volume146: {0}", node.Volume146);
        Console.WriteLine("Volume147: {0}", node.Volume147);
        Console.WriteLine("Volume148: {0}", node.Volume148);
        Console.WriteLine("Volume149: {0}", node.Volume149);
        Console.WriteLine("Volume150: {0}", node.Volume150);
        Console.WriteLine("Volume151: {0}", node.Volume151);
        Console.WriteLine("Volume152: {0}", node.Volume152);
        Console.WriteLine("Volume153: {0}", node.Volume153);
        Console.WriteLine("Volume154: {0}", node.Volume154);
        Console.WriteLine("Volume155: {0}", node.Volume155);
        Console.WriteLine("Volume156: {0}", node.Volume156);
        Console.WriteLine("Volume157: {0}", node.Volume157);
        Console.WriteLine("Volume158: {0}", node.Volume158);
        Console.WriteLine("Volume159: {0}", node.Volume159);
        Console.WriteLine("Volume160: {0}", node.Volume160);
        Console.WriteLine("Volume161: {0}", node.Volume161);
        Console.WriteLine("Volume162: {0}", node.Volume162);
        Console.WriteLine("Volume163: {0}", node.Volume163);
        Console.WriteLine("Volume164: {0}", node.Volume164);
        Console.WriteLine("Volume165: {0}", node.Volume165);
        Console.WriteLine("Volume166: {0}", node.Volume166);
        Console.WriteLine("Volume167: {0}", node.Volume167);
        Console.WriteLine("Volume168: {0}", node.Volume168);
        Console.WriteLine("Volume169: {0}", node.Volume169);
        Console.WriteLine("Volume170: {0}", node.Volume170);
        Console.WriteLine("Volume171: {0}", node.Volume171);
        Console.WriteLine("Volume172: {0}", node.Volume172);
        Console.WriteLine("Volume173: {0}", node.Volume173);
        Console.WriteLine("Volume174: {0}", node.Volume174);
        Console.WriteLine("Volume175: {0}", node.Volume175);
        Console.WriteLine("Volume176: {0}", node.Volume176);
        Console.WriteLine("Volume177: {0}", node.Volume177);
        Console.WriteLine("Volume178: {0}", node.Volume178);
        Console.WriteLine("Volume179: {0}", node.Volume179);
        Console.WriteLine("Volume180: {0}", node.Volume180);
        Console.WriteLine("Volume181: {0}", node.Volume181);
        Console.WriteLine("Volume182: {0}", node.Volume182);
        Console.WriteLine("Volume183: {0}", node.Volume183);
        Console.WriteLine("Volume184: {0}", node.Volume184);
        Console.WriteLine("Volume185: {0}", node.Volume185);
        Console.WriteLine("Volume186: {0}", node.Volume186);
        Console.WriteLine("Volume187: {0}", node.Volume187);
        Console.WriteLine("Volume188: {0}", node.Volume188);
        Console.WriteLine("Volume189: {0}", node.Volume189);
        Console.WriteLine("Volume190: {0}", node.Volume190);
        Console.WriteLine("Volume191: {0}", node.Volume191);
        Console.WriteLine("Volume192: {0}", node.Volume192);
        Console.WriteLine("Volume193: {0}", node.Volume193);
        Console.WriteLine("Volume194: {0}", node.Volume194);
        Console.WriteLine("Volume195: {0}", node.Volume195);
        Console.WriteLine("Volume196: {0}", node.Volume196);
        Console.WriteLine("Volume197: {0}", node.Volume197);
        Console.WriteLine("Volume198: {0}", node.Volume198);
        Console.WriteLine("Volume199: {0}", node.Volume199);
        Console.WriteLine("Volume200: {0}", node.Volume200);
        Console.WriteLine("CustomerKey: {0}", node.CustomerKey);
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
    GetUplineRequest req = new GetUplineRequest();

    req.TreeType = TreeType.Enroller;
    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.PeriodType = 1;
    req.PeriodID = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.
    req.BatchOffset = 1;

    //Send Request to Server and Get Response
    GetUplineResponse res = api.GetUpline(req);

    //Now examine the results:

    foreach (NodeResponse node  in res.Nodes)
    {
        Console.WriteLine("CustomerID: {0}", node.CustomerID);
        Console.WriteLine("NodeID: {0}", node.NodeID);
        Console.WriteLine("ParentID: {0}", node.ParentID);
        Console.WriteLine("Level: {0}", node.Level);
        Console.WriteLine("Position: {0}", node.Position);
        Console.WriteLine("CustomerType: {0}", node.CustomerType);
        Console.WriteLine("CustomerStatus: {0}", node.CustomerStatus);
        Console.WriteLine("RankID: {0}", node.RankID);
        Console.WriteLine("PayRankID: {0}", node.PayRankID);
        Console.WriteLine("FirstName: {0}", node.FirstName);
        Console.WriteLine("LastName: {0}", node.LastName);
        Console.WriteLine("Company: {0}", node.Company);
        Console.WriteLine("Email: {0}", node.Email);
        Console.WriteLine("Phone: {0}", node.Phone);
        Console.WriteLine("CreatedDate: {0}", node.CreatedDate);
        Console.WriteLine("Volume1: {0}", node.Volume1);
        Console.WriteLine("Volume2: {0}", node.Volume2);
        Console.WriteLine("Volume3: {0}", node.Volume3);
        Console.WriteLine("Volume4: {0}", node.Volume4);
        Console.WriteLine("Volume5: {0}", node.Volume5);
        Console.WriteLine("Volume6: {0}", node.Volume6);
        Console.WriteLine("Volume7: {0}", node.Volume7);
        Console.WriteLine("Volume8: {0}", node.Volume8);
        Console.WriteLine("Volume9: {0}", node.Volume9);
        Console.WriteLine("Volume10: {0}", node.Volume10);
        Console.WriteLine("Volume11: {0}", node.Volume11);
        Console.WriteLine("Volume12: {0}", node.Volume12);
        Console.WriteLine("Volume13: {0}", node.Volume13);
        Console.WriteLine("Volume14: {0}", node.Volume14);
        Console.WriteLine("Volume15: {0}", node.Volume15);
        Console.WriteLine("Volume16: {0}", node.Volume16);
        Console.WriteLine("Volume17: {0}", node.Volume17);
        Console.WriteLine("Volume18: {0}", node.Volume18);
        Console.WriteLine("Volume19: {0}", node.Volume19);
        Console.WriteLine("Volume20: {0}", node.Volume20);
        Console.WriteLine("Volume21: {0}", node.Volume21);
        Console.WriteLine("Volume22: {0}", node.Volume22);
        Console.WriteLine("Volume23: {0}", node.Volume23);
        Console.WriteLine("Volume24: {0}", node.Volume24);
        Console.WriteLine("Volume25: {0}", node.Volume25);
        Console.WriteLine("Volume26: {0}", node.Volume26);
        Console.WriteLine("Volume27: {0}", node.Volume27);
        Console.WriteLine("Volume28: {0}", node.Volume28);
        Console.WriteLine("Volume29: {0}", node.Volume29);
        Console.WriteLine("Volume30: {0}", node.Volume30);
        Console.WriteLine("Volume31: {0}", node.Volume31);
        Console.WriteLine("Volume32: {0}", node.Volume32);
        Console.WriteLine("Volume33: {0}", node.Volume33);
        Console.WriteLine("Volume34: {0}", node.Volume34);
        Console.WriteLine("Volume35: {0}", node.Volume35);
        Console.WriteLine("Volume36: {0}", node.Volume36);
        Console.WriteLine("Volume37: {0}", node.Volume37);
        Console.WriteLine("Volume38: {0}", node.Volume38);
        Console.WriteLine("Volume39: {0}", node.Volume39);
        Console.WriteLine("Volume40: {0}", node.Volume40);
        Console.WriteLine("Volume41: {0}", node.Volume41);
        Console.WriteLine("Volume42: {0}", node.Volume42);
        Console.WriteLine("Volume43: {0}", node.Volume43);
        Console.WriteLine("Volume44: {0}", node.Volume44);
        Console.WriteLine("Volume45: {0}", node.Volume45);
        Console.WriteLine("Volume46: {0}", node.Volume46);
        Console.WriteLine("Volume47: {0}", node.Volume47);
        Console.WriteLine("Volume48: {0}", node.Volume48);
        Console.WriteLine("Volume49: {0}", node.Volume49);
        Console.WriteLine("Volume50: {0}", node.Volume50);
        Console.WriteLine("Volume51: {0}", node.Volume51);
        Console.WriteLine("Volume52: {0}", node.Volume52);
        Console.WriteLine("Volume53: {0}", node.Volume53);
        Console.WriteLine("Volume54: {0}", node.Volume54);
        Console.WriteLine("Volume55: {0}", node.Volume55);
        Console.WriteLine("Volume56: {0}", node.Volume56);
        Console.WriteLine("Volume57: {0}", node.Volume57);
        Console.WriteLine("Volume58: {0}", node.Volume58);
        Console.WriteLine("Volume59: {0}", node.Volume59);
        Console.WriteLine("Volume60: {0}", node.Volume60);
        Console.WriteLine("Volume61: {0}", node.Volume61);
        Console.WriteLine("Volume62: {0}", node.Volume62);
        Console.WriteLine("Volume63: {0}", node.Volume63);
        Console.WriteLine("Volume64: {0}", node.Volume64);
        Console.WriteLine("Volume65: {0}", node.Volume65);
        Console.WriteLine("Volume66: {0}", node.Volume66);
        Console.WriteLine("Volume67: {0}", node.Volume67);
        Console.WriteLine("Volume68: {0}", node.Volume68);
        Console.WriteLine("Volume69: {0}", node.Volume69);
        Console.WriteLine("Volume70: {0}", node.Volume70);
        Console.WriteLine("Volume71: {0}", node.Volume71);
        Console.WriteLine("Volume72: {0}", node.Volume72);
        Console.WriteLine("Volume73: {0}", node.Volume73);
        Console.WriteLine("Volume74: {0}", node.Volume74);
        Console.WriteLine("Volume75: {0}", node.Volume75);
        Console.WriteLine("Volume76: {0}", node.Volume76);
        Console.WriteLine("Volume77: {0}", node.Volume77);
        Console.WriteLine("Volume78: {0}", node.Volume78);
        Console.WriteLine("Volume79: {0}", node.Volume79);
        Console.WriteLine("Volume80: {0}", node.Volume80);
        Console.WriteLine("Volume81: {0}", node.Volume81);
        Console.WriteLine("Volume82: {0}", node.Volume82);
        Console.WriteLine("Volume83: {0}", node.Volume83);
        Console.WriteLine("Volume84: {0}", node.Volume84);
        Console.WriteLine("Volume85: {0}", node.Volume85);
        Console.WriteLine("Volume86: {0}", node.Volume86);
        Console.WriteLine("Volume87: {0}", node.Volume87);
        Console.WriteLine("Volume88: {0}", node.Volume88);
        Console.WriteLine("Volume89: {0}", node.Volume89);
        Console.WriteLine("Volume90: {0}", node.Volume90);
        Console.WriteLine("Volume91: {0}", node.Volume91);
        Console.WriteLine("Volume92: {0}", node.Volume92);
        Console.WriteLine("Volume93: {0}", node.Volume93);
        Console.WriteLine("Volume94: {0}", node.Volume94);
        Console.WriteLine("Volume95: {0}", node.Volume95);
        Console.WriteLine("Volume96: {0}", node.Volume96);
        Console.WriteLine("Volume97: {0}", node.Volume97);
        Console.WriteLine("Volume98: {0}", node.Volume98);
        Console.WriteLine("Volume99: {0}", node.Volume99);
        Console.WriteLine("Volume100: {0}", node.Volume100);
        Console.WriteLine("Volume101: {0}", node.Volume101);
        Console.WriteLine("Volume102: {0}", node.Volume102);
        Console.WriteLine("Volume103: {0}", node.Volume103);
        Console.WriteLine("Volume104: {0}", node.Volume104);
        Console.WriteLine("Volume105: {0}", node.Volume105);
        Console.WriteLine("Volume106: {0}", node.Volume106);
        Console.WriteLine("Volume107: {0}", node.Volume107);
        Console.WriteLine("Volume108: {0}", node.Volume108);
        Console.WriteLine("Volume109: {0}", node.Volume109);
        Console.WriteLine("Volume110: {0}", node.Volume110);
        Console.WriteLine("Volume111: {0}", node.Volume111);
        Console.WriteLine("Volume112: {0}", node.Volume112);
        Console.WriteLine("Volume113: {0}", node.Volume113);
        Console.WriteLine("Volume114: {0}", node.Volume114);
        Console.WriteLine("Volume115: {0}", node.Volume115);
        Console.WriteLine("Volume116: {0}", node.Volume116);
        Console.WriteLine("Volume117: {0}", node.Volume117);
        Console.WriteLine("Volume118: {0}", node.Volume118);
        Console.WriteLine("Volume119: {0}", node.Volume119);
        Console.WriteLine("Volume120: {0}", node.Volume120);
        Console.WriteLine("Volume121: {0}", node.Volume121);
        Console.WriteLine("Volume122: {0}", node.Volume122);
        Console.WriteLine("Volume123: {0}", node.Volume123);
        Console.WriteLine("Volume124: {0}", node.Volume124);
        Console.WriteLine("Volume125: {0}", node.Volume125);
        Console.WriteLine("Volume126: {0}", node.Volume126);
        Console.WriteLine("Volume127: {0}", node.Volume127);
        Console.WriteLine("Volume128: {0}", node.Volume128);
        Console.WriteLine("Volume129: {0}", node.Volume129);
        Console.WriteLine("Volume130: {0}", node.Volume130);
        Console.WriteLine("Volume131: {0}", node.Volume131);
        Console.WriteLine("Volume132: {0}", node.Volume132);
        Console.WriteLine("Volume133: {0}", node.Volume133);
        Console.WriteLine("Volume134: {0}", node.Volume134);
        Console.WriteLine("Volume135: {0}", node.Volume135);
        Console.WriteLine("Volume136: {0}", node.Volume136);
        Console.WriteLine("Volume137: {0}", node.Volume137);
        Console.WriteLine("Volume138: {0}", node.Volume138);
        Console.WriteLine("Volume139: {0}", node.Volume139);
        Console.WriteLine("Volume140: {0}", node.Volume140);
        Console.WriteLine("Volume141: {0}", node.Volume141);
        Console.WriteLine("Volume142: {0}", node.Volume142);
        Console.WriteLine("Volume143: {0}", node.Volume143);
        Console.WriteLine("Volume144: {0}", node.Volume144);
        Console.WriteLine("Volume145: {0}", node.Volume145);
        Console.WriteLine("Volume146: {0}", node.Volume146);
        Console.WriteLine("Volume147: {0}", node.Volume147);
        Console.WriteLine("Volume148: {0}", node.Volume148);
        Console.WriteLine("Volume149: {0}", node.Volume149);
        Console.WriteLine("Volume150: {0}", node.Volume150);
        Console.WriteLine("Volume151: {0}", node.Volume151);
        Console.WriteLine("Volume152: {0}", node.Volume152);
        Console.WriteLine("Volume153: {0}", node.Volume153);
        Console.WriteLine("Volume154: {0}", node.Volume154);
        Console.WriteLine("Volume155: {0}", node.Volume155);
        Console.WriteLine("Volume156: {0}", node.Volume156);
        Console.WriteLine("Volume157: {0}", node.Volume157);
        Console.WriteLine("Volume158: {0}", node.Volume158);
        Console.WriteLine("Volume159: {0}", node.Volume159);
        Console.WriteLine("Volume160: {0}", node.Volume160);
        Console.WriteLine("Volume161: {0}", node.Volume161);
        Console.WriteLine("Volume162: {0}", node.Volume162);
        Console.WriteLine("Volume163: {0}", node.Volume163);
        Console.WriteLine("Volume164: {0}", node.Volume164);
        Console.WriteLine("Volume165: {0}", node.Volume165);
        Console.WriteLine("Volume166: {0}", node.Volume166);
        Console.WriteLine("Volume167: {0}", node.Volume167);
        Console.WriteLine("Volume168: {0}", node.Volume168);
        Console.WriteLine("Volume169: {0}", node.Volume169);
        Console.WriteLine("Volume170: {0}", node.Volume170);
        Console.WriteLine("Volume171: {0}", node.Volume171);
        Console.WriteLine("Volume172: {0}", node.Volume172);
        Console.WriteLine("Volume173: {0}", node.Volume173);
        Console.WriteLine("Volume174: {0}", node.Volume174);
        Console.WriteLine("Volume175: {0}", node.Volume175);
        Console.WriteLine("Volume176: {0}", node.Volume176);
        Console.WriteLine("Volume177: {0}", node.Volume177);
        Console.WriteLine("Volume178: {0}", node.Volume178);
        Console.WriteLine("Volume179: {0}", node.Volume179);
        Console.WriteLine("Volume180: {0}", node.Volume180);
        Console.WriteLine("Volume181: {0}", node.Volume181);
        Console.WriteLine("Volume182: {0}", node.Volume182);
        Console.WriteLine("Volume183: {0}", node.Volume183);
        Console.WriteLine("Volume184: {0}", node.Volume184);
        Console.WriteLine("Volume185: {0}", node.Volume185);
        Console.WriteLine("Volume186: {0}", node.Volume186);
        Console.WriteLine("Volume187: {0}", node.Volume187);
        Console.WriteLine("Volume188: {0}", node.Volume188);
        Console.WriteLine("Volume189: {0}", node.Volume189);
        Console.WriteLine("Volume190: {0}", node.Volume190);
        Console.WriteLine("Volume191: {0}", node.Volume191);
        Console.WriteLine("Volume192: {0}", node.Volume192);
        Console.WriteLine("Volume193: {0}", node.Volume193);
        Console.WriteLine("Volume194: {0}", node.Volume194);
        Console.WriteLine("Volume195: {0}", node.Volume195);
        Console.WriteLine("Volume196: {0}", node.Volume196);
        Console.WriteLine("Volume197: {0}", node.Volume197);
        Console.WriteLine("Volume198: {0}", node.Volume198);
        Console.WriteLine("Volume199: {0}", node.Volume199);
        Console.WriteLine("Volume200: {0}", node.Volume200);
        Console.WriteLine("CustomerKey: {0}", node.CustomerKey);
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
    Dim req as new GetUplineRequest()

    req.TreeType = TreeType.Enroller
    req.CustomerID = 1
    req.PeriodType = 1
    req.PeriodID = 1
    req.CustomerKey = "1"
    req.BatchOffset = 1

    'Send Request to Server and Get Response
    Dim res As GetUplineResponse = api.GetUpline(req)

    'Now examine the results:

    For Each node As NodeResponse In res.Nodes
        Console.WriteLine("CustomerID: {0}", node.CustomerID)
        Console.WriteLine("NodeID: {0}", node.NodeID)
        Console.WriteLine("ParentID: {0}", node.ParentID)
        Console.WriteLine("Level: {0}", node.Level)
        Console.WriteLine("Position: {0}", node.Position)
        Console.WriteLine("CustomerType: {0}", node.CustomerType)
        Console.WriteLine("CustomerStatus: {0}", node.CustomerStatus)
        Console.WriteLine("RankID: {0}", node.RankID)
        Console.WriteLine("PayRankID: {0}", node.PayRankID)
        Console.WriteLine("FirstName: {0}", node.FirstName)
        Console.WriteLine("LastName: {0}", node.LastName)
        Console.WriteLine("Company: {0}", node.Company)
        Console.WriteLine("Email: {0}", node.Email)
        Console.WriteLine("Phone: {0}", node.Phone)
        Console.WriteLine("CreatedDate: {0}", node.CreatedDate)
        Console.WriteLine("Volume1: {0}", node.Volume1)
        Console.WriteLine("Volume2: {0}", node.Volume2)
        Console.WriteLine("Volume3: {0}", node.Volume3)
        Console.WriteLine("Volume4: {0}", node.Volume4)
        Console.WriteLine("Volume5: {0}", node.Volume5)
        Console.WriteLine("Volume6: {0}", node.Volume6)
        Console.WriteLine("Volume7: {0}", node.Volume7)
        Console.WriteLine("Volume8: {0}", node.Volume8)
        Console.WriteLine("Volume9: {0}", node.Volume9)
        Console.WriteLine("Volume10: {0}", node.Volume10)
        Console.WriteLine("Volume11: {0}", node.Volume11)
        Console.WriteLine("Volume12: {0}", node.Volume12)
        Console.WriteLine("Volume13: {0}", node.Volume13)
        Console.WriteLine("Volume14: {0}", node.Volume14)
        Console.WriteLine("Volume15: {0}", node.Volume15)
        Console.WriteLine("Volume16: {0}", node.Volume16)
        Console.WriteLine("Volume17: {0}", node.Volume17)
        Console.WriteLine("Volume18: {0}", node.Volume18)
        Console.WriteLine("Volume19: {0}", node.Volume19)
        Console.WriteLine("Volume20: {0}", node.Volume20)
        Console.WriteLine("Volume21: {0}", node.Volume21)
        Console.WriteLine("Volume22: {0}", node.Volume22)
        Console.WriteLine("Volume23: {0}", node.Volume23)
        Console.WriteLine("Volume24: {0}", node.Volume24)
        Console.WriteLine("Volume25: {0}", node.Volume25)
        Console.WriteLine("Volume26: {0}", node.Volume26)
        Console.WriteLine("Volume27: {0}", node.Volume27)
        Console.WriteLine("Volume28: {0}", node.Volume28)
        Console.WriteLine("Volume29: {0}", node.Volume29)
        Console.WriteLine("Volume30: {0}", node.Volume30)
        Console.WriteLine("Volume31: {0}", node.Volume31)
        Console.WriteLine("Volume32: {0}", node.Volume32)
        Console.WriteLine("Volume33: {0}", node.Volume33)
        Console.WriteLine("Volume34: {0}", node.Volume34)
        Console.WriteLine("Volume35: {0}", node.Volume35)
        Console.WriteLine("Volume36: {0}", node.Volume36)
        Console.WriteLine("Volume37: {0}", node.Volume37)
        Console.WriteLine("Volume38: {0}", node.Volume38)
        Console.WriteLine("Volume39: {0}", node.Volume39)
        Console.WriteLine("Volume40: {0}", node.Volume40)
        Console.WriteLine("Volume41: {0}", node.Volume41)
        Console.WriteLine("Volume42: {0}", node.Volume42)
        Console.WriteLine("Volume43: {0}", node.Volume43)
        Console.WriteLine("Volume44: {0}", node.Volume44)
        Console.WriteLine("Volume45: {0}", node.Volume45)
        Console.WriteLine("Volume46: {0}", node.Volume46)
        Console.WriteLine("Volume47: {0}", node.Volume47)
        Console.WriteLine("Volume48: {0}", node.Volume48)
        Console.WriteLine("Volume49: {0}", node.Volume49)
        Console.WriteLine("Volume50: {0}", node.Volume50)
        Console.WriteLine("Volume51: {0}", node.Volume51)
        Console.WriteLine("Volume52: {0}", node.Volume52)
        Console.WriteLine("Volume53: {0}", node.Volume53)
        Console.WriteLine("Volume54: {0}", node.Volume54)
        Console.WriteLine("Volume55: {0}", node.Volume55)
        Console.WriteLine("Volume56: {0}", node.Volume56)
        Console.WriteLine("Volume57: {0}", node.Volume57)
        Console.WriteLine("Volume58: {0}", node.Volume58)
        Console.WriteLine("Volume59: {0}", node.Volume59)
        Console.WriteLine("Volume60: {0}", node.Volume60)
        Console.WriteLine("Volume61: {0}", node.Volume61)
        Console.WriteLine("Volume62: {0}", node.Volume62)
        Console.WriteLine("Volume63: {0}", node.Volume63)
        Console.WriteLine("Volume64: {0}", node.Volume64)
        Console.WriteLine("Volume65: {0}", node.Volume65)
        Console.WriteLine("Volume66: {0}", node.Volume66)
        Console.WriteLine("Volume67: {0}", node.Volume67)
        Console.WriteLine("Volume68: {0}", node.Volume68)
        Console.WriteLine("Volume69: {0}", node.Volume69)
        Console.WriteLine("Volume70: {0}", node.Volume70)
        Console.WriteLine("Volume71: {0}", node.Volume71)
        Console.WriteLine("Volume72: {0}", node.Volume72)
        Console.WriteLine("Volume73: {0}", node.Volume73)
        Console.WriteLine("Volume74: {0}", node.Volume74)
        Console.WriteLine("Volume75: {0}", node.Volume75)
        Console.WriteLine("Volume76: {0}", node.Volume76)
        Console.WriteLine("Volume77: {0}", node.Volume77)
        Console.WriteLine("Volume78: {0}", node.Volume78)
        Console.WriteLine("Volume79: {0}", node.Volume79)
        Console.WriteLine("Volume80: {0}", node.Volume80)
        Console.WriteLine("Volume81: {0}", node.Volume81)
        Console.WriteLine("Volume82: {0}", node.Volume82)
        Console.WriteLine("Volume83: {0}", node.Volume83)
        Console.WriteLine("Volume84: {0}", node.Volume84)
        Console.WriteLine("Volume85: {0}", node.Volume85)
        Console.WriteLine("Volume86: {0}", node.Volume86)
        Console.WriteLine("Volume87: {0}", node.Volume87)
        Console.WriteLine("Volume88: {0}", node.Volume88)
        Console.WriteLine("Volume89: {0}", node.Volume89)
        Console.WriteLine("Volume90: {0}", node.Volume90)
        Console.WriteLine("Volume91: {0}", node.Volume91)
        Console.WriteLine("Volume92: {0}", node.Volume92)
        Console.WriteLine("Volume93: {0}", node.Volume93)
        Console.WriteLine("Volume94: {0}", node.Volume94)
        Console.WriteLine("Volume95: {0}", node.Volume95)
        Console.WriteLine("Volume96: {0}", node.Volume96)
        Console.WriteLine("Volume97: {0}", node.Volume97)
        Console.WriteLine("Volume98: {0}", node.Volume98)
        Console.WriteLine("Volume99: {0}", node.Volume99)
        Console.WriteLine("Volume100: {0}", node.Volume100)
        Console.WriteLine("Volume101: {0}", node.Volume101)
        Console.WriteLine("Volume102: {0}", node.Volume102)
        Console.WriteLine("Volume103: {0}", node.Volume103)
        Console.WriteLine("Volume104: {0}", node.Volume104)
        Console.WriteLine("Volume105: {0}", node.Volume105)
        Console.WriteLine("Volume106: {0}", node.Volume106)
        Console.WriteLine("Volume107: {0}", node.Volume107)
        Console.WriteLine("Volume108: {0}", node.Volume108)
        Console.WriteLine("Volume109: {0}", node.Volume109)
        Console.WriteLine("Volume110: {0}", node.Volume110)
        Console.WriteLine("Volume111: {0}", node.Volume111)
        Console.WriteLine("Volume112: {0}", node.Volume112)
        Console.WriteLine("Volume113: {0}", node.Volume113)
        Console.WriteLine("Volume114: {0}", node.Volume114)
        Console.WriteLine("Volume115: {0}", node.Volume115)
        Console.WriteLine("Volume116: {0}", node.Volume116)
        Console.WriteLine("Volume117: {0}", node.Volume117)
        Console.WriteLine("Volume118: {0}", node.Volume118)
        Console.WriteLine("Volume119: {0}", node.Volume119)
        Console.WriteLine("Volume120: {0}", node.Volume120)
        Console.WriteLine("Volume121: {0}", node.Volume121)
        Console.WriteLine("Volume122: {0}", node.Volume122)
        Console.WriteLine("Volume123: {0}", node.Volume123)
        Console.WriteLine("Volume124: {0}", node.Volume124)
        Console.WriteLine("Volume125: {0}", node.Volume125)
        Console.WriteLine("Volume126: {0}", node.Volume126)
        Console.WriteLine("Volume127: {0}", node.Volume127)
        Console.WriteLine("Volume128: {0}", node.Volume128)
        Console.WriteLine("Volume129: {0}", node.Volume129)
        Console.WriteLine("Volume130: {0}", node.Volume130)
        Console.WriteLine("Volume131: {0}", node.Volume131)
        Console.WriteLine("Volume132: {0}", node.Volume132)
        Console.WriteLine("Volume133: {0}", node.Volume133)
        Console.WriteLine("Volume134: {0}", node.Volume134)
        Console.WriteLine("Volume135: {0}", node.Volume135)
        Console.WriteLine("Volume136: {0}", node.Volume136)
        Console.WriteLine("Volume137: {0}", node.Volume137)
        Console.WriteLine("Volume138: {0}", node.Volume138)
        Console.WriteLine("Volume139: {0}", node.Volume139)
        Console.WriteLine("Volume140: {0}", node.Volume140)
        Console.WriteLine("Volume141: {0}", node.Volume141)
        Console.WriteLine("Volume142: {0}", node.Volume142)
        Console.WriteLine("Volume143: {0}", node.Volume143)
        Console.WriteLine("Volume144: {0}", node.Volume144)
        Console.WriteLine("Volume145: {0}", node.Volume145)
        Console.WriteLine("Volume146: {0}", node.Volume146)
        Console.WriteLine("Volume147: {0}", node.Volume147)
        Console.WriteLine("Volume148: {0}", node.Volume148)
        Console.WriteLine("Volume149: {0}", node.Volume149)
        Console.WriteLine("Volume150: {0}", node.Volume150)
        Console.WriteLine("Volume151: {0}", node.Volume151)
        Console.WriteLine("Volume152: {0}", node.Volume152)
        Console.WriteLine("Volume153: {0}", node.Volume153)
        Console.WriteLine("Volume154: {0}", node.Volume154)
        Console.WriteLine("Volume155: {0}", node.Volume155)
        Console.WriteLine("Volume156: {0}", node.Volume156)
        Console.WriteLine("Volume157: {0}", node.Volume157)
        Console.WriteLine("Volume158: {0}", node.Volume158)
        Console.WriteLine("Volume159: {0}", node.Volume159)
        Console.WriteLine("Volume160: {0}", node.Volume160)
        Console.WriteLine("Volume161: {0}", node.Volume161)
        Console.WriteLine("Volume162: {0}", node.Volume162)
        Console.WriteLine("Volume163: {0}", node.Volume163)
        Console.WriteLine("Volume164: {0}", node.Volume164)
        Console.WriteLine("Volume165: {0}", node.Volume165)
        Console.WriteLine("Volume166: {0}", node.Volume166)
        Console.WriteLine("Volume167: {0}", node.Volume167)
        Console.WriteLine("Volume168: {0}", node.Volume168)
        Console.WriteLine("Volume169: {0}", node.Volume169)
        Console.WriteLine("Volume170: {0}", node.Volume170)
        Console.WriteLine("Volume171: {0}", node.Volume171)
        Console.WriteLine("Volume172: {0}", node.Volume172)
        Console.WriteLine("Volume173: {0}", node.Volume173)
        Console.WriteLine("Volume174: {0}", node.Volume174)
        Console.WriteLine("Volume175: {0}", node.Volume175)
        Console.WriteLine("Volume176: {0}", node.Volume176)
        Console.WriteLine("Volume177: {0}", node.Volume177)
        Console.WriteLine("Volume178: {0}", node.Volume178)
        Console.WriteLine("Volume179: {0}", node.Volume179)
        Console.WriteLine("Volume180: {0}", node.Volume180)
        Console.WriteLine("Volume181: {0}", node.Volume181)
        Console.WriteLine("Volume182: {0}", node.Volume182)
        Console.WriteLine("Volume183: {0}", node.Volume183)
        Console.WriteLine("Volume184: {0}", node.Volume184)
        Console.WriteLine("Volume185: {0}", node.Volume185)
        Console.WriteLine("Volume186: {0}", node.Volume186)
        Console.WriteLine("Volume187: {0}", node.Volume187)
        Console.WriteLine("Volume188: {0}", node.Volume188)
        Console.WriteLine("Volume189: {0}", node.Volume189)
        Console.WriteLine("Volume190: {0}", node.Volume190)
        Console.WriteLine("Volume191: {0}", node.Volume191)
        Console.WriteLine("Volume192: {0}", node.Volume192)
        Console.WriteLine("Volume193: {0}", node.Volume193)
        Console.WriteLine("Volume194: {0}", node.Volume194)
        Console.WriteLine("Volume195: {0}", node.Volume195)
        Console.WriteLine("Volume196: {0}", node.Volume196)
        Console.WriteLine("Volume197: {0}", node.Volume197)
        Console.WriteLine("Volume198: {0}", node.Volume198)
        Console.WriteLine("Volume199: {0}", node.Volume199)
        Console.WriteLine("Volume200: {0}", node.Volume200)
        Console.WriteLine("CustomerKey: {0}", node.CustomerKey)
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

    $req->TreeType = 1;
    $req->CustomerID = 1;
    $req->PeriodType = 1;
    $req->PeriodID = 1;
    $req->CustomerKey = "1";
    $req->BatchOffset = 1;

    //Send Request to Server and Get Response
    $res = $api.GetUpline($req);

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
    GetUplineRequest req = new GetUplineRequest();

    req.setTreeType(1);
    req.setCustomerID(1);
    req.setPeriodType(1);
    req.setPeriodID(1);
    req.setCustomerKey("1");
    req.setBatchOffset(1);

    //Send Request to Server and Get Response
    GetUplineResponse res = api.getExigoApiSoap().getUpline(req, auth);

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
https://api.exigo.com/3.0/csv/?method=GetUpline
&ApiLoginName=String
&ApiPassword=String
&ApiCompany=String
&TreeType=TreeType
&CustomerID=Int32
&PeriodType=Int32
&PeriodID=Nullable`1
&CustomerKey=String
&BatchSize=Nullable`1
&BatchOffset=Nullable`1
Response FieldsCustomerID,NodeID,ParentID,Level,Position,CustomerType,CustomerStatus,RankID,PayRankID,FirstName,LastName,Company,Email,Phone,CreatedDate,Volume1,Volume2,Volume3,Volume4,Volume5,Volume6,Volume7,Volume8,Volume9,Volume10,Volume11,Volume12,Volume13,Volume14,Volume15,Volume16,Volume17,Volume18,Volume19,Volume20,Volume21,Volume22,Volume23,Volume24,Volume25,Volume26,Volume27,Volume28,Volume29,Volume30,Volume31,Volume32,Volume33,Volume34,Volume35,Volume36,Volume37,Volume38,Volume39,Volume40,Volume41,Volume42,Volume43,Volume44,Volume45,Volume46,Volume47,Volume48,Volume49,Volume50,Volume51,Volume52,Volume53,Volume54,Volume55,Volume56,Volume57,Volume58,Volume59,Volume60,Volume61,Volume62,Volume63,Volume64,Volume65,Volume66,Volume67,Volume68,Volume69,Volume70,Volume71,Volume72,Volume73,Volume74,Volume75,Volume76,Volume77,Volume78,Volume79,Volume80,Volume81,Volume82,Volume83,Volume84,Volume85,Volume86,Volume87,Volume88,Volume89,Volume90,Volume91,Volume92,Volume93,Volume94,Volume95,Volume96,Volume97,Volume98,Volume99,Volume100,Volume101,Volume102,Volume103,Volume104,Volume105,Volume106,Volume107,Volume108,Volume109,Volume110,Volume111,Volume112,Volume113,Volume114,Volume115,Volume116,Volume117,Volume118,Volume119,Volume120,Volume121,Volume122,Volume123,Volume124,Volume125,Volume126,Volume127,Volume128,Volume129,Volume130,Volume131,Volume132,Volume133,Volume134,Volume135,Volume136,Volume137,Volume138,Volume139,Volume140,Volume141,Volume142,Volume143,Volume144,Volume145,Volume146,Volume147,Volume148,Volume149,Volume150,Volume151,Volume152,Volume153,Volume154,Volume155,Volume156,Volume157,Volume158,Volume159,Volume160,Volume161,Volume162,Volume163,Volume164,Volume165,Volume166,Volume167,Volume168,Volume169,Volume170,Volume171,Volume172,Volume173,Volume174,Volume175,Volume176,Volume177,Volume178,Volume179,Volume180,Volume181,Volume182,Volume183,Volume184,Volume185,Volume186,Volume187,Volume188,Volume189,Volume190,Volume191,Volume192,Volume193,Volume194,Volume195,Volume196,Volume197,Volume198,Volume199,Volume200,CustomerKey
Int32,Int32,Int32,Int32,Int32,Int32,Int32,Int32,Int32,String,String,String,String,String,DateTime,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,String

                    © 2026 Exigo.
```

</details>

---

### GetVolumes

>  Returns volume records for a current period in a periodtype.

| | |
|---|---|
| Category | Reporting |
| REST | `GET /3.0/commissions/volumes?periodType=1` |
| SOAP action | `https://api.exigo.com/GetVolumes` |
| WSDL elements | `GetVolumesRequest` → `GetVolumesResult` |
| CSV output | Yes — `GET https://api.exigo.com/3.0/csv/?method=GetVolumes&ApiLoginName=…&ApiPassword=…&ApiCompany=…` |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetVolumes |

#### Input

**`GetVolumesRequest`**

| Property | Type | Notes |
|---|---|---|
| `PeriodType` | `Int32` | Optional. Required. Defaults to 0. |
| `PeriodID` | `Int32` | Optional. Will default to current period. |
| `CustomerID` | `Int32` | Optional. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`GetVolumesResponse`**

| Property | Type | Notes |
|---|---|---|
| `Volumes` | `VolumeResponse[]` | **Lookup:** company-specific list (see company-lists.md) |

**`VolumeResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| &nbsp;&nbsp;↳ `PeriodType` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `PeriodID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `PeriodDescription` | `String` |  |
| &nbsp;&nbsp;↳ `Volume1` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume2` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume3` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume4` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume5` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume6` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume7` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume8` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume9` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume10` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume11` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume12` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume13` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume14` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume15` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume16` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume17` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume18` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume19` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume20` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume21` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume22` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume23` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume24` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume25` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume26` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume27` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume28` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume29` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume30` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume31` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume32` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume33` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume34` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume35` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume36` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume37` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume38` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume39` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume40` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume41` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume42` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume43` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume44` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume45` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume46` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume47` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume48` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume49` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume50` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume51` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume52` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume53` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume54` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume55` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume56` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume57` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume58` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume59` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume60` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume61` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume62` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume63` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume64` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume65` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume66` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume67` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume68` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume69` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume70` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume71` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume72` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume73` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume74` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume75` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume76` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume77` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume78` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume79` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume80` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume81` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume82` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume83` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume84` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume85` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume86` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume87` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume88` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume89` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume90` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume91` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume92` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume93` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume94` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume95` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume96` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume97` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume98` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume99` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume100` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `RankID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `PaidRankID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume101` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume102` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume103` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume104` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume105` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume106` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume107` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume108` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume109` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume110` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume111` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume112` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume113` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume114` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume115` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume116` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume117` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume118` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume119` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume120` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume121` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume122` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume123` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume124` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume125` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume126` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume127` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume128` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume129` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume130` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume131` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume132` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume133` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume134` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume135` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume136` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume137` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume138` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume139` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume140` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume141` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume142` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume143` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume144` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume145` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume146` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume147` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume148` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume149` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume150` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume151` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume152` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume153` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume154` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume155` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume156` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume157` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume158` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume159` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume160` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume161` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume162` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume163` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume164` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume165` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume166` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume167` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume168` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume169` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume170` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume171` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume172` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume173` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume174` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume175` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume176` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume177` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume178` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume179` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume180` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume181` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume182` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume183` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume184` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume185` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume186` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume187` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume188` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume189` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume190` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume191` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume192` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume193` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume194` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume195` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume196` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume197` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume198` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume199` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `Volume200` | `Decimal` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `CustomerKey` | `String` | Unique alpha numeric identifier for customer record . |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/commissions/volumes?periodType=1
  &periodID=1
  &customerID=1
  &customerKey=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "volumes": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetVolumes"

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
    <GetVolumesRequest xmlns="http://api.exigo.com/">
      <PeriodType>int</PeriodType>
      <PeriodID>int</PeriodID>
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
    </GetVolumesRequest>
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
    <GetVolumesResult xmlns="http://api.exigo.com/">
      <Volumes>
        <VolumeResponse>
          <CustomerID>int</CustomerID>
          <PeriodType>int</PeriodType>
          <PeriodID>int</PeriodID>
          <PeriodDescription>string</PeriodDescription>
          <Volume1>decimal</Volume1>
          <Volume2>decimal</Volume2>
          <Volume3>decimal</Volume3>
          <Volume4>decimal</Volume4>
          <Volume5>decimal</Volume5>
          <Volume6>decimal</Volume6>
          <Volume7>decimal</Volume7>
          <Volume8>decimal</Volume8>
          <Volume9>decimal</Volume9>
          <Volume10>decimal</Volume10>
          <Volume11>decimal</Volume11>
          <Volume12>decimal</Volume12>
          <Volume13>decimal</Volume13>
          <Volume14>decimal</Volume14>
          <Volume15>decimal</Volume15>
          <Volume16>decimal</Volume16>
          <Volume17>decimal</Volume17>
          <Volume18>decimal</Volume18>
          <Volume19>decimal</Volume19>
          <Volume20>decimal</Volume20>
          <Volume21>decimal</Volume21>
          <Volume22>decimal</Volume22>
          <Volume23>decimal</Volume23>
          <Volume24>decimal</Volume24>
          <Volume25>decimal</Volume25>
          <Volume26>decimal</Volume26>
          <Volume27>decimal</Volume27>
          <Volume28>decimal</Volume28>
          <Volume29>decimal</Volume29>
          <Volume30>decimal</Volume30>
          <Volume31>decimal</Volume31>
          <Volume32>decimal</Volume32>
          <Volume33>decimal</Volume33>
          <Volume34>decimal</Volume34>
          <Volume35>decimal</Volume35>
          <Volume36>decimal</Volume36>
          <Volume37>decimal</Volume37>
          <Volume38>decimal</Volume38>
          <Volume39>decimal</Volume39>
          <Volume40>decimal</Volume40>
          <Volume41>decimal</Volume41>
          <Volume42>decimal</Volume42>
          <Volume43>decimal</Volume43>
          <Volume44>decimal</Volume44>
          <Volume45>decimal</Volume45>
          <Volume46>decimal</Volume46>
          <Volume47>decimal</Volume47>
          <Volume48>decimal</Volume48>
          <Volume49>decimal</Volume49>
          <Volume50>decimal</Volume50>
          <Volume51>decimal</Volume51>
          <Volume52>decimal</Volume52>
          <Volume53>decimal</Volume53>
          <Volume54>decimal</Volume54>
          <Volume55>decimal</Volume55>
          <Volume56>decimal</Volume56>
          <Volume57>decimal</Volume57>
          <Volume58>decimal</Volume58>
          <Volume59>decimal</Volume59>
          <Volume60>decimal</Volume60>
          <Volume61>decimal</Volume61>
          <Volume62>decimal</Volume62>
          <Volume63>decimal</Volume63>
          <Volume64>decimal</Volume64>
          <Volume65>decimal</Volume65>
          <Volume66>decimal</Volume66>
          <Volume67>decimal</Volume67>
          <Volume68>decimal</Volume68>
          <Volume69>decimal</Volume69>
          <Volume70>decimal</Volume70>
          <Volume71>decimal</Volume71>
          <Volume72>decimal</Volume72>
          <Volume73>decimal</Volume73>
          <Volume74>decimal</Volume74>
          <Volume75>decimal</Volume75>
          <Volume76>decimal</Volume76>
          <Volume77>decimal</Volume77>
          <Volume78>decimal</Volume78>
          <Volume79>decimal</Volume79>
          <Volume80>decimal</Volume80>
          <Volume81>decimal</Volume81>
          <Volume82>decimal</Volume82>
          <Volume83>decimal</Volume83>
          <Volume84>decimal</Volume84>
          <Volume85>decimal</Volume85>
          <Volume86>decimal</Volume86>
          <Volume87>decimal</Volume87>
          <Volume88>decimal</Volume88>
          <Volume89>decimal</Volume89>
          <Volume90>decimal</Volume90>
          <Volume91>decimal</Volume91>
          <Volume92>decimal</Volume92>
          <Volume93>decimal</Volume93>
          <Volume94>decimal</Volume94>
          <Volume95>decimal</Volume95>
          <Volume96>decimal</Volume96>
          <Volume97>decimal</Volume97>
          <Volume98>decimal</Volume98>
          <Volume99>decimal</Volume99>
          <Volume100>decimal</Volume100>
          <RankID>int</RankID>
          <PaidRankID>int</PaidRankID>
          <Volume101>decimal</Volume101>
          <Volume102>decimal</Volume102>
          <Volume103>decimal</Volume103>
          <Volume104>decimal</Volume104>
          <Volume105>decimal</Volume105>
          <Volume106>decimal</Volume106>
          <Volume107>decimal</Volume107>
          <Volume108>decimal</Volume108>
          <Volume109>decimal</Volume109>
          <Volume110>decimal</Volume110>
          <Volume111>decimal</Volume111>
          <Volume112>decimal</Volume112>
          <Volume113>decimal</Volume113>
          <Volume114>decimal</Volume114>
          <Volume115>decimal</Volume115>
          <Volume116>decimal</Volume116>
          <Volume117>decimal</Volume117>
          <Volume118>decimal</Volume118>
          <Volume119>decimal</Volume119>
          <Volume120>decimal</Volume120>
          <Volume121>decimal</Volume121>
          <Volume122>decimal</Volume122>
          <Volume123>decimal</Volume123>
          <Volume124>decimal</Volume124>
          <Volume125>decimal</Volume125>
          <Volume126>decimal</Volume126>
          <Volume127>decimal</Volume127>
          <Volume128>decimal</Volume128>
          <Volume129>decimal</Volume129>
          <Volume130>decimal</Volume130>
          <Volume131>decimal</Volume131>
          <Volume132>decimal</Volume132>
          <Volume133>decimal</Volume133>
          <Volume134>decimal</Volume134>
          <Volume135>decimal</Volume135>
          <Volume136>decimal</Volume136>
          <Volume137>decimal</Volume137>
          <Volume138>decimal</Volume138>
          <Volume139>decimal</Volume139>
          <Volume140>decimal</Volume140>
          <Volume141>decimal</Volume141>
          <Volume142>decimal</Volume142>
          <Volume143>decimal</Volume143>
          <Volume144>decimal</Volume144>
          <Volume145>decimal</Volume145>
          <Volume146>decimal</Volume146>
          <Volume147>decimal</Volume147>
          <Volume148>decimal</Volume148>
          <Volume149>decimal</Volume149>
          <Volume150>decimal</Volume150>
          <Volume151>decimal</Volume151>
          <Volume152>decimal</Volume152>
          <Volume153>decimal</Volume153>
          <Volume154>decimal</Volume154>
          <Volume155>decimal</Volume155>
          <Volume156>decimal</Volume156>
          <Volume157>decimal</Volume157>
          <Volume158>decimal</Volume158>
          <Volume159>decimal</Volume159>
          <Volume160>decimal</Volume160>
          <Volume161>decimal</Volume161>
          <Volume162>decimal</Volume162>
          <Volume163>decimal</Volume163>
          <Volume164>decimal</Volume164>
          <Volume165>decimal</Volume165>
          <Volume166>decimal</Volume166>
          <Volume167>decimal</Volume167>
          <Volume168>decimal</Volume168>
          <Volume169>decimal</Volume169>
          <Volume170>decimal</Volume170>
          <Volume171>decimal</Volume171>
          <Volume172>decimal</Volume172>
          <Volume173>decimal</Volume173>
          <Volume174>decimal</Volume174>
          <Volume175>decimal</Volume175>
          <Volume176>decimal</Volume176>
          <Volume177>decimal</Volume177>
          <Volume178>decimal</Volume178>
          <Volume179>decimal</Volume179>
          <Volume180>decimal</Volume180>
          <Volume181>decimal</Volume181>
          <Volume182>decimal</Volume182>
          <Volume183>decimal</Volume183>
          <Volume184>decimal</Volume184>
          <Volume185>decimal</Volume185>
          <Volume186>decimal</Volume186>
          <Volume187>decimal</Volume187>
          <Volume188>decimal</Volume188>
          <Volume189>decimal</Volume189>
          <Volume190>decimal</Volume190>
          <Volume191>decimal</Volume191>
          <Volume192>decimal</Volume192>
          <Volume193>decimal</Volume193>
          <Volume194>decimal</Volume194>
          <Volume195>decimal</Volume195>
          <Volume196>decimal</Volume196>
          <Volume197>decimal</Volume197>
          <Volume198>decimal</Volume198>
          <Volume199>decimal</Volume199>
          <Volume200>decimal</Volume200>
          <CustomerKey>string</CustomerKey>
        </VolumeResponse>
      </Volumes>
    </GetVolumesResult>
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
    var req = new GetVolumesRequest();

    req.PeriodType = 1;             //Required.
    req.PeriodID = 1;               //Will default to current period.
    req.CustomerID = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.GetVolumesAsync(req);

    //Now examine the results:

    foreach (var volume  in res.Volumes)
    {
        Console.WriteLine("CustomerID: {0}", volume.CustomerID);
        Console.WriteLine("PeriodType: {0}", volume.PeriodType);
        Console.WriteLine("PeriodID: {0}", volume.PeriodID);
        Console.WriteLine("PeriodDescription: {0}", volume.PeriodDescription);
        Console.WriteLine("Volume1: {0}", volume.Volume1);
        Console.WriteLine("Volume2: {0}", volume.Volume2);
        Console.WriteLine("Volume3: {0}", volume.Volume3);
        Console.WriteLine("Volume4: {0}", volume.Volume4);
        Console.WriteLine("Volume5: {0}", volume.Volume5);
        Console.WriteLine("Volume6: {0}", volume.Volume6);
        Console.WriteLine("Volume7: {0}", volume.Volume7);
        Console.WriteLine("Volume8: {0}", volume.Volume8);
        Console.WriteLine("Volume9: {0}", volume.Volume9);
        Console.WriteLine("Volume10: {0}", volume.Volume10);
        Console.WriteLine("Volume11: {0}", volume.Volume11);
        Console.WriteLine("Volume12: {0}", volume.Volume12);
        Console.WriteLine("Volume13: {0}", volume.Volume13);
        Console.WriteLine("Volume14: {0}", volume.Volume14);
        Console.WriteLine("Volume15: {0}", volume.Volume15);
        Console.WriteLine("Volume16: {0}", volume.Volume16);
        Console.WriteLine("Volume17: {0}", volume.Volume17);
        Console.WriteLine("Volume18: {0}", volume.Volume18);
        Console.WriteLine("Volume19: {0}", volume.Volume19);
        Console.WriteLine("Volume20: {0}", volume.Volume20);
        Console.WriteLine("Volume21: {0}", volume.Volume21);
        Console.WriteLine("Volume22: {0}", volume.Volume22);
        Console.WriteLine("Volume23: {0}", volume.Volume23);
        Console.WriteLine("Volume24: {0}", volume.Volume24);
        Console.WriteLine("Volume25: {0}", volume.Volume25);
        Console.WriteLine("Volume26: {0}", volume.Volume26);
        Console.WriteLine("Volume27: {0}", volume.Volume27);
        Console.WriteLine("Volume28: {0}", volume.Volume28);
        Console.WriteLine("Volume29: {0}", volume.Volume29);
        Console.WriteLine("Volume30: {0}", volume.Volume30);
        Console.WriteLine("Volume31: {0}", volume.Volume31);
        Console.WriteLine("Volume32: {0}", volume.Volume32);
        Console.WriteLine("Volume33: {0}", volume.Volume33);
        Console.WriteLine("Volume34: {0}", volume.Volume34);
        Console.WriteLine("Volume35: {0}", volume.Volume35);
        Console.WriteLine("Volume36: {0}", volume.Volume36);
        Console.WriteLine("Volume37: {0}", volume.Volume37);
        Console.WriteLine("Volume38: {0}", volume.Volume38);
        Console.WriteLine("Volume39: {0}", volume.Volume39);
        Console.WriteLine("Volume40: {0}", volume.Volume40);
        Console.WriteLine("Volume41: {0}", volume.Volume41);
        Console.WriteLine("Volume42: {0}", volume.Volume42);
        Console.WriteLine("Volume43: {0}", volume.Volume43);
        Console.WriteLine("Volume44: {0}", volume.Volume44);
        Console.WriteLine("Volume45: {0}", volume.Volume45);
        Console.WriteLine("Volume46: {0}", volume.Volume46);
        Console.WriteLine("Volume47: {0}", volume.Volume47);
        Console.WriteLine("Volume48: {0}", volume.Volume48);
        Console.WriteLine("Volume49: {0}", volume.Volume49);
        Console.WriteLine("Volume50: {0}", volume.Volume50);
        Console.WriteLine("Volume51: {0}", volume.Volume51);
        Console.WriteLine("Volume52: {0}", volume.Volume52);
        Console.WriteLine("Volume53: {0}", volume.Volume53);
        Console.WriteLine("Volume54: {0}", volume.Volume54);
        Console.WriteLine("Volume55: {0}", volume.Volume55);
        Console.WriteLine("Volume56: {0}", volume.Volume56);
        Console.WriteLine("Volume57: {0}", volume.Volume57);
        Console.WriteLine("Volume58: {0}", volume.Volume58);
        Console.WriteLine("Volume59: {0}", volume.Volume59);
        Console.WriteLine("Volume60: {0}", volume.Volume60);
        Console.WriteLine("Volume61: {0}", volume.Volume61);
        Console.WriteLine("Volume62: {0}", volume.Volume62);
        Console.WriteLine("Volume63: {0}", volume.Volume63);
        Console.WriteLine("Volume64: {0}", volume.Volume64);
        Console.WriteLine("Volume65: {0}", volume.Volume65);
        Console.WriteLine("Volume66: {0}", volume.Volume66);
        Console.WriteLine("Volume67: {0}", volume.Volume67);
        Console.WriteLine("Volume68: {0}", volume.Volume68);
        Console.WriteLine("Volume69: {0}", volume.Volume69);
        Console.WriteLine("Volume70: {0}", volume.Volume70);
        Console.WriteLine("Volume71: {0}", volume.Volume71);
        Console.WriteLine("Volume72: {0}", volume.Volume72);
        Console.WriteLine("Volume73: {0}", volume.Volume73);
        Console.WriteLine("Volume74: {0}", volume.Volume74);
        Console.WriteLine("Volume75: {0}", volume.Volume75);
        Console.WriteLine("Volume76: {0}", volume.Volume76);
        Console.WriteLine("Volume77: {0}", volume.Volume77);
        Console.WriteLine("Volume78: {0}", volume.Volume78);
        Console.WriteLine("Volume79: {0}", volume.Volume79);
        Console.WriteLine("Volume80: {0}", volume.Volume80);
        Console.WriteLine("Volume81: {0}", volume.Volume81);
        Console.WriteLine("Volume82: {0}", volume.Volume82);
        Console.WriteLine("Volume83: {0}", volume.Volume83);
        Console.WriteLine("Volume84: {0}", volume.Volume84);
        Console.WriteLine("Volume85: {0}", volume.Volume85);
        Console.WriteLine("Volume86: {0}", volume.Volume86);
        Console.WriteLine("Volume87: {0}", volume.Volume87);
        Console.WriteLine("Volume88: {0}", volume.Volume88);
        Console.WriteLine("Volume89: {0}", volume.Volume89);
        Console.WriteLine("Volume90: {0}", volume.Volume90);
        Console.WriteLine("Volume91: {0}", volume.Volume91);
        Console.WriteLine("Volume92: {0}", volume.Volume92);
        Console.WriteLine("Volume93: {0}", volume.Volume93);
        Console.WriteLine("Volume94: {0}", volume.Volume94);
        Console.WriteLine("Volume95: {0}", volume.Volume95);
        Console.WriteLine("Volume96: {0}", volume.Volume96);
        Console.WriteLine("Volume97: {0}", volume.Volume97);
        Console.WriteLine("Volume98: {0}", volume.Volume98);
        Console.WriteLine("Volume99: {0}", volume.Volume99);
        Console.WriteLine("Volume100: {0}", volume.Volume100);
        Console.WriteLine("RankID: {0}", volume.RankID);
        Console.WriteLine("PaidRankID: {0}", volume.PaidRankID);
        Console.WriteLine("Volume101: {0}", volume.Volume101);
        Console.WriteLine("Volume102: {0}", volume.Volume102);
        Console.WriteLine("Volume103: {0}", volume.Volume103);
        Console.WriteLine("Volume104: {0}", volume.Volume104);
        Console.WriteLine("Volume105: {0}", volume.Volume105);
        Console.WriteLine("Volume106: {0}", volume.Volume106);
        Console.WriteLine("Volume107: {0}", volume.Volume107);
        Console.WriteLine("Volume108: {0}", volume.Volume108);
        Console.WriteLine("Volume109: {0}", volume.Volume109);
        Console.WriteLine("Volume110: {0}", volume.Volume110);
        Console.WriteLine("Volume111: {0}", volume.Volume111);
        Console.WriteLine("Volume112: {0}", volume.Volume112);
        Console.WriteLine("Volume113: {0}", volume.Volume113);
        Console.WriteLine("Volume114: {0}", volume.Volume114);
        Console.WriteLine("Volume115: {0}", volume.Volume115);
        Console.WriteLine("Volume116: {0}", volume.Volume116);
        Console.WriteLine("Volume117: {0}", volume.Volume117);
        Console.WriteLine("Volume118: {0}", volume.Volume118);
        Console.WriteLine("Volume119: {0}", volume.Volume119);
        Console.WriteLine("Volume120: {0}", volume.Volume120);
        Console.WriteLine("Volume121: {0}", volume.Volume121);
        Console.WriteLine("Volume122: {0}", volume.Volume122);
        Console.WriteLine("Volume123: {0}", volume.Volume123);
        Console.WriteLine("Volume124: {0}", volume.Volume124);
        Console.WriteLine("Volume125: {0}", volume.Volume125);
        Console.WriteLine("Volume126: {0}", volume.Volume126);
        Console.WriteLine("Volume127: {0}", volume.Volume127);
        Console.WriteLine("Volume128: {0}", volume.Volume128);
        Console.WriteLine("Volume129: {0}", volume.Volume129);
        Console.WriteLine("Volume130: {0}", volume.Volume130);
        Console.WriteLine("Volume131: {0}", volume.Volume131);
        Console.WriteLine("Volume132: {0}", volume.Volume132);
        Console.WriteLine("Volume133: {0}", volume.Volume133);
        Console.WriteLine("Volume134: {0}", volume.Volume134);
        Console.WriteLine("Volume135: {0}", volume.Volume135);
        Console.WriteLine("Volume136: {0}", volume.Volume136);
        Console.WriteLine("Volume137: {0}", volume.Volume137);
        Console.WriteLine("Volume138: {0}", volume.Volume138);
        Console.WriteLine("Volume139: {0}", volume.Volume139);
        Console.WriteLine("Volume140: {0}", volume.Volume140);
        Console.WriteLine("Volume141: {0}", volume.Volume141);
        Console.WriteLine("Volume142: {0}", volume.Volume142);
        Console.WriteLine("Volume143: {0}", volume.Volume143);
        Console.WriteLine("Volume144: {0}", volume.Volume144);
        Console.WriteLine("Volume145: {0}", volume.Volume145);
        Console.WriteLine("Volume146: {0}", volume.Volume146);
        Console.WriteLine("Volume147: {0}", volume.Volume147);
        Console.WriteLine("Volume148: {0}", volume.Volume148);
        Console.WriteLine("Volume149: {0}", volume.Volume149);
        Console.WriteLine("Volume150: {0}", volume.Volume150);
        Console.WriteLine("Volume151: {0}", volume.Volume151);
        Console.WriteLine("Volume152: {0}", volume.Volume152);
        Console.WriteLine("Volume153: {0}", volume.Volume153);
        Console.WriteLine("Volume154: {0}", volume.Volume154);
        Console.WriteLine("Volume155: {0}", volume.Volume155);
        Console.WriteLine("Volume156: {0}", volume.Volume156);
        Console.WriteLine("Volume157: {0}", volume.Volume157);
        Console.WriteLine("Volume158: {0}", volume.Volume158);
        Console.WriteLine("Volume159: {0}", volume.Volume159);
        Console.WriteLine("Volume160: {0}", volume.Volume160);
        Console.WriteLine("Volume161: {0}", volume.Volume161);
        Console.WriteLine("Volume162: {0}", volume.Volume162);
        Console.WriteLine("Volume163: {0}", volume.Volume163);
        Console.WriteLine("Volume164: {0}", volume.Volume164);
        Console.WriteLine("Volume165: {0}", volume.Volume165);
        Console.WriteLine("Volume166: {0}", volume.Volume166);
        Console.WriteLine("Volume167: {0}", volume.Volume167);
        Console.WriteLine("Volume168: {0}", volume.Volume168);
        Console.WriteLine("Volume169: {0}", volume.Volume169);
        Console.WriteLine("Volume170: {0}", volume.Volume170);
        Console.WriteLine("Volume171: {0}", volume.Volume171);
        Console.WriteLine("Volume172: {0}", volume.Volume172);
        Console.WriteLine("Volume173: {0}", volume.Volume173);
        Console.WriteLine("Volume174: {0}", volume.Volume174);
        Console.WriteLine("Volume175: {0}", volume.Volume175);
        Console.WriteLine("Volume176: {0}", volume.Volume176);
        Console.WriteLine("Volume177: {0}", volume.Volume177);
        Console.WriteLine("Volume178: {0}", volume.Volume178);
        Console.WriteLine("Volume179: {0}", volume.Volume179);
        Console.WriteLine("Volume180: {0}", volume.Volume180);
        Console.WriteLine("Volume181: {0}", volume.Volume181);
        Console.WriteLine("Volume182: {0}", volume.Volume182);
        Console.WriteLine("Volume183: {0}", volume.Volume183);
        Console.WriteLine("Volume184: {0}", volume.Volume184);
        Console.WriteLine("Volume185: {0}", volume.Volume185);
        Console.WriteLine("Volume186: {0}", volume.Volume186);
        Console.WriteLine("Volume187: {0}", volume.Volume187);
        Console.WriteLine("Volume188: {0}", volume.Volume188);
        Console.WriteLine("Volume189: {0}", volume.Volume189);
        Console.WriteLine("Volume190: {0}", volume.Volume190);
        Console.WriteLine("Volume191: {0}", volume.Volume191);
        Console.WriteLine("Volume192: {0}", volume.Volume192);
        Console.WriteLine("Volume193: {0}", volume.Volume193);
        Console.WriteLine("Volume194: {0}", volume.Volume194);
        Console.WriteLine("Volume195: {0}", volume.Volume195);
        Console.WriteLine("Volume196: {0}", volume.Volume196);
        Console.WriteLine("Volume197: {0}", volume.Volume197);
        Console.WriteLine("Volume198: {0}", volume.Volume198);
        Console.WriteLine("Volume199: {0}", volume.Volume199);
        Console.WriteLine("Volume200: {0}", volume.Volume200);
        Console.WriteLine("CustomerKey: {0}", volume.CustomerKey);
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
    GetVolumesRequest req = new GetVolumesRequest();

    req.PeriodType = 1;             //Required.
    req.PeriodID = 1;               //Will default to current period.
    req.CustomerID = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    GetVolumesResponse res = api.GetVolumes(req);

    //Now examine the results:

    foreach (VolumeResponse volume  in res.Volumes)
    {
        Console.WriteLine("CustomerID: {0}", volume.CustomerID);
        Console.WriteLine("PeriodType: {0}", volume.PeriodType);
        Console.WriteLine("PeriodID: {0}", volume.PeriodID);
        Console.WriteLine("PeriodDescription: {0}", volume.PeriodDescription);
        Console.WriteLine("Volume1: {0}", volume.Volume1);
        Console.WriteLine("Volume2: {0}", volume.Volume2);
        Console.WriteLine("Volume3: {0}", volume.Volume3);
        Console.WriteLine("Volume4: {0}", volume.Volume4);
        Console.WriteLine("Volume5: {0}", volume.Volume5);
        Console.WriteLine("Volume6: {0}", volume.Volume6);
        Console.WriteLine("Volume7: {0}", volume.Volume7);
        Console.WriteLine("Volume8: {0}", volume.Volume8);
        Console.WriteLine("Volume9: {0}", volume.Volume9);
        Console.WriteLine("Volume10: {0}", volume.Volume10);
        Console.WriteLine("Volume11: {0}", volume.Volume11);
        Console.WriteLine("Volume12: {0}", volume.Volume12);
        Console.WriteLine("Volume13: {0}", volume.Volume13);
        Console.WriteLine("Volume14: {0}", volume.Volume14);
        Console.WriteLine("Volume15: {0}", volume.Volume15);
        Console.WriteLine("Volume16: {0}", volume.Volume16);
        Console.WriteLine("Volume17: {0}", volume.Volume17);
        Console.WriteLine("Volume18: {0}", volume.Volume18);
        Console.WriteLine("Volume19: {0}", volume.Volume19);
        Console.WriteLine("Volume20: {0}", volume.Volume20);
        Console.WriteLine("Volume21: {0}", volume.Volume21);
        Console.WriteLine("Volume22: {0}", volume.Volume22);
        Console.WriteLine("Volume23: {0}", volume.Volume23);
        Console.WriteLine("Volume24: {0}", volume.Volume24);
        Console.WriteLine("Volume25: {0}", volume.Volume25);
        Console.WriteLine("Volume26: {0}", volume.Volume26);
        Console.WriteLine("Volume27: {0}", volume.Volume27);
        Console.WriteLine("Volume28: {0}", volume.Volume28);
        Console.WriteLine("Volume29: {0}", volume.Volume29);
        Console.WriteLine("Volume30: {0}", volume.Volume30);
        Console.WriteLine("Volume31: {0}", volume.Volume31);
        Console.WriteLine("Volume32: {0}", volume.Volume32);
        Console.WriteLine("Volume33: {0}", volume.Volume33);
        Console.WriteLine("Volume34: {0}", volume.Volume34);
        Console.WriteLine("Volume35: {0}", volume.Volume35);
        Console.WriteLine("Volume36: {0}", volume.Volume36);
        Console.WriteLine("Volume37: {0}", volume.Volume37);
        Console.WriteLine("Volume38: {0}", volume.Volume38);
        Console.WriteLine("Volume39: {0}", volume.Volume39);
        Console.WriteLine("Volume40: {0}", volume.Volume40);
        Console.WriteLine("Volume41: {0}", volume.Volume41);
        Console.WriteLine("Volume42: {0}", volume.Volume42);
        Console.WriteLine("Volume43: {0}", volume.Volume43);
        Console.WriteLine("Volume44: {0}", volume.Volume44);
        Console.WriteLine("Volume45: {0}", volume.Volume45);
        Console.WriteLine("Volume46: {0}", volume.Volume46);
        Console.WriteLine("Volume47: {0}", volume.Volume47);
        Console.WriteLine("Volume48: {0}", volume.Volume48);
        Console.WriteLine("Volume49: {0}", volume.Volume49);
        Console.WriteLine("Volume50: {0}", volume.Volume50);
        Console.WriteLine("Volume51: {0}", volume.Volume51);
        Console.WriteLine("Volume52: {0}", volume.Volume52);
        Console.WriteLine("Volume53: {0}", volume.Volume53);
        Console.WriteLine("Volume54: {0}", volume.Volume54);
        Console.WriteLine("Volume55: {0}", volume.Volume55);
        Console.WriteLine("Volume56: {0}", volume.Volume56);
        Console.WriteLine("Volume57: {0}", volume.Volume57);
        Console.WriteLine("Volume58: {0}", volume.Volume58);
        Console.WriteLine("Volume59: {0}", volume.Volume59);
        Console.WriteLine("Volume60: {0}", volume.Volume60);
        Console.WriteLine("Volume61: {0}", volume.Volume61);
        Console.WriteLine("Volume62: {0}", volume.Volume62);
        Console.WriteLine("Volume63: {0}", volume.Volume63);
        Console.WriteLine("Volume64: {0}", volume.Volume64);
        Console.WriteLine("Volume65: {0}", volume.Volume65);
        Console.WriteLine("Volume66: {0}", volume.Volume66);
        Console.WriteLine("Volume67: {0}", volume.Volume67);
        Console.WriteLine("Volume68: {0}", volume.Volume68);
        Console.WriteLine("Volume69: {0}", volume.Volume69);
        Console.WriteLine("Volume70: {0}", volume.Volume70);
        Console.WriteLine("Volume71: {0}", volume.Volume71);
        Console.WriteLine("Volume72: {0}", volume.Volume72);
        Console.WriteLine("Volume73: {0}", volume.Volume73);
        Console.WriteLine("Volume74: {0}", volume.Volume74);
        Console.WriteLine("Volume75: {0}", volume.Volume75);
        Console.WriteLine("Volume76: {0}", volume.Volume76);
        Console.WriteLine("Volume77: {0}", volume.Volume77);
        Console.WriteLine("Volume78: {0}", volume.Volume78);
        Console.WriteLine("Volume79: {0}", volume.Volume79);
        Console.WriteLine("Volume80: {0}", volume.Volume80);
        Console.WriteLine("Volume81: {0}", volume.Volume81);
        Console.WriteLine("Volume82: {0}", volume.Volume82);
        Console.WriteLine("Volume83: {0}", volume.Volume83);
        Console.WriteLine("Volume84: {0}", volume.Volume84);
        Console.WriteLine("Volume85: {0}", volume.Volume85);
        Console.WriteLine("Volume86: {0}", volume.Volume86);
        Console.WriteLine("Volume87: {0}", volume.Volume87);
        Console.WriteLine("Volume88: {0}", volume.Volume88);
        Console.WriteLine("Volume89: {0}", volume.Volume89);
        Console.WriteLine("Volume90: {0}", volume.Volume90);
        Console.WriteLine("Volume91: {0}", volume.Volume91);
        Console.WriteLine("Volume92: {0}", volume.Volume92);
        Console.WriteLine("Volume93: {0}", volume.Volume93);
        Console.WriteLine("Volume94: {0}", volume.Volume94);
        Console.WriteLine("Volume95: {0}", volume.Volume95);
        Console.WriteLine("Volume96: {0}", volume.Volume96);
        Console.WriteLine("Volume97: {0}", volume.Volume97);
        Console.WriteLine("Volume98: {0}", volume.Volume98);
        Console.WriteLine("Volume99: {0}", volume.Volume99);
        Console.WriteLine("Volume100: {0}", volume.Volume100);
        Console.WriteLine("RankID: {0}", volume.RankID);
        Console.WriteLine("PaidRankID: {0}", volume.PaidRankID);
        Console.WriteLine("Volume101: {0}", volume.Volume101);
        Console.WriteLine("Volume102: {0}", volume.Volume102);
        Console.WriteLine("Volume103: {0}", volume.Volume103);
        Console.WriteLine("Volume104: {0}", volume.Volume104);
        Console.WriteLine("Volume105: {0}", volume.Volume105);
        Console.WriteLine("Volume106: {0}", volume.Volume106);
        Console.WriteLine("Volume107: {0}", volume.Volume107);
        Console.WriteLine("Volume108: {0}", volume.Volume108);
        Console.WriteLine("Volume109: {0}", volume.Volume109);
        Console.WriteLine("Volume110: {0}", volume.Volume110);
        Console.WriteLine("Volume111: {0}", volume.Volume111);
        Console.WriteLine("Volume112: {0}", volume.Volume112);
        Console.WriteLine("Volume113: {0}", volume.Volume113);
        Console.WriteLine("Volume114: {0}", volume.Volume114);
        Console.WriteLine("Volume115: {0}", volume.Volume115);
        Console.WriteLine("Volume116: {0}", volume.Volume116);
        Console.WriteLine("Volume117: {0}", volume.Volume117);
        Console.WriteLine("Volume118: {0}", volume.Volume118);
        Console.WriteLine("Volume119: {0}", volume.Volume119);
        Console.WriteLine("Volume120: {0}", volume.Volume120);
        Console.WriteLine("Volume121: {0}", volume.Volume121);
        Console.WriteLine("Volume122: {0}", volume.Volume122);
        Console.WriteLine("Volume123: {0}", volume.Volume123);
        Console.WriteLine("Volume124: {0}", volume.Volume124);
        Console.WriteLine("Volume125: {0}", volume.Volume125);
        Console.WriteLine("Volume126: {0}", volume.Volume126);
        Console.WriteLine("Volume127: {0}", volume.Volume127);
        Console.WriteLine("Volume128: {0}", volume.Volume128);
        Console.WriteLine("Volume129: {0}", volume.Volume129);
        Console.WriteLine("Volume130: {0}", volume.Volume130);
        Console.WriteLine("Volume131: {0}", volume.Volume131);
        Console.WriteLine("Volume132: {0}", volume.Volume132);
        Console.WriteLine("Volume133: {0}", volume.Volume133);
        Console.WriteLine("Volume134: {0}", volume.Volume134);
        Console.WriteLine("Volume135: {0}", volume.Volume135);
        Console.WriteLine("Volume136: {0}", volume.Volume136);
        Console.WriteLine("Volume137: {0}", volume.Volume137);
        Console.WriteLine("Volume138: {0}", volume.Volume138);
        Console.WriteLine("Volume139: {0}", volume.Volume139);
        Console.WriteLine("Volume140: {0}", volume.Volume140);
        Console.WriteLine("Volume141: {0}", volume.Volume141);
        Console.WriteLine("Volume142: {0}", volume.Volume142);
        Console.WriteLine("Volume143: {0}", volume.Volume143);
        Console.WriteLine("Volume144: {0}", volume.Volume144);
        Console.WriteLine("Volume145: {0}", volume.Volume145);
        Console.WriteLine("Volume146: {0}", volume.Volume146);
        Console.WriteLine("Volume147: {0}", volume.Volume147);
        Console.WriteLine("Volume148: {0}", volume.Volume148);
        Console.WriteLine("Volume149: {0}", volume.Volume149);
        Console.WriteLine("Volume150: {0}", volume.Volume150);
        Console.WriteLine("Volume151: {0}", volume.Volume151);
        Console.WriteLine("Volume152: {0}", volume.Volume152);
        Console.WriteLine("Volume153: {0}", volume.Volume153);
        Console.WriteLine("Volume154: {0}", volume.Volume154);
        Console.WriteLine("Volume155: {0}", volume.Volume155);
        Console.WriteLine("Volume156: {0}", volume.Volume156);
        Console.WriteLine("Volume157: {0}", volume.Volume157);
        Console.WriteLine("Volume158: {0}", volume.Volume158);
        Console.WriteLine("Volume159: {0}", volume.Volume159);
        Console.WriteLine("Volume160: {0}", volume.Volume160);
        Console.WriteLine("Volume161: {0}", volume.Volume161);
        Console.WriteLine("Volume162: {0}", volume.Volume162);
        Console.WriteLine("Volume163: {0}", volume.Volume163);
        Console.WriteLine("Volume164: {0}", volume.Volume164);
        Console.WriteLine("Volume165: {0}", volume.Volume165);
        Console.WriteLine("Volume166: {0}", volume.Volume166);
        Console.WriteLine("Volume167: {0}", volume.Volume167);
        Console.WriteLine("Volume168: {0}", volume.Volume168);
        Console.WriteLine("Volume169: {0}", volume.Volume169);
        Console.WriteLine("Volume170: {0}", volume.Volume170);
        Console.WriteLine("Volume171: {0}", volume.Volume171);
        Console.WriteLine("Volume172: {0}", volume.Volume172);
        Console.WriteLine("Volume173: {0}", volume.Volume173);
        Console.WriteLine("Volume174: {0}", volume.Volume174);
        Console.WriteLine("Volume175: {0}", volume.Volume175);
        Console.WriteLine("Volume176: {0}", volume.Volume176);
        Console.WriteLine("Volume177: {0}", volume.Volume177);
        Console.WriteLine("Volume178: {0}", volume.Volume178);
        Console.WriteLine("Volume179: {0}", volume.Volume179);
        Console.WriteLine("Volume180: {0}", volume.Volume180);
        Console.WriteLine("Volume181: {0}", volume.Volume181);
        Console.WriteLine("Volume182: {0}", volume.Volume182);
        Console.WriteLine("Volume183: {0}", volume.Volume183);
        Console.WriteLine("Volume184: {0}", volume.Volume184);
        Console.WriteLine("Volume185: {0}", volume.Volume185);
        Console.WriteLine("Volume186: {0}", volume.Volume186);
        Console.WriteLine("Volume187: {0}", volume.Volume187);
        Console.WriteLine("Volume188: {0}", volume.Volume188);
        Console.WriteLine("Volume189: {0}", volume.Volume189);
        Console.WriteLine("Volume190: {0}", volume.Volume190);
        Console.WriteLine("Volume191: {0}", volume.Volume191);
        Console.WriteLine("Volume192: {0}", volume.Volume192);
        Console.WriteLine("Volume193: {0}", volume.Volume193);
        Console.WriteLine("Volume194: {0}", volume.Volume194);
        Console.WriteLine("Volume195: {0}", volume.Volume195);
        Console.WriteLine("Volume196: {0}", volume.Volume196);
        Console.WriteLine("Volume197: {0}", volume.Volume197);
        Console.WriteLine("Volume198: {0}", volume.Volume198);
        Console.WriteLine("Volume199: {0}", volume.Volume199);
        Console.WriteLine("Volume200: {0}", volume.Volume200);
        Console.WriteLine("CustomerKey: {0}", volume.CustomerKey);
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
    Dim req as new GetVolumesRequest()

    req.PeriodType = 1
    req.PeriodID = 1
    req.CustomerID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As GetVolumesResponse = api.GetVolumes(req)

    'Now examine the results:

    For Each volume As VolumeResponse In res.Volumes
        Console.WriteLine("CustomerID: {0}", volume.CustomerID)
        Console.WriteLine("PeriodType: {0}", volume.PeriodType)
        Console.WriteLine("PeriodID: {0}", volume.PeriodID)
        Console.WriteLine("PeriodDescription: {0}", volume.PeriodDescription)
        Console.WriteLine("Volume1: {0}", volume.Volume1)
        Console.WriteLine("Volume2: {0}", volume.Volume2)
        Console.WriteLine("Volume3: {0}", volume.Volume3)
        Console.WriteLine("Volume4: {0}", volume.Volume4)
        Console.WriteLine("Volume5: {0}", volume.Volume5)
        Console.WriteLine("Volume6: {0}", volume.Volume6)
        Console.WriteLine("Volume7: {0}", volume.Volume7)
        Console.WriteLine("Volume8: {0}", volume.Volume8)
        Console.WriteLine("Volume9: {0}", volume.Volume9)
        Console.WriteLine("Volume10: {0}", volume.Volume10)
        Console.WriteLine("Volume11: {0}", volume.Volume11)
        Console.WriteLine("Volume12: {0}", volume.Volume12)
        Console.WriteLine("Volume13: {0}", volume.Volume13)
        Console.WriteLine("Volume14: {0}", volume.Volume14)
        Console.WriteLine("Volume15: {0}", volume.Volume15)
        Console.WriteLine("Volume16: {0}", volume.Volume16)
        Console.WriteLine("Volume17: {0}", volume.Volume17)
        Console.WriteLine("Volume18: {0}", volume.Volume18)
        Console.WriteLine("Volume19: {0}", volume.Volume19)
        Console.WriteLine("Volume20: {0}", volume.Volume20)
        Console.WriteLine("Volume21: {0}", volume.Volume21)
        Console.WriteLine("Volume22: {0}", volume.Volume22)
        Console.WriteLine("Volume23: {0}", volume.Volume23)
        Console.WriteLine("Volume24: {0}", volume.Volume24)
        Console.WriteLine("Volume25: {0}", volume.Volume25)
        Console.WriteLine("Volume26: {0}", volume.Volume26)
        Console.WriteLine("Volume27: {0}", volume.Volume27)
        Console.WriteLine("Volume28: {0}", volume.Volume28)
        Console.WriteLine("Volume29: {0}", volume.Volume29)
        Console.WriteLine("Volume30: {0}", volume.Volume30)
        Console.WriteLine("Volume31: {0}", volume.Volume31)
        Console.WriteLine("Volume32: {0}", volume.Volume32)
        Console.WriteLine("Volume33: {0}", volume.Volume33)
        Console.WriteLine("Volume34: {0}", volume.Volume34)
        Console.WriteLine("Volume35: {0}", volume.Volume35)
        Console.WriteLine("Volume36: {0}", volume.Volume36)
        Console.WriteLine("Volume37: {0}", volume.Volume37)
        Console.WriteLine("Volume38: {0}", volume.Volume38)
        Console.WriteLine("Volume39: {0}", volume.Volume39)
        Console.WriteLine("Volume40: {0}", volume.Volume40)
        Console.WriteLine("Volume41: {0}", volume.Volume41)
        Console.WriteLine("Volume42: {0}", volume.Volume42)
        Console.WriteLine("Volume43: {0}", volume.Volume43)
        Console.WriteLine("Volume44: {0}", volume.Volume44)
        Console.WriteLine("Volume45: {0}", volume.Volume45)
        Console.WriteLine("Volume46: {0}", volume.Volume46)
        Console.WriteLine("Volume47: {0}", volume.Volume47)
        Console.WriteLine("Volume48: {0}", volume.Volume48)
        Console.WriteLine("Volume49: {0}", volume.Volume49)
        Console.WriteLine("Volume50: {0}", volume.Volume50)
        Console.WriteLine("Volume51: {0}", volume.Volume51)
        Console.WriteLine("Volume52: {0}", volume.Volume52)
        Console.WriteLine("Volume53: {0}", volume.Volume53)
        Console.WriteLine("Volume54: {0}", volume.Volume54)
        Console.WriteLine("Volume55: {0}", volume.Volume55)
        Console.WriteLine("Volume56: {0}", volume.Volume56)
        Console.WriteLine("Volume57: {0}", volume.Volume57)
        Console.WriteLine("Volume58: {0}", volume.Volume58)
        Console.WriteLine("Volume59: {0}", volume.Volume59)
        Console.WriteLine("Volume60: {0}", volume.Volume60)
        Console.WriteLine("Volume61: {0}", volume.Volume61)
        Console.WriteLine("Volume62: {0}", volume.Volume62)
        Console.WriteLine("Volume63: {0}", volume.Volume63)
        Console.WriteLine("Volume64: {0}", volume.Volume64)
        Console.WriteLine("Volume65: {0}", volume.Volume65)
        Console.WriteLine("Volume66: {0}", volume.Volume66)
        Console.WriteLine("Volume67: {0}", volume.Volume67)
        Console.WriteLine("Volume68: {0}", volume.Volume68)
        Console.WriteLine("Volume69: {0}", volume.Volume69)
        Console.WriteLine("Volume70: {0}", volume.Volume70)
        Console.WriteLine("Volume71: {0}", volume.Volume71)
        Console.WriteLine("Volume72: {0}", volume.Volume72)
        Console.WriteLine("Volume73: {0}", volume.Volume73)
        Console.WriteLine("Volume74: {0}", volume.Volume74)
        Console.WriteLine("Volume75: {0}", volume.Volume75)
        Console.WriteLine("Volume76: {0}", volume.Volume76)
        Console.WriteLine("Volume77: {0}", volume.Volume77)
        Console.WriteLine("Volume78: {0}", volume.Volume78)
        Console.WriteLine("Volume79: {0}", volume.Volume79)
        Console.WriteLine("Volume80: {0}", volume.Volume80)
        Console.WriteLine("Volume81: {0}", volume.Volume81)
        Console.WriteLine("Volume82: {0}", volume.Volume82)
        Console.WriteLine("Volume83: {0}", volume.Volume83)
        Console.WriteLine("Volume84: {0}", volume.Volume84)
        Console.WriteLine("Volume85: {0}", volume.Volume85)
        Console.WriteLine("Volume86: {0}", volume.Volume86)
        Console.WriteLine("Volume87: {0}", volume.Volume87)
        Console.WriteLine("Volume88: {0}", volume.Volume88)
        Console.WriteLine("Volume89: {0}", volume.Volume89)
        Console.WriteLine("Volume90: {0}", volume.Volume90)
        Console.WriteLine("Volume91: {0}", volume.Volume91)
        Console.WriteLine("Volume92: {0}", volume.Volume92)
        Console.WriteLine("Volume93: {0}", volume.Volume93)
        Console.WriteLine("Volume94: {0}", volume.Volume94)
        Console.WriteLine("Volume95: {0}", volume.Volume95)
        Console.WriteLine("Volume96: {0}", volume.Volume96)
        Console.WriteLine("Volume97: {0}", volume.Volume97)
        Console.WriteLine("Volume98: {0}", volume.Volume98)
        Console.WriteLine("Volume99: {0}", volume.Volume99)
        Console.WriteLine("Volume100: {0}", volume.Volume100)
        Console.WriteLine("RankID: {0}", volume.RankID)
        Console.WriteLine("PaidRankID: {0}", volume.PaidRankID)
        Console.WriteLine("Volume101: {0}", volume.Volume101)
        Console.WriteLine("Volume102: {0}", volume.Volume102)
        Console.WriteLine("Volume103: {0}", volume.Volume103)
        Console.WriteLine("Volume104: {0}", volume.Volume104)
        Console.WriteLine("Volume105: {0}", volume.Volume105)
        Console.WriteLine("Volume106: {0}", volume.Volume106)
        Console.WriteLine("Volume107: {0}", volume.Volume107)
        Console.WriteLine("Volume108: {0}", volume.Volume108)
        Console.WriteLine("Volume109: {0}", volume.Volume109)
        Console.WriteLine("Volume110: {0}", volume.Volume110)
        Console.WriteLine("Volume111: {0}", volume.Volume111)
        Console.WriteLine("Volume112: {0}", volume.Volume112)
        Console.WriteLine("Volume113: {0}", volume.Volume113)
        Console.WriteLine("Volume114: {0}", volume.Volume114)
        Console.WriteLine("Volume115: {0}", volume.Volume115)
        Console.WriteLine("Volume116: {0}", volume.Volume116)
        Console.WriteLine("Volume117: {0}", volume.Volume117)
        Console.WriteLine("Volume118: {0}", volume.Volume118)
        Console.WriteLine("Volume119: {0}", volume.Volume119)
        Console.WriteLine("Volume120: {0}", volume.Volume120)
        Console.WriteLine("Volume121: {0}", volume.Volume121)
        Console.WriteLine("Volume122: {0}", volume.Volume122)
        Console.WriteLine("Volume123: {0}", volume.Volume123)
        Console.WriteLine("Volume124: {0}", volume.Volume124)
        Console.WriteLine("Volume125: {0}", volume.Volume125)
        Console.WriteLine("Volume126: {0}", volume.Volume126)
        Console.WriteLine("Volume127: {0}", volume.Volume127)
        Console.WriteLine("Volume128: {0}", volume.Volume128)
        Console.WriteLine("Volume129: {0}", volume.Volume129)
        Console.WriteLine("Volume130: {0}", volume.Volume130)
        Console.WriteLine("Volume131: {0}", volume.Volume131)
        Console.WriteLine("Volume132: {0}", volume.Volume132)
        Console.WriteLine("Volume133: {0}", volume.Volume133)
        Console.WriteLine("Volume134: {0}", volume.Volume134)
        Console.WriteLine("Volume135: {0}", volume.Volume135)
        Console.WriteLine("Volume136: {0}", volume.Volume136)
        Console.WriteLine("Volume137: {0}", volume.Volume137)
        Console.WriteLine("Volume138: {0}", volume.Volume138)
        Console.WriteLine("Volume139: {0}", volume.Volume139)
        Console.WriteLine("Volume140: {0}", volume.Volume140)
        Console.WriteLine("Volume141: {0}", volume.Volume141)
        Console.WriteLine("Volume142: {0}", volume.Volume142)
        Console.WriteLine("Volume143: {0}", volume.Volume143)
        Console.WriteLine("Volume144: {0}", volume.Volume144)
        Console.WriteLine("Volume145: {0}", volume.Volume145)
        Console.WriteLine("Volume146: {0}", volume.Volume146)
        Console.WriteLine("Volume147: {0}", volume.Volume147)
        Console.WriteLine("Volume148: {0}", volume.Volume148)
        Console.WriteLine("Volume149: {0}", volume.Volume149)
        Console.WriteLine("Volume150: {0}", volume.Volume150)
        Console.WriteLine("Volume151: {0}", volume.Volume151)
        Console.WriteLine("Volume152: {0}", volume.Volume152)
        Console.WriteLine("Volume153: {0}", volume.Volume153)
        Console.WriteLine("Volume154: {0}", volume.Volume154)
        Console.WriteLine("Volume155: {0}", volume.Volume155)
        Console.WriteLine("Volume156: {0}", volume.Volume156)
        Console.WriteLine("Volume157: {0}", volume.Volume157)
        Console.WriteLine("Volume158: {0}", volume.Volume158)
        Console.WriteLine("Volume159: {0}", volume.Volume159)
        Console.WriteLine("Volume160: {0}", volume.Volume160)
        Console.WriteLine("Volume161: {0}", volume.Volume161)
        Console.WriteLine("Volume162: {0}", volume.Volume162)
        Console.WriteLine("Volume163: {0}", volume.Volume163)
        Console.WriteLine("Volume164: {0}", volume.Volume164)
        Console.WriteLine("Volume165: {0}", volume.Volume165)
        Console.WriteLine("Volume166: {0}", volume.Volume166)
        Console.WriteLine("Volume167: {0}", volume.Volume167)
        Console.WriteLine("Volume168: {0}", volume.Volume168)
        Console.WriteLine("Volume169: {0}", volume.Volume169)
        Console.WriteLine("Volume170: {0}", volume.Volume170)
        Console.WriteLine("Volume171: {0}", volume.Volume171)
        Console.WriteLine("Volume172: {0}", volume.Volume172)
        Console.WriteLine("Volume173: {0}", volume.Volume173)
        Console.WriteLine("Volume174: {0}", volume.Volume174)
        Console.WriteLine("Volume175: {0}", volume.Volume175)
        Console.WriteLine("Volume176: {0}", volume.Volume176)
        Console.WriteLine("Volume177: {0}", volume.Volume177)
        Console.WriteLine("Volume178: {0}", volume.Volume178)
        Console.WriteLine("Volume179: {0}", volume.Volume179)
        Console.WriteLine("Volume180: {0}", volume.Volume180)
        Console.WriteLine("Volume181: {0}", volume.Volume181)
        Console.WriteLine("Volume182: {0}", volume.Volume182)
        Console.WriteLine("Volume183: {0}", volume.Volume183)
        Console.WriteLine("Volume184: {0}", volume.Volume184)
        Console.WriteLine("Volume185: {0}", volume.Volume185)
        Console.WriteLine("Volume186: {0}", volume.Volume186)
        Console.WriteLine("Volume187: {0}", volume.Volume187)
        Console.WriteLine("Volume188: {0}", volume.Volume188)
        Console.WriteLine("Volume189: {0}", volume.Volume189)
        Console.WriteLine("Volume190: {0}", volume.Volume190)
        Console.WriteLine("Volume191: {0}", volume.Volume191)
        Console.WriteLine("Volume192: {0}", volume.Volume192)
        Console.WriteLine("Volume193: {0}", volume.Volume193)
        Console.WriteLine("Volume194: {0}", volume.Volume194)
        Console.WriteLine("Volume195: {0}", volume.Volume195)
        Console.WriteLine("Volume196: {0}", volume.Volume196)
        Console.WriteLine("Volume197: {0}", volume.Volume197)
        Console.WriteLine("Volume198: {0}", volume.Volume198)
        Console.WriteLine("Volume199: {0}", volume.Volume199)
        Console.WriteLine("Volume200: {0}", volume.Volume200)
        Console.WriteLine("CustomerKey: {0}", volume.CustomerKey)
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

    $req->PeriodType = 1;
    $req->PeriodID = 1;
    $req->CustomerID = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.GetVolumes($req);

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
    GetVolumesRequest req = new GetVolumesRequest();

    req.setPeriodType(1);
    req.setPeriodID(1);
    req.setCustomerID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    GetVolumesResponse res = api.getExigoApiSoap().getVolumes(req, auth);

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
https://api.exigo.com/3.0/csv/?method=GetVolumes
&ApiLoginName=String
&ApiPassword=String
&ApiCompany=String
&PeriodType=Int32
&PeriodID=Nullable`1
&CustomerID=Nullable`1
&CustomerKey=String
Response FieldsCustomerID,PeriodType,PeriodID,PeriodDescription,Volume1,Volume2,Volume3,Volume4,Volume5,Volume6,Volume7,Volume8,Volume9,Volume10,Volume11,Volume12,Volume13,Volume14,Volume15,Volume16,Volume17,Volume18,Volume19,Volume20,Volume21,Volume22,Volume23,Volume24,Volume25,Volume26,Volume27,Volume28,Volume29,Volume30,Volume31,Volume32,Volume33,Volume34,Volume35,Volume36,Volume37,Volume38,Volume39,Volume40,Volume41,Volume42,Volume43,Volume44,Volume45,Volume46,Volume47,Volume48,Volume49,Volume50,Volume51,Volume52,Volume53,Volume54,Volume55,Volume56,Volume57,Volume58,Volume59,Volume60,Volume61,Volume62,Volume63,Volume64,Volume65,Volume66,Volume67,Volume68,Volume69,Volume70,Volume71,Volume72,Volume73,Volume74,Volume75,Volume76,Volume77,Volume78,Volume79,Volume80,Volume81,Volume82,Volume83,Volume84,Volume85,Volume86,Volume87,Volume88,Volume89,Volume90,Volume91,Volume92,Volume93,Volume94,Volume95,Volume96,Volume97,Volume98,Volume99,Volume100,RankID,PaidRankID,Volume101,Volume102,Volume103,Volume104,Volume105,Volume106,Volume107,Volume108,Volume109,Volume110,Volume111,Volume112,Volume113,Volume114,Volume115,Volume116,Volume117,Volume118,Volume119,Volume120,Volume121,Volume122,Volume123,Volume124,Volume125,Volume126,Volume127,Volume128,Volume129,Volume130,Volume131,Volume132,Volume133,Volume134,Volume135,Volume136,Volume137,Volume138,Volume139,Volume140,Volume141,Volume142,Volume143,Volume144,Volume145,Volume146,Volume147,Volume148,Volume149,Volume150,Volume151,Volume152,Volume153,Volume154,Volume155,Volume156,Volume157,Volume158,Volume159,Volume160,Volume161,Volume162,Volume163,Volume164,Volume165,Volume166,Volume167,Volume168,Volume169,Volume170,Volume171,Volume172,Volume173,Volume174,Volume175,Volume176,Volume177,Volume178,Volume179,Volume180,Volume181,Volume182,Volume183,Volume184,Volume185,Volume186,Volume187,Volume188,Volume189,Volume190,Volume191,Volume192,Volume193,Volume194,Volume195,Volume196,Volume197,Volume198,Volume199,Volume200,CustomerKey
Int32,Int32,Int32,String,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Int32,Int32,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,Decimal,String

                    © 2026 Exigo.
```

</details>

---

### GetRealTimeCommissions

> Returns realtime commissions available for open periods.

| | |
|---|---|
| Category | Reporting |
| REST | `GET /3.0/commissions/realtime?customerID=1` |
| SOAP action | `https://api.exigo.com/GetRealTimeCommissions` |
| WSDL elements | `GetRealTimeCommissionsRequest` → `GetRealTimeCommissionsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetRealTimeCommissions |

#### Input

**`GetRealTimeCommissionsRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`GetRealTimeCommissionsResponse`**

| Property | Type | Notes |
|---|---|---|
| `Commissions` | `CommissionResponse[]` |  |

**`CommissionResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `CustomerID` | `Int32` | Unique numeric identifier for a customer record. |
| &nbsp;&nbsp;↳ `PeriodType` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `PeriodID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `PeriodDescription` | `String` |  |
| &nbsp;&nbsp;↳ `CurrencyCode` | `String` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `CommissionTotal` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Bonuses` | `CommissionBonusResponse[]` |  |
| &nbsp;&nbsp;↳ `CustomerKey` | `String` | Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

**`CommissionBonusResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Description` | `String` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `Amount` | `Decimal` |  |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ `BonusID` | `Int32` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/commissions/realtime?customerID=1
  &customerKey=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "commissions": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetRealTimeCommissions"

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
    <GetRealTimeCommissionsRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
    </GetRealTimeCommissionsRequest>
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
    <GetRealTimeCommissionsResult xmlns="http://api.exigo.com/">
      <Commissions>
        <CommissionResponse>
          <CustomerID>int</CustomerID>
          <PeriodType>int</PeriodType>
          <PeriodID>int</PeriodID>
          <PeriodDescription>string</PeriodDescription>
          <CurrencyCode>string</CurrencyCode>
          <CommissionTotal>decimal</CommissionTotal>
          <Bonuses>
            <CommissionBonusResponse>
              <Description>string</Description>
              <Amount>decimal</Amount>
              <BonusID>int</BonusID>
            </CommissionBonusResponse>
          </Bonuses>
          <CustomerKey>string</CustomerKey>
        </CommissionResponse>
      </Commissions>
    </GetRealTimeCommissionsResult>
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
    var req = new GetRealTimeCommissionsRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.GetRealTimeCommissionsAsync(req);

    //Now examine the results:

    foreach (var commission  in res.Commissions)
    {
        Console.WriteLine("CustomerID: {0}", commission.CustomerID);
        Console.WriteLine("PeriodType: {0}", commission.PeriodType);
        Console.WriteLine("PeriodID: {0}", commission.PeriodID);
        Console.WriteLine("PeriodDescription: {0}", commission.PeriodDescription);
        Console.WriteLine("CurrencyCode: {0}", commission.CurrencyCode);
        Console.WriteLine("CommissionTotal: {0}", commission.CommissionTotal);

        foreach (var commissionBonus  in commission.Bonuses)
        {
            Console.WriteLine("Description: {0}", commissionBonus.Description);
            Console.WriteLine("Amount: {0}", commissionBonus.Amount);
            Console.WriteLine("BonusID: {0}", commissionBonus.BonusID);
        }
        Console.WriteLine("CustomerKey: {0}", commission.CustomerKey);
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
    GetRealTimeCommissionsRequest req = new GetRealTimeCommissionsRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    GetRealTimeCommissionsResponse res = api.GetRealTimeCommissions(req);

    //Now examine the results:

    foreach (CommissionResponse commission  in res.Commissions)
    {
        Console.WriteLine("CustomerID: {0}", commission.CustomerID);
        Console.WriteLine("PeriodType: {0}", commission.PeriodType);
        Console.WriteLine("PeriodID: {0}", commission.PeriodID);
        Console.WriteLine("PeriodDescription: {0}", commission.PeriodDescription);
        Console.WriteLine("CurrencyCode: {0}", commission.CurrencyCode);
        Console.WriteLine("CommissionTotal: {0}", commission.CommissionTotal);

        foreach (CommissionBonusResponse commissionBonus  in commission.Bonuses)
        {
            Console.WriteLine("Description: {0}", commissionBonus.Description);
            Console.WriteLine("Amount: {0}", commissionBonus.Amount);
            Console.WriteLine("BonusID: {0}", commissionBonus.BonusID);
        }
        Console.WriteLine("CustomerKey: {0}", commission.CustomerKey);
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
    Dim req as new GetRealTimeCommissionsRequest()

    req.CustomerID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As GetRealTimeCommissionsResponse = api.GetRealTimeCommissions(req)

    'Now examine the results:

    For Each commission As CommissionResponse In res.Commissions
        Console.WriteLine("CustomerID: {0}", commission.CustomerID)
        Console.WriteLine("PeriodType: {0}", commission.PeriodType)
        Console.WriteLine("PeriodID: {0}", commission.PeriodID)
        Console.WriteLine("PeriodDescription: {0}", commission.PeriodDescription)
        Console.WriteLine("CurrencyCode: {0}", commission.CurrencyCode)
        Console.WriteLine("CommissionTotal: {0}", commission.CommissionTotal)

        For Each commissionBonus As CommissionBonusResponse In commission.Bonuses
            Console.WriteLine("Description: {0}", commissionBonus.Description)
            Console.WriteLine("Amount: {0}", commissionBonus.Amount)
            Console.WriteLine("BonusID: {0}", commissionBonus.BonusID)
        Next
        Console.WriteLine("CustomerKey: {0}", commission.CustomerKey)
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
    $res = $api.GetRealTimeCommissions($req);

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
    GetRealTimeCommissionsRequest req = new GetRealTimeCommissionsRequest();

    req.setCustomerID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    GetRealTimeCommissionsResponse res = api.getExigoApiSoap().getRealTimeCommissions(req, auth);

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

### GetRealTimeCommissionDetail

> Returns realtime commission detail for a customer/bonus.

| | |
|---|---|
| Category | Reporting |
| REST | `GET /3.0/commissions/realtime/detail?customerID=1` |
| SOAP action | `https://api.exigo.com/GetRealTimeCommissionDetail` |
| WSDL elements | `GetRealTimeCommissionDetailRequest` → `GetRealTimeCommissionDetailResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetRealTimeCommissionDetail |

#### Input

**`GetRealTimeCommissionDetailRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `PeriodType` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| `PeriodID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| `BonusID` | `Int32` |  |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`GetRealTimeCommissionDetailResponse`**

| Property | Type | Notes |
|---|---|---|
| `CommissionDetails` | `CommissionDetailResponse[]` |  |

**`CommissionDetailResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `FromCustomerID` | `Int32` | Unique numeric identifier for order from customer record. |
| &nbsp;&nbsp;↳ `FromCustomerName` | `String` |  |
| &nbsp;&nbsp;↳ `OrderID` | `Int32` | Unique numeric identifier for order record. |
| &nbsp;&nbsp;↳ `Level` | `Int32` |  |
| &nbsp;&nbsp;↳ `PaidLevel` | `Int32` |  |
| &nbsp;&nbsp;↳ `SourceAmount` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Percentage` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CommissionAmount` | `Decimal` |  |
| &nbsp;&nbsp;↳ `FromCustomerKey` | `String` | Unique alpha numeric identifier for order from customer record. |
| &nbsp;&nbsp;↳ `OrderKey` | `String` | Unique alpha numeric identifier for order record. |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/commissions/realtime/detail?customerID=1
  &periodType=1
  &periodID=1
  &bonusID=1
  &customerKey=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "commissionDetails": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetRealTimeCommissionDetail"

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
    <GetRealTimeCommissionDetailRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <PeriodType>int</PeriodType>
      <PeriodID>int</PeriodID>
      <BonusID>int</BonusID>
      <CustomerKey>string</CustomerKey>
    </GetRealTimeCommissionDetailRequest>
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
    <GetRealTimeCommissionDetailResult xmlns="http://api.exigo.com/">
      <CommissionDetails>
        <CommissionDetailResponse>
          <FromCustomerID>int</FromCustomerID>
          <FromCustomerName>string</FromCustomerName>
          <OrderID>int</OrderID>
          <Level>int</Level>
          <PaidLevel>int</PaidLevel>
          <SourceAmount>decimal</SourceAmount>
          <Percentage>decimal</Percentage>
          <CommissionAmount>decimal</CommissionAmount>
          <FromCustomerKey>string</FromCustomerKey>
          <OrderKey>string</OrderKey>
        </CommissionDetailResponse>
      </CommissionDetails>
    </GetRealTimeCommissionDetailResult>
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
    var req = new GetRealTimeCommissionDetailRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.PeriodType = 1;
    req.PeriodID = 1;
    req.BonusID = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.GetRealTimeCommissionDetailAsync(req);

    //Now examine the results:

    foreach (var commissionDetail  in res.CommissionDetails)
    {
        Console.WriteLine("FromCustomerID: {0}", commissionDetail.FromCustomerID);
        Console.WriteLine("FromCustomerName: {0}", commissionDetail.FromCustomerName);
        Console.WriteLine("OrderID: {0}", commissionDetail.OrderID);
        Console.WriteLine("Level: {0}", commissionDetail.Level);
        Console.WriteLine("PaidLevel: {0}", commissionDetail.PaidLevel);
        Console.WriteLine("SourceAmount: {0}", commissionDetail.SourceAmount);
        Console.WriteLine("Percentage: {0}", commissionDetail.Percentage);
        Console.WriteLine("CommissionAmount: {0}", commissionDetail.CommissionAmount);
        Console.WriteLine("FromCustomerKey: {0}", commissionDetail.FromCustomerKey);
        Console.WriteLine("OrderKey: {0}", commissionDetail.OrderKey);
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
    GetRealTimeCommissionDetailRequest req = new GetRealTimeCommissionDetailRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.PeriodType = 1;
    req.PeriodID = 1;
    req.BonusID = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    GetRealTimeCommissionDetailResponse res = api.GetRealTimeCommissionDetail(req);

    //Now examine the results:

    foreach (CommissionDetailResponse commissionDetail  in res.CommissionDetails)
    {
        Console.WriteLine("FromCustomerID: {0}", commissionDetail.FromCustomerID);
        Console.WriteLine("FromCustomerName: {0}", commissionDetail.FromCustomerName);
        Console.WriteLine("OrderID: {0}", commissionDetail.OrderID);
        Console.WriteLine("Level: {0}", commissionDetail.Level);
        Console.WriteLine("PaidLevel: {0}", commissionDetail.PaidLevel);
        Console.WriteLine("SourceAmount: {0}", commissionDetail.SourceAmount);
        Console.WriteLine("Percentage: {0}", commissionDetail.Percentage);
        Console.WriteLine("CommissionAmount: {0}", commissionDetail.CommissionAmount);
        Console.WriteLine("FromCustomerKey: {0}", commissionDetail.FromCustomerKey);
        Console.WriteLine("OrderKey: {0}", commissionDetail.OrderKey);
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
    Dim req as new GetRealTimeCommissionDetailRequest()

    req.CustomerID = 1
    req.PeriodType = 1
    req.PeriodID = 1
    req.BonusID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As GetRealTimeCommissionDetailResponse = api.GetRealTimeCommissionDetail(req)

    'Now examine the results:

    For Each commissionDetail As CommissionDetailResponse In res.CommissionDetails
        Console.WriteLine("FromCustomerID: {0}", commissionDetail.FromCustomerID)
        Console.WriteLine("FromCustomerName: {0}", commissionDetail.FromCustomerName)
        Console.WriteLine("OrderID: {0}", commissionDetail.OrderID)
        Console.WriteLine("Level: {0}", commissionDetail.Level)
        Console.WriteLine("PaidLevel: {0}", commissionDetail.PaidLevel)
        Console.WriteLine("SourceAmount: {0}", commissionDetail.SourceAmount)
        Console.WriteLine("Percentage: {0}", commissionDetail.Percentage)
        Console.WriteLine("CommissionAmount: {0}", commissionDetail.CommissionAmount)
        Console.WriteLine("FromCustomerKey: {0}", commissionDetail.FromCustomerKey)
        Console.WriteLine("OrderKey: {0}", commissionDetail.OrderKey)
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
    $req->PeriodType = 1;
    $req->PeriodID = 1;
    $req->BonusID = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.GetRealTimeCommissionDetail($req);

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
    GetRealTimeCommissionDetailRequest req = new GetRealTimeCommissionDetailRequest();

    req.setCustomerID(1);
    req.setPeriodType(1);
    req.setPeriodID(1);
    req.setBonusID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    GetRealTimeCommissionDetailResponse res = api.getExigoApiSoap().getRealTimeCommissionDetail(req, auth);

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

### GetRankQualifications

> Returns rank qualification report card.

| | |
|---|---|
| Category | Reporting |
| REST | `GET /3.0/qualification?customerID=1` |
| SOAP action | `https://api.exigo.com/GetRankQualifications` |
| WSDL elements | `GetRankQualificationsRequest` → `GetRankQualificationsResult` |
| CSV output | Yes — `GET https://api.exigo.com/3.0/csv/?method=GetRankQualifications&ApiLoginName=…&ApiPassword=…&ApiCompany=…` |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetRankQualifications |

#### Input

**`GetRankQualificationsRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `RankID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| `PeriodType` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| `PeriodID` | `Int32` | Optional. Will default to current period. |
| `CultureCode` | `String` | Optional. Return qualifications in a different language. |
| `RankGroupID` | `Int32` | Optional. Will default to primary rank group. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`GetRankQualificationsResponse`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customerd record. |
| `RankID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| `RankDescription` | `String` |  |
| `Qualifies` | `Boolean` |  |
| `QualifiesOverride` | `Boolean` |  |
| `PayeeQualificationLegs` | `QualificationResponse[][]` |  |
| `BackRankID` | `Int32` |  |
| `BackRankDescription` | `String` |  |
| `NextRankID` | `Int32` |  |
| `NextRankDescription` | `String` |  |
| `Score` | `Decimal` |  |
| `CustomerKey` | `String` | Unique alpha numeric identifier for customer record. |

**`QualificationResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `QualificationDescription` | `String` |  |
| &nbsp;&nbsp;↳ `Required` | `String` |  |
| &nbsp;&nbsp;↳ `Actual` | `String` |  |
| &nbsp;&nbsp;↳ `Qualifies` | `Boolean` |  |
| &nbsp;&nbsp;↳ `QualifiesOverride` | `Boolean` |  |
| &nbsp;&nbsp;↳ `SupportingTable` | `DataTable` |  |
| &nbsp;&nbsp;↳ `Completed` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Weight` | `Decimal` |  |
| &nbsp;&nbsp;↳ `Score` | `Decimal` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/qualification?customerID=1
  &rankID=1
  &periodType=1
  &periodID=1
  &cultureCode=1
  &rankGroupID=1
  &customerKey=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "customerID": 1,
  "rankID": 1,
  "rankDescription": "",
  "qualifies": true,
  "qualifiesOverride": true,
  "payeeQualificationLegs": null,
  "backRankID": 1,
  "backRankDescription": "",
  "nextRankID": 1,
  "nextRankDescription": "",
  "score": null,
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
SOAPAction: "https://api.exigo.com/GetRankQualifications"

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
    <GetRankQualificationsRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <RankID>int</RankID>
      <PeriodType>int</PeriodType>
      <PeriodID>int</PeriodID>
      <CultureCode>string</CultureCode>
      <RankGroupID>int</RankGroupID>
      <CustomerKey>string</CustomerKey>
    </GetRankQualificationsRequest>
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
    <GetRankQualificationsResult xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <RankID>int</RankID>
      <RankDescription>string</RankDescription>
      <Qualifies>boolean</Qualifies>
      <QualifiesOverride>boolean</QualifiesOverride>
      <PayeeQualificationLegs>
        <ArrayOfQualificationResponse>
          <QualificationResponse>
            <QualificationDescription>string</QualificationDescription>
            <Required>string</Required>
            <Actual>string</Actual>
            <Qualifies>boolean</Qualifies>
            <QualifiesOverride>boolean</QualifiesOverride>
            <SupportingTable>xmlxml</SupportingTable>
            <Completed>decimal</Completed>
            <Weight>decimal</Weight>
            <Score>decimal</Score>
          </QualificationResponse>
        </ArrayOfQualificationResponse>
      </PayeeQualificationLegs>
      <BackRankID>int</BackRankID>
      <BackRankDescription>string</BackRankDescription>
      <NextRankID>int</NextRankID>
      <NextRankDescription>string</NextRankDescription>
      <Score>decimal</Score>
      <CustomerKey>string</CustomerKey>
    </GetRankQualificationsResult>
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
    var req = new GetRankQualificationsRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.RankID = 1;
    req.PeriodType = 1;
    req.PeriodID = 1;               //Will default to current period.
    req.CultureCode = "1";          //Return qualifications in a different language.
    req.RankGroupID = 1;            //Will default to primary rank group.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.GetRankQualificationsAsync(req);

    //Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID);
    Console.WriteLine("RankID: {0}", res.RankID);
    Console.WriteLine("RankDescription: {0}", res.RankDescription);
    Console.WriteLine("Qualifies: {0}", res.Qualifies);
    Console.WriteLine("QualifiesOverride: {0}", res.QualifiesOverride);

    foreach (var qualification[]  in res.PayeeQualificationLegs)
    {
        Console.WriteLine("Length: {0}", qualification[].Length);
        Console.WriteLine("LongLength: {0}", qualification[].LongLength);
        Console.WriteLine("Rank: {0}", qualification[].Rank);
        Console.WriteLine("SyncRoot: {0}", qualification[].SyncRoot);
        Console.WriteLine("IsReadOnly: {0}", qualification[].IsReadOnly);
        Console.WriteLine("IsFixedSize: {0}", qualification[].IsFixedSize);
        Console.WriteLine("IsSynchronized: {0}", qualification[].IsSynchronized);
    }
    Console.WriteLine("BackRankID: {0}", res.BackRankID);
    Console.WriteLine("BackRankDescription: {0}", res.BackRankDescription);
    Console.WriteLine("NextRankID: {0}", res.NextRankID);
    Console.WriteLine("NextRankDescription: {0}", res.NextRankDescription);
    Console.WriteLine("Score: {0}", res.Score);
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
    GetRankQualificationsRequest req = new GetRankQualificationsRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.RankID = 1;
    req.PeriodType = 1;
    req.PeriodID = 1;               //Will default to current period.
    req.CultureCode = "1";          //Return qualifications in a different language.
    req.RankGroupID = 1;            //Will default to primary rank group.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    GetRankQualificationsResponse res = api.GetRankQualifications(req);

    //Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID);
    Console.WriteLine("RankID: {0}", res.RankID);
    Console.WriteLine("RankDescription: {0}", res.RankDescription);
    Console.WriteLine("Qualifies: {0}", res.Qualifies);
    Console.WriteLine("QualifiesOverride: {0}", res.QualifiesOverride);

    foreach (QualificationResponse[] qualification[]  in res.PayeeQualificationLegs)
    {
        Console.WriteLine("Length: {0}", qualification[].Length);
        Console.WriteLine("LongLength: {0}", qualification[].LongLength);
        Console.WriteLine("Rank: {0}", qualification[].Rank);
        Console.WriteLine("SyncRoot: {0}", qualification[].SyncRoot);
        Console.WriteLine("IsReadOnly: {0}", qualification[].IsReadOnly);
        Console.WriteLine("IsFixedSize: {0}", qualification[].IsFixedSize);
        Console.WriteLine("IsSynchronized: {0}", qualification[].IsSynchronized);
    }
    Console.WriteLine("BackRankID: {0}", res.BackRankID);
    Console.WriteLine("BackRankDescription: {0}", res.BackRankDescription);
    Console.WriteLine("NextRankID: {0}", res.NextRankID);
    Console.WriteLine("NextRankDescription: {0}", res.NextRankDescription);
    Console.WriteLine("Score: {0}", res.Score);
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
    Dim req as new GetRankQualificationsRequest()

    req.CustomerID = 1
    req.RankID = 1
    req.PeriodType = 1
    req.PeriodID = 1
    req.CultureCode = "1"
    req.RankGroupID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As GetRankQualificationsResponse = api.GetRankQualifications(req)

    'Now examine the results:
    Console.WriteLine("CustomerID: {0}", res.CustomerID)
    Console.WriteLine("RankID: {0}", res.RankID)
    Console.WriteLine("RankDescription: {0}", res.RankDescription)
    Console.WriteLine("Qualifies: {0}", res.Qualifies)
    Console.WriteLine("QualifiesOverride: {0}", res.QualifiesOverride)

    For Each qualification[] As QualificationResponse[] In res.PayeeQualificationLegs
        Console.WriteLine("Length: {0}", qualification[].Length)
        Console.WriteLine("LongLength: {0}", qualification[].LongLength)
        Console.WriteLine("Rank: {0}", qualification[].Rank)
        Console.WriteLine("SyncRoot: {0}", qualification[].SyncRoot)
        Console.WriteLine("IsReadOnly: {0}", qualification[].IsReadOnly)
        Console.WriteLine("IsFixedSize: {0}", qualification[].IsFixedSize)
        Console.WriteLine("IsSynchronized: {0}", qualification[].IsSynchronized)
    Next
    Console.WriteLine("BackRankID: {0}", res.BackRankID)
    Console.WriteLine("BackRankDescription: {0}", res.BackRankDescription)
    Console.WriteLine("NextRankID: {0}", res.NextRankID)
    Console.WriteLine("NextRankDescription: {0}", res.NextRankDescription)
    Console.WriteLine("Score: {0}", res.Score)
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
    $req->RankID = 1;
    $req->PeriodType = 1;
    $req->PeriodID = 1;
    $req->CultureCode = "1";
    $req->RankGroupID = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.GetRankQualifications($req);

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
    GetRankQualificationsRequest req = new GetRankQualificationsRequest();

    req.setCustomerID(1);
    req.setRankID(1);
    req.setPeriodType(1);
    req.setPeriodID(1);
    req.setCultureCode("1");
    req.setRankGroupID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    GetRankQualificationsResponse res = api.getExigoApiSoap().getRankQualifications(req, auth);

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
https://api.exigo.com/3.0/csv/?method=GetRankQualifications
&ApiLoginName=String
&ApiPassword=String
&ApiCompany=String
&CustomerID=Int32
&RankID=Int32
&PeriodType=Int32
&PeriodID=Nullable`1
&CultureCode=String
&RankGroupID=Nullable`1
&CustomerKey=String
Response FieldsCustomerID,RankID,RankDescription,Qualifies,QualifiesOverride,Length,LongLength,Rank,SyncRoot,IsReadOnly,IsFixedSize,IsSynchronized,BackRankID,BackRankDescription,NextRankID,NextRankDescription,Score,CustomerKey
Int32,Int32,String,Boolean,Nullable`1,Int32,Int64,Int32,Object,Boolean,Boolean,Boolean,Nullable`1,String,Nullable`1,String,Decimal,String

                    © 2026 Exigo.
```

</details>

---

### GetQualificationOverrides

> Returns Customer Overrides

| | |
|---|---|
| Category | Reporting |
| REST | `GET /3.0/qualification/override?customerID=1` |
| SOAP action | `https://api.exigo.com/GetQualificationOverrides` |
| WSDL elements | `GetQualificationOverridesRequest` → `GetQualificationOverridesResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetQualificationOverrides |

#### Input

**`GetQualificationOverridesRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Optional. Numeric identifier for customer record. |
| `OverrideID` | `Int32` | Optional. Numeric identifier for override. |
| `BatchSize` | `Int32` | Optional. Defaults to 1000 at a time. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`GetQualitificationOverridesResponse`**

| Property | Type | Notes |
|---|---|---|
| `QualificationOverrides` | `GetQualificationOverrideResponse[]` |  |

**`GetQualificationOverrideResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| &nbsp;&nbsp;↳ `OverrideID` | `Int32` |  |
| &nbsp;&nbsp;↳ `Qualifies` | `Boolean` |  |
| &nbsp;&nbsp;↳ `PeriodType` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| &nbsp;&nbsp;↳ `StartPeriodID` | `Int32` |  |
| &nbsp;&nbsp;↳ `EndPeriodID` | `Int32` |  |
| &nbsp;&nbsp;↳ `ModifiedDate` | `DateTime` |  |
| &nbsp;&nbsp;↳ `ModifiedBy` | `String` |  |
| &nbsp;&nbsp;↳ `Amount` | `Decimal` |  |
| &nbsp;&nbsp;↳ `CustomerKey` | `String` | Unique alpha numeric identifier for customer record . |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/qualification/override?customerID=1
  &overrideID=1
  &batchSize=1
  &customerKey=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "qualificationOverrides": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetQualificationOverrides"

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
    <GetQualificationOverridesRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <OverrideID>int</OverrideID>
      <BatchSize>int</BatchSize>
      <CustomerKey>string</CustomerKey>
    </GetQualificationOverridesRequest>
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
    <GetQualificationOverridesResult xmlns="http://api.exigo.com/">
      <QualificationOverrides>
        <GetQualificationOverrideResponse>
          <CustomerID>int</CustomerID>
          <OverrideID>int</OverrideID>
          <Qualifies>boolean</Qualifies>
          <PeriodType>int</PeriodType>
          <StartPeriodID>int</StartPeriodID>
          <EndPeriodID>int</EndPeriodID>
          <ModifiedDate>dateTime</ModifiedDate>
          <ModifiedBy>string</ModifiedBy>
          <Amount>decimal</Amount>
          <CustomerKey>string</CustomerKey>
        </GetQualificationOverrideResponse>
      </QualificationOverrides>
    </GetQualificationOverridesResult>
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
    var req = new GetQualificationOverridesRequest();

    req.CustomerID = 1;             //Numeric identifier for customer record.
    req.OverrideID = 1;             //Numeric identifier for override
    req.BatchSize = 1;              //Defaults to 1000 at a time
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.GetQualificationOverridesAsync(req);

    //Now examine the results:

    foreach (var getQualificationOverride  in res.QualificationOverrides)
    {
        Console.WriteLine("CustomerID: {0}", getQualificationOverride.CustomerID);
        Console.WriteLine("OverrideID: {0}", getQualificationOverride.OverrideID);
        Console.WriteLine("Qualifies: {0}", getQualificationOverride.Qualifies);
        Console.WriteLine("PeriodType: {0}", getQualificationOverride.PeriodType);
        Console.WriteLine("StartPeriodID: {0}", getQualificationOverride.StartPeriodID);
        Console.WriteLine("EndPeriodID: {0}", getQualificationOverride.EndPeriodID);
        Console.WriteLine("ModifiedDate: {0}", getQualificationOverride.ModifiedDate);
        Console.WriteLine("ModifiedBy: {0}", getQualificationOverride.ModifiedBy);
        Console.WriteLine("Amount: {0}", getQualificationOverride.Amount);
        Console.WriteLine("CustomerKey: {0}", getQualificationOverride.CustomerKey);
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
    GetQualificationOverridesRequest req = new GetQualificationOverridesRequest();

    req.CustomerID = 1;             //Numeric identifier for customer record.
    req.OverrideID = 1;             //Numeric identifier for override
    req.BatchSize = 1;              //Defaults to 1000 at a time
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    GetQualitificationOverridesResponse res = api.GetQualificationOverrides(req);

    //Now examine the results:

    foreach (GetQualificationOverrideResponse getQualificationOverride  in res.QualificationOverrides)
    {
        Console.WriteLine("CustomerID: {0}", getQualificationOverride.CustomerID);
        Console.WriteLine("OverrideID: {0}", getQualificationOverride.OverrideID);
        Console.WriteLine("Qualifies: {0}", getQualificationOverride.Qualifies);
        Console.WriteLine("PeriodType: {0}", getQualificationOverride.PeriodType);
        Console.WriteLine("StartPeriodID: {0}", getQualificationOverride.StartPeriodID);
        Console.WriteLine("EndPeriodID: {0}", getQualificationOverride.EndPeriodID);
        Console.WriteLine("ModifiedDate: {0}", getQualificationOverride.ModifiedDate);
        Console.WriteLine("ModifiedBy: {0}", getQualificationOverride.ModifiedBy);
        Console.WriteLine("Amount: {0}", getQualificationOverride.Amount);
        Console.WriteLine("CustomerKey: {0}", getQualificationOverride.CustomerKey);
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
    Dim req as new GetQualificationOverridesRequest()

    req.CustomerID = 1
    req.OverrideID = 1
    req.BatchSize = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As GetQualitificationOverridesResponse = api.GetQualificationOverrides(req)

    'Now examine the results:

    For Each getQualificationOverride As GetQualificationOverrideResponse In res.QualificationOverrides
        Console.WriteLine("CustomerID: {0}", getQualificationOverride.CustomerID)
        Console.WriteLine("OverrideID: {0}", getQualificationOverride.OverrideID)
        Console.WriteLine("Qualifies: {0}", getQualificationOverride.Qualifies)
        Console.WriteLine("PeriodType: {0}", getQualificationOverride.PeriodType)
        Console.WriteLine("StartPeriodID: {0}", getQualificationOverride.StartPeriodID)
        Console.WriteLine("EndPeriodID: {0}", getQualificationOverride.EndPeriodID)
        Console.WriteLine("ModifiedDate: {0}", getQualificationOverride.ModifiedDate)
        Console.WriteLine("ModifiedBy: {0}", getQualificationOverride.ModifiedBy)
        Console.WriteLine("Amount: {0}", getQualificationOverride.Amount)
        Console.WriteLine("CustomerKey: {0}", getQualificationOverride.CustomerKey)
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
    $req->OverrideID = 1;
    $req->BatchSize = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.GetQualificationOverrides($req);

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
    GetQualificationOverridesRequest req = new GetQualificationOverridesRequest();

    req.setCustomerID(1);
    req.setOverrideID(1);
    req.setBatchSize(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    GetQualitificationOverridesResponse res = api.getExigoApiSoap().getQualificationOverrides(req, auth);

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

### SetQualificationOverride

> Create or Edit a Customer Override

| | |
|---|---|
| Category | Reporting |
| REST | `PUT /3.0/qualification/override` |
| SOAP action | `https://api.exigo.com/SetQualificationOverride` |
| WSDL elements | `SetQualificationOverrideRequest` → `SetQualificationOverrideResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=SetQualificationOverride |

#### Input

**`SetQualificationOverrideRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `OverrideID` | `Int32` | **Lookup:** company-specific list (see company-lists.md) |
| `Qualifies` | `Boolean` |  |
| `PeriodType` | `Int32` | Optional.<br>**Lookup:** company-specific list (see company-lists.md) |
| `StartPeriodID` | `Int32` | Optional. |
| `EndPeriodID` | `Int32` | Optional. |
| `Amount` | `Decimal` | Optional. Defaults to 0.00. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`SetQualificationOverrideResponse`**

_No properties._

#### REST example

```http
PUT https://yourcompany-api.exigo.com/3.0/qualification/override HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "overrideID": 1,
  "qualifies": true,
  "periodType": 1,
  "startPeriodID": 1,
  "endPeriodID": 1,
  "amount": null,
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
SOAPAction: "https://api.exigo.com/SetQualificationOverride"

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
    <SetQualificationOverrideRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <OverrideID>int</OverrideID>
      <Qualifies>boolean</Qualifies>
      <PeriodType>int</PeriodType>
      <StartPeriodID>int</StartPeriodID>
      <EndPeriodID>int</EndPeriodID>
      <Amount>decimal</Amount>
      <CustomerKey>string</CustomerKey>
    </SetQualificationOverrideRequest>
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
    <SetQualificationOverrideResult xmlns="http://api.exigo.com/" />
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
    var req = new SetQualificationOverrideRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.OverrideID = 1;
    req.Qualifies = true;
    req.PeriodType = 1;
    req.StartPeriodID = 1;
    req.EndPeriodID = 1;
    req.Amount = 1;                 //Defaults to 0.00
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.SetQualificationOverrideAsync(req);

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
    SetQualificationOverrideRequest req = new SetQualificationOverrideRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.OverrideID = 1;
    req.Qualifies = true;
    req.PeriodType = 1;
    req.StartPeriodID = 1;
    req.EndPeriodID = 1;
    req.Amount = 1;                 //Defaults to 0.00
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    SetQualificationOverrideResponse res = api.SetQualificationOverride(req);

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
    Dim req as new SetQualificationOverrideRequest()

    req.CustomerID = 1
    req.OverrideID = 1
    req.Qualifies = true
    req.PeriodType = 1
    req.StartPeriodID = 1
    req.EndPeriodID = 1
    req.Amount = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As SetQualificationOverrideResponse = api.SetQualificationOverride(req)

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
    $req->OverrideID = 1;
    $req->Qualifies = 1;
    $req->PeriodType = 1;
    $req->StartPeriodID = 1;
    $req->EndPeriodID = 1;
    $req->Amount = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.SetQualificationOverride($req);

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
    SetQualificationOverrideRequest req = new SetQualificationOverrideRequest();

    req.setCustomerID(1);
    req.setOverrideID(1);
    req.setQualifies(1);
    req.setPeriodType(1);
    req.setStartPeriodID(1);
    req.setEndPeriodID(1);
    req.setAmount(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    SetQualificationOverrideResponse res = api.getExigoApiSoap().setQualificationOverride(req, auth);

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

### DeleteQualificationOverride

> Delete a Customer Override

| | |
|---|---|
| Category | Reporting |
| REST | `DELETE /3.0/qualification/override` |
| SOAP action | `https://api.exigo.com/DeleteQualificationOverride` |
| WSDL elements | `DeleteQualificationOverrideRequest` → `DeleteQualificationOverrideResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DeleteQualificationOverride |

#### Input

**`DeleteQualificationOverrideRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `OverrideID` | `Int32` |  |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided. |

#### Output

**`DeleteQualificationOverrideResponse`**

_No properties._

#### REST example

```http
DELETE https://yourcompany-api.exigo.com/3.0/qualification/override HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "overrideID": 1,
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
SOAPAction: "https://api.exigo.com/DeleteQualificationOverride"

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
    <DeleteQualificationOverrideRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <OverrideID>int</OverrideID>
      <CustomerKey>string</CustomerKey>
    </DeleteQualificationOverrideRequest>
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
    <DeleteQualificationOverrideResult xmlns="http://api.exigo.com/" />
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
    var req = new DeleteQualificationOverrideRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.OverrideID = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.DeleteQualificationOverrideAsync(req);

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
    DeleteQualificationOverrideRequest req = new DeleteQualificationOverrideRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.OverrideID = 1;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exeption will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    DeleteQualificationOverrideResponse res = api.DeleteQualificationOverride(req);

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
    Dim req as new DeleteQualificationOverrideRequest()

    req.CustomerID = 1
    req.OverrideID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As DeleteQualificationOverrideResponse = api.DeleteQualificationOverride(req)

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
    $req->OverrideID = 1;
    $req->CustomerKey = "1";

    //Send Request to Server and Get Response
    $res = $api.DeleteQualificationOverride($req);

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
    DeleteQualificationOverrideRequest req = new DeleteQualificationOverrideRequest();

    req.setCustomerID(1);
    req.setOverrideID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    DeleteQualificationOverrideResponse res = api.getExigoApiSoap().deleteQualificationOverride(req, auth);

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

### GetCustomReport

> Returns a custom report in dataset format.

| | |
|---|---|
| Category | Reporting |
| REST | `GET /3.0/report?reportID=1` |
| SOAP action | `https://api.exigo.com/GetCustomReport` |
| WSDL elements | `GetCustomReportRequest` → `GetCustomReportResult` |
| CSV output | Yes — `GET https://api.exigo.com/3.0/csv/?method=GetCustomReport&ApiLoginName=…&ApiPassword=…&ApiCompany=…` |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetCustomReport |

#### Input

**`GetCustomReportRequest`**

| Property | Type | Notes |
|---|---|---|
| `ReportID` | `Int32` | Unique Report ID.<br>**Lookup:** company-specific list (see company-lists.md) |
| `Parameters` | `ParameterRequest[]` | **Lookup:** company-specific list (see company-lists.md) |

**`ParameterRequest`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `ParameterName` | `String` | Optional. |
| &nbsp;&nbsp;↳ `Value` | `Object` |  |

#### Output

**`GetCustomReportResponse`**

| Property | Type | Notes |
|---|---|---|
| `ReportData` | `DataSet` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/report?reportID=1
  &parameters[0][ParameterName]=1
  &parameters[0][Value]=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "reportData": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetCustomReport"

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
    <GetCustomReportRequest xmlns="http://api.exigo.com/">
      <ReportID>int</ReportID>
      <Parameters>
        <ParameterRequest>
          <ParameterName>string</ParameterName>
          <Value />
        </ParameterRequest>
      </Parameters>
    </GetCustomReportRequest>
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
    <GetCustomReportResult xmlns="http://api.exigo.com/">
      <ReportData>
        <xsd:schema>schema</xsd:schema>xml</ReportData>
    </GetCustomReportResult>
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
    var req = new GetCustomReportRequest();

    req.ReportID = 1;               //Unique Report ID

    //Add Parameters
    var parameters = new List<ParameterRequest>();

    var parameter1 = new ParameterRequest();
    parameter1.ParameterName = "1";
    parameter1.Value = 1;
    parameters.Add(parameter1);

    var parameter2 = new ParameterRequest();
    parameter2.ParameterName = "2";
    parameter2.Value = 2;
    parameters.Add(parameter2);

    //Now attach the list to the request
    req.Parameters = parameters.ToArray();

    //Send Request to Server and Get Response
    var res = await api.GetCustomReportAsync(req);

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
    GetCustomReportRequest req = new GetCustomReportRequest();

    req.ReportID = 1;               //Unique Report ID

    //Add Parameters
    List<ParameterRequest> parameters = new List<ParameterRequest>();

    ParameterRequest parameter1 = new ParameterRequest();
    parameter1.ParameterName = "1";
    parameter1.Value = 1;
    parameters.Add(parameter1);

    ParameterRequest parameter2 = new ParameterRequest();
    parameter2.ParameterName = "2";
    parameter2.Value = 2;
    parameters.Add(parameter2);

    //Now attach the list to the request
    req.Parameters = parameters.ToArray();

    //Send Request to Server and Get Response
    GetCustomReportResponse res = api.GetCustomReport(req);

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
    Dim req as new GetCustomReportRequest()

    req.ReportID = 1

    'Add Parameters
    Dim parameters As New List(Of ParameterRequest)()

    Dim parameter1 as new ParameterRequest()
    parameter1.ParameterName = "1"
    parameter1.Value = 1
    parameters.Add(parameter1)

    Dim parameter2 as new ParameterRequest()
    parameter2.ParameterName = "2"
    parameter2.Value = 2
    parameters.Add(parameter2)

    'Now attach the list to the request
    req.Parameters = parameters.ToArray()

    'Send Request to Server and Get Response
    Dim res As GetCustomReportResponse = api.GetCustomReport(req)

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
    $parameter1->Value = 1;

    $parameter2->ParameterName = "2";
    $parameter2->Value = 2;

    //Now attach the list to the request
    req.Parameters = array(parameter1,parameter2);

    //Send Request to Server and Get Response
    $res = $api.GetCustomReport($req);

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
    GetCustomReportRequest req = new GetCustomReportRequest();

    req.setReportID(1);

    //Add Parameters
    ArrayOfParameterRequest parameters = new ArrayOfParameterRequest();

    ParameterRequest parameter1 = new ParameterRequest();
    parameter1.setParameterName("1");
    parameter1.setValue(1);
    parameters.Add(parameter1);

    ParameterRequest parameter2 = new ParameterRequest();
    parameter2.setParameterName("2");
    parameter2.setValue(2);
    parameters.Add(parameter2);

    //Now attach the list to the request
    req.setParameters(parameters);

    //Send Request to Server and Get Response
    GetCustomReportResponse res = api.getExigoApiSoap().getCustomReport(req, auth);

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
https://api.exigo.com/3.0/csv/customreport.aspx
?ApiLoginName=String
&ApiPassword=String
&ApiCompany=String
&ReportID=Int32
&ParamName1=ParamValue
&ParamName2=ParamValue
Response FieldsFieldHeader1,FieldHeader2,FieldHeader3
FieldValue1,FieldValue2,FieldValue3

                    © 2026 Exigo.
```

</details>

---

### GetCommissionReport

> Returns a commission report in json format.

| | |
|---|---|
| Category | Reporting |
| REST | `GET /3.0/commissions?periodType=1` |
| SOAP action | `https://api.exigo.com/GetCommissionReport` |
| WSDL elements | `GetCommissionReportRequest` → `GetCommissionReportResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetCommissionReport |

#### Input

**`GetCommissionReportRequest`**

| Property | Type | Notes |
|---|---|---|
| `PeriodType` | `Int32` | Optional. Required. Defaults to 0. |
| `PeriodID` | `Int32` | Optional. Will default to current period. |
| `ReportName` | `String` | Optional. Unique Report Name. |
| `ParameterData` | `String` | Optional. Json string with the required data for the report requested. |

#### Output

**`GetCommissionReportResponse`**

| Property | Type | Notes |
|---|---|---|
| `ReportData` | `String` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/commissions?periodType=1
  &periodID=1
  &reportName=1
  &parameterData=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "reportData": "",
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetCommissionReport"

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
    <GetCommissionReportRequest xmlns="http://api.exigo.com/">
      <PeriodType>int</PeriodType>
      <PeriodID>int</PeriodID>
      <ReportName>string</ReportName>
      <ParameterData>string</ParameterData>
    </GetCommissionReportRequest>
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
    <GetCommissionReportResult xmlns="http://api.exigo.com/">
      <ReportData>string</ReportData>
    </GetCommissionReportResult>
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
    var req = new GetCommissionReportRequest();

    req.PeriodType = 1;             //Required.
    req.PeriodID = 1;               //Will default to current period.
    req.ReportName = "1";           //Unique Report Name
    req.ParameterData = "1";        //Json string with the required data for the report requested.

    //Send Request to Server and Get Response
    var res = await api.GetCommissionReportAsync(req);

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
    GetCommissionReportRequest req = new GetCommissionReportRequest();

    req.PeriodType = 1;             //Required.
    req.PeriodID = 1;               //Will default to current period.
    req.ReportName = "1";           //Unique Report Name
    req.ParameterData = "1";        //Json string with the required data for the report requested.

    //Send Request to Server and Get Response
    GetCommissionReportResponse res = api.GetCommissionReport(req);

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
    Dim req as new GetCommissionReportRequest()

    req.PeriodType = 1
    req.PeriodID = 1
    req.ReportName = "1"
    req.ParameterData = "1"

    'Send Request to Server and Get Response
    Dim res As GetCommissionReportResponse = api.GetCommissionReport(req)

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

    $req->PeriodType = 1;
    $req->PeriodID = 1;
    $req->ReportName = "1";
    $req->ParameterData = "1";

    //Send Request to Server and Get Response
    $res = $api.GetCommissionReport($req);

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
    GetCommissionReportRequest req = new GetCommissionReportRequest();

    req.setPeriodType(1);
    req.setPeriodID(1);
    req.setReportName("1");
    req.setParameterData("1");

    //Send Request to Server and Get Response
    GetCommissionReportResponse res = api.getExigoApiSoap().getCommissionReport(req, auth);

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

### GetSQLReport

> Returns a SQL report in dataset format.

| | |
|---|---|
| Category | Reporting |
| REST | `GET /3.0/sqlreport?reportID=1` |
| SOAP action | `https://api.exigo.com/GetSQLReport` |
| WSDL elements | `GetSQLReportRequest` → `GetSQLReportResult` |
| CSV output | Yes — `GET https://api.exigo.com/3.0/csv/?method=GetSQLReport&ApiLoginName=…&ApiPassword=…&ApiCompany=…` |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetSQLReport |

#### Input

**`GetSQLReportRequest`**

| Property | Type | Notes |
|---|---|---|
| `ReportID` | `Int32` | Unique Report ID.<br>**Lookup:** company-specific list (see company-lists.md) |
| `ReportEngineVersion` | `Int32` | Optional. Report Engine Version. Default Value is 2. |
| `Parameters` | `ParameterRequest[]` | **Lookup:** company-specific list (see company-lists.md) |

**`ParameterRequest`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `ParameterName` | `String` | Optional. |
| &nbsp;&nbsp;↳ `Value` | `Object` |  |

#### Output

**`GetSQLReportResponse`**

| Property | Type | Notes |
|---|---|---|
| `ReportData` | `DataSet` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/sqlreport?reportID=1
  &reportEngineVersion=1
  &parameters[0][ParameterName]=1
  &parameters[0][Value]=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "reportData": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetSQLReport"

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
    <GetSQLReportRequest xmlns="http://api.exigo.com/">
      <ReportID>int</ReportID>
      <ReportEngineVersion>int</ReportEngineVersion>
      <Parameters>
        <ParameterRequest>
          <ParameterName>string</ParameterName>
          <Value />
        </ParameterRequest>
      </Parameters>
    </GetSQLReportRequest>
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
    <GetSQLReportResult xmlns="http://api.exigo.com/">
      <ReportData>
        <xsd:schema>schema</xsd:schema>xml</ReportData>
    </GetSQLReportResult>
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
    var req = new GetSQLReportRequest();

    req.ReportID = 1;               //Unique Report ID
    req.ReportEngineVersion = 1;    //Optional. Report Engine Version. Default Value is 2.

    //Add Parameters
    var parameters = new List<ParameterRequest>();

    var parameter1 = new ParameterRequest();
    parameter1.ParameterName = "1";
    parameter1.Value = 1;
    parameters.Add(parameter1);

    var parameter2 = new ParameterRequest();
    parameter2.ParameterName = "2";
    parameter2.Value = 2;
    parameters.Add(parameter2);

    //Now attach the list to the request
    req.Parameters = parameters.ToArray();

    //Send Request to Server and Get Response
    var res = await api.GetSQLReportAsync(req);

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
    GetSQLReportRequest req = new GetSQLReportRequest();

    req.ReportID = 1;               //Unique Report ID
    req.ReportEngineVersion = 1;    //Optional. Report Engine Version. Default Value is 2.

    //Add Parameters
    List<ParameterRequest> parameters = new List<ParameterRequest>();

    ParameterRequest parameter1 = new ParameterRequest();
    parameter1.ParameterName = "1";
    parameter1.Value = 1;
    parameters.Add(parameter1);

    ParameterRequest parameter2 = new ParameterRequest();
    parameter2.ParameterName = "2";
    parameter2.Value = 2;
    parameters.Add(parameter2);

    //Now attach the list to the request
    req.Parameters = parameters.ToArray();

    //Send Request to Server and Get Response
    GetSQLReportResponse res = api.GetSQLReport(req);

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
    Dim req as new GetSQLReportRequest()

    req.ReportID = 1
    req.ReportEngineVersion = 1

    'Add Parameters
    Dim parameters As New List(Of ParameterRequest)()

    Dim parameter1 as new ParameterRequest()
    parameter1.ParameterName = "1"
    parameter1.Value = 1
    parameters.Add(parameter1)

    Dim parameter2 as new ParameterRequest()
    parameter2.ParameterName = "2"
    parameter2.Value = 2
    parameters.Add(parameter2)

    'Now attach the list to the request
    req.Parameters = parameters.ToArray()

    'Send Request to Server and Get Response
    Dim res As GetSQLReportResponse = api.GetSQLReport(req)

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
    $req->ReportEngineVersion = 1;

    //Add Parameters

    $parameter1->ParameterName = "1";
    $parameter1->Value = 1;

    $parameter2->ParameterName = "2";
    $parameter2->Value = 2;

    //Now attach the list to the request
    req.Parameters = array(parameter1,parameter2);

    //Send Request to Server and Get Response
    $res = $api.GetSQLReport($req);

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
    GetSQLReportRequest req = new GetSQLReportRequest();

    req.setReportID(1);
    req.setReportEngineVersion(1);

    //Add Parameters
    ArrayOfParameterRequest parameters = new ArrayOfParameterRequest();

    ParameterRequest parameter1 = new ParameterRequest();
    parameter1.setParameterName("1");
    parameter1.setValue(1);
    parameters.Add(parameter1);

    ParameterRequest parameter2 = new ParameterRequest();
    parameter2.setParameterName("2");
    parameter2.setValue(2);
    parameters.Add(parameter2);

    //Now attach the list to the request
    req.setParameters(parameters);

    //Send Request to Server and Get Response
    GetSQLReportResponse res = api.getExigoApiSoap().getSQLReport(req, auth);

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
https://api.exigo.com/3.0/csv/?method=GetSQLReport
&ApiLoginName=String
&ApiPassword=String
&ApiCompany=String
&ReportID=Int32
&ReportEngineVersion=Int32
&Parameters=ParameterRequest[]
Response FieldsReportData
DataSet

                    © 2026 Exigo.
```

</details>

---
