{% macro build_where_clause(filters) %}
 
 {% if filters is not none and filters | length >0 %}
  where
    {{ fileters | join(' AND ') }}
  {% endif %}
  
{% endmacro %}