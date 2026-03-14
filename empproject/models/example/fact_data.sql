
/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

{{ config(materialized='table') }}

with cte as(
select job,dname,count(1) as emp_count,
from emp inner join dept
on emp.deptno=dept.deptno
group by job,dname
order by dname,job)

select dname,job,emp_count from cte