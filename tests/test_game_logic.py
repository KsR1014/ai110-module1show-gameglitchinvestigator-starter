from logic_utils import check_guess, parse_guess


# --- Bug 1: hints were backwards ---
# A guess ABOVE the secret should tell the player to go LOWER,
# and a guess BELOW the secret should tell them to go HIGHER.

def test_too_high_hint_says_go_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()
    assert "HIGHER" not in message.upper()

def test_too_low_hint_says_go_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()


# --- Bug 4: out-of-range guesses must be rejected ---
# parse_guess(raw, low, high) should reject anything outside [low, high]
# without producing a valid guess.

def test_guess_below_range_is_rejected():
    ok, value, err = parse_guess("-1", 1, 100)
    assert ok is False
    assert value is None
    assert err is not None

def test_guess_above_range_is_rejected():
    ok, value, err = parse_guess("101", 1, 100)
    assert ok is False
    assert value is None
    assert err is not None

def test_guess_in_range_is_accepted():
    ok, value, err = parse_guess("50", 1, 100)
    assert ok is True
    assert value == 50
    assert err is None

def test_range_boundaries_are_inclusive():
    assert parse_guess("1", 1, 100)[0] is True
    assert parse_guess("100", 1, 100)[0] is True

# Also fixed the 3 pre-existing tests

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"
