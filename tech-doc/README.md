## tech-doc

Generate comprehensive technical documentation for a Firefox/Gecko subsystem
(e.g. WebCodecs, MSE, WebRTC, WebAudio, Graphics, IPC). The resulting
Markdown file is meant to be loaded as **context input** for later AI coding
sessions — feature planning, spec implementation, debugging, or code
tracing — where a high-signal domain overview beats letting the model
re-derive architecture from scratch every time.

### Usage

```
/tech-doc                             # prompts for a domain
/tech-doc WebCodecs                   # generate WebCodecs documentation
/tech-doc for MSE                     # natural-language form
/tech-doc WebRTC                      # any domain from the reference table
```

If no domain is given, the skill uses `AskUserQuestion` to offer the
built-in list. Unlisted subsystems are also accepted — type a free-form
name and the skill will research it against the codebase.

### What it does

1. **Resolves the domain** — maps the requested subsystem to its primary
   source directories and related web specs via the built-in Domain
   Reference table in `SKILL.md`. For unlisted domains, it asks for
   clarification.

2. **Shows the pre-filled prompt** — before generating, previews the
   documentation request (sections, scope, target directories) and offers
   a customize step. The user can add focus areas, drop sections, or
   point the skill at extra directories.

3. **Asks where to save** — defaults to
   `.claude/skills/tech-doc/{domain}.md`; a custom path can be given for
   per-project storage.

4. **Researches the codebase** — uses file reads and (optionally)
   `searchfox-cli` to explore the relevant directories, then writes the
   document. The generated doc is the product — the skill does **not**
   merely echo the prompt template back.

### Document structure

Each generated file covers seven sections, modeled on what an AI coding
assistant needs to orient in an unfamiliar subsystem:

1. **High-Level Architecture** — modules, dependencies, process hosting,
   ASCII diagram.
2. **Core Modules Deep Dive** — purpose, key classes, lifetimes,
   thread/task model.
3. **Architectural Control Points** — orchestration, state management,
   data-flow drivers, API entry points.
4. **Key Data Flows** — sources, transformations, destinations.
5. **Key Event Flows** — event types, dispatch, state transitions, error
   paths.
6. **Action-to-Behavior Mappings** — user/system triggers → method
   chains → cross-process hops.
7. **Critical Cross-Boundary Interactions** — IPC/IPDL, threads,
   modules, C++/Rust/JS/WebIDL seams.

### Built-in domains

The Domain Reference table in `SKILL.md` pre-maps these subsystems to
their primary directories and specs, so no domain-specific prompting is
needed:

| Domain | Primary Directories |
|---|---|
| WebCodecs | `dom/media/webcodecs/`, `media/ffvpx/` |
| Media Playback | `dom/media/`, `dom/html/` |
| MSE | `dom/media/mediasource/` |
| MediaRecorder | `dom/media/mediarecorder/` |
| WebRTC | `dom/media/webrtc/`, `media/webrtc/` |
| WebAudio | `dom/media/webaudio/` |
| Graphics | `gfx/`, `dom/canvas/` |
| IPC | `ipc/`, `dom/ipc/` |
| Networking | `netwerk/` |
| Layout | `layout/` |

Free-form domains outside this list work too; the skill will infer
directories from the name or ask for them.

### Dependencies

- **Firefox source tree** — the skill is meant to be invoked from inside
  a mozilla-central checkout. Without it, the file-reading step has
  nothing to read.
- **[searchfox-cli](https://github.com/padenot/searchfox-cli)**
  *(optional, recommended)* — speeds up codebase exploration via indexed
  search. Without it, the skill falls back to `Grep`/`Glob`, which is
  slower but still works.

### Output

- A Markdown file at `.claude/skills/tech-doc/{domain}.md` (default) or
  a user-specified path.
- Self-contained: no external links are required to understand the
  document. Intended to be fed back into Claude Code as a `@file`
  reference when starting a new task in the same subsystem.
