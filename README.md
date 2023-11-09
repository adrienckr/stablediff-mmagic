
# 🚀 Text-to-Image Generation using MMagic's Stable Diffusion Model 🖼️

This Python script demonstrates how to use the MMagic API to generate stunning images from text prompts using the powerful Stable Diffusion model. Simply provide a text prompt, and the script will create an image that brings your ideas to life! 🌟

## Clone this repository
```bash
git clone https://github.com/adrienckr/stablediff-mmagic.git
```
## Prerequisites 🛠️

Before you get started, make sure you have the following dependencies installed:

- Python 3.8 (or a compatible version) 🐍
- Miniconda ⚙️

## Installation Steps 📦

Follow these simple steps to set up your environment for using the MMagic Stable Diffusion model:

1. **Install [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html) on your system if you haven't already.**

2. **Create a Conda environment and activate it using the following commands:**

   ```bash
   conda create --name mmagic python=3.8 -y
   conda activate mmagic
   ```

3. **Check your CUDA version by running the command:**

   ```bash
   nvcc --version
   ```

4. **Install PyTorch by referring to the [official PyTorch documentation](https://pytorch.org/). Select the appropriate configuration based on your system and follow the installation instructions.**

   ![PyTorch Installation](https://prod-files-secure.s3.us-west-2.amazonaws.com/16414159-cf5e-4dee-a624-4cdc703e880e/0c523fad-82b5-442b-b9d1-f72409bf9fb4/Untitled.png)

5. **Install the `MMCV` library using `MIM`, a package manager for AI and machine learning dependencies. Run the following commands:**

   ```bash
   pip install -U openmim
   mim install 'mmcv>=2.0.0'
   ```

6. **Install `mmengine` from the GitHub repository:**

   ```bash
   pip install git+https://github.com/open-mmlab/mmengine.git
   ```

7. **Install the `mmagic` toolbox in editable mode using the following command:**

   ```bash
   git clone https://github.com/open-mmlab/mmagic.git
   cd mmagic
   pip3 install -e . -v
   ```

   The `-e .` flag is used to install the Python package in editable mode, meaning that any changes made to the source code will be reflected in the installed package.

8. **Additionally, install `accelerate` for faster and less memory-intensive model loading:**

   ```bash
   pip install accelerate
   ```

9. **Run the script:**

   ```bash
   python app.py
   ```

10. **You will be prompted to enter your text prompt. Type your desired prompt and press Enter.**

11. **The script will generate an image based on your text prompt and save it to the `output` directory as `sd_res.png`. 🖼️

Now you're ready to create amazing images from your text prompts with MMagic's Stable Diffusion model! 🎨✨
