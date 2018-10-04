# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 12:52:46 2018

@author: Carles
"""
import MySQLdb

name = "state_graph_2"
def StateTableCreation(name):
    con = MySQLdb.connect(
        host = '127.0.0.1',
        port = 3306,
        user="root", passwd="")
    cursor = con.cursor()
    
    sql = 'CREATE DATABASE '+ name
    cursor.execute(sql)
    print("Table" +name + "created")

    edgessql = '''CREATE TABLE edges (
           FromId int(11) ,INDEX USING BTREE (id),
           ToId int(11) ,INDEX USING BTREE (id),
           Occurrence int(11) DEFAULT 0
           ) 
           '''
    print("Table edges created")

    cursor.execute(edgessql)
    
    nodessql = '''CREATE TABLE nodes (
           NodeId int(11), INDEX USING BTREE (id),
           NamesID VARCHAR(20) ,
           EventTypeId VARCHAR(20),
           GD int(11),
           MD int(11),
           Period int(11),
           TeamId VARCHAR(20) ,
           PlayerId VARCHAR(20),
           Zone VARCHAR(20) ,
           Occurence int(11)
           ) 
           '''
    
    cursor.execute(nodessql)
    print("Table nodes created")
    node_infosql = '''CREATE TABLE node_info(
           GameId int(11)
           EventNumber int(11) ,
           previous int(11)
           current int(11) ,
           ) 
           '''
    
    cursor.execute(node_infosql)
    print("Table node_info created")
    
    rewardssql = '''CREATE TABLE rewards(
           NodeId int(11)
           RewardGoal int(11) ,
           RewardWin int(11)
           ) 
           '''
    
    cursor.execute(rewardssql)
    print("Table rewards created")
    pass

StateTableCreation(name= name)