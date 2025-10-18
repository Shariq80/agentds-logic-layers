# What the Manufacturing Data Looks Like
The synthetic manufacturing dataset contains multimodal data that simulates real-world industrial environments, including sensor readings, quality inspection records, and production schedules.

## Predictive Maintenance: Sensor Data
Time-series sensor data from manufacturing equipment, capturing temperature, vibration, and pressure readings for failure prediction, along with operator and production logs.

```python
timestamp,machine_id,temperature_c,vibration_mms,pressure_kpa,failure_24h
2025-01-01T00:00:00Z,MCH_001,70.0,0.25,100.0,0
2025-01-01T00:00:00Z,MCH_003,70.0,0.25,100.0,0
2025-01-01T00:00:00Z,MCH_006,70.0,0.25,100.0,0
2025-01-01T00:00:00Z,MCH_008,70.0,0.25,100.0,0
2025-01-01T00:00:00Z,MCH_010,70.0,0.25,100.0,0
```          
```json
Operator Logs
[
  {
    "date": "2025-01-01",
    "shift": 1,
    "machine_id": "MCH_007",
    "operator_id": "OP_065", 
    "operator_name": "Jessica Lee",
    "log_text": "MCH_007 is operating smoothly without any issues."
  }
]
```
- sensor_readings_train.csv – Sensor data for predictive maintenance
- operator_logs.json – Operator observations and logs
## Quality Cost Prediction: Batch Data
Production batch data with manufacturing parameters and associated rework costs for quality cost prediction.
```python
unit_id,machine_id,speed_rpm,feed_mm_rev,coolant_pct,target_temp_c,ReworkCostUSD
U00001,MCH_049,1149.0,0.069,14.1,952.0,11.68
U00003,MCH_005,1986.0,0.084,13.9,1048.0,132.55
U00004,MCH_044,3255.0,0.19,9.7,1039.0,42.38
U00008,MCH_029,847.0,0.129,15.1,978.0,6.44
```
- batches_train.csv - Production batch data with rework costs
## Production Delay Forecasting: Shift Workload
Shift workload data with planned jobs, processing times, and environmental conditions for predicting production delays.
```python
Shift Workload Data
date,shift,machine_id,planned_jobs,avg_proc_time_min,std_proc_time_min,ambient_temp_c,HoursDelayed
2025-01-01,1,MCH_001,12,28.1,14.84,25.4,2.77
2025-01-01,1,MCH_003,14,38.83,18.63,22.4,2.23
2025-01-01,1,MCH_005,15,28.99,15.72,27.1,11.22
2025-01-01,1,MCH_006,10,35.38,19.71,23.1,1.72
```
```json          
Production Logs
[
  {
    "date": "2025-01-01",
    "shift": 1,
    "machine_id": "MCH_001",
    "operator_id": "OP_034",
    "operator_name": "William Thomas",
    "log_text": "Shift 1 on MCH_001 - standard operating procedures. 12 jobs processed."
  }
]
```          
- shift_workload_train.csv – Shift workload data for delay forecasting
- production_logs.json – Production shift summaries