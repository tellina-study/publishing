# RU-доступ: CDN перед origin (без Cloudflare)

**Проблема:** origin на Vultr-Amsterdam (`136.244.103.245`) режется РКН — из РФ виден только под VPN.
**Решение:** RU-достижимый CDN перед origin. Origin (сайт + Umami + Remark42) остаётся на Vultr,
CDN отдаёт кэш в РФ и проксирует динамику. Рекомендация — **Gcore** (RU-корни, точно виден из РФ,
есть free CDN); альтернатива — **BunnyCDN** (есть московский PoP, pay-as-you-go ~$0.01/ГБ).

## Архитектура
```
RU-пользователь ─► CDN edge (RU PoP) ─► origin.tellian.io (Vultr, Caddy)
                     кэширует /assets, /*.html
                     проксирует без кэша /stats/*, /comments/*
lessons.tellian.io  = CNAME → CDN
origin.tellian.io   = A → 136.244.103.245 (новый хост под origin, TLS от Caddy)
```
Same-origin для Umami/Remark42 сохраняется: всё под `lessons.tellian.io`, шаблон не меняем.

## Что делает владелец
1. **Завести аккаунт** Gcore (или BunnyCDN).
2. **Создать CDN-ресурс (pull-zone):**
   - Custom domain (что отдаём пользователю): `lessons.tellian.io`
   - Origin (откуда тянуть): `origin.tellian.io`, схема HTTPS
   - HTTPS для custom domain: включить (Let's Encrypt у CDN)
   - **Правило кэша:** `/stats/*` и `/comments/*` — **bypass cache** (динамика Umami/Remark42);
     остальное (`/assets/*`, html) — кэшировать.
   - Получить **CNAME-таргет** CDN (вида `xxxx.gcdn.co` / `xxx.b-cdn.net`).
3. **DNS (tellian.io):**
   - `origin.tellian.io` → **A** → `136.244.103.245`
   - `lessons.tellian.io` → сменить A на **CNAME** → `<CDN CNAME>`
4. **Прислать мне** CDN CNAME + подтвердить DNS — я добавлю `origin.tellian.io` в Caddy (auto-TLS),
   проверю кэш-правила и RU-доступ.

## Что делаю я после этого
- Добавлю `origin.tellian.io` в Caddyfile (тот же root + reverse-proxy /stats,/comments), auto-TLS.
- Проверю: сайт открывается через CDN, /stats и /comments не кэшируются, слайды кэшируются.
- (Опц.) закрою прямой доступ к origin по IP, оставив только через CDN.

> Пока CDN не поднят — сайт работает глобально и из РФ под VPN. Origin-инфра готова.
