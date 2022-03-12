+++
title = "Git e GitHub"
slug = "git-e-github"
date = "2022-03-11 15:26:47 UTC-03:00"
tags = "git, github, controle de versão"
category = ""
link = ""
description = "Breve introdução ao Git e Github"
type = "text"
+++

Na aula de ontem (aula 05) o Fabio falou um pouco sobre Git e GitHub. [Eu já tinha postado a respeito quando falei do repositório com o material do curso](http://pythonassipt.vento.eng.br/posts/repositorio-do-curso/). Expliquei qual a idéia por trás disso mas não entrei mais a fundo. O Fabio só mostrou que o Git e o GitHub pode ser utilizado diretamente do editor [Visual Studio Code](https://code.visualstudio.com/).

## O que é o Git

Git é uma ferramente de controle de versões. O que quer dizer isso? Basicamente ele permite que você gerencie os arquivos de um projeto de software. [Dê uma lida rápida sobre a motivação no post sobre o repositório do curso](http://pythonassipt.vento.eng.br/posts/repositorio-do-curso/).

Quando eu falo gerenciar os arquivos de um projeto de software, eu quero dizer que podemos acessar toda a história de modificação de cada arquivo. Voltar atrás em algo que não gostamos, testar alternativas diferentes e coisas do tipo.

Para começar vamos tentar trabalhar com o repositório do curso mesmo.

<!-- TEASER_END -->

Uma coisa importante: aqui estamos falando de projetos de software pois este é um curso de programação e a ferramenta foi criada para este tipo de aplicação. Mas na verdade, o controle de versão pode ser usado em *qualquer tipo de arquivo e aplicação*. Mas a coisa funciona bem com arquivos texto. Eu uso bastante na elaboração de relatórios em [LaTeX](https://pt.wikipedia.org/wiki/LaTeX). 

## Instalando o Git

Para instalar o Git, baixe o software em <https://git-scm.com/> e instale. O Git é uma ferramenta de linha de comando. Se você está no Linux ou MacOS, isso é fácil. No Windows as coisas são um pouco mais chatas mas a versão do Windows do Git vem com uma ferramente chamada Git Bash que nada mais é que um terminal, bem parecido com o terminal do Linux onde você pode usar o Git sem dificuldades.

Existem algumas interfaces gráficas para o Git. Quem tiver aversão à linha de comando, pode optar por usar alguma destas interfaces. Duas populares são:

 * [TortoiseGit](https://tortoisegit.org/) que é integrado ao gerenciador de arquivos do WIndows.
 * [GitKraken](https://www.gitkraken.com/) que dizem ser muito poderoso e fácil de usar.

A idéia aqui é mostrar como funciona e os elementos básicos do Git. Então para esta breve exposição, a linha de comando pode ser mais adequada (além de ser o que eu uso...).

## Clonando o repositório do curso

O Git trabalha com arquivos. Geralmente isso é feito localmente. Mas hoje é interessante que as coisas estejam na nuvem e existem diversos serviços que permitem hospedar projetos entre eles vale destacar

 * [GitHub](https://github.com)
 * [Bitbucket](https://bitbucket.org)
 * [GitLab](https://gitlab.com)

Com estes serviços você pode armazenar seu projeto na nuvem e colaborar com outras pessoas. Vamos usar aqui o GitHub que é o mais popular.

Vamos começar com um projeto que já existe: o próprio repositório do curso! O primeiro passo é baixar o repositório da nuvem. O termo exato é *clonar*. Talvez alguém já tenha ouvido falar de ferramentas mais antigas como CVS ou Subversion. Estes sistemas são centralizados. O Git é um sistema de controle de versões distribuído e tem várias vantagens (na pior das hipósteses você pode trabalhar maneira semelhante ao CVS ou Subversion). Mas a primeira etapa é clonar o repositório. Você está realmente baixando o repositório *inteiro*. Não se preocupe, isso é mais eficiente do que soa.

```bash
pjabardo@makhno:~$ git clone https://github.com/assipt/pythonassipt
Cloning into 'pythonassipt'...
remote: Enumerating objects: 139, done.
remote: Counting objects: 100% (139/139), done.
remote: Compressing objects: 100% (90/90), done.
remote: Total 139 (delta 46), reused 128 (delta 35), pack-reused 0
Receiving objects: 100% (139/139), 299.01 KiB | 2.45 MiB/s, done.
Resolving deltas: 100% (46/46), done.
pjabardo@makhno:~$ 
```

Agora você pode entrar nesta pasta e ver o que está rolando:
```bash
pjabardo@makhno:~$ cd pythonassipt/
pjabardo@makhno:~/pythonassipt$ ls
01-aula  02-aula  03-aula  04-aula  05-aula  pagina-web  README.md
pjabardo@makhno:~/pythonassipt$ git log
commit 42af482dff5fd33989d834766cd187a435cac374 (HEAD -> main, origin/main, origin/HEAD)
Author: Paulo José Saiz Jabardo <pjabardo@ipt.br>
Date:   Mon Mar 7 20:38:20 2022 -0300

    Aula 05 - funções
    
    Já estou com as notas de aula e a página web

commit 5a352ee1aa0669d41bbf3d77c83797b4a722776f
Author: Paulo Jabardo <pjabardo@gmail.com>
Date:   Fri Mar 4 07:50:40 2022 -0300

    Erro de digitação no título

commit 5f305a2e33b0a428569d2b259d7cf4087d864a9c
Author: Paulo Jabardo <pjabardo@gmail.com>
Date:   Fri Mar 4 07:38:12 2022 -0300

    Tirando o output
    
    para variar...

```

O comando `git log` permite você ver toda a história do repositório. Já o comando `git status` permite ver o estado atual do repositório. Como acabamos de clonar, não existe nada interessante:

```bash
pjabardo@makhno:~/pythonassipt$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
pjabardo@makhno:~/pythonassipt$ 
```

## Trabalhando no repositório


Mas existe algo novo: eu estou trabalhando neste repositório *neste momento* mas em outro lugar. Então posso ir para lá e ver o que está acontecendo:

```bash
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	pagina-web/pythonassipt/posts/git-e-github.md

nothing added to commit but untracked files present (use "git add" to track)
pjabardo@makhno:~/Documents/assipt/pythonassipt$ 
```

Existe um arquivo que não está sendo rastreado. Para rastrear, eu preciso executar (como sugerido acima) o comando `git add`:

```bash
pjabardo@makhno:~/Documents/assipt/pythonassipt$ git add pagina-web/pythonassipt/posts/git-e-github.md 
pjabardo@makhno:~/Documents/assipt/pythonassipt$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   pagina-web/pythonassipt/posts/git-e-github.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   pagina-web/pythonassipt/posts/git-e-github.md

pjabardo@makhno:~/Documents/assipt/pythonassipt$ 

```

Agora preciso gravar esta modificação (a inclusão do arquivo que vai gerar esta página web). Para isso se usa o comando `git commit`:

```bash
pjabardo@makhno:~/Documents/assipt/pythonassipt$ git commit
[main af4addf] Escrevendo sobre o git e github
 1 file changed, 135 insertions(+)
 create mode 100644 pagina-web/pythonassipt/posts/git-e-github.md
```

Isso vai abrir um editor de texto onde você pode descrever as modificações que você fez. Esse é o texto que aparace no comando `git log`:

```bash
commit af4addf5d8dde8c8eee05c680f1fc35f108f599a (HEAD -> main)
Author: Paulo José Saiz Jabardo <pjabardo@ipt.br>
Date:   Fri Mar 11 16:33:56 2022 -0300

    Escrevendo sobre o git e github
```

Aqui temos algumas informações. O monte de letrinhas é um [*hash*](https://pt.wikipedia.org/wiki/Fun%C3%A7%C3%A3o_hash_criptogr%C3%A1fica) que caracteriza as modificações que eu fiz. Também tem o autor e a data das modificações. Finalmente o texto que escrevi no editor que abriu ao executar o comando `git commit`.


É lógico que ainda estou editando este arquivo. Então o `git status` vai mostrar isso:

```bash
jabardo@makhno:~/Documents/assipt/pythonassipt$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   pagina-web/pythonassipt/posts/git-e-github.md

no changes added to commit (use "git add" and/or "git commit -a")
```

Se eu quiser ver a diferença do que eu fiz em relação ao último commit (quando executei o comando `git commit`, basta usar o comando `git diff`:

```bash
pjabardo@makhno:~/Documents/assipt/pythonassipt$ git diff
diff --git a/pagina-web/pythonassipt/posts/git-e-github.md b/pagina-web/pythonassipt/posts/git-e-github.md
index 3f9cbac..8a3354f 100644
--- a/pagina-web/pythonassipt/posts/git-e-github.md
+++ b/pagina-web/pythonassipt/posts/git-e-github.md
@@ -98,6 +98,9 @@ nothing to commit, working tree clean
 pjabardo@makhno:~/pythonassipt$ 
\```
 
+## Trabalhando no repositório
+
+
 Mas existe algo novo: eu estou trabalhando neste repositório *neste momento* mas em outro lugar. Então posso ir para lá e ver o que está acontecendo:
 
\```bash
@@ -133,3 +136,43 @@ pjabardo@makhno:~/Documents/assipt/pythonassipt$
 
\```
 
+Agora preciso gravar esta modificação (a inclusão do arquivo que vai gerar esta página web). Para isso se usa o comando `git commit`:
+
+\```bash
+pjabardo@makhno:~/Documents/assipt/pythonassipt$ git commit
+[main af4addf] Escrevendo sobre o git e github
+ 1 file changed, 135 insertions(+)
+ create mode 100644 pagina-web/pythonassipt/posts/git-e-github.md
+\```
+
+Isso vai abrir um editor de texto onde você pode descrever as modificações que você fez. Esse é o texto que aparace no comando `git log`:
+
+```
+commit af4addf5d8dde8c8eee05c680f1fc35f108f599a (HEAD -> main)
+Author: Paulo José Saiz Jabardo <pjabardo@ipt.br>
+Date:   Fri Mar 11 16:33:56 2022 -0300
+
+    Escrevendo sobre o git e github
+\```
+
+Aqui temos algumas informações. O monte de letrinhas é um [*hash*](https://pt.wikipedia.org/wiki/Fun%C3%A7%C3%A3o_hash_criptogr%C3%A1fica) que caracteriza as modificações que eu fiz. Também tem o autor e a data das modificações. Finalmente o texto que escrevi no editor que abriu ao executar o comando `git commit`.
+
+
+É lógico que ainda estou editando este arquivo. Então o `git status` vai mostrar isso:
+
+\```bash
+jabardo@makhno:~/Documents/assipt/pythonassipt$ git status
+On branch main
+Your branch is ahead of 'origin/main' by 1 commit.
+  (use "git push" to publish your local commits)
+
+Changes not staged for commit:
+  (use "git add <file>..." to update what will be committed)
+  (use "git restore <file>..." to discard changes in working directory)
+       modified:   pagina-web/pythonassipt/posts/git-e-github.md
+
+no changes added to commit (use "git add" and/or "git commit -a")
+\```
+
+Se eu quiser ver a diferença do que eu fiz em relação ao último commit (quando executei o comando `git commit`, basta usar o comando `git diff`:
+
pjabardo@makhno:~/Documents/assipt/pythonassipt$ 

```

Esse diff mostra o que tem de diferença em relação à última versão. Para salvar esta última versão, basta executar o comando `git commit -a`. A opção `-a` já executa o comando `git add`.

Novamente vai abrir um editor onde vou descrever as modificações realizadas.


Se você quiser, você pode enviar estas modificações para a nuvem, neste caso o GitHub, com o comando `git push`:

```bash
pjabardo@makhno:~/Documents/assipt/pythonassipt$ git commit -a
[main 728e3d0] Trabalhando na descrição do git e github.
 1 file changed, 110 insertions(+)
pjabardo@makhno:~/Documents/assipt/pythonassipt$ git push
Enumerating objects: 16, done.
Counting objects: 100% (16/16), done.
Delta compression using up to 4 threads
Compressing objects: 100% (10/10), done.
Writing objects: 100% (12/12), 4.63 KiB | 4.63 MiB/s, done.
Total 12 (delta 5), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (5/5), completed with 2 local objects.
To https://github.com/assipt/pythonassipt
   42af482..728e3d0  main -> main
```

Agora o repositório no github <https://github.com/assipt/pythonassipt> está com as modificações que eu fiz.

## Algumas omissões
É lógico que é necessário ter uma conta no GitHub. Existe ainda a questão da autenticação e outros detalhes. O objetivo aqui é descrever brevemente o Git e o GitHub.

## Como criar um repositório novo

### Criando o repositório no GitHub

O jeito mais fácil é você fazer isso no GitHub. Se você já tem uma conta e está logado, vá para sua conta. No meu caso é <https://github.com/pjabardo/>. Aí, clica no no botão + no canto superior direito (ver a figura a seguir) e clique em *New Repository* e siga as instruções. Você clona este repositório e começa a trabalhar nos arquivos. Adicionando arquivos novos e modificações, realizando os *commits* e depois dando os *push*s da vida.


![screenshot do GitHub](../../images/criando-repositorio.png)


### Criando o repositório localmente

Você também pode criar o repositório localmente usando o Git diretamente. Entre na pasta onde você quer criar o repositório e execute o comando `git init .` onde o ponto se refere à pasta atual onde o terminal está.

```bash
[pjabardo@durruti temp]$ cd meu-repositorio/
[pjabardo@durruti meu-repositorio]$ ls
[pjabardo@durruti meu-repositorio]$ git init .
Initialized empty Git repository in /home/pjabardo/temp/meu-repositorio/.git/
[pjabardo@durruti meu-repositorio]$ ls -la
total 12
drwxr-xr-x 3 pjabardo pjabardo 4096 mar 12 10:01 .
drwxr-xr-x 5 pjabardo pjabardo 4096 mar 12 10:01 ..
drwxr-xr-x 7 pjabardo pjabardo 4096 mar 12 10:01 .git
```

Repare que este comando criou a pasta `.git`. Entre lá e dê uma olhada. Esta pasta é onde está, de fato, o repositório.

Agora você pode trabalhar neste repositório normalmente. Basta usar os comandos que já usamos acima: `git add`, `git status`, `git log`, e `git commit`. Se você quiser armazenar este repositório na nuvem, você precisará criar o repositório no serviço que está usando. *Por isso que eu recomendo criar o repositório diretamente na nuvem e clon´-lo para trabalhar localmente*. Mais simples, menos trabalho e dá menos problemas.


## Colaborando com outras pessoas

### Criando o repositório

Vou criar o repositório <https://github.com/assipt/scripts-python> como mostrei acima.

```bash
[pjabardo@durruti ~]$ git clone https://github.com/assipt/scripts-python
Cloning into 'scripts-python'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (4/4), done.
```

### Adicionando coisas ao repositório

Agora vou adicionar um script que implementei para a próxima aula:

```bash
[pjabardo@durruti ~]$ cd scripts-python/
[pjabardo@durruti scripts-python]$ cp ~/Documents/assipt/pythonassipt/05-aula/
05-funcoes.ipynb  utilidades.py     
[pjabardo@durruti scripts-python]$ cp ~/Documents/assipt/pythonassipt/05-aula/utilidades.py .
[pjabardo@durruti scripts-python]$ git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	utilidades.py

nothing added to commit but untracked files present (use "git add" to track)
[pjabardo@durruti scripts-python]$ git add utilidades.py 
[pjabardo@durruti scripts-python]$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   utilidades.py

[pjabardo@durruti scripts-python]$ git commit 
[main 35521d7] Adicionei o arquivo utilidades.py
 1 file changed, 44 insertions(+)
 create mode 100644 utilidades.py
[pjabardo@durruti scripts-python]$ git push
Username for 'https://github.com': pjabardo
Password for 'https://pjabardo@github.com': 
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 778 bytes | 778.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/assipt/scripts-python
   930260e..35521d7  main -> main
[pjabardo@durruti scripts-python]$ 
```

### Um outro usuário quer modificar

Agora o script está lá no repositório. Um colega nosso, no entusiasmo de aprender python teve uma idéia e acha legal compartilhar essa idéia. Então ele abre uma conta no GitHub e loga na sua conta. Neste momemento ele visita a página do projeto <https://github.com/assipt/scripts-python>. Neste exemplo, o intrépido aluno é o usuário do GitHub `pjsjipt`.

O primeiro passo é fazer um *fork* (basicamente clonar o projeto para a sua conta) aí ele clica no botão *Fork* como indicado na figura abaixo:

![Fork no GitHub](../../images/github-fork-marca.png)

Neste momento o navegodor vai para [*a página de pjsjipt*](https://github.com/pjsjipt/scripts-python).


Aí nosso colega vai clonar o repositório:

```bash
[pjsjipt@durruti temp]$ git clone https://github.com/pjsjipt/scripts-python
Cloning into 'scripts-python'...
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 7 (delta 1), reused 3 (delta 0), pack-reused 0
Receiving objects: 100% (7/7), done.
Resolving deltas: 100% (1/1), done.
[pjsjipt@durruti temp]$ 
```

Agora ele faz as suas modificações que ele verifica com os comandos `git status` (para verificar quais arquivos foram modificados) e `git diff` (para ver as alterações exatas):

```bash
[pjsjipt@durruti scripts-python]$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   utilidades.py

no changes added to commit (use "git add" and/or "git commit -a")
[pjsjipt@durruti scripts-python]$ git diff
diff --git a/utilidades.py b/utilidades.py
index 83cfdf8..e4ce487 100644
--- a/utilidades.py
+++ b/utilidades.py
@@ -41,4 +41,7 @@ def sim_ou_não(msg, ntentativas=3, x="s"):
         
     msg = f"{msg} (s/n): "
     return entrada(msg, converter_sn, xmin=None, xmax=None, x=x)
-    
+
+
+def num_string(x, n=3):
+    return str(x + 10**n)[1:]
[pjsjipt@durruti scripts-python]$ 
```

Agora ele salva as modificações com o comando `git commit -a` e empurra para o *repositório dele* com o comando `git push`:

```bash
[pjsjipt@durruti scripts-python]$ git commit -a
[main 73d5355] Função para escrever números com zeros
 1 file changed, 4 insertions(+), 1 deletion(-)
[pjsjipt@durruti scripts-python]$ ^C
[pjsjipt@durruti scripts-python]$ git push
Username for 'https://github.com': pjsjipt
Password for 'https://pjsjipt@github.com': 
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 365 bytes | 365.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/pjsjipt/scripts-python
   35521d7..73d5355  main -> main
[pjsjipt@durruti scripts-python]$ 
```

Agora ele precisa me avisar (o autor original do repositório) que ele quer me passar sua estimada contribuição. Eu, que não sou bobo (só um pouquinho...) vou querer dar uma olhada. Então o que ele faz é um *pull request*: ele está pedindo que eu puxe as modificações que ele fez do repositório dele para o meu.

Para ele fazer o *pull request*, ele vai na aba `Pull requests` e clica o botão New pull request:


![Pull request no GitHub](../../images/pull-request-editado.png)


Agora abre uma janela mostrando o que foi feito (as diferenças). Para criar o pull request, ele clica no botão verde `Create pull request`. Abre uma janela onde ele pode descrever o que foi feito:


![Open pull request no GitHub](../../images/open-pull-request.png)


Agora ele clica no botão e o pull request foi aberto. Eu vou ser notificado, dependendo das configurações do GitHub pode ser até por email. Na minha conta, na aba Pull requests vai aparecer o número 1 (um pull request). Clicando no no Pull request, eu posso inspecionar o trabalho. Se eu gostar, basta clicar no botão *Merge pull request* que vai trazer estas modificações do repositório. Mas se eu não gostar posso avisá-lo e aí pode rolar uma discussão saudável (ou nem tanto...).

![Open pull request no GitHub](../../images/merge-pull-request.png)


## E agora?

Eu mostrei a essência do trabalho com Git e GitHub. Estas são ferramentas complexas e poderosas. Existem questões que eu não abordei mas são importantes como conflitos.

O que acontece se duas pessoas fazem modificações no mesmo projeto? E no mesmo arquivo? (Acontece...). O Git tem ferramentas para facilitar este tipo de coisa.

Outra área importante são os ramos, em inglês branches: você pode trabalhar em paralelo com alguma nova funcionalidade ou teste.

Para maiores informações, consulte a documentação. O livro Pro Git de Scott Chacon e Ben Straub está disponível na web: <https://git-scm.com/book/en/v2>. Existe até uma tradução parcial para o português: <https://git-scm.com/book/pt-br/v2>.

Existe também um livro publicado em português [Git: um guia prático de Richard E. Silverman](https://novatec.com.br/livros/git-guia-pratico/) e até mesmo um livro sobre o GitHub (que pode estar um pouco ultrapassado): [Introdução ao GitHub de Peter Bell e Brent Beer](https://novatec.com.br/livros/introgithub/).

Não tenho dúvida de que existem outros tutoriais e vídeos em português. Em inglês tem bastante.



