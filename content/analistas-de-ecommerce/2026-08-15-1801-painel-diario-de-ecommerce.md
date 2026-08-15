# PromptLab.AI — Analista de E-commerce

- Data: 2026-08-15
- Horário: 18:01
- Tema: Painel diário de operação do e-commerce
- Formato do Reel: COM AVATAR + VOZ NATURAL PT-BR

## Profissão

Analista de e-commerce / gestor de loja virtual / coordenador de operação digital.

## Problema resolvido

Vendas, pedidos, estoque, atendimento, campanhas, devoluções e pendências ficam espalhados entre plataforma da loja, marketplace, planilhas, WhatsApp, e-mail e dashboards. O profissional perde tempo reunindo dados antes de decidir o que precisa de atenção.

## Benefício esperado

Transformar informações brutas da operação em um painel diário com prioridades, gargalos, alertas, ações por responsável, acompanhamento de pedidos, estoque, atendimento e campanhas, sem inventar métricas, metas ou causas.

## Prompt principal

```text
Você será meu Assistente Sênior de Operação para E-commerce.

Sua missão é transformar as informações que eu fornecer sobre vendas, pedidos, estoque, atendimento, campanhas, devoluções e pendências em um PAINEL DIÁRIO DE OPERAÇÃO claro, priorizado e acionável.

REGRAS IMPORTANTES

- Não invente vendas, pedidos, estoque, preços, margens, conversão, CAC, ROAS, prazos, metas, disponibilidade ou causas.
- Diferencie claramente:
  FATO INFORMADO
  ALERTA
  HIPÓTESE DE VERIFICAÇÃO
  PENDÊNCIA
  BLOQUEIO
  INFORMAÇÃO FALTANTE
- Não trate correlação como causa.
- Não altere preço, estoque, campanha, pedido, reembolso, frete ou política automaticamente.
- Quando uma ação depender de regra da plataforma, marketplace, meio de pagamento ou transportadora, marque:
  “VERIFICAR REGRA ATUAL DA PLATAFORMA / FORNECEDOR”.
- Preserve dados pessoais de clientes e nunca exponha endereço, telefone, documento, cartão, senha, token ou informação sensível.
- Não prometa prazo de entrega, reembolso ou solução se isso não estiver confirmado.
- Priorize impacto operacional, experiência do cliente, prevenção de ruptura, rastreabilidade e próximos passos.
- Use linguagem objetiva e pronta para execução.

DADOS DO DIA

Loja / operação:
[preencher]

Data:
[preencher]

Canais de venda:
[site próprio, marketplace, social commerce etc.]

Vendas do período:
[preencher]

Pedidos recebidos:
[preencher]

Pedidos pendentes:
[preencher]

Pedidos com problema:
[preencher]

Produtos com estoque baixo:
[preencher]

Produtos sem estoque:
[preencher]

Devoluções / trocas / cancelamentos:
[preencher]

Chamados de clientes:
[preencher]

Campanhas ativas:
[preencher]

Métricas disponíveis:
[preencher somente o que realmente foi medido]

Problemas com pagamento:
[preencher]

Problemas com frete / transportadora:
[preencher]

Pendências internas:
[preencher]

Mensagens e observações da equipe:
[cole aqui]

DEPOIS DE ANALISAR, ENTREGUE:

1. RESUMO EXECUTIVO

Resuma em até 8 pontos:
- situação geral da operação;
- principal prioridade;
- maior bloqueio;
- pedido ou grupo de pedidos que exige atenção;
- principal risco de estoque;
- principal pendência de atendimento;
- campanha ou canal que precisa de verificação;
- próximo passo mais importante.

2. PAINEL DE PRIORIDADES

Crie uma tabela com:
- item;
- categoria;
- prioridade;
- impacto;
- responsável, se informado;
- dependência;
- próximo passo.

Use as prioridades:
CRÍTICA
ALTA
NORMAL
AGUARDANDO

Se os dados forem insuficientes, escreva:
“PRIORIDADE PRECISA SER CONFIRMADA”.

3. PEDIDOS E FULFILLMENT

Organize em:
- pedidos sem pendência;
- pedidos aguardando ação;
- pedidos com problema;
- pedidos dependentes de pagamento;
- pedidos dependentes de estoque;
- pedidos dependentes de transportadora.

Não invente status.

4. ESTOQUE

Crie uma tabela com:
- produto/SKU, se informado;
- situação;
- estoque informado;
- risco operacional;
- venda/campanha relacionada, se informada;
- ação a avaliar;
- dado que precisa ser confirmado.

Não recomende quantidade de compra sem dados suficientes.

5. ATENDIMENTO AO CLIENTE

Separe os chamados em:
- urgente por impacto informado;
- aguardando resposta interna;
- aguardando transportadora/plataforma;
- resolvido;
- precisa confirmar.

Para cada um informe:
- assunto;
- status;
- próximo passo;
- responsável conhecido.

6. CAMPANHAS E CONVERSÃO

Organize somente as métricas fornecidas.

Para cada campanha ou canal, informe:
- objetivo informado;
- investimento informado;
- resultado medido;
- anomalia observada;
- hipótese de verificação;
- dado faltante.

Não conclua causa sem evidência.

7. DEVOLUÇÕES, TROCAS E CANCELAMENTOS

Crie um resumo contendo:
- quantidade informada;
- motivo informado;
- status;
- dependência;
- ação pendente;
- padrão recorrente somente se houver evidência suficiente.

8. TOP 5 AÇÕES DO DIA

Para cada ação informe:
- ação;
- motivo;
- impacto;
- responsável conhecido;
- dependência;
- prazo, somente se informado.

9. ALERTAS

Liste somente alertas sustentados pelos dados, como:
- risco de ruptura;
- pedido parado;
- falha de pagamento;
- atraso logístico;
- aumento de chamados;
- campanha com dado anômalo;
- integração ou processo com falha.

10. MENSAGENS PARA A EQUIPE

Crie rascunhos curtos para as áreas que precisam agir, como:
- estoque;
- atendimento;
- logística;
- financeiro;
- marketing;
- tecnologia.

Não envie automaticamente.

11. MENSAGEM PARA CLIENTE

Quando houver caso que exija retorno, crie um rascunho curto contendo:
- confirmação de recebimento;
- entendimento do problema;
- próximo passo conhecido;
- informação que ainda precisa ser confirmada;
- sem prometer prazo não informado.

12. CHECKLIST DE FECHAMENTO DO DIA

Confirme:
- pedidos críticos revisados;
- estoque crítico revisado;
- chamados pendentes registrados;
- devoluções/cancelamentos acompanhados;
- campanhas verificadas;
- bloqueios encaminhados;
- responsáveis definidos quando possível;
- informações sensíveis removidas;
- próximos passos registrados.

13. RESUMO PARA HANDOVER

Crie um resumo de até 10 linhas para a próxima pessoa ou turno contendo:
- situação geral;
- prioridades;
- pedidos críticos;
- estoque;
- atendimento;
- campanhas;
- bloqueios;
- próximos passos.

14. INFORMAÇÕES QUE AINDA PRECISO CONFIRMAR

Liste tudo que possa mudar prioridade, diagnóstico operacional ou decisão.
```

## Modo de usar

Cole os dados disponíveis da loja, pedidos, estoque, atendimento, campanhas e pendências. Não é necessário ter todas as métricas: o prompt deve trabalhar somente com o que foi informado e apontar o que falta. Revise a saída antes de alterar preço, pedido, estoque, campanha, reembolso ou política.

## Reel — HeyGen

### Formato: COM AVATAR + VOZ NATURAL PT-BR

```text
Crie um Reel vertical 9:16 para a PromptLab.AI.

FORMATO

COM AVATAR/APRESENTADOR PROFISSIONAL VISÍVEL.
UTILIZAR voz natural em português do Brasil.

APRESENTADOR

Profissional de e-commerce com visual moderno, postura confiante e linguagem objetiva.

CENÁRIO

Escritório digital moderno com notebook, dashboard genérico, cards de pedidos, estoque e atendimento.

B-ROLL

Intercalar com:
- pedidos genéricos;
- estoque baixo;
- mensagens de atendimento sem dados reais;
- painel de campanhas;
- checklist;
- interface genérica de IA organizando informações.

Nunca mostrar dados reais de clientes, pedidos ou lojas.

IDENTIDADE VISUAL

- azul-marinho/preto;
- detalhes verde-limão;
- estética tecnológica;
- legendas grandes embutidas;
- cortes a cada 1,5–3 segundos;
- trilha discreta abaixo da narração.

0–3s — GANCHO

APRESENTADOR:
“E-commerce: você começa o dia abrindo cinco telas só para descobrir onde está o problema?”

TEXTO:
VENDAS + PEDIDOS + ESTOQUE + ATENDIMENTO
=
INFORMAÇÃO ESPALHADA

3–10s

“Pedidos, estoque, devoluções, campanhas e chamados ficam divididos entre plataformas, planilhas e mensagens.”

B-ROLL:
Dashboard, planilha, mensagens e pedidos genéricos.

10–20s

“Com um único prompt, a inteligência artificial transforma esses dados em um painel diário de operação.”

TEXTO:
PRIORIDADES
PEDIDOS
ESTOQUE
ALERTAS

20–31s

“Ela organiza gargalos, aponta o que precisa de atenção, separa responsáveis e cria os próximos passos.”

B-ROLL:
Painel sendo organizado e checklist sendo marcado.

31–38s

APRESENTADOR:
“A IA não muda preço nem pedido por você. Ela organiza a operação para você decidir mais rápido.”

TEXTO:
MENOS CAÇA A DADOS.
MAIS CONTROLE.

38–45s — CTA

APRESENTADOR:
“Salve este vídeo e comente LOJA para receber o prompt completo da PromptLab.AI.”

TEXTO FINAL:
COMENTE: LOJA

SALVE • TESTE • COMPARTILHE

CAPA DO REEL:

ANALISTA DE E-COMMERCE

TRANSFORME DADOS ESPALHADOS
EM UM PAINEL DIÁRIO

COM IA
```

## Capa do post — Canva

Formato: 1080 × 1350.

**ANALISTA DE E-COMMERCE**

**TRANSFORME DADOS ESPALHADOS EM UM PAINEL DIÁRIO COM IA**

Pedidos • Estoque • Atendimento • Campanhas

**SALVE ESTE POST E USE O PROMPT**

Direção visual: fundo azul-marinho/preto, detalhes verde-limão, vários cards desorganizados à esquerda e um dashboard limpo à direita.

## Legenda Instagram

🛒 **Analista de e-commerce: quanto tempo você perde todo dia só reunindo informação antes de agir?**

Pedidos, estoque, atendimento, devoluções e campanhas acabam espalhados entre plataforma, planilha, e-mail e WhatsApp.

O prompt de hoje transforma tudo isso em:

✅ resumo executivo
✅ painel de prioridades
✅ pedidos que exigem ação
✅ riscos de estoque
✅ chamados de clientes
✅ campanhas a verificar
✅ Top 5 ações
✅ handover do dia

A IA não altera preço, pedido ou campanha por você.

**Ela organiza a operação para você identificar mais rápido o que precisa de atenção.**

📌 Salve este post.
💬 Comente **LOJA**.
🚀 Siga a **PromptLab.AI**.

## Legenda TikTok

🛒 E-commerce: transforme **pedidos + estoque + atendimento + campanhas** em um painel diário usando um único prompt.

**Menos tempo procurando dados. Mais clareza para agir.**

📌 Salve.
💬 Comente **LOJA**.

## Stories

### Story 1 — Enquete

**VOCÊ COMEÇA O DIA ABRINDO VÁRIAS TELAS PARA ENTENDER A OPERAÇÃO?**

Enquete:
- Sim 😵‍💫
- Já centralizo ✅

### Story 2 — Valor

**UM BOM PROMPT VIRA UM PAINEL DIÁRIO.**

Pedidos
Estoque
Atendimento
Campanhas
Alertas
Próximos passos

### Story 3 — Interação

**O QUE MAIS CONSOME TEMPO NA SUA OPERAÇÃO?**

Caixa de perguntas:
Pedidos? Estoque? Atendimento? Frete? Campanhas? Outro?

### Story 4 — CTA

**QUER O PROMPT COMPLETO?**

Responda:

**LOJA**

Menos informação espalhada.
Mais controle.
Mais velocidade para decidir.

## Comentário fixado

**PROMPT DO DIA: ANALISTAS DE E-COMMERCE 🛒**

Comente **LOJA** se você quer o comando completo para transformar pedidos, estoque, atendimento e campanhas em um painel diário de operação.

## Hashtags

`#PromptLabAI #Ecommerce #LojaVirtual #GestaoDeEcommerce #Marketplace #OperacaoDigital #InteligenciaArtificial #ChatGPT #Produtividade #Prompts #IAnoTrabalho #VendasOnline`

## Oportunidade de monetização

Produto sugerido: **Kit IA para Operação de E-commerce**.

Pode incluir prompts para painel diário, gestão de pedidos, estoque, atendimento, devoluções, análise de campanhas, handover, checklist de lançamento, relatório semanal e comunicação entre áreas.

Funil recomendado:

**Reel/Post → comentário LOJA → prompt gratuito → mini-kit → Kit IA para E-commerce → assinatura PromptLab.AI.**

Proposta de valor:

**menos tempo consolidando informação + mais rastreabilidade + resposta mais rápida a problemas + capacidade de operar mais canais com método.**

## Ferramentas escolhidas

- ChatGPT: prompt principal, estrutura e copy.
- HeyGen: Reel COM AVATAR + VOZ NATURAL PT-BR.
- Canva: capa e Stories pela rapidez, custo e consistência visual.
