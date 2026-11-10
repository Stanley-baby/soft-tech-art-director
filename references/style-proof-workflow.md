# Style Proof Workflow

Use this after original references and a Reference Contract are confirmed. A Style Proof is one static, product-specific keyframe that converts several external references into a new visual anchor before interactive implementation. Use progressive delivery so the user receives the visual system before waiting for the preview.

## Phase A · Immediate direction pack

Before invoking image generation, send a useful intermediate deliverable:

1. Case Board for human review.
2. Reference Contract with Primary, Supporting, and Constraint roles.
3. Concise Visual Rules for core visual, page structure, color, typography, surface, data expression, and motion.
4. Draft Implementation Tokens for color, typography, spacing, radius, border, surface, light, and motion.

Every rule and token must cite `PRODUCT` or a confirmed `REF-ID`. Label the token set `Draft · pending preview calibration`. Keep it concise enough to scan while the preview is being generated.

Then send one plain-language progress line:

> 视觉规则与 Draft Tokens 已整理好；我正在结合这些独立参考图生成预览关键帧。

Do not expose tool calls, elapsed-time speculation, package checks, or image-generation diagnostics.

## Input hierarchy

Apply inputs in this order:

1. Product Invariants: audience, AI behavior, page job, required content, accessibility, existing locked brand constraints.
2. Primary References: one or two original images controlling the dominant composition or hero visual.
3. Supporting References: original images controlling color, type, material, or data expression.
4. Constraint References or notes: boundaries and patterns not to inherit.

Do not pass a long Style Profile or the merged Case Board. Draft rules may be passed only when they preserve confirmed structure, accessibility, or brand constraints. Let the original references control visual nuance; do not force speculative decorative token values into the prompt.

## Phase B · Generate

- Use the image-generation workflow when available and classify the asset as `ui-mockup`.
- Include every selected original image separately. Label each image role explicitly.
- Generate one polished keyframe for the inferred Frame Goal.
- Preserve exact required product copy only when necessary; otherwise keep text minimal because the keyframe validates visual direction, not final content accuracy.
- Keep exclusions concise and internal. Do not show a standalone Negative Prompt to the user.
- If image generation is unavailable, output the same structured spec and list the original files the user must attach separately.

## Phase C · Preview delivery and review

When the keyframe is ready, lead with the preview. Then briefly state:

- which reference role is most visible;
- what changed from the Draft Direction Pack;
- which Draft Tokens remain stable and which require calibration.

Inspect the result against:

- Product meaning
- Primary-reference composition or hero form
- Supporting-reference color and typography
- Generic-template leakage
- Usability and implementability

Treat two or more role scores below 3/5 as a failed proof. Change the reference set, hierarchy, or generation route before adding adjectives.

Ask one user decision:

- `确认风格`: approve this Style Proof.
- `调整关键帧`: make one targeted visual change.
- `更换参考图`: return to the Reference Contract.

Use this visible prompt immediately after the preview and brief calibration note:

> 这张预览可以作为你的 Style Proof 吗？
>
> `确认风格` · `调整关键帧` · `更换参考图`

Never stop at the image and never treat `继续` alone as proof approval.

Iterate with one change at a time.

## Phase D · Reconcile the final system

Only after approval, reconcile the Draft Visual Rules and Tokens into the Final Style Profile and Tokens from:

- `PRODUCT`
- confirmed `REF-ID`s
- approved `STYLE-PROOF`

Separate locked existing tokens from newly derived tokens. Do not rewrite values that already align; change only conflicts revealed by the approved proof. The approved proof plus final tokens become the source of truth for implementation.

## Phase E · Final delivery and What's Next

Do not end with a visible Negative Prompt or QA Checklist. Keep both as internal guardrails. Offer at most three context-relevant next steps:

- Refine or extend the keyframe with image generation
- Turn the keyframe into HTML, then move it into Figma for precise editing
- Start building an interactive demo or product
- Extend into more screens or a design system
- Save confirmed and rejected references, proof, and tokens into a personal moodboard or visual library

Frame these choices with a concise encouraging close:

> 我们已经一起走完了一次专业的风格定义流程：从产品表达、视觉坐标、参考分工，到关键帧验证和实现规则。你现在掌握的不是一组流行效果，而是一套判断风格的方法。
>
> 好的审美很少一次命中。高级且独特的视觉方向，通常来自长期积累、反复比较、尝试与偶然发现——这也是专业设计师真实的工作过程。接下来，你可以通过以下方式继续把它变得更好：

Adapt the wording to the user and follow it with no more than three concrete next steps. Do not overclaim that one journey makes the user a professional designer.
