from fastapi import APIRouter, HTTPException
from app.models.text_analysis import TextAnalysisRequest, TextAnalysisResponse
from app.services.analyzer import analyze_kyrgyz_readability, analyze_text

router = APIRouter()

@router.post("/analyze", response_model=TextAnalysisResponse)
def analyze(request: TextAnalysisRequest):
    if not request.text or not request.text.strip():
        raise HTTPException(status_code=400, detail="Text is required")

    ari_result = analyze_text(request.text)
    kyrgyz_result = analyze_kyrgyz_readability(request.text)

    if "error" in ari_result or "error" in kyrgyz_result:
        raise HTTPException(
            status_code=400,
            detail=ari_result.get("error") or kyrgyz_result.get("error"),
        )

    return TextAnalysisResponse(
        words_count=ari_result["words_count"],
        sentences_count=ari_result["sentences_count"],
        total_syllables=kyrgyz_result["total_syllables"],
        avg_syllables_per_word=kyrgyz_result["avg_syllables_per_word"],
        avg_words_per_sentence=kyrgyz_result["avg_words_per_sentence"],
        avg_characters_per_word=ari_result["avg_characters_per_word"],
        characters_count=ari_result["characters_count"],
        ari_score=ari_result["ari_score"],
        readability_score=kyrgyz_result["readability_score"]
    )
