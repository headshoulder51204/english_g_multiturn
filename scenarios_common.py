"""Common data builder helpers for TalkieTown US scenarios."""

def make_opt(text: str, is_correct: bool, tip: str):
    return {"text": text, "isCorrect": is_correct, "tip": tip}

def make_turn(idx: int, name: str, avatar: str, npc_en: str, npc_kr: str,
              mission: str, target: str, reaction_en: str, reaction_kr: str,
              tip: str, correct_tip: str,
              wrong1_text: str, wrong1_tip: str,
              wrong2_text: str, wrong2_tip: str):
    return {
        "turnIndex": idx,
        "npcName": name,
        "npcAvatar": avatar,
        "npcEn": npc_en,
        "npcKr": npc_kr,
        "mission": mission,
        "target": target,
        "npcReactionEn": reaction_en,
        "npcReactionKr": reaction_kr,
        "culturalTip": tip,
        "options": [
            make_opt(target, True, correct_tip),
            make_opt(wrong1_text, False, wrong1_tip),
            make_opt(wrong2_text, False, wrong2_tip)
        ]
    }

def make_ep(ep_id: str, tier_id: str, title: str, ep_title: str, art_key: str, turns: list):
    return {
        "id": ep_id,
        "tierId": tier_id,
        "title": title,
        "episode": ep_title,
        "artKey": art_key,
        "turns": turns
    }
