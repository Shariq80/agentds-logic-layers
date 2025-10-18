# What the Insurance Data Looks Like
The synthetic insurance benchmark combines structured, text, image, graph, and document data. These demo samples illustrate the multi-source realism of the challenge datasets.
## Structured Tabular Data
The Structured data forms the backbone of insurance analytics, enabling precise risk assessment and pricing. Our tabular datasets capture the complex relationships between policy attributes, customer characteristics, and risk factors.

```python
PolicyID,HolderAge,VehicleType,AnnualMileage,LocationUrban,CreditScore,PolicyStart,PolicyEnd,NextYearLoss
POL-003116,66.61,Sedan,7145.43,1,0.723,2023/7/30,2024/7/30,0
POL-005296,32.40,SUV,11053.49,1,0.715,2023/4/3,2024/4/3,0
POL-005440,64.24,Sedan,5994.79,1,0.954,2023/11/20,2024/11/20,0
POL-002212,61.80,Sedan,10082.29,1,0.835,2023/11/6,2024/11/6,29716.46
```          
- train_policies_subset.csv – Policy records for risk pricing
- train_claims.csv – Claim records for complexity and fraud prediction

## Claims Data
Claims data contains detailed information about insurance claims including damage amounts, involved parties, claim types, and complexity classifications for fraud detection and complexity prediction.
```python
ClaimID,PolicyID,ClaimDate,ClaimType,ReportedDamage,NumParties,ClaimComplexityLabel,FraudLabel
CLM-000002,POL-000005,2023/4/6 2:32,Theft/Comprehensive,942.04,1,Simple,0
CLM-000003,POL-000010,2024/2/13 4:09,Fender-Bender,8242.20,2,Simple,0
CLM-000004,POL-000012,2023/10/4 8:37,Fender-Bender,9452.74,2,Simple,0
CLM-000005,POL-000026,2023/5/10 23:21,Theft/Comprehensive,813.53,1,Simple,1
```  
- train_claims.csv – Claim records with complexity and fraud labels
- invoice_CLM-000001.pdf – Sample claim invoice     
## Visual Inputs: Imagery Samples
Vehicle images provide crucial visual context for auto insurance risk assessment and claims processing, supporting accurate damage evaluation and repair cost estimation.