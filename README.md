# Como passar de um reCAPTCHA com Python

Este projeto foi desenvolvido para pode "Quebrar" ou melhor PASSAR pelos reCAPTCHA e enfim dar continuidade as suas automações WEB.

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Espero que ajude. 😄

### 📋 Instalação dos Pacotes necessarios

Para começarmos, crie um diretório para inicializarmos nosso projeto. Depois de criado, vamos criar nosso ambiente virtual.

Para criar nosso ambiente virtual temos duas maneiras.

### OBS: Caso você esteja querendo implementar este projeto em seu ambiente corporativo onde a medida de proteção à Rede de sua empresa ira impedir que os comandos PIP sejam executados, é recomendado que entre em contato com a equipe de TI de sua empresa e que eles possam orientar você a como seguir o processo com segurança... 

#### Caso sejá autorizado e mesmo assim continue dando erro ao usar o PIP, use o comando abaixo para referenciar de qual site estão vindo os pacotes:

```
    pip install --trusted-host files.pythonhosted.org "Pacote que deseja instalar por Exemplo:" pandas
```

# Continuando 😁

## Primeira maneira de Instalação

1º Primeiro passo : Abra seu terminal e acesse o diretório criado, Digite o seguinte comando em seu terminal.

```
    py -m venv NomeDoSeuAmbiente
```

2º Segundo passo : Para ativar seu ambiente virtual digite em seu terminal.

```
    NomeDoSeuAmbiente\Scripts\Activate
```

E pronto Ambiente Baixado e Ativado.

## Segunda maneira de instalação

1º Primeiro passo:Abra seu terminal e acesse o diretório criado. Eu recomendo essa maneira pois tem a possibilidade de escolher a versão de Python que queremos usar em nosso projeto... Iremos instalar a Biblioteca Virtualenv e a VirtualenvWrapper-win. Digite em seu terminal:

```
    pip install virtualenv virtualenvwrapper-win
```

2º Segundo passo: Após ter instalado os pacotes, digite o seguinte comando em seu terminal.

```
    virtualenv --python=Caminho/Para/Executavel/Python/QueDeseja/python.exe "NomeDoSeuAmbiente"
```

Substitua o "Caminho/Para/Executavel/Python/QueDeseja/python.exe" pelo caminho seu executavel de python e p "NomeDoSeuAmbiente" pelo nome desejado para o seu Ambiente Virtual.

3º Terceiro passo: Para ativar seu ambiente virtual digite em seu terminal.

```
    NomeDoSeuAmbiente\Scripts\Activate
```

E pronto Ambiente Baixado e Ativado.

# Código 🔩⚙️

### Dependencias

As Bibliotecas que foram usadas no projeto são:

#### Selenium, Undetected-chromedriver, seleniumabsxy e mousekey. 

A Versão de Python recomendada para o projeto e a que foi usada é a 3.10.11, Foi feito testes em versões mais recente mais ouve alguns problemas em algumas Libs.


```
    pip install selenium undetected-chromedriver seleniumabsxy mousekey
```

## Código Principal

```

import time
from seleniumabsxy import coordsclicker, click_on_coords
import undetected_chromedriver as uc
from mousekey import MouseKey
from selenium.webdriver.common.alert import Alert

driver = uc.Chrome()
Alerta = Alert(driver)
mkey = MouseKey()


def captcha():
    mkey.left_click_xy_natural(
        849,
        678,
        delay=.3,
        min_variation=-10,
        max_variation=10,
        use_every=4,
        sleeptime=(0.005, 0.009),
        print_coords=True,
        percent=90,
    )

def pesquisar():
    mkey.left_click_xy_natural(
        996,
        683,
        delay=2,
        min_variation=-10,
        max_variation=10,
        use_every=4,
        sleeptime=(0.005, 0.009),
        print_coords=True,
        percent=90,
    )

def passarCaptcha():

    coordsclicker.driver = driver
    driver.get("https://jurisprudencia.trt15.jus.br/")
    driver.maximize_window()

    time.sleep(2)
    captcha()

    time.sleep(10)
    pesquisar()

    time.sleep(5)

    driver.close()

passarCaptcha()
```

## Código segundario para a capitura das Cordenadas

Para fazer a capitura das cordenadas onde deseja simular sigas os passos abaixo:


1º Primeiro passo: Vá ao seu terminal, verifique se seu ambiente virtual está ativo, se estiver ativo, entre no console do Python digitando python. Feito isso digite no console:

```
exec(open(r"Caminho/DoSeu/Projeto.py").read())
```

Substitua o "Caminho/DoSeu/Projeto.py" pelo caminho real do seu arquivo que deseja executar, este comando fará que o arquivo seja executado em um console interativo, onde você pode codar, chamar funções e interagir com a automação em tempo real.


2º Segundo passo: Direcione o mouse aonde deseja move e simular o clique do mouse e precione o comando (CTRL + ALT + K), isso exibira no seu console as cordenadas atual do mouse.

Pronto, só inserir as cordenadas no código principal e o código está feito.

```
from seleniumabsxy import set_show_hotkey_coords, coordsclicker
import undetected_chromedriver as uc
from time import sleep

if __name__=="__main__":
    set_show_hotkey_coords(hotkey='ctrl+alt+k')
    driver = uc.Chrome()
    coordsclicker.driver = driver
    sleep(5)
    driver.get("https://jurisprudencia.trt15.jus.br/")
    driver.maximize_window()
```

## ✒️ Autores

Este projeto foi desenvolvido e usado algumas ferramentas feitas por:

* **Hans alemão** - *Trabalho Inicial* - ([HansAlemao](https://github.com/linkParaPerfil)) 

* **Documentação das Libs feitas pelo Hans Alemão** - *Documentação* - ([Hans alemao](pypi.org/user/hansalemao))

* **Higor** - *Projeto Adaptado e criado* - ([Higor3693](https://github.com/Higor3693?tab=projects))
