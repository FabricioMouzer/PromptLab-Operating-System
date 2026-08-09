# Automação social PromptLab.AI + ZeloVita

**Status:** pronta para importar e configurar no n8n  
**Data:** 2026-08-09  
**Publicador:** Postiz  
**Gerador de conteúdo:** workflow publicado no Dify

## O que este pacote entrega

Dois workflows independentes:

1. `01-generate-content-package.json`: recebe marca, tema e canais; chama o Dify; valida a resposta e devolve um pacote em português do Brasil com status de rascunho.
2. `02-publish-approved-package.json`: recebe um pacote aprovado, valida marca, mídia, contas e regras; converte o conteúdo para o formato do Postiz; cria rascunho, agenda ou publica.

Essa separação impede que uma saída incorreta do modelo seja publicada sem aprovação.

## Arquivos

```text
automation/n8n/social-publishing/
├── 01-generate-content-package.json
├── 02-publish-approved-package.json
├── README.md
├── activation-checklist.md
├── dify-content-workflow-prompt.md
└── examples/
    ├── promptlab-generate-request.json
    ├── zelovita-generate-request.json
    └── publish-draft-request.json
```

## Pré-requisitos

- n8n Cloud ou self-hosted;
- um workflow publicado no Dify;
- Postiz hospedado ou self-hosted;
- contas conectadas ao Postiz por OAuth;
- credenciais separadas e armazenadas no n8n;
- mídia previamente enviada ao Postiz para Instagram e TikTok.

## Credenciais que devem ser criadas no n8n

### PromptLab Social Webhook

- tipo: Header Auth;
- nome sugerido: `PromptLab Social Webhook`;
- header sugerido: `X-PromptLab-Key`;
- valor: segredo forte, nunca salvo no GitHub.

### Dify App API

- tipo: Header Auth;
- nome sugerido: `Dify App API`;
- header: `Authorization`;
- valor: `Bearer SUA_CHAVE_DO_APP_DIFY`.

### Postiz API

- tipo: Header Auth;
- nome sugerido: `Postiz API`;
- header: `Authorization`;
- valor: a chave da API do Postiz, sem prefixo Bearer.

Após importar, abra cada node com alerta de credencial e selecione a credencial correta.

## Importação

1. No n8n, abra `Workflows`.
2. Selecione `Import from File`.
3. Importe primeiro `01-generate-content-package.json`.
4. Importe `02-publish-approved-package.json`.
5. Atribua as três credenciais.
6. Confirme as URLs do Dify e do Postiz nos nodes HTTP.
7. Execute usando as URLs de teste do Webhook.
8. Só publique os workflows depois dos testes da checklist.

## Fluxo de geração

```text
POST /webhook/promptlab-social-generate
→ valida solicitação
→ chama POST /v1/workflows/run no Dify
→ interpreta JSON
→ força status pending
→ devolve pacote para revisão
```

## Fluxo de publicação

```text
POST /webhook/promptlab-social-publish
→ exige approved=true
→ valida marca e canais
→ verifica mídia de Instagram/TikTok
→ aplica controles ZeloVita/TikTok
→ monta payload Postiz
→ chama POST /public/v1/posts
→ devolve IDs e status
```

## Modos de publicação

- `draft`: salva no Postiz sem publicar;
- `schedule`: agenda usando `scheduled_at` em ISO 8601;
- `now`: publica imediatamente.

Começar sempre com `draft`.

## Separação das marcas

O campo `brand` aceita somente:

- `promptlab`;
- `zelovita`.

Erros comuns como `PromptLive` e `ProptLive` são normalizados para `promptlab` no workflow de geração. A publicação, porém, exige o valor canônico para evitar ambiguidade.

Cada canal deve trazer o `provider_integration_id` da conta correta no Postiz. Não reutilizar o ID de uma marca na outra.

## Mídia

O Postiz exige que arquivos sejam enviados primeiro para `POST /public/v1/upload`. O retorno fornece `id` e `path`; ambos entram no array `media` do pedido de publicação.

Exemplo:

```json
"media": [
  {
    "id": "ID-RETORNADO-PELO-POSTIZ",
    "path": "https://uploads.postiz.com/arquivo.mp4"
  }
]
```

Canva e HeyGen não estão incorporados automaticamente nesses workflows porque exigem autorizações e APIs próprias. O pacote aceita a mídia produzida por eles depois do upload no Postiz.

## Controles de segurança

- publicação exige `approved: true`;
- ZeloVita com flag `health_claim` exige `health_reviewed: true`;
- Instagram e TikTok exigem mídia;
- TikTok público exige `tiktok_audit_confirmed: true`;
- canais duplicados são rejeitados;
- modo desconhecido vira erro, não publicação;
- nenhum token está incluído nos arquivos.

## Estado real da entrega

Os workflows são modelos importáveis e foram validados estruturalmente e como JSON. A execução ponta a ponta depende das credenciais, do workflow publicado no Dify, das contas conectadas ao Postiz e das aprovações das plataformas.

## Referências oficiais

- [n8n Webhook](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/)
- [Dify: Run Workflow](https://docs.dify.ai/en/api-reference/workflow-runs/run-workflow)
- [Postiz: Create Post](https://docs.postiz.com/public-api/posts/create)
- [Postiz: Upload File](https://docs.postiz.com/public-api/uploads/upload-file)
- [Postiz: Instagram](https://docs.postiz.com/public-api/providers/instagram)
- [Postiz: Facebook](https://docs.postiz.com/public-api/providers/facebook)
- [Postiz: TikTok](https://docs.postiz.com/public-api/providers/tiktok)
