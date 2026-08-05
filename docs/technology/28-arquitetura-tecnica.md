# Arquitetura técnica inicial

**Status:** Proposta aprovada para MVP  
**Data:** 2026-08-05

## Visão geral

```text
WhatsApp Business Platform
        ↓
Webhook de entrada
        ↓
Orquestrador (n8n ou Make)
        ↓
Validação e normalização
        ↓
Classificador de intenção
        ↓
Agente Comercial PromptLab
        ↓
Knowledge Engine + CRM + memória
        ↓
Guardrails e decisão de handoff
        ↓
Resposta pelo WhatsApp
```

## Componentes

### WhatsApp Business Platform

Canal oficial para recebimento e envio de mensagens, templates e mídia.

### Orquestrador

Responsável por webhooks, regras, integrações, filas, tratamento de erros e observabilidade.

### Modelo de IA

Responsável por classificação, compreensão da necessidade, geração de resposta e recomendação de próximo passo.

### Knowledge Engine

Fornece informações aprovadas sobre produtos, planos, políticas, perguntas frequentes e processos.

### CRM e memória

Armazena dados autorizados do lead, etapa do funil, histórico resumido, consentimento e ações pendentes.

### Guardrails

Validam conteúdo, limites comerciais, privacidade, segurança e necessidade de intervenção humana.

## Requisitos não funcionais

- rastreabilidade;
- idempotência dos webhooks;
- proteção de dados;
- controle de acesso;
- logs sem exposição indevida;
- tolerância a falhas;
- possibilidade de desligamento manual;
- separação entre desenvolvimento e produção;
- versionamento de prompts e regras.

## Segredos

Tokens e chaves deverão permanecer em cofres de segredo ou variáveis de ambiente. Nunca deverão ser gravados no GitHub.

## Decisão pendente

A escolha definitiva entre n8n e Make deverá ser validada por custo, facilidade operacional, hospedagem, controle de dados e capacidade de manutenção.
