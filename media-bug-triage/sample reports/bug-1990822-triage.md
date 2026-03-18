# Bug 1990822 Triage Analysis

**Generated:** 2026-03-18
**Bug URL:** https://bugzilla.mozilla.org/show_bug.cgi?id=1990822

## Bug Information

- **Summary:** Crash in [@ libspeechd.so.2] with libspeechd.so.2 2.6.0.0
- **Reporter:** Sebastian Hengst [:aryx] (aryx.bugmail@gmx-topmail.de)
- **Status:** NEW
- **Product:** Core
- **Component:** Web Speech
- **Severity:** S2 (set by jmathies@mozilla.com on 2026-02-05)
- **Priority:** P2 (set by jmathies@mozilla.com on 2026-01-22)
- **Keywords:** crash (was `topcrash` Sep 26 – Dec 19, 2025)
- **Blocks:** [1708504](https://bugzilla.mozilla.org/show_bug.cgi?id=1708504) ([meta] Media Triage)
- **Created:** 2025-09-25 (~6 months ago)
- **Security Sensitive:** No

## Research Summary and Key Findings

Firefox dynamically loads `libspeechd.so.2` at startup to provide Web Speech Synthesis on Linux via the Speech Dispatcher daemon. The initialization code in [SpeechDispatcherService.cpp](https://searchfox.org/mozilla-central/source/dom/media/webspeech/synth/speechd/SpeechDispatcherService.cpp) loads the library, resolves function symbols, opens a connection with `spd_open()`, and then calls `spd_list_synthesis_voices()` at line 358 to enumerate available voices. In libspeechd version 2.6.0.0, this call passes a null pointer to `__strlen_avx2` (libc's AVX2-optimized strlen), triggering a `SIGSEGV / SEGV_MAPERR @ 0x0` crash in the parent process. The crash occurs entirely inside the library (frames #1–#3), so Firefox has no opportunity to catch it.

Paul Adenot (padenot@mozilla.com, Comment 3) identified the fix approach: detect the library version at runtime and skip or disable Speech Dispatcher for the broken 2.6.0.0 release. The code currently checks for ABI compatibility by probing for the `spd_get_volume` symbol (introduced in v0.8.2), but there is no version-specific block for 2.6.0.0. No fix or patch has landed yet.

**Socorro data** shows [3,741 crashes in the last 90 days](https://crashes.mozilla.org/signatures?q=signature%3A%22libspeechd.so.2%22) (as of 2026-03-18), spanning Firefox 146 through the current 148.x release and affecting ESR channels. The bug was removed from the topcrash list in December 2025 (was previously in the top 5 Linux desktop crashes on release), but the crash volume remains significant and persistent — it has not self-resolved through library updates.

No closely related duplicate bugs were found in the Web Speech component. The bug blocks [1708504](https://bugzilla.mozilla.org/show_bug.cgi?id=1708504), the Media Triage meta bug.

## Regression Timeline

Not a regression in the traditional sense. The crash started appearing at high volume when Speech Dispatcher 2.6.0.0 was shipped by Linux distributions (Ubuntu and derivatives, given correlations with Noto fonts and Ubuntu-specific kernel strings). The bug was filed 2025-09-25 with 600+ crashes already recorded, quickly triggering topcrash criteria on 2025-09-26. Volume has gradually declined (removed from topcrash 2025-12-19) but remains ongoing as many users are still running libspeechd 2.6.0.0.

## Classification

| Signal | Detected | Evidence |
|--------|----------|----------|
| Clear STR | No | No user-reproducible steps; triggers at browser startup when Speech Dispatcher 2.6.0.0 is installed |
| Test Case | No | None provided |
| Crash Stack | Yes | SIGSEGV in `__strlen_avx2` ← libspeechd.so.2 (×3 frames) ← `SpeechDispatcherService::Setup()` @ SpeechDispatcherService.cpp:358 |
| Fuzzing | No | Filed by human reporter from Socorro data |

**Platform:** Linux only (100% of crashes), parent process (100%), strongly correlated with Ubuntu and derivatives.

**Crash signature:** [libspeechd.so.2](https://crashes.mozilla.org/signatures?q=signature%3A%22libspeechd.so.2%22)

## Assessment

- **Suggested Severity:** S2 (confirmed — crashes the parent process, no workaround short of disabling `media.webspeech.synth.enabled`)
- **Suggested Priority:** P2 (confirmed — 3,741 parent-process crashes in 90 days, ongoing across all current releases)

### Assessment Reasoning

This is a parent-process crash (the most severe crash type for user experience) triggered on any Linux system where libspeechd.so.2 version 2.6.0.0 is installed. The root cause is a bug in the upstream Speech Dispatcher 2.6.0.0 library, but Firefox is responsible for providing a version guard since the library is dynamically loaded at runtime. S2/P2 is appropriate: the crash affects a meaningful number of Linux users, the parent process going down affects the full browser session, and there is currently no workaround available to end-users without manual pref editing.

The fix is well understood but not yet implemented: Firefox needs to detect libspeechd version 2.6.0.0 at runtime (e.g., via a symbol-presence check or reading ELF version information via `dlinfo()`/`dladdr()`) and disable Speech Dispatcher initialization for that specific version. The existing version-checking infrastructure (lines 328–334 in SpeechDispatcherService.cpp) already demonstrates the pattern for doing this.

The fact that crashes are still accumulating on the latest 148.x release means this requires active attention; it will not self-resolve without a Firefox-side patch or until 2.6.0.0 is phased out of all active Ubuntu LTS releases.

## Codebase Investigation

**Key file:** [SpeechDispatcherService.cpp](https://searchfox.org/mozilla-central/source/dom/media/webspeech/synth/speechd/SpeechDispatcherService.cpp)

The `Setup()` function (starting at line 312) performs the following steps:
1. `PR_LoadLibrary("libspeechd.so.2")` — dynamically loads the library
2. `PR_FindFunctionSymbol(speechdLib, "spd_get_volume")` — ABI compatibility check for v0.8.2+
3. Symbol resolution loop for all required `spd_*` functions
4. `spd_open(...)` — opens a connection to the Speech Dispatcher daemon
5. **Line 358:** `spd_list_synthesis_voices(mSpeechdClient)` — **crash point** in v2.6.0.0

The library declares no version-getter function (the comment on line 329 notes this), meaning a version check must use indirect means. Possible approaches:
- Check for a symbol introduced in v2.6.1 (or removed in v2.6.0) to identify the bad version
- Use `dlinfo(handle, RTLD_DI_LINKMAP, ...)` to get the full library path, then parse the ELF `DT_SONAME` or package metadata
- Check for the `spd_get_client_version` symbol (confirmed absent in Firefox's integration; needs upstream verification of when it was added)

## Suggested Investigation Areas

1. **Version detection** — Determine what symbols or ELF fields distinguish libspeechd 2.6.0.0 from 2.6.1+ (or earlier). The upstream speechd changelog/git history at https://github.com/brailcom/speechd would be the authoritative source. A symbol that was *added* after 2.6.0.0 or *removed* from 2.6.0.0 can serve as a cheap runtime version probe using the existing `PR_FindFunctionSymbol` pattern.

2. **Guard at line 358** — Once a version check is in place, add a `NotifyError(u"lib-too-old"_ns)` return path immediately before the `spd_list_synthesis_voices` call (matching the pattern at lines 331–333), gating specifically on v2.6.0.0.

3. **Upstream bug** — The issue should also be reported to Speech Dispatcher upstream at https://github.com/brailcom/speechd if not already done (Comment 2 asks this question; no follow-up recorded in the bug).

## Bugzilla Use Tracking

- Total Bugzilla Queries: 5
- Total Bugs Processed: 3 (1990822, 1708504, Web Speech component search)
- Estimated Download Bandwidth Used: ~0.05 MB
- Inaccessible Bugs Due to Permissions: 0
