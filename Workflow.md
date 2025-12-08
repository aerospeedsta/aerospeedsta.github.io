# Publishing Workflow: Obsidian to Hugo

This guide outlines the process for bringing your Obsidian blog posts into your Hugo website, ensuring tags, links, and math render correctly.

## 1. Writing in Obsidian

Write your posts normally in Obsidian.
- **Wikilinks**: Use `[[tag-name]]` for tags or internal links. These will be automatically converted to colored tag links.
    - Example: `This is a post about [[machine-learning]].`
- **Math/LaTeX**: Use Standard LaTeX syntax.
    - Inline: `$E=mc^2$`
    - Block: `$$ \int x dx $$`
- **Images**: Use standard markdown image syntax `![Alt Text](image.png)`.

## 2. Moving Content to Hugo

1.  **Copy the File**:
    - Copy your `.md` file from your Obsidian vault to the website folder: `aerospeedsta.dev/content/posts/`.
    - *Tip*: You can drag and drop headers or files if you have the folders open side-by-side.

2.  **Move Images**:
    - If your post has images, move the image files to `aerospeedsta.dev/static/images/`.
    - Update the image link in your markdown file to: `![Alt Text](/images/your-image.png)`. Note the leading slash!

## 3. Frontmatter Check

Ensure your markdown file starts with valid Hugo Frontmatter (YAML). It should look like this:

```yaml
---
title: "My New Post"
date: 2025-12-09
summary: "A brief summary for the dashboard."
tags: ["some-tag"]
---
```

## 4. Automatic Tag Syncing (The Magic Script)

Your Obsidian posts likely use `[[wikilinks]]` in the body that aren't in the frontmatter `tags` list yet. To fix this automatically:

1.  Open your terminal/command prompt.
2.  Navigate to your site folder: `cd /path/to/aerospeedsta.dev`.
3.  Run the Auto-Tagger script:

    ```bash
    python3 scripts/auto_tag.py
    ```

    **What this does**:
    - Scans all posts for `[[tag-name]]`.
    - Adds any missing tags to the `tags: [...]` list in the frontmatter.
    - Use `hugo server` to see the new tag pages generated automatically!

## 5. Grouping New Tags (Optional)

By default, new tags appear as **Gray** and listed under "General / Uncategorized" on the `/tags/` page. To assign them a color and group (e.g., "Robotics", "ML"):

1.  Open `hugo.yaml`.
2.  Find the `tagGroups` section.
3.  Add your new tag slug to the `match` list of the desired group.

```yaml
  tagGroups:
    ML:
      color: "#60A5FA"
      match: ["machine-learning", "new-tag-here"] # <--- Add here
```

If you want a **New Group**:
1.  Add a new block in `hugo.yaml`:

```yaml
    MyNewGroup:
      color: "#FF5733" # Your custom hex color
      match: ["my-new-tag"]
```

## 6. Verification

1.  Run `hugo server` (if not already running).
2.  Visit `http://localhost:1313/posts/your-post/`.
3.  Check:
    - **Tags**: Are they clickable and colored? (Green/Blue if grouped, Gray if new).
    - **Math**: Do equations render correctly?
    - **Images**: Do they appear?

## troubleshooting

- **Link is Gray**: Run `python3 scripts/auto_tag.py` and restart `hugo server`.
- **Math looks like code**: Ensure you haven't wrapped the math in backticks (`` ` ``). It should be plain `$`.

## Advanced Layouts: Side-by-Side Images & Auto-Numbering
I enabled **Automatic Figure Numbering**! You don't need to manually type "Figure 1".
Just use the standard HTML `<figure>` tag.

### Side-by-Side Example (with Auto-Numbering)
Paste this into your markdown:

```html
<div style="display: flex; gap: 20px; align-items: end;">
  <!-- Image 1 -->
  <figure style="flex: 1; margin: 0;">
    <img src="/images/image1.png" alt="Alt Text" style="width: 100%; border-radius: 8px;">
    <figcaption>Description of first image</figcaption>
  </figure>

  <!-- Image 2 -->
  <figure style="flex: 1; margin: 0;">
    <img src="/images/image2.png" alt="Alt Text" style="width: 100%; border-radius: 8px;">
    <figcaption>Description of second image</figcaption>
  </figure>
</div>
```

The site will automatically render labels like **Figure 1: Description...**, **Figure 2: Description...**.
