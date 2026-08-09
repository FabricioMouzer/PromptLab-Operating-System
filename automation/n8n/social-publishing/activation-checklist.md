# Checklist de ativação

## 1. Infraestrutura

- [ ] n8n acessível por HTTPS.
- [ ] Postiz hospedado ou self-hosted acessível por HTTPS.
- [ ] Dify com workflow publicado.
- [ ] Backups e logs habilitados.

## 2. Credenciais no n8n

- [ ] Header Auth `PromptLab Social Webhook` criado.
- [ ] Header Auth `Dify App API` criado.
- [ ] Header Auth `Postiz API` criado.
- [ ] Nenhuma chave foi escrita em node, arquivo ou GitHub.

## 3. Dify

- [ ] Prompt de geração configurado.
- [ ] Entradas usam os nomes documentados.
- [ ] Saída é JSON válido em `outputs.result`.
- [ ] Cinco testes PromptLab aprovados.
- [ ] Cinco testes ZeloVita aprovados.

## 4. Postiz

- [ ] Facebook PromptLab conectado.
- [ ] Instagram PromptLab conectado.
- [ ] TikTok PromptLab conectado ou marcado como pendente.
- [ ] Facebook ZeloVita conectado.
- [ ] Instagram ZeloVita conectado.
- [ ] TikTok ZeloVita conectado ou marcado como pendente.
- [ ] IDs das seis integrações registrados em local seguro.

## 5. Testes seguros

- [ ] Gerar rascunho PromptLab pelo webhook de teste.
- [ ] Gerar rascunho ZeloVita pelo webhook de teste.
- [ ] Enviar uma imagem de teste ao Postiz e guardar `id` e `path`.
- [ ] Criar somente `draft` para Facebook.
- [ ] Criar somente `draft` para Instagram.
- [ ] Criar somente `draft` privado para TikTok.
- [ ] Confirmar que a conta e marca estão corretas.
- [ ] Simular `approved=false` e verificar bloqueio.
- [ ] Simular ZeloVita com `health_claim` sem revisão e verificar bloqueio.
- [ ] Simular TikTok público sem auditoria e verificar bloqueio.

## 6. Liberação progressiva

- [ ] Dez rascunhos consecutivos corretos.
- [ ] Dez publicações supervisionadas corretas.
- [ ] Limite diário configurado.
- [ ] Procedimento de pausa definido.
- [ ] Alertas de falha testados.
- [ ] Publicação automática limitada autorizada por Fabrício.

## Critério de pronto

A automação só estará operacional quando todos os itens das seções 1 a 5 estiverem concluídos. TikTok público depende também da auditoria aplicável da plataforma.
