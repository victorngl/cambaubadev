# Como acessar o servidor e fazer deploy
Acesse o servidor com o seguinte comando:

``` shell
ssh -p 2250 datacartes@200.218.242.101
```

Insira a seguinte senha:

```shell
D@t@C@rt3s
```

Entre como super usuário com o seguinte comando:

```shell
sudo su
```

Insira novamente a senha caso necessário

Rode os seguintes comandos:

```shell
cd /root/
cd cambauba/
source env_cambauba/bin/activate
cd cambauba/
git pull origin master
```

Adicione o username e o token:
```shell
datacartes
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
```

Faça os seguintes comandos (CASO NECESSÁRIO)
```shell
python manage.py migrate
python manage.py collectstatic
```

Reinicie o servidor com o seguinte comando:
```shell
service gunicorn restart
```

Acesse o servidor e veja se tudo está como você espera
Link: https://intranet.cambauba.com.br/
Usuário: flavio
Senha: Novadata123

Saia do modo super usuário com
```shell
exit
```

Saia do modo servidor com
```shell
exit
```

Deploy feito! Parabéns!