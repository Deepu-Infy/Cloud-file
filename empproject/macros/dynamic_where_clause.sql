{% macro dynamic_where_clause(MKTSEGMENT, 
							 key_column, key_value) %}
  WHERE 1=1 -- A common pattern to easily chain conditions
  {% if MKTSEGMENT is not none %}
    AND DEEPU_DB.TEST_SCHEMA1.TPCH_CUSTOMER.C_MKTSEGMENT = '{{ MKTSEGMENT }}'
  {% endif %}
  {% if key_column is not none and key_value is not none %}
    AND {{ key_column }} >= '{{ key_value }}'
  {% endif %}
{% endmacro %}
