# Firefox Mozconfig Build Options Reference

This document provides comprehensive reference information for Firefox build configurations. Use this to understand mozconfig options and generate correct configurations for different build types.

---

## 1. Preset Mozconfigs

Complete, ready-to-use mozconfigs for common development scenarios. These are self-contained and don't require additional file resolution.

### Debug Build (All Platforms)

Standard debug build with assertions and debug symbols.

```bash
# Debug build configuration
mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/obj-debug

# Enable debug mode with assertions
ac_add_options --enable-debug

# Package JS shell for testing
export MOZ_PACKAGE_JSSHELL=1
```

### Debug Build - No Optimization (All Platforms)

Debug build with optimizations completely disabled. Useful for debugging but very slow.

```bash
# Debug build with no optimization
mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/obj-debug-noopt

# Enable debug mode
ac_add_options --enable-debug

# Disable optimization completely
ac_add_options --disable-optimize

# Package JS shell
export MOZ_PACKAGE_JSSHELL=1
```

### ASan Optimized Build (Linux/macOS/Windows)

Optimized Address Sanitizer build. Recommended for most ASan testing.

```bash
# ASan optimized build configuration
mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/obj-asan

# Enable Address Sanitizer
ac_add_options --enable-address-sanitizer

# Required by ASan
ac_add_options --disable-jemalloc
ac_add_options --disable-crashreporter
ac_add_options --disable-elf-hack
ac_add_options --disable-profiling

# Keep symbols to symbolize ASan traces
ac_add_options --disable-install-strip

# Line tables only for smaller binaries
ac_add_options --enable-debug-symbols=-gline-tables-only

# Linux only: enable valgrind compatibility
# ac_add_options --enable-valgrind
```

**Platform-specific notes:**
- **Linux**: Add `ac_add_options --enable-valgrind` for valgrind compatibility
- **Windows**: ASan is 64-bit only, uses clang-cl automatically
- **macOS**: No special requirements

### ASan Debug Build (Linux/macOS/Windows)

Debug+opt Address Sanitizer build. Better for debugging ASan findings.

```bash
# ASan debug build configuration
mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/obj-asan-debug

# Enable debug with minimal optimization
ac_add_options --enable-debug
ac_add_options --enable-optimize="-O1"

# Enable Address Sanitizer
ac_add_options --enable-address-sanitizer

# Required by ASan
ac_add_options --disable-jemalloc
ac_add_options --disable-crashreporter
ac_add_options --disable-elf-hack
ac_add_options --disable-profiling

# Keep symbols
ac_add_options --disable-install-strip

# Linux only: enable valgrind and gczeal
# ac_add_options --enable-valgrind
# ac_add_options --enable-gczeal
```

### TSan Build (Linux Only)

Thread Sanitizer build. **TSan is only supported on Linux.**

```bash
# TSan build configuration (Linux only!)
mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/obj-tsan

# Enable Thread Sanitizer
ac_add_options --enable-thread-sanitizer

# Required by TSan
ac_add_options --disable-jemalloc
ac_add_options --disable-crashreporter
ac_add_options --disable-elf-hack
ac_add_options --disable-profiling

# TSan is not compatible with sandboxing
ac_add_options --disable-sandbox

# Keep symbols
ac_add_options --disable-install-strip

# Line tables only
ac_add_options --enable-debug-symbols=-gline-tables-only

# Disable warnings as errors (Rust nightly may have warnings)
ac_add_options --disable-warnings-as-errors

# Required for Rust TSan support
export RUSTFLAGS="-Zsanitizer=thread"

# rustfmt may be missing in Rust nightly
unset RUSTFMT
```

**Important:** TSan requires a special Rust toolchain. Run:
```bash
./mach artifact toolchain --from-build linux64-rust-dev
rm -rf ~/.mozbuild/rustc-sanitizers
mv rustc ~/.mozbuild/rustc-sanitizers
rustup toolchain link gecko-sanitizers ~/.mozbuild/rustc-sanitizers
rustup override set gecko-sanitizers
```

### Non-Unified Build (All Platforms)

Disables unified compilation. Useful for finding hidden dependencies.

```bash
# Non-unified build
mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/obj-non-unified

# Disable unified build
ac_add_options --disable-unified-build

# Usually combined with debug
ac_add_options --enable-debug
```

**Warning:** Non-unified builds are significantly slower to compile.

### Artifact Build (All Platforms)

Downloads pre-built binaries, only builds frontend code. Fastest for frontend development.

```bash
# Artifact build (frontend-only development)
mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/obj-artifact

# Enable artifact builds
ac_add_options --enable-artifact-builds
ac_add_options --enable-artifact-build-symbols
```

**Use `./mach build faster` for artifact builds after initial setup.**

### Code Coverage Build (Linux)

Enables code coverage instrumentation for gcov/llvm-cov.

```bash
# Code coverage build
mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/obj-coverage

# Enable coverage instrumentation
ac_add_options --enable-coverage

# Required for coverage builds
ac_add_options --disable-install-strip
ac_add_options --disable-sandbox
ac_add_options --disable-dmd
ac_add_options --disable-profiling
ac_add_options --disable-warnings-as-errors
ac_add_options --without-wasm-sandboxed-libraries

# Rust coverage flags
export RUSTFLAGS="-Ccodegen-units=1 -Zprofile -Cpanic=abort -Zpanic_abort_tests -Coverflow-checks=off"
export RUSTDOCFLAGS="-Cpanic=abort"
```

### Fuzzing + ASan Build (Linux)

Combined fuzzing and ASan build. Ideal for fuzzing workflows.

```bash
# Fuzzing + ASan build
mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/obj-fuzzing-asan

# Enable fuzzing support
ac_add_options --enable-fuzzing

# Enable Address Sanitizer
ac_add_options --enable-address-sanitizer

# Required by ASan
ac_add_options --disable-jemalloc
ac_add_options --disable-crashreporter
ac_add_options --disable-elf-hack
ac_add_options --disable-profiling

# Keep symbols
ac_add_options --disable-install-strip

# Debug symbols
ac_add_options --enable-debug-symbols=-gline-tables-only

# Enable valgrind (Linux)
ac_add_options --enable-valgrind

# Optional: debug mode for better debugging
# ac_add_options --enable-debug
# ac_add_options --enable-optimize="-O1"
```

### Valgrind Build (Linux)

Optimized for running under Valgrind.

```bash
# Valgrind build
mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/obj-valgrind

# Enable valgrind support
ac_add_options --enable-valgrind

# Required for valgrind
ac_add_options --disable-jemalloc
ac_add_options --disable-install-strip
ac_add_options --disable-dmd
ac_add_options --disable-gtest-in-build
```

---

## 2. ac_add_options Reference

Complete reference of commonly-used `ac_add_options` flags, grouped by category.

### Optimization & Debug

| Option | Description |
|--------|-------------|
| `--enable-debug` | Enable debug build with assertions, debug runtime checks |
| `--disable-debug` | Disable debug mode (default for release builds) |
| `--enable-optimize` | Enable optimizations (default: `-O2` or `-O3`) |
| `--enable-optimize="-O1"` | Enable minimal optimization (good for debug+opt builds) |
| `--enable-optimize="-O2"` | Standard optimization level |
| `--enable-optimize="-O3"` | Aggressive optimization |
| `--disable-optimize` | Disable all optimizations (very slow builds) |
| `--enable-release` | Enable release mode (affects branding and features) |

### Debug Symbols

| Option | Description |
|--------|-------------|
| `--enable-debug-symbols` | Enable debug symbols (default level) |
| `--enable-debug-symbols=-gline-tables-only` | Line tables only (smaller binaries, sufficient for ASan/TSan) |
| `--enable-debug-symbols=-g1` | Minimal debug info |
| `--disable-debug-symbols` | No debug symbols |
| `--disable-install-strip` | Don't strip symbols during install (required for sanitizers) |

### Sanitizers

| Option | Description |
|--------|-------------|
| `--enable-address-sanitizer` | Enable AddressSanitizer (ASan) |
| `--enable-thread-sanitizer` | Enable ThreadSanitizer (TSan, Linux only) |
| `--enable-memory-sanitizer` | Enable MemorySanitizer (MSan, rarely used) |
| `--enable-undefined-sanitizer` | Enable UndefinedBehaviorSanitizer (UBSan) |

**Required with sanitizers:**
- `--disable-jemalloc` (all sanitizers)
- `--disable-crashreporter` (all sanitizers)
- `--disable-elf-hack` (ASan/TSan on Linux)
- `--disable-profiling` (ASan/TSan)
- `--disable-sandbox` (TSan only)

### Fuzzing & Analysis

| Option | Description |
|--------|-------------|
| `--enable-fuzzing` | Enable fuzzing support (libFuzzer) |
| `--enable-coverage` | Enable code coverage instrumentation |
| `--enable-valgrind` | Enable Valgrind support/suppressions |
| `--enable-gczeal` | Enable GC testing modes (useful with debug) |

### Memory & Allocators

| Option | Description |
|--------|-------------|
| `--enable-jemalloc` | Use jemalloc allocator (default) |
| `--disable-jemalloc` | Use system allocator (required for sanitizers) |
| `--enable-dmd` | Enable Dark Matter Detector (leak detection) |
| `--disable-dmd` | Disable DMD |

### Testing

| Option | Description |
|--------|-------------|
| `--enable-tests` | Build test suite (default) |
| `--disable-tests` | Skip building tests |
| `--disable-gtest-in-build` | Don't build gtests (faster builds) |

### Build Mode

| Option | Description |
|--------|-------------|
| `--disable-unified-build` | Disable unified compilation (slower, finds hidden deps) |
| `--enable-artifact-builds` | Download pre-built binaries (frontend-only dev) |
| `--enable-artifact-build-symbols` | Include symbols in artifact builds |
| `--enable-profile-generate` | PGO: generate profile data |
| `--enable-profile-use` | PGO: use profile data |
| `--enable-lto` | Enable Link-Time Optimization |

### Branding & Distribution

| Option | Description |
|--------|-------------|
| `--with-branding=browser/branding/nightly` | Nightly branding |
| `--with-branding=browser/branding/official` | Official release branding |
| `--enable-official-branding` | Use official Firefox branding |

### Cross-compilation

| Option | Description |
|--------|-------------|
| `--target=x86_64-pc-windows-msvc` | Windows 64-bit target |
| `--target=i686-pc-windows-msvc` | Windows 32-bit target |
| `--target=x86_64-apple-darwin` | macOS x86_64 target |
| `--target=aarch64-apple-darwin` | macOS ARM64 target |

### Platform-Specific

| Option | Description |
|--------|-------------|
| `--enable-default-toolkit=cairo-gtk3-x11-wayland` | Linux: X11+Wayland (default) |
| `--enable-default-toolkit=cairo-gtk3-x11-only` | Linux: X11 only |
| `--disable-sandbox` | Disable sandboxing (required for TSan, bad for security) |
| `--disable-crashreporter` | Disable crash reporter (required for sanitizers) |
| `--disable-elf-hack` | Disable ELF optimization (required for ASan on Linux) |
| `--without-wasm-sandboxed-libraries` | Disable WASM sandboxing |

### Miscellaneous

| Option | Description |
|--------|-------------|
| `--enable-warnings-as-errors` | Treat warnings as errors (default in CI) |
| `--disable-warnings-as-errors` | Allow warnings (needed for TSan, coverage) |
| `--enable-js-shell` | Build JavaScript shell |

---

## 3. mk_add_options Reference

Options that affect the build system itself.

| Option | Description |
|--------|-------------|
| `MOZ_OBJDIR=@TOPSRCDIR@/obj-ff-asan` | Set object directory path |
| `MOZ_OBJDIR=@TOPSRCDIR@/../obj-@CONFIG_GUESS@` | Object dir outside source tree |
| `AUTOCLOBBER=1` | Automatically clobber when needed (used in CI) |
| `MOZ_MAKE_FLAGS="-j8"` | Set parallel make jobs (usually auto-detected) |

### Environment Variables (export)

| Variable | Description |
|----------|-------------|
| `MOZ_PACKAGE_JSSHELL=1` | Package JS shell in build output |
| `MOZ_PKG_SPECIAL=asan` | Add suffix to package name |
| `MOZILLA_OFFICIAL=1` | Official build (enables breakpad) |
| `MOZ_TELEMETRY_REPORTING=` | Disable telemetry (empty value) |
| `RUSTFLAGS="-Zsanitizer=address"` | Rust compiler flags (e.g., for ASan) |
| `RUSTFLAGS="-Zsanitizer=thread"` | Rust TSan support |
| `RUSTDOCFLAGS="-Cpanic=abort"` | Rust doc flags |
| `LLVM_SYMBOLIZER=/path/to/llvm-symbolizer` | Path to symbolizer (sanitizers) |

---

## 4. Platform Notes

### Linux x86_64

**Supported configurations:**
- All sanitizers (ASan, TSan, MSan, UBSan)
- All build types
- Valgrind support
- Code coverage
- Fuzzing

**Special considerations:**
- TSan requires custom Rust toolchain (see TSan preset)
- ASan benefits from `--enable-valgrind` flag
- Default toolkit: cairo-gtk3-x11-wayland

### macOS (x86_64 and ARM64)

**Supported configurations:**
- ASan (both architectures)
- Debug, optimized, artifact builds
- Fuzzing + ASan

**NOT supported:**
- TSan (Linux only)
- MSan (Linux only)
- Code coverage (primarily Linux)

**Special considerations:**
- CI builds use cross-compilation from Linux
- Native builds work but cross-builds match CI
- May need to specify SDK: `--with-macos-sdk=/path/to/SDK`
- Content sandbox blocks llvm-symbolizer; set `MOZ_DISABLE_CONTENT_SANDBOX=1` when debugging ASan in content processes

### Windows (x86_64 and x86)

**Supported configurations:**
- ASan (64-bit only)
- Debug, optimized, artifact builds

**NOT supported:**
- TSan (Linux only)
- MSan (Linux only)
- ASan on 32-bit Windows

**Special considerations:**
- Uses clang-cl compiler (MSVC-compatible Clang)
- ASan on Windows requires 64-bit: `--target=x86_64-pc-windows-msvc`
- LeakSanitizer (LSan) not supported on Windows
- First-chance Access Violations in WinDbg are normal with ASan (run `sxi av` to ignore)

### Android

**Special considerations:**
- Uses separate Gradle-based build system
- Build with `./mach gradle` commands
- Mozconfig used but with different options
- Cross-compilation from Linux host

---

## 5. Try Server Mozconfig Directory Map

Layout of `browser/config/mozconfigs/` with key configurations per platform.

### Linux64 (`browser/config/mozconfigs/linux64/`)

**Common presets:**
- `debug` - Standard debug build
- `noopt-debug` - Debug with no optimization
- `debug-asan` - Debug + ASan
- `nightly-asan` - Optimized ASan (nightly)
- `tsan` - Thread Sanitizer
- `code-coverage` - Code coverage instrumentation
- `valgrind` - Valgrind-optimized build
- `debug-fuzzing` - Fuzzing support + debug
- `nightly-fuzzing-asan` - Fuzzing + ASan optimized
- `plain-opt` - Plain optimized build
- `nightly` - Nightly release build

### Win64 (`browser/config/mozconfigs/win64/`)

**Common presets:**
- `debug` - Standard debug build
- `noopt-debug` - Debug with no optimization
- `debug-asan` - Debug + ASan (64-bit only)
- `nightly-asan` - Optimized ASan
- `debug-fuzzing` - Fuzzing support
- `plain-opt` - Plain optimized build
- `nightly` - Nightly release build
- `common-win64` - Base config for all Win64 builds

### macOS64 (`browser/config/mozconfigs/macosx64/`)

**Common presets:**
- `debug` - Standard debug build
- `debug-asan` - Debug + ASan
- `nightly-asan` - Optimized ASan
- `debug-fuzzing` - Fuzzing support
- `cross-noopt-debug` - Cross-compiled debug (from Linux)
- `plain-opt` - Plain optimized build
- `nightly` - Nightly release build

---

## 6. Mozconfig Source Hierarchy

Understanding how mozconfigs include each other. **When flattening for local use, CI-only files should be stripped.**

### Linux Include Chain

```
browser/config/mozconfigs/linux64/debug-asan
├── build/unix/mozconfig.asan
│   └── build/unix/mozconfig.unix
│       └── build/mozconfig.common
│           ├── build/mozconfig.automation (CI only - strip)
│           ├── build/mozconfig.rust
│           └── build/mozconfig.cache (CI only - strip)
└── build/mozconfig.common.override
```

### Windows Include Chain

```
browser/config/mozconfigs/win64/debug-asan
├── build/mozconfig.win-common
├── browser/config/mozconfigs/common (CI only - strip)
├── browser/config/mozconfigs/win64/common-win64
│   └── build/mozconfig.clang-cl
└── build/win64/mozconfig.asan
    └── browser/config/mozconfigs/win64/common-win64 (already included)
└── build/mozconfig.common.override
```

### macOS Include Chain

```
browser/config/mozconfigs/macosx64/debug-asan
├── build/macosx/mozconfig.common
└── build/mozconfig.common
    └── (same as Linux)
```

### Files to Strip for Local Builds

When converting try server configs to local use, **remove or replace** these:

1. **CI fetch paths**: Any reference to `$MOZ_FETCHES_DIR`
2. **Automation files**:
   - `build/mozconfig.automation`
   - `build/mozconfig.cache`
   - `build/mozconfig.common` (contains CI-only exports)
3. **CI exports**:
   - `MOZ_AUTOMATION_*` variables
   - `AUTOCLOBBER=1`
   - `MOZ_PKG_SPECIAL`
   - `MOZ_PACKAGE_JSSHELL` (optional, but CI-specific)
   - `MOZ_INCLUDE_SOURCE_INFO`
4. **API keys**: Any `--with-*-keyfile` options
5. **Branding**: CI-specific branding paths (use local paths)
6. **Sccache**: Cloud sccache configuration

### Safe to Keep

- All `ac_add_options` lines (except keyfiles)
- `RUSTFLAGS` exports
- `unset RUSTFMT`
- Debug/optimization settings
- Sanitizer flags

---

## 7. Common Pitfalls

### Clobber Requirements

**Always clobber when:**
- Switching sanitizers (ASan ↔ TSan ↔ no sanitizer)
- Enabling/disabling unified builds
- Changing optimization levels significantly
- Switching between artifact and full builds
- Adding/removing jemalloc

**Command:** `./mach clobber && ./mach build`

### Incompatible Option Combinations

**Never combine:**
- Sanitizers + jemalloc (always use `--disable-jemalloc` with sanitizers)
- TSan + sandbox (always use `--disable-sandbox` with TSan)
- Artifact builds + source changes to C++/Rust (use `./mach build faster` for frontend only)

**Rarely makes sense:**
- ASan + TSan (use separately)
- MSan + anything else (MSan requires everything to be MSan-instrumented)

### Sanitizer-Specific Issues

**ASan:**
- Requires `-gline-tables-only` or better debug symbols
- On Linux, add `--enable-valgrind` for better compatibility
- On macOS, content processes need `MOZ_DISABLE_CONTENT_SANDBOX=1` to symbolize
- On Windows, only 64-bit is supported
- Disable `--enable-elf-hack` on Linux

**TSan:**
- Linux only
- Requires custom Rust toolchain
- Must disable sandbox
- Requires in-process symbolization (set `TSAN_SYMBOLIZER_PATH`)
- May need to disable GPU acceleration on NVIDIA with proprietary drivers

**Environment variables for symbolization:**
```bash
# ASan
export ASAN_SYMBOLIZER_PATH=/path/to/llvm-symbolizer
export ASAN_OPTIONS=symbolize=1

# TSan (required)
export TSAN_SYMBOLIZER_PATH=/path/to/llvm-symbolizer
```

### Performance Tips

**Faster builds:**
- Use artifact builds for frontend work: `ac_add_options --enable-artifact-builds`
- Use ccache/sccache: `mk_add_options "export CCACHE_DIR=/path/to/cache"`
- Reduce parallelism if running out of memory: `mk_add_options MOZ_MAKE_FLAGS="-j4"`

**Faster linking:**
- Use `mold` linker on Linux (automatically detected)
- Avoid LTO in debug builds (it's slow)

### Debug Symbol Size

**If binaries are too large:**
- Use `-gline-tables-only` instead of full `-g`
- Use `--enable-optimize` (optimized builds are smaller)
- Consider `--disable-debug-symbols` if you don't need them

### Common Errors

**"cannot specify -o when generating multiple output files"**
- Add: `ac_add_options --disable-elf-hack`

**ASan/TSan crashes on startup**
- Check that jemalloc is disabled
- Verify symbolizer is in PATH or set via environment variable
- On TSan+NVIDIA, disable GPU acceleration

**Rust warnings breaking build**
- Add: `ac_add_options --disable-warnings-as-errors`

**Tests failing with sanitizers**
- Some tests are disabled for sanitizers (expected)
- Check for known issues in bug tracker with `[asan]`, `[tsan]` tags

---

## References

**Authoritative sources:**
- `tools/sanitizer/docs/asan.rst` - ASan documentation
- `tools/sanitizer/docs/tsan.rst` - TSan documentation
- `browser/config/mozconfigs/` - All try server configurations
- `build/` - Base mozconfig includes
- Firefox Build Documentation: https://firefox-source-docs.mozilla.org/setup/

**Last updated:** 2026-02-14 (based on mozilla-central)
