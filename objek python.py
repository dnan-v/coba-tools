import datetime
import time

datetime_waktu = datetime.timezone
time_waktu = time.altzone

print(datetime_waktu)
print(time_waktu)

programer = "programer"
def programer_makan():
    print(" {} makan nasi bebek ". format(programer))

programing = "programing"
def programing_makan():
    print(" {} makan nasi ayam ". format(programing))

petani = "petani"
def petani_sultan():
    print(" {} makan bebek emas ". format(petani))


programer_makan()
programing_makan()
petani_sultan()