BooleanSearch
===========

To support queries of matching keywords is a “must-have” function in databases. A query term with boolean operations, such as “國際 and 籃球", is very useful to quickly identify required content in databases.
In this HW, we will give you a lot of “Chinese news titles”.  You should implement the query function to support simple boolean operations. Your query time and index time will be accumulated as your ranking.

Method
======

load the query.txt into a list and the source.csv into a dict, check if the word in database one by one and return the title number, and use the set to do boolean at last.