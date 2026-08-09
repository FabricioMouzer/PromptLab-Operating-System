# Plano de ativação da automação social

**Planejado em:** 2026-08-09  
**Início da execução:** 2026-08-10  
**Responsável:** Fabrício Mouzer  
**Marcas:** PromptLab.AI e ZeloVita  
**Regra:** somente uma tarefa ativa por vez

## Objetivo

Colocar em funcionamento uma automação capaz de gerar, revisar, agendar e publicar conteúdos da PromptLab.AI e da ZeloVita no Facebook, Instagram e TikTok, com rastreabilidade e controles de segurança.

## Definição de concluído

O projeto será considerado concluído quando:

- n8n estiver ativo e com os workflows importados;
- Dify estiver ativo e gerando pacotes válidos em português;
- Postiz estiver ativo e conectado às contas autorizadas;
- as seis integrações sociais estiverem identificadas;
- credenciais estiverem guardadas somente nas plataformas apropriadas;
- um rascunho da PromptLab for criado com sucesso;
- um rascunho da ZeloVita for criado com sucesso;
- um teste privado do TikTok for validado quando a plataforma permitir;
- uma publicação supervisionada for concluída sem erro;
- logs e procedimento de pausa estiverem testados.

## Estratégia escolhida

Começar em nuvem para validar a operação antes de instalar e manter servidores.

| Serviço | Opção inicial | Motivo | Decisão de custo |
|---|---|---|---|
| n8n | Cloud trial | instalação imediata, HTTPS e menor complexidade | não assinar antes do teste |
| Dify | Sandbox Cloud | gratuito para os primeiros workflows | começar no plano gratuito |
| Postiz | teste gratuito | OAuth e publicação mais simples que self-hosting | criar somente quando as contas estiverem prontas |

### Referência de custos em 2026-08-09

- n8n Starter: 20 euros por mês quando faturado anualmente; teste sem cartão disponível.
- Dify Sandbox: gratuito, com limites adequados para protótipo.
- Postiz: teste de sete dias.
- Postiz Standard: US$ 29/mês e cinco canais; insuficiente para seis contas.
- Postiz Team: US$ 39/mês e dez canais; primeiro plano adequado às duas marcas e três redes.

Nenhuma assinatura paga será aprovada antes de um teste funcional e de uma avaliação de custo-benefício.

## Regras de execução

1. Uma tarefa por vez.
2. Não avançar sem cumprir o critério de saída.
3. Se houver bloqueio de login, permissão ou 2FA, parar e resolver o bloqueio.
4. Não compartilhar senha, token, chave ou código de recuperação no chat ou GitHub.
5. Usar OAuth e métodos oficiais.
6. Manter workflows inativos até os testes em rascunho.
7. TikTok começa privado.
8. Conteúdo ZeloVita com alegação de saúde exige revisão humana.
9. Registrar evidência e status ao final de cada sessão.

## Sequência de execução

### Tarefa 1 — Criar ou acessar o n8n

**Data-alvo:** 2026-08-10  
**Duração prevista:** 30 a 60 minutos  
**Status:** próxima tarefa

Passos:

- acessar o n8n Cloud;
- criar ou recuperar a conta;
- criar o workspace `PromptLab Automations`;
- configurar fuso `America/Sao_Paulo`;
- habilitar autenticação em dois fatores quando disponível;
- importar os dois workflows do GitHub;
- manter ambos inativos;
- confirmar que os nodes aparecem sem erro estrutural.

Critério de saída:

- dashboard acessível;
- dois workflows importados;
- nenhuma credencial real incluída;
- captura da tela final para registro.

Não fazer nesta tarefa:

- ativar webhook de produção;
- inserir credenciais do Postiz;
- publicar conteúdo.

### Tarefa 2 — Criar ou acessar o Dify

**Data-alvo:** 2026-08-11  
**Status:** aguardando Tarefa 1

Passos:

- criar ou acessar Dify Sandbox;
- criar workspace `PromptLab AI`;
- criar um aplicativo do tipo Workflow;
- adicionar as entradas documentadas;
- inserir o prompt do repositório;
- configurar saída `result` como JSON;
- publicar o workflow;
- gerar uma chave do aplicativo;
- armazenar a chave como credencial no n8n;
- executar um teste PromptLab e um teste ZeloVita.

Critério de saída:

- os dois testes retornam JSON válido;
- conteúdo está em português do Brasil;
- marca e canais estão corretos;
- nenhum conteúdo foi publicado.

### Tarefa 3 — Inventário das contas sociais

**Data-alvo:** 2026-08-12  
**Status:** aguardando Tarefa 2

Verificar uma conta por vez:

| Marca | Rede | Estado conhecido | Ação |
|---|---|---|---|
| PromptLab.AI | Instagram | `@promptlabai2026` já identificado | confirmar conta profissional e acesso Meta |
| PromptLab.AI | Facebook | confirmar página correta | localizar ou criar somente se realmente ausente |
| PromptLab.AI | TikTok | não confirmado | localizar conta ou registrar ausência |
| ZeloVita | Facebook | página existente; integração Meta precisava de ajuste no último diagnóstico | confirmar portfólio e permissão |
| ZeloVita | Instagram | não confirmado | localizar conta ou registrar ausência |
| ZeloVita | TikTok | não confirmado | localizar conta ou registrar ausência |

Critério de saída:

- nome, URL/arroba, proprietário e acesso de cada conta registrados;
- contas ausentes claramente identificadas;
- nenhuma conta duplicada criada por engano.

### Tarefa 4 — Corrigir Meta Business e contas ausentes

**Data-alvo:** 2026-08-13  
**Status:** aguardando inventário

Ordem:

1. Facebook PromptLab;
2. Instagram PromptLab;
3. Facebook ZeloVita;
4. Instagram ZeloVita;
5. TikTok PromptLab;
6. TikTok ZeloVita.

Passos:

- confirmar portfólio empresarial;
- confirmar propriedade e permissões de administrador;
- vincular página e Instagram da mesma marca;
- corrigir vínculo anterior do portfólio `MestredosPrompts.ai` se necessário;
- adicionar Facebook ZeloVita ao portfólio correto;
- configurar 2FA oficial.

Se SMS não estiver disponível, usar aplicativo autenticador, dispositivo já reconhecido ou código de recuperação oficial.

Critério de saída:

- quatro contas Meta acessíveis e organizadas por marca;
- duas contas TikTok confirmadas ou uma decisão explícita de criá-las.

### Tarefa 5 — Criar o Postiz e conectar PromptLab

**Data-alvo:** 2026-08-14  
**Status:** aguardando contas prontas

O teste de sete dias começa somente nesta tarefa.

Passos:

- criar ou acessar Postiz;
- criar grupo `PromptLab.AI`;
- conectar Facebook PromptLab;
- testar conexão;
- conectar Instagram PromptLab;
- testar conexão;
- registrar os IDs das integrações em local seguro.

Critério de saída:

- Facebook e Instagram PromptLab aparecem conectados;
- nenhuma publicação realizada;
- IDs das duas integrações identificados.

### Tarefa 6 — Conectar ZeloVita ao Postiz

**Data-alvo:** 2026-08-15  
**Status:** aguardando Tarefa 5

Passos:

- criar grupo `ZeloVita`;
- conectar Facebook ZeloVita;
- testar conexão;
- conectar Instagram ZeloVita;
- testar conexão;
- registrar os IDs das integrações em local seguro.

Critério de saída:

- Facebook e Instagram ZeloVita aparecem conectados;
- IDs das duas integrações identificados;
- grupos não misturam as marcas.

### Tarefa 7 — Conectar os TikToks

**Data-alvo:** 2026-08-16  
**Status:** aguardando Tarefa 6

Ordem:

1. TikTok PromptLab;
2. TikTok ZeloVita.

Passos:

- conectar por OAuth oficial;
- verificar as permissões apresentadas;
- iniciar com `SELF_ONLY`/privado;
- não afirmar que Direct Post público está liberado sem confirmação real;
- registrar os IDs das integrações.

Critério de saída:

- os dois TikToks aparecem conectados ou o bloqueio oficial está documentado;
- nenhum vídeo público foi publicado.

### Tarefa 8 — Configurar credenciais e testar rascunhos

**Data-alvo:** 2026-08-17  
**Status:** aguardando Tarefa 7

Passos:

- criar Header Auth do webhook no n8n;
- selecionar credencial do Dify;
- criar e selecionar credencial do Postiz;
- testar geração PromptLab;
- testar geração ZeloVita;
- enviar mídia de teste ao Postiz;
- criar rascunho PromptLab;
- criar rascunho ZeloVita;
- conferir contas e conteúdo.

Critério de saída:

- os dois rascunhos aparecem no Postiz na marca correta;
- logs do n8n mostram sucesso;
- nenhuma publicação pública ocorreu.

### Tarefa 9 — Primeira publicação supervisionada

**Data-alvo:** 2026-08-18  
**Status:** aguardando rascunhos aprovados

Passos:

- escolher um conteúdo de baixo risco;
- revisar texto, mídia, CTA, marca e horário;
- publicar primeiro no Facebook ou Instagram;
- verificar o post diretamente na rede;
- registrar URL e resultado;
- não publicar automaticamente nas seis contas no primeiro teste.

Critério de saída:

- uma publicação real concluída e verificada;
- nenhum erro de marca, conta ou mídia;
- decisão registrada sobre continuar ou corrigir.

## Quadro de controle

| Nº | Tarefa | Status | Evidência |
|---:|---|---|---|
| 1 | n8n | Próxima | — |
| 2 | Dify | Aguardando | — |
| 3 | Inventário social | Aguardando | — |
| 4 | Meta e contas ausentes | Aguardando | — |
| 5 | Postiz + PromptLab | Aguardando | — |
| 6 | Postiz + ZeloVita | Aguardando | — |
| 7 | TikToks | Aguardando | — |
| 8 | Credenciais e rascunhos | Aguardando | — |
| 9 | Publicação supervisionada | Aguardando | — |

## Primeira ação de amanhã

Abrir o n8n Cloud no computador. Fabrício enviará uma captura da primeira tela e seguirá apenas as orientações da Tarefa 1. Não iniciaremos Dify antes de concluir e registrar o n8n.

## Fontes oficiais

- [n8n Pricing](https://n8n.io/pricing/)
- [Dify Cloud Pricing](https://dify.ai/pricing/dify-cloud)
- [Postiz Pricing](https://postiz.com/pricing)
- [Automação pronta para importar](../../automation/n8n/social-publishing/README.md)
