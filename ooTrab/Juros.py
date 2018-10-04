class Juros(object):

    def __init__(self, vInicial, taxa, tempo, montante):
        self.vInicial = vInicial
        self.taxa = taxa
        self.tempo = tempo
        self.montante = montante


    def jurosSimplesMontante(Juros):
        Juros.montante = Juros.vInicial*(1 + (Juros.taxa/100) * Juros.tempo)
        return Juros

    def jurosSimplesVinicial(Juros):
        Juros.vInicial = Juros.montante/(1 + (Juros.taxa/100) * Juros.tempo)

        return Juros

    def jurosSimplesTaxa(Juros):


        return Juros

    def jurosSimplesPeriodo(Juros):


        return Juros

    def jurosCompostosMontante(Juros):
        Juros.montante = Juros.vInicial*(1+(Juros.taxa/100))**Juros.tempo

        return Juros

    def jurosCompostosVinicial(Juros):


        return Juros

    def jurosCompostosTaxa(Juros):


        return Juros

    def jurosCompostosPerioso(Juros):



        return Juros
