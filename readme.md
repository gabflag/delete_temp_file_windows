# deleteTempFile.py

# Linguagem utilizada:

  - Python 3.11.2
  - Roda no seu interpretador Python.
  
# Sobre o programa:

Este script permite limpar as pastas temporárias do seu sistema, incluindo a pasta Temp do usuário local logado e a pasta Temp do Windows. Ele exclui arquivos e pastas dentro desses diretórios, liberando espaço em disco.

# Funções:

# main:
    A função main chama as outras duas funções (clean_windows_temp_folder && clean_local_temp_folder).
    Colocado um tempo de espera de 60 segundos para apreciação do usuário dos arquivos excluidos.

# clean_local_temp_folder:
    Obtém o caminho para a pasta Temp do usuário local usando a variável de ambiente LOCALAPPDATA.
    Percorre a estrutura de diretórios dentro da pasta Temp usando os.walk().
    Exclui os arquivos dentro de cada diretório usando os.remove().
    Exclui as subpastas dentro de cada diretório usando shutil.rmtree().
    Conta o número de arquivos e pastas excluídos e exibe uma mensagem para cada arquivo ou pasta excluído.
    Mostra o total de arquivos e pastas excluídos.
    limpar_pasta_windows_temp()
    Esta função limpa a pasta Temp do Windows. Ela realiza ações semelhantes à função limpar_pasta_local_temp(), mas especificamente para a pasta Temp do Windows localizada em C:\Windows\Temp.

# clean_windows_temp_folder:
    Define o caminho da pasta Temp do Windows como C:\Windows\Temp.
    Utiliza o os.walk() para percorrer recursivamente a estrutura de diretórios dentro da pasta Temp do Windows.
    O argumento topdown=False é fornecido para garantir que os arquivos e pastas sejam processados de baixo para cima, permitindo que os arquivos sejam excluídos antes das pastas.
    O loop externo percorre cada diretório dentro da pasta Temp do Windows.
    O loop interno percorre os arquivos dentro de cada diretório.
    Tenta excluir cada arquivo encontrado utilizando os.remove().
    Se ocorrer um PermissionError (erro de permissão), o bloco except é acionado e a exceção é ignorada com o comando pass.
    Tenta excluir cada pasta encontrada utilizando shutil.rmtree().
    Se ocorrer um PermissionError (erro de permissão), o bloco except é acionado e a exceção é ignorada com o comando pass.
    Se ocorrer qualquer outra exceção durante a execução da função, ela é capturada pelo bloco except Exception as e e uma mensagem de erro é impressa.

# Observações:
Alguns arquivos ou pastas dentro das pastas Temp podem estar em uso por outros processos e não podem ser excluídos até que esses processos sejam encerrados. Verifique se nenhum processo crítico está utilizando esses arquivos antes de executar este script.