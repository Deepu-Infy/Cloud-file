{{ config(
    materialized='incremental',
	schema='Test_Schema2',
	incremental_strategy='merge',
    unique_key='cusomer_id'    
  )
}}
select * from  {{source('subscriber', 'cust_subscriber')}}
{% if is_incremental() %}
 where created_time > (select max(created_time) from {{this}})
 {% endif %}