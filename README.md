### Criação de novo repositorio
- …or create a new repository on the command line
- echo "# comandos_linux_basicos" >> README.md
- git init
- git add README.md
- git commit -m "first commit"
- git branch -M main
- git remote add origin https://github.com/ceslima/comandos_linux_basicos.git
- git push -u origin main

### Caso ja exista um repositorio
- …or push an existing repository from the command line
- git remote add origin https://github.com/ceslima/comandos_linux_basicos.git
- git branch -M main
- git push -u origin main

### passo a passo atualização
1 - git add .
2 - git commit -m "comit"
3 - git push -u origin main

### Inicializar a pasta no git
git init

### Fazer a conexao com o diretorio remoto precisa ter a pasta e o direitorio no git hub
git remote add origin https://github.com/seu-usuario/linux.git

### passo a passo para alterar o github pelo terminal 
1 - git add .
2 - git commit -m "adcionando pasta com codigos do tema"
3 - git push

### Adiciona o novo entre na pasta raiz do projeto
git add .

### Salva com uma mensagem clara
git commit -m "adcionando pasta com codigos do tema"

### Envia para o GitHub atualiza o repositorio online
git push

### Criar um arquivo de texto dentro da pasta pelo terminal 
echo . > .\introducao_panda\codigos.py

### Para atualizar a pasta do computador com os arquivos do github
git pull

# Use o comando code para abrir uma nova aba para criar programas
cd /diretorio_do_aquivo/
code nome_do_arquivo.py

