#-*- coding: utf8 -*-
''' POSTGRES LIST URLS '''

import re

def generate_url(con,config_dict):
    with con:
        
        f = open("url.txt", "w")
        
        cur = con.cursor()
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema  = '"+config_dict['schema']+"' ")        
        raw_result = cur.fetchall()

        blacklist_char = "(),'"

        print("\n***********************************************************************************\n")
        
        for table_name in raw_result:
            table = re.sub("["+blacklist_char+"]", '', str(table_name))
            f.write("# "+table+"\n")
            f.write("url(r'^api/cgiis/(?P<pk>[0-9]+)$', views."+table+"_detail),\n")
            f.write("url(r'^api/cgiis$', views."+table+"),\n\n")
            
        print("# URL has been generated. Refer url.txt ")
        print("\n***********************************************************************************\n")

        f.close()