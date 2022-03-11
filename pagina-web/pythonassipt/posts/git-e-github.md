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
