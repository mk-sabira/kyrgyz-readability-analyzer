KYRGYZ_VOWELS = set("аоуыэиеөүёюя")

def count_syllables_in_word(word: str) -> int:

    word = word.lower()
    syllable_count = 0
    previous_was_vowel = False

    for char in word:
        is_vowel = char in KYRGYZ_VOWELS
        
        if is_vowel and not previous_was_vowel:
            syllable_count += 1
        previous_was_vowel = is_vowel

    return syllable_count