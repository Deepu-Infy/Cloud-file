{%macro get_cst_by_id(column_name,filter_value) %}
where {{column_name}}={{filter_value}}
{% endmacro %}
