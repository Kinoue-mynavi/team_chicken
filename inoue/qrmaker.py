import qrcode
import os

def read_file_at_dir(dir_path, filename):
    os.makedirs(dir_path, exist_ok=True)
    f = open(os.path.join(dir_path, filename), "r")
    lines = f.readlines()
    f.close()

    # 改行を取り除いて変換
    return [line.rstrip("\n") for line in lines]

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

OUTPUT_DIRECTORY = "./inoue/output"
INPUT_DIRECTORY = "./inoue"

def create_file(file_name):
    return os.path.join(OUTPUT_DIRECTORY, f"{file_name}.png")
        
if __name__ == "__main__":
    urls = read_file_at_dir(INPUT_DIRECTORY, "urls.txt")

    for i, url in enumerate(urls):
        file_path = create_file(f"{i + 1}")
        generate_qr_code(url, file_path)