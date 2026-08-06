# PromptLab.AI — Gestor de Projetos

**Data:** 06/08/2026 18:01 (BRT)  
**Profissão:** Gestor de Projetos  
**Tema:** Transformar atualizações soltas em status report e plano de ação com IA  
**Problema resolvido:** consolidar mensagens, tarefas, riscos, bloqueios e prioridades sem perder tempo montando relatórios manualmente.  
**Benefício esperado:** mais clareza operacional, menos tempo em consolidação, decisões mais rápidas e comunicação mais profissional com equipe e liderança.

## Ferramentas escolhidas

- **Reel:** HeyGen — escolhido para produzir rapidamente um vídeo vertical com apresentador, voz natural em português e legendas sincronizadas.
- **Feed:** geração gráfica direta em PNG — escolhida nesta execução para garantir tipografia exata, legibilidade e evitar erros de texto comuns em geração visual por IA. O layout pode ser replicado/editado no Canva.
- **Stories:** geração gráfica direta em PNG — escolhida pelo mesmo motivo, preservando formato 1080x1920, margens de segurança e CTAs claros.

## Prompt completo — pronto para copiar e colar

```text
Você será meu PMO Sênior e Assistente de Gestão de Projetos, especializado em priorização, acompanhamento de execução, comunicação com stakeholders, riscos, dependências e organização de planos de ação.

Sua missão é transformar atualizações brutas de projeto em um status claro, objetivo e acionável, sem inventar informações.

REGRAS IMPORTANTES

- Não invente datas, responsáveis, percentuais, custos, prazos ou decisões.
- Quando um dado importante não tiver sido informado, marque como “não informado”.
- Se houver informações contraditórias, destaque a contradição antes de concluir.
- Priorize usando impacto, urgência, dependências e risco de atraso.
- Separe fatos, riscos, decisões pendentes e recomendações.
- Evite jargão desnecessário. Escreva de forma executiva e prática.
- Se um item não puder ser classificado com segurança, explique o motivo.

DADOS DO PROJETO

Nome do projeto:
[preencher]

Objetivo principal:
[preencher]

Prazo final:
[preencher]

Principais marcos:
[preencher]

Equipe e responsáveis conhecidos:
[preencher]

Atualizações brutas da equipe:
[cole aqui mensagens de WhatsApp, Slack, e-mails, anotações ou atas]

Tarefas em aberto:
[preencher]

Bloqueios conhecidos:
[preencher]

Dependências:
[preencher]

Riscos já identificados:
[preencher]

Decisões pendentes:
[preencher]

Público do status:
[equipe, liderança, cliente, diretoria ou outro]

Depois de analisar os dados, entregue exatamente nesta estrutura:

1. RESUMO EXECUTIVO

Faça um resumo de até 5 pontos contendo:
- situação geral do projeto;
- avanço mais importante;
- principal risco;
- principal bloqueio;
- decisão ou ação mais urgente.

2. SAÚDE DO PROJETO

Avalie, somente com base nas informações fornecidas:
- escopo;
- prazo;
- custo;
- qualidade;
- recursos/equipe.

Use os status:
- Verde = sob controle;
- Amarelo = atenção;
- Vermelho = crítico;
- Não informado = dados insuficientes.

Explique cada classificação em uma frase.

3. TOP 5 PRIORIDADES

Liste as cinco ações mais importantes em ordem de execução.

Para cada uma, informe:
- ação;
- motivo da prioridade;
- responsável, se conhecido;
- prazo, se informado;
- dependência relevante.

4. BLOQUEIOS E RISCOS

Monte uma tabela com:
- item;
- tipo: risco ou bloqueio;
- impacto;
- urgência;
- responsável, se conhecido;
- próximo passo recomendado;
- prazo, se informado.

5. DEPENDÊNCIAS CRÍTICAS

Liste quais atividades dependem de outras pessoas, aprovações, fornecedores, informações ou entregas.

Mostre:
- dependência;
- quem ou o que está aguardando;
- impacto se atrasar;
- ação recomendada.

6. PLANO DAS PRÓXIMAS 24–48 HORAS

Crie um plano objetivo dividido em:
- fazer agora;
- acompanhar;
- cobrar;
- decidir;
- comunicar.

7. DECISÕES NECESSÁRIAS

Liste somente decisões que realmente precisam ser tomadas.

Para cada decisão, explique:
- o que precisa ser decidido;
- impacto da demora;
- opções existentes, se houver informação suficiente.

8. STATUS PARA LIDERANÇA

Crie uma versão executiva de até 180 palavras pronta para enviar por e-mail, WhatsApp ou Slack.

Tom:
- profissional;
- direto;
- sem excesso de detalhes;
- foco em progresso, riscos, decisões e próximos passos.

9. MENSAGEM PARA A EQUIPE

Crie uma mensagem curta e humana contendo:
- principal prioridade;
- próximos passos;
- bloqueios que precisam de ajuda;
- fechamento motivador sem exageros.

10. AGENDA DE REUNIÃO DE 15 MINUTOS

Monte uma agenda com:
- 2 minutos: contexto;
- 5 minutos: prioridades;
- 4 minutos: bloqueios e riscos;
- 3 minutos: decisões;
- 1 minuto: responsáveis e próximos passos.

11. INFORMAÇÕES FALTANTES

Finalize com uma lista das informações que faltam para tornar a análise mais confiável.
```

## Modo de usar

1. Copie o prompt completo.
2. Cole no ChatGPT.
3. Preencha os campos básicos do projeto.
4. Cole as atualizações brutas da equipe sem precisar organizá-las antes.
5. Revise responsáveis, datas e decisões antes de distribuir o relatório.
6. Repita diariamente ou antes das reuniões de status.

## Reel — prompt completo para HeyGen

```text
Crie um vídeo vertical 9:16, com duração entre 35 e 45 segundos, em português do Brasil, para a PromptLab.AI.

OBJETIVO
Mostrar a gestores de projetos como usar IA para transformar atualizações soltas da equipe em um status report e plano de ação.

APRESENTADOR
Use um apresentador profissional, confiante e natural, com aparência de gestor de projetos ou PMO.

CENÁRIO
Escritório moderno com notebook e dashboard de projeto ao fundo. Inserir imagens de apoio com quadro Kanban, tarefas, alertas de risco e resumo executivo.

ESTILO
Moderno, corporativo e dinâmico. Paleta escura com detalhes verde-limão, alinhada à identidade visual da PromptLab.AI.

VOZ
Português do Brasil, natural e humana. Evitar ritmo robótico.

LEGENDAS
Adicionar legendas grandes e sincronizadas. Destacar em verde-limão as palavras:
“GESTOR DE PROJETOS”
“PRIORIDADES”
“RISCOS”
“PLANO DE AÇÃO”
“IA”

ROTEIRO

0–4s
“Gestor de projetos, quanto tempo você perde juntando atualizações da equipe?”

4–10s
“Mensagens, tarefas, prazos, bloqueios e riscos acabam espalhados em vários lugares.”

10–18s
“Com um bom prompt, a IA pode organizar tudo e mostrar o que realmente precisa da sua atenção.”

18–28s
“Ela gera resumo executivo, prioridades, riscos, dependências, plano das próximas 48 horas e até a mensagem para a equipe.”

28–36s
“Você continua tomando as decisões. A IA elimina o trabalho repetitivo de consolidar informação.”

36–43s
“O prompt completo está na descrição. Salve este vídeo e siga a PromptLab.AI.”

CAPA DO REEL
GESTOR DE PROJETOS
Transforme updates em PLANO DE AÇÃO com IA

TELA FINAL
PROMPTLAB.AI
IA aplicada ao trabalho real.
CTA: “Salve e use o prompt”
```

## Post para Feed

### Texto da capa

**GESTOR DE PROJETOS**  
**Transforme atualizações soltas em um PLANO DE AÇÃO com IA**

Destaques:
- Prioridades claras
- Riscos visíveis
- Status em minutos

CTA: **SALVE ESTE POST E USE O PROMPT**

### Legenda para Instagram

📊 **Gestor de projetos: pare de gastar tempo montando status report na mão.**

Mensagens da equipe, tarefas, prazos, riscos e decisões costumam chegar espalhados. O problema não é falta de informação — é transformar tudo em uma visão clara do que precisa acontecer agora.

O prompt de hoje organiza essas atualizações e entrega:

✅ resumo executivo;  
✅ Top 5 prioridades;  
✅ bloqueios e riscos;  
✅ dependências críticas;  
✅ plano das próximas 24–48h;  
✅ mensagem para a equipe;  
✅ agenda de reunião de 15 minutos.

A IA não substitui a decisão do gestor. Ela reduz o trabalho repetitivo para que você tenha mais tempo para **decidir, alinhar e executar**.

📌 Salve este post.  
💬 Comente **GESTOR** para receber mais prompts profissionais.  
🚀 Siga a **PromptLab.AI** para aprender a aplicar IA no trabalho real.

### Legenda para TikTok

Gestor de projetos: transforme updates espalhados em prioridades, riscos e plano de ação com um único prompt. 📊⚡

A IA organiza. Você decide.

Salve o vídeo e comente **GESTOR** para mais prompts práticos.

## Stories

### Story 1 — Enquete

**Você ainda monta STATUS REPORT manualmente?**

Texto de apoio: “Copiando mensagens, cobrando updates e tentando descobrir o que realmente é prioridade?”

Enquete:
- Sim, ainda faço tudo na mão 😓
- Já automatizo uma parte ⚡

### Story 2 — Valor

**Um bom prompt pode organizar o projeto em segundos.**

Entregas:
1. Resumo executivo
2. Top 5 prioridades
3. Bloqueios e riscos
4. Próximas 24–48h
5. Mensagem para a equipe
6. Agenda de reunião

### Story 3 — Interação

**O que mais trava seus projetos?**

Caixa de perguntas:
“Prioridade, prazo, equipe, aprovação, cliente ou dependências?”

Complemento:
“O prompt de hoje ajuda a separar risco, bloqueio, prioridade e status.”

### Story 4 — CTA

**Quer o prompt COMPLETO para gestão de projetos?**

CTA principal:
**Responda GESTOR**

e receba o comando pronto para copiar.

## Hashtags

#PromptLabAI #GestaoDeProjetos #ProjectManagement #PMO #InteligenciaArtificial #ChatGPT #Produtividade #GestorDeProjetos #Automacao #Prompts #IAnoTrabalho

## Comentário fixado

📌 **PROMPT DO DIA:** Gestor de Projetos.  
Se você quer mais comandos prontos para a sua profissão, escreva **GESTOR** nos comentários. O objetivo aqui é simples: menos tarefa repetitiva e mais tempo para decidir e executar. ⚡

## Oportunidade de monetização

Transformar este conteúdo em porta de entrada para um **Kit IA para Gestão de Projetos**, contendo:
- prompt de status report;
- prompt de ata de reunião;
- prompt de análise de riscos;
- prompt de priorização;
- prompt de comunicação com stakeholders;
- prompt de plano semanal;
- modelos para WhatsApp, Slack e e-mail.

Funil recomendado: conteúdo gratuito → palavra-chave “GESTOR” → entrega do prompt de entrada → oferta do kit profissional → assinatura recorrente da biblioteca de prompts por profissão.

## Ativos visuais gerados nesta execução

Arquivos preparados em PNG:
- `feed_gestor_de_projetos.png` — 1080x1350
- `story_01_gestor_de_projetos.png` — 1080x1920
- `story_02_gestor_de_projetos.png` — 1080x1920
- `story_03_gestor_de_projetos.png` — 1080x1920
- `story_04_gestor_de_projetos.png` — 1080x1920
- `capa_reel_gestor_de_projetos.png` — 1080x1920

## Observações para futuras campanhas

- Testar variações de gancho focadas em “menos reunião” versus “status em minutos”.
- Medir comentários com a palavra-chave GESTOR.
- Avaliar salvamentos do post como principal indicador de utilidade.
- Transformar dúvidas recebidas nos Stories em novos prompts específicos para gestão de projetos.
