# What the Retail Banking Data Looks Like
The synthetic retail banking benchmark combines structured account data, transaction histories, customer profiles, and relationship networks to simulate real-world banking analytics challenges.
## Transaction Data
Transaction data captures customer banking activities across channels with fraud labels for detection modeling.
```python
Timestamp_dt,TxnID,Timestamp,SessionID,CustomerID,SrcAccount,DstAccount,Channel,MCC_Group,Amount,FraudLabel
2025/1/1 0:00,532ceea0-846f-4689-80e7-953913c8cbd5,2025/1/1 0:00,,C000352,A92e83abd,,ATM,Groceries,37.84,0
2025/1/1 0:02,cdaeae81-0137-426a-92c7-c88726184fa7,2025/1/1 0:02,,C000965,A3f209383,,ATM,Salary/Benefit,71.31,0
2025/1/1 0:03,68cfb36d-e2a9-4f70-ad4b-3f0029cd17cb,2025/1/1 0:03,,C000441,Adb76359d,,ATM,Other,53.41,0
```          
- transactions_train.csv – Transaction data for fraud detection
## Customer Demographics
Customer demographic and profile information including age, tenure, credit scores, and location data.
```python
CustomerID,Age,Tenure,CreditScore,HomeCity,AnnualSalary
C000001,61.13,1.35,704.15,City096,47958.17
C000002,33.77,4.66,766.62,City023,35542.79
C000003,46.31,5.29,793.35,City096,44178.55
```          
- customers_all.csv – Customer demographics and profiles
## Account Information
Account details including types, balances, credit limits, and opening dates for customer financial profiles.
```python 
CustomerID,AccountID,Type,Balance,Limit,OpenDate
C000001,Aa95695be,credit_card,535.15,24081.77,2019-07-02
C000002,A04c87035,credit_card,188.57,8485.57,2020-09-17
C000002,A7464b435,checking,150.32,,2020-11-22
```          
- accounts_all.csv – Account details and balances
- devices_all.csv – Customer device associations
## Customer Panel Data
Customer panel data tracks credit utilization, payment behavior, and hard inquiries over time for default prediction modeling.
```python
CustomerID,Week,Utilisation,PaymentRatio,HardInquiries,DefaultLabel
C000005,1,0,0,1,0
C000005,2,0,0,0,0
C000005,3,0,0,1,0
C000005,4,0,0,0,0
```          
- customer_panel_train.csv – Customer credit behavior for default prediction
## Device & Security Data
Security-related data includes login patterns, device information, and behavioral biometrics that help with fraud detection and authentication analysis.
```json
[
  {
    "CustomerID": "C000001",
    "SessionID": "551a1ac3-4f20-4ce9-b6d6-c7cb07b460d5",
    "Timestamp": "2025-01-01T01:11:12",
    "City": "City096",
    "IP": "10.145.14.7",
    "DeviceID": "B5E74E",
    "Actions": ["login", "logout"]
  }
]
```   
- device_sessions_all.json – Customer device sessions and activity logs