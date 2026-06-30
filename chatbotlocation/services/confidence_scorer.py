from rapidfuzz import fuzz
from typing import Optional


def score_confidence(
    method: str,
    resolved_boundary_name: str,
    reverse_village_name: str,
    importance: float,
    venue_resolved: bool = True,
    locality_used: Optional[str] = None,
) -> tuple[float, str, str]:
    """
    Phase 4: Calculates composite confidence score and maps to a warning message.

    When venue_resolved is False (venue could not be geocoded, only the locality
    was resolved), the base score is capped at 0.65 regardless of extraction method,
    and a note is appended to the warning.
    """
    # 1. Base Score depending on method of spatial boundary extraction
    if method == "enclosing":
        base_score = 0.80
    elif method == "nearby":
        base_score = 0.50
    else:  # reverse_geocode
        base_score = 0.30

    # Override base score when venue was not resolved
    if not venue_resolved:
        base_score = 0.65
        print(f"[Confidence Scorer] venue_resolved=False — base score overridden to 0.65")

    score = base_score
    print(f"[Confidence Scorer] Method: '{method}' | Base Score: {base_score}")

    # 2. Modifier: agreement bonus (+0.15) if reverse village name matches resolved Overpass name
    if resolved_boundary_name and reverse_village_name:
        # Strip common organizational suffixes to fuzzy compare the core geographic names
        def clean_for_fuzzy(name: str) -> str:
            name_lower = name.lower()
            suffixes = [
                "gram panchayat", "gp", 
                "nagar nigam", "municipal corporation", 
                "nagar palika parishad", "nagar palika", "municipal council",
                "nagar panchayat", "town panchayat"
            ]
            for suffix in suffixes:
                name_lower = name_lower.replace(suffix, "")
            return name_lower.strip()
            
        cleaned_boundary = clean_for_fuzzy(resolved_boundary_name)
        cleaned_village = clean_for_fuzzy(reverse_village_name)
        
        fuzzy_score = fuzz.token_sort_ratio(cleaned_boundary, cleaned_village)
        print(f"[Confidence Scorer] Fuzzy match core name: '{cleaned_boundary}' vs '{cleaned_village}' -> Score: {fuzzy_score}")
        
        if fuzzy_score >= 85:
            score += 0.15
            print("[Confidence Scorer] Added +0.15 agreement bonus.")

    # 3. Modifier: additive from Nominatim importance score normalized to [0, 0.05]
    importance_val = float(importance or 0.0)
    importance_val = max(0.0, min(1.0, importance_val))
    importance_boost = importance_val * 0.05
    score += importance_boost
    print(f"[Confidence Scorer] Added importance boost: {importance_boost} (raw importance: {importance_val})")

    # 4. Clip final score to [0.0, 1.0] range and round
    score = max(0.0, min(1.0, score))
    score = round(score, 2)

    # 5. Determine level and warnings based on thresholds
    # >= 0.70 -> "high"
    # 0.40 - 0.69 -> "medium"
    # < 0.40 -> "low"
    if score >= 0.70:
        level = "high"
        warning = None
    elif score >= 0.40:
        level = "medium"
        warning = "Nearby boundary match used. Please verify jurisdiction locally."
    else:
        level = "low"
        warning = "Low geocoding precision. Verify exact jurisdiction before submitting documents."

    # Append venue-not-resolved note when applicable
    if not venue_resolved:
        venue_note = f"Exact venue could not be pinpointed; jurisdiction resolved from {locality_used or 'locality'}."
        if warning:
            warning = f"{warning} {venue_note}"
        else:
            warning = venue_note

    print(f"[Confidence Scorer] Final Confidence Score: {score} | Level: {level}")
    return score, level, warning
