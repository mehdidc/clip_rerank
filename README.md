# clip_rerank

Simple script to re-rank images using OpenAI's CLIP https://github.com/openai/CLIP.

## How to install ?

1. First you need to install clip <https://github.com/openai/CLIP>
2. `pip install clize`

## How to use ?

Here is an example:

`clip_rerank "<FOLDER>/*.jpg" --text="a bird with yellow and cream belly , the bill is short and pointed , with a small head compared to its body" --target_folder=target`
  

What will this do?

this will look for all jpg images in `<FOLDER>`, apply CLIP similary with the provided text, then rank the images, then save the ranked
images into the target folder. Filenames on target folder will start from 0, which will be the image with highest CLIP score. 
