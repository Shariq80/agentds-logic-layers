# What the Healthcare Data Looks Like
The synthetic healthcare benchmark combines patient demographics, admission records, ED cost history, and discharge planning data to create a comprehensive dataset reflecting real hospital workflows.

## Patient Demographics
Common patient reference table linking demographics across all healthcare challenges.
```python
patient_id,age,sex,insurance,zip3
1,45,M,private,551
2,67,F,public,554
3,34,M,self_pay,553
4,78,F,private,552
5,29,F,public,551
```          
- patients.csv – Patient demographics and insurance info
## Hospital Admissions
Inpatient admission records with clinical indicators for readmission prediction.
```python
admission_id,patient_id,primary_dx,los_days,acuity_emergent,charlson_band,ed_visits_6m,discharge_weekday,readmit_30d
1001,346,Pneumonia,4,1,2,1,3,0
1002,3843,DiabetesComp,6,0,3,2,5,1
1003,972,COPD,8,1,4,3,1,0
1004,2987,CHF,12,1,3,1,6,1
```          
- admissions_train.csv – Training data for readmission prediction
- discharge_notes.json – Discharge summaries per admission

## Emergency Department Costs
Historical ED utilization and cost data for forecasting future healthcare expenses.
```python
patient_id,primary_chronic,prior_ed_visits_5y,prior_ed_cost_5y_usd,ed_cost_next3y_usd
1080,HF,4,1031.3,2818.38
1807,HF,8,5664.15,4966.03
3038,DiabetesComp,3,1025.28,1823.47
1314,DiabetesComp,3,1852.77,2722.92
```          
- ed_cost_train.csv – Historical ED costs and utilization
- receipt_1.pdf – Sample medical receipt
## Hospital Stays
Inpatient stay records with unit types and admission reasons for discharge readiness assessment.
```python
stay_id,patient_id,unit_type,admission_reason,discharge_ready_day11
1493,346,med_surg,Pneumonia,0
1746,3843,stepdown,DiabetesComp,1
592,972,med_surg,DiabetesComp,1
1561,2987,stepdown,COPD,0
```          
- stays_train.csv – Hospital stay records
- vitals_timeseries.json – 10-day vitals and daily notes