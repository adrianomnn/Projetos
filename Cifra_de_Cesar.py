import random

class Cifra_de_Cesar:

    def __init__(self, caracteres='ABCDEFGHIJKLMNOPQRSTUVWXYZ#$&*@().:,!?[]=+-%abcdefghijklmnopqrstuvwxyz'):
        self.caracteres = caracteres
     
    #método para criptografar um carcater de acordo com a chave passada  
    def criptografar(self, caracter, chave):
        self.caracter = caracter
        self.chave = int(chave)
        tamanho = len(self.caracteres)
        if caracter in self.caracteres:
            posicao = self.caracteres.index(caracter)
            if posicao + chave >= len(self.caracteres):
                return self.caracteres[(posicao+chave)%tamanho]
            else:
                return self.caracteres[posicao+chave]
        else:
            return self.caracter
        
    #método para descriptografar um carcater de acordo com a chave passada    
    def descriptografar(self, caracter, chave):
        self.caracter = caracter
        self.chave = int(chave)
        tamanho = len(self.caracteres)
        if caracter in self.caracteres:
            posicao = self.caracteres.index(caracter)
            if posicao + chave >= len(self.caracteres):
                return self.caracteres[(posicao-chave)%tamanho]
            else:
                return self.caracteres[posicao-chave]
        else:
            return self.caracter
    #método para criptografar um arquivo .txt    
    def criptografar_arquivo (self, nome_arquivo = '', chave = 0):
        self.nome_arquivo = nome_arquivo
        self.chave = chave
        #if abs(self.chave) > len(self.caracteres):
            #self.chave = randint
        if self.chave > 0 and self.chave >= len(self.caracteres):
            self.chave = random.randint(1, len(self.caracteres) - 1)
        if self.chave < 0 and self.chave <= -len(self.caracteres):
            self.chave = random.randint(-len(self.caracteres) + 1, -1)
        novo_texto_criptografado = []
        while True:
            if self.nome_arquivo == '':
                self.nome_arquivo = input('Digite o nome do arquivo:')
            try:
                with open(self.nome_arquivo, 'r') as f:
                    while True:
                        c = f.read(1)
                        if not c:
                            #print ("End of file")
                            break
                        #print ("Read a character:", c)
                        #print('Codificação', teste.criptografar(c, self.chave))
                        criptografia = self.criptografar(c, self.chave)
                        novo_texto_criptografado.append(criptografia)
                    novo_texto_criptografado = ''.join(novo_texto_criptografado)
                    nome_do_arquivo = self.nome_arquivo.split('.')
                    nome = nome_do_arquivo[0] +str('Cripto')
                    final = nome + str('.txt')
                    with open(final, 'w') as f:
                        f.write(novo_texto_criptografado)        
                print('A chave é:', self.chave)
                break
            except FileNotFoundError:
                print('Este arquivo não existe!')
                break
                
    #método para descriptografar um arquivo .txt             
    def descriptografar_arquivo (self, nome_arquivo, chave):
        self.nome_arquivo = nome_arquivo
        self.chave = chave
        texto_descriptografado = []
        while True:
            try:
                with open(self.nome_arquivo, 'r') as f:
                    while True:
                        c = f.read(1)
                        if not c:
                            #print ("End of file")
                            break
                        #print ("Read a character:", c)
                        #print('Codificação', teste.criptografar(c, self.chave))
                        descriptografia = self.descriptografar(c, self.chave)
                        texto_descriptografado.append(descriptografia)
                    texto_descriptografado = ''.join(texto_descriptografado)
                    nome_do_arquivo = self.nome_arquivo.split('.')
                    nome = nome_do_arquivo[0] +str('Descripto')
                    final = nome + str('.txt')
                    with open(final, 'w') as f:
                        f.write(texto_descriptografado)        
                break
            except FileNotFoundError:
                print('Este arquivo não existe!')
                break
               
        
    #método para criptografar um arquivo texto e sobrescrevê-lo, agora, criptografado
    def criptografar_sobrescrever_arquivo (self, nome_arquivo = '', chave = 0):
        self.nome_arquivo = nome_arquivo
        self.chave = chave
        #if abs(self.chave) > len(self.caracteres):
            #self.chave = randint
        while True:
            if self.chave > 0 and self.chave >= len(self.caracteres):
                print('Essa chave não é válida!')
                break
            if self.chave < 0 and self.chave <= -len(self.caracteres):
                print('Essa chave não é válida!')
                break
            novo_texto_criptografado = []
            while True:
                if self.nome_arquivo == '':
                    self.nome_arquivo = input('Digite o nome do arquivo:')
                try:
                    with open(self.nome_arquivo, 'r') as arquivo:
                        for linha in arquivo:
                            for ch in linha:
                                criptografia = self.criptografar(ch, self.chave)
                                novo_texto_criptografado.append(criptografia)        
                    novo_texto_criptografado = ''.join(novo_texto_criptografado)
                    with open(self.nome_arquivo, 'w') as f:
                        f.write(novo_texto_criptografado)
                        f.close()
                    print('A chave é:', self.chave)
                    break
                except FileNotFoundError:
                    print('Este arquivo não existe!')
                    break
            break
