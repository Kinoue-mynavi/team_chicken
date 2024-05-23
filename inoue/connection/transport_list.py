from database import session
from tables import Transport

# 全権取得
transport_list = session.query(Transport).all()

for transport in transport_list:
    print(transport.date)