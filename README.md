# Nutris - Reconhecimento de Alimentos

Nutris é uma aplicação que utiliza da arquitetura YOLOv8 para reconhecer multiplos alimentos em uma imagem.

Os alimentos que a aplicação reconhece no atual momento são:
- Arroz
- Carne
- Feijão
- Frango
- Ovo
- Salada

O retorno da API é uma lista de alimentos encontrados. Dentro da lista possuímos o nome do alimento e suas informações nutricionais para cada 100g, além da contagem daquele alimento encontrado.
## Autores

- [@arthur-cabral](https://www.github.com/arthur-cabral)
- [@giovanna-oliveira](https://www.github.com/giovanna-oliveira)
- [@mateus-gomes](https://www.github.com/mateus-gomes)

## Pré-requisitos

Para replicação do resultado obtido, é necessário a instalação de algumas ferramentas:

- Python 3.10.10
## Rodando

Para executar o projeto apenas alguns passos são necessários.

Clone o projeto no diretório desejado:

```bash
  $ git clone https://github.com/arthur-cabral/be-nutris-food-recognition.git
```

Serão necessárias duas bibliotecas para o funcionamento do projeto, para baixa-las:

```bash
  $ pip3 install django
```
```bash
  $ pip3 install ultralytics
```

Após isso, entre na pasta backendnutris:

```bash
  $ cd backendnutris
```

Agora inicie a aplicação:

```bash
  $ python manage.py runserver
```

Pronto! A aplicação já está rodando localmente em http://localhost:8000
## Utilizando a aplicação

Para fazer um reconhecimento, basta enviar uma requisição para o endpoint  http://localhost:8000/ com o método POST.

O body da requisição deve ser do tipo form-data, com a chave `image`, do tipo `file`.

Para facilitar, pode importar o seguinte curl na sua plataforma de APIs(postman, insomnia, etc.). Apenas será necessário adicionar a imagem que deseja reconhecer.

```
curl --location 'http://localhost:8000/' \
--form 'image=@"/path/to/file"'
```
## Resultados

Esse é um exemplo do retorno da API.
````json
{
    "lista_de_alimentos": [
        {
            "nome_alimento": "Arroz",
            "calorias": 128,
            "gordura": "0,2",
            "proteina": "2,5",
            "carboidrato": "28,1",
            "contagem": 1
        },
        {
            "nome_alimento": "Carne",
            "calorias": 225,
            "gordura": "9",
            "proteina": "29,9",
            "carboidrato": "4,2",
            "contagem": 1
        },
        {
            "nome_alimento": "Feijão",
            "calorias": 76,
            "gordura": "0,5",
            "proteina": "4,8",
            "carboidrato": "13,6",
            "contagem": 1
        },
        {
            "nome_alimento": "Salada (alface)",
            "calorias": 11,
            "gordura": "0,2",
            "proteina": "1,3",
            "carboidrato": "1,7",
            "contagem": 1
        }
    ]
}
````

Essa é a maneira como o modelo reconhece a imagem.
![pf1 (1)](https://github.com/arthur-cabral/be-nutris-food-recognition/assets/61799587/3a104cc2-47d7-4de2-9870-d5e35f8fbd51)



## Licença

[MIT](https://choosealicense.com/licenses/mit/)

