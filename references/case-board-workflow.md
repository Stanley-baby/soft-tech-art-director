# Case Board Workflow

Use this after reference confirmation to create a human-readable decision record and the first visible part of the Visual Direction Pack before Style Proof generation.

## Goal

Summarize selected images in a task-specific visual overview. Keep the board image-heavy; store interpretation in separate Reference Notes. The Case Board is not a generation input. Deliver it immediately with Visual Rules and Draft Implementation Tokens so image-generation latency does not block useful output.

## Select references by role

Select three or four references. Use atomic crops when available rather than complete Style Card collages.

| User-facing task | Internal role | Default weight | Controls |
| --- | --- | ---: | --- |
| 找核心画面 | Hero Material | 40% | Main form, surface, texture, depth, light behavior |
| 找喜欢的页面结构 | Composition | 25% | Scale, placement, crop, whitespace, density |
| 找喜欢的配色 | Color | 20% | Background, palette, accent, gradient, contrast |
| 找喜欢的文字布局 | Typography | 15% | Type voice, hierarchy, alignment, labels, numbers |
| 找喜欢的操作方式（按需） | Interaction & Data | variable | Controls, data density, states, borders, product credibility |

Weights are only human-facing emphasis cues and are not executable model controls. Prefer labels such as `PRIMARY`, `SUPPORTING`, and `CONSTRAINT` in the Reference Contract. Keep the board to three or four tiles; an optional interaction reference must replace or merge another role.

## Selection constraints

- Use references that fit the product and chosen provisional route; allow them to refine the final Style Profile.
- Give each image one role; never label a reference `overall style`.
- Prefer different roles over several visually similar images.
- Do not use rejected references as visual inputs; convert rejection into text exclusions.
- Crop out logos, irrelevant copy, and unrelated components when practical.
- Record a stable Reference ID from the index.
- For every reference, write one concise `Borrow` instruction and one `Do not inherit` instruction in separate Reference Notes, not on the visual board.

## Assemble the board

When local image files and Python are available, create a JSON spec and run the dependency-free SVG builder:

```bash
python3 scripts/build_case_board.py --spec case-board.json --output case-board.svg
```

Example spec:

```json
{
  "title": "ENERGY JOURNAL · CASE BOARD",
  "subtitle": "Quiet Generative Perception",
  "references": [
    {
      "id": "GP-M03",
      "path": "/absolute/path/GP-M03.jpg",
      "role": "CORE VISUAL · HERO MATERIAL",
      "weight": 45,
      "borrow": "Asymmetric living volume and internal density",
      "avoid": "Do not inherit spiritual glow or original palette"
    },
    {
      "id": "QI-L02",
      "path": "/absolute/path/QI-L02.jpg",
      "role": "PAGE STRUCTURE · COMPOSITION",
      "weight": 30,
      "borrow": "Restrained central focus and editorial whitespace",
      "avoid": "Do not inherit medical-dashboard styling"
    },
    {
      "id": "QG-T01",
      "path": "/absolute/path/QG-T01.jpg",
      "role": "COLOR & TYPE · TYPE & COLOR",
      "weight": 25,
      "borrow": "Calm neutral typography and controlled color field",
      "avoid": "Do not inherit brand copy or gradient buttons"
    }
  ]
}
```

The generated board should devote at least 85% of its content area to reference images. Show only role, Reference ID, and optional human-facing emphasis beneath each tile. Output `Borrow` and `Do not inherit` separately as a table. The builder uses only the Python standard library; never install Pillow or another package for this step.

If the toolchain is unavailable, output the selected images individually plus a Reference Notes table.

Run environment checks silently. Do not mention Pillow, Python packages, commands, or fallbacks to the user unless Case Board creation actually fails and no in-scope alternative works. Case Board creation must not interrupt the design journey.

## Bind the prompt to the board

Never attach the merged Case Board as the default image-generation input. Attach the original atomic references separately and start Style Proof prompts with this contract, adapted to the actual references:

> Use the attached original reference images as a role-based visual system. Keep every image separate: Reference A controls only material and silhouette. Reference B controls only scale, placement, and whitespace. Reference C controls only typography and color restraint. Reference D controls only interaction and data density. Do not inherit logos, copy, proprietary brand identity, or unrelated interface structures. The merged Case Board is only a human-facing decision record and must not be used as the generation input.

Then describe the product, target surface, hierarchy, exact visual behavior, and internal exclusions. Do not rely on the board's small crops.

## Route the output

- For a bitmap key visual: generate the core visual asset without interface text first.
- For a finished interface: generate the visual asset separately, then implement typography, grid, spacing, and controls in Figma, HTML/CSS, or code.
- For platforms that accept only one image: attach the strongest original reference and express secondary roles in text; do not attach the merged board.
- For platforms that accept several images with reference roles: attach atomic tiles and preserve the same role contract.

## Review

After generation, compare the result role by role:

1. Did material follow Hero Material rather than a generic genre trope?
2. Did composition preserve the intended scale and whitespace?
3. Did typography and color remain restrained?
4. Did interaction look implementable rather than like concept art?
5. Did any `Do not inherit` feature leak into the result?

If two or more checks fail, revise the reference set or crops before adding more adjectives to the prompt.
