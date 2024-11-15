
from funcoes import adicionar_tarefa,ver_tarefas, tarefas, atualizar_nome_tarefa,completar_tarefa,deletar_tarefas_completadas

while True:
  print("""
    \nMenu do Gerenciador de Lista de tarefas:
    1. Adicionar tarefa
    2. Ver tarefas
    3. Atualizar Tarefas
    4. Completar Tarefas")
    5. Deletar tarefas completadas
    6. Sair
  """)

  escolha = int(input("Digite a sua escolha: "))

  if escolha == 1:
    print("\n ---------- Adicionar uma Tarefa ----------")
    nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
    adicionar_tarefa(tarefas, nome_tarefa)

  elif escolha == 2:
    print("\n ---------- Lista de Tarefas ----------")
    ver_tarefas(tarefas)
    print("\n --------------------------------------")
  elif escolha == 3:
    
    ver_tarefas(tarefas)
    print("\n ---------- Atualizar uma Tarefa ----------")
    indice_tarefa = int(input("Digite o número da tarefa que deseja atualizar: "))
    novo_nome = input("Digite o novo nome da tarefa: ")
    atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)

  elif escolha ==4:
    ver_tarefas(tarefas)
    print("\n ---------- Completar uma Tarefa ----------")
    indice_tarefa = int(input("Digite o número da tarefa que deseja completar: "))
    completar_tarefa(tarefas, indice_tarefa)

  elif escolha == 5:
    print("\n ---------- Deletar Tarefas completadas ----------")
    deletar_tarefas_completadas(tarefas)
    ver_tarefas(tarefas)

  elif escolha == 6:
    break

print("Programa finalizado")
