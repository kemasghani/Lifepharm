# Exigo API — Files/Folders

API version v2025.11.7.6. Crawled 2026-11-11 from https://api.exigo.com/3.0/. Back to [index](../README.md).

Customer file and folder management operations

| Operation | REST | Summary |
|---|---|---|
| [CreateCustomerFolder](#createcustomerfolder) | `POST /3.0/folder` | Creates a folder for the customer in their default directory or a chosen parent folder. |
| [CreateCustomerFile](#createcustomerfile) | `POST /3.0/file` | Creates a file for the customer in their default directory |
| [DeleteCustomerFileFolder](#deletecustomerfilefolder) | `DELETE /3.0/folder` | Deletes a file or folder for the customer in their default directory or a chosen parent folder. |
| [GetCustomerFolders](#getcustomerfolders) | `GET /3.0/folderAuthorization:` | Gets a list of customer folders. |
| [GetFiles](#getfiles) | `GET /3.0/file?customerID=1` | Returns an array of files Note: This request can participate in a transaction. Learn more about transactions. |
| [GetFileContents](#getfilecontents) | `GET /3.0/file/content?customerID=1` | Returns a customer file for the given criteria Note: This request can participate in a transaction. Learn more about transactions. |
| [MoveCustomerFile](#movecustomerfile) | `POST /3.0/file/move` | Moves a customer folder to a provided file. |

---
### CreateCustomerFolder

> Creates a folder for the customer in their default directory or a chosen parent folder.

| | |
|---|---|
| Category | Files/Folders |
| REST | `POST /3.0/folder` |
| SOAP action | `https://api.exigo.com/CreateCustomerFolder` |
| WSDL elements | `CreateCustomerFolderRequest` → `CreateCustomerFolderResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateCustomerFolder |

#### Input

**`CreateCustomerFolderRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exception will occur if CustomerID & CustomerKey are provided. |
| `FolderName` | `String` | Name of new subfolder (do not include path). Must be unique within the parent folder. |
| `ParentFolderID` | `Int32` | Optional. Unique numeric identifier for the parent destination folder. Must be set with existing folder's ID if set. Defaults to customer's root. |

#### Output

**`CreateCustomerFolderResponse`**

| Property | Type | Notes |
|---|---|---|
| `FolderID` | `Int32` | Unique identifier for the new folder. |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/folder HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "folderID": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateCustomerFolder"

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
    <CreateCustomerFolderRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
      <FolderName>string</FolderName>
      <ParentFolderID>int</ParentFolderID>
    </CreateCustomerFolderRequest>
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
    <CreateCustomerFolderResult xmlns="http://api.exigo.com/">
      <FolderID>int</FolderID>
    </CreateCustomerFolderResult>
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
    var req = new CreateCustomerFolderRequest();

    //Send Request to Server and Get Response
    var res = await api.CreateCustomerFolderAsync(req);

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
    CreateCustomerFolderRequest req = new CreateCustomerFolderRequest();

    //Send Request to Server and Get Response
    CreateCustomerFolderResponse res = api.CreateCustomerFolder(req);

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
    Dim req as new CreateCustomerFolderRequest()

    'Send Request to Server and Get Response
    Dim res As CreateCustomerFolderResponse = api.CreateCustomerFolder(req)

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
    $res = $api.CreateCustomerFolder($req);

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
    CreateCustomerFolderRequest req = new CreateCustomerFolderRequest();

    //Send Request to Server and Get Response
    CreateCustomerFolderResponse res = api.getExigoApiSoap().createCustomerFolder(req, auth);

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

### CreateCustomerFile

> Creates a file for the customer in their default directory

| | |
|---|---|
| Category | Files/Folders |
| REST | `POST /3.0/file` |
| SOAP action | `https://api.exigo.com/CreateCustomerFile` |
| WSDL elements | `CreateCustomerFileRequest` → `CreateCustomerFileResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=CreateCustomerFile |

#### Input

**`CreateCustomerFileRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `FileName` | `String` | Name of destination file in customer's folder (do not include path). |
| `FileData` | `Byte[]` | An array of bytes than comprise the file contents. |
| `OverwriteExistingFile` | `Boolean` | Optional. . Defaults to False. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exception will occur if CustomerID & CustomerKey are provided. |
| `FolderName` | `String` | Optional. Name of subfolder (do not include path). If not already existing in the parent folder, subfolder will be created. |
| `ParentFolderID` | `Int32` | Optional. Unique numeric identifier for the parent destination folder. Must be set with existing folder's ID if set. Defaults to customer's root. |

#### Output

**`CreateCustomerFileResponse`**

| Property | Type | Notes |
|---|---|---|
| `FolderID` | `Int32` | Unique identifier for the location of the new file. |
| `FileID` | `Int32` | Unique identifier for the new file. |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/file HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{
  "customerID": 1,
  "fileName": "1",
  "fileData": null,
  "overwriteExistingFile": true,
  "customerKey": "1",
  "folderName": "1",
  "parentFolderID": 1
}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "folderID": 1,
  "fileID": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/CreateCustomerFile"

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
    <CreateCustomerFileRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <FileName>string</FileName>
      <FileData>base64Binary</FileData>
      <OverwriteExistingFile>boolean</OverwriteExistingFile>
      <CustomerKey>string</CustomerKey>
      <FolderName>string</FolderName>
      <ParentFolderID>int</ParentFolderID>
    </CreateCustomerFileRequest>
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
    <CreateCustomerFileResult xmlns="http://api.exigo.com/">
      <FolderID>int</FolderID>
      <FileID>int</FileID>
    </CreateCustomerFileResult>
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
    var req = new CreateCustomerFileRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.FileName = "1";             //Name of destination file in customer's folder (do not include path).

    //Add FileData
    var filedata = new List<Byte>();
    filedata.Add(1);
    filedata.Add(2);

    //Now attach the list to the request
    req.FileData = filedata.ToArray();
    req.OverwriteExistingFile = true;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exception will occur if CustomerID & CustomerKey are provided.
    req.FolderName = "1";           //Name of subfolder (do not include path). If not already existing in the parent folder, subfolder will be created.
    req.ParentFolderID = 1;         //Unique numeric identifier for the parent destination folder. Must be set with existing folder's ID if set. Defaults to customer's root.

    //Send Request to Server and Get Response
    var res = await api.CreateCustomerFileAsync(req);

    //Now examine the results:
    Console.WriteLine("FolderID: {0}", res.FolderID);
    Console.WriteLine("FileID: {0}", res.FileID);
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
    CreateCustomerFileRequest req = new CreateCustomerFileRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.FileName = "1";             //Name of destination file in customer's folder (do not include path).

    //Add FileData
    List<Byte> filedata = new List<Byte>();
    filedata.Add(1);
    filedata.Add(2);

    //Now attach the list to the request
    req.FileData = filedata.ToArray();
    req.OverwriteExistingFile = true;
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exception will occur if CustomerID & CustomerKey are provided.
    req.FolderName = "1";           //Name of subfolder (do not include path). If not already existing in the parent folder, subfolder will be created.
    req.ParentFolderID = 1;         //Unique numeric identifier for the parent destination folder. Must be set with existing folder's ID if set. Defaults to customer's root.

    //Send Request to Server and Get Response
    CreateCustomerFileResponse res = api.CreateCustomerFile(req);

    //Now examine the results:
    Console.WriteLine("FolderID: {0}", res.FolderID);
    Console.WriteLine("FileID: {0}", res.FileID);
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
    Dim req as new CreateCustomerFileRequest()

    req.CustomerID = 1
    req.FileName = "1"

    'Add FileData
    Dim filedata As New List(Of Byte)()
    filedata.Add(1)
    filedata.Add(2)

    'Now attach the list to the request
    req.FileData = filedata.ToArray()
    req.OverwriteExistingFile = true
    req.CustomerKey = "1"
    req.FolderName = "1"
    req.ParentFolderID = 1

    'Send Request to Server and Get Response
    Dim res As CreateCustomerFileResponse = api.CreateCustomerFile(req)

    'Now examine the results:
    Console.WriteLine("FolderID: {0}", res.FolderID)
    Console.WriteLine("FileID: {0}", res.FileID)
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
    $req->FileName = "1";

    //Add FileData

    //Now attach the list to the request
    req.FileData = array(fileDat1,fileDat2);
    $req->OverwriteExistingFile = 1;
    $req->CustomerKey = "1";
    $req->FolderName = "1";
    $req->ParentFolderID = 1;

    //Send Request to Server and Get Response
    $res = $api.CreateCustomerFile($req);

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
    CreateCustomerFileRequest req = new CreateCustomerFileRequest();

    req.setCustomerID(1);
    req.setFileName("1");

    //Add FileData
    ArrayOfSystem.Byte filedata = new ArrayOfSystem.Byte();

    Byte fileDat1 = new Byte();
    filedata.Add(fileDat1);

    Byte fileDat2 = new Byte();
    filedata.Add(fileDat2);

    //Now attach the list to the request
    req.setFileData(filedata);
    req.setOverwriteExistingFile(1);
    req.setCustomerKey("1");
    req.setFolderName("1");
    req.setParentFolderID(1);

    //Send Request to Server and Get Response
    CreateCustomerFileResponse res = api.getExigoApiSoap().createCustomerFile(req, auth);

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

### DeleteCustomerFileFolder

> Deletes a file or folder for the customer in their default directory or a chosen parent folder.

| | |
|---|---|
| Category | Files/Folders |
| REST | `DELETE /3.0/folder` |
| SOAP action | `https://api.exigo.com/DeleteCustomerFileFolder` |
| WSDL elements | `DeleteCustomerFileFolderRequest` → `DeleteCustomerFileFolderResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=DeleteCustomerFileFolder |

#### Input

**`DeleteCustomerFileFolderRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exception will occur if CustomerID & CustomerKey are provided. |
| `FileID` | `Int32` | Optional. Unique numeric identifier for the file to be deleted. |
| `FolderID` | `Int32` | Optional. Unique numeric identifier for the folder to be deleted. Folder must be empty. |

#### Output

**`DeleteCustomerFileFolderResponse`**

_No properties._

#### REST example

```http
DELETE https://yourcompany-api.exigo.com/3.0/folder HTTP/1.1
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
SOAPAction: "https://api.exigo.com/DeleteCustomerFileFolder"

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
    <DeleteCustomerFileFolderRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
      <FileID>int</FileID>
      <FolderID>int</FolderID>
    </DeleteCustomerFileFolderRequest>
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
    <DeleteCustomerFileFolderResult xmlns="http://api.exigo.com/" />
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
    var req = new DeleteCustomerFileFolderRequest();

    //Send Request to Server and Get Response
    var res = await api.DeleteCustomerFileFolderAsync(req);

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
    DeleteCustomerFileFolderRequest req = new DeleteCustomerFileFolderRequest();

    //Send Request to Server and Get Response
    DeleteCustomerFileFolderResponse res = api.DeleteCustomerFileFolder(req);

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
    Dim req as new DeleteCustomerFileFolderRequest()

    'Send Request to Server and Get Response
    Dim res As DeleteCustomerFileFolderResponse = api.DeleteCustomerFileFolder(req)

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
    $res = $api.DeleteCustomerFileFolder($req);

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
    DeleteCustomerFileFolderRequest req = new DeleteCustomerFileFolderRequest();

    //Send Request to Server and Get Response
    DeleteCustomerFileFolderResponse res = api.getExigoApiSoap().deleteCustomerFileFolder(req, auth);

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

### GetCustomerFolders

> Gets a list of customer folders.

| | |
|---|---|
| Category | Files/Folders |
| REST | `GET /3.0/folderAuthorization:` |
| SOAP action | `https://api.exigo.com/GetCustomerFolders` |
| WSDL elements | `GetCustomerFoldersRequest` → `GetCustomerFoldersResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetCustomerFolders |

#### Input

**`GetCustomerFoldersRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exception will occur if CustomerID & CustomerKey are provided. |
| `ParentFolderID` | `Int32` | Optional. Unique numeric identifier for the parent folder to fetch from. Defaults to customer's root. |

#### Output

**`GetCustomerFoldersResponse`**

| Property | Type | Notes |
|---|---|---|
| `FolderCount` | `Int32` | Count of folders returned. |
| `ParentFolderID` | `Int32` | Unique numeric ID of the parent folder. |
| `ParentFolderName` | `String` | Name of the parent folder. |
| `CustomerFolderList` | `CustomerFoldersResponse[]` | List of folders containing the FolderID, FolderName, and count of SubFolders and SubFiles contained by each folder. |

**`CustomerFoldersResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `FolderID` | `Int32` |  |
| &nbsp;&nbsp;↳ `FolderName` | `String` |  |
| &nbsp;&nbsp;↳ `SubFoldersCount` | `Int32` |  |
| &nbsp;&nbsp;↳ `SubFilesCount` | `Int32` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/folderAuthorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "folderCount": 1,
  "parentFolderID": 1,
  "parentFolderName": "",
  "customerFolderList": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetCustomerFolders"

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
    <GetCustomerFoldersRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
      <ParentFolderID>int</ParentFolderID>
    </GetCustomerFoldersRequest>
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
    <GetCustomerFoldersResult xmlns="http://api.exigo.com/">
      <FolderCount>int</FolderCount>
      <ParentFolderID>int</ParentFolderID>
      <ParentFolderName>string</ParentFolderName>
      <CustomerFolderList>
        <CustomerFoldersResponse>
          <FolderID>int</FolderID>
          <FolderName>string</FolderName>
          <SubFoldersCount>int</SubFoldersCount>
          <SubFilesCount>int</SubFilesCount>
        </CustomerFoldersResponse>
      </CustomerFolderList>
    </GetCustomerFoldersResult>
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
    var req = new GetCustomerFoldersRequest();

    //Send Request to Server and Get Response
    var res = await api.GetCustomerFoldersAsync(req);

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
    GetCustomerFoldersRequest req = new GetCustomerFoldersRequest();

    //Send Request to Server and Get Response
    GetCustomerFoldersResponse res = api.GetCustomerFolders(req);

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
    Dim req as new GetCustomerFoldersRequest()

    'Send Request to Server and Get Response
    Dim res As GetCustomerFoldersResponse = api.GetCustomerFolders(req)

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
    $res = $api.GetCustomerFolders($req);

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
    GetCustomerFoldersRequest req = new GetCustomerFoldersRequest();

    //Send Request to Server and Get Response
    GetCustomerFoldersResponse res = api.getExigoApiSoap().getCustomerFolders(req, auth);

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

### GetFiles

> Returns an array of files
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Files/Folders |
| REST | `GET /3.0/file?customerID=1` |
| SOAP action | `https://api.exigo.com/GetFiles` |
| WSDL elements | `GetFilesRequest` → `GetFilesResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetFiles |

#### Input

**`GetFilesRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exception will occur if CustomerID & CustomerKey are provided. |
| `ParentFolderID` | `Int32` | Optional. Unique numeric identifier for folder to get files from. Defaults to customer's root. |

#### Output

**`GetFilesResponse`**

| Property | Type | Notes |
|---|---|---|
| `FileCount` | `Int32` | Count of files returned. |
| `ParentFolderID` | `Int32` | Unique numeric identifier of the file's parent folder. |
| `ParentFolderName` | `String` | Name of the file's parent folder. |
| `CustomerFileList` | `CustomerFilesResponse[]` | List of files containing the FileName, FileID, and customer identifier for each file found. |

**`CustomerFilesResponse`**

| Property | Type | Notes |
|---|---|---|
| &nbsp;&nbsp;↳ `FileName` | `String` | Name of destination file in Customers folder (do not include path). |
| &nbsp;&nbsp;↳ `FileID` | `Int32` | The ID of a successfully created customer file. |
| &nbsp;&nbsp;↳ `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| &nbsp;&nbsp;↳ `CustomerKey` | `String` | Unique alpha numeric identifier for customer record . |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/file?customerID=1
  &customerKey=1
  &parentFolderID=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "fileCount": 1,
  "parentFolderID": 1,
  "parentFolderName": "",
  "customerFileList": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetFiles"

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
    <GetFilesRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
      <ParentFolderID>int</ParentFolderID>
    </GetFilesRequest>
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
    <GetFilesResult xmlns="http://api.exigo.com/">
      <FileCount>int</FileCount>
      <ParentFolderID>int</ParentFolderID>
      <ParentFolderName>string</ParentFolderName>
      <CustomerFileList>
        <CustomerFilesResponse>
          <FileName>string</FileName>
          <FileID>int</FileID>
          <CustomerID>int</CustomerID>
          <CustomerKey>string</CustomerKey>
        </CustomerFilesResponse>
      </CustomerFileList>
    </GetFilesResult>
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
    var req = new GetFilesRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exception will occur if CustomerID & CustomerKey are provided.
    req.ParentFolderID = 1;         //Unique numeric identifier for folder to get files from. Defaults to customer's root.

    //Send Request to Server and Get Response
    var res = await api.GetFilesAsync(req);

    //Now examine the results:
    Console.WriteLine("FileCount: {0}", res.FileCount);
    Console.WriteLine("ParentFolderID: {0}", res.ParentFolderID);
    Console.WriteLine("ParentFolderName: {0}", res.ParentFolderName);

    foreach (var customerFiles  in res.CustomerFileList)
    {
        Console.WriteLine("FileName: {0}", customerFiles.FileName);
        Console.WriteLine("FileID: {0}", customerFiles.FileID);
        Console.WriteLine("CustomerID: {0}", customerFiles.CustomerID);
        Console.WriteLine("CustomerKey: {0}", customerFiles.CustomerKey);
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
    GetFilesRequest req = new GetFilesRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exception will occur if CustomerID & CustomerKey are provided.
    req.ParentFolderID = 1;         //Unique numeric identifier for folder to get files from. Defaults to customer's root.

    //Send Request to Server and Get Response
    GetFilesResponse res = api.GetFiles(req);

    //Now examine the results:
    Console.WriteLine("FileCount: {0}", res.FileCount);
    Console.WriteLine("ParentFolderID: {0}", res.ParentFolderID);
    Console.WriteLine("ParentFolderName: {0}", res.ParentFolderName);

    foreach (CustomerFilesResponse customerFiles  in res.CustomerFileList)
    {
        Console.WriteLine("FileName: {0}", customerFiles.FileName);
        Console.WriteLine("FileID: {0}", customerFiles.FileID);
        Console.WriteLine("CustomerID: {0}", customerFiles.CustomerID);
        Console.WriteLine("CustomerKey: {0}", customerFiles.CustomerKey);
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
    Dim req as new GetFilesRequest()

    req.CustomerID = 1
    req.CustomerKey = "1"
    req.ParentFolderID = 1

    'Send Request to Server and Get Response
    Dim res As GetFilesResponse = api.GetFiles(req)

    'Now examine the results:
    Console.WriteLine("FileCount: {0}", res.FileCount)
    Console.WriteLine("ParentFolderID: {0}", res.ParentFolderID)
    Console.WriteLine("ParentFolderName: {0}", res.ParentFolderName)

    For Each customerFiles As CustomerFilesResponse In res.CustomerFileList
        Console.WriteLine("FileName: {0}", customerFiles.FileName)
        Console.WriteLine("FileID: {0}", customerFiles.FileID)
        Console.WriteLine("CustomerID: {0}", customerFiles.CustomerID)
        Console.WriteLine("CustomerKey: {0}", customerFiles.CustomerKey)
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
    $req->ParentFolderID = 1;

    //Send Request to Server and Get Response
    $res = $api.GetFiles($req);

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
    GetFilesRequest req = new GetFilesRequest();

    req.setCustomerID(1);
    req.setCustomerKey("1");
    req.setParentFolderID(1);

    //Send Request to Server and Get Response
    GetFilesResponse res = api.getExigoApiSoap().getFiles(req, auth);

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

### GetFileContents

> Returns a customer file for the given criteria
>
> Note: This request can participate in a transaction. Learn more about transactions.

| | |
|---|---|
| Category | Files/Folders |
| REST | `GET /3.0/file/content?customerID=1` |
| SOAP action | `https://api.exigo.com/GetFileContents` |
| WSDL elements | `GetFileContentsRequest` → `GetFileContentsResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=GetFileContents |

#### Input

**`GetFileContentsRequest`**

| Property | Type | Notes |
|---|---|---|
| `FileName` | `String` | Optional. File Name requested with file extention. Either FileName or FileID must be provided. |
| `FileID` | `Int32` | Optional. Unique numeric identifier for the file. Either FileName or FileID must be provided. |
| `ParentFolderID` | `Int32` | Optional. Unique numeric identifier for the file's parent folder. Defaults to customer's root. |
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exception will occur if CustomerID & CustomerKey are provided. |

#### Output

**`GetFileContentsResponse`**

| Property | Type | Notes |
|---|---|---|
| `File` | `Byte[]` |  |

#### REST example

```http
GET https://yourcompany-api.exigo.com/3.0/file/content?customerID=1
  &customerKey=1
Authorization: Basic base64Encoded<yourlogin@yourcompany:yourpassword)
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "file": null,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/GetFileContents"

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
    <GetFileContentsRequest xmlns="http://api.exigo.com/">
      <FileName>string</FileName>
      <FileID>int</FileID>
      <ParentFolderID>int</ParentFolderID>
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
    </GetFileContentsRequest>
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
    <GetFileContentsResult xmlns="http://api.exigo.com/">
      <File>base64Binary</File>
    </GetFileContentsResult>
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
    var req = new GetFileContentsRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exception will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    var res = await api.GetFileContentsAsync(req);

    //Now examine the results:

    foreach (var byte  in res.File)
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
    GetFileContentsRequest req = new GetFileContentsRequest();

    req.CustomerID = 1;             //Unique numeric identifier for customer record.
    req.CustomerKey = "1";          //Unique alpha numeric identifier for customer record. Exception will occur if CustomerID & CustomerKey are provided.

    //Send Request to Server and Get Response
    GetFileContentsResponse res = api.GetFileContents(req);

    //Now examine the results:

    foreach (Byte byte  in res.File)
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
    Dim req as new GetFileContentsRequest()

    req.CustomerID = 1
    req.CustomerKey = "1"

    'Send Request to Server and Get Response
    Dim res As GetFileContentsResponse = api.GetFileContents(req)

    'Now examine the results:

    For Each byte As Byte In res.File
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
    $res = $api.GetFileContents($req);

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
    GetFileContentsRequest req = new GetFileContentsRequest();

    req.setCustomerID(1);
    req.setCustomerKey("1");

    //Send Request to Server and Get Response
    GetFileContentsResponse res = api.getExigoApiSoap().getFileContents(req, auth);

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

### MoveCustomerFile

> Moves a customer folder to a provided file.

| | |
|---|---|
| Category | Files/Folders |
| REST | `POST /3.0/file/move` |
| SOAP action | `https://api.exigo.com/MoveCustomerFile` |
| WSDL elements | `MoveCustomerFileRequest` → `MoveCustomerFileResult` |
| CSV output | No |
| Source | https://api.exigo.com/3.0/ExigoApi.asmx?op=MoveCustomerFile |

#### Input

**`MoveCustomerFileRequest`**

| Property | Type | Notes |
|---|---|---|
| `CustomerID` | `Int32` | Unique numeric identifier for customer record. |
| `CustomerKey` | `String` | Optional. Unique alpha numeric identifier for customer record. Exception will occur if CustomerID & CustomerKey are provided. |
| `FileID` | `Int32` | Unique numeric identifier for the file. |
| `FolderID` | `Int32` | Unique numeric identifier for the destination folder. |

#### Output

**`MoveCustomerFileResponse`**

| Property | Type | Notes |
|---|---|---|
| `FileID` | `Int32` | Unique numeric identifier for the file. |
| `FolderID` | `Int32` | Unique numeric identifier for the file's new location. |

#### REST example

```http
POST https://yourcompany-api.exigo.com/3.0/file/move HTTP/1.1
Content-Type: application/json
Authorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)

{}
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: length

{
  "fileID": 1,
  "folderID": 1,
  "result": null
}
```

<details><summary>SOAP 1.1 request / response</summary>

```xml
POST /3.0/ExigoApi.asmx HTTP/1.1
Host: api.exigo.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "https://api.exigo.com/MoveCustomerFile"

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
    <MoveCustomerFileRequest xmlns="http://api.exigo.com/">
      <CustomerID>int</CustomerID>
      <CustomerKey>string</CustomerKey>
      <FileID>int</FileID>
      <FolderID>int</FolderID>
    </MoveCustomerFileRequest>
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
    <MoveCustomerFileResult xmlns="http://api.exigo.com/">
      <FileID>int</FileID>
      <FolderID>int</FolderID>
    </MoveCustomerFileResult>
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
    var req = new MoveCustomerFileRequest();

    //Send Request to Server and Get Response
    var res = await api.MoveCustomerFileAsync(req);

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
    MoveCustomerFileRequest req = new MoveCustomerFileRequest();

    //Send Request to Server and Get Response
    MoveCustomerFileResponse res = api.MoveCustomerFile(req);

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
    Dim req as new MoveCustomerFileRequest()

    'Send Request to Server and Get Response
    Dim res As MoveCustomerFileResponse = api.MoveCustomerFile(req)

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
    $res = $api.MoveCustomerFile($req);

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
    MoveCustomerFileRequest req = new MoveCustomerFileRequest();

    //Send Request to Server and Get Response
    MoveCustomerFileResponse res = api.getExigoApiSoap().moveCustomerFile(req, auth);

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
