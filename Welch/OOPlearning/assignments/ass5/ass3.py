from ass5 import ConfigDict


cc = ConfigDict("config_text.json")

print(cc["sql_query"])
print(cc['email_to'])

cc['database'] = 'mysql_managed'

print(cc)
