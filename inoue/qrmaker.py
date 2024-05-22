import qrcode
import os

# ターゲットとなるパスを生成
def create_file_path(dir_path, file_name):
    return os.path.join(dir_path, file_name)

# 任意のファイルを読み込む
def read_file_at_dir(dir_path, file_name):
    os.makedirs(dir_path, exist_ok=True)
    f = open(create_file_path(dir_path, file_name), "r")
    lines = f.readlines()
    f.close()

    return [line.rstrip("\n") for line in lines] # 改行を取り除いた上で返却

# QRコードを生成
def generate_qr_code(url, file_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)
    img.show()
        
if __name__ == "__main__":
    # Reading
    urls = read_file_at_dir("./inoue", "urls.txt")

    # Writing
    for i, url in enumerate(urls):
        generate_qr_code(url, create_file_path("./inoue/output", f"{i + 1}.png"))