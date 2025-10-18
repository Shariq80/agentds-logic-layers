# What the Food Production Data Looks Like
The synthetic food production benchmark combines time-series demand data, quality control measurements, supply chain records, and event logs to create a comprehensive multimodal dataset reflecting real-world challenges.

## Demand Time Series Data
Weekly sales records across multiple years showing seasonal patterns and regional variations. This data is critical for forecasting and production planning.
```python
region_id,sku_id,week,sku_base,price,base_price,promo_flag,feature_display,stockout_prev,seasonal_index,units_sold_next_week
7,1160,13,55.89,5.34,7.67,1,1,0,0.1974,73.267
10,1132,5,54.86,8.18,8.15,0,1,0,0.1208,57.256
10,1054,2,45.79,8.96,11.13,1,0,1,0.0666,67.878
```          
 - demand_train.csv – Regional demand data for forecasting
## Batch Storage Data
Production batch storage conditions including temperature, humidity, and door opening patterns for shelf life prediction.
```python
batch_id,sku_id,site_id,dwell_hours,mean_temp_F,mean_rh_pct,door_opens_count,shelf_life_remaining_days
10002,1018,8,22,39.32,86.6,25,10.626
10004,1148,6,21,38.35,84.98,23,16.721
10005,1114,9,49,2.72,52.02,35,38.681
```          
```json
Storage Time Series
[
  {
    "batch_id": 10001,
    "series": [
      { "temp_F": 37.4, "rh": 83.6 },
      { "temp_F": 37.6, "rh": 83.7 },
      { "temp_F": 37.2, "rh": 83.5 }
    ],
    "notes": [
      "door cycling high overnight",
      "condensation cleaned"
    ]
  }
]
```          
- batches_train.csv – Batch storage data for shelf life prediction
- storage_timeseries.json – Storage time series with temperature and humidity
## Quality Control: Process Parameters
Production lot data with process parameters and lab plate images for microbiological quality assessment.
```python
lot_id,sku_id,site_id,cook_temp_F,cook_time_min,chill_time_min,acidification_pH,line_speed,sanitation_gap_min,inspector_note,qc_pass
201596,1065,8,170.1,38.2,42.6,5.01,86.8,37.1,no residue on lid,0
200492,1120,3,171.5,29.5,38.6,4.91,79.9,16.5,no residue on lid; no swelling noted,1
201302,1185,10,178.4,43.7,54.3,4.61,64.4,30.8,color within normal variation; package undistorted,1
```
          
Lab Plate Images
 - lots_train.csv – Production lot data with QC results
## Reference Data: Products, Sites & Regions
Reference tables providing product catalog, production sites, and regional information used across all food production challenges.
```python
sku_id,category,storage_class,base_shelf_life_days
1001,Prepared,refrigerated,8
1002,Dairy,refrigerated,15
1003,Produce,produce,13
1004,Produce,produce,5
1005,Meat,refrigerated,12
```   
```python       
Sites Information
site_id,region_id,line_type
1,10,HTST
2,6,HTST
3,4,pack
4,8,HTST
5,4,HTST
```      
```python    
Regional Data
region_id,name,seasonality_amp
1,Region-1,0.709
2,Region-2,0.234
3,Region-3,0.535
4,Region-4,0.246
```      
```python   
Market Memos
region_id,week,memo
1,1,price matching buzz widespread; lighting standard
1,2,"basket down trading signs, promo cadence accelerated — promo signage dense"
1,3,flyers active across chains; music playlist updated
1,4,"pricing signage unchanged, holiday buzz absent"
```          
- products.csv – Product catalog with categories and shelf life
- market_memos.csv – Weekly market intelligence memos
- sites.csv – Production site information
- regions.csv – Regional market data