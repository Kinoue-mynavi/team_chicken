from database import session
from tables import transport

import sys
arg = sys.argv

file_name = arg[1]

translist = session.query(transport).all()

s = open("/home/matcha-23training/projects/files/{0}".format(file_name),mode="w", encoding="utf-8")

for item in translist:
    s.write('"' + str(item.date) + '",')
    s.write('"' + str(item.departure) + '",')
    s.write('"' + str(item.arrival) + '",')
    s.write('"' + str(item.via) + '",')
    s.write('"' + str(item.amount) + '",')
    s.write('"' + str(item.seq) + '"')
    s.write("\n")

s.close()
