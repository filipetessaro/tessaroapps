# tessaroapps

Site estático com as páginas de **privacidade, termos de uso, exclusão de conta e suporte**
de todos os aplicativos. Publicado por GitHub Pages em **https://apps.tessaroapps.com**.

Repo público de propósito: as lojas exigem que essas URLs abram sem login.
Nada de segredo entra aqui.

## Mapa

| App | Páginas |
|---|---|
| Devocional Diário | `/devocional/` · `privacy/` · `terms/` |
| Íris | `/iris/` · `privacy/` · `terms/` · `delete-account/` · `psicologos/` |
| GarageRank | `/garagerank/` · `privacy/` |
| Coin Value Snap | `/coinsnap/` · `privacy/` · `delete-account/` |
| PhotoEvolve | `/photoevolve/` · `privacy/` · `terms/` · `delete-account/` — idem em `/en/` e `/es/` |
| PlantScan AI | `/plantscan/` · `privacy/` · `terms/` |
| InBloom | `/inbloom/` · `privacy/` |
| Idle Realms: Rise | `/idle-realms/` · `privacy/` · `terms/` · `delete-account/` |

**Slugs em inglês em todos os apps**, inclusive nos de conteúdo em português: a URL é
infraestrutura, não texto de leitura, e é o que revisor de loja espera encontrar.

Cada página é uma **pasta com `index.html`** — o GitHub Pages não serve extensão implícita
de forma confiável. Por isso a **barra final** da URL importa.

## Um repo para todos os apps

Substitui o padrão antigo de um repo por app. Os seis repos originais continuam no ar,
com cada página trocada por um redirect para cá:

| Repo antigo | Vai para |
|---|---|
| `iris-privacy` | `/iris/` |
| `plantscan-ai-legal` | `/plantscan/` |
| `coin-value-snap-privacy` | `/coinsnap/` |
| `photocollector-site` (pasta local `photoevolve-site`) | `/photoevolve/` |
| `garagerank-legal` | `/garagerank/` |
| `inbloom-app-legal` | `/inbloom/` |

O repo do PhotoEvolve chama `photocollector-site` no GitHub, nome anterior do app — a
pasta local se chama `photoevolve-site` e aponta para ele. Procurar por "photoevolve" no
GitHub não acha.

**Não apague esses repos.** As fichas das lojas ainda apontam para eles, e link quebrado
em ficha publicada é motivo de suspensão. Arquivar só depois que todas as lojas estiverem
apontando para cá.

O conteúdo das páginas migradas **não foi reescrito** — são textos legais já aceitos por
loja. O que mudou foi onde moram e os links internos, ajustados para a nova profundidade
pelo script `migrar.py` (descartável, rodou uma vez).

## DNS

O domínio está na HostGator e a **raiz não é tocada** — só o subdomínio:

| Tipo | Nome | Valor |
|---|---|---|
| CNAME | `apps` | `filipetessaro.github.io` |

Em Settings → Pages: Source = branch `main`, Custom domain = `apps.tessaroapps.com`,
e **Enforce HTTPS** quando o certificado for emitido.

## Pendências

- [ ] Atualizar a URL de privacidade **na ficha de cada app** no Google Play e na App Store.
- [ ] Atualizar os links **dentro do código** de cada app (só chega ao usuário com release novo).
- [ ] Unificar o visual: as páginas migradas ainda usam o CSS que cada site tinha.
- [ ] Conferir se o **objeto social / CNAE** da empresa cobre publicação de software —
      a razão social é de treinamento profissional.
- [ ] Revisão jurídica.
