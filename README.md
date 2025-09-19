# AutoGeTS: Knowledge-based Automated Generation of Text Synthetics for Improving Text Classification

**Authors**: Chenhao Xue, Raia Hadsell, Hugo Larochelle

---

## Abstract

When developing text classification models for real world applications, one major challenge is the difficulty to collect sufficient data for all text classes. In this work, we address this challenge by utilizing large language models (LLMs) to generate synthetic data and using such data to improve the performance of the models without waiting for more real data to be collected and labeled. As an LLM generates different synthetic data in response to different input examples, we formulate an automated workflow, which searches for input examples that lead to more ``effective'' synthetic data for improving the model concerned. We study three search strategies with an extensive set of experiments, and use experiment results to inform an ensemble algorithm that selects a search strategy according to the characteristics of a class. Our further experiments demonstrate that this ensemble approach is more effective than each individual strategy in our automated workflow for improving classification models using LLMs.

---

## Citation

If you find this work useful, please cite our paper:

```bibtex
@misc{xue2025autogets,
      title={AutoGeTS: Knowledge-based Automated Generation of Text Synthetics for Improving Text Classification}, 
      author={Chenhao Xue and Raia Hadsell and Hugo Larochelle},
      year={2025},
      eprint={2508.10000},
      archivePrefix={arXiv},
      url={[https://arxiv.org/abs/2508.10000](https://arxiv.org/abs/2508.10000)}
}
