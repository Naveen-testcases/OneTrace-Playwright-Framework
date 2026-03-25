import os
from openpyxl import Workbook
from PIL import Image


def create_test_files():
    files = {}

    # CSV
    with open("test.csv", "w") as f:
        f.write("id,name\n1,test")
    files["csv"] = os.path.abspath("test.csv")

    # XLSX
    wb = Workbook()
    ws = wb.active
    ws["A1"] = "Test"
    wb.save("test.xlsx")
    files["xlsx"] = os.path.abspath("test.xlsx")

    # JPG
    img = Image.new("RGB", (100, 100), color="blue")
    img.save("test.jpg")
    files["jpg"] = os.path.abspath("test.jpg")

    return files