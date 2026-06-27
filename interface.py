"""
TakeMeter — Post Classifier Inference UI
-----------------------------------------
Run this after fine-tuning in the TakeMeter notebook.
Requires the saved model at ./takemeter-model and the tokenizer.

Usage (in Colab, after Section 3):
    !pip install -q gradio
    %run takemeter_inference.py
"""

import numpy as np
import torch
import gradio as gr
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import os
for root, dirs, files in os.walk("./takemeter-model"):
    for f in files:
        print(os.path.join(root, f))
# ── Config ────────────────────────────────────────────────────────────────
MODEL_DIR = "./takemeter-model/checkpoint-144"  # match whatever number you see
MODEL_NAME  = "distilbert-base-uncased"   # used as tokenizer fallback
MAX_LENGTH  = 256

LABEL_MAP = {
    "discussion":     0,
    "news":           1,
    "misc":           2,
    "recommendation": 3,
}
ID_TO_LABEL = {v: k for k, v in LABEL_MAP.items()}

LABEL_META = {
    "discussion":     {"emoji": "💬", "color": "#4f86c6"},
    "news":           {"emoji": "📰", "color": "#e07b39"},
    "misc":           {"emoji": "📦", "color": "#7c6f9f"},
    "recommendation": {"emoji": "⭐", "color": "#4caf82"},
}

# ── Load model ────────────────────────────────────────────────────────────
print("Loading model...")
try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
except Exception:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

from transformers import DistilBertForSequenceClassification
model = DistilBertForSequenceClassification.from_pretrained(MODEL_DIR)
model.eval()
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
print(f"✅ Model loaded on {device}")


# ── Inference ─────────────────────────────────────────────────────────────
def classify(title: str, body: str, flair: str) -> tuple[str, dict]:
    """Run inference and return (label, confidence_dict)."""
    parts = []
    if flair.strip():
        parts.append(f"[{flair.strip()}]")
    parts.append(title.strip())
    if body.strip():
        parts.append(body.strip())
    text = " ".join(parts)

    if not text.strip():
        return "—", {}

    inputs = tokenizer(
        text,
        truncation=True,
        max_length=MAX_LENGTH,
        return_tensors="pt",
    ).to(device)

    with torch.no_grad():
        logits = model(**inputs).logits

    probs = torch.softmax(logits, dim=-1).squeeze().cpu().numpy()
    pred_id = int(np.argmax(probs))
    label   = ID_TO_LABEL[pred_id]

    confidence = {ID_TO_LABEL[i]: float(probs[i]) for i in range(len(probs))}
    return label, confidence


def run(title: str, body: str, flair: str):
    if not title.strip():
        return (
            gr.update(value="Enter a post title above.", visible=True),
            gr.update(visible=False),
            gr.update(value={}),
        )

    label, confidence = classify(title, body, flair)
    meta  = LABEL_META[label]
    pct   = confidence[label] * 100
    color = meta["color"]
    emoji = meta["emoji"]

    badge_html = f"""
    <div style="
        display:inline-flex; align-items:center; gap:10px;
        background:{color}18; border:2px solid {color};
        border-radius:10px; padding:14px 22px; margin-top:4px;
    ">
        <span style="font-size:2rem">{emoji}</span>
        <div>
            <div style="font-size:1.4rem; font-weight:700; color:{color}; letter-spacing:.02em">
                {label}
            </div>
            <div style="font-size:.9rem; color:#666; margin-top:2px">
                {pct:.1f}% confidence
            </div>
        </div>
    </div>
    """

    bar_html = "<div style='margin-top:8px'>"
    for lbl, prob in sorted(confidence.items(), key=lambda x: -x[1]):
        m   = LABEL_META[lbl]
        pct_bar = prob * 100
        bold = "font-weight:700;" if lbl == label else ""
        bar_html += f"""
        <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px">
            <span style="width:120px; font-size:.85rem; {bold} color:#333">{m['emoji']} {lbl}</span>
            <div style="flex:1; background:#eee; border-radius:4px; height:10px; overflow:hidden">
                <div style="width:{pct_bar:.1f}%; background:{m['color']}; height:100%; border-radius:4px"></div>
            </div>
            <span style="width:44px; text-align:right; font-size:.82rem; {bold} color:#555">
                {pct_bar:.1f}%
            </span>
        </div>"""
    bar_html += "</div>"

    return (
        gr.update(value=badge_html, visible=True),
        gr.update(value=bar_html,   visible=True),
        gr.update(value=confidence),
    )


# ── UI ────────────────────────────────────────────────────────────────────
css = """
#card { max-width: 680px; margin: 0 auto; }
#title-in textarea { font-size: 1rem !important; }
footer { display: none !important; }
"""

FLAIR_CHOICES = [
    "", "Discussion", "Episode", "Rewatch", "What to Watch?", "Help",
    "News", "Official Media", "Fanart", "Video", "Video Edit", "Clip",
    "Infographic", "Daily", "Weekly", "Announcement", "Misc.", "Essay",
    "Review", "Writing Club",
]

with gr.Blocks(css=css, title="TakeMeter Classifier") as demo:
    gr.Markdown(
        """
        # 🎌 TakeMeter — Post Classifier
        Paste an r/anime post to see how the fine-tuned model labels it.
        """,
        elem_id="card",
    )

    with gr.Column(elem_id="card"):
        flair_in = gr.Dropdown(
            choices=FLAIR_CHOICES,
            value="",
            label="Flair (optional but improves accuracy)",
            allow_custom_value=True,
        )
        title_in = gr.Textbox(
            label="Post title",
            placeholder="e.g. Does demon slayer get better?",
            lines=1,
            elem_id="title-in",
        )
        body_in = gr.Textbox(
            label="Post body (optional)",
            placeholder="Paste the post body here if you have it…",
            lines=4,
        )
        btn = gr.Button("Classify", variant="primary")

        gr.Markdown("### Result")
        badge_out = gr.HTML(visible=False)
        bars_out  = gr.HTML(visible=False)

        with gr.Accordion("Raw probabilities (JSON)", open=False):
            json_out = gr.JSON()

    btn.click(
        fn=run,
        inputs=[title_in, body_in, flair_in],
        outputs=[badge_out, bars_out, json_out],
    )
    title_in.submit(
        fn=run,
        inputs=[title_in, body_in, flair_in],
        outputs=[badge_out, bars_out, json_out],
    )

if __name__ == "__main__":
    demo.launch(share=True, debug=False)