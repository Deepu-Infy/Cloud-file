{{config(materializd='table')}}

select AIRLINE,
count(BOOKING_REFERENCE) as BOOKING_COUNT
from {{source('TEST_SCHEMA1','INTM_BOOKING_FLIGHTS')}}
group by AIRLINE
