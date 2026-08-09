# ADR — Arquitetura do agente de criação e publicação social

**Data:** 2026-08-09  
**Status:** aprovado para protótipo  
**Decisor:** Fabrício Mouzer

## Contexto

A PromptLab.AI e a ZeloVita precisam produzir conteúdo recorrente e publicar no Instagram, Facebook e TikTok com menos intervenção manual. Foi solicitada a pesquisa de um repositório que funcionasse como um agente capaz de receber comandos, criar publicações e enviá-las às redes.

Não foi encontrado um único projeto confiável que execute criação, mídia, aprovação, publicação, métricas e governança com segurança. As APIs das plataformas também impõem autenticação, revisão, limites e consentimentos.

## Decisão

Adotar arquitetura composta:

- **n8n:** orquestração do fluxo;
- **Dify/LLM:** criação e adaptação do conteúdo;
- **Whisper:** entrada por áudio;
- **Crawl4AI:** pesquisa somente em fontes públicas e autorizadas;
- **Canva/HeyGen:** produção de mídia quando houver integração adequada;
- **Postiz:** calendário e publicação multicanal;
- **GitHub:** fonte oficial de verdade, regras e documentação;
- **Quality Gate:** validação antes da publicação.

Postiz é o candidato aprovado para o primeiro teste de publicação. TikTok permanece fora da publicação pública automática até o cliente cumprir os requisitos de auditoria e consentimento da plataforma.

## Alternativas consideradas

### Usar apenas Postiz

Rejeitada como arquitetura completa. Postiz publica e agenda, mas não substitui todas as etapas de estratégia, pesquisa, criação, revisão e governança.

### Usar apenas n8n com chamadas diretas às redes

Possível, mas rejeitada para o primeiro protótipo. Exige manter individualmente uploads, formatos, tokens, filas e mudanças de cada API.

### Usar Mixpost Lite

Mantida como alternativa. No momento, o Postiz apresenta melhor aderência ao objetivo multicanal e possui CLI direcionada a agentes.

### Criar um superagente sem aprovação

Rejeitada na fase inicial pelo risco operacional e reputacional.

## Consequências positivas

- separação entre criação e publicação;
- possibilidade de trocar componentes;
- rastreabilidade;
- redução de trabalho repetitivo;
- expansão progressiva da autonomia;
- proteção das contas e marcas.

## Consequências negativas

- exige configuração de várias ferramentas;
- haverá custo de servidor e APIs;
- Meta e TikTok podem exigir revisão de aplicativo;
- manutenção e atualização serão contínuas;
- a primeira versão não será completamente autônoma.

## Riscos e mitigação

- **Publicação errada:** aprovação inicial, prévia e limite diário.
- **Duplicidade:** chave idempotente e consulta de status antes de repetir.
- **Conta bloqueada:** OAuth oficial e respeito às políticas.
- **Vazamento de segredo:** variáveis de ambiente e cofre de segredos.
- **Conteúdo inadequado:** Quality Gate e regras específicas por marca.
- **Falha de provedor:** logs, alerta e procedimento manual.

## Critério de revisão

Revisar após 30 dias ou depois de 30 publicações supervisionadas. Aumentar autonomia somente se não houver incidente grave e se o sistema demonstrar ganho real de tempo, confiabilidade e resultado comercial.
