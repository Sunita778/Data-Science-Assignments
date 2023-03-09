create database if not exists sql_task;
use sql_task;
-- 1. Create a table attribute dataset and dress dataset.
CREATE TABLE if not exists attribute_data(
Dress_ID int,
Style varchar(30),
Price varchar(30),
Rating decimal(5.0),
Size varchar(30),
Season varchar(30),
NeckLine varchar(30),
SleeveLength varchar(30),
waiseline varchar(30),
Material varchar(30),
FabricType varchar(30),
Decoration varchar(30),
PatternType varchar(30),
Recommendation int
);

CREATE TABLE if not exists dress_data(
Dress_ID int,
`29/8/2013` int,
`31/8/2013` int,
`09/02/2013` int,
`09/04/2013` int,
`09/06/2013` int,
`09/08/2013` int,
`09/10/2013` int,
`09/12/2013` int,
`14/9/2013` int,
`16/9/2013` int,
`18/9/2013` int,
`20/9/2013` int,
`22/9/2013` int,
`24/9/2013` int,
`26/9/2013` int,
`28/9/2013` int,
`30/9/2013` int,
`10/02/2013` int,
`10/04/2013` int,
`10/06/2013`int,
`10/08/2010` int,
`10/10/2013` int,
`10/12/2013` int);

-- 2. Do a bulk load for these two table for respective dataset. 

SHOW GLOBAL VARIABLES LIKE 'local_infile';
set global local_infile = 1;

load data local infile
'/Attribute_DataSet.csv'
into table attribute_data
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 rows;

load data local infile
'/Dress_Sales.csv'
into table dress_data
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 rows;

describe dress_data;
select * from sql_task.attribute_data;
select * from sql_task.dress_data;

-- 6. In sql task try to perform left join operation with attrubute dataset and dress dataset on column Dress_ID
select * from attribute_data left join dress_data on attribute_data.Dress_ID = dress_data.Dress_ID; 

-- 7. Write a sql query to find out how many unique dress that we have based on dress id 
select count(distinct(Dress_ID)) from attribute_data;

-- 8. Try to find out how mnay dress is having recommendation 0
select count(*) from attribute_data where Recommendation = 0;

