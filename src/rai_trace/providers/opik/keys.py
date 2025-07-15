from typing import Optional, Union
from ...validation import GenerativeMetricsValidator


class OpikGenerativeMetrics(GenerativeMetricsValidator):
    Equals: Optional[Union[str, float, int]] = None
    Contains: Optional[Union[str, float, int]] = None
    RegexMatch: Optional[Union[str, float, int]] = None
    IsJson: Optional[Union[str, float, int]] = None
    # LevenshteinRatio: Optional[Union[str, float, int]] = None
    SentenceBLEU: Optional[Union[str, float, int]] = None
    CorpusBLEU: Optional[Union[str, float, int]] = None
    ROUGE: Optional[Union[str, float, int]] = None
    Sentiment: Optional[Union[str, float, int]] = None
    Moderation: Optional[Union[str, float, int]] = None
    Usefulness: Optional[Union[str, float, int]] = None
    AnswerRelevance: Optional[Union[str, float, int]] = None
    ContextPrecision: Optional[Union[str, float, int]] = None
    ContextRecall: Optional[Union[str, float, int]] = None