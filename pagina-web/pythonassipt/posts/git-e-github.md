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

Uma coisa importante: aqui estamos falando de projetos de software pois este é um curso de programação e a ferramenta foi criada para este tipo de aplicação. Mas na verdade, o controle de versão pode ser usado em *qualquer tipo de arquivo e aplicação*. Mas a coisa funciona bem com arquivos texto. Eu uso bastante na elaboração de relatórios em [LaTeX](https://pt.wikipedia.org/wiki/LaTeX). 

## Instalando o Git

Para instalar o Git, baixe o software em <https://git-scm.com/> e instale. O Git é uma ferramenta de linha de comando. Se você está no Linux ou MacOS, isso é fácil. No Windows as coisas são um pouco mais chatas mas a versão do Windows fo Git vem com uma ferramente chamada Git Bash que nada mais é que um terminal, bem parecido com Linux onde você pode usar o Git sem dificuldades.

Existem algumas interfaces gráficas para o Git. Quem tiver aversão à linha de comando, pode optar por usar alguma destas interfaces. Duas populares são:

 * [TortoiseGit](https://tortoisegit.org/) que é integrado ao gerenciador de arquivos do WIndows.
 * [GitKraken](https://www.gitkraken.com/) que dizem ser muito poderoso e fácil de usar.

A idéia aqui é mostrar como funciona e os elementos básicos do Git. Então para esta breve exposição, a linha de comando pode ser mais adequada (além de ser o que eu uso...).

## Clonando o repositório do curso

O Git trabalha com arquivos. Geralmente isso é feito localmente. Mas hoje é interessante que as coisas estejam na nuvem e existem diversos serviços que permitem hospedar projetos entre eles vale destacar

 * [GitHub](https://github.com)
 * [Bitbucket](https://bitbucket.org)
 * [GitLab](https://gitlab.com)

Com estes serviços você pode armazenar seu projeto na núvem e colaborar com outras pessoas.

Vamos começar com um projeto que já existe: o próprio repositório do curso! O primeiro passo é baixar o repositório da núvem. O termo exato é *clonar*. Talvez alguém já tenha ouvido falar de ferramentas mais antigas como CVS ou SubVersion. Estes sistemas são centralizados. O Git é um sistema de controle de versões distribuído e tem várias vantagens (na pior das hipósteses você pode trabalhar maneira semelhante ao CVS ou SubVersion). Mas a primeira etapa é clonar o repositório. Você está realmente baixando o repositório *inteiro*. Não se preocupe, isso é mais eficiente do que parece.

```shell script
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
```shell script
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

O comando `git log` permite você ver toda a história do repositório. Já o comando
`git status` permite ver o estado atual do repositório. Como acabamos de clonar, não existe nada interessante:

```shell script
pjabardo@makhno:~/pythonassipt$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
pjabardo@makhno:~/pythonassipt$ 
```

## Trabalhando no repositório


Mas existe algo novo: eu estou trabalhando neste repositório *neste momento* mas em outro lugar. Então posso ir para lá e ver o que está acontecendo:

```shell script
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	pagina-web/pythonassipt/posts/git-e-github.md

nothing added to commit but untracked files present (use "git add" to track)
pjabardo@makhno:~/Documents/assipt/pythonassipt$ 
```

Existe um arquivo que não está sendo rastreado. Para rastrear, eu preciso executar (como sugerido acima) o comando `git add`:

```shell script
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

```shell script
pjabardo@makhno:~/Documents/assipt/pythonassipt$ git commit
[main af4addf] Escrevendo sobre o git e github
 1 file changed, 135 insertions(+)
 create mode 100644 pagina-web/pythonassipt/posts/git-e-github.md
```

Isso vai abrir um editor de texto onde você pode descrever as modificações que você fez. Esse é o texto que aparace no comando `git log`:

```
commit af4addf5d8dde8c8eee05c680f1fc35f108f599a (HEAD -> main)
Author: Paulo José Saiz Jabardo <pjabardo@ipt.br>
Date:   Fri Mar 11 16:33:56 2022 -0300

    Escrevendo sobre o git e github
```

Aqui temos algumas informações. O monte de letrinhas é um [*hash*](https://pt.wikipedia.org/wiki/Fun%C3%A7%C3%A3o_hash_criptogr%C3%A1fica) que caracteriza as modificações que eu fiz. Também tem o autor e a data das modificações. Finalmente o texto que escrevi no editor que abriu ao executar o comando `git commit`.


É lógico que ainda estou editando este arquivo. Então o `git status` vai mostrar isso:

```shell script
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

```shell script
pjabardo@makhno:~/Documents/assipt/pythonassipt$ git diff
diff --git a/pagina-web/pythonassipt/posts/git-e-github.md b/pagina-web/pythonassipt/posts/git-e-github.md
index 3f9cbac..8a3354f 100644
--- a/pagina-web/pythonassipt/posts/git-e-github.md
+++ b/pagina-web/pythonassipt/posts/git-e-github.md
@@ -98,6 +98,9 @@ nothing to commit, working tree clean
 pjabardo@makhno:~/pythonassipt$ 
 ```
 
+## Trabalhando no repositório
+
+
 Mas existe algo novo: eu estou trabalhando neste repositório *neste momento* mas em outro lugar. Então posso ir para lá e ver o que está acontecendo:
 
 ```shell script
@@ -133,3 +136,43 @@ pjabardo@makhno:~/Documents/assipt/pythonassipt$
 
 ```
 
+Agora preciso gravar esta modificação (a inclusão do arquivo que vai gerar esta página web). Para isso se usa o comando `git commit`:
+
+```shell script
+pjabardo@makhno:~/Documents/assipt/pythonassipt$ git commit
+[main af4addf] Escrevendo sobre o git e github
+ 1 file changed, 135 insertions(+)
+ create mode 100644 pagina-web/pythonassipt/posts/git-e-github.md
+```
+
+Isso vai abrir um editor de texto onde você pode descrever as modificações que você fez. Esse é o texto que aparace no comando `git log`:
+
+```
+commit af4addf5d8dde8c8eee05c680f1fc35f108f599a (HEAD -> main)
+Author: Paulo José Saiz Jabardo <pjabardo@ipt.br>
+Date:   Fri Mar 11 16:33:56 2022 -0300
+
+    Escrevendo sobre o git e github
+```
+
+Aqui temos algumas informações. O monte de letrinhas é um [*hash*](https://pt.wikipedia.org/wiki/Fun%C3%A7%C3%A3o_hash_criptogr%C3%A1fica) que caracteriza as modificações que eu fiz. Também tem o autor e a data das modificações. Finalmente o texto que escrevi no editor que abriu ao executar o comando `git commit`.
+
+
+É lógico que ainda estou editando este arquivo. Então o `git status` vai mostrar isso:
+
+```shell script
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
+```
+
+Se eu quiser ver a diferença do que eu fiz em relação ao último commit (quando executei o comando `git commit`, basta usar o comando `git diff`:
+
pjabardo@makhno:~/Documents/assipt/pythonassipt$ 

```

Esse diff mostra o que tem de diferença em relação à última versão. Para salvar esta última versão, basta executar o comando `git commit -a`. A opção `-a` já executa o comando `git add`.

Novamente vai abrir um editor onde vou descrever as modificações realizadas.


Se você quiser, você pode enviar estas modificações para a núvem, neste caso o GitHub, com o comando `git push`:

```shell script
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

O jeito mais fácil é você fazer isso no GitHub. Se você já tem uma conta e está logado, vá para sua conta. No meu caso é <https://github.com/pjabardo/>. Aí, clica no no botão + no canto superior direito (ver a figura a seguir) e clique em *New Repository* e siga as instruções. Você clona este repositório e começa a trabalhar nos arquivos. Adicionando arquivos novos e modificações, realizando os *commits* e depois dando os *push*s da vida.


