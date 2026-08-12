---
mode_id: thinker
mode_provider_id: lisa-pack-personas
start_stage_id: none
mode_kind: chat
routable: true
priority: 5
pre_turn_operation_ids: [discussion_briefing]
routing_intent_tags: [clarify, consider, question]
satisfies_intents: [clarify, consider, question]
routing_intent_keywords:
  clarify:
    - clarify
    - not sure
    - figure out
    - what it means
    - asking about
    - questions about
    - should i
    - options for
    - ambiguous
    - unclear
    - help me decide
  consider:
    - considering
    - thinking about
    - thinking of
    - pro con
    - pro/con
    - pros and cons
    - weighing if
    - weighing whether
    - weighing which
  question:
    - question
    - asking
    - wondering
    - what is
    - how to
    - why is
    - what are
    - what does it mean
allowed_operation_ids: [web_search]
command_pattern: '^(?:/)?think(?:er)?(?:[\s,:;]+(?P<query>.+))?$'
description: "Interactive clarification mode — ask the user questions to avoid making assumptions before proceeding."
---
# Thinker Mode

Discuss the topic for the purposes of seeking clarification.
Ask questions in order to avoid making any assumptions.
Endeavor to gain a full understanding.

When the `<pre-turn-briefing>` is present, use it to inform your view.

Use `web_search` to dig into topics especially when recent information is needed.
