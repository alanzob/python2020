import pyodbc

def cleanForInsert (Value):
    ProperValue = Value.replace("'","''")
    return ProperValue

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DSQL-02;'
                      'Database=ISSMeta;'
                      'Trusted_Connection=yes;',autocommit=True)

conn2 = pyodbc.connect('Driver={SQL Server};'
                      'Server=DSQL-02;'
                      'Database=ISSMeta;'
                      'Trusted_Connection=yes;',autocommit=True)




cursor = conn.cursor()


cursor.execute("SELECT top 1 IC.GuidISSColumn , IC.GuidISSTable , IC.Name , IC.KeyType , IC.OrdinalPosition , IC.Datatype , IC.Datalength , IC.NumericScale , IC.IsAllowNull , IC.DefaultValue , CAST(IC.InsertedTimestamp AS VARCHAR(MAX)) InsertedTimestamp , CAST(IC.LastModifiedTimestamp AS VARCHAR(MAX)) LastModifiedTimestamp , IC.Description , IC.IsSystem , IC.IsInInsightSourceDatabase FROM ISSMeta.dbo.ISSColumn AS IC")


#isscolumn = cursor.fetchall()
columnNames = []
for row in cursor.columns(table='ISSColumn'):
    print (row.column_name)
    columnNames.append(row.column_name)
    
print (columnNames)
isscolumn = cursor.fetchall()
insertStatement = ""
for row in isscolumn:
    insertStatement= ("INSERT INTO ISSMeta.dbo.ISSColumnTEST (GuidISSColumn , GuidISSTable , Name , KeyType , OrdinalPosition , Datatype , Datalength , NumericScale , IsAllowNull , DefaultValue , InsertedTimestamp , LastModifiedTimestamp , Description , IsSystem , IsInInsightSourceDatabase) VALUES (")
    insertStatement=insertStatement+ ("'"+cleanForInsert(str(row.GuidISSColumn))+"',"+"'"+cleanForInsert(str(row.GuidISSTable))+"',"+"'"+cleanForInsert(str(row.Name))+"',"+"'"+cleanForInsert(str(row.KeyType))+"',"+"'"+cleanForInsert(str(row.OrdinalPosition))+"',"+"'"+cleanForInsert(str(row.Datatype))+"',"+"'"+cleanForInsert(str(row.Datalength))+"',"+"'"+cleanForInsert(str(row.NumericScale))+"',"+"'"+cleanForInsert(str(row.IsAllowNull))+"',"+"'"+cleanForInsert(str(row.DefaultValue))+"',"+"'"+cleanForInsert(str(row.InsertedTimestamp))+"',"+"'"+cleanForInsert(str(row.LastModifiedTimestamp))+"',"+"'"+cleanForInsert(str(row.Description))+"',"+"'"+cleanForInsert(str(row.IsSystem))+"',"+"'"+cleanForInsert(str(row.IsInInsightSourceDatabase))+"',")
    insertStatement=insertStatement+")"
    insertStatement=insertStatement.replace(",)",")").replace("'None'","NULL")
    
    conn2.execute (insertStatement)
    #print (insertStatement)


    