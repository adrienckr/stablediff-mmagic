from mmagic.apis import MMagicInferencer
import torch
# torch.set_default_tensor_type(torch.float16)
sd_inferencer = MMagicInferencer(model_name='stable_diffusion')
text_prompts = 'oilpainting style, a new world with an icy landscape, fantastic creatures and a spacecraft in the sky, space, starts, science fiction, 8K, high quality, unreal engine 5, fantasy art, clean design, epic Instagram, artstation, splash of colorful paint, contour, hyperdetailed intricately detailed, unreal engine, a full moon in the night sky, Creepy, horror, Terrifying, Scary, fantastical, intricate detail, splash screen, complementary colors, fantasy concept art, 8k resolution, deviantart masterpiece, oil painting, paint drippin, smooth, sharp focus, trending on artforum, by Atey Ghailan, by Jeremy Mann, Greg Manchess, Anthonis Mor, Studio Ghibli, oil painting, heavy strokes, paint dripping'
result_out_dir = 'output/sd_res.png'
sd_inferencer.infer(text=text_prompts, result_out_dir=result_out_dir)
