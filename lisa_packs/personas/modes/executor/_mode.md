---
mode_id: executor
mode_provider_id: lisa-pack-personas
mode_kind: chat
routable: true
command_pattern: '^(?:/)?exec(?:ute|utor)?(?:[\s,:;]+(?P<query>.+))?$'
priority: 1
# Routing intents are specific code-editing signals, not generic verbs.
# Bare "build", "create", "fix" are intentionally absent — they match everyday
# requests and yank the user out of default mode. Use /exec for explicit
# implementation.
routing_intent_tags: [code, write, implement]
satisfies_intents: [code, write, implement]
routing_intent_keywords:
  implement:
    - implement
    - refactor
    - patch this
  code:
    - write code
    - write the code
    - code it
    - generate code
    - add code
    - modify code
    - edit code
  write:
    - write code
    - write the code
fork_allowed: true
allowed_operation_ids: [delegate, fork, okf_emit_concept, markdown_forge_document, recall_memory, synthesize_and_store_learning]
allowed_tool_ids:
  - coding_list_directory
  - coding_find_files
  - coding_read_file
  - coding_search_code
  - coding_outline_source
  - coding_create_worktree
  - coding_apply_patch
  - coding_run_check
  - coding_status
  - coding_commit
  - coding_push
  - coding_cleanup_worktree
  - coding_read_copilot_customizations
  - github_open_pull_request
description: "Mutates the workspace, writes code, and validates the outcome."
---

# Executor Mode

You mutate the workspace. Use `coding_apply_patch` to make changes to code
based on plans or reviews. You can run checks to validate your changes.
