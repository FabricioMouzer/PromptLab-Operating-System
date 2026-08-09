# PromptLab.AI — Mecânico automotivo

- **Data:** 2026-08-09
- **Horário:** 06:00 (America/Sao_Paulo)
- **Profissão:** Mecânico automotivo / consultor técnico de oficina
- **Tema:** Triagem inteligente da ordem de serviço
- **CTA principal:** OFICINA

## Problema resolvido

Clientes frequentemente descrevem sintomas de forma vaga — “barulho”, “carro fraco”, “luz acesa”, “vibração” — e essas informações chegam incompletas à equipe técnica. Isso aumenta retrabalho, perguntas repetidas, risco de esquecer condições importantes de ocorrência e dificuldade para explicar ao cliente o que será inspecionado.

## Benefício esperado

Transformar o relato do cliente e os dados do veículo em uma ordem de serviço estruturada, com perguntas faltantes, sintomas organizados, checklist inicial de inspeção, prioridades e mensagem profissional para o cliente, sem inventar diagnóstico ou substituir a avaliação técnica.

## Prompt completo

```text
Você será meu Assistente Sênior de Triagem para Oficina Automotiva.

Sua missão é transformar o relato do cliente, os dados do veículo e as observações iniciais da oficina em uma ORDEM DE SERVIÇO CLARA, COMPLETA E ACIONÁVEL.

REGRAS IMPORTANTES

- Não invente diagnóstico, causa, peça defeituosa, preço, prazo ou quilometragem.
- Não trate hipótese como diagnóstico confirmado.
- Diferencie claramente: fato informado, sintoma, hipótese de inspeção, risco e dado faltante.
- Não forneça instruções de reparo, torque, desmontagem ou procedimentos que substituam manual técnico e avaliação profissional.
- Quando houver possível risco de segurança, destaque para avaliação técnica prioritária.
- Se houver informação contraditória, sinalize antes de organizar a conclusão.
- Use linguagem objetiva e profissional.

DADOS DO VEÍCULO

Marca/modelo:
[preencher]

Ano:
[preencher]

Motorização:
[preencher]

Quilometragem:
[preencher]

Combustível:
[preencher]

Placa/identificador interno:
[preencher]

Histórico de manutenção conhecido:
[preencher]

RELATO DO CLIENTE

Cole aqui exatamente o que o cliente informou:
[preencher]

QUANDO O SINTOMA ACONTECE?

[partida fria, quente, aceleração, frenagem, curva, marcha lenta, alta velocidade, chuva, subida etc.]

FREQUÊNCIA

[constante, intermitente, primeira ocorrência etc.]

LUZES OU ALERTAS NO PAINEL

[preencher]

SERVIÇOS RECENTES

[preencher]

OBSERVAÇÕES INICIAIS DA OFICINA

[preencher]

Depois de analisar as informações, entregue:

1. RESUMO DA RECLAMAÇÃO

Reescreva o relato do cliente em linguagem técnica simples, preservando exatamente os fatos informados.

2. DADOS FALTANTES

Liste as perguntas que precisam ser feitas ao cliente antes do diagnóstico.

Priorize perguntas que ajudem a identificar:
- quando o sintoma aparece;
- frequência;
- intensidade;
- condição do motor/veículo;
- ruído, vibração, cheiro ou perda de desempenho;
- manutenção recente;
- alertas no painel.

3. ORDEM DE SERVIÇO ESTRUTURADA

Organize em:
- reclamação principal;
- sintomas associados;
- condições de ocorrência;
- histórico relevante;
- observações iniciais;
- itens pendentes de confirmação.

4. CHECKLIST DE INSPEÇÃO INICIAL

Crie um checklist de pontos que a equipe deve VERIFICAR, sem afirmar causa ou defeito.

Separe em:
- inspeção visual;
- leitura de alertas/diagnóstico eletrônico, quando aplicável;
- fluidos e vazamentos aparentes;
- pneus, freios e suspensão, quando relacionados ao relato;
- ruídos e vibrações;
- teste funcional conforme procedimento seguro da oficina.

5. PRIORIDADE DE TRIAGEM

Classifique como:
- normal;
- atenção;
- prioritária por possível segurança.

Explique o motivo usando apenas as informações fornecidas.

6. HIPÓTESES DE INSPEÇÃO

Liste áreas ou sistemas que podem precisar ser VERIFICADOS.

Use sempre a expressão “verificar” e nunca apresente hipótese como diagnóstico confirmado.

7. INFORMAÇÕES PARA O ORÇAMENTO

Liste o que precisa ser confirmado tecnicamente antes de elaborar orçamento.

8. MENSAGEM PARA O CLIENTE

Crie uma mensagem curta e profissional explicando:
- que a reclamação foi registrada;
- quais pontos serão verificados;
- quais informações adicionais ainda são necessárias;
- que diagnóstico, prazo e orçamento serão confirmados após a inspeção.

9. RESUMO PARA O MECÂNICO

Crie um resumo operacional de até 8 linhas contendo somente o essencial para iniciar a triagem.

10. CHECKLIST DE FECHAMENTO DA OS

Antes de finalizar a ordem de serviço, confirme se foram registrados:
- relato do cliente;
- condição de ocorrência;
- quilometragem;
- alertas no painel;
- histórico recente;
- inspeções realizadas;
- diagnóstico confirmado pela equipe;
- serviço autorizado;
- orientação entregue ao cliente.
```

## Modo de usar

Preencha os dados básicos do veículo, cole o relato do cliente sem “traduzir” antes e acrescente as observações da oficina. Use a saída como estrutura de triagem e comunicação. O diagnóstico final, os procedimentos técnicos, a autorização e o orçamento continuam sob responsabilidade da equipe da oficina.

## Reel — HeyGen

**Ferramenta:** HeyGen

**Formato:** 9:16, 35–45 segundos

```text
Crie um Reel vertical 9:16 para a PromptLab.AI.

APRESENTADOR

Profissional de oficina automotiva com postura confiante, ambiente organizado e visual moderno.

CENÁRIO

Oficina limpa, veículo ao fundo, tablet ou prancheta com ordem de serviço.

IDENTIDADE VISUAL

- fundo escuro;
- detalhes verde-limão;
- linguagem objetiva;
- legendas grandes;
- B-roll de atendimento, checklist, inspeção visual e ordem de serviço.

NARRAÇÃO

0–4s

“Mecânico: quantas vezes o cliente chega dizendo só ‘o carro está fazendo um barulho’?”

4–11s

“Se o relato chega incompleto para a oficina, a equipe perde tempo fazendo as mesmas perguntas e a ordem de serviço começa fraca.”

11–20s

“Com um único prompt, a IA organiza o relato do cliente e transforma tudo em uma triagem estruturada.”

20–31s

“Ela gera perguntas faltantes, condições do sintoma, checklist inicial, prioridade e até uma mensagem profissional para o cliente.”

31–39s

“A IA não faz o diagnóstico. Ela organiza a informação para o mecânico diagnosticar melhor.”

39–45s

“Salve este vídeo e use o prompt completo da PromptLab.AI.”

CAPA

MECÂNICO AUTOMOTIVO

TRANSFORME O RELATO DO CLIENTE
EM UMA OS CLARA

COM IA

CTA FINAL

SALVE E USE ESTE PROMPT
```

## Post — capa

**Ferramenta recomendada:** Canva

**Formato:** 1080 × 1350

**Headline:** MECÂNICO AUTOMOTIVO

**Subheadline:** Transforme “o carro está fazendo um barulho” em uma ordem de serviço clara com IA.

**Destaques:** Relato • Perguntas • Checklist • Prioridade

**CTA de capa:** SALVE ESTE POST E USE O PROMPT

## Legenda para Instagram

🔧 **Mecânico: o diagnóstico começa antes de abrir o capô.**

Quando o cliente diz apenas “está fazendo um barulho”, ainda faltam informações importantes: quando acontece, em qual condição, com que frequência, se há luz no painel e o que foi feito recentemente.

O prompt de hoje organiza tudo isso em:

✅ reclamação estruturada
✅ perguntas faltantes
✅ checklist inicial de inspeção
✅ prioridade de triagem
✅ áreas que precisam ser verificadas
✅ mensagem pronta para o cliente
✅ resumo para a equipe técnica

A IA não substitui o diagnóstico do mecânico.

**Ela melhora a qualidade da informação que chega até ele.**

📌 Salve este post.
💬 Comente **OFICINA**.
🚀 Siga a PromptLab.AI.

## Legenda para TikTok

🔧 Mecânico automotivo: transforme um relato vago do cliente em uma ordem de serviço organizada usando um único prompt.

**Menos perguntas repetidas. Mais informação para diagnosticar.**

Salve e comente **OFICINA**.

## Stories

### Story 1 — Enquete

**O CLIENTE JÁ CHEGOU DIZENDO SÓ:**

“Está fazendo um barulho.” 😅

**Enquete:**
- Toda semana
- Direto 😂

### Story 2 — Valor

**UM BOM PROMPT ORGANIZA A TRIAGEM.**

- relato do cliente;
- condição do sintoma;
- perguntas faltantes;
- checklist inicial;
- prioridade;
- mensagem para o cliente.

### Story 3 — Interação

**QUAL RELATO MAIS DIFÍCIL DE INTERPRETAR NA OFICINA?**

Caixa de perguntas:

“Barulho? Vibração? Perda de força? Luz no painel? Outro?”

### Story 4 — CTA

**QUER O PROMPT COMPLETO?**

Responda:

**OFICINA**

e use o comando pronto para copiar.

**Menos retrabalho. Mais organização. Mais profissionalismo no atendimento.**

## Comentário fixado

**PROMPT DO DIA: MECÂNICO AUTOMOTIVO 🔧**

Comente **OFICINA** se você quer o prompt completo para transformar o relato do cliente em uma ordem de serviço mais clara e organizada.

## Hashtags

`#PromptLabAI #Mecanico #MecanicaAutomotiva #OficinaMecanica #OficinaAutomotiva #InteligenciaArtificial #ChatGPT #Produtividade #Prompts #IAnoTrabalho #GestaoDeOficina #AtendimentoAutomotivo`

## Ferramentas

- **Prompt e copy:** ChatGPT — melhor para estruturar raciocínio, linguagem e versões reutilizáveis.
- **Reel:** HeyGen — melhor equilíbrio entre velocidade, apresentador virtual e produção vertical.
- **Feed e Stories:** Canva — melhor para manter template editável, identidade visual consistente e reaproveitamento.
- **Arquivo operacional:** GitHub — base permanente e pesquisável da biblioteca PromptLab.AI.

## Monetização

### Produto sugerido

**Kit IA para Oficinas Automotivas**

Módulos possíveis:
- triagem de atendimento;
- ordem de serviço;
- checklist de recebimento;
- explicação de orçamento;
- mensagens de aprovação;
- follow-up pós-serviço;
- lembrete de manutenção;
- resposta a avaliações;
- conteúdo para redes sociais da oficina.

### Funil

Conteúdo gratuito → comentário **OFICINA** → prompt gratuito → mini-kit para oficinas → Kit IA para Oficinas → assinatura PromptLab.AI.

### Proposta de valor

Não vender “um prompt”, mas **padronização de atendimento, redução de retrabalho, ganho de tempo e comunicação mais profissional com o cliente**.
