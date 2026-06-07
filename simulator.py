import json
import subprocess
from datetime import datetime

FILE_JSON = "data/suhu.json"

while True:
    try:
        suhu = float(input("Masukkan suhu: "))
        kelembaban = float(input("Masukkan kelembaban: "))

        data_baru = {
            "suhu": suhu,
            "kelembaban": kelembaban,
            "waktu": datetime.now().strftime("%H:%M:%S")
        }

        # baca data lama
        with open(FILE_JSON, "r") as file:
            data = json.load(file)

        # tambah data baru
        data.append(data_baru)

        # simpan data
        with open(FILE_JSON, "w") as file:
            json.dump(data, file, indent=4)

        print("Data berhasil disimpan")

        # upload github
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "update data suhu"])
        subprocess.run(["git", "push"])

        print("Data berhasil upload ke GitHub\n")

    except Exception as e:
        print("Terjadi error:", e)
