from pydantic import BaseModel, field_validator
from typing import Union
from enum import Enum

class GenerativeMetricsValidator(BaseModel):
    @field_validator("*", mode='before')
    @classmethod
    def check_value_under_100(cls, v):
        numeric_value = None
        if isinstance(v, (int, float)):
            numeric_value = v
        elif isinstance(v, str):
            try:
                # Try to convert string to a float for comparison
                numeric_value = float(v)
            except ValueError:
                # If conversion fails, it's a non-numeric string like "N/A", raise an error.
                if v == "":
                    pass
                else:
                    raise ValueError(f"value '{v}' must be a valid number")
        
        if numeric_value is not None and numeric_value > 100:
            raise ValueError("value must be less than or equal to 100")
        
        return v

class UseCaseEnum(str, Enum):
    TRANSPORTATION = "transportation"
    FINANCIAL_SERVICES = "financial_services"
    HEALTHCARE_DIAGNOSTICS = "healthcare_diagnostics"
    CUSTOMER_SUPPORT = "customer_support"
    SPEECH_RECOGNITION_SYSTEMS = "speech_recognition_systems"
    INDUSTRIAL_AUTOMATION = "industrial_automation"
    MARKETING_AND_ADVERTISING = "marketing_and_advertising"
    ECOMMERCE_AND_RETAIL = "ecommerce_and_retail"
    LEGAL_DOCUMENT_REVIEW = "legal_document_review"
    AGRICULTURE = "agriculture"
    ENERGY_MANAGEMENT_AND_UTILITIES = "energy_management_and_utilities"
    SUPPLY_CHAIN_OPTIMIZATION = "supply_chain_optimization"
    FRAUD_DETECTION_IN_FINANCE_AND_SECURITY = "fraud_detection_in_finance_and_security"
    CYBERSECURITY_AND_THREAT_DETECTION = "cybersecurity_and_threat_detection"
    URBAN_PLANNING_AND_SMART_INFRASTRUCTURE = "urban_planning_and_smart_infrastructure"
    DRUG_DISCOVERY = "drug_discovery"
    EDUCATION_AND_EDTECH = "education_and_edtech"
    RETAIL_PRICING_OPTIMIZATION = "retail_pricing_optimization"
    ENVIRONMENTAL_MONITORING = "environmental_monitoring"
    MENTAL_HEALTH_SUPPORT = "mental_health_support"
    AUTONOMOUS_DRONES = "autonomous_drones"
    FAKE_NEWS_DETECTION_IN_MEDIA_AND_JOURNALISM = "fake_news_detection_in_media_and_journalism"
    INSURANCE_CLAIMS_PROCESSING = "insurance_claims_processing"
    LAW_ENFORCEMENT_AND_PUBLIC_SAFETY = "law_enforcement_and_public_safety"
    BIOMETRICS_SYSTEM = "biometrics_system"
    IMAGE_GENERATION = "image_generation"
    ROBOTICS = "robotics"
    OTHERS = "others"