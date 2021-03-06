class Pesan(object):
    """Sebuah class bernama Pesan.
    Untuk memahami konsep Class dan Object"""
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('Kalimatku mempunyai', len(self.teks), 'karaktaer.')
    def perbarui(self, stringBaru):
        self.teks = stringBaru

#A        
    def apakahTerkandung(self, kata):
        self.kata = kata
        if self.kata in self.teks:
            return True
        else:
            return False

#B        
    def hitungKonsonan(self):
            a = self.teks
            vokal = 'aiueoAIUEO'
            jumlah = 0
            for i in a :
                if i.lower() not in vokal :
                    jumlah += 1
            return jumlah

#C        
    def hitungVokal(self):
            b = self.teks
            vokal = 'aiueoAIUEO'
            jumlah = 0
            for j in b :
                if j in vokal:
                    jumlah += 1
            return jumlah
        
