# PromptLab.AI — Síndicos e Administradores de Condomínio

**Data:** 2026-08-10  
**Horário:** 18:00  
**Tema:** Central inteligente de ocorrências do condomínio  
**Reel:** SEM AVATAR + VOZ EM OFF

## Profissão e público-alvo

Síndicos profissionais, síndicos moradores, administradores de condomínio e equipes administrativas condominiais.

## Problema resolvido

Solicitações de moradores, ocorrências, manutenções, fornecedores, pendências e comunicados chegam por WhatsApp, e-mail, portaria e conversas presenciais. Sem uma triagem estruturada, itens urgentes podem se misturar a demandas rotineiras, responsáveis ficam indefinidos e o acompanhamento vira retrabalho.

## Benefício esperado

Transformar informações dispersas em uma fila operacional com prioridade, responsável, dependências, próximos passos, mensagens de retorno, pontos que exigem fornecedor ou profissional habilitado e um resumo executivo para acompanhamento.

## Prompt principal — pronto para copiar e colar

```text
Você será meu Assistente Sênior de Organização Condominial.

Sua missão é transformar relatos de moradores, ocorrências, pedidos de manutenção, informações da portaria, mensagens de fornecedores e pendências administrativas em uma CENTRAL DE OCORRÊNCIAS clara, priorizada e acionável.

REGRAS IMPORTANTES

- Não invente fatos, datas, responsáveis, prazos, custos, causas ou soluções técnicas.
- Não trate reclamação ou relato como fato comprovado quando houver necessidade de verificação.
- Preserve dados pessoais e exponha apenas o mínimo necessário para a gestão da ocorrência.
- Não produza decisão jurídica, laudo técnico, diagnóstico elétrico, estrutural, hidráulico, de incêndio, elevadores ou qualquer orientação que dependa de profissional habilitado.
- Quando houver possível risco à segurança, patrimônio ou funcionamento essencial, marque: “AVALIAR COM PRIORIDADE / ACIONAR PROFISSIONAL HABILITADO”.
- Quando houver possível questão jurídica, de convenção, regimento ou assembleia, marque: “VALIDAR COM ADMINISTRAÇÃO / ASSESSORIA RESPONSÁVEL”.
- Diferencie claramente: RELATO, FATO CONFIRMADO, PENDÊNCIA, BLOQUEIO, RISCO e PRÓXIMO PASSO.
- Nunca exponha dados sensíveis de moradores em comunicados coletivos.
- Use linguagem objetiva, profissional, respeitosa e não acusatória.

DADOS DO CONDOMÍNIO

Condomínio:
[preencher]

Data:
[preencher]

Responsável pela gestão no dia:
[preencher]

Canais de entrada analisados:
[WhatsApp, e-mail, portaria, aplicativo, livro de ocorrências etc.]

OCORRÊNCIAS E SOLICITAÇÕES

Cole abaixo as mensagens, anotações ou relatos recebidos:
[colar]

MANUTENÇÕES EM ANDAMENTO
[preencher]

FORNECEDORES ACIONADOS
[preencher]

PENDÊNCIAS ADMINISTRATIVAS
[preencher]

SERVIÇOS PROGRAMADOS
[preencher]

RESTRIÇÕES OU INFORMAÇÕES IMPORTANTES
[preencher]

DEPOIS DE ANALISAR, ENTREGUE:

1. RESUMO EXECUTIVO

Resuma em até 8 pontos:
- quantidade e tipos de demandas recebidas;
- ocorrência de maior prioridade;
- principal bloqueio;
- manutenção crítica em andamento;
- fornecedor que exige acompanhamento;
- pendência administrativa relevante;
- comunicação que precisa ser enviada;
- próximo passo mais importante.

2. TRIAGEM DAS OCORRÊNCIAS

Crie uma tabela contendo:
- ocorrência;
- origem do relato;
- categoria;
- status;
- prioridade sugerida;
- justificativa da prioridade;
- responsável, se informado;
- dependência;
- próximo passo.

Use as categorias:
- segurança;
- manutenção;
- limpeza;
- convivência;
- acesso/portaria;
- fornecedor;
- administrativo;
- comunicação;
- outro.

3. PRIORIDADE OPERACIONAL

Classifique cada item como:
- IMEDIATA — quando houver informação concreta que indique possível risco relevante ou interrupção essencial;
- ALTA — precisa ser tratada no curto prazo;
- NORMAL — rotina operacional;
- AGUARDANDO — depende de informação, fornecedor ou decisão.

Se os dados forem insuficientes, escreva “PRIORIDADE PRECISA SER CONFIRMADA”.

4. TOP 5 AÇÕES

Para cada ação informe:
- o que fazer;
- por que importa;
- responsável conhecido;
- dependência;
- próximo passo;
- prazo, somente se informado.

5. MANUTENÇÕES E FORNECEDORES

Organize em tabela:
- serviço;
- fornecedor;
- status;
- visita/data, se informada;
- pendência;
- evidência necessária;
- próximo acompanhamento.

6. ITENS QUE EXIGEM PROFISSIONAL HABILITADO

Liste separadamente qualquer situação que possa envolver:
- elétrica;
- estrutura;
- gás;
- incêndio;
- elevador;
- instalação hidráulica relevante;
- segurança patrimonial;
- outra especialidade técnica.

Não dê solução técnica. Apenas registre a necessidade de avaliação adequada.

7. PENDÊNCIAS POR RESPONSÁVEL

Agrupe por:
- síndico/gestão;
- administradora;
- portaria;
- zeladoria/manutenção;
- fornecedor;
- morador;
- conselho;
- profissional habilitado.

Somente associe responsável quando isso estiver informado ou for claramente uma etapa de encaminhamento.

8. MENSAGENS DE RETORNO

Crie rascunhos curtos e respeitosos para os moradores que precisam de atualização.

Cada mensagem deve:
- confirmar o recebimento;
- resumir o entendimento da solicitação;
- informar o próximo passo conhecido;
- não prometer prazo que não tenha sido informado;
- evitar expor dados de terceiros.

9. COMUNICADO COLETIVO — SOMENTE SE NECESSÁRIO

Se houver um fato confirmado que realmente precise ser comunicado a vários moradores, crie um rascunho contendo:
- o que aconteceu ou o que será realizado;
- área afetada;
- período, somente se informado;
- orientação objetiva;
- canal para dúvidas.

Se não houver necessidade de comunicado coletivo, escreva: “NENHUM COMUNICADO COLETIVO NECESSÁRIO COM OS DADOS ATUAIS”.

10. BLOQUEIOS

Liste:
- informação faltante;
- autorização pendente;
- fornecedor pendente;
- orçamento pendente;
- acesso necessário;
- decisão administrativa;
- validação técnica.

11. BRIEFING DE 5 MINUTOS PARA A EQUIPE

Crie um roteiro com:
- prioridades do turno;
- ocorrências críticas;
- serviços programados;
- fornecedores esperados;
- pontos de atenção;
- responsáveis conhecidos;
- pendências que precisam de retorno.

12. CHECKLIST DE ENCERRAMENTO DO DIA

Confirme:
□ ocorrências registradas;
□ prioridades revisadas;
□ responsáveis identificados;
□ moradores atualizados quando necessário;
□ fornecedores acompanhados;
□ pendências transferidas para o próximo período;
□ riscos encaminhados ao profissional adequado;
□ informações sensíveis preservadas.

13. INFORMAÇÕES QUE AINDA PRECISO CONFIRMAR

Liste todos os dados ausentes que possam mudar prioridade, responsável ou próximo passo.
```

## Modo de usar

No início ou fim do turno, cole as mensagens relevantes recebidas no WhatsApp, e-mail, portaria ou aplicativo do condomínio. Acrescente manutenções, fornecedores e pendências já conhecidas. O prompt transforma tudo em uma fila operacional para revisão humana. Antes de agir, confirme fatos, responsáveis, prazos, regras internas e qualquer necessidade de profissional habilitado.

## Reel — HeyGen

**Formato:** 9:16  
**Duração:** 40–45 segundos  
**Estilo:** SEM AVATAR + VOZ EM OFF natural em português do Brasil

```text
Crie um Reel vertical 9:16 para a PromptLab.AI.

IMPORTANTE:
- NÃO utilizar avatar.
- NÃO utilizar apresentador falando para a câmera.
- Utilizar voz em off natural em português brasileiro.
- Utilizar B-roll de condomínio, portaria, áreas comuns, smartphone com mensagens genéricas, checklist, painel de tarefas, manutenção e fornecedor chegando.
- Nunca mostrar nomes, apartamentos, rostos identificáveis ou dados reais de moradores.
- Inserir motion graphics discretos, legendas dinâmicas e identidade visual PromptLab.AI.

IDENTIDADE VISUAL
- fundo escuro / azul-marinho;
- detalhes verde-limão;
- visual tecnológico, profissional e limpo;
- legendas grandes;
- cortes a cada 1,5–3 segundos;
- trilha discreta abaixo da narração.

0–3s — GANCHO

B-roll: várias notificações surgindo rapidamente sobre uma tela genérica de celular.

VOZ:
“Síndico: quantas solicitações chegam em lugares diferentes todos os dias?”

TEXTO NA TELA:
WHATSAPP + PORTARIA + E-MAIL + FORNECEDORES

3–10s

B-roll: livro de ocorrências, tela de mensagens, elevador, corredor e manutenção.

VOZ:
“Manutenção, barulho, acesso, fornecedor, limpeza e pendências acabam misturados no mesmo fluxo.”

10–19s

B-roll: informações entrando em uma interface genérica de IA e virando uma lista organizada.

VOZ:
“Com um único prompt, a inteligência artificial transforma esses relatos em uma central de ocorrências priorizada.”

TEXTO NA TELA:
PRIORIDADE • RESPONSÁVEL • STATUS • PRÓXIMO PASSO

19–31s

B-roll: checklist sendo marcado, fornecedor em área técnica, tela com cards de tarefas.

VOZ:
“Ela separa urgências, manutenções, fornecedores, bloqueios, mensagens de retorno e o que precisa de profissional habilitado.”

31–38s

B-roll: gestor acompanhando painel em notebook, sem rosto em destaque.

VOZ:
“A IA não substitui o síndico nem o especialista técnico. Ela organiza a informação para a gestão agir com mais clareza.”

38–45s — CTA

Tela final com identidade PromptLab.AI.

VOZ:
“Salve este vídeo e comente CONDOMÍNIO para receber o prompt completo.”

TEXTO FINAL:
COMENTE: CONDOMÍNIO
SALVE • TESTE • COMPARTILHE

CAPA DO REEL:
SÍNDICO
ORGANIZE AS OCORRÊNCIAS
COM IA

Solicitações • Prioridades • Fornecedores • Retornos
```

## Capa do post — Canva

**Formato:** 1080 × 1350  
**Headline:** SÍNDICO / ADMINISTRADOR DE CONDOMÍNIO  
**Título:** ORGANIZE AS OCORRÊNCIAS COM IA  
**Linha de apoio:** Solicitações • Prioridades • Fornecedores • Retornos  
**CTA:** SALVE ESTE POST E USE O PROMPT

Direção visual: fundo azul-marinho/preto, detalhe verde-limão, smartphone com notificações genéricas à esquerda e painel de ocorrências organizado à direita. Não usar dados pessoais ou números reais de apartamentos.

## Legenda Instagram

🏢 **Síndico: o problema não é receber solicitações. É conseguir acompanhar todas sem perder o controle.**

WhatsApp, portaria, e-mail, fornecedores, manutenção e conversas presenciais acabam criando várias filas ao mesmo tempo.

O prompt de hoje transforma essas informações em:

✅ triagem das ocorrências  
✅ prioridade operacional  
✅ Top 5 ações  
✅ acompanhamento de fornecedores  
✅ pendências por responsável  
✅ mensagens de retorno  
✅ bloqueios  
✅ briefing da equipe

A IA não substitui decisões da gestão nem profissionais habilitados.

**Ela organiza a informação para você acompanhar melhor o condomínio e reduzir retrabalho.**

📌 Salve este post.  
💬 Comente **CONDOMÍNIO**.  
🚀 Siga a **PromptLab.AI**.

## TikTok

🏢 Síndico: transforme **WhatsApp + portaria + fornecedores + pendências** em uma central de ocorrências usando um único prompt.

**Menos informação perdida. Mais controle da gestão.**

📌 Salve.  
💬 Comente **CONDOMÍNIO**.

## Stories

### Story 1 — Enquete

**AS SOLICITAÇÕES DO CONDOMÍNIO CHEGAM POR QUANTOS LUGARES DIFERENTES?**

Enquete:
- “Muitos 😵‍💫”
- “Já centralizamos ✅”

### Story 2 — Valor

**UM BOM PROMPT VIRA UMA CENTRAL DE OCORRÊNCIAS.**

- prioridade;
- responsável;
- status;
- fornecedor;
- próximo passo;
- retorno ao morador.

### Story 3 — Interação

**O QUE MAIS TOMA TEMPO NA GESTÃO DO CONDOMÍNIO?**

Caixa de perguntas:
“Manutenção? Moradores? Fornecedores? Portaria? Cobranças? Outro?”

### Story 4 — CTA

**QUER O PROMPT COMPLETO?**

Responda:

**CONDOMÍNIO**

Menos informação perdida.  
Mais organização.  
Mais previsibilidade na gestão.

## Comentário fixado

**PROMPT DO DIA: SÍNDICOS E ADMINISTRADORES DE CONDOMÍNIO 🏢**

Comente **CONDOMÍNIO** se você quer o comando completo para organizar solicitações, manutenções, fornecedores e retornos.

## Hashtags

`#PromptLabAI #Sindico #SindicoProfissional #Condominio #AdministracaoCondominial #GestaoCondominial #InteligenciaArtificial #ChatGPT #Produtividade #Prompts #IAnoTrabalho #Gestao`

## CTAs

**CTA principal:** Comente **CONDOMÍNIO**.  
**CTA secundário:** Salve para testar no próximo turno de gestão.  
**CTA de crescimento:** Siga a PromptLab.AI para receber novos prompts profissionais.

## Ferramentas

- **ChatGPT:** criação do prompt, estrutura operacional e copy.
- **HeyGen:** Reel SEM AVATAR + VOZ EM OFF, com B-roll e motion graphics.
- **Canva:** capa do Feed e Stories, por velocidade, custo, consistência visual e facilidade de reaproveitamento.

## Monetização

Produto sugerido: **Kit IA para Síndicos e Administradores de Condomínio**.

Possíveis módulos:
- central de ocorrências;
- acompanhamento de fornecedores;
- organização de manutenção preventiva;
- preparação de pauta de reunião;
- resumo de atas e pendências;
- comunicados aos moradores;
- follow-up de serviços;
- handover entre turnos/equipe;
- calendário operacional.

Funil recomendado:

**Conteúdo gratuito → comentário CONDOMÍNIO → prompt gratuito → mini-kit → Kit IA para Gestão Condominial → assinatura PromptLab.AI.**

Posicionamento comercial: **menos retrabalho administrativo, mais rastreabilidade, melhor comunicação e maior capacidade de acompanhamento da operação.**
