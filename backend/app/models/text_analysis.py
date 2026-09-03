from pydantic import BaseModel


class TextAnalysisRequest(BaseModel):
    text: str


class TextAnalysisResponse(BaseModel):
    words_count: int
    sentences_count: int
    total_syllables: int
    avg_syllables_per_word: float
    avg_words_per_sentence: float
    avg_characters_per_word: float
    characters_count: int
    ari_score: float
    readability_score: float