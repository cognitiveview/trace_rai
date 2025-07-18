from typing import Optional, Union
from ...validation import GenerativeMetricsValidator


class DeepEvalGenerativeMetrics(GenerativeMetricsValidator):
    AnswerRelevancyMetric: Optional[Union[str, float, int]] = None
    ContextualPrecisionMetric: Optional[Union[str, float, int]] = None
    ContextualRecallMetric: Optional[Union[str, float, int]] = None
    ContextualRelevancyMetric: Optional[Union[str, float, int]] = None
    ConversationCompletenessMetric: Optional[Union[str, float, int]] = None
    ConversationRelevancyMetric: Optional[Union[str, float, int]] = None
    ConversationalGEval: Optional[Union[str, float, int]] = None 
    FaithfulnessMetric: Optional[Union[str, float, int]] = None
    KnowledgeRetentionMetric: Optional[Union[str, float, int]] = None
    RoleAdherenceMetric: Optional[Union[str, float, int]] = None
    TaskCompletionMetric: Optional[Union[str, float, int]] = None
    ToolCorrectnessMetric: Optional[Union[str, float, int]] = None
    BiasMetric: Optional[Union[str, float, int]] = None
    ToxicityMetric: Optional[Union[str, float, int]] = None
    SummarizationMetric: Optional[Union[str, float, int]] = None
    PromptAlignmentMetric: Optional[Union[str, float, int]] = None
    JsonCorrectnessMetric: Optional[Union[str, float, int]] = None
    HallucinationMetric: Optional[Union[str, float, int]] = None
    RAGASAnswerRelevancyMetric: Optional[Union[str, float, int]] = None
    RAGASFaithfulnessMetric: Optional[Union[str, float, int]] = None
    RAGASContextualPrecisionMetric: Optional[Union[str, float, int]] = None
    RAGASContextualRecallMetric: Optional[Union[str, float, int]] = None