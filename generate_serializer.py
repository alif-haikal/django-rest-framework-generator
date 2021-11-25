import re

def generate_serializer(con,config_dict):
    with con:

        f = open("serializer.txt", "w")

        cur = con.cursor()
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema  = '"+config_dict['schema']+"' ")
        raw_result = cur.fetchall()

        blacklist_char = "(),'"
        
        serializer_code = "from rest_framework import serializers\n"
        for table_name in raw_result:
            table_capitalize = re.sub("[(),_']", ' ', str(table_name)).title().replace(" ","")
            serializer_code = serializer_code + "from "+str(config_dict['application_name'])+".models import "+ table_capitalize +" \n"
            
        for table_name in raw_result:
            
            table_capitalize = re.sub("[(),_']", ' ', str(table_name)).title().replace(" ","")
            table_name = re.sub("["+blacklist_char+"]", '', str(table_name))

            sql = "select column_name  FROM information_schema.columns WHERE table_schema = '"+ str(config_dict['schema']) +"' AND table_name   = '"+ str(table_name) +"';"
            cur.execute(sql)
            rows = cur.fetchall()
            
            serializer_code = serializer_code + "\n# "+table_capitalize+"\n"
            serializer_code = serializer_code + "class "+table_capitalize+"Serializers(serializers.ModelSerializers):\n"
            
            serializer_code = serializer_code + "\n"+" "*4+"class Meta:\n"
            serializer_code = serializer_code + " "*8 +"model = "+table_capitalize+"\n"
            
            str_column_name = ''
            for row in rows:
                str_column_name = str_column_name + "'" +str(row[0]) + "'," 
            
            
            serializer_code = serializer_code + " "*8 +"fields = ["+str_column_name[:-1]+"]\n"
            
    print("\n***********************************************************************************\n")
    f.write(serializer_code)
    print("# SERIALIZER has been generated. Refer serializer.txt ")
    print("\n***********************************************************************************\n")

    f.close()
      