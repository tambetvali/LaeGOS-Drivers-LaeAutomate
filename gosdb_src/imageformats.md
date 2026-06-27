https://github.com/tambetvali/LaeGOS-Drivers-LaeAutomate

SC5N will contain different image formats than SC5:
- Raster format in console mode, such as ansiplus.
- Raster format in md, which contains code block with exact non-colored lines.
- Vector format in delta-enabled format, similar to ones used in cnc or svg, where letters and numbers encode head positioning and movement and use deltas for compression, and ascii visible chars for common support
- Ico format icons will be generated last.

These formats are the initial importance, because GPT models would
access almost all content, and it looks kind of trivial to reader.
