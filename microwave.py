import time
import keyboard

def countdown(time_sec):
    waktu_awal = time.time()
    waktu_akhir = waktu_awal + time_sec

    while time.time() < waktu_akhir:
        remaining_time = int(waktu_akhir - time.time())
        mins, secs = divmod(remaining_time, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        if keyboard.is_pressed('esc'):
            print("00:00")
            print("Waktu selesai")   
            time.sleep(0.3)         
            return
        elif keyboard.is_pressed('enter'):
                waktu_akhir += 30
                time.sleep(0.3)
        
    print("00:00")
    print("Waktu selesai")


print("Mode yang bisa dipilih adalah manual, defrost, popcorn, coffee/milk, dan reheat")
mode = input("Pilih mode yang diinginkan: ")

if mode == "manual":
    suhu = int(input("Pilih suhu yang diinginkan (celcius): "))
    waktu = int(input("Tentukan lama proses pemanasan (detik): "))
    detik = waktu
    menit = detik//60
    detik -= menit*60
    print(f"Microwave akan bekerja pada suhu {suhu} derajat celcius selama {menit} menit {detik} detik")
elif mode == "defrost":
    waktu = 12*60
    print("Microwave akan bekerja pada suhu 40 derajat celcius selama 12 menit")
elif mode == "popcorn":
    waktu = 3*60
    print("Microwave akan bekerja pada suhu 180 derajat celcius selama 3 menit")
elif mode == "coffee/milk":
    waktu = 2*60
    print("Microwave akan bekerja pada suhu 60 derajat celcius selama 2 menit")
elif mode == "reheat":
    waktu = 4*60
    print("Microwave akan bekerja pada suhu 60 derajat celcius selama 4 menit")

countdown(waktu)