from pathlib import Path
from uuid import uuid4

import torch
from diffusers import DiffusionPipeline

# Folder where generated images will be saved
OUTPUT_DIR = Path("app/static/generated")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load once, reuse for later requests
pipeline = None


def get_device() -> str:

    return "cuda" if torch.cuda.is_available() else "cpu"


def load_pipeline():

    global pipeline

    if pipeline is None:
        device = get_device()
        dtype = torch.float16 if device == "cuda" else torch.float32

        pipeline = DiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=dtype,
            use_safetensors=True
        )

        pipeline = pipeline.to(device)

    return pipeline


def generate_image(prompt: str) -> dict:
    # Generate multiple images from the prompt and save them locally.
    # Returns metadata including all generated image URLs.
    pipe = load_pipeline()

    enhanced_prompt = f"space theme, digital art, {prompt}"

    # Generate 3 images for one prompt
    result = pipe(
        enhanced_prompt,
        num_inference_steps=20,
        guidance_scale=7.5,
        num_images_per_prompt=3
    )  # type: ignore

    image_urls = []

    for image in result.images:
        filename = f"{uuid4().hex}.png"
        output_path = OUTPUT_DIR / filename
        image.save(output_path)
        image_urls.append(f"/static/generated/{filename}")

    return {
        "status": "success",
        "original_prompt": prompt,
        "enhanced_prompt": enhanced_prompt,
        "image_urls": image_urls
    }