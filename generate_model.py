import re

def generate_model(con,config_dict):
    with con:

        f = open("model.txt", "w")

        cur = con.cursor()
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema  = '"+config_dict['schema']+"' ")
        raw_result = cur.fetchall()

        blacklist_char = "(),'"
        
        model_code = "from django.db import models\n\n"
            
        for table_name in raw_result:
            
            table_capitalize = re.sub("[(),_']", ' ', str(table_name)).title().replace(" ","")
            table_name = re.sub("["+blacklist_char+"]", '', str(table_name))
            
            sql = "select column_name ,  data_type , udt_name , character_maximum_length , is_nullable FROM information_schema.columns WHERE table_schema = '"+ config_dict['schema'] +"' AND table_name   = '"+ table_name +"';"
            cur.execute(sql)
            rows = cur.fetchall()
            
            model_code = model_code + "# "+table_capitalize+"\n"
            model_code = model_code + "class "+table_capitalize+"(models.Model):\n"

            for row in rows:
                column_name = row[0]
                data_type = row[1] 
                udt_name = row[2]
                character_maximum_length = row[3]
                is_nullable = row[4]

                if "int" in udt_name:
                    model_code = model_code + integer(column_name , is_nullable)
                    
                elif "numeric" in udt_name:
                    model_code = model_code + time(column_name , is_nullable)
                    
                elif "varchar" in udt_name:
                    model_code = model_code + varchar(column_name , is_nullable , character_maximum_length)
                
                elif "char" in udt_name:
                    model_code = model_code + char(column_name , is_nullable , character_maximum_length)

                elif "float" in udt_name:
                    model_code = model_code + float(column_name , is_nullable)
                    
                elif "date" in udt_name:
                    model_code = model_code + date(column_name , is_nullable)

                elif "timestamp" in udt_name:
                    model_code = model_code + timestamp(column_name , is_nullable)
                    
                elif "time" in udt_name:
                    model_code = model_code + time(column_name , is_nullable)
                    
                elif "text" in udt_name:
                    model_code = model_code + text(column_name , is_nullable)
                    
            model_code = model_code + "\n"+" "*4+"class Meta:"
            model_code = model_code + "\n"+" "*8+"db_table = '" + config_dict['schema'] + '"."' + table_name + "'\n\n"

    print("\n***********************************************************************************\n")
    f.write(model_code)
    print("# MODEL has been generated. Refer model.txt ")
    print("\n***********************************************************************************\n")

    f.close()
        
def integer(column_name , is_nullable):
    if is_nullable == "YES":
        return " "*4 +column_name + " = models.IntegerField()\n"
    else:
        return " "*4 +column_name + " = models.IntegerField(blank=False)\n"

def varchar(column_name , is_nullable , character_maximum_length):
    if is_nullable == "YES":
        return " "*4 + str(column_name) + " = models.CharField(max_length="+str(character_maximum_length)+", default='')\n"
    else:
        return " "*4 + str(column_name) + " = models.CharField(max_length="+str(character_maximum_length)+",blank=False, default='')\n"

def char(column_name , is_nullable , character_maximum_length):
    if is_nullable == "YES":
        return " "*4 + str(column_name) + " = models.CharField(max_length="+str(character_maximum_length)+", default='')\n"
    else:
        return " "*4 + str(column_name) + " = models.CharField(max_length="+str(character_maximum_length)+",blank=False, default='')\n"

def float(column_name , is_nullable):
    if is_nullable == "YES":
        return " "*4 +column_name + " = models.FloatField(default='')\n"
    else:
        return " "*4 +column_name + " = models.FloatField(blank=False, default='')\n"
    
def date(column_name , is_nullable):
    if is_nullable == "YES":
        return " "*4 +column_name + " = models.DateField(default='')\n"
    else:
        return " "*4 +column_name + " = models.DateField(blank=False, default='')\n"

def timestamp(column_name , is_nullable):
    if is_nullable == "YES":
        return " "*4 +column_name + " = models.DateTimeField(default='', auto_now_add=True)\n"
    else:
        return " "*4 +column_name + " = models.DateTimeField(blank=False, default='', auto_now_add=True)\n"

def time(column_name , is_nullable):
    if is_nullable == "YES":
        return " "*4 +column_name + " = models.TimeField(default='')\n"
    else:
        return " "*4 +column_name + " = models.TimeField(blank=False, default='')\n"
    
def text(column_name , is_nullable):
    if is_nullable == "YES":
        return " "*4 +column_name + " = models.TextField(default='')\n"
    else:
        return " "*4 +column_name + " = models.TextField(blank=False, default='')\n"    
