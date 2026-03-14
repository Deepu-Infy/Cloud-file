{%macro m1(name)%}
select 'Hello,'||{{name}}||'as greeting'
{%endmacro%}