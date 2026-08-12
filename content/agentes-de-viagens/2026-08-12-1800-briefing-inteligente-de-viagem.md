# PromptLab.AI — Agente de viagens / Consultor de turismo

**Data:** 2026-08-12  
**Horário:** 18:00  
**Tema:** Briefing inteligente de viagem  
**Reel:** SEM AVATAR + VOZ EM OFF

## Profissão

Agente de viagens / Consultor de turismo.

## Problema resolvido

Pedidos de viagem costumam chegar incompletos: destino aberto, orçamento pouco claro, datas flexíveis, perfil dos viajantes, preferências, restrições, ritmo de viagem e prioridades espalhados entre mensagens. Isso gera retrabalho, propostas desalinhadas e tempo perdido pesquisando opções que não fazem sentido para o cliente.

## Benefício esperado

Transformar mensagens e anotações do cliente em um briefing de viagem estruturado, com prioridades, dados faltantes, critérios de pesquisa, perguntas de confirmação, esqueleto de roteiro e checklist de proposta. A IA organiza a demanda; preços, disponibilidade, regras de entrada, horários e condições comerciais devem ser verificados em fontes atuais antes da venda.

## Prompt principal

```text
Você será meu Assistente Sênior de Briefing e Planejamento Comercial para Agência de Viagens.

Sua missão é transformar as informações fornecidas pelo cliente em um BRIEFING DE VIAGEM claro, completo e acionável, pronto para orientar a pesquisa e a montagem de uma proposta personalizada.

REGRAS IMPORTANTES

- Não invente preços, disponibilidade, horários, regras de entrada, exigências migratórias, políticas de bagagem, taxas, clima, eventos ou condições comerciais.
- Sempre diferencie: FATO INFORMADO, PREFERÊNCIA, RESTRIÇÃO, INFORMAÇÃO FALTANTE e ITEM QUE PRECISA DE VERIFICAÇÃO ATUAL.
- Não trate estimativas antigas como informação atual.
- Marque preços, disponibilidade, horários, documentos, vistos, vacinas, regras de entrada, taxas e políticas como: “VERIFICAR EM FONTE ATUAL ANTES DA VENDA”.
- Não reserve, compre ou confirme nada automaticamente.
- Não altere datas, orçamento ou categoria de serviço sem deixar explícito que se trata de uma alternativa sugerida.
- Preserve dados pessoais e use somente as informações necessárias para o planejamento.
- Quando houver criança, idoso, gestante, pessoa com mobilidade reduzida ou necessidade especial informada, destaque requisitos de acessibilidade e conforto sem fazer suposições médicas.
- Priorize aderência ao perfil, clareza comercial, redução de retrabalho e experiência do cliente.

DADOS DO CLIENTE

Nome ou identificador:
[preencher]

Quantidade de viajantes:
[preencher]

Adultos / crianças / idades relevantes:
[preencher]

Origem da viagem:
[preencher]

Destino desejado:
[preencher]

Datas ou período:
[preencher]

Flexibilidade de datas:
[preencher]

Duração desejada:
[preencher]

Orçamento total ou por pessoa:
[preencher]

O orçamento inclui:
[passagens, hospedagem, traslados, passeios, alimentação, seguro, outros]

Objetivo principal da viagem:
[lazer, lua de mel, família, negócios, aniversário, evento, descanso, aventura etc.]

Ritmo desejado:
[tranquilo, equilibrado, intenso]

Perfil de hospedagem:
[preencher]

Preferências de localização:
[preencher]

Preferências de voo/transporte:
[preencher]

Interesses:
[gastronomia, praias, história, compras, natureza, vida noturna, parques, museus etc.]

Itens indispensáveis:
[preencher]

O que o cliente quer evitar:
[preencher]

Restrições de mobilidade ou acessibilidade informadas:
[preencher]

Bagagem ou necessidades logísticas relevantes:
[preencher]

Documentação já conhecida:
[preencher]

Programas de fidelidade / milhas, se o cliente quiser considerar:
[preencher]

Mensagens e observações do cliente:
[cole aqui]

DEPOIS DE ANALISAR, ENTREGUE:

1. RESUMO DO PERFIL DA VIAGEM

Resuma em até 8 pontos:
- quem viaja;
- objetivo;
- destino/período;
- orçamento informado;
- ritmo;
- preferências principais;
- restrições;
- prioridade número 1 do cliente.

2. INFORMAÇÕES FALTANTES

Liste somente o que ainda precisa ser confirmado antes de iniciar uma pesquisa comercial eficiente.

Separe em:
- datas;
- orçamento;
- transporte;
- hospedagem;
- interesses;
- restrições;
- documentação;
- forma de pagamento, somente se relevante e informado pelo processo da agência.

3. TOP 7 PERGUNTAS PARA O CLIENTE

Crie perguntas objetivas que reduzam retrabalho e ajudem a definir a proposta.

Evite perguntas que já foram respondidas.

4. CRITÉRIOS DE PESQUISA

Organize os critérios que a agência deverá usar para procurar opções.

Crie uma tabela com:
- categoria;
- preferência do cliente;
- requisito obrigatório ou desejável;
- faixa/orçamento informado;
- item que precisa de verificação atual.

5. PRIORIDADES DA PROPOSTA

Classifique como:
- ESSENCIAL;
- IMPORTANTE;
- FLEXÍVEL.

Use somente informações fornecidas pelo cliente.

6. POSSÍVEIS CONFLITOS

Identifique conflitos como:
- orçamento x padrão de hospedagem;
- duração x quantidade de atividades;
- localização x preço;
- conforto x conexões;
- ritmo tranquilo x roteiro excessivo.

Não resolva alterando preferências sem autorização. Apenas sinalize e proponha o que precisa ser confirmado.

7. ESQUELETO DE ROTEIRO

Crie uma estrutura de roteiro sem inventar horários, preços ou disponibilidade.

Organize por dia/período com:
- objetivo do dia;
- região ou tipo de atividade;
- ritmo;
- observação logística;
- item que precisa de verificação atual.

Se o destino ainda não estiver definido, substitua o roteiro por uma MATRIZ DE DESTINOS para pesquisa.

8. CHECKLIST DA PROPOSTA

Crie um checklist contendo:
- transporte;
- hospedagem;
- traslados;
- passeios;
- seguro, se aplicável ao processo da agência;
- documentação a verificar;
- bagagem/regras a verificar;
- política de cancelamento a verificar;
- taxas a verificar;
- observações do cliente.

9. MENSAGEM DE CONFIRMAÇÃO DO BRIEFING

Crie uma mensagem curta para o cliente contendo:
- resumo do que foi entendido;
- dados ainda faltantes;
- próximos passos;
- aviso de que preços e disponibilidade serão confirmados no momento da cotação.

10. RESUMO INTERNO PARA O AGENTE

Crie um handover de até 10 linhas contendo:
- perfil;
- orçamento;
- prioridades;
- restrições;
- pesquisa necessária;
- riscos de desalinhamento;
- próximo passo.

11. OPORTUNIDADES DE UPSELL E CROSS-SELL

Somente quando fizer sentido para o perfil informado, liste possibilidades para o AGENTE AVALIAR, como:
- traslado;
- seguro viagem;
- passeio;
- ingresso;
- upgrade;
- noite adicional;
- serviço premium.

Não apresente como necessidade obrigatória e não invente preço.

12. INFORMAÇÕES QUE PRECISAM DE VERIFICAÇÃO ATUAL

Liste tudo que deve ser checado em fonte oficial ou fornecedor atual antes da proposta final, incluindo quando aplicável:
- preço;
- disponibilidade;
- regras de entrada;
- documentação;
- visto;
- exigências sanitárias;
- horários;
- política de bagagem;
- taxas;
- cancelamento;
- funcionamento de atrações.
```

## Modo de usar

Cole as mensagens do cliente, preencha os dados conhecidos e execute o prompt antes de iniciar a cotação. Use a saída como briefing e checklist interno. Depois, confirme preços, disponibilidade, documentos, regras de entrada, horários e políticas em fontes atuais antes de enviar qualquer proposta final.

## Reel — HeyGen

**Formato:** SEM AVATAR + VOZ EM OFF  
**Duração:** 40–45 s  
**Idioma:** Português do Brasil  
**Formato de tela:** 9:16

```text
Crie um Reel vertical 9:16 para a PromptLab.AI.

IMPORTANTE

NÃO utilizar avatar.
NÃO utilizar apresentador falando para a câmera.

Utilizar:
- voz em off natural em português do Brasil;
- B-roll de viagens;
- aeroporto;
- mala;
- mapas genéricos;
- notebook com proposta de viagem sem dados reais;
- mensagens genéricas de cliente;
- calendário;
- hotel e transporte em cenas ilustrativas;
- motion graphics;
- legendas dinâmicas;
- identidade visual PromptLab.AI.

Nunca mostrar documentos, passaportes, nomes, reservas ou dados reais de clientes.

IDENTIDADE VISUAL

- azul-marinho/preto;
- detalhes verde-limão;
- estética tecnológica e premium;
- cortes a cada 1,5–3 segundos;
- legendas grandes e embutidas;
- trilha moderna e discreta abaixo da narração.

0–3s — GANCHO

B-roll:
Várias mensagens surgindo rapidamente:
“Quero viajar em outubro.”
“Pode ser praia.”
“Não quero gastar muito.”

VOZ:
“Agente de viagens: quantas cotações começam com um pedido assim?”

TEXTO NA TELA:
PEDIDO VAGO = RETRABALHO

3–10s

B-roll:
Mapa, calendário, hotéis e mensagens misturados na tela.

VOZ:
“Sem orçamento claro, datas, perfil e prioridades, você pesquisa dezenas de opções que talvez nem sirvam para o cliente.”

10–20s

B-roll:
As informações entram em uma interface genérica de IA e viram um briefing organizado.

VOZ:
“Com um único prompt, a IA transforma as mensagens em um briefing de viagem pronto para orientar a cotação.”

TEXTO:
DATAS
ORÇAMENTO
PREFERÊNCIAS
RESTRIÇÕES

20–31s

B-roll:
Checklist, estrutura de roteiro, prioridades e mensagem para o cliente.

VOZ:
“Ela identifica o que está faltando, organiza prioridades, cria perguntas e prepara o esqueleto da proposta.”

31–38s

B-roll:
Agente trabalhando em notebook, sem rosto em destaque, conferindo fornecedores.

VOZ:
“A IA organiza o pedido. Preços, disponibilidade e regras continuam sendo confirmados pelo profissional em fontes atuais.”

38–45s — CTA

Tela PromptLab.AI.

VOZ:
“Salve este vídeo e comente VIAGEM para receber o prompt completo.”

TEXTO FINAL:
COMENTE: VIAGEM
SALVE • TESTE • COMPARTILHE

CAPA DO REEL:
AGENTE DE VIAGENS
TRANSFORME PEDIDOS VAGOS
EM BRIEFINGS CLAROS
COM IA
```

## Capa do post — Canva

**Formato:** 1080 x 1350

**Headline:** AGENTE DE VIAGENS

**Título:** TRANSFORME PEDIDOS VAGOS EM BRIEFINGS CLAROS COM IA

**Linha de apoio:** Datas • Orçamento • Preferências • Roteiro

**CTA:** SALVE ESTE POST E USE O PROMPT

**Direção visual:** fundo azul-marinho/preto, detalhes verde-limão, mapa/avião estilizado, smartphone com mensagens genéricas à esquerda e briefing organizado à direita. Evitar excesso de ícones turísticos; manter estética profissional e tecnológica.

## Legenda — Instagram

✈️ **Agente de viagens: quanto tempo você perde pesquisando antes de descobrir que faltava uma informação básica do cliente?**

“Quero viajar em outubro.”  
“Pode ser praia.”  
“Não quero gastar muito.”

O prompt de hoje transforma mensagens assim em:

✅ perfil da viagem  
✅ informações faltantes  
✅ perguntas para o cliente  
✅ critérios de pesquisa  
✅ prioridades da proposta  
✅ esqueleto de roteiro  
✅ checklist comercial  
✅ mensagem de confirmação

A IA não substitui a cotação profissional.

**Ela organiza o pedido antes de você gastar tempo pesquisando opções.**

📌 Salve este post.  
💬 Comente **VIAGEM**.  
🚀 Siga a **PromptLab.AI**.

## Legenda — TikTok

✈️ Agente de viagens: transforme **mensagens vagas + orçamento + preferências** em um briefing claro usando um único prompt.

**Menos pesquisa desperdiçada. Mais propostas alinhadas.**

📌 Salve.  
💬 Comente **VIAGEM**.

## Stories

### Story 1 — Enquete

**SEU CLIENTE JÁ DISSE:**

“QUERO VIAJAR, MAS AINDA NÃO SEI DIREITO PARA ONDE”? 

Enquete:
- Toda semana 😵‍💫
- Meu briefing já é bom ✅

### Story 2 — Valor

**UM BOM PROMPT VIRA UM BRIEFING DE VIAGEM.**

Datas  
Orçamento  
Preferências  
Restrições  
Perguntas  
Critérios de pesquisa

### Story 3 — Interação

**O QUE MAIS ATRASA SUA COTAÇÃO?**

Caixa de perguntas:

Destino? Datas? Orçamento? Hotel? Voo? Cliente indeciso? Outro?

### Story 4 — CTA

**QUER O PROMPT COMPLETO?**

Responda:

**VIAGEM**

Menos retrabalho.  
Mais clareza.  
Mais tempo para vender.

## CTA principal

**Comente VIAGEM para receber o prompt completo.**

## Comentário fixado

**PROMPT DO DIA: AGENTES DE VIAGENS ✈️**

Comente **VIAGEM** se você quer o comando completo para transformar mensagens do cliente em briefing, perguntas, prioridades e estrutura de proposta.

## Hashtags

#PromptLabAI #AgenteDeViagens #ConsultorDeViagens #Turismo #AgenciaDeViagens #InteligenciaArtificial #ChatGPT #Produtividade #Prompts #IAnoTrabalho #Vendas #AtendimentoAoCliente

## Ferramentas escolhidas

- **ChatGPT:** desenvolvimento do prompt, estrutura e copy.
- **HeyGen:** Reel SEM AVATAR + VOZ EM OFF, com B-roll, motion graphics e legendas.
- **Canva:** capa e Stories, pela velocidade, custo, consistência visual e facilidade de reutilizar templates.

## Oportunidade de monetização

Produto sugerido: **Kit IA para Agentes de Viagens e Consultores de Turismo**.

O kit pode incluir prompts para:
- briefing de viagem;
- qualificação de lead;
- comparação de opções;
- estrutura de proposta;
- follow-up de orçamento;
- roteiro-base;
- checklist pré-embarque;
- mensagem pós-venda;
- pedido de avaliação;
- reativação de clientes.

### Funil recomendado

Reel/Post → comentário **VIAGEM** → prompt gratuito → mini-kit → Kit IA para Agentes de Viagens → assinatura PromptLab.AI.

### Proposta de valor

Menos retrabalho na coleta de informações, mais propostas alinhadas, atendimento mais profissional e maior capacidade de responder leads sem aumentar proporcionalmente a carga administrativa.
