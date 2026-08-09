# Avaliação de repositórios para automação de redes sociais

**Verificação:** 2026-08-09

## Conclusão

O melhor candidato encontrado para a camada de publicação é o **Postiz**. Ele não substitui o cérebro do agente: deve ser combinado com **n8n** para orquestração e com um modelo/Dify para criação do conteúdo.

## Comparação

| Projeto | Papel adequado | Instagram | Facebook | TikTok | Licença/condição | Avaliação |
|---|---|---:|---:|---:|---|---|
| [Postiz](https://github.com/gitroomhq/postiz-app) | calendário, upload, agendamento e publicação | Sim | Páginas | Sim, com exigências do TikTok | AGPL-3.0 | Melhor publicador para o protótipo |
| [Postiz Agent CLI](https://github.com/gitroomhq/postiz-agent) | permitir que agentes acionem a API do Postiz | Sim | Sim | Sim | AGPL-3.0 | Ponte promissora, mas não é um agente de conteúdo completo |
| [n8n](https://github.com/n8n-io/n8n) | orquestração, agenda, regras, aprovações e logs | Via API/nó | Via API/nó | Via API ou Postiz | Source available/fair-code | Melhor coordenador do fluxo |
| [Mixpost Lite](https://github.com/inovector/mixpost) | gestão e calendário de redes | Depende da edição/configuração | Depende da edição/configuração | Verificar edição | MIT para o repositório Lite; Pro é comercial | Alternativa, porém menos aderente ao agente multicanal pretendido |

## Por que Postiz

- projeto oficial ativo e não arquivado;
- documentação de instalação por Docker;
- API pública e CLI própria para agentes;
- suporte declarado a Instagram, Facebook Page e TikTok;
- upload, calendário, agendamento e métricas em uma camada central;
- integração prevista com n8n e Make.

## Limitações importantes

### Não é “custo zero”

Self-hosting requer servidor, banco PostgreSQL, Redis, Temporal, armazenamento, domínio, HTTPS, backups e manutenção.

### Meta exige configuração

Instagram e Facebook dependem de aplicativo Meta, OAuth e permissões. Aplicativos públicos podem exigir verificação da empresa e revisão de permissões.

### TikTok é o maior bloqueio

O TikTok exige aplicação de desenvolvedor, site HTTPS, domínio verificado e auditoria para Direct Post público. Clientes não auditados podem ficar limitados a conteúdo privado. A experiência também precisa expor configurações e consentimentos exigidos pela plataforma.

### Confiabilidade deve ser testada

Existem relatos públicos de falhas de publicação e conexão após mudanças das APIs. Isso não invalida o projeto, mas exige versão fixada, ambiente de teste, monitoramento e plano manual de contingência.

### Licença

Postiz usa AGPL-3.0. Modificações e oferta do software pela rede podem gerar obrigações de disponibilização do código correspondente. Rever a licença antes de transformar a implantação em serviço comercial para clientes.

## Decisão recomendada

### Protótipo

- usar n8n como orquestrador;
- usar Dify/LLM para texto estruturado;
- testar Postiz como publicador;
- conectar primeiro uma página de teste do Facebook e uma conta profissional de Instagram;
- manter TikTok em rascunho até concluir auditoria e fluxo de consentimento.

### Produção

- escolher entre Postiz hospedado e self-hosted após medir custo e confiabilidade;
- fixar versões e acompanhar notas de segurança;
- usar domínio próprio e HTTPS;
- separar contas, chaves e logs de PromptLab e ZeloVita;
- não depender de scraping de Instagram ou TikTok.

## Alternativas rejeitadas

### Um único “superagente” com acesso irrestrito

Rejeitado por risco de publicação errada, vazamento de credenciais, bloqueio de contas e ausência de rastreabilidade.

### Copiar todos os repositórios para o PromptLab OS

Rejeitado por tamanho, atualização, segurança e licenças. Este repositório guarda a arquitetura e os contratos; componentes externos continuam separados.

### Automatizar TikTok desde o primeiro dia

Rejeitado até aprovação técnica. A plataforma impõe restrições que não podem ser eliminadas por código open source.

## Links de validação

- [Postiz: repositório principal](https://github.com/gitroomhq/postiz-app)
- [Postiz: instalação oficial por Docker Compose](https://github.com/gitroomhq/postiz-docker-compose)
- [Postiz: Instagram](https://docs.postiz.com/providers/instagram)
- [Postiz: Facebook](https://docs.postiz.com/providers/facebook)
- [Postiz: TikTok](https://docs.postiz.com/providers/tiktok)
- [TikTok: Content Posting API](https://developers.tiktok.com/products/content-posting-api)
- [TikTok: diretrizes para Direct Post](https://developers.tiktok.com/doc/content-sharing-guidelines/)
