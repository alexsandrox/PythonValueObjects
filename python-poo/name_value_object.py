class NameValueObject:
    def __init__(self, first_name, last_name):
        self.validade_complete_name(first_name, last_name)
        self.first_name = first_name
        self.last_name = last_name

    def to_string(self, first:str, last:str):
        return print('{} {}'.format(first, last))

    def validade_complete_name(self, first:str, last:str):
        if first == None or first == "" or first.isdecimal() or last == None or last == "" or last.isdecimal():
            print('>>  Nome e Sobrenome devem ser preenchidos corretamente')
            return False
        else:
            self.to_string(first, last)
            return True

# testando a classe
name = NameValueObject('Alexsandro', 'Andrade')