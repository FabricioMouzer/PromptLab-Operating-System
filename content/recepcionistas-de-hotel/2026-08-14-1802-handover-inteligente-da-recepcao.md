# PromptLab.AI — Recepcionista de Hotel

**Data:** 2026-08-14  
**Horário:** 18:02  
**Profissão:** Recepcionista de hotel / Front Desk  
**Tema:** Handover inteligente da recepção  
**Formato do Reel:** SEM AVATAR + VOZ EM OFF  

## Problema resolvido

Informações importantes do turno ficam espalhadas entre sistema de reservas, mensagens, anotações, solicitações de hóspedes, manutenção e comunicação interna. Isso aumenta o risco de esquecer pendências, repetir perguntas e entregar um turno sem contexto suficiente para a próxima equipe.

## Benefício esperado

Transformar as informações do turno em um handover claro, com chegadas, saídas, solicitações, pendências, ocorrências, manutenção, responsáveis conhecidos e próximos passos, preservando dados pessoais e sem alterar reservas automaticamente.

## Prompt principal

```text
Você será meu Assistente Sênior de Organização de Turno para Recepção de Hotel.

Sua missão é transformar as informações que eu fornecer sobre hóspedes, reservas, chegadas, saídas, solicitações, manutenção e pendências em um HANDOVER DE TURNO claro, objetivo e acionável para a equipe seguinte.

REGRAS IMPORTANTES

- Não invente nomes, horários, reservas, valores, números de quarto, políticas, disponibilidade, upgrades, cortesias, prazos ou responsáveis.
- Não altere, confirme, cancele ou modifique reservas automaticamente.
- Não prometa early check-in, late check-out, upgrade, reembolso, desconto, compensação ou qualquer benefício sem autorização explícita.
- Não exponha números completos de documentos, dados de cartão, senhas, códigos, informações médicas ou outros dados sensíveis.
- Quando houver dados sensíveis no texto, substitua por: [DADO SENSÍVEL REMOVIDO].
- Use somente as informações mínimas necessárias para a operação.
- Diferencie claramente:
  FATO CONFIRMADO
  SOLICITAÇÃO DO HÓSPEDE
  PENDÊNCIA
  BLOQUEIO
  INFORMAÇÃO A CONFIRMAR
  PRÓXIMO PASSO
- Quando a situação depender de política do hotel, autorização gerencial ou setor especializado, marque:
  “VALIDAR COM RESPONSÁVEL / POLÍTICA DO HOTEL”.
- Quando houver possível risco à segurança, emergência, saúde, incêndio, acesso indevido ou situação crítica, marque:
  “ACIONAR PROCEDIMENTO INTERNO E RESPONSÁVEL IMEDIATAMENTE”.
- Não faça diagnóstico médico, jurídico ou técnico.
- Não trate reclamação como fato confirmado sem evidência.
- Use linguagem profissional, discreta, objetiva e adequada a um handover operacional.

DADOS DO TURNO

Hotel / unidade:
[preencher]

Data:
[preencher]

Turno:
[manhã, tarde, noite]

Responsável pelo turno:
[preencher]

Chegadas previstas:
[colar informações relevantes]

Saídas previstas:
[colar informações relevantes]

Reservas com alguma pendência conhecida:
[preencher]

Solicitações de hóspedes:
[colar]

Manutenções abertas:
[preencher]

Ocorrências registradas:
[preencher]

Entregas, fornecedores ou serviços esperados:
[preencher]

Mensagens internas importantes:
[colar]

Informações que precisam ser acompanhadas pelo próximo turno:
[preencher]

DEPOIS DE ANALISAR, ENTREGUE:

1. RESUMO EXECUTIVO DO TURNO

Resuma em até 8 pontos:
- situação geral;
- principal pendência;
- chegada que exige atenção operacional;
- saída que exige acompanhamento;
- solicitação relevante;
- manutenção em aberto;
- ocorrência que precisa de continuidade;
- próximo passo mais importante.

2. HANDOVER ESTRUTURADO

Crie uma tabela com:
- categoria;
- situação;
- status;
- responsável, se informado;
- dependência;
- próximo passo.

Use categorias como:
- chegada;
- saída;
- hospedagem em andamento;
- solicitação;
- manutenção;
- ocorrência;
- fornecedor;
- administrativo;
- comunicação interna.

3. CHEGADAS A ACOMPANHAR

Liste somente as chegadas que tenham alguma informação operacional relevante.

Para cada item, informe:
- horário, somente se fornecido;
- observação necessária;
- pendência;
- próximo passo;
- informação que precisa ser confirmada.

4. SAÍDAS A ACOMPANHAR

Liste:
- pendências informadas;
- solicitações registradas;
- itens a confirmar;
- encaminhamento necessário.

Não invente cobrança, consumo, prazo ou condição comercial.

5. SOLICITAÇÕES DE HÓSPEDES

Organize por status:
- recebida;
- encaminhada;
- aguardando retorno;
- concluída;
- precisa confirmar.

Para cada solicitação informe:
- pedido;
- setor responsável, se conhecido;
- status;
- próximo passo.

6. MANUTENÇÃO E BLOQUEIOS

Crie uma tabela com:
- problema relatado;
- local ou unidade, somente se necessário e informado;
- status;
- setor ou fornecedor acionado;
- impacto operacional;
- próximo acompanhamento.

Não diagnostique a causa técnica.

7. OCORRÊNCIAS QUE EXIGEM CONTINUIDADE

Separe:
- fato confirmado;
- relato ainda não verificado;
- ação já realizada;
- pendência;
- quem deve acompanhar.

8. TOP 5 PRIORIDADES DO PRÓXIMO TURNO

Para cada prioridade informe:
- ação;
- motivo;
- dependência;
- responsável conhecido;
- prazo, somente se informado.

9. MENSAGENS INTERNAS

Crie rascunhos curtos para os setores que precisam receber atualização, como:
- governança;
- manutenção;
- reservas;
- segurança;
- alimentos e bebidas;
- gerência.

Não envie automaticamente.

10. RASCUNHO DE RESPOSTA AO HÓSPEDE

Quando houver solicitação pendente, crie uma mensagem curta e profissional contendo:
- confirmação de recebimento;
- resumo do pedido;
- próximo passo conhecido;
- aviso de que qualquer prazo ou condição depende de confirmação, quando aplicável.

11. CHECKLIST DE TROCA DE TURNO

Confirme:
- chegadas revisadas;
- saídas revisadas;
- solicitações pendentes registradas;
- manutenção atualizada;
- ocorrências encaminhadas;
- setores avisados quando necessário;
- informações sensíveis removidas;
- responsáveis e próximos passos registrados;
- itens a confirmar destacados.

12. INFORMAÇÕES QUE AINDA PRECISO CONFIRMAR

Liste tudo que possa mudar prioridade, atendimento, autorização ou próximo passo.
```

## Modo de usar

O recepcionista cola somente as informações operacionais necessárias do turno, removendo dados pessoais desnecessários. A IA organiza o handover; qualquer alteração de reserva, concessão comercial, atendimento crítico ou decisão sujeita a política interna continua sob responsabilidade da equipe e da gestão do hotel.

## Reel — HeyGen

**Formato:** SEM AVATAR + VOZ EM OFF  
**Proporção:** 9:16  
**Duração sugerida:** 40–45 segundos  

```text
Crie um Reel vertical 9:16 para a PromptLab.AI.

IMPORTANTE:

NÃO utilizar avatar.
NÃO utilizar apresentador falando para a câmera.

Usar:
- voz em off natural em português do Brasil;
- B-roll de recepção de hotel;
- balcão de atendimento;
- notebook com tela genérica;
- telefone;
- cartões de tarefa sem dados reais;
- malas e lobby;
- quadro de pendências;
- interface genérica de IA;
- motion graphics;
- legendas dinâmicas.

Nunca mostrar nomes, documentos, cartões, números reais de quarto, códigos de reserva ou dados de hóspedes.

IDENTIDADE VISUAL

- azul-marinho/preto;
- detalhes verde-limão;
- estética tecnológica e premium;
- cortes a cada 1,5–3 segundos;
- legendas grandes embutidas;
- trilha discreta abaixo da narração.

0–3s — GANCHO

B-roll:
Recepção movimentada, telefone tocando e várias anotações aparecendo rapidamente.

VOZ:
“Recepcionista de hotel: seu turno termina e ainda tem informação espalhada em todo lugar?”

TEXTO:
TURNO SEM HANDOVER
=
RETRABALHO

3–10s

B-roll:
Mensagens, checklist, manutenção e chegadas genéricas.

VOZ:
“Chegadas, saídas, pedidos de hóspedes, manutenção e pendências precisam passar para a próxima equipe sem perder contexto.”

10–20s

B-roll:
Informações entrando em uma interface genérica de IA e virando um painel organizado.

VOZ:
“Com um único prompt, a inteligência artificial transforma essas informações em um handover claro e acionável.”

TEXTO:
CHEGADAS
SAÍDAS
PENDÊNCIAS
PRÓXIMOS PASSOS

20–31s

B-roll:
Checklist sendo marcado, setores recebendo tarefas e painel de prioridades.

VOZ:
“Ela organiza solicitações, manutenção, ocorrências, responsáveis conhecidos e as cinco prioridades do próximo turno.”

31–38s

B-roll:
Recepção organizada e profissional conferindo uma lista, sem rosto em destaque.

VOZ:
“A IA não muda reservas nem decide por você. Ela reduz o retrabalho de organizar a passagem de serviço.”

38–45s — CTA

Tela PromptLab.AI.

VOZ:
“Salve este vídeo e comente TURNO para receber o prompt completo.”

TEXTO FINAL:
COMENTE: TURNO

SALVE • TESTE • COMPARTILHE

CAPA DO REEL:

RECEPCIONISTA DE HOTEL

TRANSFORME O FIM DO TURNO
EM UM HANDOVER CLARO

COM IA
```

## Capa do post — Canva

**Formato:** 1080 × 1350

**Headline:** RECEPCIONISTA DE HOTEL

**Título:** TRANSFORME O FIM DO TURNO EM UM HANDOVER CLARO COM IA

**Linha de apoio:** Chegadas • Saídas • Pendências • Próximos passos

**CTA:** SALVE ESTE POST E USE O PROMPT

**Direção visual:** fundo azul-marinho/preto, detalhes verde-limão, recepção de hotel e painel de tarefas genérico; não exibir dados reais de hóspedes.

## Legenda Instagram

🏨 **Recepcionista de hotel: quanto tempo você gasta no fim do turno tentando lembrar tudo que precisa passar para a próxima equipe?**

Chegadas, saídas, pedidos de hóspedes, manutenção, ocorrências e pendências acabam espalhados entre sistema, mensagens e anotações.

O prompt de hoje transforma essas informações em:

✅ resumo executivo do turno  
✅ handover estruturado  
✅ chegadas e saídas a acompanhar  
✅ solicitações pendentes  
✅ manutenção e bloqueios  
✅ Top 5 prioridades  
✅ mensagens internas  
✅ checklist de troca de turno

A IA não altera reservas nem substitui as políticas do hotel.

**Ela organiza a passagem de serviço para reduzir retrabalho e perda de contexto.**

📌 Salve este post.  
💬 Comente **TURNO**.  
🚀 Siga a **PromptLab.AI**.

## Legenda TikTok

🏨 Recepcionista de hotel: transforme **chegadas + saídas + pedidos + pendências** em um handover claro usando um único prompt.

**Menos informação perdida. Mais continuidade entre turnos.**

📌 Salve.  
💬 Comente **TURNO**.

## Stories

### Story 1 — Enquete

**NO FIM DO TURNO, VOCÊ AINDA PRECISA JUNTAR INFORMAÇÕES DE VÁRIOS LUGARES?**

Enquete:
- Sim 😵‍💫
- Já tenho um processo ✅

### Story 2 — Valor

**UM BOM PROMPT VIRA UM HANDOVER OPERACIONAL.**

Chegadas  
Saídas  
Solicitações  
Manutenção  
Pendências  
Próximos passos

### Story 3 — Interação

**O QUE MAIS SE PERDE NA TROCA DE TURNO?**

Caixa de perguntas:

Chegadas? Solicitações? Manutenção? Ocorrências? Recados internos? Outro?

### Story 4 — CTA

**QUER O PROMPT COMPLETO?**

Responda:

# TURNO

**Menos retrabalho.  
Mais continuidade.  
Atendimento mais organizado.**

## Comentário fixado

**PROMPT DO DIA: RECEPCIONISTAS DE HOTEL 🏨**

Comente **TURNO** se você quer o comando completo para transformar informações do turno em um handover claro, com prioridades, pendências e próximos passos.

## Hashtags

`#PromptLabAI #RecepcionistaDeHotel #Hotelaria #Hospitalidade #FrontDesk #AtendimentoAoCliente #InteligenciaArtificial #ChatGPT #Produtividade #Prompts #IAnoTrabalho #GestaoHoteleira`

## Ferramentas escolhidas

- **ChatGPT:** criação do prompt, estrutura operacional e copy.
- **HeyGen:** Reel SEM AVATAR + VOZ EM OFF, com B-roll, motion graphics e legendas.
- **Canva:** capa e Stories, pela velocidade, custo, consistência visual e reaproveitamento de templates.

## Monetização

**Produto sugerido:** Kit IA para Recepção de Hotel e Hospitalidade.

Pode incluir prompts para:
- handover de turno;
- organização de solicitações;
- respostas a hóspedes;
- checklist de chegadas e saídas;
- acompanhamento de manutenção;
- resumo de ocorrências;
- briefing de equipe;
- follow-up de pendências;
- respostas a avaliações;
- comunicação interna.

**Funil sugerido:**

Reel/Post → comentário **TURNO** → prompt gratuito → mini-kit → Kit IA para Hotelaria → assinatura PromptLab.AI.

**Proposta de valor:** menos retrabalho + melhor continuidade entre turnos + comunicação mais clara + maior capacidade operacional.
