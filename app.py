from mmagic.apis import MMagicInferencer
import torch
# torch.set_default_tensor_type(torch.float16)

sd_inferencer = MMagicInferencer(model_name='stable_diffusion')

text_prompts = input("Enter your prompt: ")
result_out_dir = 'output/sd_res.png'
sd_inferencer.infer(text=text_prompts, result_out_dir=result_out_dir)
