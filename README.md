### lmsimpacta
Repostório destinado ao Projeto das Disciplinas da Faculdade Impacta

-------


![logo](https://raw.githubusercontent.com/dbgarcia/lmsimpacta/master/core/static/Impacta1.png "Logo")


-------

Website com Django + Python + Azure

- [Requisitos](#requisitos)

## Requisitos

- [Python 3.4+](https://www.python.org/downloads/)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
- [Django](https://www.djangoproject.com/download/)
- [Nuvem Microsoft Azure](https://azure.microsoft.com/pt-br/)


Configurar Azure, para subir seu `Fork`, você precisar realizar o seguinte passo:

 1. Ir em Web Apps e criar um `Aplicativo Web`;
 2. Ativar o `MySQL no Aplicativo`;
 3. Em `Opções de implantação`, escolhe `Github`;
 4. Escolhe o `Fork` do projeto;
 5. Selecionar branch na qual realizou a modificação e salvar;
 6. Esperar alguns segundos e azure vai atualizar o repositório local para aplicar as modififcações;

-------

Depois faça o `Fork` do projeto ou download, link: `https://github.com/dbgarcia/lmsimpacta.git`

> Se preferir usar via terminal ou prompt de comando:

```bash
$ git remote add origin https://github.com/dbgarcia/lmsimpacta.git
```
```bash
$ git remote -v
```
```bash
$ git push -u origin master
```

Apartir deste momento seu repositorio esta atualizado e configurado. Crie uma nova branch e aplique as modificaçes nesta branch:

> Comandos branch via terminal ou prompt de comando:

```bash
$ git checkout -b [novaFuncaoDjango]
```

> Trocando para a branch:

```bash
$ git checkout [novaFuncaoDjango]
```

> Enviar branch para o github:

```bash
$ git push origin [novaFuncaoDjango]
```


