# Copy Markdown to Clipboard as Rich Text

Write markdown to a temp file, convert to HTML with pandoc, then copy as rich text:

- **Linux (Wayland)**: `pandoc file.md -f markdown -t html | wl-copy -t text/html`
- **Linux (X11)**: `pandoc file.md -f markdown -t html | xclip -selection clipboard -t text/html -i`
- **macOS**: `pandoc file.md -f markdown -t html -o /tmp/report.html && textutil -convert rtf /tmp/report.html -output /tmp/report.rtf && pbcopy < /tmp/report.rtf`
- **Windows (Git Bash/PowerShell)**: `pandoc file.md -f markdown -t html -o /tmp/report.html` then tell the user to open and copy from the HTML file
