# SpaceView Studio

SpaceView Studio is a FastAPI-based generative AI project that creates space-themed artwork from text prompts using a diffusion model.

# Features

- Generate AI images from text prompts
- Space-themed prompt presets
- Multiple images per prompt
- Simple and clean web interface
- FastAPI backend
- Docker support

# Tech Stack

- Python
- FastAPI
- Jinja2
- Hugging Face Diffusers
- PyTorch
- Pillow
- Docker

# Project Structure

spaceview-studio/
├── app/
│   ├── __init__.py
│   ├── generator.py
│   ├── main.py
│   ├── static/
│   │   └── generated/
│   └── templates/
│       └── index.html
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt