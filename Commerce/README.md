# What the Commerce Data Looks Like
The synthetic commerce benchmark combines structured data, time series, customer profiles, and product imagery to simulate real-world commerce analytics challenges.

## Structured Tabular Data
The commerce datasets capture sales patterns, inventory movements, product details, and customer behaviors across multiple channels and time periods.

```python
sku_id,week,units_sold,price,promo_flag
1,1,51,0.72,0
1,2,41,0.7,0
1,3,47,0.69,0
1,4,50,0.68,0
1,5,72,0.68,0
```          
- sales_history_train.csv – Weekly SKU sales data for demand forecasting
- purchases_train.csv – Customer purchase history for recommendations
- coupon_offers_train.csv – Coupon offers for redemption prediction
- products.csv – Product catalog metadata
- customers.csv – Customer profiles and demographics

## Product Imagery
Visual product data provides essential context for recommendation systems and enhances the richness of the benchmark. These high-quality product images represent the diversity of a commerce catalog.

## Customer Interactions
Customer interaction data captures the digital footprint of shoppers across web, mobile, and in-store touchpoints. This data is crucial for understanding customer journeys and building personalized recommendation systems.
```python
customer_id,order_id,month,sku_id
1,1,1,562
1,2,1,633
1,3,1,573
1,4,1,615
2,6,1,611
```
          
- purchases_train.csv – Customer purchase history for recommendations

## Coupon Offers
Coupon offer data includes customer targeting, discount details, and redemption outcomes for marketing optimization.
```python
offer_id,customer_id,sku_id,category,discount_pct,price_tier,hist_spend,email_open_rate,avg_basket_value,target_redeem
761,381,236,Snacks,5,high,49.48,0.324,20.47,1
989,495,1123,Personal Care,26,low,138.29,0.359,87.96,0
375,188,1389,Small Appliances,25,mid,238.53,0.218,75.50,0
```          
- coupon_offers_train.csv – Coupon offers with redemption data