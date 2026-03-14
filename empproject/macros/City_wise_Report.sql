{% macro custom_grp(col_list) %}
group by
{% for col in col_list %}
{{col}} {% if not loop.last %},{% endif %}
{% endfor %}
{% endmacro %}