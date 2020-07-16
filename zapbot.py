#Importando webdriver do Selenium
from selenium import webdriver

#Importando time para controle de tempo da automação
import time 

#Início Classe WhatsappBot
class WhatsappBot:

    # Criação do método para construir os dados a serem utilizados
    def __init__(self):

        # Configurando os contatos para envio
        self.contatos = ["Moor", "Itamar Maninho"]
        
        # Configurando mensagens para envio
        self.mensagens = ["Oi "," Tudo jóia?"]

        # Selecionando as configurações do Chrome e jogando para uma variável
        options = webdriver.ChromeOptions()

        # Definindo a linguagem do chat
        options.add_argument('lang=pt-br')

        # Executando arquivo para rodar juntamente com o Selenium (ChromeDriver)
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    # Fim do método para construir os dados a serem utilizados   

    # Criação do método para enviar a mensagem
    def EnviarMensagem(self):

        # Definir qual o link que será acessado (Whatsapp Web)
        self.driver.get('https://web.whatsapp.com/')

        # Tempo (segundos) descansando para que seja feita a leitura do código pelo usuário
        time.sleep(15)

        # Um laço de repetição para ler os contatos
        for contato in self.contatos:

            # Altera a posição 0 da lista para pegar nome do contato
            self.mensagens[0] =  "Oi "+contato+" !"

            # Aqui vai procurar um elemento do tipo span que tenha a propriedade title de acordo
            # com os contatos do método construtor
            contato = self.driver.find_element_by_xpath(f"//span[@title='{contato}']")
            for mensagem in self.mensagens:
                # Tempo descansando para que não seja detectado o robô
                time.sleep(3)

                # Clica no contato depois de conferir o title
                contato.click()

                # Localiza a classe onde será digitada a mensagem
                chatBox = self.driver.find_element_by_class_name('_3uMse')

                # Tempo descansando para que não seja detectado o robô
                time.sleep(3)

                # Clica para iniciar a digitação da mensagem
                chatBox.click()

                # Digita a mensagem a ser enviada
                chatBox.send_keys(mensagem)

                # Localiza o elemento do tipo que tenha a propriedade data-icon, no caso, 
                # o botão para enviar a mensagem
                btnEnviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")

                # Tempo descansando para que não seja detectado o robô
                time.sleep(3)

                # Clica no botão para enviar a mensagem
                btnEnviar.click()

                # Tempo descansando para que não seja detectado o robô
                time.sleep(5)

# Define o bot para os dados que serão enviados
bot = WhatsappBot()

# Pede para ele executar o método de enviar a mensagem
bot.EnviarMensagem()