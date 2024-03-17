# HinglishEval
Are our Large Language Models good at code-generation when prompted in native languages?

## Prompting in Hinglish
We used GPT-4 to translate prompts in HumanEval to _Hinglish_ and manually verified and fixed these translations. The new dataset, __HinglishEval__ is available as a JSON file (`HinglishEval.json`) in the repository.

## Results
We evaluated 18 models on the HinglishEval dataset, at temperatures 0 (greedy decoding).

| Model | Pass@1 | 
| --- | --- |
| GPT 4 | 79.27 |
| GPT 3.5 Turbo | 58.54 |
| Gemma 7B | 31.71 |
| Gemma 2B | 17.68 |
| Codegen 6B Mono | 15.24 |
| Codegen 2B Mono | 9.76 |
| Codegen 6B Multi | 8.54 |
| Santacoder | 6.71 |
| Codegen-2 1B | 4.88 |
| Codegen 6B NL | 3.66 |
| Codegen 350M Mono | 3.05 |
| Codegen 350M Multi | 3.05 |
| Codegen 2B NL | 2.44 |
| Polycoder 2.7B | 1.83 |
| Codegen 2B Multi | 1.83 |
| Polycoder 0.4B | 0.00 |
| Polycoder 160M | 0.00 |
| Codegen 350M NL | 0.00 |

## Contributions and Usage
1. Translated HumanEval to Hinglish
2. Released Code Samples for 18 models
3. Evaluated 18 models on HinglishEval

## Future Work
