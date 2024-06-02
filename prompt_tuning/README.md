# Prompt tuning-

## Further Experimentation
Further experimentation with the models used for HinglishEval. It is an extension to see if any new prompting techniques can help improve the performance of the models in understanding prompts in native languages. 

## Dataset:
For the initial test we have used translated docstrings from the HumanEval database for basic programming problems. Now we choose a subset of them to further test various strategies intended to improve the performance of certain poor performing models. 

The refining of the problems has been done based on how we feel the kind of problems (the way they are stated) affects the performance. They are not to be chosen to only aid performance but to give us a clear view on how particular prompting strategies affect the performances of certain types of questions and models.

## Prompting strategies:
Drawing inspiration from some of the other research works being done in the same domain such as this [Study on Solving Multilingual Tasks with Large Language Models](https://arxiv.org/pdf/2403.10258), we construct and use a few of the prompting strategies mentioned in this.

Our original work was based on the aforementioned - ***Basic prompt with native instructions (NATIVEBASIC)***

We would now be adding on to that to implement two further strategies described:
- English chain-of-thought (EN-COT) We pose the question in the native language but instruct the model to reason in English with the instruction *"Let’s think step by step in English"*.
- Cross-lingual-thought (XLT) XLT (Huang et al., 2023) is a state-of-the-art prompting method to handle multilingual NLP tasks. It prompts LLMs to translate the question into English and solve the problem step-by-step in English, leveraging the English-centric bias of LLMs.
- Paraphrasing the prompt is a technique in which we modify the prompt without changing the actual meaning and context of the problem and provide it to the model and test if it can solve the problem better.

We design our own versions of this technique and implement that to monitor the behaviour of the performance of the models under these strategies.
## Technique 1:

**Chain of Thought** - This will be a strategy in which we breakdown the prompt into more than one sub-prompts and use the strategy of [few shot prompting](https://www.kdnuggets.com/2023/07/ensuring-reliable-fewshot-prompt-selection-llms.html). We feed these prompts step by step to the model by specifying the intent initially to the model that it would be a step-wise prompt and ask it to interpret it in the same way.
This can only be done for models that can store the history of their prompts and answers. 
We shall automate the process of breaking down a prompt into sub-prompts by using a primary model such as GPT-4 and then manually verify the same after the results have been produced.
To be tested on models on more than one temperature range.

## Technique 2:
**Cross Lingual Thought** - This will be a strategy to provide the model with the Hinglish prompt and then ask itself to first translate the prompt back to the native English language in which it is more comfortable and the provide that to the model to get the final solution.
This can use the same initial dataset and can be tried on more number of models and maybe on more than a single temperature as well.


## Technique 3:
**Paraphrasing prompts** - In this strategy we use an external API / another primary model such as GPT-4 to paraphrase the initial prompt. We then provide this new paraphrased prompt to the models and test their performance.
We can manually handle the verification of the paraphrased prompts and even have more than one version for a single problem. Again this strategy can be tested on more than one temperatures of the model.