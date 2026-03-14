{{ config
(
materialized='incremental',
schema='Test_Schema2',
incremental_strategy='merge',
unique_key='customer_id'
)}}
with source_data as (
    select 
        *
    from {{ source('subscriber', 'cust_subscriber')}}
)
select
    *
from source_data
{%if is_incremental() %}
where created_time > (select max(created_time) from {{this}})
{%endif%}