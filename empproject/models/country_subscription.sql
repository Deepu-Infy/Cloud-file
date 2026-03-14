{{config(
materialized='table')
}} 
with source_data as (
    select 
        *
    from {{ source('customer', 'cust_site') }} -- Referencing your source.yml
)
select
    *
from source_data