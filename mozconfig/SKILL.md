---
name: mozconfig
description: Generate or modify Firefox mozconfig build configuration files. Use when the user asks to create a mozconfig, configure a build, set up ASan/TSan/debug builds, or match try server configurations.
argument-hint: "[preset-name or description]"
---

# Mozconfig Skill

This skill generates correct, complete Firefox mozconfig files for various build configurations. Mozconfigs control build options like debug mode, sanitizers (ASan/TSan), optimization levels, and more.

## When to Use This Skill

Use this skill when the user:
- Asks to create a mozconfig file
- Wants to set up a specific build configuration (debug, ASan, TSan, etc.)
- Wants to replicate a try server or CI build configuration locally
- Needs help configuring Firefox builds
- Mentions build types like "ASan build", "debug build", "fuzzing build", etc.

## What You Will Do

Follow these steps in order. This skill is **interactive** - use `AskUserQuestion` to gather requirements and preferences from the user.

---

## Step 1: Detect Platform

**Detect the user's operating system and architecture.**

1. Run these commands to detect the platform:
   ```bash
   uname -s  # Operating system
   uname -m  # Architecture
   ```

2. Map the results:
   - Linux + x86_64 → **linux64** (all configs supported)
   - Darwin + x86_64 → **macosx64** (no TSan)
   - Darwin + arm64 → **macosx64-aarch64** (no TSan)
   - MINGW*/MSYS*/CYGWIN* + x86_64 → **win64** (ASan 64-bit only, no TSan)

3. **Report to user**: Tell them what platform was detected and any limitations:
   - Linux: All configurations supported
   - macOS: TSan not supported
   - Windows: ASan 64-bit only, TSan not supported

4. Note any special platform constraints for later steps.

---

## Step 2: Determine Configuration Mode

**Ask the user how they want to configure their build.**

Use `AskUserQuestion` to present three options:

```
Question: "How would you like to configure your Firefox build?"
Header: "Config mode"
Options:
  1. "Common preset" - "Pre-built configurations for common use cases (debug, ASan, TSan, etc.)"
  2. "Try server match" - "Replicate a CI/try server configuration locally"
  3. "Custom configuration" - "Interactive guided configuration for specific needs"
```

Based on their choice, proceed to **Step 3A**, **Step 3B**, or **Step 3C**.

---

## Step 3A: Preset Mode

**For users who selected "Common preset".**

### Present Platform-Appropriate Presets

Use `AskUserQuestion` to show available presets. **Filter by platform** - don't show TSan on macOS/Windows, for example.

```
Question: "Which preset configuration do you want?"
Header: "Build preset"
Options (filter by platform):
  1. "Debug" - "Standard debug build with assertions and symbols"
  2. "Debug (no optimization)" - "Debug build with --disable-optimize (very slow but best for debugging)"
  3. "ASan optimized" - "Address Sanitizer with optimization (recommended for testing)"
  4. "ASan debug" - "Address Sanitizer with debug mode (better for debugging ASan findings)"
  5. "TSan" - "Thread Sanitizer (Linux only)" [only show on Linux]
  6. "Non-unified build" - "Disable unified compilation (slower build, finds hidden dependencies)"
  7. "Artifact build" - "Frontend-only development (downloads pre-built C++/Rust)"
  8. "Code coverage" - "Instrumented build for code coverage analysis (Linux)" [only show on Linux]
  9. "Fuzzing + ASan" - "Combined fuzzing and ASan support (for fuzzing workflows)"
  10. "Valgrind" - "Optimized for running under Valgrind (Linux)" [only show on Linux]
```

### Generate Mozconfig from Preset

1. **Read the reference file**: Open `.claude/skills/mozconfig/references/build-options-reference.md`

2. **Find the preset section**: Look for the preset they selected in section "1. Preset Mozconfigs"

3. **Extract the mozconfig**: Copy the complete mozconfig for that preset

4. **Apply platform-specific adjustments**:
   - For ASan on Linux, uncomment the `--enable-valgrind` line
   - For ASan debug on Linux, uncomment `--enable-valgrind` and `--enable-gczeal`
   - Ensure Windows configs don't have Linux-only options
   - Ensure macOS configs have appropriate SDK if needed

5. **Proceed to Step 4** to write the file.

---

## Step 3B: Try Server Match Mode

**For users who selected "Try server match".**

### Ask Which Try Configuration to Match

Use `AskUserQuestion` to determine the target configuration:

```
Question: "Which try server configuration do you want to replicate?"
Header: "Target platform"
Options:
  1. "Current machine" - "Match a try config for my detected platform (recommended)"
  2. "linux64" - "Linux 64-bit configuration"
  3. "win64" - "Windows 64-bit configuration"
  4. "macosx64" - "macOS x86_64 configuration"
  5. "macosx64-aarch64" - "macOS ARM64 configuration"
```

Then ask for build type:

```
Question: "Which build type from try server?"
Header: "Build type"
Options (examples, adjust based on platform):
  1. "debug" - "Standard debug build"
  2. "debug-asan" - "Debug with Address Sanitizer"
  3. "nightly-asan" - "Optimized Address Sanitizer build"
  4. "tsan" - "Thread Sanitizer (Linux only)"
  5. "code-coverage" - "Code coverage instrumentation"
  6. "debug-fuzzing" - "Debug with fuzzing support"
  7. "nightly" - "Nightly release configuration"
  8. "plain-opt" - "Plain optimized build"
```

### Resolve and Flatten the Mozconfig

Now you need to read and flatten the try server mozconfig files.

1. **Start with the base file**: Read `browser/config/mozconfigs/<platform>/<type>`
   - Example: `browser/config/mozconfigs/linux64/debug-asan`

2. **Follow all includes recursively**: When you see `. $topsrcdir/path/to/file` or `. "$topsrcdir/path/to/file"`, read that file too

3. **Build a complete mozconfig** by concatenating all the files in order

4. **Strip CI-only lines**: Remove lines that reference:
   - `$MOZ_FETCHES_DIR` (CI artifact fetches)
   - `$topsrcdir/browser/config/mozconfigs/common` (CI-only base)
   - `$topsrcdir/build/mozconfig.common` (contains CI exports)
   - `$topsrcdir/build/mozconfig.automation` (CI-only)
   - `$topsrcdir/build/mozconfig.cache` (CI-only)
   - `$topsrcdir/build/mozconfig.common.override` (CI-only)
   - `AUTOCLOBBER=1` (CI auto-clobber)
   - `MOZ_AUTOMATION_*` exports
   - `MOZ_PKG_SPECIAL` exports (optional)
   - `MOZ_PACKAGE_JSSHELL` (optional, but CI-specific)
   - `MOZ_INCLUDE_SOURCE_INFO` (CI-only)
   - `MOZILLA_OFFICIAL=1` (CI-only)
   - API keyfile paths (`--with-*-keyfile`)
   - Branding paths referencing automation
   - Lines setting `LLVM_SYMBOLIZER` to `$MOZ_FETCHES_DIR` paths
   - Sccache cloud configuration

5. **Keep important lines**:
   - All `ac_add_options` (except keyfiles and automation paths)
   - `RUSTFLAGS` exports
   - `unset RUSTFMT`
   - Debug/optimization settings
   - Sanitizer configuration

6. **Replace CI paths with local equivalents**:
   - Instead of `$MOZ_FETCHES_DIR/llvm-symbolizer/bin/llvm-symbolizer`, use a comment suggesting to set `ASAN_SYMBOLIZER_PATH` or `TSAN_SYMBOLIZER_PATH` environment variable

7. **Add helpful comments**: Explain what each section does

8. **Proceed to Step 4** to write the file.

---

## Step 3C: Custom Mode

**For users who selected "Custom configuration".**

### Guide User Through Configuration Options

Use `AskUserQuestion` iteratively to build the configuration. **Read the reference file first** to understand available options.

#### Question 1: Optimization Level

```
Question: "What optimization level do you want?"
Header: "Optimization"
Options:
  1. "Default optimization" - "Standard -O2/-O3 (fast, production-like)"
  2. "Minimal optimization (-O1)" - "Useful for debug+opt builds"
  3. "No optimization" - "Slowest, but easiest to debug"
```

#### Question 2: Debug Mode

```
Question: "Enable debug mode with assertions?"
Header: "Debug mode"
Options:
  1. "Yes" - "Enable debug assertions and runtime checks"
  2. "No" - "Optimized build without debug checks"
```

#### Question 3: Debug Symbols

```
Question: "What level of debug symbols?"
Header: "Debug symbols"
Options:
  1. "Line tables only" - "Minimal symbols (smaller binaries, good for sanitizers)"
  2. "Default symbols" - "Standard debug symbols"
  3. "Full symbols (-g)" - "Maximum debug info (large binaries)"
  4. "No symbols" - "Strip all debug symbols"
```

#### Question 4: Sanitizer

```
Question: "Which sanitizer (if any)?"
Header: "Sanitizer"
Options:
  1. "None" - "No sanitizer"
  2. "ASan" - "Address Sanitizer (memory errors)"
  3. "TSan" - "Thread Sanitizer (data races, Linux only)" [only on Linux]
  4. "MSan" - "Memory Sanitizer (uninitialized memory, rarely used)"
  5. "UBSan" - "Undefined Behavior Sanitizer"
```

**If ASan or TSan is selected**, automatically add required options:
- `--disable-jemalloc`
- `--disable-crashreporter`
- `--disable-elf-hack` (Linux)
- `--disable-profiling`
- `--disable-install-strip`

**If TSan is selected**, also add:
- `--disable-sandbox`
- `export RUSTFLAGS="-Zsanitizer=thread"`
- `unset RUSTFMT`
- `--disable-warnings-as-errors`

#### Question 5: Additional Features

Allow multiple selections:

```
Question: "Select any additional features you need:"
Header: "Features"
Multi-select: true
Options:
  1. "Fuzzing support" - "Enable libFuzzer integration"
  2. "Code coverage" - "Enable coverage instrumentation"
  3. "Valgrind support" - "Valgrind compatibility (Linux)"
  4. "Disable unified build" - "Build files separately (slower, finds hidden deps)"
  5. "Artifact build mode" - "Download pre-built binaries (frontend-only)"
```

### Assemble the Mozconfig

Based on all answers:

1. **Start with MOZ_OBJDIR**: Generate an appropriate object directory name based on the config
   - Example: `obj-debug`, `obj-asan`, `obj-tsan`, `obj-debug-asan`

2. **Add optimization flags** based on Question 1

3. **Add debug flags** based on Question 2

4. **Add debug symbol flags** based on Question 3

5. **Add sanitizer flags and required options** based on Question 4
   - Use the reference file section "2. ac_add_options Reference" → "Sanitizers"

6. **Add feature flags** based on Question 5

7. **Add platform-specific options**:
   - Linux with ASan: consider adding `--enable-valgrind`
   - TSan: ensure all TSan requirements are present

8. **Add helpful comments** explaining each section

9. **Proceed to Step 4** to write the file.

---

## Step 4: Generate and Write Mozconfig

**Final step: create the mozconfig file with user confirmation.**

### Prepare the Mozconfig Content

1. **Add a header comment** to the generated mozconfig:
   ```bash
   # Firefox mozconfig
   # Generated by Claude Code mozconfig skill
   # Configuration: [describe the config - e.g., "Debug + ASan optimized build"]
   # Platform: [detected platform]
   # Generated: [current date]
   ```

2. **Organize the content into commented sections**:
   - Object directory
   - Optimization settings
   - Debug settings
   - Sanitizer configuration
   - Additional features
   - Platform-specific settings
   - Environment variables

3. **Add usage notes at the end** as comments:
   ```bash
   # Build instructions:
   # 1. Save this file as 'mozconfig' in your mozilla-central directory
   # 2. Run: ./mach clobber && ./mach build
   # 3. Run Firefox: ./mach run
   #
   # [Add sanitizer-specific notes if applicable]
   ```

### Ask Where to Write

Use `AskUserQuestion`:

```
Question: "Where should I save the mozconfig file?"
Header: "Output path"
Options:
  1. "./mozconfig (recommended)" - "Standard location in repository root"
  2. "./mozconfig-[configname]" - "Named config file (e.g., mozconfig-asan)"
  3. "Custom path" - "Specify a different location"
```

### Check for Existing File

If the file already exists:

1. **Read the existing mozconfig**

2. **Show a diff**: Display what would change (you can describe the changes textually)

3. **Ask for confirmation**:
   ```
   Question: "A mozconfig already exists. How should I proceed?"
   Header: "File exists"
   Options:
     1. "Overwrite" - "Replace the existing mozconfig"
     2. "Write to different path" - "Save with a different name"
     3. "Cancel" - "Don't write the file"
   ```

### Write the File

1. **Write the mozconfig** to the chosen path using the Write tool

2. **Confirm to user**: Report success with the path

### Important Warnings

After writing, **always warn the user** about:

1. **Clobber requirement**:
   ```
   ⚠️  Important: Run `./mach clobber && ./mach build` after creating or changing your mozconfig.
   ```

2. **Sanitizer-specific warnings** if applicable:

   **For ASan:**
   ```
   ASan Notes:
   - Set ASAN_SYMBOLIZER_PATH environment variable to your llvm-symbolizer location
   - On macOS, set MOZ_DISABLE_CONTENT_SANDBOX=1 to symbolize content process crashes
   ```

   **For TSan:**
   ```
   TSan Notes:
   - TSan requires a special Rust toolchain. Run:
     ./mach artifact toolchain --from-build linux64-rust-dev
     rm -rf ~/.mozbuild/rustc-sanitizers
     mv rustc ~/.mozbuild/rustc-sanitizers
     rustup toolchain link gecko-sanitizers ~/.mozbuild/rustc-sanitizers
     rustup override set gecko-sanitizers
   - Set TSAN_SYMBOLIZER_PATH to your llvm-symbolizer location (required)
   - On NVIDIA with proprietary drivers, you may need to disable GPU acceleration
   ```

3. **Build time estimate** if appropriate:
   - Artifact builds: "Very fast (minutes)"
   - Optimized builds: "Moderate (15-30 minutes typical)"
   - Debug builds: "Moderate (15-30 minutes typical)"
   - Non-unified builds: "Very slow (can be hours)"
   - Sanitizer builds: "Moderate to slow (20-40 minutes typical)"

### Offer MOZ_OBJDIR Customization

Ask if they want to customize the object directory name:

```
Question: "The object directory is set to [current value]. Would you like to change it?"
Header: "Object dir"
Options:
  1. "Keep default" - "Use [current value]"
  2. "Use config-based name" - "Use a name based on the config (e.g., obj-asan)"
  3. "Custom name" - "Specify a custom object directory name"
```

If they choose option 2, suggest names like:
- Debug: `obj-debug`
- ASan: `obj-asan`
- TSan: `obj-tsan`
- Debug+ASan: `obj-debug-asan`
- Artifact: `obj-artifact`

---

## Step 5: Summary and Next Steps

**Provide a clear summary of what was created.**

Tell the user:

1. ✅ **What was created**: "Created [config type] mozconfig at [path]"

2. **Next steps**:
   ```
   Next steps:
   1. Run: ./mach clobber && ./mach build
   2. After build completes: ./mach run
   3. [If sanitizer: Set environment variables as noted above]
   ```

3. **Offer additional help**:
   ```
   Need help?
   - Modify the mozconfig file directly to adjust options
   - Run /mozconfig again to create a different configuration
   - Check .claude/skills/mozconfig/references/build-options-reference.md for all options
   ```

---

## Reference Files

This skill uses the following reference files:

- `.claude/skills/mozconfig/references/build-options-reference.md` - Comprehensive reference of all mozconfig options, presets, and platform notes

**Always read the reference file** when you need to:
- Look up preset mozconfigs
- Understand what options are available
- Check platform-specific constraints
- Generate custom configurations

---

## Error Handling

If something goes wrong:

- **File read errors**: Gracefully explain that the try server config couldn't be read and suggest using a preset instead
- **Invalid options**: Warn the user and offer to use a safe default
- **Platform incompatibility**: Clearly explain why an option isn't available (e.g., "TSan is only supported on Linux")

---

## Additional Notes

- **Always be helpful**: If the user is uncertain, guide them toward common, safe configurations
- **Explain trade-offs**: When presenting options, help them understand the implications (speed vs. debuggability, etc.)
- **Validate combinations**: Don't allow incompatible options (e.g., jemalloc + sanitizers)
- **Use the reference**: The reference file is comprehensive - trust it and use it
- **Platform matters**: Always respect platform limitations

---

## Success Criteria

You've successfully completed this skill when:

1. ✅ User's platform is detected
2. ✅ Configuration mode is selected
3. ✅ Mozconfig is generated based on their choices
4. ✅ File is written to their chosen location
5. ✅ User is given clear next steps and warnings
6. ✅ User understands what was created and how to use it
