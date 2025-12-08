import os
import re
import glob

# Configuration
CONTENT_DIR = "content"
TAG_REGEX = r"\[\[([a-zA-Z0-9\s\-_]+)\]\]"

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split Frontmatter and Content
    parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
    
    if len(parts) < 3:
        return

    frontmatter_raw = parts[1]
    body = parts[2]

    # Find matches in body
    found_tags = set(re.findall(TAG_REGEX, body))
    if not found_tags:
        return 

    # Clean tags found in regex
    # Hugo urlizes tags in URLs but preserves them in titles. 
    # We should probably lowercase or hyphenate for the "tag name" 
    # to match what the wikilink usually implies (linking to /tags/slug).
    # Ideally, we keep the user's intent. "Space Travel" -> "Space-Travel" or "space-travel"?
    # For now, let's use a simple slugify.
    clean_tags = set()
    for t in found_tags:
        # Simple slugify: lowercase, space to hyphen
        slug = t.strip().lower().replace(' ', '-')
        clean_tags.add(slug)

    # Parse existing tags from frontmatter using Regex
    # Looking for: tags: ["a", "b"] or tags: \n - a \n - b
    # Let's support the likely inline format first: tags: ["a", "b"]
    
    tags_line_match = re.search(r'^tags:\s*\[(.*?)\]', frontmatter_raw, re.MULTILINE)
    current_tags = set()
    
    if tags_line_match:
        # Parse inline list
        raw_list = tags_line_match.group(1)
        # simplistic split by comma and quote stripping
        for item in raw_list.split(','):
            cleaned = item.strip().strip('"').strip("'")
            if cleaned:
                current_tags.add(cleaned)
    else:
        # Check for multiline list format? For now assume empty or inline.
        # If no tags line, we will append it.
        pass

    new_tags = clean_tags - current_tags

    if not new_tags:
        return 

    print(f"[{filepath}] Adding tags: {new_tags}")
    
    # Update Frontmatter
    updated_current_tags = sorted(list(current_tags.union(new_tags)))
    formatted_tags = 'tags: [' + ', '.join(f'"{t}"' for t in updated_current_tags) + ']'
    
    if tags_line_match:
        # Replace existing line
        new_frontmatter = frontmatter_raw.replace(tags_line_match.group(0), formatted_tags)
    else:
        # Append to end of frontmatter
        new_frontmatter = frontmatter_raw.strip() + '\n' + formatted_tags + '\n'

    new_content = f"---\n{new_frontmatter}\n---{body}"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    print("Scanning content for new [[wikilinks]]...")
    files = glob.glob(f"{CONTENT_DIR}/**/*.md", recursive=True)
    for f in files:
        process_file(f)
    print("Done.")

if __name__ == "__main__":
    main()
