import colorama
from colorama import Fore,Style

# Dicionario para receber os contatos;
contatos = {}

def cadastrar():
  nome = str(input('Informe o nome: '))
  telefone = int(input('Informe o telefone: '))
  contatos[nome] = telefone

#pagina para salvar exteno;
  
  agenda = open('doc.text','a')
  dados = f'{nome};{telefone};\n'
  agenda.write(dados)
  agenda.close()
  print('gravado com sucesso')
  
def l():
  if not contatos:
    print('Lista de contatos vazia')

  else:
    for nome, telefone in contatos.items():
  
      print(Fore.BLUE + f'Nome contato {nome}.', Fore.GREEN + f'\nTelefone contato {telefone} \033[m')
      
def delete():
  nome = str(input('Informe o nome: '))
  if nome in contatos:
    del contatos[nome]
    print('Contato Deletado')

  else:
    print('Contato não exite na lista')
    
def buscar():

  nome = str(input('Informe o nome: '))
  if nome in contatos:
    telefone = contatos[nome]
    print(f'{nome}: {telefone}')

  else:
    print('Nome não encontrado')
    
def atualizar():
  nome = str(input('Informe o nome: ')) 
  if nome in contatos:
    telefone = int(input('Informe o telefone: '))
    contatos[nome] = telefone
    print('Contato Atualizado')

  else:
    print(Fore.Red + 'Contato não achado')

while True:
  print("""
  ==========================================================
  [1] Cadastrar Contato
  [2] Listar Contados
  [3] Deletar Contato
  [4] Buscar Contato
  [5] Atualizar Contato
  ===========================================================\n""")

  esco = int(input('Escolha Uma Das Opições: '))

  if esco == 1:
    cadastrar()
    
  elif esco == 2:
    l()
    
  elif esco == 3:
    delete()
    
  elif esco == 4:
    buscar()
    
  elif esco == 5:
    atualizar()
  
  elif esco == 6:
    break
    
  else:
    print('Numero não entendido!!!')
      