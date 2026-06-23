import os
import re
import requests
from notion_client import Client
from markdownify import markdownify as md

# -----------------------------
# CONFIGURATION
# -----------------------------

NOTION_TOKEN = os.environ.get("NOTION_TOKEN")
OUTPUT_DIR = "docs"
IMAGE_DIR = os.path.join(OUTPUT_DIR, "images")

TITLE_PREFIX = "Laegna"   # filter pages by title prefix

# -----------------------------
# INITIALIZE NOTION CLIENT
# -----------------------------

notion = Client(auth=NOTION_TOKEN)

# -----------------------------
# HELPERS
# -----------------------------

def safe_filename(name: str) -> str:
    name = name.lower()
    name = re.sub(r"[^a-z0-9]+", "_", name)
    return name.strip("_") or "page"


def ensure_dirs():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(IMAGE_DIR, exist_ok=True)


def write_markdown(title: str, content: str):
    ensure_dirs()
    filename = safe_filename(title) + ".md"
    path = os.path.join(OUTPUT_DIR, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print("✓ Exported:", path)


# -----------------------------
# IMAGE HANDLING
# -----------------------------

def download_notion_image(block):
    """Download only Notion-hosted images."""
    file_data = block["image"]

    # Only internal Notion files
    if file_data["type"] != "file":
        return None

    url = file_data["file"]["url"]
    name = file_data["file"]["expiry_time"]  # unique-ish
    ext = ".png"

    # Try to detect extension
    if ".jpg" in url or ".jpeg" in url:
        ext = ".jpg"
    if ".gif" in url:
        ext = ".gif"
    if ".webp" in url:
        ext = ".webp"

    filename = safe_filename(name) + ext
    local_path = os.path.join(IMAGE_DIR, filename)

    # Download
    r = requests.get(url)
    with open(local_path, "wb") as f:
        f.write(r.content)

    print("  → downloaded image:", filename)
    return filename


# -----------------------------
# BLOCK → MARKDOWN
# -----------------------------

def block_to_md(block):
    t = block["type"]

    # IMAGE BLOCK
    if t == "image":
        local_name = download_notion_image(block)
        if local_name:
            return f"![image](images/{local_name})\n\n"
        return ""

    # TEXT BLOCKS
    if t == "paragraph":
        text = block[t].get("rich_text", [])
        return "".join(rt.get("plain_text", "") for rt in text) + "\n\n"

    if t == "heading_1":
        return "# " + "".join(rt["plain_text"] for rt in block[t]["rich_text"]) + "\n\n"

    if t == "heading_2":
        return "## " + "".join(rt["plain_text"] for rt in block[t]["rich_text"]) + "\n\n"

    if t == "heading_3":
        return "### " + "".join(rt["plain_text"] for rt in block[t]["rich_text"]) + "\n\n"

    if t == "bulleted_list_item":
        return "- " + "".join(rt["plain_text"] for rt in block[t]["rich_text"]) + "\n"

    if t == "numbered_list_item":
        return "1. " + "".join(rt["plain_text"] for rt in block[t]["rich_text"]) + "\n"

    if t == "quote":
        return "> " + "".join(rt["plain_text"] for rt in block[t]["rich_text"]) + "\n\n"

    if t == "code":
        lang = block[t].get("language", "")
        code = "".join(rt["plain_text"] for rt in block[t]["rich_text"])
        return f"```{lang}\n{code}\n```\n\n"

    # FALLBACK
    if "rich_text" in block[t]:
        html = "".join(rt.get("plain_text", "") for rt in block[t]["rich_text"])
        return md(html) + "\n"

    return ""


# -----------------------------
# RECURSIVE BLOCK WALKER
# -----------------------------

def export_blocks(block_id):
    md_output = ""
    children = notion.blocks.children.list(block_id=block_id)

    for block in children["results"]:
        md_output += block_to_md(block)

        if block.get("has_children"):
            md_output += export_blocks(block["id"])

    return md_output


# -----------------------------
# EXPORT A SINGLE PAGE
# -----------------------------

def export_page(page):
    title_prop = page["properties"].get("title")
    if not title_prop or not title_prop["title"]:
        return

    title = title_prop["title"][0]["plain_text"]

    print(f"\n=== Exporting page: {title} ===")

    md_content = f"# {title}\n\n"
    md_content += export_blocks(page["id"])

    write_markdown(title, md_content)


# -----------------------------
# WORKSPACE SEARCH EXPORT
# -----------------------------

def export_workspace():
    print("Searching workspace…")

    results = notion.search(
        query=TITLE_PREFIX,
        filter={"value": "page", "property": "object"}
    )

    pages = results["results"]

    print(f"Found {len(pages)} pages matching prefix '{TITLE_PREFIX}'")

    for page in pages:
        export_page(page)


# -----------------------------
# MAIN
# -----------------------------

if __name__ == "__main__":
    print("Starting workspace export with images…")
    export_workspace()
    print("\nAll pages and images exported into:", OUTPUT_DIR)
