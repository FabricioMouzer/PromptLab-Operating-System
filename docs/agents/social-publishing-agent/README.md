# Agente de criação e publicação em redes sociais

**Data:** 2026-08-09  
**Status:** aprovado para protótipo controlado  
**Marcas:** PromptLab.AI e ZeloVita

## Objetivo

Receber uma solicitação escrita ou falada, produzir um pacote completo de conteúdo e publicar ou agendar nas contas autorizadas do Instagram, Facebook e TikTok.

O termo “fazer tudo que eu pedir” significa operar dentro de ferramentas, contas, permissões, políticas e ações previamente autorizadas. Não inclui acesso irrestrito, contorno de proteções ou publicação de conteúdo sensível sem revisão.

## Arquitetura recomendada

```text
Comando de Fabrício
        ↓
Whisper, quando a entrada for áudio
        ↓
n8n — orquestração, agenda, tentativas e registros
        ↓
Dify/LLM — pauta, roteiro, legenda, CTA e adaptação por rede
        ↓
Quality Gate — marca, fatos, risco, direitos e formato
        ↓
Canva/HeyGen ou mídia fornecida
        ↓
Postiz — calendário, upload e publicação
        ↓
APIs oficiais de Instagram, Facebook e TikTok
        ↓
Registro de resultado, URL, métricas e falhas
```

## Responsabilidades

### n8n

- receber comandos e eventos;
- coordenar todas as etapas;
- controlar horários, repetição e tratamento de falhas;
- pedir aprovação quando a regra exigir;
- registrar o status da execução.

### Dify ou agente de IA

- transformar briefing em pauta;
- gerar versões adequadas a cada rede;
- produzir roteiro, legenda, CTA e hashtags;
- devolver dados estruturados conforme o esquema do repositório.

### Postiz

- conectar contas por OAuth;
- guardar o calendário editorial;
- receber as mídias;
- agendar e publicar pelas integrações disponíveis;
- devolver status e identificadores quando a plataforma fornecer.

### Whisper e Crawl4AI

- Whisper: converter comandos e briefings falados em texto;
- Crawl4AI: coletar somente fontes públicas, permitidas e relevantes;
- nenhum deles deve ser usado para burlar autenticação ou restrições das redes sociais.

## Regras por marca

### PromptLab.AI

- foco em IA aplicada ao trabalho real;
- conteúdo prático, copiável e demonstrável;
- registrar prompt, roteiro, mídia, CTA e monetização no GitHub.

### ZeloVita

- foco em bem-estar, autocuidado e comparação responsável;
- não fazer diagnóstico, prescrição ou promessa terapêutica;
- registrar fonte, produto, link de afiliado e aviso aplicável;
- priorizar clareza para o público de 35 a 60 anos.

## Níveis de autonomia

### Nível 1 — rascunho

O agente cria e salva. Fabrício revisa e publica. Usar nos primeiros testes.

### Nível 2 — publicação supervisionada

O agente prepara e agenda. Fabrício aprova antes do horário. Liberar após dez pacotes corretos consecutivos.

### Nível 3 — publicação automática limitada

Liberar apenas conteúdos de baixo risco, formatos previamente aprovados e contas específicas. Exigir pelo menos 30 publicações supervisionadas sem incidente grave, limite diário, logs e botão de pausa.

Conteúdos de saúde, alegações de produto, promoções, crises, política, uso de imagem de terceiros e alterações de preço permanecem sujeitos à aprovação.

## Requisitos das plataformas

### Instagram e Facebook

- contas profissionais/páginas compatíveis;
- aplicativo Meta, OAuth e permissões adequadas;
- revisão do aplicativo quando exigida;
- mídia nos formatos aceitos pela API.

### TikTok

- conta de desenvolvedor, site público com HTTPS e domínio verificável;
- Login Kit e Content Posting API;
- mídia acessível por URL HTTPS autorizada;
- auditoria do cliente para publicação pública direta.

Sem a auditoria do TikTok, publicações por Direct Post podem ficar restritas a visibilidade privada. Portanto, TikTok não deve ser prometido como totalmente automático na primeira versão.

## Quality Gate obrigatório

Antes de publicar, validar:

- marca e canal corretos;
- ortografia e idioma português do Brasil;
- fatos e fontes;
- direitos de imagem, música e texto;
- ausência de dados pessoais e segredos;
- CTA e link corretos;
- proporção, duração e tamanho da mídia;
- ausência de duplicidade;
- conformidade com as políticas da plataforma.

## Tratamento de falhas

- não repetir automaticamente uma publicação sem verificar se ela já foi criada;
- limitar tentativas e aplicar espera progressiva;
- registrar mensagem de erro, plataforma, horário e pacote;
- pausar a fila após falhas repetidas;
- nunca trocar de conta ou marca para “resolver” uma falha.

## Critérios de aceitação do MVP

1. Um comando gera um pacote estruturado para as duas marcas.
2. Fabrício escolhe marca, tema, redes e horário.
3. O pacote inclui texto e mídia ou indica claramente a mídia pendente.
4. O sistema solicita aprovação no nível inicial.
5. Instagram e Facebook recebem um teste não público ou controlado.
6. TikTok é tratado como rascunho até que as aprovações técnicas sejam concluídas.
7. Cada execução deixa um log rastreável.

## Métricas

- tempo entre solicitação e pacote pronto;
- taxa de aprovação sem edição;
- sucesso de publicação por canal;
- falhas e duplicidades;
- custo por conteúdo;
- alcance, cliques, leads, vendas e comissão;
- retorno por marca e formato.

## Próxima implementação

Construir primeiro o fluxo:

```text
Tema → pacote de texto → aprovação → Postiz → Instagram e Facebook → log
```

Adicionar geração de mídia automática e TikTok somente após esse fluxo funcionar de ponta a ponta.

## Fontes oficiais

- [Postiz](https://github.com/gitroomhq/postiz-app)
- [Postiz Agent CLI](https://github.com/gitroomhq/postiz-agent)
- [Postiz Docker Compose](https://github.com/gitroomhq/postiz-docker-compose)
- [Documentação de provedores do Postiz](https://docs.postiz.com/providers/overview)
- [TikTok Content Posting API](https://developers.tiktok.com/products/content-posting-api)
- [Diretrizes do TikTok para publicação](https://developers.tiktok.com/doc/content-sharing-guidelines/)
