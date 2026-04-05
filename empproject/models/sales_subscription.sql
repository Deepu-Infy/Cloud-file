{% set grouping_cols = ['COUNTRY', 'CITY'] %}

SELECT 
    {% for col in grouping_cols -%}
    {{ col }},
    {%- endfor %}
    count(customer_id) as subscription_count
FROM {{ source('subscriber', 'cust_subscriber') }}
GROUP BY 
    {% for col in grouping_cols -%}
    {{ loop.index }}{{ "," if not loop.last }}