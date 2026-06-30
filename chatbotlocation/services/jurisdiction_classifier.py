def classify_jurisdiction(resolved_name: str, tags: dict, admin_level: int) -> tuple[str, str]:
    """
    Phase 3: Classifies a resolved administrative boundary as a Gram Panchayat (rural)
    or Urban Local Body (ULB) and maps them to a specific body type.
    """
    name_lower = resolved_name.lower()
    ulb_keywords = ["nagar nigam", "municipal corporation", "nagar palika", "nagar panchayat", "ward", "urban"]
    
    # Check if any ULB keyword matches the name
    is_ulb = any(kw in name_lower for kw in ulb_keywords)
    
    # Check if any tag contains a ULB keyword
    for v in tags.values():
        if any(kw in str(v).lower() for kw in ulb_keywords):
            is_ulb = True
            break

    # Override: if admin_level is exactly 8 and there are no ULB keywords, classify as GP
    if admin_level == 8 and not is_ulb:
        is_ulb = False

    if is_ulb:
        # Determine specific Urban Local Body category
        body_type = "Municipal Corporation"  # default
        if "nagar nigam" in name_lower or "municipal corporation" in name_lower:
            body_type = "Municipal Corporation"
        elif "nagar palika" in name_lower or "municipal council" in name_lower:
            body_type = "Municipal Council"
        elif "nagar panchayat" in name_lower or "town panchayat" in name_lower:
            body_type = "Town Panchayat"
            
        body_name = resolved_name
    else:
        # Rural body classification
        body_type = "Gram Panchayat"
        # Standardize naming to prevent duplicate suffixes
        if not ("gram panchayat" in name_lower or "gp" in name_lower):
            body_name = f"{resolved_name} Gram Panchayat"
        else:
            body_name = resolved_name

    print(f"[Jurisdiction Classifier] Classified '{resolved_name}' -> body_type: '{body_type}', body_name: '{body_name}'")
    return body_type, body_name
