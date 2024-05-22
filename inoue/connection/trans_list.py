import sys
import os
from database import session
from tables import Transport

args = sys.argv

input_file_name = str(args[1])

def save_file_at_dir(dir_path, filename, file_content, mode='w'):
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, filename), mode) as f:
        f.write(file_content)

# 全権取得
def fetch_all_transport():
    return session.query(Transport).all()

if __name__ == '__main__':
    transport_list = fetch_all_transport()
    text = ""
    for transport in transport_list:
        text += f'"{transport.date}", "{transport.seq}", "{transport.departure}", "{transport.arrival}", "{transport.via}", "{transport.amount}"cccccbjkkvrilkielhvgrjrlftnjihdrnrcuhfbvvfhe
        \n'
    
    save_file_at_dir('./inoue/output', 'output.txt', text)
