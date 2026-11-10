# Keyframe Reference Journey

Use this after the user chooses one of the three provisional Style Routes and before Style Proof. Keep the visible experience to `Search → Upload → Reference Contract`.

## 1. Infer the frame goal

Infer the page, user moment, primary information, AI state, and memorable visual from the Product Expression, Visual Coordinates, chosen provisional route, and conversation. Present one sentence for lightweight confirmation. Do not invent final tokens or reopen product-positioning questions unless ambiguity changes the output.

## 2. Produce four simple search tasks

Use plain language with beginners. Keep the professional role internal.

| User-facing task | Internal role | What it controls |
| --- | --- | --- |
| 找核心画面 | Hero Material | Main form, surface, texture, depth, and light |
| 找喜欢的页面结构 | Composition | Scale, placement, hierarchy, whitespace, and density |
| 找喜欢的配色 | Color | Background, dominant colors, accents, gradient, and contrast |
| 找喜欢的文字布局 | Typography | Type voice, size contrast, alignment, labels, and numbers |
| 找喜欢的操作方式（按需） | Interaction & Data | Controls, states, data density, and product credibility |

Do not show terms such as `Composition` unless the user asks for the design vocabulary.

For each task output:

1. `你要找什么`: one concrete sentence.
2. `重点看`: three to five visible signals.
3. `不用管`: content, brand, color, or another dimension outside this task.
4. `搜索词`: two to four English queries and one or two Chinese queries derived from the Style Profile.
5. `去这里找`: direct links when stable and copyable queries otherwise.
6. `请保存`: one to three images, normally two.

### Search Kit output contract

Make search access frictionless. This is a required display format:

- Give every English Pinterest query its own clickable Markdown link.
- Put the exact query in the link label so the user can judge it before opening.
- URL-encode the complete query in the destination. Never output only `Pinterest: query`.
- Show two or three high-signal Pinterest links per task, followed by at most two secondary-platform links.
- Keep Chinese queries as copyable text unless a verified Chinese-language deep link is available.

Use this exact pattern:

```markdown
- [Pinterest · generative geometry light installation](https://www.pinterest.com/search/pins/?q=generative%20geometry%20light%20installation)
- [Pinterest · scientific editorial web design](https://www.pinterest.com/search/pins/?q=scientific%20editorial%20web%20design)
```

Before sending, verify that every Pinterest destination contains `/search/pins/?q=` and a non-empty encoded query. If the current platform cannot render Markdown links, show the complete URL immediately after its query instead of omitting it.

## 3. Match platforms to the task

- Pinterest: material, color, typography, visual metaphor, and cross-domain inspiration. Build a separate direct query URL for every recommended query as `https://www.pinterest.com/search/pins/?q=<URL-ENCODED QUERY>`.
- Cosmos: restrained editorial, art, brand, and cross-domain references. Provide the current platform link plus copyable keywords.
- Variant: contemporary digital, experimental, and product aesthetics. Provide the current platform link plus copyable keywords.
- Mobbin: real interface structure, screen patterns, hierarchy, and interaction. Prefer a current screen-pattern or UI-element page over a vague keyword link.

Verify current platform and deep links when web access is available. If a stable deep link cannot be verified, link the platform home and provide the exact query to paste. Never imply that every platform is equally good for every task.

## 4. Receive and critique

Let the user upload all images without explaining them. Preserve filenames as Reference IDs and infer the likely task. For every image output:

- Plain-language task
- `Borrow`: the single most transferable rule
- `Do not inherit`: the strongest contamination risk
- `Keep`, `Replace`, or `Partial`

Select one primary image per required task. Keep the final board to three or four tiles; when interaction is essential, replace or merge the least relevant visual role rather than creating a fifth tile. Ask one combined confirmation: keep the proposed set or name the image to replace.

## 5. Build the Reference Contract

After confirmation:

1. Translate the plain-language tasks to professional roles.
2. Select one or two Primary References. Mark remaining images as Supporting or Constraint References; do not present percentages as model controls.
3. Write one short `Borrow` and `Do not inherit` rule per image.
4. Create the visual-heavy Case Board as a human decision record only.
5. Keep each original image available as a separate atomic input for Style Proof generation.
6. Hand the Reference Contract and original images to [style-proof-workflow.md](style-proof-workflow.md), which first produces Visual Rules and Draft Tokens, then generates the Style Proof.

If an image covers several dimensions, assign only the dimension for which it is strongest. The goal is not a moodboard of attractive images; it is a visual contract for one keyframe.
