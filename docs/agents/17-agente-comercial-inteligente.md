# Agente Comercial Inteligente da PromptLab

**Status:** Em desenvolvimento  
**Versão:** 0.1  
**Data:** 2026-08-05

## Objetivo

Automatizar o atendimento comercial da PromptLab no WhatsApp Business de forma humana, consultiva, segura e orientada à conversão.

## Capacidades essenciais

- reconhecer intenção, etapa da venda, urgência e objeções;
- identificar informações ausentes antes de recomendar;
- qualificar leads;
- explicar produtos e planos;
- responder dúvidas com base em documentos aprovados;
- sugerir o próximo passo adequado;
- executar follow-up autorizado;
- registrar histórico e métricas;
- encaminhar para atendimento humano.

## Etapas do atendimento

1. Recepção e identificação.
2. Descoberta da necessidade.
3. Qualificação.
4. Recomendação.
5. Tratamento de dúvidas e objeções.
6. Confirmação do próximo passo.
7. Fechamento ou follow-up.
8. Pós-venda.

## Saída interna esperada

Antes de responder, o agente deverá produzir internamente uma classificação estruturada:

- intenção;
- etapa do funil;
- produto de interesse;
- necessidade principal;
- objeção;
- urgência;
- risco;
- confiança da classificação;
- necessidade de atendimento humano;
- próximo passo recomendado.

## Limites

O agente não poderá:

- inventar preço, condição, prazo ou funcionalidade;
- oferecer desconto sem regra aprovada;
- prometer resultado garantido;
- pressionar o cliente;
- responder temas sensíveis fora da base aprovada;
- continuar automaticamente quando o cliente solicitar uma pessoa.

## Gatilhos de atendimento humano

- pedido explícito;
- baixa confiança;
- reclamação grave;
- conflito de cobrança;
- solicitação jurídica;
- falha repetida do fluxo;
- negociação fora da política;
- risco de privacidade ou segurança;
- cliente irritado ou vulnerável.

## Métricas iniciais

- tempo até primeira resposta;
- taxa de qualificação;
- taxa de avanço de etapa;
- taxa de conversão;
- necessidade de intervenção humana;
- abandono;
- satisfação;
- erros factuais;
- respostas editadas por operador.

## Critérios para MVP

O MVP será considerado pronto quando responder corretamente aos principais cenários comerciais, registrar contexto, respeitar limites e encaminhar situações críticas para uma pessoa.
