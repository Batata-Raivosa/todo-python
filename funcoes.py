def adicionar_tarefa(tarefas,nome_tarefa):
	tarefa ={"tarefa":nome_tarefa,"completada":False}
	tarefas.append(tarefa)
	print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
	
def ver_tarefas(tarefas):
	print("\nLista de tarefas")
	for indice, item in enumerate(tarefas, start=1): #começa a enumerar 1
		status = "✓" if item["completada"] else " "
		print(f"{indice}. [{status}] {item['tarefa']}")
		
def atualizar_nome_tarefa(tarefas, indice_tarefa,novo_nome_tarefa):
	indice_tarefa_ajustado = indice_tarefa-1
	if indice_tarefa_ajustado >=0 and indice_tarefa_ajustado<len(tarefas):
		tarefas[indice_tarefa_ajustado]["tarefa"]=novo_nome_tarefa
		print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
	else:
		print("Índice de tarefa inválido.")

def completar_tarefa(tarefas, indice_tarefa):
	indice_tarefa_ajustado = indice_tarefa-1
	tarefas[indice_tarefa_ajustado]["completada"]=True
	print(f"Tarefa {indice_tarefa} marcada como completada.")

def deletar_tarefas_completadas(tarefas):
  for tarefa in tarefas:
    if tarefa["completada"]:
      tarefas.remove(tarefa)
  print("Tarefas completadas foram deletadas.")
  
tarefas = []