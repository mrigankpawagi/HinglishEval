# HinglishEval
Are our Large Language Models good at code-generation when prompted in native languages?

## Prompting in Hinglish
We used GPT-4 to translate prompts in HumanEval to _Hinglish_ and manually verified and fixed these translations. Our benchmark, __HinglishEval__ is available as a JSON file (`HinglishEval.json`) in this repository.

### Why Hinglish?
Hindi is one of the most widely spoken languages in the world, and the most widely spoen in India. A majority of the population in India does not speak English as their first language, and therefore language models that can understand prompts in native languages are important for wider accessibility. Hinglish is a blend of Hindi and English, with frequent usage of English words in sentences with standard Hindi grammar. This is not representative of everyday spoken Hindi for most people, but is rather common in coversations involving technical language, especially in the context of programming.

Therefore it is most natural for Hindi speaking users to prompt LLMs in Hinglish when they want to generate code, or ask for help with programming in general (like explanations or debugging). This benchmark is an attempt to understand how well LLMs can understand and generate code when prompted in such a language.

## Results
We evaluated 18 models on the HinglishEval dataset, at temperature 0 (greedy decoding).

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

### The HinglishEval Benchmark
The HinglishEval benchmark contains all the problems in the HumanEval benchmark, with their prompts translated to Hinglish. The translation does not modify function signatures or doctests, and is limited to the purpose statement (supplied as a __docstring__ in Python) of each function. The translations were manually verified and corrected to ensure that they sound like spoken Hinglish.

### Code Samples for 18 models
We have publicly released completions generated from 18 models on the prompts in the HinglishEval benchmark. These completions are available in the `samples/unsanitized` directory. Sanitized versions of these completions are also available in the `samples/sanitized` directory. Sanitization involves clipping the completions to only include function that was asked for, and removing any extraneous text.

### Evaluation of 18 models on HinglishEval
We evaluated 18 models on the HinglishEval dataset and reported the results in the table above. We report only the Pass@1 metric since the models were evaluated at temperature 0 (greedy decoding). 

## Future Work
We encourage the community to
1. Interpret the results of this evaluation
2. Explore different prompting strategies to improve the performance of models on HinglishEval
3. Evaluate more models and with different temperature settings, particularly models for native languages
4. Extend the benchmark to more native languages
