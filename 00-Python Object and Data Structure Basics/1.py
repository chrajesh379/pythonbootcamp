from datetime import datetime, timedelta
from pytz import timezone,utc
from pyspark.sql.types import StructField, StructType, ArrayType, LongType, StringType, BooleanType, TimestampType, \
    IntegerType, DoubleType,DateType,Row


now = datetime.now()
date_format='%Y-%m-%d %H:%M:%S.%f'
pst_date = datetime.now(tz=utc).astimezone(timezone('US/Pacific')).strftime(date_format)
v_date = datetime.strptime(pst_date,date_format).date()

def list_analysis():
    # List are Mutable
    #List items are ordered, changeable, and allow duplicate values.
    #When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
    #The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.



    l1 = [1,2,"abc",3,3.0]
    print(l1[1])
    l2=['a', ['bb', 'cc'], 'd']
    print(l2[1])
    print(l2[1][0])
    l2.append("f")
    print(l2)
    l2.append(["gg","hh"])
    print(l2)
    l2[1].insert(0,"bc")
    print(l2)
    l3=[(1,2),(3,4),(5,6)]
    print(l2[3])
    l3.append("7")
    print(l3)
    l3.append((8,9))
    print(l3)
    l4=[1,4,2,5,3,9,8]
    l4.sort()
    print(l4)

def dict_analysis():
    d1 = {1:"apple",2:"orange"}
    print(d1.items())
    d2={"edp.sales.shipment":"snapshotdate"
        ,"edp.sales.contract":"snapshotdate"
        ,"edp.sales.carepack": "snapshotdate"
        }
    print(d2)
    v_sql=''
    for k,v in d2.items():
        v_sql += f" UNION ALL SELECT MAX({v}) AS snapshot_date,'{k.split('.')[2]}' as table_name FROM {k}"
        print(v_sql)
    print("update sql")
    v_sql = f"{v_sql[11:]}"
    print(v_sql)
    v_sql = f"SELECT * FROM ({v_sql}) WHERE date(snapshot_date)!='{v_date}'"
    print(v_sql)

def convert_listof_dict():
    l1=[{'name': 'insights', 'type': 'INTEGER'}, {'name': 'changestatus', 'type': 'STRING'}, {'name': 'isdebug', 'type': 'BOOLEAN'}
        , {'name': 'feedbased', 'type': 'BOOLEAN'}, {'name': 'linkedcount', 'type': 'INTEGER'},
        {'mode': 'REPEATED', 'name': 'linkedincidents', 'type': 'INTEGER'}, {'name': 'parent', 'type': 'STRING'}, {'name': 'notifytime', 'type': 'TIMESTAMP'}
        , {'name': 'rawclosereason', 'type': 'STRING'}, {'name': 'openduration', 'type': 'INTEGER'}
        , {'name': 'attachment', 'type': 'STRING'}, 
        {'fields': [{'name': 'type', 'type': 'STRING'}, {'name': 'value', 'type': 'STRING'}], 'mode': 'REPEATED', 'name': 'labels', 'type': 'RECORD'}
        , {'name': 'closed', 'type': 'TIMESTAMP'}, {'name': 'reason', 'type': 'STRING'}, {'name': 'rawname', 'type': 'STRING'}, {'name': 'rawtype', 'type': 'STRING'}
        , {'name': 'autime', 'type': 'INTEGER'}, {'name': 'account', 'type': 'STRING'}, {'name': 'cacheversn', 'type': 'INTEGER'}
        , {'name': 'version', 'type': 'INTEGER'}, {'name': 'readonlyroles', 'type': 'STRING'}, {'name': 'vulcanmode', 'type': 'STRING'}
        , {'name': 'vulcanstatus', 'type': 'STRING'}, {'name': 'tmp', 'type': 'INTEGER'}
        , {'mode': 'REPEATED', 'name': 'test', 'type': 'STRING'}, {'name': 'sourcebrand', 'type': 'STRING'}
        , {'mode': 'REPEATED', 'name': 'regionsmarketing', 'type': 'STRING'}, {'name': 'phase', 'type': 'STRING'}
        , {'name': 'heaptarget', 'type': 'STRING'}, {'name': 'dbotstatus', 'type': 'STRING'}, {'name': 'dbotmirrorlastsync', 'type': 'TIMESTAMP'}
        , {'name': 'dbotmirrorinstance', 'type': 'STRING'}, {'name': 'dbotmirrordirection', 'type': 'STRING'}
        , {'name': 'dbotduedate', 'type': 'TIMESTAMP'}, {'name': 'dbotcreatedby', 'type': 'STRING'},
        {'name': 'closinguserid', 'type': 'STRING'}, {'name': 'lastopen', 'type': 'TIMESTAMP'}, {'name': 'closereason', 'type': 'STRING'}
        , {'name': 'frameworkphase', 'type': 'STRING'}, {'name': 'dbottotaltime', 'type': 'TIMESTAMP'}
        , {'mode': 'REPEATED', 'name': 'botunsubscribedusers', 'type': 'STRING'}, {'mode': 'REPEATED', 'name': 'botreporttable', 'type': 'STRING'}
        , {'mode': 'REPEATED', 'name': 'xsiambotemailcommunication', 'type': 'STRING'}
        , {'fields': [{'name': 'value', 'type': 'STRING'}, {'name': 'total', 'type': 'INTEGER'}], 'mode': 'REPEATED', 'name': 'useremail', 'type': 'RECORD'}
       ]
       print(l1)
    fields_schema = []
    fields_dict = {}
    string_schema = []

    schema_map_1 = {"INTEGER": IntegerType(), "STRING": StringType(), "TIMESTAMP": StringType()
        , "BOOLEAN": BooleanType(), 'FLOAT': LongType(), 'BYTES': StringType()
        , 'DATE': DateType()
                    }

    for field in l1:
        name = field.get("name",'')
        data_type = field.get("type",'')
        fields = field.get("fields", [])
        mode = field.get("mode", 'NULLABLE')
        value_name = ''
        if mode == 'REPEATED' and not fields:
            #print("12")
            # fields_schema.append(StructField(name, ArrayType(schema_map_1[data_type]), True))
            # fields_schema.append(data_type_conversion(name,schema_map_1[data_type]))
            value_name =(StructField(name, ArrayType(schema_map_1[data_type]), True))
            fields_schema.append(value_name)
            string_schema.append(StructField(name, ArrayType(StringType()), True))
        elif data_type != 'RECORD' and not fields:
            # fields_schema.append(data_type_conversion(name,data_type))
            value_name = (StructField(name, schema_map_1[data_type], True))
            fields_schema.append(value_name)
            string_schema.append(StructField(name, StringType(), True))
        elif data_type == 'RECORD':
            sub_col_list = []
            sub_col_list_string =[]
            for sub_col in fields:
                # print(sub_col)
                sub_col_list.append(StructField(sub_col['name'], schema_map_1[sub_col['type']], True))
                sub_col_list_string.append(StructField(sub_col['name'],StringType() , True))
                # print(sub_col_list)
                value_name = (StructField(name, (ArrayType(StructType(list(sub_col_list)), True)), True))
            fields_schema.append(value_name)
            string_schema.append((StructField(name, (ArrayType(StructType(list(sub_col_list_string)), True)), True)))
        fields_dict[name] = value_name
    print(fields_dict)
    print(fields_schema)
    print(string_schema)

def convert_list_to_string():
    list_of_tables="Below are the tables not refreshed: \n"
    l1=[['2023-09-19', 'shipment`'], ['2023-09-19', 'contract`'],
     ['2023-09-19', '_deployment_rate`']]
    for i in l1:
        list_of_tables += f"{i[1]} : {i[0]} \n"
    print(list_of_tables)

def tuple_analysis():
    #Tuples are immutable and used for Data Integrity (Can not chnage the values)
    #Tuple items are ordered, unchangeable, and allow duplicate values.
    #When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
    #Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

    t1=(1,2,3,7,6,5,9)
    print(t1[0])
    print(t1.index(3))
    print(sorted(t1))
    print(t1)

def sets_analysis():
    #sets are unorderes colletion of unique elements
    print("-------------------sets analysis--------------------")
    s = {1,2,3}
    print(s)
    l=[1,1,1,1,1,12,2,2,2,2,8,9,0,0,0,0]
    print(set(l))
    print("-------------------sets analysis--------------------")

if __name__=="__main__":
    list_analysis()
    dict_analysis()
    convert_listof_dict()
    convert_list_to_string()
    tuple_analysis()
    sets_analysis()
