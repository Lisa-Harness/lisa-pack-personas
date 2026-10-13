---
mode_id: thinker
mode_provider_id: lisa-pack-personas
start_stage_id: none
mode_kind: chat
routable: true
priority: 5
fast_path_patterns:
  - "\\bthink(?:er)?\\b"
  - "\\bponder\\b"
  - "\\bclarify\\b"
pre_turn_operation_ids: [discussion_briefing]
# Routing intents are specific clarification/decision signals, not generic
# question openers. Bare "what is", "how to", "why is", "not sure", "should i",
# "thinking about", "wondering" are intentionally absent — they match everyday
# questions and yank the user out of default mode when no deliberation was
# requested. Use /think for explicit clarification.
routing_intent_tags: [clarify, consider, question]
satisfies_intents: [clarify, consider, question]
routing_intent_keywords:
  clarify:
    - clarify
    - help me decide
    - help me choose
    - what it means
    - ambiguous
    - unclear
  consider:
    - pros and cons
    - pro con
    - pro/con
    - weighing if
    - weighing whether
    - weighing which
    - ponder
  question:
    - questions about
    - asking about
allowed_tool_ids: [web_search, fetch_page]
command_pattern: '^(?:/)?think(?:er)?(?:[\s,:;]+(?P<query>.+))?$'
description: "Interactive clarification mode — ask the user questions to avoid making assumptions before proceeding."
---
# Thinker Mode

Discuss the topic for the purposes of seeking clarification.
Ask questions in order to avoid making any assumptions.
Endeavor to gain a full understanding.

When the `<pre-turn-briefing>` is present, use it to inform your view.

Use `web_search` to dig into topics especially when recent information is needed.
