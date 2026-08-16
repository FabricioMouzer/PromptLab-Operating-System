# PromptLab.AI — Gerente de Restaurante

**Data:** 2026-08-16  
**Horário:** 18:02  
**Profissão:** Gerente de Restaurante / Supervisor de Operação  
**Tema:** Briefing inteligente de turno  
**Formato do Reel:** SEM AVATAR + VOZ EM OFF NATURAL PT-BR

## Problema resolvido

Antes de cada turno, informações importantes ficam espalhadas entre reservas, escala, mensagens da equipe, estoque, manutenção, ocorrências e pedidos especiais. Isso aumenta o risco de atraso, item indisponível, falha de comunicação e atendimento inconsistente.

## Benefício esperado

Transformar as informações do dia em um briefing operacional claro, com prioridades, equipe, reservas, estoque crítico, produção, manutenção, riscos, comunicação interna e handover para o próximo turno.

## Prompt principal

```text
Você será meu Assistente Sênior de Organização de Turno para Restaurante.

Sua missão é transformar as informações que eu fornecer sobre reservas, equipe, estoque, produção, manutenção, atendimento e pendências em um BRIEFING OPERACIONAL DE TURNO claro, priorizado e acionável.

REGRAS IMPORTANTES

- Não invente reservas, horários, quantidade de clientes, escala, estoque, preço, disponibilidade, prazo, responsável ou procedimento interno.
- Diferencie claramente:
  FATO INFORMADO
  PENDÊNCIA
  RISCO
  BLOQUEIO
  INFORMAÇÃO A CONFIRMAR
  PRÓXIMO PASSO
- Não altere escala, reserva, cardápio, preço, compra ou processo sem aprovação humana.
- Não prometa disponibilidade de mesa, prato, ingrediente, compensação ou prazo quando isso não estiver confirmado.
- Quando houver informação relacionada a alergia ou restrição alimentar, não improvise substituições e marque:
  “VALIDAR COM COZINHA / PROCEDIMENTO INTERNO ANTES DE CONFIRMAR AO CLIENTE”.
- Quando houver possível risco de segurança alimentar, incêndio, gás, elétrica, equipamento crítico ou acidente, marque:
  “ACIONAR PROCEDIMENTO INTERNO E RESPONSÁVEL IMEDIATAMENTE”.
- Não faça diagnóstico técnico de equipamentos.
- Preserve dados pessoais de clientes e funcionários.
- Não exponha telefone, documento, pagamento ou informação sensível em comunicados coletivos.
- Priorize continuidade do serviço, segurança, experiência do cliente, disponibilidade real de recursos e clareza de responsabilidade.
- Use linguagem objetiva, profissional e pronta para briefing de equipe.

DADOS DO TURNO

Restaurante / unidade:
[preencher]

Data:
[preencher]

Turno:
[almoço, jantar, outro]

Responsável pelo turno:
[preencher]

Horário de operação:
[preencher]

Equipe escalada:
[preencher]

Ausências / atrasos informados:
[preencher]

Reservas relevantes:
[preencher]

Eventos / grupos / mesas grandes:
[preencher]

Pedidos especiais informados:
[preencher]

Itens de cardápio indisponíveis ou com estoque baixo:
[preencher]

Ingredientes críticos:
[preencher]

Produção / pré-preparo pendente:
[preencher]

Equipamentos com problema:
[preencher]

Manutenção em andamento:
[preencher]

Ocorrências do turno anterior:
[preencher]

Pendências de fornecedores:
[preencher]

Mensagens e observações da equipe:
[cole aqui]

DEPOIS DE ANALISAR, ENTREGUE:

1. RESUMO EXECUTIVO DO TURNO

Resuma em até 8 pontos:
- situação geral;
- principal prioridade;
- maior risco;
- reserva ou grupo que exige atenção;
- principal limitação de estoque;
- pendência de produção;
- manutenção ou equipamento relevante;
- próximo passo mais importante.

2. TOP 7 PRIORIDADES DO TURNO

Para cada prioridade, informe:
- ação;
- motivo;
- responsável, se informado;
- dependência;
- prazo ou horário, somente se informado;
- impacto se não for resolvida.

3. EQUIPE E COBERTURA

Organize em tabela:
- área;
- profissional / função;
- status;
- ausência ou limitação informada;
- necessidade de cobertura;
- responsável por confirmar.

Não redistribua pessoas automaticamente se isso não tiver sido aprovado.

4. RESERVAS E ATENDIMENTOS ESPECIAIS

Liste somente os casos que exigem atenção operacional.

Para cada item, informe:
- horário, somente se informado;
- quantidade de pessoas, somente se informada;
- necessidade especial;
- status;
- dependência;
- próximo passo.

5. ESTOQUE E CARDÁPIO

Separe em:
- disponível;
- estoque baixo;
- indisponível;
- precisa confirmar;
- pode impactar o serviço.

Nunca invente substituições de ingrediente ou prato.

6. PRODUÇÃO E PRÉ-PREPARO

Crie uma lista contendo:
- item;
- status;
- responsável, se informado;
- dependência;
- prioridade;
- observação.

Não invente quantidade ou tempo de preparo.

7. EQUIPAMENTOS E MANUTENÇÃO

Crie uma tabela com:
- equipamento / área;
- problema relatado;
- status;
- impacto operacional;
- setor ou fornecedor acionado, se informado;
- próximo acompanhamento.

Não diagnostique causa técnica.

8. RISCOS E PONTOS DE ATENÇÃO

Liste somente riscos sustentados pelos dados, como:
- falta de equipe;
- item crítico indisponível;
- equipamento essencial fora de operação;
- grupo grande sem alinhamento;
- pedido especial sem confirmação;
- atraso de fornecedor;
- pendência de limpeza ou organização;
- informação de segurança alimentar a validar.

9. BRIEFING DE 5 MINUTOS PARA A EQUIPE

Crie um roteiro curto contendo:
- objetivo do turno;
- reservas importantes;
- itens indisponíveis;
- prioridades;
- equipe e coberturas;
- pontos de atenção;
- comunicação entre salão e cozinha;
- próximo passo crítico.

10. COMUNICAÇÕES INTERNAS

Crie rascunhos curtos, quando necessário, para:
- cozinha;
- salão;
- bar;
- recepção;
- estoque / compras;
- manutenção;
- gerência.

Não envie automaticamente.

11. MENSAGEM PARA CLIENTE — SOMENTE SE NECESSÁRIO

Quando houver reserva ou pedido especial pendente, crie uma mensagem curta contendo:
- confirmação do que foi entendido;
- informação que ainda precisa ser validada;
- próximo passo conhecido;
- sem prometer disponibilidade ou condição não confirmada.

12. CHECKLIST DE ABERTURA DO TURNO

Confirme:
- equipe revisada;
- reservas revisadas;
- grupos especiais alinhados;
- indisponibilidades comunicadas;
- produção pendente identificada;
- equipamentos críticos verificados;
- manutenção acompanhada;
- pontos de segurança encaminhados;
- responsáveis definidos quando possível.

13. CHECKLIST DE ENCERRAMENTO E HANDOVER

Confirme:
- ocorrências registradas;
- pendências transferidas;
- estoque crítico atualizado;
- equipamento com problema registrado;
- reservas futuras relevantes sinalizadas;
- fornecedor pendente registrado;
- próximo responsável informado;
- informações sensíveis removidas.

14. INFORMAÇÕES QUE AINDA PRECISO CONFIRMAR

Liste tudo que possa mudar prioridade, disponibilidade, atendimento ou próximo passo.
```

## Modo de usar

Cole as informações do turno antes da abertura ou no momento da passagem de serviço. Revise a saída com salão, cozinha e responsáveis antes de comunicar qualquer disponibilidade, mudança de escala ou condição ao cliente.

## Reel — HeyGen

**Formato:** 9:16  
**Duração:** 40–45 segundos  
**Formato do Reel:** SEM AVATAR + VOZ EM OFF NATURAL PT-BR

```text
Crie um Reel vertical 9:16 para a PromptLab.AI.

IMPORTANTE:

NÃO utilizar avatar.
NÃO utilizar apresentador falando para a câmera.

Usar:
- voz em off natural em português do Brasil;
- B-roll de restaurante antes da abertura;
- salão sendo preparado;
- cozinha em pré-preparo;
- reservas genéricas;
- checklist;
- quadro de equipe;
- estoque e ingredientes;
- interface genérica de IA organizando informações;
- motion graphics;
- legendas dinâmicas.

Nunca mostrar nomes reais de clientes, números de telefone, pagamentos ou dados internos sensíveis.

IDENTIDADE VISUAL
- azul-marinho/preto;
- detalhes verde-limão;
- estética tecnológica e profissional;
- cortes a cada 1,5–3 segundos;
- legendas grandes embutidas;
- trilha moderna e discreta abaixo da narração.

0–3s — GANCHO

B-roll:
Reservas, escala, mensagens e estoque aparecendo rapidamente na tela.

VOZ:
“Gerente de restaurante: seu turno começa antes mesmo da primeira mesa sentar.”

TEXTO:
RESERVAS + EQUIPE + ESTOQUE + PRODUÇÃO
=
MUITA COISA AO MESMO TEMPO

3–10s

B-roll:
Equipe chegando, cozinha preparando mise en place e salão sendo organizado.

VOZ:
“Quando essas informações ficam espalhadas, o problema aparece no meio do atendimento.”

10–20s

B-roll:
As informações entram em uma interface genérica de IA e viram um painel organizado.

VOZ:
“Com um único prompt, a inteligência artificial transforma tudo isso em um briefing claro para o turno.”

TEXTO:
PRIORIDADES
RESERVAS
ESTOQUE
PENDÊNCIAS

20–31s

B-roll:
Checklist, reservas importantes, item indisponível e manutenção sendo acompanhada.

VOZ:
“Ela organiza equipe, grupos especiais, estoque crítico, produção, manutenção e as prioridades que precisam de atenção.”

31–38s

B-roll:
Briefing rápido da equipe antes da abertura.

VOZ:
“A IA não gerencia o restaurante por você. Ela organiza a informação para sua equipe começar o turno mais alinhada.”

TEXTO:
MENOS IMPROVISO.
MAIS ALINHAMENTO.

38–45s — CTA

Tela PromptLab.AI.

VOZ:
“Salve este vídeo e comente TURNO para receber o prompt completo.”

TEXTO FINAL:
COMENTE: TURNO

SALVE • TESTE • COMPARTILHE

CAPA DO REEL:
GERENTE DE RESTAURANTE

TRANSFORME O INÍCIO DO TURNO
EM UM BRIEFING CLARO

COM IA
```

## Capa do post — Canva

**GERENTE DE RESTAURANTE**

### TRANSFORME O INÍCIO DO TURNO  
### EM UM BRIEFING CLARO  
### COM IA

**Equipe • Reservas • Estoque • Produção • Pendências**

**SALVE ESTE POST E USE O PROMPT**

Direção visual: fundo azul-marinho/preto, detalhes verde-limão, restaurante em preparação, cards de reservas e estoque à esquerda e painel organizado de prioridades à direita.

## Legenda Instagram

🍽️ **Gerente de restaurante: quanto tempo do seu turno é gasto apenas reunindo informação antes de abrir a operação?**

Reservas, equipe, estoque, produção, manutenção e pedidos especiais costumam chegar de vários lugares.

O prompt de hoje transforma tudo isso em:

✅ resumo executivo  
✅ Top 7 prioridades  
✅ equipe e cobertura  
✅ reservas importantes  
✅ estoque crítico  
✅ produção e pré-preparo  
✅ manutenção e riscos  
✅ briefing de 5 minutos para a equipe

A IA não substitui a liderança do gerente.

**Ela organiza a informação para o turno começar com mais alinhamento e menos improviso.**

📌 Salve este post.  
💬 Comente **TURNO**.  
🚀 Siga a **PromptLab.AI**.

## Legenda TikTok

🍽️ Gerente de restaurante: transforme **reservas + equipe + estoque + produção** em um briefing de turno usando um único prompt.

**Menos improviso. Mais alinhamento antes da primeira mesa.**

📌 Salve.  
💬 Comente **TURNO**.

## Stories

### Story 1 — Enquete

**ANTES DE ABRIR O TURNO, VOCÊ PRECISA JUNTAR INFORMAÇÕES DE VÁRIOS LUGARES?**

Enquete:
- Sim 😵‍💫
- Já tenho um processo ✅

### Story 2 — Valor

**UM BOM PROMPT VIRA UM BRIEFING OPERACIONAL.**

Equipe  
Reservas  
Estoque  
Produção  
Manutenção  
Prioridades

### Story 3 — Interação

**O QUE MAIS COMPLICA O INÍCIO DO TURNO?**

Caixa de perguntas:
**Equipe? Reservas? Estoque? Cozinha? Manutenção? Outro?**

### Story 4 — CTA

**QUER O PROMPT COMPLETO?**

Responda:

## TURNO

**Menos improviso.  
Mais alinhamento.  
Mais controle da operação.**

## Comentário fixado

**PROMPT DO DIA: GERENTES DE RESTAURANTE 🍽️**

Comente **TURNO** se você quer o comando completo para transformar equipe, reservas, estoque, produção e pendências em um briefing operacional claro.

## Hashtags

`#PromptLabAI #GerenteDeRestaurante #Restaurante #GestaoDeRestaurante #Hospitalidade #FoodService #Operacao #InteligenciaArtificial #ChatGPT #Produtividade #Prompts #IAnoTrabalho`

## Ferramentas escolhidas

- **ChatGPT:** prompt principal, estrutura e copy.
- **HeyGen:** Reel **SEM AVATAR + VOZ EM OFF NATURAL PT-BR**, com B-roll, motion graphics e legendas.
- **Canva:** capa e Stories pela rapidez, baixo custo e consistência visual.

## Monetização

Produto sugerido: **Kit IA para Restaurantes e Food Service**.

Pode incluir prompts para briefing de turno, handover, organização de reservas, indisponibilidades, checklist de abertura, ocorrências, treinamento, comunicação interna, estoque e resumo operacional.

**Funil recomendado:**

Reel/Post → comentário **TURNO** → prompt gratuito → mini-kit → **Kit IA para Restaurantes** → assinatura PromptLab.AI.

**Proposta de valor:** menos retrabalho de comunicação + melhor alinhamento entre salão e cozinha + operação mais previsível + maior capacidade de padronização.
