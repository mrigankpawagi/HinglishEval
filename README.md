# HinglishEval
Artifact for **HinglishEval: Evaluating the Effectiveness of Code-generation Models on Hinglish Prompts**.

## Prompting in Hinglish
We used GPT-4 to translate prompts in OpenAI's [HumanEval Benchmark](https://github.com/openai/human-eval) to _Hinglish_ and manually verified and fixed these translations. Our benchmark, __HinglishEval__ is available as a JSON file (`HinglishEval.json`) in this repository.

### Why Hinglish?
Hindi is one of the most widely spoken languages in the world, and the most widely spoen in India. A majority of the population in India does not speak English as their first language, and therefore language models that can understand prompts in native languages are important for wider accessibility. Hinglish is a blend of Hindi and English, with frequent usage of English words in sentences with standard Hindi grammar. This is not representative of everyday spoken Hindi for most people, but is rather common in coversations involving technical language, especially in the context of programming.

Therefore it is most natural for Hindi speaking users to prompt LLMs in Hinglish when they want to generate code, or ask for help with programming in general (like explanations or debugging). This benchmark is an attempt to understand how well LLMs can understand and generate code when prompted in such a language.

## Contributions and Usage

### The HinglishEval Benchmark
The HinglishEval benchmark contains all the problems in the HumanEval benchmark, with their prompts translated to Hinglish. The translation does not modify function signatures or doctests, and is limited to the purpose statement (supplied as a __docstring__ in Python) of each function. The translations were manually verified and corrected to ensure that they sound like idiomatic Hinglish.

### Code Samples for 18 models
We have publicly released completions generated from 18 models on the prompts in the HinglishEval benchmark. 
<!-- These completions are available in the `samples/unsanitized` directory. Sanitized versions of these completions are also available in the `samples/sanitized` directory. Sanitization involves clipping the completions to only include function that was asked for, and removing any extraneous text. -->

### Evaluation of models on HinglishEval <!-- add number of models -->
<!-- We evaluated 18 models on the HinglishEval dataset and reported the results in the table above. We report only the Pass@1 metric since the models were evaluated at temperature 0 (greedy decoding). -->
We evaluate models on the HinglishEval dataset using the pass@1 metric as well as Item Response Theory (IRT).
