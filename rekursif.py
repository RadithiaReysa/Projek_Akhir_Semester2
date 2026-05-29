class Rekursif:
    def total_suara(self, data):
        if len(data) == 0:
            return 0
        
        return (
            data[0].suara +
            self.total_suara(data[1:]))