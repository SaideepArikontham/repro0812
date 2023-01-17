# Databricks notebook source
# MAGIC %sql
# MAGIC 
# MAGIC delete from demo

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC create table demo(id int, gname varchar(20));
# MAGIC insert into demo values(1,'Ana');
# MAGIC insert into demo values(2,'Ceb');
# MAGIC insert into demo values(3,'Topson');

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC 
# MAGIC create table demo1(id int, team varchar(20));
# MAGIC insert into demo1 values(1,'OG');
# MAGIC insert into demo1 values(2,'OG');
# MAGIC insert into demo1 values(3,'N/A');

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC 
# MAGIC select a.id,a.gname,b.team from demo as a join demo1 as b on a.id=b.id 

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC update demo set id=10 from demo join demo1 on demo.id=demo1.id where demo.id=1

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC --CREATE TEMPORARY VIEW for_updt as (select a.id,a.gname,b.team from demo as a join demo1 as b on a.id=b.id );
# MAGIC 
# MAGIC update demo set id=10 where id in(select id from for_updt where) and (demo.id=1)

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC 
# MAGIC select * from demo

# COMMAND ----------


