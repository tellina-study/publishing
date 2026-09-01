#!/usr/bin/env bash
# PreToolUse(Bash) guard: LIVE blog publish requires explicit owner approval.
# Fires only for `scripts/wp_publish.py ... --status publish` (или --status=publish).
# Draft publish (без --status publish) — свободно (хук молчит → allow по умолчанию).
cmd=$(jq -r '.tool_input.command // ""' 2>/dev/null)
if printf '%s' "$cmd" | grep -Eq 'wp_publish\.py.*--status[[:space:]=]+publish'; then
  cat <<'JSON'
{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":"Публикация в ЛАЙВ на tellian.io (wp_publish.py --status publish). По правилу владельца требуется явное подтверждение перед выходом наружу. Черновик (без --status publish) разрешён свободно."}}
JSON
fi
