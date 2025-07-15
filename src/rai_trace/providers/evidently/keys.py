from typing import Optional, Union
from ...validation import GenerativeMetricsValidator


class EvidentlyGenerativeMetrics(GenerativeMetricsValidator):
    ContextRelevance: Optional[Union[str, float, int]] = None
    BLEU: Optional[Union[str, float, int]] = None
    ROUGE: Optional[Union[str, float, int]] = None
    BERTScore: Optional[Union[str, float, int]] = None
    ExactMatch: Optional[Union[str, float, int]] = None
    MAP: Optional[Union[str, float, int]] = None
    NDCG: Optional[Union[str, float, int]] = None
    MRR: Optional[Union[str, float, int]] = None
    HitRate: Optional[Union[str, float, int]] = None
    FaithfulnessLLMEval: Optional[Union[str, float, int]] = None
    CorrectnessLLMEval: Optional[Union[str, float, int]] = None
    IsValidJSON: Optional[Union[str, float, int]] = None
    DeclineLLMEval: Optional[Union[str, float, int]] = None
    PIILLMEval: Optional[Union[str, float, int]] = None
    BiasLLMEval: Optional[Union[str, float, int]] = None
    ToxicityLLMEval: Optional[Union[str, float, int]] = None
    Sentiment: Optional[Union[str, float, int]] = None
    NegativityLLMEval: Optional[Union[str, float, int]] = None
    Diversity: Optional[Union[str, float, int]] = None
    Serendipity: Optional[Union[str, float, int]] = None
    ScoreDistribution: Optional[Union[str, float, int]] = None
    OOVWordsPercentage: Optional[Union[str, float, int]] = None
    PrecisionTopK: Optional[Union[str, float, int]] = None
    RecallTopK: Optional[Union[str, float, int]] = None
    FBetaTopK: Optional[Union[str, float, int]] = None
    RegExp: Optional[Union[str, float, int]] = None
    Contains: Optional[Union[str, float, int]] = None
    TextLength: Optional[Union[str, float, int]] = None
    Perplexity: Optional[Union[str, float, int]] = None  