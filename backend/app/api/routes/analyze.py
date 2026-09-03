from fastapi import APIRouter
from app.models.text_analysis import TextAnalysisRequest, TextAnalysisResponse
from app.services.analyzer import analyze_kyrgyz_readability, analyze_text

router = APIRouter()

@router.post("/analyze", response_model=TextAnalysisResponse)
def analyze(request: TextAnalysisRequest):
    ari_result = analyze_text(request.text)
    kyrgyz_result = analyze_kyrgyz_readability(request.text)

    return TextAnalysisResponse(
        word_count=ari_result["word_count"],
        sentences_count=ari_result["sentences_count"],
        total_syllables=kyrgyz_result["total_syllables"],
        avg_syllables_per_word=kyrgyz_result["avg_syllables_per_word"],
        avg_words_per_sentence=kyrgyz_result["avg_words_per_sentence"],
        avg_characters_per_word=ari_result["avg_characters_per_word"],
        characters_count=ari_result["characters_count"],
        ari_score=ari_result["ari_score"],
        readability_score=kyrgyz_result["readability_score"]
    )
